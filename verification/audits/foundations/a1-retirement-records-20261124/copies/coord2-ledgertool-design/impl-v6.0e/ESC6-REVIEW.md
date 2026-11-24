# ESC-6: the README correction and the review of the local correction note

Writer's record (implementation of v6.0e). Not a review of the implementation.

Inputs, verified by sha256 before use and not modified:

| Input | sha256 |
|---|---|
| `coord2-q10/DISPOSITION.md` (accepted Q10 disposition) | 7ae4448024bd04256cf585b722f4b97a2a9ba3dc9b449ad40fc4865bd9345f89 |
| `coord2-q10/OWNER-DECISION-20261124.md` (final acceptance) | 39521663157964a9e227b952a32bb6cd9efed96202c647a6da5fa535754b423b |
| `impl-stage1-s1/CORRECTION-Q10.md` (the note reviewed here) | 44fb8665e7f1ab3663ed0a742e713208c6688fd458e5056abbfbe24c49830c86 |
| `impl-stage1-s1/EXACT-DELTA.md` (the S1 classifications the note corrects) | as in `impl-stage1-s1/MANIFEST.sha256` |

## 1. The README correction (landed text)

`verification/audits/foundations/ledger-coverage-tool-20261123/README.md` at the final commit replaces the S1
section "References to commits not on `main`" (one group label, "provenance only") with "References to content not
on `main` (sec. A.42 item 8)": a table with one row per reference, giving where it is, what reads it, and its
classification. Mapping to the disposition:

