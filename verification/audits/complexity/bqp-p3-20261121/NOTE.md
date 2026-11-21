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
| Q1 operations | Under R-READ: OBSTRUCTION (OPRES §5, [R]). Under ¬R-READ: INCONCLUSIVE | Does the native readout outside the configuration algebra also supply a coherence creator, or a coherent resource, with a non-monomial net action? | When READOUT-ALG names a candidate readout, an exact DIO/MIO test of it (preregistered as C-1, §4; not run) |
| Q2 composition | INCONCLUSIVE | Under ¬R-READ: is the cost of a native readout outside the configuration algebra polynomial in the precision it reaches? (BQ1 forces any efficient route to break H4) | Paper bound on readout-cone growth with resolution in Proposition U's setting (§2.3) |
| Q3 preparation, measurement, acceptance | Preparation and final readout in the configuration basis: native as algebra, (I) on KIN. Bounded-error amplification: INCONCLUSIVE | Are repeated runs of one deterministic universe independent enough to amplify? | Paper check of which posit, (v) mixing or (EM), would give independence of runs, and whether either is stated for that purpose (§3.3) |

**Standing statement.** Native Turing universality, even if established, would not by itself
prove BQP capability:
- it supplies classical hosting, and BQ1-D shows that classical hosting under H1–H5 with
  polynomial resources stays in BPP;
- BQP capability additionally needs Q1's two coherent elements (OPRES Theorem C), Q2's
  polynomial composition, and Q3's acceptance semantics.

**Productivity (PLAN §4).**
- **P2 is met** by all three decisive sub-questions.
- **P3 is met** by §3.3: bounded-error amplification needs independence across runs, which no
  reviewed record lists.
- **P1 is met** by §2.2: an efficient route must break H4, and in the ¬R-READ branch H4 fails
  automatically. This sharpens BQ1 against OPRES.

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

- **R-READ holds.** Every native element lies in 𝒩, so Theorem C gives an **OBSTRUCTION**. No
  non-monomial unitary is realized within the stated distances by any finite protocol of native
  elements, with any control, feedforward, randomness, size or depth. Label: (I) on KIN and R-READ.
  This only restates OPRES §5 (CONFIRMING).
- **R-READ fails.** Some native readout has an effect E outside the configuration algebra.
  - Its Heisenberg dual takes a configuration effect out of the configuration algebra, so it is
    **non-DIO**. The detector half is then present.
  - It need not be non-MIO. A destructive readout whose post-measurement state is a
    configuration is MIO.
  - A creator could still arise from the same instrument: a Lüders-type update with a
    non-configuration effect E produces a non-diagonal output from a diagonal input whenever E
    does not commute with the configuration projectors. That holds only if the native
    post-measurement rule is Lüders-type, which nothing in the corpus establishes.
  - **INCONCLUSIVE.**

**Decisive sub-question (P2).** In the ¬R-READ branch, does the native readout instrument have a
non-diagonal post-measurement state on some configuration input? If so, are the creator and
detector it supplies enough to generate a non-monomial net action?
- **Yes:** one native instrument plays both roles of Theorem C, and Q1 turns POSITIVE
  representationally. The operational question remains (OPRES §6; D-W).
- **No:** a separate native creator is still needed, with the S2 routes as the only candidates.

### 1.3 Established / Assumed / Missing

- **Established.**
  - The R-READ branch is OBSTRUCTION ([R], CONFIRMING).
  - The ¬R-READ branch reduces to the instrument's post-measurement rule ([W], P2).
- **Assumed.** KIN; countable carriers (Theorem C); posit (iv)-type diagonal priors for the
  preparation half.
- **Missing.** The earliest unsupported step is a physical mechanism: a native readout outside
  the configuration algebra (¬R-READ), and its update rule.

## 2. Q2: composition with polynomial overhead

### 2.1 What is known

- **BQ1 [R].** Under H1–H5, native runs are classically samplable in poly(n). Efficient BQP
  hosting would then give BQP ⊆ BPP (BQ1-D, (I)).
- **Proposition U [R], (I) via (xiv).** Exact native reproduction of even one qubit's
  prepare-and-measure behaviour needs readout cones that lie in no finite region. The behaviour
  matrix factors through |Q|^{|R|} configurations, and the qubit's nonnegative rank is unbounded
  (Main [55]).
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
- (P1) BQ1 is not a premise here. The conclusion is a consistency check under PLAN §2.

