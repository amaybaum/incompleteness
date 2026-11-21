# GATE-A r6: plan (premise reconciliation and decision wording)

**WIP / UNVERIFIED. Design and paper research only.** The plan is committed before the
reconciliation note (round-4 owner record, #1169 c.7067281228). It adopts nothing and runs no
computation.

**Base.** Branch `research/gate-a-r6-20261121`, stacked on #1503 at
`109b9590c72a0d5d00aaa1690298bf9b3580e3c5` (GA r5.8, confirmed at #1503 c.7067277470). #1503
stays as reviewed. Thread Issue #1502.

## 1. Task 1: reconcile the missing premises

**Objects.** E; I-3 (D5 open as a research unit, #1169 c.7065620072; I3-SOURCE found no
independently justified criterion, #1508 at `df520f3b`); J-coh; FE-ADM; BF (#1510 at `c45b82cf`,
folded in GA r5.7–r5.8); O1 as two separate obligations, a non-MIO element and a non-DIO element
(#1169 c.7066541026; OPRES Theorem C, Proposition D and Remark D′, #1511 at `7669e511`, all (I)).

**Questions, each answered at a declared layer.** The layers are: effect, instrument and
accessible algebra; ontic and Born-form; typing, soundness and operational. A result is stated at
the layer where it is proved.
- Q1. For each premise: where does it enter, at which layer, and is it (N) or (I)?
- Q2. Which pairs are independent? Each independence claim needs a model meeting one premise and
  failing the other, at least as a sketch.
- Q3. Which implications hold between them? The candidate implication is BF together with a
  non-monomial target ⇒ the O1 pair in the Born-form description, via Theorem C. It must be checked
  against Theorem C's exact hypotheses.
- Q4. Is there a formal map between O1 and I-3? The bridge rule applies: no identification
  without an explicit map.

**Productivity test, fixed now.** The reconciliation is a gem iff it yields at least one of:
- an implication between premises, proved under stated hypotheses;
- an independence, with a separating model;
- a layer error in an existing record.

A table that only lists the premises is a non-gem and is recorded as such. **INCONCLUSIVE** is an
admissible outcome for each question. It is reported with the missing premise named.

## 2. Task 2: exact wording for D1–D4 and D7

For each decision, the note gives:
- the exact text the owner would adopt;
- each alternative, word for word;
- what each choice changes, in the record, in `main`'s contract, and in #1428.

No option is recommended as adopted. D5 and D6 are decided (c.7065620072) and are not reopened.

## 3. Boundaries

- No edit to #1503, #1508, #1510 or #1511.
- No manuscript change.
- No adoption of any premise.
- No computation.
- No post on #1169.
- R-READ is treated as unresolved (READOUT-ALG #1513 under review).
- The three readout levels are kept distinct: effects, complete instruments, and accessible
  algebras.
