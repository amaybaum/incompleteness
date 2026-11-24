# Proposed change inventory, revision 3 (provisional; paper-only; authorizes nothing)

CHANGE-INVENTORY-r2.md still applies, with the replacements below. The source of each change is in
`CHANGES-r2-to-r3.md`.

## A. `PREREG.md`: §32 append (`diffs-r3/PREREG-append-s32-r3.diff`, against P's sha256 `bc05340f…e928`)

These sections differ from r2:

| Section | Change |
|---|---|
| preamble | the edits enter only by the owner decision quoted in §32.9, which supersedes c.7093128173's clause for them |
| §32.1 | Eleven edit records added (D402–D412) |
| §32.4 row 7 | appB:235/246 are named by LEDGER.md:304; the FULL mirrors are false positives by mirror convention |
| §32.7 | caveat on today's `main` blobs |
| §32.8 | the missing items include the scientific review of D402–D412 and the adoption decision |
| §32.9 | Rewritten. It has the adoption-decision placeholder, the edit table with D410–D412, the dependency table, "The wording", the open dependencies 1–6 and the results. |
| §32.10 | `edits.json` `1adaadb93769005bf8eb27ff82a8941359f82f20f395eeb61101a73f240f1778`; `ledger.json` `afbd4d00ce21c663bf34ef25841b1e5374372de2f70a82a835f6131693123fbd`. 410 splices in 44 files; 412 edit records. |

## B. `edits.json` and `ledger.json`

- **Edit records.** 11 are appended: D402–D409 as in r2, except that D402's and D403's new text changes; D410, D411
  and D412 are new, all at `papers/SM.md:1394`, parts 3, 4 and 5, class "needs scientific review". See
  `diffs-r3/new-edit-records-D402-D412.json` and `diffs-r3/EDITS-P-to-r3.diff`, which has additions only.
- **Splices.** 11 are added (`diffs-r3/LEDGER-new-splices-D402-D412.json`). The 399 P splices are byte-equal.
- **`files` entries.** Only SM, ch09, ch19 and FULL change.
- **Derived at execution.** SM.tex, whose expected diff against T1′ is in `diffs-r3/`. FULL.tex is unchanged from r2.
  Also the SM and FULL PDFs, and the SC-42 result. No coverage fingerprint is affected: `coverage_check` output is
  identical.

## C. `retirement-config.json` (`diffs-r3/retirement-config-r3.json.proposed`; `CONFIG-r2-to-r3.diff`; `CONFIG-staged-draft-to-r3.diff`)

As r2, plus two changes:

- `adapters.ledger.blob_sha256` → `afbd4d00…bfd`;
- `adapters.ledger.companion[edits].blob_sha256` → `1adaadb9…1778`.

## D. Other files

These are unchanged from r2:

- `w1-w2-allow-v2.json`, copied to `diffs-r3/`;
- the review records;
- the side-change and reconciliation records;
- the procedural steps.

## E. Explicitly unchanged

As r2 F:

- item 7's wording;
- P and its files;
- D001–D401 and the 399 splices;
- every scientific statement other than D402–D412.
