# Independent review r1: drift reconciliation proposal, revision 1

Reviewer: independent non-author session, the same reviewer as `review/review-records.md`. This
review was read-only, under the owner's limits: no repository, git or GitHub writes, and no workflow
runs. It used only read-only `git show`, `git rev-parse`, `git diff` and `git log` on
`<repo>`, and `gh api` GET requests. The writer's `r1-work/` scripts were not run
or reused. Only their sha256 values were compared with the ones the proposal cites, and all four
match.

## Inputs (sha256 verified first; all match)

| Input | sha256 |
|---|---|
| `DRIFT-RECONCILIATION-PROPOSAL-r1.md` | 459987f565a95c3641238df0362ff401dae37bf0593e3d8f8989da240ba6c238 |
| `DRIFT-CHANGES-r1.md` | 118eef9ab2fa3ee5730ecdea3306e6f89b211869778ef3bf3addb25a8310e752 |
| `review/review-records.md` | 1ef18f194efa1c2055874f0ccac51ef55b902e1dcd2e6420af05859ef256a5f8 |
| `DESIGN-v5.1.md` (for sec. 6.3, 13, 16.2) | 0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe |

Objects read:

| Name | Commit |
|---|---|
| H | `53c6601a10419b6b333cc992474272501ab542af` |
| P | `4c79be642ca631573f06b444903be75ec4f5e2b6` |
| W | `413b0bb88f39cad901befcf4684355c7ee39480b` |
| M | `4fb2c1eed350edf95da2b316abcca93717246589`; `gh api` GET `git/ref/heads/main` returns this same commit |
| Q | PR #1553 head, `47e23023450fb8fcbd61b5c776a69ba61897f267` |
| T1' | `14ac71b4b0a0c0aa2d7068d6799a73f474097060` |

`DESIGN-v2.md` was also read for v2 sec. 13, which v5.1 sec. 13 keeps.

The owner decision is #1169 comment 7099655517, by `amaybaum`, at 2026-11-23T11:26:50Z. I read it with
`gh api`, and it is saved as `c7099655517.json`. It keeps H, chooses "a reconciliation record frozen
together with the re-frozen plan", and classifies the settings file as tool configuration and the
workflow as the trial workflow. It approves the approach only.

My scripts and their outputs are in this directory:

- `rv1_facts.py` / `rv1_facts.out`: the facts at H, M, Q and T1'.
- `rv1_q_added.py` / `rv1_q_added.out`: every module-level regex of `edits_check.py` at P, run on the
  lines PR #1553 adds.
- `rv1_blobids.py` / `rv1_blobids.out`: git blob ids computed in memory. No object was written.

## Verdict: ACCEPT WITH REQUIRED CORRECTIONS (4)

Every measured fact re-derives exactly. All six corrections from my earlier review are resolved. The
chosen approach is sound under the design: a record written, reviewed and owner-authorized before
`F`, and frozen with `F`. Its checks R1-R12 point the right way, and they are enough to show the three
things the owner asked for. Four points need correcting before the proposal is used as the
specification:

- where the records live in the object store for the pre-landing safeguard run;
- one control's named outcome;
- a factual claim about blob ids;
- one incomplete Stage 1 expectation.

***

## 1. My six corrections

| # | Status | Evidence |
|---|---|---|
| 1 | Resolved | Sec. 1.2 gives bytes 2332 to 2382 (end exclusive), lines 37-38, and the character offset 2305 with its reason. |
| 2 | Resolved | Sec. 1.2 states the 4-line insertion at H byte 46677, which is M bytes [46677, 47031), lines 715-718. It also states the 28-line append at M bytes [102604, 104517). "Append-only" is removed. |
| 3 | Resolved | Sec. 2 cites PREREG §31.12.7 (W as the workflow base). Both files are pinned `{path, blob_sha256}` in `roles.side_change_classes` and in the class record. Control N10 is added. |
| 4 | Resolved | Sec. 3.2 withdraws the re-base of one path, with the correct reasons. Sec. 3.3 records the move of H as excluded and lists its consequences. |
| 5 | Resolved | Sec. 3.1 reads sec. 13.3 correctly and adopts the pre-`F` record frozen with `F`. |
| 6 | Resolved in substance | Sec. 5 states Stage 1's predicted-main result and the route that meets the sec. 13.4 safeguard. It leaves out the tool's own landing paths; see required correction 4. |

