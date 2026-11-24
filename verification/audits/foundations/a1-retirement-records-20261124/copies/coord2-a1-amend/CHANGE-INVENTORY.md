# Proposed change inventory: A1 plan amendment (provisional)

**Status.** Provisional. This inventory is paper-only and authorizes nothing (see PROPOSAL.md sec. 0). It depends on
the final tool design being adopted and its implementation verified. Placeholders are written `<…>`.

Every change below is written as a change to the plan's record directory
`verification/audits/foundations/a1exit-deletion-20261121/` on the plan branch, made in commits after `P`
(`4c79be642ca631573f06b444903be75ec4f5e2b6`), which stays unchanged.

Reason codes:

- ESC-n: the Q10 escalation the change resolves.
- PDEP: the dependency on `P`.
- P1–P8: the plan items of the v6.0c inventory, table 6.
- PROC: procedure needed for §A.42.

## A. PREREG.md (append only; diff `diffs/PREREG-append-s32.diff`, against `P`'s PREREG sha256 `bc05340f…e928`)

| Section | Content | Reason |
|---|---|---|
| §32 heading and preamble | Quotes owner decision c.7093128173, with author and time. Placeholders for the owner decision authorizing the amendment and for the Q10 closure record. Goal link. Order rule (append only; earlier text governs nothing that §32 restates). | §A.42 item 7; P1 |
| §32.1 Unchanged | `H`, ledger, edits, checkers, fixture and §31.31 digests are unchanged. T0′ and T1′ of `P` are evidence of what they tested, and are not evidence for §32.6. | owner instruction; c.7093128173 |
| §32.2 The tool and the configuration | `T`. The configuration's path and the fields it carries (`tool`, `repository_id`, `records` holding records and reviews only, P artifacts read at `F`). Its review record. The pinned workflow's steps and inputs. Pins. | P4, P8, PDEP |
| §32.3 The designation of F | Quoted in the execution note and in the landing record. Not read by the tool. | P2 |
| §32.4 The checks of §11 as tool commands | The invocation with `--freeze F --config F:…/retirement-config.json --out`. A table for items 1–14, with item 7 open. The acceptance predicate. | P3 |
| §32.5 The records and their support from main | The table for w1-w2 v2, register-infinity-params-v1, repo-scope-v1 and gr58-v1, classified under §A.42 item 8. The review requirement. | ESC-1–ESC-4 |
| §32.6 Trials and the pre-freeze gate | The gate is re-run. T0″ and T1″ are built as in §31.8 from the candidate head. One dispatch of the tool workflow over T1″. Owner approval for each push and dispatch. | consequences (PROPOSAL sec. 6) |
| §32.7 Reachability from main and the landing | `T` is on `main` before `F`. The plan PR is merged by a merge commit after `F` and before `L`. A post-`F` side-change class for the plan directory at `M`. No freeze-ledger append and no form comment. | PROC, P5, P8 |
| §32.8 Verification status | Evidence level, what is missing, the accountable Issue | §A.46 item 4 |
| §32.9 Record pins (new last subsection) | The six `PINNED` digests, unchanged from §31.31. Added: `retirement-config.json`, `review-retirement-config-v1.json`, `w1-w2-allow-v2.json` and the review records, as `<SHA256>` until written. | P8; `preserve_check` and the tool read the last subsection |
| §32.10 Open for the owner | Item 7 | acceptance criterion (O-1) |

No line of §0–§31 changes. The Record-pins subsections §26.4 and §31.11 to §31.31 are unchanged.

## B. New files in the plan's record directory (frozen with F)

| File | Content | Reason |
|---|---|---|
| `retirement-config.json` | The staged draft (sha256 `75558ee3…`) with the changes in table C (`diffs/retirement-config.json.proposed`) | P4, P8, PDEP, ESC-1 |
| `review-retirement-config-v1.json` | Written by a non-author reviewer. Covers every field, `tool.workflow` included. | P8 (design sec. 6.3) |
| `w1-w2-allow-v2.json` | v1 with the changes in table D (`diffs/w1-w2-allow-v2.json.proposed`, `diffs/ESC1-w1-w2-allow-v1-to-v2.diff`) | ESC-1 |
| `review-w1-w2-allow-v2.json` | Review of v2. No widening review, because v1 to v2 is not widening. | ESC-1 (the one review this proposal adds) |
| `review-w1-w2-allow-v1.json`, `widening-review-w1-w2-allow-v1.json` | v1 as the predecessor. Needed for v1 in any case, since a first allow-rule file is widening. | existing requirement |
| `review-dr-deny-v1.json`, `review-resid-v1.json`, `review-register-infinity-params-v1.json`, `review-repo-scope-v1.json`, `review-side-change-classes-v1.json`, `review-gr58-hit-classification-v1.json` | Ordinary reviews. The repo-scope review is done against `edits_check.py` at `F` (ESC-3). The gr58 review re-derives the line from `H` plus D040 and D041 (ESC-4). The params review checks against the checker at `F` (ESC-2). | existing requirement; method set by ESC-2/3/4 |

The final set of review records is whatever the adopted tool's chain requires (for example, whether the delegation
contract and controls file each need one). This list is indicative.

## C. `retirement-config.json`: field-by-field, against the staged draft (diff `diffs/CONFIG-staged-draft-to-proposed.diff`)

