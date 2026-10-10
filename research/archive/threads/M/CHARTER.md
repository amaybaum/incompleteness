# Thread M — full-equivalence dependency audit (launched 2026-10-02 after I, J, K, L reported and were verified)

Inputs (read all; re-verify any claim used against the tree at 6d0abf6b):
- threads/I/RESULT.md — V4′: DERIVED for the passive dynamics (ClassicalBranchDomain.evolve), NEEDS-PREMISE for the
  drive group; minimal form V4′-gen (one seed, closure under flow elements and J).
- threads/J/RESULT.md — P1 seed: CONDITIONAL on SC∞ (stage consistency), not on finite predictive rank; finite rank
  needed only for compactness/SEC (F's B8).
- threads/K/RESULT.md — K∞-R: transitivity DERIVABLE in affine dimension 3 (drive forces an ellipsoid); FALSE in
  dimension ≥ 4; dimension ≤ 2 vacuous; sourcing OPEN (`elementaryDrivability_of_substratum`); dimension 3 cannot be
  taken from NB-1 (circular).
- threads/L/RESULT.md + OrbitGeneration.lean (draft, not kernel-checked) — the reduced theorem needs P1 (sharp, with a
  0 value), V4′, K∞-R (literal transitivity/COVER) and a fourth premise G-AUT; body literally ball3 in those
  coordinates; index set Σb²=1.
- Background: threads/F/LEDGER.md, G/REPORT.md, H/RESULT.md and their CHARTER dispositions.

Tasks:
1. Forward implication: assemble the full chain from OI premises to the final target that consumes
   `lorentz_of_effects` (NativeGateBall.lean:105) and onward through NB-1 to whatever the corpus states as the final
   reconstruction target (find it: ROADMAP, Main.md, NB-1 round record, KINF-2 record). List EVERY assumption on the
   chain, each tagged: landed kernel theorem / conditional on a named open item (SC∞, V4′-gen, drive sourcing,
   dimension-3 sourcing, G-AUT, coordinates/body identification, finite rank, D3) / unidentified gap.
   In particular identify the remaining assumptions between `lorentz_of_effects` and the final target.
2. Coordinate/identification gap: L requires the body to be literally ball3 in the coordinates of r and G; K gives an
   ellipsoid. Decide whether the affine normalization ellipsoid → ball3 is free (written + exact) or hides a premise.
3. Dimension-3 sourcing: K says it cannot come from NB-1. Find whether anything landed fixes the two-level body's
   affine dimension non-circularly; else name it.
4. Reverse implication: verify that in the matrix/quantum model (QuantumArchitecture, genTheory_qm_of_quantumArchitecture
   SubstratumSource.lean:136, fullClass) every forward premise holds, in particular that V4′-gen is discharged
   automatically there (and G-AUT, SC∞, transitivity, dimension 3) — kernel identifiers where they exist, written
   otherwise. Flag any forward premise that FAILS in the quantum model (that would be a fatal overreach).
5. Deliverable: a dependency graph (text/mermaid), the full premise table, the minimal set of open items whose proof
   (or adoption as named premises) closes the equivalence, and a recommended order of formal rounds.

Limits: threads/COMMON-LIMITS.md applies, except item 8 is replaced by: you MAY read threads I–L outputs (that is your
job), but must re-verify every claim you rely on. Do not launch formal rounds; do not edit the repo.
