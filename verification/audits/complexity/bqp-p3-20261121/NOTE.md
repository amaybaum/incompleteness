# BQP-P3: research proposal and paper analysis for Q1–Q3

**Status: WIP / UNVERIFIED. Paper research at design level; awaiting an independent non-author
review.**
- Authorization: #1169 c.7066630306.
- It walks the nodes of `PLAN.md`, which was committed before this note at `550e8482`.
- No computation is run. No manuscript, Lean or registry file is edited. No premise is adopted.

**Inputs, at their reviewed standing:**
- OPRES, #1511 at `7669e511`;
- I3-SOURCE, #1508 at `df520f3b`;
- GATE-A r5, #1503 at `fd3cb064`, with D5 and D6 decided (c.7065620072);
- P-ST, #1510 at `c45b82cf`;
- BQ1, #1498 at `3269772a`;
- Proposition U, #1504 at `31594967`.

Corpus lines are at `main` `df6da1c6`.

**Labels.**
- [R] a reviewed record, cited; [W] a derivation here, not reviewed; [LIT2] literature from
  memory, not re-located.
- (N) and (I) follow the owner standard: an (I) result is not a failure.
- **KIN** is the Born-form representation on configurations, as OPRES and I3-SOURCE use it.
- **R-READ** (every native readout effect lies in the configuration algebra) is **unresolved**.
  READOUT-ALG is checking it, and it is carried as a case split.

## 0. Summary

| Q | Outcome | Decisive sub-question | Cheapest decisive step |
|---|---|---|---|
| Q1 operations | Under R-READ: OBSTRUCTION (OPRES §5, [R]), which also needs configuration post-measurement states. Under ¬R-READ: INCONCLUSIVE | On both branches: what is the native post-measurement rule? Is it configuration-valued (no creator), or does it give a non-diagonal output on some configuration input, with a non-monomial net action? | The post-measurement rule of the native readout, from READOUT-ALG. C-1 (§4, MIO half; not run) once a candidate is named |
| Q2 composition | INCONCLUSIVE | Joint scaling of the readout cone, \|R(n, ε)\|, in the qubit count n (route (ii), R-READ). Route (i), ¬R-READ: the native cost model of the readout. An efficient route must break one of H1–H5 | Paper: check Montina's ontic-state dimension result and Hardy's excess baggage for n-qubit scaling (§2.3) |
| Q3 preparation, measurement, acceptance | Preparation and final readout in the configuration basis: native as algebra, (I) on KIN. Bounded-error amplification: INCONCLUSIVE | Are successive "accept" records coarse-grained local observables to which Main:764's exponential decorrelation under (EM) applies, at separations compatible with the (C2)/(C4) memory windows? | Paper: Chernoff bound for exponentially mixing sequences under Main:764, with the run budget of Structure:1231 (§3.3) |

**Standing statement.** Native Turing universality, even if established, would not by itself
prove BQP capability:
- it supplies classical hosting, and BQ1-D shows that classical hosting under H1–H5 with
  polynomial resources stays in BPP;
- BQP capability additionally needs Q1's two coherent elements (OPRES Theorem C), Q2's
  polynomial composition, and Q3's acceptance semantics.

**Productivity (PLAN §4).**
- **P2 is met** by all three decisive sub-questions.
- **P3 is met, narrowly**, by §3.3: no record lists independence of runs as a hypothesis of
  amplification. The corpus does state a decorrelation bound (Main:764).
- The earlier P1 claim (¬R-READ breaks H4) is close to definitional and is not counted.

## 1. Q1: native implementation of the required operations

### 1.1 What is known

- **Necessity, OPRES Theorem C [R].** This is (I) on KIN and countable carriers, at layer X. A
  protocol within diamond distance 2κ_col(W) of Ad_W contains a non-MIO element. One within
  2κ_row(W) contains a non-DIO element. For non-monomial W both bounds are positive. The pair is
  tight, as one-bit teleportation (CC-1) shows: a |+⟩ creator and a ⟨±| detector suffice for
  Hadamard.
- **Native status, OPRES §5 [R].**
  - The stated native operations lie in 𝒩 ⊆ MIO ∩ DIO: bijective dynamics, configuration
    preparations and priors, configuration readouts, and feedforward.
  - This verdict is (I) on KIN and **conditional on R-READ**. Dynamics alone is (N):
    `substratumClass_monomial` [K].
- **I3-SOURCE S1 and S2 [R]**, (I) under their assumptions (a)–(e):
  - a permutation dilation realizes Ad_W only for monomial W;
  - under any same-basis unitary encoding, its one-step channel has root-of-unity spectrum, so
    an exact irrational rotation is excluded.
  - The routes left open:
    - FLOW, which is non-monomial;
    - preparation-dependent coherent hidden states, dropping (c);
    - uncountable carriers with non-classical hidden states, dropping (e);
    - protocol realization, dropping (b).
