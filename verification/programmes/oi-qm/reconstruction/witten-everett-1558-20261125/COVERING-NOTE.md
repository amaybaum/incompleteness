# #1558: covering note for the comparison report (for independent scientific review)

This note is separate from `REPORT.md` and changes nothing in it. `REPORT.md` is preserved byte for byte as the
coordinating session saved it: SHA-256 `27829dd218fc7afc860a1d05224d9644868f6ae081751ec9de1dd7f8b57c4743`, 531 lines.

## Status

Paper-only research record, unreviewed. It establishes no claim, adopts no premise, proposes no manuscript change and
authorizes nothing. It is preserved for independent scientific review, not for merge.

Owner decisions (amaybaum, 2026-11-25, coordinating session):
- "Let's investigate 1558 in parallel."
- "Proceed with option 1. Preserve the complete report, including §5.4 and §8, byte for byte on a dedicated research
  branch, and provide its exact commit and full SHA-256 for independent scientific review. Keep the covering summary
  separate. Explicitly record that sections B and parts of D of the updated #1558 remain unassessed." The same decision
  defers the proposed structural resolution of the quantum measurement problem until this review is complete and
  authorizes no §9 addendum, manuscript correction, premise change, successor investigation or merge.

## Provenance

- Written by a read-only investigation agent of the coordinating session, as text; saved verbatim by the coordinating
  session. §5.4 (observation versus knowledge) and §8 (addendum on the owner's scrutiny points) were requested by the
  owner after the first version and inserted verbatim. The report's opening "Covering summary" is the agent's summary,
  with one inserted note by the coordinating session (marked "Note (owner's scrutiny, §8)") that points to §8's
  revised Track 2 verdict; the earlier verdicts are kept as given.
- OI corpus pinned at `e2e2a623265187a28ebec604ab8bcc672742888f` (merge of #1557), read from the pinned objects.
- External sources retrieved: Witten arXiv:2610.04804v1 (W26), arXiv:2303.02837v2 (W23), Chandrasekaran-Longo-Penington-
  Witten arXiv:2206.10780v5 (CLPW; §§1, 2.5, 2.6, 3 read, §§4-5 and appendices not read in full). Not retrieved: Everett
  1957, Witten arXiv:2308.03663, Wall, Bousso, Blommaert et al., the IAS talk of 16 March 2026. Items marked
  [background] were not verified against a retrieved source.
- Lean identifiers were read in the pinned source; no Lean build was run. The investigation ran no computation.

## Scope against the updated #1558

The report was written before #1558's body was updated on 2026-11-25. Against that updated body:
- Sections A (observational versus epistemic incompleteness) and C (dependency and obstruction checks) are addressed by
  §5.4 and §8 of the report.
- **Section B (a possible structural resolution of the quantum measurement problem) is not assessed.**
- **Parts of Section D are not assessed**: whether OI can provide a structural resolution of the definite-outcome problem,
  and whether OI currently reproduces the quantum measurement rules (Born rule, measurement basis selection,
  repeatability, observer agreement, contextuality, Bell correlations). The report touches some of these only in
  passing. Whether explaining knowledge is necessary is addressed for the structure of observation (§8.2, §8.3), not for
  measurement rules.

These remain outstanding research questions in #1558, deferred by the owner until this review is complete.

## Requested review focus (from the owner)

1. The principled separation between observational and epistemic incompleteness (§5.4, §8.2), including whether the
   counterexamples for the independence of knowledge and operational access hold, whether complete knowledge of the
   actual configuration is physically realizable by an embedded observer, and whether retained knowledge changes
   observational equivalence.
2. The physical versus epistemic interpretation of the hidden prior `μ_H` (§5.4, §8.2): whether reading it as physical
   preparation preserves every dependent result. This may be substantive, not editorial.
3. The dependency of established results on Axiom 1's first-person interpretation (§8.3), including whether removing
   that interpretation preserves the justification of the framework's starting premises, not only its theorems.
4. The distinction between an abstract hyperfinite II₁ correspondence and physically realizable quantum operations
   through admissible observer operations (§8.1, revised Track 2 verdict: unresolved).
5. The identified manuscript errors (§7, §8.4). Any correction is a separate, separately authorized correction package.

Nothing in the report or this note establishes that OI reproduces quantum mechanics, resolves the measurement problem,
derives Witten's algebra or entropy, or is endorsed by Witten.
