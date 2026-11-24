# Independent review r3: drift reconciliation proposal r3 (bounded check)

Reviewer: the same independent non-author session as review-records, review-r1 and review-r2.

This was a read-only check. I made no repository, git or GitHub writes, and I used only `git show`
on `<repo>`. My own script is `rv3_binding.py`, and its output is
`rv3_binding.out`. I did not run the writer's `r3-work` scripts.

## Inputs

All 11 entries of `coord2-records/MANIFEST-r3.sha256` verify with `sha256sum -c`.

| File | sha256 |
|---|---|
| Proposal | c16ecbb790dfc29725d1fe6d94b7dde1a402d745434926f609167b6253ad2cff |
| Changes | 7b25e75ea561db2d29a6f1126638ee5e08d6b862dc44f56603e0d2f4a220053e |
| `records-draft-r3/a1exit-recon-agents-md-1.json` | dd725be9004bc47672b90af749d204d3d70175e83d687bdd766a5e7ceb4aec19 |
| `records-draft-r3/a1exit-scc-tool-configuration-1.json` | e4895e0f9c45660178e62f2ca4618e47c4f47fd85534dd10d99f787a5531e4b5 |
| `records-draft-r3/a1exit-scc-trial-workflow-1.json` | 67561f97f4fd0236c437468e36c3ee3a5d60d69f5dbb161890357df9847b112f |

The manifest also covers the r3-work variant files.

## Verdict: ACCEPT

Both corrections from review-r2 are applied correctly. Nothing is blocking. There are two optional
points below.

***

## 1. Ledger binding (R13)

**Hashes re-derived.** I recomputed the three binding hashes from `ledger.json` and `edits.json` at
P (`4c79be64`), using the record's stated canonical rule:
`json.dumps(sort_keys=True, separators=(',',':'), ensure_ascii=False)`, UTF-8, sha256.

| Bound item | sha256 | Ids |
|---|---|---|
| AGENTS.md `files` entry | 926eaa8b21e933576422f1c7854f6cc8dd0aa178b8225e44b05067ac933dc514 | |
| AGENTS.md splice list, in ledger order | dd0acccd6566e2e5f5e6b24bd3d0e6d2527cbb33210acb5fe368d0ac2c374119 | [D296] |
| AGENTS.md edit records, in file order | fbb374e270690352e68e307a7e921fb6972b9efa03a0abcaa727ccdefa9f1395 | [D296] |

All three equal the record's values. The record's inline `value` of the files entry equals the
ledger's entry, and `ledger_base` equals the ledger's `base`, which is H. The new `edits.git_blob`
(ec384fdf…) and the `ledger.git_blob` (ba37c1cd…) are the correct blob ids of the files at P.

**Is binding only the AGENTS.md entries sufficient?** Yes.

- **The record's claims depend only on the bound data.** The claims are: D296 is unique at H and at
  `main`, the approved text, the expected X and L blobs, and §A.49 untouched. R3 to R9 compute these
  from exactly three AGENTS.md inputs: the files entry (`base_sha256`, `expected_sha256`), the
  splice list (span, `old_sha256`, `new`, `new_sha256`) and the edit records (`old`, `new`). R13
  binds all three.
- **No other part of either file carries AGENTS.md data.**
  - The ledger's other top-level keys are `schema`, `edits_sha256` and `retained_unchanged`. The
    last is [D032, D039], neither of which is in AGENTS.md.
  - No other edit record names AGENTS.md in `site` or `mirror_of`.
  - The edit list's other keys carry no per-file data.
- **R10 and R11 need no binding.** R10 reads the run's ledger for the other files and checks each
  against H. R11 checks corpus paths and classes directly. An amendment elsewhere is therefore
  checked, not trusted.
- **Whole-blob equality would be wrong here.** It would void the record for any amendment to other
  files' entries or to `edits_sha256`, which the re-freeze is expected to make. Reporting it as
  information is right.

**Do controls P5 to P7 and N12 to N18 point the right way?** Yes. I wrote my own R13 function, not
the writer's, and applied it to mutated in-memory copies of the P ledger and edit list.

