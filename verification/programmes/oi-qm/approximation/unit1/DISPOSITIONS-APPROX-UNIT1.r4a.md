# APPROX-UNIT1 r4a — dispositions of independent r4 nits

**Status: WIP; focused diff-only review and green ordinary CI required.** Accountable issue [#1216](https://github.com/amaybaum/incompleteness/issues/1216). Integration requires a separate owner decision.

Owner (amaybaum), current Codex instruction, 2026-11-09: apply the three editorial corrections, preserve the accepted scientific scope, require a focused diff-only check and green CI, and return the corrected artifact for integration approval. No scientific execution, freeze or merge is authorized. No new physical premise, designation or special workflow dispatch is included.

## Source identity

- Accepted r4 assessment SHA-256: `cb5c4c6a37d3a5ab321b4ad0aba464104aeed4b1d9c57c298704b376b2269b44`.
- Original r4 writer ledger SHA-256: `ef669e30e72c71e17db058081c05934abab098d4561aa60c4599a43fd982897a`; retained unchanged as a historical writer record.
- Independent full-text r4 review: `REVIEW-APPROX-UNIT1.r4.md`, SHA-256 `e2749ff93827e368d375e0329fa9f70804fb6b4099ae5114c13f894dd707cb5a`, **ACCEPT WITH NITS**, no blocking scientific findings. The report is retained unchanged.
- r4a assessment: `APPROX-UNIT1.md`, SHA-256 `e2d95d1a67e2d317062ca80b43de5ee59b52ae9ed96d7b60f3dc6c7fec318458`.
- Repository integration base: `cac5d26441dd33e9348151487e4df7b547195481`; scientific source citations remain pinned to `fd539e150759a6ea51ab279aeeac80fc06050ade`.

## Finding-to-diff map

| Finding | Correction | Assessment location | Preserved scope |
| --- | --- | --- | --- |
| N1: #945 numerical-source ambiguity | Attribute 6.9063 versus 4.0000, d=4, b=24, explicitly to assessment comment c.6567879503 §2 and its assessment-review checks R-1/R-2; remove the conflicting bracket attribution to `6d494e30`. | §2.2 precision-regime paragraph | The counterexample refutes the per-parent proof step; it does not refute the final TV bound or prove reachability. The earlier proof review's different figures remain separate. |
| N2: floating-point instances labelled exact | Add [N] for numerical floating-point instances and use it for `opglue_probes.py` checks 8–9 in A3 and D6, with their 1e−12 tolerance. Retain [P] for the paper proof and [X] for exact checks elsewhere. | §1 evidence key; §2.1 A3 evidence cell; §7 D6 | Main's theorem remains paper-proved within the same exact-ring regime. No new exact or kernel certification is claimed. |
| N3: admissibility versus availability | Remove the claim that the displayed K enters `genTheory CM` through products/blocks. State that K witnesses admissible nonmonomial FI-1 membership, is not an isometric primitive, and requires no branch-availability claim. | §4.2 CM countermodel's final bullet | FI-1 still fails to imply system-NX-1 in the same countermodel; every available branch preserves diagonals. No available native operation is added. |
| Necessary revision metadata | Identify r4a, record r4's independent verdict and the focused review/CI gate, and distinguish the original r4 no-write history from the current draft-publication instruction. | Header; §9 review status; §11 verification scope; §12 digest pointer | No scientific conclusion, source pin, probe output, physical premise or authorization for another workstream changes. |

## Focused-check brief

Compare the preserved r4 baseline with r4a, check only N1–N3 and necessary metadata, and report whether the changes preserve the independently accepted scope. Verify exact source and ledger identities. No new full scientific review is required unless the diff changes substantive claims. The existing r4 report's comparison limits and the assessment's §1.1 off-main support gaps remain; a diff acceptance does not close them for integration.

Level A remains supported only within its stated precision regimes. OI-derived Level B remains unsatisfied. Neither simulator success nor the formulation of Level B establishes full OI–QM equivalence.

No scientific program, probe, simulation or Lean build was run for this cleanup. Ordinary repository CI is a verification gate, not a new research execution or scientific acceptance.
