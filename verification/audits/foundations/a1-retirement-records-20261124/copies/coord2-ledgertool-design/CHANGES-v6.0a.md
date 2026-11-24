# DESIGN-v6.0a: bounded correction of DESIGN-v6.0

## Inputs and scope

Verified by sha256 before use, unchanged by this work:

- `DESIGN-v6.0.md` (draft, base): 5d4ddf784164c496d98b3194030524b20353cfcd5695fbf102eae68ced85e145
- `review-v6.0/review.md` (independent, REJECT on B-1 to B-4; nits N-1 to N-7): 43cfe728198588eb4f01a38dd817f4d207e50494bb98c5bb20c895df4fddb0ec
- `DESIGN-v5.5.9.md` (adopted): cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9

Owner decision of 2026-11-24 (owner `amaybaum`, relayed by the coordinating session; quoted in the
design's "Status and authority"). "Owner item n" is its item n. Paper-only: no repository file,
commit, push, GitHub write, GraphQL call or CI run. Built by exact, once-only replacements
(`work-v60a/apply_a.py`; text parts in `work-v60a/parts/`; row edits in `work-v60a/rows.py`).

New identifiers: EI1-EI5. TR15 and TR50 return with their v5.5.9 meaning (v6.0, unadopted, had
retired them); the pins they compare against are now held by the configuration at `F`. TR28, TR48
and TR52 return to their v5.5.9 meaning against the same pins; v6.0's checkout case of TR28 moves to
the new EI1, so no id changes meaning against v5.5.9. No id is renumbered or reused with another
meaning; no id introduced by the unadopted drafts v5.5.10 and v5.5.10a is used.

## Size

| Diff | Hunks | Lines removed | Lines added | Lines |
|---|---|---|---|---|
| `CHANGES-v6.0a-from-v6.0.diff` | 29 | 101 | 176 | 2887 -> 2957 |
| `CHANGES-v6.0a-from-v5.5.9.diff` | 44 | 518 | 399 | 3152 -> 2957 |

## Hunks (v6.0 line numbers)

| # | Hunk | v6.0 lines | Location | Change | Source |
|---|---|---|---|---|---|
| 1 | `@@ -1,15 +1,36 @@` | 1-15 | title; Status | "v6.0" -> "v6.0a"; new v6.0a bullet quoting the review and the owner decision; v6.0 bullet refers to `INVENTORY-v6.0a.md` and the v5.5.9 diff | owner items 1-6 |
| 2 | `@@ -37,16 +58,14 @@` | 41-50 | Status, "What the tool verifies" | shortened; names the tool and workflow pins, repository and event; points to the one normative sentence (sec. 1) and the class-meaning table | B-4, N-4, B-1, B-2 |
| 3 | `@@ -77,7 +96,9 @@` | 79-80 | Status, identifiers | EI1-EI5 added; TR15, TR50 restored | owner item 1 |
| 4 | `@@ -155,7 +176,7 @@` | 157 | 0.2 lead | `INVENTORY-v6.0a.md` | traceability |
| 5 | `@@ -214,11 +235,12 @@` | 217, 221 | 0.2 rows | V3/R-D3 row names the `tool` pins and TR15, TR50, EI1, EI2; new row for the v6.0 review | traceability |
| 6 | `@@ -390,8 +412,9 @@` | 391-394 | sec. 1, "Approval is outside the tool" | the single normative no-approval sentence | N-4 (one statement), B-4 |
| 7 | `@@ -762,26 +785,24 @@` | 763-784 | sec. 5, acceptance predicate | tool blobs equal the configuration's `tool` pins; repository and head repository ids equal `repository_id`; event `push` or `workflow_dispatch`; workflow blob; "or another workflow"; EI3 named; the "This predicate is technical" paragraph removed | B-1, B-2, N-1, N-4 |
| 8 | `@@ -878,6 +899,23 @@` | after 880 | sec. 5, "Class meanings" | fixed `class_meaning` table; explanations quote it; technical terms only; no text-lint control | B-4; owner item 2 |
| 9 | `@@ -1113,14 +1151,14 @@` | 1116-1123 | sec. 6.2 step 3 | "approved text / location / sentence" -> "fingerprinted" | N-3 |
| 10 | `@@ -1139,7 +1177,7 @@` | 1142 | sec. 6.2, location | "approved text and its approved neighbours" -> "fingerprinted" | N-3 |
| 11 | `@@ -1202,8 +1240,8 @@` | 1205-1206 | 6.3, owner approval | duplicate "no tool output states or implies it" removed | N-4 |
| 12 | `@@ -1247,48 +1285,60 @@` | 1250-1294 | 6.3, configuration admission and execution identity | `--pin-table` and `--config-sha256` removed; pin table derived from the `PREREG.md` beside the configuration, last `Record pins` subsection, refusals stated; execution identity: run record with head repository and event, `repository_id`, event rule, `tool.files` and `tool.workflow` pins, consumer repeats against the configuration at `F`; on-`main` stated as not checked | B-3, N-4, B-1, B-2 |
| 13 | `@@ -1328,8 +1378,8 @@` | 1331-1332 | 6.3 snapshot | head repository id, event; tool blob hashes | B-1, B-2 |
| 14 | `@@ -1347,16 +1397,15 @@` | 1350, 1357-1360 | 6.3 snapshot; residual trust | "It records no approval" removed; trusted run fields include head repository and event | N-4; B-2 |
| 15 | `@@ -1682,7 +1731,9 @@` | 1685 | 7.2 host-run classes | one clause: event `push` or `workflow_dispatch`, repository and head repository ids equal `repository_id` | N-6 (one-clause change consistent with B-1) |
| 16 | `@@ -1884,11 +1935,12 @@` | 1887-1891 | sec. 10, retired identifiers | TR15, TR50 leave the retired list; EI1-EI5 named; `INVENTORY-v6.0a.md` | owner item 1 |
| 17 | `@@ -1994,7 +2046,7 @@` | 1998 | X10 | engine blob against the configuration's `tool` pin | B-1 |
| 18 | `@@ -2048,34 +2100,36 @@` | 2051-2077 | WB3-WB8, WB13-WB15; TR2, TR5, TR13, TR14; TR15 inserted; TR28, TR48; TR50 inserted; TR52 | WB: wording; TR2: derived pin table, no `--config-sha256`; TR5: positive control with pins, repository, event; TR13: point renumbered; TR14: fork `pull_request` case, `repository_id`, tool and consumer; TR15, TR50 restored; TR28, TR48, TR52: against `tool.files` | N-3; B-3, N-4; B-1; B-2; B-1 |
| 19 | `@@ -2105,12 +2159,17 @@` | after 2111 | 10.4 | EI1 (checkout), EI2 (event), EI3 (`F`, pin table, configuration path differ from the landing record), EI4 (second `PREREG.md`, no pin-table argument, earlier subsection, missing or malformed), EI5 (`git ls-remote` failures) | B-1, N-1, B-3, N-2; owner items 1, 3 |
| 20 | `@@ -2365,6 +2424,9 @@` | after 2367 | 13.4 | `git ls-remote` failure handling refuses the landing | N-2; owner item 3 |
| 21 | `@@ -2560,8 +2622,8 @@` | 2562-2563 | sec. 15 item 10 | review of v6.0a against v6.0 and v5.5.9; `INVENTORY-v6.0a.md` | owner item 6 |
| 22 | `@@ -2569,8 +2631,9 @@` | 2571-2573 | sec. 15 item 12 | the plan's frozen configuration carries the `tool` pins and `repository_id`, beside the `PREREG.md` that lists it | owner item 4 |
| 23 | `@@ -2677,7 +2740,7 @@` | 2680 | 16.2 `retirement` | owner login removed | N-4 |
| 24 | `@@ -2692,6 +2755,8 @@` | after 2696 | 16.2 fields | `tool`, `repository_id` | B-1, B-2 |
| 25 | `@@ -2712,7 +2777,9 @@` | 2715-2716 | 16.2 lint | `tool.files` paths; `repository_id` integer | B-1, B-2 |
| 26 | `@@ -2738,6 +2805,7 @@` | after 2740 | 16.2 widening | any change to `tool` or `repository_id` is widening | B-1, B-2 |
| 27 | `@@ -2796,6 +2864,7 @@` | before 2799 | 16.4 | the tool pins and repository id go to `tool`, `repository_id` | B-1, B-2 |
| 28 | `@@ -2875,7 +2944,8 @@` | 2878 | 16.7 | run repository, head repository, event; tool blobs equal their pins | B-1, B-2 |
| 29 | `@@ -2884,4 +2954,4 @@` | 2886 | S13 | TR13-TR15, TR50-TR52, EI1-EI5 | owner item 1 |

## Row changes

Compared by script (every table row keyed by its first cell).

Against v6.0: changed X10, WB3-WB8, WB13-WB15, TR2, TR5, TR13, TR14, TR28, TR48, TR52, the 16.2
`retirement` row and S13; added TR15, TR50, EI1-EI5, the 16.2 `tool` and `repository_id` rows, the
16.4 tool-pin row, the 0.2 review row, the class-meaning table (four rows), and the reworded 0.2
V3/R-D3 row (which replaces v6.0's); none removed otherwise.

Against v5.5.9 (`INVENTORY-v6.0a.md` table 2): table rows retained 422, modified 40, removed 65,
added 18; control rows retained 186, modified 28, removed 58. Headings: 45 retained, 25 modified,
none removed. Retired control ids: O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47, TR49, TR53-TR70,
LN9, LN11, LN12.

## Expectation changes against v6.0

Each is stricter, or restores v5.5.9:

- **TR28, TR48, TR52, X10** compare against the configuration's `tool` pins (v5.5.9: `A.engine_pins`);
  CX-1 (an engine changed at an unpinned `T'`) is ERROR / non-acceptance again.
- **TR15, TR50** restored: a workflow blob other than `tool.workflow` is ERROR / non-acceptance; CX-2
  (a forged result written by a changed workflow) is refused.
- **TR14**: ERROR at the tool as in v5.5.9 (repository or head repository id differs from
  `repository_id`); the fork `pull_request` case is refused, which v6.0's expectation was false for.
- **TR2**: unchanged outcome; the pin table is now the derived one.
- **TR5**: positive control with the additional pins.
- **TR13**: cross-reference only.
- **WB rows**: wording only; outcomes unchanged.
- **EI1-EI5**: new refusals.

## Preserved

- Every removal of automated owner-authorization verification in v6.0 stands (owner item 5): no
  authority record, form, thread, comment, edit-history, freeze-ledger or GraphQL read returns, and
  no authorization record or approval field is added. `tool` and `repository_id` are technical
  identity values in the configuration at `F`, compared and recorded; they state nothing about
  approval.
- No new host read: `head_repository` and `event` are fields of the run record v6.0 already read.
- No text-lint control (owner item 2).

## Flags

- **Residual of B-3 (F-2 in the inventory).** The plan's record directory is identified by the
  configuration path, a caller input that is recorded and compared with the landing record (EI3).
  A second directory of `F` with its own `PREREG.md` and configuration would be admitted if named.
  Closing that inside the tool needs a reference value outside `F` and the caller, which is what the
  authority record was; v6.0a adds none. It is confirmed with `F` procedurally, and the plan
  amendment names the directory (P8).
- **N14** keeps "the record's approved text" (reconciliation wording, outside N-3's scope; F-10).
- **Purity value set** (F-11): the `tool.files` paths join Z9's value set in the implementation.
- Nothing else could not be implemented without additional infrastructure or without weakening a
  guarantee.