| Control | Case | R13 |
|---|---|---|
| P5 | the ledger and edit list at P | holds |
| P6 | another file's splice, `edits_sha256` and another file's edit record changed | holds |
| N12 | D296 `new` changed | fails |
| N13 | `expected_sha256` changed | fails |
| N14 | span shifted | fails |
| N15 | an extra AGENTS.md splice | fails |
| N16 | D296 edit `reason` changed | fails |
| N17 | the AGENTS.md entry removed | fails |
| N18 | `base` changed | fails |

I added two controls of my own:

- Reversing the whole splice list holds, because the AGENTS.md-only order is unchanged.
- An extra AGENTS.md record added only to `edits.json` fails.

All behave as stated. Failing R13 leads to "record does not apply, `base-drift` stands", which is
fail closed. N16 is conservative: a change to `reason` alone voids the record. That is acceptable,
since a superseding record is cheap and the alternative would need a field-level exception.

P7 (a moved path) holds by construction, because R13 binds content, not paths. The configuration pins
the path, so a moved ledger is still a configuration change under its own review.

## 2. Wording fixes

Both fixes are applied.

- `item_text.R1` now reads "main resolved by git ls-remote origin refs/heads/main at each run (the
  pre-landing safeguard, F and landing)". The proposal's sec. 4.3 opening says the same.
- `main.applies_while` now reads "the record applies only if R13 and R1-R12 all hold there (R13 ...
  first)". `items` lists R1 to R13.
- `item_text` R6, R8 and R10 now say they read the run's ledger and edit list.

## 3. Sec. 7 note

Applied. Sec. 7 states that the dry-run file keeps `id` `a1exit-recon-agents-md-1` and `supersedes`
null, that it is a computation of the changed values and not a superseding record, and that a real
regeneration changes both.

## 4. Class records and the PR #1553 variant

**Class records.** A field-level diff of r2 against r3 shows that each class record differs only in
`draft_status`. Their new hashes are:

| Record | sha256 | git blob |
|---|---|---|
| tool configuration | e4895e0f… | e6f43d4d… |
| trial workflow | 67561f97… | a24eb4f8… |

The reconciliation record's `side_change_classes` cites these new values.

**Reconciliation record, r2 to r3.** The only differences are:

- the new `ledger_binding` and `edits.git_blob`;
- R13 added to `items` and `item_text`;
- the reworded `item_text` R1, R6, R8 and R10, `applies_while` and `ledger.note`;
- `draft_status`;
- the two class-record pins.

No measured value changed.

**The PR #1553 variant.** Its class records are byte-identical to the r3 drafts. Its reconciliation
record differs from the r3 draft in exactly the fields reviewed in r2, with the same values:

- `computed_at` set to Q;
- `blobs.M` 2503bb8d / 702dbf57…, 105492 bytes;
- `main_changes[1]` ending at 105492, line 1572;
- `protected` §A.49 ending at 104848, sha256 7601f051…;
- `expected.L` 3ce53ebb / b7fdda74…, 105469 bytes;
- `side_change_commits` plus 4e375f6e, 6a547791 and 47e23023.

## 5. Blocking issues

None.

***

## Optional

- **R10's count.** `unchanged_ledgered.count` is fixed at 43, but R10 now reads the run's ledger. If
  the amendment adds or removes a ledgered file, the recorded count would be stale. State that the
  count is informational at P, or that R10 checks every entry of the run's ledger whatever their
  number.
- **The manifest count attribution.** Sec. 9 and `DRIFT-CHANGES-r3.md` say "r2's report wrongly said
  13". The r2 report said that the coordinator's brief spoke of 13 files and that the manifest has
  11. The figure of 13 came from the brief, so the attribution should say so.

## Not verified

- The tool's behaviour. The tool does not exist; R13 was checked with my own reimplementation of its
  stated rule.
- The final record hashes. The drafts still change before review.
- The state of `main` and of PR #1553 since review-r2. I did not re-query GitHub for this bounded
  check.
