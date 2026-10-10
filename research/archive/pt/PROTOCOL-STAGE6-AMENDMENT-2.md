# Protocol — stage 6 (Q-EX-FULL), amendment 2: step 4 launch conditions (append-only; amendment 1 and `PROTOCOL-STAGE6.md` unchanged)

Issued 2026-10-10 after the step-2 and step-3 threads G6 and R6 reported and were audited
(`pt/audit/stage6-inputs/G-audit/AUDIT-G.md`, `pt/audit/stage6-inputs/R-audit/AUDIT-R.md`). Base L = `9f9f8257…`,
read-only. Research only; every hold of `PROTOCOL-STAGE6.md` §0 stands (no repository change, no branch, no PR,
no CI, no governed round, no publication, no manuscript edit). Amendment 1's A1.1 (working directory `pt/T6/`),
A1.6 (the assignment) and A1.7 (common rules) apply unchanged; this amendment fixes only what step 4 reads and
how its outcome is stated.

## A2.1 Inputs of T6 (replaces A1.2's "never read `pt/G6/`, `pt/R6/`" for step 4 only)

- The frozen step-2 and step-3 records, read-only: `pt/G6/` (`GRAPH.md`, `graph.tsv`, `NOTES.md`, `RESULT.md`,
  scripts and outputs) and `pt/R6/` (`REASSESSMENT.md`, `NOTES.md`, `RESULT.md`, scripts and outputs). Their
  audits are binding where they qualify a claim: `pt/audit/stage6-inputs/G-audit/AUDIT-G.md` and
  `pt/audit/stage6-inputs/R-audit/AUDIT-R.md`. Of `pt/audit/stage6-inputs/` T6 reads exactly these two files and
  `I-audit/AUDIT-I.md`; nothing else in that directory (the coordinator's pre-audit material is for the auditor,
  not for the thread).
- Everything A1.2 lists: the step-1 records `pt/I1/`–`pt/I4/`; the stage-4 and stage-5 integration notes, audits
  and thread records; the stage-3 records under `pt/` where a cone's construction is needed (the explicit cones
  K(E0) and K(Z_F) are defined in `pt/R6/REASSESSMENT.md` §1 with their stage-3 provenance); the kernel,
  manuscripts and roadmap at L under `pt/base/`.
- Never read: `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`,
  `pt/audit/stage6-inputs/OWNER-*` and every other file of `pt/audit/stage6-inputs/` not named above,
  `pt/audit/reviews/`, `pt/audit/aborted-launches/`, the `evidence/` quarantine copies under `pt/D5/` and `pt/C5/`.

## A2.2 Sweeps and pre-existing coordinator files

A1.3's exclusions stand. The following exist before the launch and are not anomalies: `pt/audit/stage6-inputs/`
(the coordinator's audit area, including `G-audit/`, `R-audit/` and their `replay/` subdirectories), this
amendment with its sidecar `pt/PROTOCOL-STAGE6-AMENDMENT-2.sha256` (verifies from the scratchpad directory, as the
stage-4/5/6 sidecars do), and the launch entry appended to `pt/audit/STAGE3-RELAUNCH-LOG.md`.

## A2.3 The applicable premise set, as audited

- The complete applicable premise set at L is R6's list of 199 items (`pt/R6/r1_inventory.out`,
  `REASSESSMENT.md` §2–§3), each at its actual status. Of these, 68 are NOT REACHED for every alternative because
  L has no H→P, M→P or G→P bridge (G6's NO-MEET, reproduced in AUDIT-G §2); they enter a derivation of (b) only
  through an obligation G6 names (K2, P-STAGE2, P-ACT2, K∞-Act, K∞-Drive, K1), and such an obligation is not a
  premise at L. The 131 remaining items are, per alternative, SATISFIES or FAILS in R6's audited tables; every
  FAILS row is a hypothesis (do-not-assume item, [D] four-token hypothesis, PT-record candidate), never a theorem
  or definition at L (AUDIT-R §2, §5).
- `K({F, cnot F})` and `K(e_c)` (named in `PROTOCOL-STAGE6.md` step 3) were not reassessed by R6 (amendment 1's
  A1.5 omitted them). T6 relies on the explicit cones K(E0), K(Z_F) and the EXOTIC-E seeds of R6's Table A3; if
  T6's countermodel is one of the two omitted cones, T6 reassesses it itself against the 199 items with exact
  scripts before using it.

## A2.4 Outcome statement

As A1.6, with the two-way form of `PROTOCOL-STAGE6.md` step 4:

- **DERIVATION**: a chain from inventory items at their actual status to (b) in its weakest sufficient form,
  each step [K], [W] or [X]; every premise passes the disguise test of `PROTOCOL-STAGE5.md`; no do-not-assume
  item enters except as the item under test, named. A chain that uses an inventory item whose status at L is
  assumed, conditional, open or empirically motivated yields **CONDITIONAL on that item**, named at its status
  (as stage 5's α–δ), not DERIVATION.
- **INDEPENDENCE**: a countermodel that satisfies every item reaching the pair cone at L — cited row by row
  against R6's audited table for that alternative (SATISFIES or NOT REACHED on every non-hypothesis item) — and
  violates (b) in its weakest sufficient form by an exact witness; the missing assumption is isolated and stated
  as the exact content that would close the gap, with its own disguise test (which named inventory item or
  do-not-assume clause it restates, if any).
- **UNRESOLVED**: a failed derivation without a countermodel, or a countermodel without the row-by-row check;
  both failures recorded.

Depth-first: the derivation attempt first (every route stage 5 left open for the complete premise set, including
the items stage 5 did not have — the H-, M-, G-level items now in the inventory — and the kernel-completed
dependencies G6 added), then the countermodel. The productivity test and the decision vocabulary are fixed in
`NOTES.md` before the first node. Exact scripts; decision rules in headers before the first run.
