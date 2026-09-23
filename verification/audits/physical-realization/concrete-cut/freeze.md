# The concrete-cut freeze

`verification/C1C4-MINIMALITY-AUDIT.md` (Audit A), `verification/CONCRETE-CUT-AUDIT.md` (Audit B),
`verification/audit-census.json` and `verification/lean/audit_census_probe.py` (the census),
`verification/lean/edge_rigidity_probe.py` guards `R7-AUDA` and `R7-AUDB`.

This is not a round. It is the corrected interpretation the two audits earned, stated once, in the
form the guards enforce, so that later rounds — OI-N first, CT3 after — build on it rather than
re-deriving or quietly re-compressing it.

## The canonical table

Copied verbatim from `CONCRETE-CUT-AUDIT.md`, which is where it is guarded.

| cut | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| cosmological horizon (`[GR]` §2.2) | verified structurally | verified, timescale margin | verified, capacity margin | named, not presently discharged |
| lattice observer cut (`[SM]` Theorem 22) | structural | hypothesis | capacity floor, data processing | hypothesis |

Two rows, not one. Collapsing them into a single "verified" line for the first three conditions is
not a statement the audits earned: at the lattice cut C2 is a hypothesis and C3 is a floor for the
realized process rather than a margin. Within the
first row the entries differ in kind: C1 is verified structurally, from the constraint equations, and
carries no margin; C2 and C3 are verified with enormous margins, of timescale and of capacity
respectively.

## What is frozen, and where each statement lives

**The recurrence chain names C1.** Finiteness gives recurrence; recurrence *together with C1* gives
returns of information from hidden to visible at the recurrence timescale. The uncoupled product
system is the reason the coupling cannot be dropped, certified in `partition_coupling_probe.py`
against the corpus's own coin-and-die control. (`[Main]` §2.3, Chapter 1 §1.7, Chapter 18 §18.7.)

**C4 is the primitive, and it is not discharged at either physical cut.** `[Main]` §3.4 derives C1
and C3 from C4 in any faithful realization, so verifying those two at a cut is never evidence for
C4. At the cosmological cut C4 is a named realization condition, not presently discharged, with
what remains stated — a visible-history record written into hidden boundary degrees routed back
into future visible conditionals within the accessible window. At the lattice cut it is an explicit
hypothesis of Theorem 22, with the genericity lemma that would discharge it named and unproved.
Bidirectional coupling is a strengthened C1 and does not supply the routing; H-scramble governs
Page-curve typicality, not next-step conditionals; H-Hawking is a KMS condition. (`[GR]` §2.2,
Chapter 7 §7.2, Chapter 1 §1.2, `[SM]` §2.1 and Theorem 22.)

**C1–C4 are diagnostics of a realization, not hypotheses of the derivations.** The `ħ` calibration
depends on the cosmological-horizon partition, the partial-trace/Stinespring machinery, H-slope, and
the stated horizon, frame and KMS conditions; Layer 0 follows from the bijection's coupling structure
and cubic-group representation theory. Neither consumes any C-condition. (`[Main]` §1.3, `[GR]` §8.4,
`[SM]` §8 Layer 0, Chapter 4.)

**The OI core is forward-redundant.** `qm_implies_oiCore` is containment; `completedOI_iff_physical`
is redundancy; nothing shows a hidden sub-quantum level is required. (`OI-CORE-FORWARD-REDUNDANCY.md`.)

**The minimal-carrier machinery underwrites no manuscript statement.** `PassiveQuotient.lean` and
`ObservabilityQuotient.lean` are kernel-proved infrastructure with no ledger entry; a manuscript that
wants to lean on passive minimality writes the ledger entry and the statement first.

## How the freeze is enforced

Thirty-two census vocabularies re-run on every CI pass, failing on drift; `R7-AUDA` and `R7-AUDB`
pin the repaired forms in every parallel source, the table's five distinctive cells, and the
forbidden inferences — "any partition", "automatic at the horizon", "satisfies all four", "the full
equivalence applies in our universe", the three-condition sentence, the blanket margins, and the
Layer 0 attribution. Drift is not automatically a defect; the manifest carries the rule for
re-deciding it, and never widening a pattern to make a mismatch disappear.

## What the freeze does not claim

That C4 fails at either cut, or cannot be demonstrated there — only that the corpus does not
presently demonstrate it. That C2 fails at the lattice cut. That the `ħ` derivation, the
Bekenstein–Hawking coefficient, the running-vacuum form, or any Layer 0 result is affected: their
conditions are the ones named at their point of use, and none is a C-condition. That the two audits
exhaust the corpus: their charters fix their vocabularies, and a different charter would find
different things. That anything here bears on CT3, which stays paused behind OI-N.
