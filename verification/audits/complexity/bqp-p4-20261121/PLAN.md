# BQP-P4 plan: the next test of efficient native quantum computation

**Status: WIP / UNVERIFIED. Committed before any analysis node is written.**

- **Authority.** Owner decision #1169 c.7067281228 (round 4): design and paper research only. No
  preregistered computation is run. Nothing is implemented, merged or written into a manuscript.
  No imported quantum operation is counted as native. No premise is adopted.
- **Stacking.** The branch is stacked on #1514 at its reviewed head `c7a16eb1`, which is not
  moved. Issue: #1487.

## 1. Starting point (#1514, reviewed)

- **Q1 (operations).** Blocked under effect-level R-READ through Theorem C(a): there is no
  creator. Native non-DIO is Open. READOUT-ALG (#1513) is a constraint under review, not an
  impossibility theorem.
- **Q2 (composition).** The deciding scaling is in the qubit count n.
- **Q3 (acceptance).** Main:764 and (C2)/(C4) are in tension over amplification.

## 2. Task

1. Select the **single** decisive sub-question for efficient native quantum computation.
2. Design a test or proof plan for it.

The selection is argued in the analysis against the alternatives, under the criterion in §3.

## 3. Selection criterion (fixed now)

A sub-question is **decisive** iff it meets all three conditions:

- **(S1)** Each of its answers would assign a different classification to "efficient native
  quantum computation on the native reading": OBSTRUCTION, a named escape route, or INCONCLUSIVE.
- **(S2)** It is stated at the layer at which it would be proved:
  - effect, instrument or accessible algebra;
  - ontic or Born-form;
  - typing, soundness or operational.
- **(S3)** No other open sub-question is a precondition for it to bear on efficiency.

## 4. Productivity test (fixed now)

The record is **productive** iff it gives at least one of:

- **(P1)** a selection argument showing why the other candidates fail S1, S2 or S3, at their
  layer;
- **(P2)** a proof plan or test whose two outcomes are named in advance, with the decision rule;
- **(P3)** an exposed hypothesis, or a layer confusion in a reviewed record.

A restatement of reviewed results is CONFIRMING and does not count.

## 5. Outcomes

Exactly one per decisive sub-question:

- **OBSTRUCTION**, with its class and labels;
- **ESCAPE**: a named native route that the analysis cannot exclude;
- **INCONCLUSIVE**: the missing item is named.

INCONCLUSIVE is admissible.

## 6. Layer rule and labels

- Every result is stated at the layer at which it is proved. Where a layer is not reached, that
  is said.
- Labels: (N) or (I), and Established / Assumed / Missing.
- Readout statements keep three levels apart: effects; instruments and their state updates;
  operationally accessible algebras. The abstract full matrix algebra (Str:742, Str:788,
  Main:722, GR:366) is not used as a supply of operations.

## 7. Computations

None is run. Any computation proposed in the analysis is preregistered there, with its decision
rule and controls, and needs separate authorization.
