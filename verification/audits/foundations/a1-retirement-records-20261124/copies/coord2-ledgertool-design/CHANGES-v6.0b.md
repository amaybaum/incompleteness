# DESIGN-v6.0b: bounded correction of DESIGN-v6.0a

## Inputs and scope

Verified by sha256 before use, unchanged by this work:

- `DESIGN-v6.0a.md` (draft, base): 105db5efe8803876107e525f868051593227f0cc20f0bd2fb7600ea312113585
- `review-v6.0a/review.md` (independent, REJECT on R-1; CX-3 demonstrated, CX-4 design-level; nits N1-N6): f5f4f57b6c028f0b995984be74be0c1a799e9cd3875dc4c82097a9a0167e9f2a
- `review-v6.0a/cx3/` (`run_cx3.sh`, `hashlib_probe.py`, `run_cx3.out`), read
- `DESIGN-v5.5.9.md` (adopted): cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9

Owner decision of 2026-11-24 (owner `amaybaum`, relayed by the coordinating session; quoted in the
design's "Status and authority"). "Owner bullet n" is its n-th bullet: 1 main history, 2 workflow
dependencies and import environment, 3 the hashlib.py control, 4 the six nits, 5 removal of
authorization verification preserved, 6 fresh review. Paper-only: no repository file, commit,
push, GitHub write, GraphQL call or CI run. Built by exact, once-only replacements
(`work-v60b/apply_b.py`; parts in `work-v60b/parts/`; rows in `work-v60b/rows.py`).

New identifiers: EI6, EI7. TR29 regains its v5.5.9 first case with its v5.5.9 meaning, so its
meaning returns to v5.5.9's; no id is reused with another meaning, and no id of the unadopted
drafts v5.5.10 and v5.5.10a is used.

## Size

| Diff | Hunks | Lines removed | Lines added | Lines |
|---|---|---|---|---|
| `CHANGES-v6.0b-from-v6.0a.diff` | 18 | 29 | 86 | 2957 -> 3013 |
| `CHANGES-v6.0b-from-v5.5.9.diff` | 45 | 520 | 457 | 3152 -> 3013 |

## Hunks (v6.0a line numbers)

| # | Hunk | v6.0a lines | Location | Change | Source |
|---|---|---|---|---|---|
| 1 | `@@ -1,9 +1,35 @@` | 1, 7 | title; Status | "v6.0a" -> "v6.0b"; new v6.0b bullet quoting the review and the owner decision | owner bullets 1-6 |
| 2 | `@@ -23,14 +49,10 @@` | 26-33 | Status, v6.0a and v6.0 bullets | v6.0a's authority sentence and v6.0's inventory pointer moved into the v6.0b bullet | traceability |
| 3 | `@@ -97,8 +119,9 @@` | 100-101 | Status, identifiers | EI6, EI7; TR29's first case restored | owner bullets 1, 3 |
| 4 | `@@ -176,7 +199,7 @@` | 179 | 0.2 lead | `INVENTORY-v6.0b.md` | traceability |
| 5 | `@@ -241,6 +264,7 @@` | after 243 | 0.2 | row for review v6.0a | traceability |
| 6 | `@@ -774,7 +798,8 @@` | 776-777 | sec. 5, wrapper | the package is loaded by location after the isolation check | R-1; owner bullets 2, 3 |
| 7 | `@@ -792,7 +817,7 @@` | 795 | sec. 5, predicate | consumer repeats points 1-3, 5 and 6 | R-1 |
| 8 | `@@ -800,6 +825,7 @@` | after 802 | sec. 5, predicate | `T` on `M`'s first-parent chain (TR29) | R-1; owner bullet 1 |
| 9 | `@@ -1306,10 +1332,10 @@` | 1309-1313 | 6.3 | the owner's procedural confirmation names the configuration path with `F`; execution identity heading adds R-1 | N2 |
| 10 | `@@ -1331,14 +1357,38 @@` | 1334-1341 | 6.3 execution identity | point 4 repeats the `uses:` check; "Whether `T` lies on `main` is not checked" removed; point 5 (nothing unpinned executes: isolated interpreter, no checkout directory on `sys.path`, package loaded by location, entry-point refusal before any package import; workflow executes only the entry point and fixed `git` commands, `uses:` entries of other repositories by full commit id, no `./`, checked by the tool) and point 6 (`T` on `M`'s first-parent chain) added; no option, environment value or other field sets `tool` or `repository_id` | R-1 (CX-3, CX-4); N3, N5; owner bullets 1-3 |
| 11 | `@@ -1406,8 +1456,9 @@` | 1409-1410 | 6.3 residual trust | the runner sentence holds given point 5; interpreter and standard library of the image named | N6 |
| 12 | `@@ -1937,9 +1988,9 @@` | 1938-1939 | sec. 10 lead | EI1-EI7; `INVENTORY-v6.0b.md` | owner bullet 3; traceability |
| 13 | `@@ -2122,7 +2173,7 @@` | 2125 | TR29 | first case restored: `head_sha` not on `main`'s first-parent chain; checked at the consumer against `M` | R-1; owner bullet 1 |
| 14 | `@@ -2164,6 +2215,8 @@` | after 2166 | 10.4 | EI6 (unpinned `tools/hashlib.py` and siblings never execute; entry point refuses a non-isolated interpreter or a checkout directory on `sys.path`); EI7 (`uses:` with `./`, a tag or a branch refused) | owner bullets 2, 3; R-1; N5 |
| 15 | `@@ -2422,11 +2475,13 @@` | 2425-2429 | 13.4 | `ls-remote` against the repository `repository_id` names; the consumer then requires `T` on `M`'s chain | N4; R-1 |
| 16 | `@@ -2622,8 +2677,8 @@` | 2625-2626 | sec. 15 item 10 | review of v6.0b against v6.0a and v5.5.9; `INVENTORY-v6.0b.md` | owner bullet 6 |
| 17 | `@@ -2631,9 +2686,10 @@` | 2634-2636 | sec. 15 item 12 | the plan's pinned workflow meets point 5; `INVENTORY-v6.0b.md` | plan item P8 |
| 18 | `@@ -2954,4 +3010,4 @@` | 2957 | S13 | EI1-EI7 | owner bullet 3 |

N1 (twelve `Record pins` subsections, the last §31.31) is applied in `INVENTORY-v6.0b.md` table 6;
the design text states the derived rule and names no count.

## Row changes

Against v6.0a (rows keyed by first cell): changed TR29 and S13; added EI6, EI7 and the 0.2 row for
review v6.0a; none removed.

Against v5.5.9 (`INVENTORY-v6.0b.md` table 2): table rows retained 422, modified 40, removed 65,
added 21; control rows retained 186, modified 28, removed 58. Headings: 45 retained, 25 modified,
none removed. Retired control ids are unchanged from v6.0a: O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44,
TR47, TR49, TR53-TR70, LN9, LN11, LN12.

## Expectation changes against v6.0a

All are stricter:

- **TR29**: a run whose `head_sha` is not on `main`'s first-parent chain is refused again (v5.5.9
  meaning), at the consumer against `M` from `git ls-remote`. CX-3 and CX-4 at an off-`main` `T'`
  are thereby refused, and `T` is reachable from `main`.
- **EI6**: an unpinned `tools/hashlib.py` (the review's probe) never executes; the run is
  unaffected at the tool, and its result is not accepted unless its `T` is on `main`. This is
  fail-closed: the file cannot influence the computation because it is never on the import path,
  and the isolation precondition is checked by the pinned entry point before it imports any
  package; a run that violates the precondition stops with ERROR before any check could be patched.
- **EI7**: local actions, `./` reusable workflows and tag or branch references in `uses:` are
  refused.

## Preserved

- The removal of automated owner-authorization verification stands (owner bullet 5): no authority
  record, form, thread, comment, edit-history, freeze-ledger or GraphQL read returns. The on-`main`
  check is a fact about the object graph, read through the verified reader from `M`, which EI5
  already resolves; no host read is added.
- No new infrastructure: the import rule is the interpreter's isolated mode plus loading the
  package by location; the workflow rule is a check of `uses:` lines of a blob already read.

## Flags

- **F-14.** The workflow's run-step content rule (no step runs a checkout file other than the entry
  point) is not parsed mechanically; it is checked in the configuration's review of
  `tool.workflow`, fixed by the pin (TR15, TR50) and bounded by TR29. Parsing shell steps would be
  added infrastructure.
- **F-15.** The interpreter, standard library and installed packages of the runner image stay under
  the host-runner trust; isolated mode keeps the checkout and the environment off the import path
  but does not verify the image.
- **F-2** (record directory identified by the configuration path) stays a procedural residual,
  which review v6.0a judged acceptable; sec. 6.3 now names the configuration path in the owner's
  procedural confirmation (N2).
- Nothing else could not be implemented without additional infrastructure or without weakening a
  guarantee.