- **The native rule.** R_q: SM:294 gives the formula, and `papers/main_repro/lyapunov_v3.py:16–19`
  the code. It is a bijection on configurations, so its one-step map is a permutation and monomial
  (N).

### 1.2 Case split on R-READ [W]

- **R-READ holds.** With configuration-valued post-measurement states (below), every native
  element is **MIO**, though not necessarily DIO. An effect-level R-READ does not exclude a
  detector: the #1513 addendum's countermodel K₀ = H ⊕ 0, K₁ = |2⟩⟨2| (c.7066739331) has diagonal
  effects and is not DIO. The **OBSTRUCTION** therefore rests on Theorem C(a), the absence of a
  creator, alone. No non-monomial unitary is realized within the stated distances by any finite protocol of native
  elements, with any control, feedforward, randomness, size or depth. Label: (I) on KIN and R-READ.
  This only restates OPRES §5 (CONFIRMING).
  - **Implicit premise.** R-READ concerns *effects* only (OPRES §0; READOUT-ALG). Effects in the
    configuration algebra do not by themselves give MIO: a configuration readout followed by
    preparing |+⟩ has diagonal effects and is not MIO. The obstruction therefore also needs
    native post-measurement states to be configurations. Under KIN this is (N) as algebra where
    the corpus defines the instrument's state-update rule: permutation instruments,
    `localLuders`, `readProj` and `recordInstr` (addendum items 2, 3 non-selective, and 5–10).
    Where the corpus defines no state-update rule, at addendum items 1, 4, 11, 12 and 22, the
    premise is **Open**.
- **R-READ fails.** Some native readout has an effect E outside the configuration algebra.
  - **This is a live reading.** The corpus states that the observable algebra on each finite
    region is the full matrix algebra on its configuration space (Structure:742, :788;
    Main:722; GR:366). Whether elements of that algebra outside the configuration algebra are
    *native readouts*, i.e. implementable by the substratum, is what READOUT-ALG (#1513, under
    REVISE) checks.
  - By READOUT-ALG RA-1 (unreviewed), R-READ holds under readings R1 and R2 on countable
    carriers. ¬R-READ then needs an R3/R4 (supplied or represented) instrument, whose
    post-measurement rule is supplied data. The question becomes whether that supply is native.
  - Its Heisenberg dual takes a configuration effect out of the configuration algebra, so it is
    **non-DIO**. The detector half is then present.
  - It need not be non-MIO. A destructive readout whose post-measurement state is a
    configuration is MIO.
  - A creator could still arise from the same instrument: a Lüders-type update with a
    non-configuration effect E produces a non-diagonal output from a diagonal input whenever E
    does not commute with the configuration projectors. That holds only if the native
    post-measurement rule is Lüders-type, which nothing in the corpus establishes.
  - **INCONCLUSIVE.**

**Decisive sub-question (P2), on both branches.** What is the native post-measurement rule?
- Under R-READ, a configuration-valued rule is what makes the obstruction hold. A
  non-configuration rule would supply a creator even with diagonal effects.
- Under ¬R-READ, does the native instrument have a non-diagonal post-measurement state on some
  configuration input? If so, are the creator and detector it supplies enough to generate a
  non-monomial net action?
- **Yes:** one native instrument plays both roles of Theorem C, and Q1 turns POSITIVE
  representationally. The operational question remains (OPRES §6; D-W).
- **No:** a separate native creator is still needed, with the S2 routes as the only candidates.

### 1.3 Established / Assumed / Missing

- **Established.**
  - The R-READ branch is OBSTRUCTION ([R], CONFIRMING).
  - The ¬R-READ branch reduces to the instrument's post-measurement rule ([W], P2).
- **Assumed.**
  - KIN, and countable carriers (Theorem C).
  - Posit (iv)-type diagonal priors, for the preparation half.
  - Configuration post-measurement states, for the R-READ obstruction: (N) as algebra under KIN
    for instruments with a corpus-defined update rule; **Open** for readouts with none (addendum
    items 1, 4, 11, 12, 22).
  - The standing of R-READ's measurable-carrier case, which READOUT-ALG makes conditional on
    measurability.
- **Missing.** The earliest unsupported step is a physical mechanism: the native post-measurement
  rule on both branches, and under ¬R-READ a native, not supplied, readout outside the
  configuration algebra.

## 2. Q2: composition with polynomial overhead

### 2.1 What is known