| README row | Disposition | Agreement |
|---|---|---|
| `T1'` in each allow rule's `recorded_at` (w1-w2) | R1: gap (per-rule `recorded_at` read by the lint and the `rule-stale` scoping), ESC-1 | same |
| `T1'` in w1-w2's top-level `recorded_at` | R1: provenance (not read) | same |
| `T1'` in dr-deny's top-level `recorded_at` | R2: provenance; ESC-5 administrative | same |
| `T1'` in resid's top-level `recorded_at` | R3: provenance; ESC-5 administrative | same |
| `P` in register-infinity's `recorded_at` and `lint.checker.commit` | R4: provenance for the record's two fields; gap for the parameters' stated equality to `P`'s checker (lint against the configuration's `checker` companion), ESC-2 | same |
| `P` in repo-scope's `source.commit` | R5: not read; gap in the record's support (agreement with `P`'s checker), ESC-3 | same |
| `T1'` in gr58's `classifications[0].tree` | R6: not read; gap (the line exists only at `T1'`), ESC-4 | same |
| control input `agents-md-at-T1p` | sec. 3.4: provenance (RT-DR3W only; no deny countercontrol names it) | same |
| "at `T1'`" case texts in `controls.json` | sec. 3.4: provenance | same |
| `T`/`P` constants of `a1_controls.py` | sec. 3.2: provenance | same |
| `a1_conformance.py`: `T1'`/`P` by import, blob 9f4fc3e8 | sec. 3.3: provenance | same |
| 86d79863 | sec. 3.3, 4: provenance; a computed identifier, not an object | same |
| `P` and `T1'` named in the README | sec. 3.1: provenance (descriptive) | same |

Differences from the disposition, all due to v6.0e and stated in the README rather than copied:

- The disposition's admission decision 1 ("authority admission", `engine/authority.py`) no longer exists. Under
  v6.0e the tool's own admission (configuration admission from `F`, execution identity) reads none of the six
  records: `cli.freeze_admission` reads only the configuration, the `PREREG.md` beside it and the files its pin table
  lists; `cli.execution_identity` reads `T`'s tool files and workflow. The README says so ("None of these references
  is read by the tool's own admission or execution identity").
- The disposition cites code by file:line at 443e871f; the README describes the reading code by function, since the
  lines moved.
- The README's own file-table rows that said "fingerprinted at T1'" and "classification of papers/GR.md:58 at T1'"
  (disposition sec. 3.1, lines 27-28, provenance) are reworded to name the commit through `recorded_at` and the
  retirement candidate, without a commit name; the full ids of `P` and `T1'` remain only in the classification
  section, where they are classified.
- New references introduced by v6.0e are classified in the README: the two action commit ids of the workflow text
  (commits of other repositories, pinned by the workflow, not content of this repository) and two fixture values
  (the fixture workflow's checkout id and the placeholder id of the refused workflow forms).
- `controls.json`'s header named design v5.1 (disposition sec. 3.4, noted, not edited). v6.0e's inventory makes
  `controls.json` a modified file (GV1-GV7, EI1-EI15 added); its header now names DESIGN-v6.0e with that file's
  sha256.

Not verified here: reachability of `P` and `T1'` from `main` (taken from the disposition, which rests on GitHub
compare reads of 2026-11-24 against `9deb6956`; this writer made no host read). Static reading plus the local runs
of this implementation; no run reads `T1'`'s objects as admission evidence.

## 2. Review of `impl-stage1-s1/CORRECTION-Q10.md` against the disposition (findings; the note is not edited)

| # | Note's statement | Finding |
|---|---|---|
| N-1 | w1-w2: "unchanged in substance: per-rule recorded_at (T1′) is read; evidence gap (ESC-1). The file-level recorded_at is not read (provenance)" | accurate (disposition R1) |
| N-2 | dr-deny, resid: EXACT-DELTA's "load-bearing (same mechanism)" is "incorrect: the T1′ citation is not read; provenance only (ESC-5, administrative)" | accurate (R2, R3, sec. 2 note R2/R3; ESC-5) |
| N-3 | register-infinity: "imprecise: the record's own P fields are not read; the lint uses the checker that the A1 configuration pins to P's edits_check.py; evidence gap (ESC-2)" | accurate (R4) |
| N-4 | repo-scope: "incorrect: `source` is never read or extracted; the engine applies only the lists; the record's claim of agreement with P's checker needs P; evidence gap in support (ESC-3)" | accurate (R5) |
| N-5 | gr58: "unchanged in substance: `tree` is not read, but the classified line exists only at T1′; evidence gap (ESC-4)" | accurate (R6) |
| N-6 | "The README's single 'provenance only' label for the group (S1 review nit N3) is incorrect for w1-w2, register-infinity, repo-scope and gr58" | accurate as a summary, with one imprecision: the disposition (sec. 3.1) finds the blanket statement accurate for the record-field reads of R4 and R5 and wrong for their claims' support; "incorrect for register-infinity, repo-scope" should read "incorrect for the support of their claims". The S1 review's nit N3 is correctly cited (`review-stage1-s1/review.md`, lines 124 and 172) |
| N-7 | "The README is to be corrected during the v5.5.10 implementation, once authorized ..." | stale: v5.5.10 and v5.5.10a were never adopted (owner decision of 2026-11-24 paused that cycle); the correction is made by the v6.0e implementation (this change), under the owner's authorization of 2026-11-24 quoted in the task ("Complete the ESC-6 README correction and review the existing local correction note"). The note's requirement "classifying every off-main reference individually per the disposition, under explicit independent review" is met by the README text; the independent review is pending |
| N-8 | "86d79863… is a computed blob id … not an existing Git object" | accurate (disposition sec. 4; owner decision point 4) |
| N-9 | "accepted as final by owner amaybaum, 2026-11-24, in session" | accurate (`OWNER-DECISION-20261124.md`, "Final acceptance") |
| N-10 | coverage of EXACT-DELTA's Q10 table | incomplete but not wrong: the note corrects the six record rows and the README label; EXACT-DELTA's rows for `a1_controls.py`, `a1_conformance.py`, `controls.json` and the README's descriptive mentions ("applied: … narrowing") are not discussed. The disposition (sec. 3.2-3.4) classifies each of them as provenance, which matches EXACT-DELTA's outcome for those rows, so no correction is missing; the note does not say so |
| N-11 | "ESC-6 stays open until the README correction and this note are both completed and reviewed" | consistent with the owner's final acceptance (point 3); after this change the README correction exists, and ESC-6 closes only on independent review of it and of this note (this record does not close it) |

Overall: the note's six classifications agree with the accepted disposition; one scheduling statement is stale (N-7)
and one summary is imprecise (N-6). Neither changes a classification.