| Field | Staged draft | Proposed | Reason |
|---|---|---|---|
| `notes` | "UNREVIEWED AND UNAUTHORIZED DRAFT, NOT ADMITTED. …" | removed | false at `F`; not a field of v6.0c sec. 16.2 (P4, P8) |
| `retirement.owner` | 7273571 | removed (`retirement` = `{name: "A1-EXIT", issue: "#1169"}`) | P1, P4 |
| `adapters.ledger.commit` | `4c79be64…` | removed (read at `F`) | PDEP |
| `adapters.ledger.companion[edits].commit` | `4c79be64…` | removed | PDEP |
| `adapters.ledger.companion[checker].commit` | `4c79be64…` | removed | PDEP, ESC-2 |
| `profiles[ptr].source.commit` | `4c79be64…` | `null` (read at `F`) | PDEP |
| `profiles[repo].source.commit` | `4c79be64…` | `null` | PDEP, ESC-3 |
| `profiles[register].source.commit` | `4c79be64…` | `null` | PDEP |
| `profiles[register-caps].source.commit` | `4c79be64…` | `null` | PDEP |
| `profiles[infinity].source.commit` | `4c79be64…` | `null` | PDEP |
| `rules[2]` | `…/ledger-coverage-tool-20261123/rules/w1-w2-allow-v1.json`, `0cbb97c9…b171` | `…/a1exit-deletion-20261121/w1-w2-allow-v2.json`, `<SHA256>` | ESC-1 |
| `records` | scope, side-change-classes, hit-classification | the same three entries, plus nine `kind: review` entries (table B) | P4 |
| `tool` | absent | `{files: [<entry point and every file under tools/ledger_coverage/ at T, by sha256>], workflow: {path: <pinned workflow>, blob_sha256: <…>}}` | P8 |
| `repository_id` | absent | `1156244443` | P8 |

Unchanged in the configuration: `schema`, `config_id`, `version` (1), `supersedes` (null), `roles` (`H`, `E`, record
commit `H`, `side_change_classes`), `corpus`, `adapters.ledger` adapter, module, path and blob values,
`adapters.sitemap` (commit `H`, which is on `main`), `adapters.replay`, the paths, extractors, blob hashes and
`pattern_sha256` of every profile, `checks`, the other three `rules` entries, `context_mapping`, `indicators`,
`sentence`, `hp_obligations`, `delegation`, `operations`, `controls` and `author`.

## D. `w1-w2-allow-v2.json` against v1 (sha256 `0cbb97c9…b171`)

| Field | v1 | v2 |
|---|---|---|
| `status` | "UNREVIEWED DRAFT: …" | states that it supersedes v1 and that only `recorded_at` differs |
| `supersedes` | `null` | `{path: …/ledger-coverage-tool-20261123/rules/w1-w2-allow-v1.json, blob_sha256: 0cbb97c9…b171}` |
| `recorded_at` (top level) | `14ac71b4…` (T1′) | `53c6601a…` (`H`) |
| `rules[W1-a … W2-b].recorded_at` (6 rules) | `14ac71b4…` | `53c6601a…` |
| `author` (top level) | `implementation-writer-20261123` | `<the writer of v2>` |

Unchanged: `schema`, `record_id`, and in every rule `id`, `kind`, `profiles`, `scope`, `matcher`, `context_required`,
`max_instances`, all 11 `fingerprints` (sentence and context sha256 and negative allowances), `positive_examples`,
`negative_examples`, `reason` and the rule-level `author`. This was checked mechanically by `work/make_json.py`.

## E. Procedural changes (no file)

| Step | Reason |
|---|---|
| The plan branch takes in a `main` that holds `T`, by an additive merge, before the amendment commits | PDEP (`F`'s tree must hold the tool's audit directory) |
| The gate, the review, and the owner's designation of `F` with the configuration path | P2; §A.50 items 2 and 5 |
| T0″ and T1″ built from the candidate head; `a1exit-trial-verify.yml` and `verify.yml` dispatched as in §31.8; one dispatch of the tool workflow over T1″ | c.7093128173; consequences |
| The plan PR #1477 merged into `main` by a merge commit after `F` and before `L`, outside the T0″–T1″ window | PROC (§A.42 items 2, 3 and 8) |
| A side-change class record, written after `F`, for the plan directory's paths at `M` | PROC (landing rule, V11) |

## F. Explicitly unchanged

- The commit `P` and its seven files: `PREREG.md` §0–§31 (`6931e3be…`), `edits.json`, `ledger.json`, `edits_check.py`,
  `guards_check.py`, `preserve_check.py` and `t0_jobs_44939798305.json`.
- The 399 ledgered splices in 44 files, the 401 edit records, every replacement text, scope assertion and checker
  rule, and every §11 and §31 expectation other than item 7, which is open.
- `H`, `E`, the six pinned merges and the §31.31 digests.
- T0′ (`02172b20`) and T1′ (`14ac71b4`), their branches, runs and artifacts. The T0 and T1 evidence of P\* on `main`.
- Every file of the tool landing, including the six v1 records and their README. ESC-6 is handled separately.
- Every recorded scientific value: fingerprints, matchers, examples, repo-scope lists, the gr58 classification, and
  the params values.