- **BQ1 [R].** Under H1–H5, native runs are classically samplable in poly(n). Efficient BQP
  hosting would then give BQP ⊆ BPP (BQ1-D, (I)).
- **Proposition U [R], (I) via (xiv).** For native measurements whose *outcome is a function of
  configurations on a finite region*, exact reproduction of even one qubit's prepare-and-measure
  behaviour needs readout cones that lie in no finite region. The behaviour matrix factors
  through |Q|^{|R|} configurations, and the qubit's nonnegative rank is unbounded (Main [55]).
  Its premise is a configuration-algebra readout, i.e. R-READ. It does **not** apply on the
  ¬R-READ branch.
- **OPRES §6 [R].** Representational necessity does not imply operational necessity:
  Gottesman–Knill dynamics is coherent and efficiently simulable.

### 2.2 Relation to BQ1 [W]

- H4 requires the readout to be a polynomial-time function of the visible configuration. That
  is a configuration-algebra readout, so **¬R-READ breaks H4 by definition**.
- Under R-READ, Q1 is already obstructed representationally. Operationally, any efficient
  quantum advantage would have to break H1, H2, H3 or H5 instead.
- So the two routes to efficient BQP hosting are:
  - (i) ¬R-READ, with readouts of polynomial cost;
  - (ii) R-READ, with failure of an H1, H2, H3 or H5 hypothesis. The realization theorems of
    Main:574–590 take this route through H2/H5 (BQ1 check (h)), at a cost of 4ⁿ register
    entries, which is not polynomial.
- In both routes an efficient hosting must break **one of H1–H5**. ¬R-READ breaks H4
  automatically; that is close to definitional and is not counted as productive.
- BQ1 is not a premise here. The conclusion is a consistency check under PLAN §2.

### 2.3 Decisive sub-question and cheapest step

**Route (ii), R-READ with H5 failing: decisive sub-question (P2).** What is the joint scaling
of the readout cone |R(n, ε)| in the qubit count n and the precision ε?
- Proposition U gives |R| ≳ log rank₊ / log|Q|, with rank₊ the nonnegative rank of the
  prepare-and-measure fragment.
- At fixed n the ε-scaling is likely benign. Finite-precision ontological models for one qubit
  use about poly(1/ε) ontic states, as in a discretized Kochen–Specker model [LIT2, from the
  review]. That would give |R| = O(log 1/ε).
