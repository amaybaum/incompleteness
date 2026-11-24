# DESIGN-v6.0e: completion of the v6.0d editorial correction

## Inputs and scope

Verified by sha256 before use, unchanged by this work:

- `DESIGN-v6.0d.md` (draft, base): 1927e1356c7491ff00861e963d43308232e6ee51622ff5916b4f7921d32ef923
- `review-v6.0d/review.md` (delta review, REJECT on B-1 only; nits S-1 to S-3): 19f04b053854673230a4a93b980eba7b8289cce21806a0000bbaa1ba4a807eb1
- `review-v6.0d/probe/` and `review-v6.0d/probe/wf/` (24 workflow files), read
- `DESIGN-v5.5.9.md` (adopted): cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9

Scope: the owner-approved v6.0d editorial correction (owner `amaybaum`, 2026-11-24; quoted in the
design), completed so that the R-a line rule refuses every form its text says it refuses, plus S-1
to S-3. Nothing else. Paper-only: no repository file, commit, push, GitHub write, GraphQL call or
CI run. Built by exact, once-only replacements (`work-v60e/apply_e.py`).

No new identifier. EI7 gains cases within its meaning.

## Size

Counted as every line beginning with `-` or `+` after the two diff header lines.

| Diff | Hunks | Lines removed | Lines added | Lines |
|---|---|---|---|---|
| `CHANGES-v6.0e-from-v6.0d.diff` | 9 | 12 | 22 | 3109 -> 3119 |
| `CHANGES-v6.0e-from-v5.5.9.diff` | 45 | 596 | 563 | 3152 -> 3119 |

## Hunks (v6.0d line numbers)

| # | Hunk | v6.0d lines | Location | Change | Source |
|---|---|---|---|---|---|
| 1 | `@@ -1,9 +1,15 @@` | 1, before 7 | title; Status | "v6.0d" -> "v6.0e"; v6.0e bullet naming the delta review, `CHANGES-v6.0e.md` and `INVENTORY-v6.0e.md` | traceability (S-1) |
| 2 | `@@ -12,7 +18,8 @@` | 14-15 | Status, v6.0d bullet | the owner instruction quoted in full, with "If the delta review passes, bring v6.0d for adoption." | S-3 |
| 3 | `@@ -231,7 +238,7 @@` | 234 | 0.2 lead | `INVENTORY-v6.0e.md` | S-1 |
| 4 | `@@ -1446,11 +1453,12 @@` | 1452-1456 | 6.3 point 5, `uses:` line rule | prefix "any number of `-` or `---` markers each followed by whitespace" (`^\s*((-|---)\s+)*`); value pattern "a colon followed by any whitespace and then `{`, `[`, `&`, `*` or `!`" (`:\s+[{[&*!]`) | B-1 |
| 5 | `@@ -1466,6 +1474,8 @@` | after 1468 | 6.3 point 5, checklist | inputs only through `env:`; fetch `git fetch --no-tags -- origin "$F"`; no `${{ inputs.* }}` in any `run:` line | S-2 |
| 6 | `@@ -2076,7 +2086,7 @@` | 2079 | sec. 10 lead | `INVENTORY-v6.0e.md` | S-1 |
| 7 | `@@ -2304,7 +2314,7 @@` | 2307 | EI7 | adds the B-1 forms: escaped key, flow mapping and tag after a dash and two spaces; nested dash; whole-document flow mapping after `---`; tab after the dash; tab after a colon before a flow collection | B-1 |
| 8 | `@@ -2774,7 +2784,7 @@` | 2777 | sec. 15 item 10 | `INVENTORY-v6.0e.md` | S-1 |
| 9 | `@@ -2782,7 +2792,7 @@` | 2785 | sec. 15 item 12 | `INVENTORY-v6.0e.md` | S-1 |

The `INVENTORY-v6.0c.md` citation in the v6.0c status bullet (v6.0d line 40) describes v6.0c's own
inventory and is left as it is; S-1 names lines 234, 2079, 2777 and 2785.

## Probe result (B-1)

`work-v60e/line_rule_v60e.py` implements the corrected rule from the v6.0e text, written
independently of the reviewer's `line_rule.py`: the exact `uses` form for any line containing `uses`
in any letter case; the prefix `^\s*((-|---)\s+)*` before the entry-start test; and the value
pattern `:\s+[{[&*!]`. Run over the reviewer's 24 workflows in `review-v6.0d/probe/wf/`
(`work-v60e/line_rule_v60e.out`):

- all 22 refused forms (r01-r14, r20-r27) refuse, including the seven the v6.0d text admitted
  (r20-r26: two-space dash with an escaped key, with a tab, with a flow mapping, with a tag; nested
  dash; `---` whole-document flow mapping; tab after a colon before a flow collection);
- both conforming workflows pass (c01, c02, the latter a complete pinned workflow with the pre-run
  step);
- 0 unexpected results.

## Row changes

Against v6.0d: changed EI7; none added or removed.

Against v5.5.9 (`INVENTORY-v6.0e.md` table 2): table rows retained 422, modified 40, removed 65,
added 30; control rows retained 186, modified 28, removed 58. Headings: 45 retained, 25 modified,
none removed. Retired control ids are unchanged.

## Flags

- The source of S-3's final sentence of the owner instruction is the delta review's citation; this
  writer received the instruction without it from the coordinating session.
- Nothing else could not be applied within the owner's bounds, and no guarantee is weakened.
