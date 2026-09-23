# Arc C preregistration — Amendment 1: retire adversarial bias controls

This is an **execution-affecting control-plane amendment** to
`verification/programmes/oi-qm/track-i/arc-c-quantum-representation/preregistration.md`.

Frozen preregistration provenance:

- freeze commit: `38a8f09d9d314fdd3d7747d0d0351f07c693c582`;
- authoritative frozen blob: `8177527b11a0970c7fc71f1bff382112aaf93aa6`;
- preregistration merge commit on `main`: `073ef65ae286e67e84ce4dfc0f634252cf29939f`.

The frozen preregistration remains byte-for-byte unchanged. This amendment supersedes only the
adversarial/bias-control requirements identified below. No Arc C construction, counterexample
search, proof search, census, probe, or simulation occurred between the preregistration merge and
this amendment.

## Decision

The Arc C round no longer uses an adversarial-target allocation or a drafting-prior bias protocol.
The disclosed drafting expectations in the frozen preregistration remain part of the historical
freeze record only. They have **no procedural or evidentiary role** in the execution of the round.

In particular:

- no target or proof direction is assigned according to who drafted the preregistration or what that
  drafter expected before execution;
- no person is required to take a constructive or adversarial side;
- no special verdict authority is created by the disclosed priors;
- the round does not audit whether work was performed against or in favour of a prior;
- the final report need not classify the disclosed priors as confirmed, refuted, or untested.

The ordinary evidence rules remain unchanged: a theorem, counterexample, classification, or open
status must meet the evidence standard already frozen for that kind of claim. A prior is neither
positive nor negative evidence simply because it was written before execution.

## Superseded frozen clauses

The following parts of `OI-QUANTUM-REPRESENTATION-AUDIT.md` are superseded for Arc C execution:

1. **Authorship assignment.** The sentence stating that the draft is written by the side that will
   take the adversarial target no longer assigns any execution role.
2. **Drafting-expectation bias language.** The language requiring the disclosed priors to determine
   adversarial work, and the instruction that a reviewer treat correlated priors as a bias-control
   point, are retired. The four listed expectations remain historical provenance only.
3. **Mandatory control 10 — Prior-disclosure control.** Control 10 is retired. Controls 1–9 and
   11–13 remain in force under their original numbering; the frozen file is not renumbered.
4. **Execution allocation.** The execution-discipline sentence requiring a post-freeze allocation in
   which the author holds the adversarial targets and the freeze authority does not inherit the
   drafting priors is retired. No bias-based target allocation is required before research begins.
5. **Final-report item 11.** The requirement to state which drafting priors were confirmed, refuted,
   or untested, and what independent evidence carried each confirmed prior, is retired. The other
   final-report requirements remain in force under their original numbering.

## Execution discipline after this amendment

After this amendment is separately frozen and merged to `main`, the single Arc C execution/result PR
may begin from that resulting `main`. Any contributor or reviewer may pursue T1, T2, T3,
constructive routes, obstruction routes, or intersection results as useful. The final exact-head
review remains required as a quality and evidence audit, not as an adversarial-bias mechanism.

Nothing else in the frozen Arc C preregistration changes. In particular, the frozen definition of
`Q*(V)`, the horizon quantifier quarantine, finite-visible scope, T1/T2/T3 targets, RC1–RC5 outcome
taxonomy, readout-injectivity split, positive-root-mass condition, evidence hierarchy, Arc D/E
boundary, immutable-file discipline, single execution/result PR rule, and explicit owner merge
direction remain binding.

This amendment itself must be frozen by exact commit SHA and blob SHA and merged to `main` before
any Arc C execution begins.
