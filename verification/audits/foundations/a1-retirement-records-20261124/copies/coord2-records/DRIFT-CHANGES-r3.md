# Changes from `DRIFT-RECONCILIATION-PROPOSAL-r2.md` to `DRIFT-RECONCILIATION-PROPOSAL-r3.md`

- **Base.** `DRIFT-RECONCILIATION-PROPOSAL-r2.md`, sha256
  bfc6fa25ec4861d2ff927598a5a20cc5de830abd97d41e956c2f1b4aeeabc072, and its drafts in
  `records-draft/`. Both stay as written.
- **Review.** `review-r2/review-drift-r2.md`, sha256
  fb236df1712f67abd23fb50fe82cadc36c49e712a524f6c223247fb537b0435f. Verdict: ACCEPT WITH REQUIRED
  CORRECTIONS (2).
- **Instruction.** Relayed by the coordinating session on 2026-11-23: apply both corrections, and
  state the dry-run `id` and `supersedes` explicitly.

Section numbers refer to r3. No measured value from r2 changed: AGENTS.md blobs, D296's position,
§A.49, the expected `X` and `L` blobs and the PR #1553 values are all as in r2.

## Required corrections of review-r2

**1. Ledger binding.**
- Proposal: sec. 4.2 (fields), sec. 4.3 (the new paragraph "Which ledger and edit list"; R6, R8 and
  R10 reworded; new row R13), sec. 4.4 (P5 to P7, N12 to N18), sec. 5 step 3, sec. 7.
- Record: `ledger_binding`, `item_text` R6, R8, R10 and R13, `items`, `edits.git_blob`.
- Generator: `binding()`, `r13()`, the controls.

What changes:
- R3 to R10 read the ledger and edit list the configuration uses at the run.
- A new item, R13, is checked first. The run's ledger must have `base` = `H`, and the AGENTS.md
  `files` entry, the AGENTS.md splice list and the AGENTS.md edit records must equal the pinned
  canonical-JSON hashes:

  | Pinned item | sha256 |
  |---|---|
  | AGENTS.md `files` entry | 926eaa8b… |
  | AGENTS.md splice list | dd0acccd… |
  | AGENTS.md edit records | fbb374e2… |

- Otherwise the record does not apply, fails closed with `base-drift`, and needs a superseding
  record.
- Whole-blob equality of `ledger.json` and `edits.json` is reported but not required. This is the
  review's "at minimum" form. The reason, given in sec. 4.3, is that the re-freeze is expected to
  change those files elsewhere.
- **Controls in both directions:**
  - positive: P5 (ledger at `P`), P6 (an amendment elsewhere), P7 (moved path);
  - negative: N12 (D296 `new` changed), N13 (`expected_sha256`), N14 (span), N15 (an extra splice),
    N16 (edit record changed), N17 (entry removed), N18 (`base`).
- The generator ran all ten in memory: 0 mismatches.
- The new item is numbered R13, not inserted among R1-R12, so that the existing item ids keep their
  meaning.

**2. Consistent wording.**
- Proposal: sec. 4.2, sec. 4.3 R1. Record: `item_text.R1`, `main.applies_while`.
- `item_text.R1` now reads: "main resolved by git ls-remote origin refs/heads/main at each run (the
  pre-landing safeguard, F and landing)". `applies_while` names "R13 and R1-R12 ... (R13, the ledger
  binding, first)". The instruction asked for R1-R12; with R13 added by correction 1, naming every
  item is the consistent form, and the proposal says the same.

**3. Sec. 7 dry run** (instruction; review-r2 optional).
- Proposal: sec. 7. Sec. 7 now says the dry-run file keeps `id` `a1exit-recon-agents-md-1` and
  `supersedes` null, and that a real regeneration changes both.
- It adds that r3 drafts keep the r2 ids, because no draft was ever a reviewed or authorized record.

## Optional points of review-r2

| Point | Decision | Section |
|---|---|---|
| Class records: first-parent commit list | Not adopted. The blob pin fails closed already. | 9 |
| Manifest count | Corrected. `MANIFEST-r2.sha256` has 11 entries; the r2 report's "13" was wrong. | 9; this file |

## Other changes

- Sec. 0: the revision chain and the r3 scripts.
- Sec. 8: the drafts are now in `records-draft-r3/`, with new hashes.
  - The class drafts differ from r2 only in `draft_status`.
  - Sec. 7 cites the r3 class hashes.
  - The proposal's field block cites them in `side_change_classes`.

## New files (all covered by `MANIFEST-r3.sha256`)

- `DRIFT-RECONCILIATION-PROPOSAL-r3.md`
- `DRIFT-CHANGES-r3.md`
- `records-draft-r3/`:
  - `a1exit-recon-agents-md-1.json`
  - `a1exit-scc-tool-configuration-1.json`
  - `a1exit-scc-trial-workflow-1.json`
- `r3-work/`:
  - `gen_records_r3.py`
  - `gen_records_r3.M.out`
  - `gen_records_r3.Q.out`
- `r3-work/variant-pr1553-head/`: the same three record files (a dry run with PR #1553's head
  standing in for `main`)
