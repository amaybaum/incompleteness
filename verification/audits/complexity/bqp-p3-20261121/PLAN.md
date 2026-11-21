# BQP-P3 plan: from an expressive substratum to efficient quantum computation

**Status: WIP / UNVERIFIED. Committed before any analysis node is written.**

- **Authority.** Owner decision #1169 c.7066630306 authorizes BQP Phase 3 as a proposal at
  design level: paper research, literature, proof exploration and preregistration. It does not
  authorize running computations, implementation, CI, Lean builds, manuscript changes or new
  premises.
- **Stacking.** The branch is stacked on #1498 at its reviewed head `3269772a`, which is not
  moved. Issue: #1487.

## 1. Questions

- **Q1.** Can the actual native OI rule implement the operations that quantum computation needs?
  The necessity criterion is OPRES Theorem C (#1511 at `7669e511`): realizing a non-monomial
  unitary needs a non-MIO element (a coherence creator) and a non-DIO element (a coherence
  detector), possibly one and the same. The analysis uses I3-SOURCE S1 and S2 (#1508 at
  `df520f3b`). **R-READ**, the claim that native readouts lie in the configuration algebra, is
  **unresolved** and is carried as a case split, never as a premise.
- **Q2.** Can those operations be composed with polynomial overhead?
- **Q3.** Can preparation, measurement and bounded-error acceptance be established without
  importing the desired quantum behaviour?

**Standing statement.** Native Turing universality, even if established (#1461/#1499), would not
by itself prove BQP capability. It gives classical hosting. Under BQ1 (#1498), classical hosting
with polynomial resources stays inside BPP.

## 2. Separation from BQ1

BQ1's hypotheses H1–H5 are not premises of Q1–Q3. BQ1 enters only as a **consistency check**:
- a positive route to efficient BQP hosting must break at least one of H1–H5, unless
  BQP ⊆ BPP (BQ1-D);
- each node names which hypothesis its route breaks.

## 3. Method

The walk is depth-first (§A.12, §A.31). For each question the node records:
1. what is known, with labels;
2. the decisive sub-question;
3. the cheapest decisive step.

Labels follow the owner standard (#1169 c.7064859041): (N) or (I), and Established / Assumed /
Missing.

## 4. Productivity test (fixed now)

A node is **productive** iff it yields at least one of:
- **(P1)** a statement, with its scope, that strictly sharpens what OPRES, I3-SOURCE, BQ1 or
  Proposition U already give for the question;
- **(P2)** a decisive sub-question whose two answers would lead to different classifications of
  the question;
- **(P3)** an exposed hypothesis that some reviewed record or corpus statement uses without
  listing.

A restatement of reviewed results is recorded as CONFIRMING and does not count.

## 5. Outcomes (per question, exactly one)

- **POSITIVE**: a native route with every element shown native, at the stated label.
- **OBSTRUCTION**: a no-go for a stated class, with its scope.
- **INCONCLUSIVE**: the decisive sub-question is named and is not answered here. An INCONCLUSIVE
  result is an admissible outcome, not a failure.

A question conditioned on R-READ reports its outcome for each branch of the case split.

## 6. Computations

No computation is run under this plan. Any computation proposed in the analysis is preregistered
there, with its decision rule and controls, and needs its own authorization to run.