## 2. Measured facts re-derived (rv1_facts.out)

All of the following agree with the proposal.

**Ledger and D296**

- `ledger.json` at P has `base` = H, 44 `files` entries and 399 splices. `edits.json` has 401
  records over 44 files.
- D296 is the only AGENTS.md splice: `start` 2332, `end` 2382, `old_sha256` 8711166b...0e6f,
  `new_sha256` 532c5919...f051. The replacement shortens the text by 23 bytes (δ = −23).
- Its `old` bytes occur exactly once at H, at M and at Q, always at byte 2332 and line 37. The
  character offset is 2305. At each commit, `sha256(blob[2332:2382])` equals `old_sha256`.

**AGENTS.md blobs**

| Commit | git blob | sha256 | Length (bytes) |
|---|---|---|---|
| H | 12a9281f | d87acac5...7e27 | 102250 |
| M | 4a348007 | f75e0d58...eb80 | 104517 |
| Q | 2503bb8d | 702dbf57...ac0e | 105492 |

**The #1552 changes**

- The common prefix of H and M is 46677 bytes.
- M is H with 354 bytes inserted at 46677, M lines 715-718, followed by H's tail. The appended
  block starts at M byte 102604, line 1524.

**D296 applied**

| Result | sha256 | Note |
|---|---|---|
| H + D296 | 59b68984...82ce2 | equals the ledger's `expected_sha256` and AGENTS.md at T1' |
| M + D296 | 31bf9ac2...d720 | |
| Q + D296 | b7fdda74...a29a | |

**§A.49**

- At M, §A.49 occurs once, header at byte 102610, and runs to the end of the file at 104517. Its
  sha256 is 07c69d0b...107e.
- At Q it spans [102610, 104848), with sha256 7601f051...2ce3. §A.50 starts at 104853.
- In M + D296 and in Q + D296, every byte after the splice equals the original, shifted by −23. So
  §A.49 is byte-identical in both.

**Other ledgered files, pinned blobs and scans**

- The other 43 ledgered files have the same blob at H, M and Q, and each hashes to its
  `base_sha256`.
- Pinned blobs:
  - `.claude/settings.json`: git b7f9b0a6, sha256 ad4130d0...5b9b at M and Q, absent at H and W.
  - The workflow: git bca44ac0, sha256 f8c36855...1646 at W, M and Q; git dfcfd732, sha256
    5c767c9f...e747 at H.
- Scan counts with `PTR`, `CRIT5`, `REPO_PAT` and `IDENT` from `edits_check.py` at P:

  | File | H | M | Q |
  |---|---|---|---|
  | AGENTS.md | 1 (`A1`, line 38; PTR and REPO_PAT) | same | same |
  | workflow | 2 (lines 1 and 3; PTR and REPO_PAT) | 2 | 2 |
  | settings | absent | 0 | 0 |

- On the 27 lines #1553 adds, every module-level pattern gives 0 hits except `CAPS` ("REST",
  "API"). `CAPS` and `REG` are applied only to the replacement text of ledger edits
  (`edits_check.py` lines 377-379; the report at line 659 prints those results). The proposal's
  statement that they never touch tree content is correct.

**PR #1553**

- `git log M..Q` shows the three commits 4e375f6e, 6a547791 and 47e23023. Only AGENTS.md changes,
  +27/-6.
- The first differing byte is 103702, on line 1542. The hunks are `-1542,5 +1542,8` and
  `-1551 +1554,19`.
- §A.50 item 2 reads "amending, freezing or executing the posit-retirement plan of #1169, or
  dispatching its trials".
- `gh api`: the PR is open and a draft, based on M, with head 47e23023, no reviews and no comments.
  Its description still names head 6a547791.