### 2.3 Decisive sub-question and cheapest step

**Decisive sub-question (P2).** Route (i): does a native readout outside the configuration
algebra cost poly(n, log 1/ε) native sites and steps per use, at precision ε?

- Proposition U shows that exact qubit behaviour needs unbounded readout cones. The **rate** of
  growth with resolution is not stated there.
- If log |Q|^{|R(ε)|} grows faster than poly(log 1/ε), no polynomial composition exists, even
  with fault tolerance, since fault tolerance needs gates at a constant error rate and readout
  at precision 1/poly.

**Cheapest decisive step (paper).** Bound |R(ε)| in Proposition U's setting.
- A *lower* bound would follow from the ε-approximate nonnegative rank of qubit
  prepare-and-measure fragments at resolution ε.
- An *upper* bound would follow from an explicit native construction. None is known.
- Literature to check first (§A.12 item 4): approximate nonnegative-rank and ontological-model
  overhead results for one qubit, such as Kochen–Specker-type and Montina-type ontic-state
  counting [LIT2]. Not located for this record.

**Outcome: INCONCLUSIVE.**
- **Established:** the route split (i)/(ii) [W].
- **Assumed:** H1–H5 as BQ1 states them; (xiv) for Proposition U.
- **Missing:** the scaling of |R(ε)|, which needs mathematics. Its physical side needs a native
  readout.

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
- Independence, or a sufficient decorrelation, of successive runs is therefore a needed
  hypothesis. No reviewed record lists it:
  - BQ1 treats one run;
  - OPRES and Proposition U treat one protocol.
- **Candidates.** The hidden-sector mixing hypothesis, posit (v) (ETH-motivated, Main:736), or
  the effective-mixing hypothesis (EM) behind the structural observer-selection theorem
  (Main:754–770). (EM) is stated with a mixing time τ_mix; whether that yields the needed
  decorrelation is the question below.
  Neither is stated for repetition independence. Both are posits.
- **Decisive sub-question (P2).** Does (v) or (EM) imply that the empirical frequency of
  "accept" over k successive runs concentrates at rate exp(−Ω(k)) around the single-run
  probability? Or are correlations across runs possible that defeat majority vote?
- **Cheapest step: paper.** Read the exact statements of (v) and (EM) and check whether a
  mixing-time or decay-of-correlations bound is stated. If one is, derive a Chernoff-type bound
  under it. If none is, record the gap.
- **Outcome: INCONCLUSIVE.**
- **Assumed:** KIN; posit (iv); (v) or (EM) where used.
- **Missing:** a decorrelation statement for successive runs. It needs mathematics given a
  stated posit, and a physical mechanism to justify the posit.

## 4. Preregistered computation (design only; not run; needs its own authorization)

**C-1: exact DIO/MIO test of a candidate native readout.**
- **Trigger.** READOUT-ALG supplies a concrete native readout instrument {Φ_o} on a finite
  carrier.
- **Quantity.**
  - Φ is DIO iff Φ*(|y⟩⟨y|) is diagonal for every configuration y, equivalently
    Δ∘Φ = Δ∘Φ∘Δ.
  - Φ is MIO iff Φ(|x⟩⟨x|) is diagonal for every x.
  - Both are tested exactly, with rational or algebraic arithmetic, on matrix entries.
- **Decision rule.**
  - **Non-DIO:** some entry ⟨y′|Φ*(|y⟩⟨y|)|y″⟩ with y′ ≠ y″ is nonzero.
  - **Non-MIO:** some off-diagonal entry of Φ(|x⟩⟨x|) is nonzero.
  - Otherwise the instrument is DIO or MIO respectively, which is evidence about that instrument
    only.
- **Controls**, which must give the stated result or the verdict is void:
  - a configuration-basis Lüders measurement must give DIO and MIO;
  - a Hadamard-basis Lüders measurement on one bit must give non-DIO and non-MIO;
  - a destructive Hadamard-basis readout that re-prepares a configuration must give non-DIO and
    MIO.
- **Not covered.** Composition, cost, infinite carriers.

No other computation is proposed.

## 5. What this record does not claim

- It does not claim that R-READ holds or fails.
- It does not claim native universality in either direction (#1461/#1499).
- It does not use BQ1's hypotheses as premises of Q1–Q3.
- It proposes no new premise, and no manuscript wording.