- The deciding scaling is in **n**. If the ontic-state dimension of n qubits is exponential in n
  (Montina 2008; Hardy's ontological excess baggage [LIT2]), then |R| is exponential in n, and
  BQ1's conditional answer applies: a polynomial cone gives BPP.

**Route (i), ¬R-READ.** Proposition U does not apply. The decisive sub-question is the native
cost model of a readout outside the configuration algebra: native sites and steps per use as a
function of n. No such model exists in the corpus, so this needs the readout itself first (Q1).

**Cheapest decisive step (paper).**
- Check Montina's result and Hardy's excess-baggage argument for their exact hypotheses:
  - preparation independence, i.e. (xiv);
  - exactness against approximation;
  - the class of fragments.
- Then state the n-scaling of |R(n, ε)| for route (ii) at the hypotheses those results carry.
- Literature first (§A.12 item 4). Not located for this record.

**Outcome: INCONCLUSIVE.**
- **Established:** the route split, and the restriction of Proposition U to route (ii) [W].
- **Assumed:** H1–H5 as BQ1 states them; (xiv) for Proposition U.
- **Missing:**
  - route (ii): the n-scaling of |R(n, ε)|, which needs mathematics;
  - route (i): a native readout and its cost model, which needs a physical mechanism.

## 3. Q3: preparation, measurement and bounded-error acceptance

### 3.1 Preparation and final readout

- A computational-basis preparation |0…0⟩ is a configuration, element (n2). A final readout in
  the computational basis is a configuration readout, element (n3).
- Both are native as algebra. Calling them quantum preparation and measurement is (I) on KIN,
  since KIN fixes the computational basis as the configuration basis.
- They are not the coherent elements. Theorem C places those strictly inside the protocol, so
  this part imports no quantum behaviour.
- **Established** (CONFIRMING, from OPRES Lemma C).

### 3.2 Acceptance probability

- The probability that the readout reads "accept" is a pushforward of the hidden prior. Under
  posit (iv) it is the counting-measure probability of the set of accepting microstates (Main:54).
- Its equality with the Born probability ⟨ψ|Π_acc|ψ⟩ is exactly what KIN plus Q1's coherent
  elements would have to deliver. Taking it as a premise would import the desired behaviour.
- With R-READ and the dynamics in 𝒩, the acceptance probability is a classical pushforward,
  which is what BQ1 uses.
- **Established:** the identification of the import [W].

### 3.3 Bounded-error amplification (P3)

- BQP's 2/3 versus 1/3 gap is amplified by majority vote over independent repetitions. In one
  deterministic universe, "repetitions" are later runs of the same trajectory, so their hidden
  initial conditions are not independent draws from the prior.
- **What the corpus states (§A.19).**
  - **Main:764,** in the proof of the observer-selection theorem: under (EM), the dissipative
    gap "bounds the decay of such coarse-grained correlations exponentially at rate
    1/τ_mix". So a decorrelation bound exists, for coarse-grained local observables under (EM),
    a posit.
  - **Structure:1231.** The visible factor of a finite reversible substratum has zero entropy
    rate, so its fresh randomness is capped at log|C_V × C_H|. That caps the number of
    effectively independent runs on a finite representative.
  - **OI-PE-1, PE-03** (`verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/README.md`).
    It is prospective. It compares one fixed hidden seed with independently supplied randomness
    across repeated and adaptive measurements, so it raises this question without answering it.
- **What follows, given (EM) [W].** If successive "accept" records are coarse-grained local
  observables in Main:764's sense, then a Chernoff-type bound for exponentially mixing sequences
  [LIT2, standard] gives concentration of the majority vote. It holds with k runs separated by
  Δ ≫ τ_mix, up to the Structure:1231 budget.
- **Tension.** The observer's own memory must persist: Main:161 and (C2)/(C4) need hidden memory
  to survive on windows kτ_S ≪ τ_B, where τ_B is set by the same coarse-grained mixing ((EM),
  Main:161). Runs separated by Δ ≫ τ_mix decorrelate the hidden sector, and with it the record
  memory the computation relies on.
  - The observer's records of earlier runs are visible records and need not decay. So the
    tension is not a contradiction.
  - It does constrain the design: amplification must keep the run memory visible and let the
    hidden sector remix between runs.
  - Whether a single native protocol can do both is not settled here.
- **Decisive sub-question (P2).** Are successive "accept" records coarse-grained local observables
  in Main:764's sense, at a separation Δ that is compatible with the (C2)/(C4) windows required
  inside each run?
- **Cheapest step: paper.** State the Chernoff bound under Main:764's decay as a lemma with its
  hypotheses, and check the record-observable condition against Main:756's definition of
  Σ_loc.
- P3 is met only narrowly: no record lists independence as a hypothesis of amplification.
- **Outcome: INCONCLUSIVE.**
- **Assumed:** KIN; posit (iv); (EM) (posit), where used.
- **Missing:** the applicability of Main:764 to accept records, which needs mathematics, and the
  resolution of the memory/remixing tension, which needs a protocol.

## 4. Preregistered computation (design only; not run; needs its own authorization)

**C-1: exact MIO test of a candidate native readout.**
- **Status.** Dormant. It is not decision-relevant until triggered; READOUT-ALG RA-1 currently
  names no candidate.
- **Trigger.** READOUT-ALG supplies a concrete native readout instrument {Φ_o} on a finite
  carrier with an effect outside the configuration algebra.
- **What is already settled.** For any such trigger candidate, non-DIO is proved analytically
  (§1.2: Φ_o*(1) = E_o is not diagonal). Here DIO means the detection-incoherent class,
  Δ∘Φ = Δ∘Φ∘Δ, not the dephasing-covariant class of Chitambar–Gour. **Only the MIO half
  discriminates.**
- **Quantity.**
  - Φ is MIO iff Φ(|x⟩⟨x|) is diagonal for every configuration x. This is tested exactly, with
    rational or algebraic arithmetic.
  - The DIO test, Φ*(|y⟩⟨y|) diagonal for every y, is kept only as an exactness control, and it
    must reproduce the analytic non-DIO verdict.
- **Decision rule.** **Non-MIO** iff some off-diagonal entry of Φ(|x⟩⟨x|) is nonzero; otherwise
  MIO. The verdict is evidence about that instrument only.
- **Controls**, which must give the stated result or the verdict is void:
  1. a configuration-basis Lüders measurement gives DIO and MIO;
  2. a Hadamard-basis Lüders measurement on one bit gives non-DIO and non-MIO;
  3. a destructive Hadamard-basis readout that re-prepares a configuration gives non-DIO and
     MIO;
  4. a configuration readout that re-prepares |+⟩ gives DIO and non-MIO.
- **Not covered.** Composition, cost, infinite carriers.

No other computation is proposed.

## 5. What this record does not claim

- It does not claim that R-READ holds or fails.
- It does not claim native universality in either direction (#1461/#1499).
- It does not use BQ1's hypotheses as premises of Q1–Q3.
- It proposes no new premise, and no manuscript wording.
