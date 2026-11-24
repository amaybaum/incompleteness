# Proposed change inventory, revision 4 (provisional; paper-only; authorizes nothing)

CHANGE-INVENTORY-r3.md still applies, with the replacements below.

## A. `PREREG.md`: §32 append (`diffs-r4/PREREG-append-s32-r4.diff`; pure append on P's sha256 `bc05340f…e928`)

These sections differ from r3:

- **§32.9:** the edit table carries the r4 texts of D402 and D403. The 1/α₀ row and open item 4 are corrected. The
  A1 column wording and the non-independence sentence are added. The results record NC1–NC5.
- **§32.10:** `edits.json` `19eb79bd478275110b4ff1cd3ae2271c37574e849d45be272f53b8e75e726b4b`; `ledger.json`
  `d20495f0084f29ac5c58c5a0480be5f0ed342334381e6680e9cca58952940976`. The other four pins are unchanged.

## B. `edits.json` and `ledger.json`

There are 11 added records, D402–D412 (`diffs-r4/new-edit-records-D402-D412.json`; `diffs-r4/EDITS-P-to-r4.diff`,
additions only), and 11 added splices (`diffs-r4/LEDGER-new-splices-D402-D412.json`).

| Edit | Changed from r3? |
|---|---|
| D402 | the new text and the reason text |
| D403 | the new text and the reason text |
| D404–D412 | byte-identical |

- The 399 P splices are byte-equal.
- The `files` entries change for SM, ch09, ch19 and FULL only.
- Derived artifacts: SM.tex (sha256 `96176b43…`; its diff against T1′ is in `diffs-r4/`). FULL.tex is unchanged from
  r2 and r3.

## C. `retirement-config.json`

`diffs-r4/retirement-config-r4.json.proposed`. Its diffs are `CONFIG-r3-to-r4.diff` and
`CONFIG-staged-draft-to-r4.diff`.

- `adapters.ledger.blob_sha256` becomes `d20495f0…0976`.
- The `edits` companion's `blob_sha256` becomes `19eb79bd…6b4b`.
- Every other field is as in r3.

## D. New O-13 documents

- `O13-INVENTORY-r4.md`
- `O13-DECISION-DRAFT-r4.md`

Neither is a proposed repository file. They are inputs to the owner's decision.

## E. Unchanged

These are as in r3:

- `w1-w2-allow-v2.json`, copied to `diffs-r4/`;
- the review records;
- the side-change and reconciliation records;
- the procedure;
- item 7;
- P;
- D001–D401 and the 399 splices;
- every scientific statement outside D402–D412.
