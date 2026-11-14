# Target theorem for the OI ↔ QM equivalence: candidates, status and owner decision (2026-11-14)

Planning record for Issue #914. It adopts no premise, proves no result and changes no scientific
status; where a statement here and its cited source differ, the source governs.

## Contents

| File | What it is |
| --- | --- |
| `TARGET-THEOREM-r3.md` | The reviewed text: the two sides defined, the candidate target theorems with each direction's status and witness, the proved obstructions, what the records already decide, the residual obligations and the open questions |
| `OWNER-BRIEF-r3.md` | Plain-language summary of r3 for the owner's choice |
| `TARGET-THEOREM-r1.md`, `TARGET-THEOREM-r2.md` | Earlier revisions, kept because the reviews cite their text |
| `NOTES-r1.md` | The writer's reading list and what was not checked |
| `REVIEW-r1.md` | Non-author review of r1: REVISE |
| `RESPONSE-r1.md` | Dispositions of the review's findings and of the confirmation review's changes |
| `CONFIRM-r2.md` | Confirmation review of r2: ACCEPT WITH CHANGES; its six changes are applied in r3 |

The files are the texts as written and reviewed, unedited.

## Status of this record

- Paper-only: reading and hand reasoning. No computation was run and no Lean was built; Lean
  statements were read with their hypotheses.
- The reviews are model reviews by a non-author. They are not independent verification, not a human
  review and not an owner decision. r3 itself, which applies the confirmation review's six changes,
  has no review of its own.
- Statements about research records off `main` carry those records' own status (model-reviewed,
  not independently verified).

## Names used in the files

The files name the checkouts they were read from. They resolve as follows.

| Name in the files | Content |
| --- | --- |
| `wt-mainread` | `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` |
| `wt-bellplan` | branch `records/bell-landing-plan-868-20261114` at `a0fa2502d4b3fa525256399d8f297803684fd67e` (off `main`) |
| `wt-tune1plan` | branch `records/tune1-landing-plan-1236-20261114` at `ea9bff9c2f2f0f238db66690073868e281e43501` (off `main`) |
| `wt-3a` | branch `research/tune1-step3a-1236-20261113` at `8228b3c24e17a17f324b6779b53b04ad296b4308` (off `main`) |
| `wt-tune1src` | branch `research/tune1-sourcing-1236-20261113` at `c539a60c5081540be033e07aa4f141caa1d0014b` (off `main`) |

The off-`main` branches are provenance for the "latest findings" sections; no status in r3 rests
on them alone.

## Owner decision

Recorded on #914, comment 6875046763. The owner (`amaybaum`, 2026-11-14, in the coordinating
session) wrote: "I adopt all five decisions and the target theorem; preserve r3 now". The text
adopted, quoted from the proposal the owner relayed in the same session:

1. Target: "Extension form as the formal target; native form as the sourcing programme".
2. Exact vs approximate: "Exact as the ultimate target; approximation as a separate milestone".
3. Bell: "Separate research track, mandatory for full equivalence".
4. Complex matrices: "Allowed as a conditional mathematical input, not a physical explanation".
5. Evidence standard: "Lean for final mathematical equivalence claims; independently reviewed paper
   proofs allowed as intermediate results".

Target theorem: "Identify an independently physically justified extension of OI and a single common
substratum–observer realization such that the complete operational experiment family of the
extended model is equivalent, in both directions, to finite-system quantum mechanics." The two
directions are (⇒) OI + E ⟹ QM_fin and (⇐) QM_fin ⟹ OI + E, and "The two directions must use a
compatible model and operational interface, not unrelated constructions selected separately for
each experiment."

Neither direction is proved, and no extension E that is independently physically justified has been
identified. In the terms of r3 the decision takes the extension form (T3) as the formal target and
the native form (T5) as the sourcing programme, with the Bell clause as a separate obligation that
the full equivalence requires.