## 3. The approach against DESIGN-v5.1 sec. 13 and 16.2

- **Sec. 13.1, invariants on H and X.** Every invariant holds unchanged: H is fixed, every
  `base_sha256` is H's blob, and X is a single-parent child of H with X:AGENTS.md = H + D296. The
  landing rule ("L's bytes equal M's bytes with C's splices applied at M-translated offsets, each
  `old_sha256` re-verified against M") is exactly what R3-R9 establish in advance, and the landing
  re-runs them. v2 sec. 13.2's "both changed" branch (L[p] equals the blob the reconciliation record
  names) is met by `expected.L_sha256`. Directed correctly.
- **Sec. 13.3.** The foreseeability limit applies only to records written after `F`. A record that
  is written, reviewed and authorized before `F`, and referenced from `retirement-config.json`
  pinned in `F`'s table, is not subject to it. Its other two rules, "changes no decision on X" and
  the ownership chain, are carried as R12, N9 and sec. 4.1. Sound.
- **Sec. 6.3 and 16.2.** The record, its review (`oi-review-record/1`, one verdict per item id R1-R12)
  and its authorization (`oi-owner-authorization/1`, listing record and review by `{path,
  blob_sha256}`) follow the chain. The config references all three by `{path, blob_sha256}` and is
  rooted in `F`'s pin table. N8 maps to design controls O1, O2 and O4, and N9 maps to N2. Sound.
  One gap is required correction 1.
- **Sufficiency of R1-R12 for the owner's three conditions.**
  - Exactly one location: R3 and R4 (counting overlaps, at H and at `M_F`).
  - The approved text: R6, R7 and R8, with the landing bound by `expected.L_sha256`.
  - No byte of §A.49 changes: R9, which also requires that no byte after the splice change.

  R5 handles a non-identity translation. R10 and R11 confine the record to AGENTS.md. N7 makes the
  record lapse if the landing `M` differs from the recorded one. The controls run in both
  directions; P4 and N3 exercise the translation path. Sufficient.
- **Fidelity to v2 sec. 13.3's content list.** The list asks for "H, M, X and L blob ids" for each
  path. The record names H and M blob ids, and gives sha256 only for X and L. The text says X and L
  blob ids "do not exist yet". That holds for commit ids, but the per-path git blob ids are fully
  determined and computable without writing anything (`rv1_blobids.out`):
  - X:AGENTS.md = git 9f4fc3e830707c90ffc105842d26d5b51f01760b, identical to T1''s blob;
  - L:AGENTS.md at M = git 4075b78a1fc7cb39ed83d446822d699b21d83cb8;
  - L:AGENTS.md at Q = git 3ce53ebb93a91a4e1fc6577ed114670226cbe42b.

  See required correction 3.

## 4. PR #1553 section

Accurate in every measured detail. Its consequences are stated correctly:

- the record is computed at `M_F`, not at M;
- if #1553 merges first, `blobs.M`, `side_change_commits`, `main_changes`, `protected` and
  `expected.L_sha256` change, and an earlier authorized record is superseded before `F`;
- §A.49's extent changes, so R9 is evaluated on §A.49 as it stands at `M_F`. With Q standing in for
  `M_F`, R9 holds and the expected L is b7fdda74...a29a.

The note that §A.50 item 2 would make the re-freeze need the owner's approval each time is correct.
The absence of the PR's independent review from GitHub is not a defect of the proposal, as
instructed.

## 5. The flagged owner decision: does sec. 13.4 need records authorized before the tool lands?

**The reading is right.** Sec. 13.4 requires that, before the tool lands, RT-L2 against a predicted
`M` containing the tool's landing paths show "every side change classified and no `base-drift`".
With H fixed, AGENTS.md is a ledgered side change, and v2 sec. 13.2 makes it `base-drift` "unless a
reviewed reconciliation record covers it". Under sec. 6.3, a record without an independent review and
an owner authorization naming both blobs is FAIL `record-invalid`. The tool lands before `F`. So the
safeguard can pass only if the reconciliation record, and the class records, are reviewed and
owner-authorized before the tool lands.

