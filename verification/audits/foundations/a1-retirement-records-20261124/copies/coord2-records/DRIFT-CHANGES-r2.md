# Changes from `DRIFT-RECONCILIATION-PROPOSAL-r1.md` to `DRIFT-RECONCILIATION-PROPOSAL-r2.md`

- **Base.** `DRIFT-RECONCILIATION-PROPOSAL-r1.md`, sha256
  459987f565a95c3641238df0362ff401dae37bf0593e3d8f8989da240ba6c238.
- **Review.** `review-r1/review-drift-r1.md`, sha256
  3f9482d78782ea006c17a2c75c85523fc800607aea36f28fa277cba02b2100b4. Verdict: ACCEPT WITH REQUIRED
  CORRECTIONS (4).
- **Instruction.** The owner-authorized continuation relayed by the coordinating session on
  2026-11-23: draft the three records, and state for each whether a merge of PR #1553 requires its
  regeneration.

Section numbers below refer to r2. Sections 1 to 3 are r1's, changed only where listed.

## Required corrections of review-r1

**1. Record location for the pre-landing safeguard.** Sections changed: 4.1 (new), 5 (steps 1-3),
4.4 N8.

- The review's in-design option is adopted. The records, with their reviews and authorizations, are
  files in the tool's audit directory (sec. 6.3, sec. 12.1), with a placeholder directory name.
- They land with the tool as part of its landing commit.
- The pre-landing RT-L2 reads them from the object store in the tree of the predicted `M`.
- `retirement-config.json` at `F` references the same `{path, blob_sha256}`.
- Moving a record requires a new authorization, and a changed record is a new record with
  `supersedes`. N8 gains a relocation case.
- **Consequence also applied.** A record authorized before the tool lands cannot name `M_F`. In r2
  it names `main.computed_at` and is bound by blobs and by the first-parent commits that change
  `AGENTS.md`; it is re-checked at every run. R1 is reworded accordingly, and the record no longer
  carries a full list of changed paths, since R11 evaluates that at run time (sec. 4.2).

**2. N4's outcome.** Section changed: 4.4. N4 now expects FAIL `landing-conflict-unresolved`, the
v2 sec. 13.2 "both changed" branch, and explains why `landing-drops-main-change` does not apply. N0
and N5 name the same rule id.

**3. Blob ids.** Sections changed: 1.2, 3.1, 4.2 (table), 4.3 R7/R8, 4.4 P1/P2/N4, 7.

- "cannot name blob ids" becomes "cannot name commit ids".
- The `AGENTS.md` git blob ids are stated for each tree:

  | Tree | git blob id |
  |---|---|
  | `X` | 9f4fc3e8..., equal to `T1'`'s |
  | expected `L` at `M` | 4075b78a... |
  | `main` with #1553 merged | 2503bb8d... |
  | expected `L` with #1553 merged | 3ce53ebb... |

  Each is computed in memory, with no object written, and agrees with `rv1_blobids.out`.

**4. Stage 1 expectation.** Section changed: 5 (table). The tool's own landing paths are listed as
REVIEW `side-change-unclassified`, together with any draft records placed there as fixtures, which
are FAIL `record-invalid` (N11).

## Optional points of review-r1 (all adopted)

| Point | Sections changed |
|---|---|
| Self-reference of the tool-landing class record (it must exclude record files, which are matched by the configuration's `records` list instead) | 9; 5 step 1 |
| R11 names the plan amendment's paths; the note on `R`'s tree | 4.3 |
| Distinct reported form of reconciled drift, never `base-drift` | 4.3; 4.4 P3; 5 step 2 |
| PR #1553's current head beside the stale description head | 0 (symbol table); 6 |

## Instruction items

| Item | Sections and files |
|---|---|
| Draft records with every field filled from git objects, owner-authorization placeholders, marked as drafts inside, field names to be reconciled with the implemented schema, sha256 given | 8; `records-draft/a1exit-recon-agents-md-1.json`, `records-draft/a1exit-scc-tool-configuration-1.json`, `records-draft/a1exit-scc-trial-workflow-1.json`; generator `r2-work/gen_records_r2.py` |
| For each record, whether merging PR #1553 requires regeneration, which fields change, and the new values | 7; `r2-work/variant-pr1553-head/`, `r2-work/gen_records_r2.Q.out` |

## Other changes

- Sec. 0 is rewritten for r2: the revision chain, the review, the continuation and its limits, the
  scripts, and `Q` as a symbol.
- Sec. 2: one class record with two items becomes **two class records**, one per class, as
  instructed.
- Sec. 6: the per-record regeneration analysis moves to sec. 7.
- Sec. 10 ("does not do") is r1's sec. 7 with the drafts and their status added.
- Section 2 and 3 headings now say "review-records correction(s)", to keep them apart from
  review-r1's corrections.
