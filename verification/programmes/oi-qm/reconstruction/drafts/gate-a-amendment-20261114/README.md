# Gate A forward amendment for the superset target (#1169), 2026-11-14

Work in progress, published under AGENTS.md §A.43. A paper-only planning record: it proves
nothing, adopts no extension E and no sector condition C, and changes no scientific status. It
does not edit the accepted Gate A contract,
`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`, or the target-theorem
record on PR #1287.

**Authorization.** #1169, comment 6875724719 (posted from the owner's account, 2026-11-14T10:12:11Z),
which records the owner's approval of a paper-only forward amendment reconciling Gate A with the
three-part target recorded on #914, comment 6875548603. The owner confirmed in the coordinating
session that both paper-only units of that day were authorized and may continue.

## Contents

| File | What it is |
| --- | --- |
| `GATE-A-AMEND-r3.md` | The current text of the amendment |
| `GATE-A-AMEND-r3-TRACE.md` | One disposition (kept, superseded or replaced) for each of the 113 nonblank lines of `endpoints.md` at `c3b5f37a`, and the status table |
| `OWNER-QUESTIONS-r3.md` | The four open owner questions, with options and what each commits to |
| `GATE-A-AMEND-r2.md`, `GATE-A-AMEND-r2-TRACE.md` | The revision the confirmation review read |
| `GATE-A-AMEND-r1.md`, `NOTES-r1.md` | The first draft and the writer's reading list |
| `REVIEW-r1.md` | Non-author review of r1: REVISE (one blocking, sixteen should-fix findings) |
| `RESPONSE-r1.md` | Dispositions of the review's findings and of the confirmation review's changes |
| `CONFIRM-r2.md` | Confirmation review of r2: ACCEPT WITH CHANGES (one blocking change K1, K2–K5, nits N1–N4) |

## Review status, exactly

- `REVIEW-r1.md` found that the superseded obligation was correctly identified and quoted, and
  returned REVISE because the draft did not account for every line of the contract.
- r2 adds a residual clause (every line of `endpoints.md` not listed as superseded stays in force
  unchanged) and the line-by-line trace. `CONFIRM-r2.md` confirmed the clause, the full trace and
  the sixteen dispositions, and asked for five changes, the blocking one being that the sector
  statements compare only the quantum-labelled protocols, so that an access-closure obligation is
  needed.
- r3 applies K1–K5 and N1–N4, two in modified form (`RESPONSE-r1.md`). The trace changes only in the
  row for EP:51. r3 itself has not been reviewed. The reviews are non-author model reviews, not
  independent verification.

## What the amendment states

- Superseded: the class-wide display at `endpoints.md`:56–59 (every admitted OI model matches a
  quantum theory) and the forward half of `endpoints.md`:157; EP:51 partly. Every other line stays
  in force.
- Target: quantum inclusion; quantum-sector soundness and coverage with explicit quantifiers, with
  necessity as a separate, unadopted option; access closure inside the sector (S-A); confinement of
  observation to the sector (S-J); the Bell clause; gravity compatibility, with the field equations
  and #873 open.

## Names used in the files

| Name in the files | Content |
| --- | --- |
| `wt-mainread` | `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` |
| `wt-target` | branch `records/target-theorem-914-20261114` (PR #1287), off `main` |
