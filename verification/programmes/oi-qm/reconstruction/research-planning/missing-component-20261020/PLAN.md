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
  - Three notions are kept apart:
    - Heralded: the tests give an exact Z on a heralded branch. An X-test on |0⟩ yields |−⟩ with probability 1/2, then
      kickback.
    - Almost surely terminating: repeating until success terminates with probability 1 and defines Ad Z exactly, but
      only as the limit of the finite-depth channels Φ_n = (1 − 2^−n) Ad Z + 2^−n id.
    - Finite protocols: finite `InstAvail` protocols built from primitives satisfying `OnesNormal` (generic unsharp
      Lüders instruments included) yield no deterministic ray-moving unitary channel and no deterministic |−⟩.
  - Every Φ_n is `OnesNormal` and Ad Z is not, so `OnesNormal` is not closed under channel limits. The cost is exactly
    2^n Kraus operators at depth n. Entrywise nonnegativity of unitary conjugations is limit-closed
    (`preservesNonneg_of_approx`), and Φ_n already violates nonnegativity from n = 2. Only non-native tests make Φ_n
    available at all.
  - The A1 endpoint requires the deterministic Ad Z channel. Admitting almost-surely terminating protocols would be a
    restricted limit-closure rule, which the adopted gates do not admit without a separate owner ruling. Whether TU
    meets the existing A2 endpoint (`KrausDense`, `DenseFiniteQM`) is open.
  - The continuum of measurement bases that makes the layer flow exact is itself unsourced: OI's readout is
    configuration readout, and the bases are posited.
  - Adding the deterministic Ad Z channel to these tests gives full control on qubit registers. This is shown for Z
    only, and the register step rests on Barenco et al. [L] and a written argument [W].
  - O-B is not sourced and stays open.
  - The F2 ledger's monomial-lemma wording (LEDGER.md §5 item 2) is corrected to this scope.

- **`mc-node2/`, dense availability and operational completion as a candidate: NEW, narrow, [W].**
  - Sharp Lüders tests in three fixed non-configuration bases (X, Y and one real basis), with the native class, meet
    the A2 endpoint `DenseFiniteQM` = `KrausSoundExt ∧ KrausDense` (DiscreteCompletion.lean:59). Every finite Kraus
    instrument is approximated outcome by outcome, without `DenseUnitaryControl` and without `DerivedOI`. This is the
    converse of the kernel's own sufficiency route (DenseInstrumentBridge.lean:437). It is a written argument with
    exact and numerical instances at level one; soundness and theory-hood of the extended theory are [W].
  - So the phase gap and the continuum of test bases are both A1-only. At A2, G4's uniform-ray clause is not
    necessary: every one-outcome unitary of this dense theory fixes the uniform ray.
  - Heralded branches count as outcomes of an available family; renormalized postselected branches do not.
  - Completion rules of word type (almost-sure termination, stopping-time rules, countable mixtures, postselection
    that does not depend on the input state) keep `countable_not_pairFlowSourced` and `fixedGateTheory_not_qm`: they
    can supply the phase but not
    the continuum. Topological closure, convergent infinite compositions and basis-set closure erase the fixed-gate
    control: they are the dense endpoint relabelled. Shown for the eight listed forms only.
  - Almost-sure termination exceeds any fixed finite representative, as every A1-exact continuum does.
  - No OI posit or derivation found supplies the test bases, operational completion or O-B. Purification with
    uniqueness would cover all three, but only as a posit. G6 stays open.

- **`mc-node3/`, classical enlargement and the observer's choice of test: ELABORATING, one NEW (narrow) item, [W].**
  - Cone lemma: in the pointwise hidden model, with κ1 read as mixed priors, κ2 (processes are configuration
    bijections), κ3 (the G3 identification), κ4 (configuration readouts with feed-forward) and measurable dynamics,
    every available outcome map lies in the finitely generated, closed cone of nonnegative combinations of Ad_P, P a
    0/1 partial permutation. This holds at any substratum cardinality, in discrete or continuous time, with any real
    couplings and with observer settings of any origin. So `NonnegBounded` and `OnesNormal` hold, effects and reachable
    states are diagonal, and level-one conjugations lie in six rays: no (a), (b) or (c), and limits or almost-sure
    termination do not escape.
  - The new item: the classical-enlargement escape in the countable-realization conclusion is empty. Enlarging a
    classical substratum's size or time model adds nothing.
  - A coherent (Koopman–von Neumann) reading of the hidden prior leaves the cone, though not `NonnegBounded`, so the
    mixed reading of κ1 is load-bearing.
  - Each dropped κ leaves the cone, but none reaches A1 on its own, and for non-classical candidates the
    countable-realization premises remain load-bearing (`fixedGateTheory_not_qm`).
  - The global antiunitary gives no deterministic phase. The reconstruction principles each need a non-classical
    primitive. G6: none.

**Form the missing component must take under A1, as the reviewed nodes have narrowed it:**
- It contains a primitive of non-classical kind (κ1 read as mixed priors, κ2, or κ4 dropped; κ3 is barred by G3), and,
  for (a) at A1, it is non-supervenient or rests on an infinite substratum of non-classical kind. Enlarging a classical
  substratum's cardinality or time model adds nothing (`mc-node3`).
- It includes a primitive outside `OnesNormal`, such as a phase-type isometry or a deterministic preparation of |−⟩, or
  else a rule admitting almost-surely terminating protocols. This is needed for a deterministic phase at A1 exactness;
  heralded phase branches need neither.
- It includes an uncountable non-monomial family, for which a continuum of Lüders test bases suffices.
- It includes the G3 identification and multi-token compatibility clauses, for O-B.
- An independent prediction (G6) is still open.
