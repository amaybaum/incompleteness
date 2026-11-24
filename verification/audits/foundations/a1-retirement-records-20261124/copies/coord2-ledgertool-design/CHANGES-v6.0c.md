# DESIGN-v6.0c: bounded correction of DESIGN-v6.0b

## Inputs and scope

Verified by sha256 before use, unchanged by this work:

- `DESIGN-v6.0b.md` (draft, base): f87dd8bee2c0a9d20beaf462351245f4735eaf056ad0485616fe391dacceb452
- `review-v6.0b/review.md` (independent, ACCEPT-WITH-NITS; Q-1, O-1, N-a to N-h, O-2, O-3): 0c41ec5aa395e7971665b156275fbffdb3fee05a283459d11a4bcf0b4a3445aa
- `review-v6.0b/probe/` (`entry_v60b.py`, `entry_v60b_fix.py`, `run_probes.sh`, `run_probes.out` and helpers), read
- `DESIGN-v5.5.9.md` (adopted): cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9

Owner decision of 2026-11-24 (owner `amaybaum`, relayed by the coordinating session; quoted in the
design's "Status and authority"): O-1 option (b), the nits, and the preserved items "verify
executable dependencies before the verification tool runs", "retain the independent consumer
checks", "preserve all scientific and technical guarantees", "do not reintroduce automated
owner-authorization verification", focused independent review. Paper-only: no repository file,
commit, push, GitHub write, GraphQL call or CI run. Built by exact, once-only replacements
(`work-v60c/apply_c.py`; parts in `work-v60c/parts/`; rows in `work-v60c/rows.py`).

New identifiers: EI8-EI14. No id is reused or changes meaning: TR29's first case keeps its v5.5.9
meaning (its tool-level ERROR returns, N-c), and EI1 and EI6 keep their cases with corrected
wording. No id of the unadopted drafts v5.5.10 and v5.5.10a is used.

## Size

Counted as every line beginning with `-` or `+` after the two diff header lines.

| Diff | Hunks | Lines removed | Lines added | Lines |
|---|---|---|---|---|
| `CHANGES-v6.0c-from-v6.0b.diff` | 14 | 39 | 100 | 3013 -> 3074 |
| `CHANGES-v6.0c-from-v5.5.9.diff` | 45 | 596 | 518 | 3152 -> 3074 |

**Correction of earlier counts (N-a).** By the same rule: v6.0b from v6.0a removes 30 lines (not 29)
and adds 86; v6.0b from v5.5.9 removes 596 (not 520) and adds 457; v6.0a from v6.0 removes 106 (not
101); v6.0a from v5.5.9 removes 594 (not 518); v6.0 from v5.5.9 removes 577 and adds 312. The earlier
counts omitted removed or added lines whose text begins with `-` or `+`. `CHANGES-v6.0a.md` and
`CHANGES-v6.0b.md` are kept unchanged as records.

## Hunks (v6.0b line numbers)

| # | Hunk | v6.0b lines | Location | Change | Source |
|---|---|---|---|---|---|
| 1 | `@@ -1,9 +1,32 @@` | 1, 7 | title; Status | "v6.0b" -> "v6.0c"; v6.0c bullet quoting the review and the owner decision | owner decision |
| 2 | `@@ -25,11 +48,7 @@` | 28-32 | Status, v6.0b bullet | its authority sentence and inventory pointer move into the v6.0c bullet | traceability |
| 3 | `@@ -120,8 +139,8 @@` | 123-124 | Status, identifiers | EI8-EI14 | owner decision |
| 4 | `@@ -199,7 +218,7 @@` | 202 | 0.2 lead | `INVENTORY-v6.0c.md` | traceability |
| 5 | `@@ -265,6 +284,7 @@` | after 267 | 0.2 | row for review v6.0b | traceability |
| 6 | `@@ -799,7 +819,8 @@` | 800-802 | sec. 5, wrapper | isolation check precedes every import not loaded at interpreter start | N-g |
| 7 | `@@ -817,7 +838,7 @@` | 820 | sec. 5, predicate | the consumer repeats points 1-3, the `uses:` check of point 5, and point 6 | N-d |
| 8 | `@@ -1364,27 +1385,60 @@` | 1367-1389 | 6.3 execution identity points 5-6 | point 5 scoped to every run of the pinned workflow; delegated checker runs excluded; the pre-run pin check (inline `python3 -I -S -B -c` step from the workflow text, `F` fetched by full id, configuration read with `git cat-file`, `os.lstat` without following links, regular files and directories only, exact path set, sha256 pins, failure ends the job before the entry point); import-path sentence true given the pre-run check; isolation check before the first import; workflow executes only the pre-run check, entry point, fixed `git` commands and named pinned actions; fail-closed `uses:` line rule; review checklist; point 6: ERROR at the tool unless `head_branch` is `main` | O-1 (b), Q-1, N-b, N-c, N-g, N-h; owner "verify executable dependencies before the tool runs" |
| 9 | `@@ -1988,9 +2042,9 @@` | 1991-1993 | sec. 10 lead | `INVENTORY-v6.0c.md`; EI1-EI14 | traceability |
| 10 | `@@ -2173,7 +2227,7 @@` | 2176 | TR29 | first case: ERROR at the tool (`head_branch`) and non-acceptance at the consumer | N-c |
| 11 | `@@ -2210,13 +2264,20 @@` | 2213, 2218, after 2219 | EI1; EI6; EI8-EI14 | EI1 scoped to a direct run of the tool, the pre-run check failing first in the workflow; EI6 second case "before any import of a module not already loaded"; EI8 clean tree passes; EI9 (P4 bytecode), EI10 (P7 extension), EI11 (P9 symlink), EI12 (P10 symlinked entry point), EI13 (changed, missing, extra or non-regular files; `F` or configuration missing) fail before the entry point; EI14 (CX-3 tree) | O-1 (b), N-e, N-g; owner "retain the independent consumer checks" (EI1, EI14 name the consumer refusals) |
| 12 | `@@ -2677,8 +2738,8 @@` | 2680-2681 | sec. 15 item 10 | focused independent review of v6.0c; `INVENTORY-v6.0c.md` | owner decision |
| 13 | `@@ -2686,10 +2747,10 @@` | 2689-2691 | sec. 15 item 12 | the plan's workflow includes the pre-run pin check | plan item P8 |
| 14 | `@@ -3010,4 +3071,4 @@` | 3013 | S13 | EI1-EI14 | owner decision |

N-e (stale EI1-EI5 references and control-runner assignment) and N-f (G23a disposition) are applied in
`INVENTORY-v6.0c.md` tables 1a, 2, 3b, 3c, 3d and 4. O-2 and O-3 are recorded unchanged as open items
in table 7.

## Row changes

Against v6.0b (rows keyed by first cell): changed TR29, EI1, EI6, S13; added EI8-EI14 and the 0.2
row for review v6.0b; none removed.

Against v5.5.9 (`INVENTORY-v6.0c.md` table 2): table rows retained 422, modified 40, removed 65,
added 29; control rows retained 186, modified 28, removed 58. Headings: 45 retained, 25 modified,
none removed. Retired control ids are unchanged: O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47,
TR49, TR53-TR70, LN9, LN11, LN12.

## Expectation changes against v6.0b

All are stricter or wording only:

- **EI9-EI13**: the P4, P7, P9 and P10 trees and changed, missing, extra or non-regular tool files
  now fail before any tool code runs (v6.0b: the code ran, and the consumer refused).
- **TR29**: a run off `main` is ERROR at the tool as well as non-acceptance at the consumer.
- **EI14**: the CX-3 tree is refused at the tool by TR29; the file never executes (EI6).
- **EI1, EI6**: wording (scope and ordering); outcomes unchanged.

## Choices stated

- **Entry-point package scan (review Q-1's optional hardening): not included.** The pre-run check
  covers the same entries (bytecode, extension modules, symlinks, extra files) before any tool code
  runs; a second scan would be a second mechanism.
- **N-c: the tool-level ERROR is restored**, using the run record's `head_branch`, a field point 1
  already reads; no new host read and no run-time `ls-remote`.
- **Pre-run check scope:** the entry point and `tools/ledger_coverage/`. The CX-3 file outside them is
  handled by isolation (EI6) and by TR29 (EI14); widening the scope to `tools/` would refuse the
  repository's other tools.

## Preserved

- No automated owner-authorization verification returns; the pre-run check compares files with the
  configuration's pins, a technical comparison.
- The independent consumer checks (point 4, TR28, TR51, TR52, TR29) are unchanged.
- No new host read and no new trust root: the pre-run check's program is part of the pinned workflow
  blob.

## Flags

- **F-16** (CX-3 tree passes the pre-run check; refused by TR29, never executed), **F-17** (no
  entry-point scan), **F-18** (`head_branch` is host-attested; the consumer's walk binds), **F-19**
  (a run without `F` and the configuration path fails the pre-run check; `workflow_dispatch`-only is
  left to the workflow's review), **F-20** (corrected counts). Details in `INVENTORY-v6.0c.md`
  table 7.
- Nothing else could not be implemented without additional infrastructure or without weakening a
  guarantee.
