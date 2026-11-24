# DESIGN-v6.0d: bounded editorial correction of DESIGN-v6.0c

## Inputs and scope

Verified by sha256 before use, unchanged by this work:

- `DESIGN-v6.0c.md` (draft, base): dd72ee5b9f1ed3718b5f1584bf88b957dbb481b0c9ac9dca3d6ff784389aa594
- `review-v6.0c/review.md` (focused, ACCEPT-WITH-NITS; open item O-4, nits R-a to R-e): 48dd41d0c0cc8b9169f61377eec7c606170b1fc6b7bb5c9aef0b5e7d4010ad20
- `review-v6.0c/probe/`, read
- `DESIGN-v5.5.9.md` (adopted): cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9

Owner decision of 2026-11-24 (owner `amaybaum`, relayed by the coordinating session), quoted in the
design: "Approve the bounded v6.0d editorial correction: the one-line O-4 fix and the identified
nits. Obtain a focused independent delta review against v6.0c. Do not reopen settled design
questions or introduce new requirements." Paper-only: no repository file, commit, push, GitHub
write, GraphQL call or CI run. Built by exact, once-only replacements (`work-v60d/apply_d.py`).

New identifier: EI15. No id is reused or changes meaning; EI7, EI13 and EI14 gain cases within
their meaning.

## Size

Counted as every line beginning with `-` or `+` after the two diff header lines.

| Diff | Hunks | Lines removed | Lines added | Lines |
|---|---|---|---|---|
| `CHANGES-v6.0d-from-v6.0c.diff` | 10 | 22 | 57 | 3074 -> 3109 |
| `CHANGES-v6.0d-from-v5.5.9.diff` | 45 | 596 | 553 | 3152 -> 3109 |

## Hunks (v6.0c line numbers)

| # | Hunk | v6.0c lines | Location | Change | Source |
|---|---|---|---|---|---|
| 1 | `@@ -1,9 +1,22 @@` | 1, before 7 | title; Status | "v6.0c" -> "v6.0d"; v6.0d bullet quoting the review and the owner decision | traceability |
| 2 | `@@ -140,7 +153,7 @@` | 143 | Status, identifiers | EI15 | O-4 (its control) |
| 3 | `@@ -1361,7 +1374,8 @@` | 1364 | 6.3 execution identity point 1 | the head branch listed among the fields read | R-c |
| 4 | `@@ -1392,21 +1406,29 @@` | 1395-1410 | 6.3 point 5, pre-run check | "after the checkout and the fetch of `F`"; refuse unless `GITHUB_REF` is `refs/heads/main` and `F` matches `^[0-9a-f]{40}$`; `tools` and every parent of a checked path a real directory; the step located by its name and its program extracted verbatim from its single `run:` line | O-4, R-c, R-d, R-e |
| 5 | `@@ -1418,12 +1440,22 @@` | 1421-1426 | 6.3 point 5, `uses:` rule | the line rule on raw text with no YAML parser: any line containing `uses` in another form; any entry beginning with a quote, flow collection, complex-key, anchor, alias or tag marker; any flow collection, anchor, alias or tag as a value; the rule only refuses | R-a |
| 6 | `@@ -1433,7 +1465,9 @@` | 1436 | 6.3 point 5, checklist | no `continue-on-error` and no `if:` after the pre-run check; no reusable workflow | R-b |
| 7 | `@@ -2044,7 +2078,7 @@` | 2047 | sec. 10 lead | EI1-EI15 | traceability |
| 8 | `@@ -2270,14 +2304,15 @@` | 2273, 2279, 2280 | EI7; EI13; EI14; EI15 | EI7: quoted key, escaped key `"\x75ses"`, flow mapping, flow sequence, anchor and alias, block scalar, complex key; EI13: `tools` a symlink (inside and outside the checkout); EI14: at a branch `T'` the pre-run check fails (`GITHUB_REF`); EI15 (new): branch dispatch with a caller-chosen `F'`, a tag `main`, `F` not a full lowercase id | R-a, R-d, O-4 |
| 9 | `@@ -2738,7 +2773,7 @@` | 2741 | sec. 15 item 10 | focused delta review of v6.0d against v6.0c; "the owner's requirement 5" removed | R-c; owner decision |
| 10 | `@@ -3071,4 +3106,4 @@` | 3074 | S13 | EI1-EI15 | traceability |

R-c's inventory part (table 6 row P8's description of what the workflow runs) and R-e's runner part
(table 3b) are applied in `INVENTORY-v6.0d.md`, together with F-16 and F-18 (`GITHUB_REF` removes the
tag ambiguity of `head_branch`).

**EI14 (consequence of O-4).** With the `GITHUB_REF` test, the pre-run check now fails for the CX-3
tree dispatched on a branch; EI14's expectation is updated to say so, and its on-`main` case is
unchanged. This follows from O-4 and adds no requirement.

## Row changes

Against v6.0c: changed EI7, EI13, EI14, S13; added EI15; none removed.

Against v5.5.9 (`INVENTORY-v6.0d.md` table 2): table rows retained 422, modified 40, removed 65,
added 30; control rows retained 186, modified 28, removed 58. Headings: 45 retained, 25 modified,
none removed. Retired control ids are unchanged.

## Flags

- **The `uses:` line rule (R-a)** refuses some YAML forms a parser would read harmlessly (for example
  a run line beginning with a quote, or a value written as a flow mapping); the pinned workflow is
  written without them. It never admits a form the text says it refuses. No YAML parser is added.
- **The pre-run program on a single `run:` line (R-e)** must avoid the line rule's refused patterns
  (for example `: {`); this is a constraint on how the workflow is written.
- Nothing else could not be implemented within the owner's bounds, and no guarantee is weakened.