**Is there an alternative within the design?**

- No route lets the safeguard pass without authorized records:
  - re-basing one path or moving H is excluded (sec. 3.2 and 3.3; c.7093128173; c.7099655517);
  - draft or fixture records are `record-invalid`;
  - suppressing the result is excluded.
- The only design-internal freedom is **where** the authorized records live. Sec. 6.3 allows a
  record "in the audit directory of sec. 12.1, or in the amended plan's record directory for records
  frozen with the plan". Records authorized before the tool lands can therefore sit in the tool's
  audit directory and land with the tool. The configuration at `F` then references them by `{path,
  blob_sha256}`. This avoids writing into a plan directory before the plan amendment exists, and
  means authorizing them is not itself an amendment or freeze of the plan. Whether it is an action
  under §A.50 item 2 (if #1553 merges) is for the owner to say.
- Outside the design, the alternative is the owner amending sec. 13.4's wording. The proposal
  correctly names this option and does not propose it.

***

## Required corrections

1. **Record location for the pre-landing safeguard (sec. 4.1, sec. 5 step 2).** Sec. 6.3 fails a
   record that is not read from the git object store. A record also fails if its referenced blob
   does not exist at its path at `F`. And an authorization binds `{path, blob_sha256}`, so changing
   the path needs a new authorization. The proposal places the record "in the amended plan's record
   directory", which does not exist before the tool lands, and does not say from which tree the
   predicted RT-L2 reads it. It should state:
   - where the records are committed for the safeguard run (for example the tool's sec. 12.1 audit
     directory, as part of the tool's landing paths, or a named branch);
   - that the same path and blob are referenced by the configuration at `F`;
   - that any relocation means a new authorization.
2. **N4's named outcome (sec. 4.4).** AGENTS.md is changed on both sides. Under v2 sec. 13.2, an L
   whose blob differs from the blob the reconciliation record names is FAIL
   `landing-conflict-unresolved`. `landing-drops-main-change` is the outcome for a path only M
   changed. Correct N4's expected rule id, or cite the design passage that maps it to
   `landing-drops-main-change`. Countercontrols assert the target rule id (design sec. 6.4, O3).
3. **X and L blob ids (sec. 4.2).** Replace "cannot name blob ids of X, C or L" with "cannot name
   their commit ids". Add the per-path git blob ids of AGENTS.md for X (9f4fc3e8..., equal to T1''s)
   and for the expected L (4075b78a... at M today), beside the sha256 values, so that the record
   meets v2 sec. 13.3's list ("H, M, X and L blob ids").
4. **Stage 1 expectation (sec. 5).** The predicted `M` is M plus the tool's landing paths. Without a
   class record for those paths, they are also REVIEW `side-change-unclassified`. List them in the
   expected Stage 1 result, so that the preregistered expectation covers every side change in the
   predicted tree.

## Optional

- **Self-reference.** A class record for the tool's own landing paths cannot pin its own blob if it
  is itself one of those paths. Place it outside the set it classifies, or exclude record files from
  the class explicitly.
- **R11 and the plan amendment.** R11 should name the plan amendment's own paths, which are on
  `M_F` if the amendment lands before `F`. It should also note how sec. 13.1's "R's tree at M is
  pinned" applies if the amended plan writes into R's directory.
- **Reconciled drift.** State the tool's reported form of reconciled drift, distinct from
  `base-drift`, so that "no `base-drift`" in sec. 13.4 can be read mechanically.
- **PR #1553 head.** Record the PR's current head next to its stale description head; the proposal
  already notes the discrepancy.

## Not verified

- The tool's actual behaviour and outcome names. The tool does not exist; every predicted outcome is
  the design's stated behaviour.
- The independent review of PR #1553 (held off GitHub, as instructed) and of PR #1552.
- Whether anything merges to `main` before `F`. All figures are as of M = 4fb2c1ee and Q = 47e23023.
