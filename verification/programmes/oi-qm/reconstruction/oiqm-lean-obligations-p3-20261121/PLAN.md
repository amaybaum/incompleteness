# OIQM-LEAN P3: plan

**Standing.** WIP / UNVERIFIED. This is a round-4 design unit for #1169 (c.7067281228). It is stacked
on #1517 at `81888955` and tracked in Issue #1505.

The unit is design only:
- no `.lean` file, no build and no computation;
- no manuscript edit and no adopted premise;
- no imported quantum operation counted as native.

**Question.** Which claims have been independently accepted since #1517, and what are precise Lean
proof obligations for each? Each obligation is stated at the layer at which its claim is proved:
- effect, instrument or accessible algebra;
- ontic or Born-form;
- typing, soundness or operational.

**Candidates** (coordinator list). Each is checked for acceptance before it is used.
- OPRES Theorem C, Proposition D and Remark D′ (#1511).
- READOUT-ALG RA-1′ for items 2, 3 and 5–10 (#1513).
- P-ST as integrated in GATE-A r5.8 (#1503).
- Lemma P and C-T (#1516).
- BQ1 (#1498).

**Acceptance check.** A candidate is used only if a review verdict of CONFIRMED or CONFIRMED WITH NITS
pins a commit on its PR, and the head named here differs from that pin by nit commits alone. The pin
and the delta are recorded. An item outside the confirmed set is excluded.

**Exclusions decided in advance.**
- Unreviewed proposals: PO-19a of #1517 §4.
- Anything whose Lean form belongs to another thread. BQ1's Lean designs belong to the BQP ladder
  (#1498, #1514), so they are cross-referenced and not restated.

**Productivity test (§A.31).** The unit is productive if both of the following hold:
1. It gives at least one obligation that #1517 does not already state, for an accepted claim. Each
   such obligation carries an exact statement, a verified kernel and Mathlib basis, a label with its
   imports as hypotheses, a difficulty and a §A.35 impact.
2. It exposes at least one place where the Lean statement must sit at a *different* layer than a
   naive reading of the claim would give.

If neither holds, the unit is a non-gem and is recorded as such.

**Outcomes allowed.**
- PRODUCTIVE.
- NON-GEM: every accepted claim is already covered by #1517.
- INCONCLUSIVE: acceptance status or layer cannot be settled from the records.

**Layer rule, applied to each obligation.** The statement names its layer. It must not be stated one
layer above where the paper claim is proved. In particular:
- an effect-level result is never typed as an instrument result;
- a Born-form statement is never typed as an ontic one;
- a typing-layer construction is never typed as soundness or as an operational result.
