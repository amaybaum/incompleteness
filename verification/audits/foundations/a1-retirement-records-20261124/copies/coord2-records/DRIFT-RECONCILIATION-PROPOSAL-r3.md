# A1 plan: reconciliation of `main` drift after the scientific base (revision 3, for review)

## 0. Status, authority and goal link

This is a paper-only proposal. It changes no plan, record, ledger or baseline, writes nothing to the
repository or to GitHub, and authorizes nothing. The three records it drafts (sec. 8) are
unreviewed and unauthorized.

- **Revision history.**
  - This revision supersedes `DRIFT-RECONCILIATION-PROPOSAL-r2.md` (sha256
    bfc6fa25ec4861d2ff927598a5a20cc5de830abd97d41e956c2f1b4aeeabc072) and its drafts in
    `records-draft/`, all of which stay as written.
  - r3 applies the two required corrections of the bounded review `review-r2/review-drift-r2.md`
    (sha256 fb236df1712f67abd23fb50fe82cadc36c49e712a524f6c223247fb537b0435f, verdict ACCEPT WITH
    REQUIRED CORRECTIONS):
    - the ledger binding, new item R13 with its controls (sec. 4.2 to 4.4);
    - consistent wording of R1 and `applies_while`.

    It also states the dry-run `id` and `supersedes` explicitly (sec. 7), and decides that review's
    optional points (sec. 9).
  - Earlier revisions:
    - r1 is `DRIFT-RECONCILIATION-PROPOSAL-r1.md` (sha256
      459987f565a95c3641238df0362ff401dae37bf0593e3d8f8989da240ba6c238);
    - the first draft is `DRIFT-RECONCILIATION-PROPOSAL.md` (sha256
      f870c7630b41ecf0cd218a2a525ae4a7941d1942978633b654d8040628aa2c2d).
  - r2 applied the four required corrections of the independent review
    `review-r1/review-drift-r1.md` (sha256
    3f9482d78782ea006c17a2c75c85523fc800607aea36f28fa277cba02b2100b4, verdict ACCEPT WITH REQUIRED
    CORRECTIONS). It also adopts that review's optional points (sec. 9).
  - It keeps r1's application of the corrections of `review/review-records.md` (sha256
    1ef18f194efa1c2055874f0ccac51ef55b902e1dcd2e6420af05859ef256a5f8).
  - `DRIFT-CHANGES-r3.md` maps the changes from r2; `DRIFT-CHANGES-r2.md` maps those from r1.
- **Design.** `DESIGN-v5.1.md` (sha256
  0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe), accepted as the final reviewed
  design. The sections used are:
  - 6.3, records and the ownership chain;
  - 12.1, placement;
  - 13, the four trees;
  - 16.2, the configuration.

  Section 13 opens with "The v2 sec. 13 rules stand, with the corrections below". The content list
  of a reconciliation record is therefore v2 sec. 13.3, read with v5.1 sec. 13.1.
- **Owner decisions.**
  - #1169 comment 7093128173 (`amaybaum`, 2026-11-23T06:13:50Z): the exception-free verification
    route. It keeps `H` as the immutable scientific base: "No change to the ledger base H ... is
    authorized".
  - #1169 comment 7099655517 (`amaybaum`, 2026-11-23T11:26:50Z; author and time read with `gh api`
    GET). It records Stage 1's authorization and treats the §A.49 merge as a real baseline change.
    - The drift failure is not suppressed, and no baseline is updated silently.
    - `H` is kept unchanged.
    - `.claude/settings.json` is classified as tool configuration, and
      `.github/workflows/a1exit-trial-verify.yml` as the trial workflow.
    - The owner chose "a reconciliation record frozen together with the re-frozen plan". That
      record must show that splice D296 still identifies exactly one location, yields the approved
      text and changes no byte of §A.49.
    - The comment approves an approach only: "no plan amendment, re-freeze, trial rebuild, CI
      dispatch, retirement execution or merge is authorized".
  - The owner-authorized continuation relayed by the coordinating session (2026-11-23) asks for
    this revision and the draft records. It is not a GitHub record and authorizes nothing beyond
    paper work.
- **Goal link (AGENTS.md §A.47).** A1-EXIT (#1169), the exception-free verification route. This
  proposal decides how the drift of the ledgered file `AGENTS.md` after `H` is reconciled at the
  plan's re-freeze. It decides no scientific question and no row disposition.

| Symbol | Commit |
|---|---|
| `H` | 53c6601a10419b6b333cc992474272501ab542af, the scientific base (ledger base) |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6, the frozen plan (`verification/audits/foundations/a1exit-deletion-20261121/`) |
| `W` | 413b0bb88f39cad901befcf4684355c7ee39480b, the workflow base of PREREG §31.12.7 (Merge #1543) |
| `M` | 4fb2c1eed350edf95da2b316abcca93717246589, `main` today (Merge #1552; read-only `git ls-remote` confirms `refs/heads/main` = `M`) |
| `T1'` | 14ac71b4b0a0c0aa2d7068d6799a73f474097060, the trial tree |
| `F` | the future freeze of the amended plan |
| `M_F` | `main` as resolved at `F` |
| `X`, `C`, `L` | candidate, certified execution head, landing merge (design notation) |
| `Q` | 47e23023450fb8fcbd61b5c776a69ba61897f267, PR #1553's current head (open draft, not merged; its description still names an earlier head, 6a547791) |

Scripts for this revision:

- `r3-work/gen_records_r3.py` (sha256
  c32a981beeae41648e2ffa2fa34f58bb11b559bbdba864ae4c4efb09cae6b57c) reads only git objects,
  computes git blob ids in memory, asserts the checks of sec. 4.3 while generating, and writes only
  the draft records. It also runs the R13 controls of sec. 4.4 in memory, on mutated copies of the
  ledger and edit list.
- Its outputs, `r3-work/gen_records_r3.M.out` (sha256
  11bf7db0384413a7de0c9e3edcdb964a17a914cd3d313f14210deb142fe1eb6c, at `M`) and
  `r3-work/gen_records_r3.Q.out` (sha256
  8858b9aaa27dbd53151cfc65d6409aa0bc923a9433d570779137c1f3e6b8fa3f, with `Q` standing in for
  `main`), give the figures of sec. 4 to 8.
- r1's scripts in `r1-work/` give the figures of sec. 1.

## 1. Measured facts (read-only, from git objects)

The scripts are in `r1-work/`. `derive_r1.py` (sha256
9c23b4c3e093370e321a15f6d12e005e2f41feda0ab24ee676893b1ebbc94fe6) and `scans_r1.py` (sha256
43d39fe0b18c5b94323e85b812fbe38643b1bbfb5cd9c8a450cbe5732fd609f9) read only the object store. Their
outputs are `derive_r1.out` (sha256 4b6a08b42c67e33b2573ab9f35488c125fa0e9aa69852973527b928d329c2d02)
and `scans_r1.out` (sha256 269098fef03e88015fe7ebc0e932262cd2fdbea351134fa1f0af1554524f797b). Every
figure below was re-derived for this revision and agrees with the review's `rv_drift.py` and
`rv_scans.py` where they overlap.

### 1.1 History and changed paths

- `H` is on `M`'s first-parent chain. The first-parent commits after `H` are:
  - `413b0bb8` = `W`, Merge #1543 (first parent `H`);
  - `4fb2c1ee` = `M`, Merge PR #1552 (first parent `W`, second parent
    0dba9faf3b0d82e450f3457c7144d68d5f3d3e68).
- There are three paths changed from `H` to `M`:

| Path | Status | Lines | First-parent commit | Blob at `H` | Blob at `M` |
|---|---|---|---|---|---|
| `AGENTS.md` | modified | +32 / -0 | `4fb2c1ee` | git 12a9281f, sha256 d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27 | git 4a348007, sha256 f75e0d58b358f5b7e2c08a0990ea372ff496f9cd640740abbb9a5ebbc7b2eb80 |
| `.github/workflows/a1exit-trial-verify.yml` | modified | +6 / -5 | `413b0bb8` | git dfcfd732, sha256 5c767c9fb0166ad282664b0a8e3b2ec824493f24d5832514b61bdb71e27ee747 | git bca44ac0, sha256 f8c36855cf6e61891cbbd41011714af503b094b9dd63065ac042304817621646 |
| `.claude/settings.json` | added | +7 | `4fb2c1ee` | absent | git b7f9b0a6, sha256 ad4130d0d5f61f0a2807e488706c925cfc6766b9a4cefc2cf04612bb4bb65b9b |

- `W..M` changes only `.claude/settings.json` and `AGENTS.md`. The workflow blob at `M` is `W`'s.
- No `papers/` or `book/` path changed, and no generated artifact changed.

### 1.2 The ledger and `AGENTS.md`

- `edits.json` at `P` has `drafting_base` = `H` and 401 edit records over 44 distinct files.
  `ledger.json` at `P` has `base` = `H`, 44 `files` entries and 399 splices. No edit or splice
  targets `.github/` or `.claude/`.
- Exactly one ledgered file changed from `H` to `M`: `AGENTS.md`. The other 43 have the same blob at
  `H` and `M`, and each hashes to its `base_sha256`. `AGENTS.md`'s `base_sha256` (d87acac5...7e27)
  equals `H`'s blob and differs from `M`'s. That difference is the drift.
- D296 is the only `AGENTS.md` splice. In `ledger.json` it has `start` 2332, `end` 2382 (bytes),
  `old_sha256` 8711166bd781e39db75b410808aa17a00d5decf5f6f58544d3eacf459da00e6f and `new_sha256`
  532c5919b0acfcb31e0c16b799e1b2832b1c07a77d2865d136267c044e9cf051. Its `old` text is
  `"including total\n  finiteness (A1), linearity (A5),"` and its `new` text is
  `"including\n  linearity (A5),"`. The `new` text was approved by owner decision #1169 c.7058783437,
  as D296's `reason` field quotes.
- **Position (correction 1).** At `H` and at `M`, D296's `old` text occurs exactly once, at **bytes
  2332 to 2382** (end exclusive), on lines 37-38. The character offset of the same position is 2305.
  It differs from the byte offset because `AGENTS.md` has multibyte characters (`§`, `—`) before the
  splice. The tool and the design work in bytes. `sha256(M[2332:2382])` equals `old_sha256`.
- **What #1552 changed (correction 2).** The change is not append-only. It makes two insertions:
  - **4 lines inserted into the lessons register**, after `H` line 714 ("and responsibility is not
    retention."). They sit at `H` byte 46677, which is `M` bytes 46677 to 47031 (354 bytes), `M`
    lines 715-718. They begin "For at least four weeks, agent-written Issue and pull-request text
    ..." and end "Hence §A.49.";
  - **28 lines appended** at the end of the file (`H` byte 102250, `M` bytes 102604 to 104517, `M`
    lines 1524-1551): a blank line, `***`, and §A.49 with its adoption line.

  The first byte that differs between `H` and `M` is 46677. Every change therefore lies at or after
  `H` byte 46677, far beyond D296's end at 2382. D296's span and every byte before it are identical
  at `H` and `M`, so the offset translation from `H` to `M` for D296 is the identity.
- **D296 applied at `M`** gives lines 36-38: "Every posit of the substratum model — the posit ledger
  of `papers/Main.md`, including / linearity (A5), the lattice and its coupling range, the form of
  the update and". The results are:
  - `M + D296` has git blob id 4075b78a1fc7cb39ed83d446822d699b21d83cb8 and sha256
    31bf9ac238e8017d48e8c03b2aaec396e2f38e3c2f7472fdb5df4d1ab8c5d720 (104494 bytes). This is the
    expected `L:AGENTS.md` at today's `main`.
  - `H + D296` has git blob id 9f4fc3e830707c90ffc105842d26d5b51f01760b and sha256
    59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2. This is byte-identical to
    `AGENTS.md` at `T1'` (the same git blob) and equals the ledger's `expected_sha256`. It is the
    expected `X:AGENTS.md`.
  - Git blob ids are computed in memory as the SHA-1 of `"blob <length>\0"` followed by the bytes.
    No object is written. The values agree with the review's `rv1_blobids.out`.
  - The line diff between `H + D296` and `M + D296` equals the line diff between `H` and `M`.
  - `M + D296` contains no "(A1)" and no "total finiteness".
- **§A.49.** Its header `## §A.49` occurs once at `M`, at byte 102610 (line 1527). §A.49 runs to the
  end of the file (byte 104517) and its bytes have sha256
  07c69d0b45cc750fe5bb77b10feab331dc719e70352f8eaeddecb6532c58107e. In `M + D296`, every byte after
  the splice equals `M`'s, shifted by the length change of -23. In particular §A.49 is byte-identical.
  D296 changes no byte of §A.49.

### 1.3 Other plan checks that read these files

- The plan's tree-scan patterns `PTR`, `CRIT5`, `REPO_PAT` and `IDENT` (from `edits_check.py` at `P`)
  give the same result on `AGENTS.md` at `H`, `M` and PR #1553's head. That result is one occurrence,
  `A1` on line 38, matched by `PTR` and by `REPO_PAT`. PREREG's occurrence row
  "unexplained | AGENTS.md | 1 | 0" is unaffected.
- On the workflow file, `PTR` and `REPO_PAT` give 2 at `H` and 2 at `M`. Both occurrences are covered
  by `edits_check.py`'s `EXPLAINED` entry for that path ("unrelated label", the programme name
  A1-EXIT). On `.claude/settings.json` every pattern gives 0.
- RT-DR3W reads `AGENTS.md` by blob id at `H` (12a9281f) and is unaffected.
- `preserve_check.py --verify-run` requires the workflow blob at a dispatch's head to equal `W`'s
  (PREREG §31.12.7 part 1; §31.12.8 part 4). At `M` it does (bca44ac0), so a dispatch from `M` is
  valid under the frozen plan. The self-test's hard-coded guard `led['base'].startswith('53c6601a')`
  (`preserve_check.py` line 1245) and the constant `WORKFLOW_BASE` = `W` (line 657) are untouched
  while `H` and `W` stay fixed.

## 2. Classification of each side change (review-records correction 3)

Under design sec. 13.1, every path changed between `H` and `M` is a side change. A side change to a
ledgered or corpus path is `base-drift`, a FAIL for the landing unless it is reconciled. Any other
side change is classified by a reviewed side-change class record, or it is REVIEW_REQUIRED
`side-change-unclassified`.

| Path | Class | Basis | Pinned blob | Tool outcome without records |
|---|---|---|---|---|
| `AGENTS.md` | ledgered path; change outside every splice span; base drift, reconciled by the record of sec. 4 | sec. 13.1; ledger `files` entry | `M`: sha256 f75e0d58...eb80 (in the reconciliation record, sec. 4) | FAIL `base-drift`, which is correct and not to be suppressed |
| `.claude/settings.json` | `tool-configuration` | owner decision c.7099655517. It is a Claude Code configuration file (`{"attribution": {"commit": "", "pr": "", "sessionUrl": false}}`), not ledgered and not corpus, and no plan check reads it | `{path: ".claude/settings.json", blob_sha256: "ad4130d0d5f61f0a2807e488706c925cfc6766b9a4cefc2cf04612bb4bb65b9b"}` | REVIEW `side-change-unclassified` |
| `.github/workflows/a1exit-trial-verify.yml` | `trial-workflow` | owner decision c.7099655517, and **PREREG §31.12.7 at `P`**, which defines `W` as the **workflow base** that decides how each trial is checked, distinct from the ledger base `H`. `preserve_check.py` enforces that the workflow blob at every dispatch head equals `W`'s. The design names the trial workflow as an example class (sec. 13.1) and assigns `W`'s workflow to `roles.side_change_classes` (sec. 16.4) | `{path: ".github/workflows/a1exit-trial-verify.yml", blob_sha256: "f8c36855cf6e61891cbbd41011714af503b094b9dd63065ac042304817621646"}`, `W`'s blob | REVIEW `side-change-unclassified` |

**Pinning.** Design sec. 16.2 gives `roles.side_change_classes` as `{path, blob_sha256}`, and sec. 6.3
makes a side-change class record a record under the ownership chain. This proposal pins at both
levels, so it satisfies either reading:

- **The classified files.** `retirement-config.json` lists each classified file in
  `roles.side_change_classes` as the `{path, blob_sha256}` above.
- **The class records.** There are two records, one per class, each with schema
  `oi-side-change-classes/1` and one item:
  - `a1exit-scc-tool-configuration-1`: `.claude/settings.json`, git blob b7f9b0a6, sha256
    ad4130d0...5b9b, class `tool-configuration`, introduced by first-parent commit `4fb2c1ee`;
  - `a1exit-scc-trial-workflow-1`: `.github/workflows/a1exit-trial-verify.yml`, git blob bca44ac0,
    sha256 f8c36855...1646, class `trial-workflow`, introduced by first-parent commit `413b0bb8`
    (`W`), with its reason citing PREREG §31.12.7.

  Each is referenced, with its review and authorization records, in `records` as `{kind, path,
  blob_sha256}`. The reconciliation record also references both (sec. 4.2). Drafts are in
  `records-draft-r3/` (sec. 8).

A later change to either file gives a blob that differs from the pinned one. That file is then
unclassified again (REVIEW) until a new class record covers it. For the workflow this agrees with
§31.12.7, under which a dispatch head whose workflow blob is not `W`'s is void.

A class covers only non-ledgered, non-corpus paths. It never covers `AGENTS.md`.

## 3. The approach for `AGENTS.md` (review-records corrections 4 and 5)

### 3.1 Chosen: a reconciliation record frozen with `F`

The owner chose this approach in comment 7099655517. `H` stays `53c6601a`. Every `base_sha256` stays
`H`'s blob, and `X` stays a single-parent child of `H`, so every sec. 13.1 invariant on `H` and `X`
holds unchanged. The drift is reported by the tool and resolved by a reviewed record. No baseline
changes.

**Sec. 13.3, read correctly.** Its first rule reads: "A record written after `F` is allowed only for
side changes on `M` that the freeze could not foresee." The foreseeability limit applies only to
records written after `F`. The record proposed here is written, reviewed and owner-authorized before
`F`, and frozen with the amended plan at `F`. It is referenced from `retirement-config.json`, which
`F`'s pin table pins. The limit does not restrict it. The draft's statement that a landing-time
record "fits poorly" because the drift is known now remains true of a record written after `F`. That
is why the record is frozen with `F` rather than written at landing. Sec. 13.3's other two rules
apply in full:

- the record changes no decision of op C on `X` and relabels no failing retirement check;
- it is under the ownership chain of sec. 6.3.

**How it resolves the landing.** At landing, `AGENTS.md` is changed on both sides: `X` applies D296
and `M` carries #1552 (and any later change). By sec. 13.1, `L`'s `AGENTS.md` passes only if it
equals `M`'s bytes with `C`'s splices applied at `M`-translated offsets, each `old_sha256`
re-verified against `M`. By v2 sec. 13.2, `L[p]` must equal the blob the reconciliation record names.
The record states that blob in advance, as a git blob id and a sha256, and proves that it is the composition the rule
demands.

### 3.2 Excluded: re-basing `AGENTS.md` alone

The draft recommended re-resolving the ledger base of `AGENTS.md` to the blob at the new freeze's
`main`. That route is withdrawn. Under the accepted design it is incoherent, for four reasons:

1. **The base invariant fails.** Sec. 13.1 requires that every `base_sha256` equal `H`'s blob, and v2
   sec. 13.2 makes a mismatch an ERROR. A per-file base of `M_F`'s blob with `H` = `53c6601a` breaks
   that invariant for `AGENTS.md`.
2. **The drift would remain.** Base drift is defined by the paths that changed between `H` and `M`,
   not by a per-file hash. `AGENTS.md` would still be a ledgered side change and still `base-drift`.
3. **`X` contradicts it.** `X` has the single parent `H`, and its ledgered files must equal `H` plus
   their splices. So `X`'s `AGENTS.md` is `H + D296` (59b68984...), the ledger's `expected_sha256`.
   It is not built from `M_F`'s text. A base hash taken from `M_F` would contradict the expected hash
   and the parent rule.
4. **It is the baseline update the owner excluded.** It changes a recorded base hash to make the
   drift disappear, which is what comment 7099655517 excludes ("no baseline is updated silently").
   Comment 7093128173 does the same ("No change to the ledger base H").

### 3.3 Excluded: moving `H`

Moving the scientific base to a later commit H′ would be coherent with sec. 13, but the owner
decisions exclude it: c.7093128173 calls `H` the immutable scientific base, and c.7099655517 keeps
`H` unchanged. It would also carry all of the following:

- `roles.scientific_base` = H′;
- the HP segment E..H extended to E..H′ (sec. 3, sec. 16.2 lint, sec. 16.6);
- every `base_sha256` re-verified at H′;
- `ledger.json`'s `base` and `edits.json`'s `drafting_base` changed;
- `X`, T0′ and T1′ rebuilt as children of H′;
- `R`'s tree re-pinned at H′;
- PREREG §31.12.7's ledger-base row changed;
- the hard-coded `H` checks in the plan's checkers replaced (for example `preserve_check.py` line
  1245).

It is recorded here only as excluded.

### 3.4 Not viable: no reconciliation

The landing check FAILs `base-drift` on `AGENTS.md`, and the retirement cannot land. Suppressing that
failure is excluded by the owner decision.

## 4. The reconciliation record

### 4.1 Location in the object store and ownership chain (review-r1 correction 1)

**Where the records sit.** Sec. 6.3 allows a record in two places: "in the audit directory of sec.
12.1, or in the amended plan's record directory for records frozen with the plan". The amended
plan's record directory does not exist before the tool lands. The pre-landing safeguard of sec. 13.4
therefore cannot read the records from there. This proposal adopts the review's in-design option:

1. **The tool's audit directory.** The reconciliation record and the two side-change class
   records, with their review records and owner authorization records, are files in the tool's own
   audit directory under `verification/audits/` (sec. 12.1). That directory "holds ...
   reconciliation records" and the other reviewed records.
   - Today its name is a placeholder, `verification/audits/<TOOL-AUDIT-DIR>/`, because Stage 1
     fixes it.
   - The file names are those of the drafts in sec. 8.
2. **They land with the tool.** They are part of the tool's landing paths. The landing commit
   reaches `main` through the tool's own review and the owner's merge decision.
3. **What the safeguard reads.** The pre-landing safeguard (sec. 5) reads the records from the
   object store, in the tree of the predicted `M`: `main` plus the tool's landing commit, which
   contains them. The predicted configuration references them by `{path, blob_sha256}`. The tool
   never reads a working-tree file (sec. 6.3, "a record not read from the git object store" fails).
4. **The same path and blob at `F`.** `retirement-config.json`, frozen with the amended plan at `F`
   and pinned in `F`'s table, references each record, its review and its authorization by the same
   `{path, blob_sha256}` that the safeguard read. The blobs then exist on `M_F` at those paths, as
   sec. 6.3 requires ("a referenced blob that does not exist at `F` at its path ... fails"). This
   is how the record is "frozen together with the re-frozen plan": the plan's frozen configuration
   pins it, while it sits in the tool's audit directory.
5. **Relocation needs a new authorization.** An owner authorization binds `{path, blob_sha256}`, so
   moving a record changes what was authorized. A record moved to another path (for example into
   the amended plan's record directory) needs a new owner authorization, and a new review if its
   bytes change. A record whose path or bytes differ from those authorized is `record-invalid`.
   Any change to a record's content is a new record with `supersedes`, a new review and a new
   authorization. The same holds for a change to a referenced class record's path or blob, which
   changes the reconciliation record's `side_change_classes` field.

**Ownership chain (sec. 6.3).** It is unchanged from r1:

- **Writer.** The record's `author` names the writer, who may not review it.
- **Review.** A separate `oi-review-record/1` record by a non-author. It names exactly the record's
  blob, its `method` names every object id read, and it gives one `accept` verdict per item id
  (R1-R13, or SC1 for a class record).
- **Owner authorization.** A separate `oi-owner-authorization/1` record. It quotes `owner`, `time`
  and `comment_id`, and lists `{record, review}` by `{path, blob_sha256}`. One authorization may list
  all three records and their reviews.

The configuration at `F` lists all of them in `records` and lists the two classified files in
`roles.side_change_classes`. Its own sha256 is in `F`'s pin table.

### 4.2 Content (review-r1 correction 3)

The design fixes the schema id `oi-reconciliation/1` (sec. 16.1) and the content list of v2 sec.
13.3:

- `M`;
- the paths covered;
- for each path, the `H`, `M`, `X` and `L` blob ids and the resolution;
- for a ledgered path, the splices re-verified by hash and span against `M` and translated by `M`'s
  own change;
- the reviewer and the owner record.

It gives no field-level schema. The draft in `records-draft-r3/a1exit-recon-agents-md-1.json` (sec. 8)
renders that list with the field names of this proposal. **The field names must be reconciled with
the `oi-reconciliation/1` JSON Schema implemented in Stage 1 before the record is reviewed.** If
they differ, the record follows the schema and the content below remains the requirement.

**Blob ids.** A record written before `F` cannot name the **commit ids** of `X`, `C` or `L`, which
do not exist yet. It does name the **per-path git blob ids**, which are fully determined now and
computed without writing any object:

| Tree | `AGENTS.md` git blob id | sha256 | How it is determined |
|---|---|---|---|
| `H` | 12a9281fb88c14395b6715a3bf4b4f6b030f433c | d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27 | read |
| `M` (today) | 4a34800747d70b338e0040af29127ef2e608118a | f75e0d58b358f5b7e2c08a0990ea372ff496f9cd640740abbb9a5ebbc7b2eb80 | read |
| `X` (and `C`) | 9f4fc3e830707c90ffc105842d26d5b51f01760b | 59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2 | `H` + D296; equals `T1'`'s blob and the ledger's `expected_sha256` |
| expected `L` at `M` | 4075b78a1fc7cb39ed83d446822d699b21d83cb8 | 31bf9ac238e8017d48e8c03b2aaec396e2f38e3c2f7472fdb5df4d1ab8c5d720 | `M` + D296 at the identity translation |
| `main` with PR #1553 merged (`Q`'s blob) | 2503bb8d38c01c907ac2348af91be19f6344e9a8 | 702dbf573955cde535f26bc87efd62564f90945af825358558d3746ff6e8ac0e | read at `Q` |
| expected `L` with PR #1553 merged | 3ce53ebb93a91a4e1fc6577ed114670226cbe42b | b7fdda74933ffff369d8550b71b4755b20e3ad6c78eba7469f454f18f907a29a | `Q` + D296 at the identity translation |

The two PR #1553 rows assume that a merge leaves `AGENTS.md` at `main` equal to `Q`'s blob. That
holds for a merge of `Q` into `M` with no further change. It is to be re-read at the actual merge.

**Fields** (draft values at `M`; `<...>` marks a placeholder):

```text
schema               oi-reconciliation/1
draft_status         (drafts only) UNREVIEWED, UNAUTHORIZED DRAFT ...   -- removed before review
id                   a1exit-recon-agents-md-1          (never reused)
supersedes           null
author               <writer>
scientific_base      53c6601a10419b6b333cc992474272501ab542af
main                 {computed_at: 4fb2c1ee..., applies_while: "..."}   -- see below
ledger               {path: <plan dir>/ledger.json, commit: P, blob_sha256: 2055e68f...b5, git_blob: ba37c1cd...}
edits                {path: <plan dir>/edits.json, commit: P, blob_sha256: 528f146d...dec1, git_blob: <computed>}
ledger_binding       {canonical_json rule, ledger_base H,
                      agents_files_entry {value, sha256 926eaa8b21e933576422f1c7854f6cc8dd0aa178b8225e44b05067ac933dc514},
                      agents_splices {ids [D296], sha256 dd0acccd6566e2e5f5e6b24bd3d0e6d2527cbb33210acb5fe368d0ac2c374119},
                      agents_edit_records {ids [D296], sha256 fbb374e270690352e68e307a7e921fb6972b9efa03a0abcaa727ccdefa9f1395},
                      rule (R13)}
paths[0]:
  path               AGENTS.md
  class              ledgered
  side_change_commits [4fb2c1eed350edf95da2b316abcca93717246589]
  blobs              {H: {git 12a9281f..., sha256 d87acac5..., bytes 102250},
                      M: {git 4a348007..., sha256 f75e0d58..., bytes 104517}}
  main_changes       [{insert, main bytes [46677, 47031), main lines 715-718, after H line 714},
                      {insert, main bytes [102604, 104517), main lines 1524-1551, after H line 1519}]
  common_prefix_H_M_bytes 46677
  splices            [{D296, start_H 2332, end_H 2382, start_M 2332, end_M 2382, translation identity,
                       old_sha256 8711166b...0e6f, new_sha256 532c5919...f051,
                       old_count_H 1, old_count_M 1, char_offset_H 2305, lines [37, 38]}]
  protected          [{§A.49, header "## §A.49", start_M 102610, end_M 104517, sha256 07c69d0b...107e}]
  expected           {X: {git 9f4fc3e8..., sha256 59b68984...}, L: {git 4075b78a..., sha256 31bf9ac2..., bytes 104494}}
  length_delta       -23
  resolution         "L:AGENTS.md = main's AGENTS.md with C's splices at main-translated offsets ..."
unchanged_ledgered   {count 43, rule}
unchanged_corpus     {rule, evaluated at run time}
side_change_classes  [{path <TOOL-AUDIT-DIR>/a1exit-scc-tool-configuration-1.json, blob_sha256 e4895e0f...},
                      {path <TOOL-AUDIT-DIR>/a1exit-scc-trial-workflow-1.json,  blob_sha256 67561f97...}]
changes_decisions_on_X []
items                R1 ... R13, with item_text
ownership_chain      (drafts only) placeholders for the separate review and authorization records
```

**`main` names no later commit (consequence of correction 1).** r1 had the record name `M_F`. A
record authorized before the tool lands cannot do that: the tool's own landing, and possibly the
plan amendment, move `main` before `F`. In r2 the record therefore states:

- the commit it was computed at (`main.computed_at`);
- the blobs and the first-parent commits that change `AGENTS.md`, which are the facts it asserts.

At every run (the safeguard, `F` and landing), `main` is resolved afresh, and the record applies
only if R13 and R1 to R12 all hold there, R13 first. The draft's `main.applies_while` and `item_text.R1` say the same: `main` is resolved by `git ls-remote origin refs/heads/main` at each run, not only at `F`. The tool's landing paths and the plan amendment change neither
`AGENTS.md` nor any ledgered or corpus path, so they do not invalidate the record. Any change to
`AGENTS.md` does, and a new record is then needed. For the same reason the record carries no list of
all changed paths. R11 evaluates that list at run time.

**The facts the record asserts:**

- the drift on `AGENTS.md` between `H` and the resolved `main` comes only from
  `side_change_commits`, and `main`'s blob is `blobs.M`;
- D296's `old` text occurs exactly once at `H` and exactly once at `main`, and the span translates
  as stated;
- applying D296 at `main` yields the approved `new` text in place, with the stated `L` blob id and
  sha256;
- D296 changes no byte of §A.49 as it stands at `main`, and no other byte after the splice;
- every other ledgered path and every corpus path is unchanged from `H`;
- the record changes no decision on `X`.

### 4.3 Checks a verifier runs from git objects

Each check reads only the object store (`git cat-file`, `git rev-list`, `git diff --name-status`) and
the pinned record files. `main` is the commit resolved by `git ls-remote origin refs/heads/main` for
the run, at each run: the pre-landing safeguard, `F` and landing. Bytes are compared as bytes, and
offsets are byte offsets. Each check is an item id, so the reviewer gives one verdict for each. The
generator asserts every check while it builds the draft.

**Which ledger and edit list (review-r2 correction 1).** R3, R4, R6, R8 and R10 read the ledger and
edit list that the configuration uses at the run: `adapters.ledger` and its companion, read from the
object store at their configured `{path, blob_sha256}`. They do not read the copies at `P` named in
the record's `ledger` and `edits` fields. R13 binds the two.
- **R13 is checked first.** If it fails, the record does not apply. The drift stays `base-drift`
  (fail closed), and only a superseding record computed against the new ledger can reconcile it.
- **What R13 binds.** It requires the AGENTS.md `files` entry, the AGENTS.md splice list and the
  AGENTS.md edit records to be byte-equal (canonical JSON) to the pinned ones. That is the minimum
  the review names, and exactly the ledger data R3 to R8 consume. It does not require whole-blob
  equality of `ledger.json` and `edits.json` (2055e68f... and 528f146d... at `P`).
- **Why not whole-blob equality.** The re-freeze is expected to change those files elsewhere (other
  files' entries, `edits_sha256`). Requiring whole-blob equality would void a record authorized
  before the tool lands for a change that touches none of its facts.
- **What is reported.** Whether the whole blobs are equal is still reported.
- **R10.** It needs no binding of its own. It reads every other `files` entry of the run's ledger and
  requires each to be unchanged from `H` and equal to its `base_sha256`, so an amended entry for
  another file is checked against `H` as it stands at the run.

| Item | Check | At `M` today |
|---|---|---|
| R1 | `main` is resolved by `git ls-remote origin refs/heads/main` at this run (safeguard, `F` or landing); `H` is on `main`'s first-parent chain; the first-parent commits on `H..main` that change `AGENTS.md` are exactly `side_change_commits` | `[4fb2c1ee]` |
| R2 | `AGENTS.md` at `main` has git blob id and sha256 = `blobs.M` | 4a348007 / f75e0d58...eb80 |
| R3 | **Uniqueness at `H`:** the overlapping occurrence count of D296's `old` bytes is 1, at `start_H` = 2332; `sha256(H[2332:2382])` = `old_sha256` | 1 at 2332 |
| R4 | **Uniqueness at `main`:** the same count is 1, at `start_M`; `sha256(main[start_M:end_M])` = `old_sha256` | 1 at 2332 |
| R5 | **Translation:** if the common byte prefix of `H` and `main` is ≥ `end_H`, the translation is the identity; otherwise the recorded delta equals the length change before `start_H`, and no `main_changes` range meets `[start_M, end_M)` | prefix 46677: identity |
| R6 | **Approved text** (`new` and `new_sha256` from the run's ledger and edit list, bound by R13): `Lx = main[:start_M] + new + main[end_M:]`; `Lx[start_M : start_M+len(new)] = new`; `sha256(new)` = `new_sha256`; lines 36-39 of `Lx` equal those of `H` + D296 (= `T1'`) | holds |
| R7 | **Expected landing blob:** the git blob id and sha256 of `Lx` = `expected.L` | 4075b78a / 31bf9ac2...d720 |
| R8 | **Expected candidate blob:** the git blob id and sha256 of `H` + D296 = `expected.X` = the `expected_sha256` of the AGENTS.md entry of the run's ledger (bound by R13), and `T1'`'s blob | 9f4fc3e8 / 59b68984...82ce2 |
| R9 | **§A.49 untouched:** `## §A.49` occurs once in `main` and once in `Lx`, at byte `a` ≥ `end_M`. With `δ` = −23, `Lx[a+δ : b+δ] = main[a:b]`, where `[a, b)` runs from the header to the start of the next line that is exactly `***`, or to the end of the file; its sha256 = `protected[0].sha256`. Also `Lx[end_M+δ:] = main[end_M:]` | [102610, 104517); equal |
| R10 | **Other ledgered paths:** each `files` entry of the run's ledger other than AGENTS.md (43 at `P`) has the same blob at `main` as at `H`, and sha256 = `base_sha256` | 43 of 43 |
| R11 | **Corpus and other side changes:** `git diff --name-status H main` lists no corpus path and no generated corpus artifact. Every other listed path is covered by a referenced class record whose pinned blob matches, or by another reviewed class record: the tool's landing paths, and the plan amendment's own paths if the amendment lands on `main` before `F` | only the two classified files at `M` |
| R12 | `changes_decisions_on_X` is empty | empty |
| R13 | **Ledger binding, checked first:** the run's ledger has `base` = `scientific_base`. Under the canonical JSON rule (`json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False)`, UTF-8, sha256), its AGENTS.md `files` entry, its list of AGENTS.md splices (in ledger order) and the run's edit-list records for AGENTS.md (in file order) hash to `ledger_binding`'s three values, with the same id lists. Otherwise the record does not apply, and a superseding record is needed | holds with the ledger and edit list at `P` |

At landing the tool re-runs R13 and R1 to R12 against the `M` it resolves then (sec. 13.4), and also
requires `L:AGENTS.md` = `expected.L` by git blob id and sha256.

**Reported form (optional point adopted).** A drift that R13 and R1 to R12 reconcile is reported as its own
item, naming the record's id and blob, for example `base-drift-reconciled`. It is never reported as
`base-drift`. "No `base-drift`" in sec. 13.4 can therefore be read mechanically from the structured
output. The exact class name is fixed by the Stage 1 implementation and goes into the controls file.

**`R`'s tree (optional point adopted).** Sec. 13.1 requires "`R`'s tree at `M` is pinned". `R` is
the frozen ledger record directory (tree b05efdca). The records proposed here sit in the tool's
audit directory, not in `R`. If the amended plan writes into `R`'s directory, the amendment must
re-pin `R`'s tree or show that it is unchanged. That is outside this record.

### 4.4 Controls in both directions

All controls run in memory: synthetic commit objects held by the tool's reader, as for RT-L and
RT-L2. No commit, ref or merge is created in the repository. Each control asserts its target
rule id, not only the run's outcome (design sec. 6.4, O3).

**Positive controls (the record must apply and the composition must PASS):**

| Id | Case | Expected |
|---|---|---|
| P1 | real objects `H`, `M` = 4fb2c1ee, the ledger and edit list at `P` | R13 and R1 to R12 hold; `L:AGENTS.md` git 4075b78a, sha256 31bf9ac2...d720 |
| P2 | real objects with `Q` = 47e23023 standing in for `main` (no claim that it merges), against a record regenerated there (sec. 7) | R13 and R1 to R12 hold; `L:AGENTS.md` git 3ce53ebb, sha256 b7fdda74...a29a |
| P3 | an in-memory landing with parents (`M`, an `X` = `H` + all splices, as `T1'`), composed under the record | landing composition PASS; `L:AGENTS.md` = `expected.L`; the workflow at `L` equals `W`'s blob; the item is reported as reconciled drift |
| P4 | synthetic `M′` with one line inserted before byte 2332, with a record carrying the correct delta | R4 to R9 hold at the translated offset |
| P5 | the run's ledger and edit list equal to those at `P` | R13 holds |
| P6 | an amended ledger and edit list that change another file's splice, the ledger's `edits_sha256` field and another file's edit record, leaving every AGENTS.md entry unchanged | R13 holds (whole-blob inequality reported); R10 then checks the other files against `H` |
| P7 | the same content, with the ledger at another path in the configuration | R13 holds (the binding is by content; the configuration pins the path) |

**Negative controls (each must fail with the named rule id):**

| Id | Case | Expected |
|---|---|---|
| N0 | `M` today with no reconciliation record | FAIL `base-drift` on `AGENTS.md`, and the landing composition FAIL `landing-conflict-unresolved` (design v2 R7) |
| N1 | `M′` = `M` with a second copy of D296's `old` text after §A.49 | R4 fails (count 2); the record does not apply; `base-drift` |
| N2 | `M′` with one byte changed inside [2332, 2382) | R4 fails (`old_sha256`); `base-drift` |
| N3 | P4's `M′` with a record still claiming the identity translation | R4 and R5 fail; `base-drift` |
| N4 | a record whose `expected.L` is `H` + D296 (git 9f4fc3e8, sha256 59b68984...) | R7 fails. An `L` built to it differs from the composition the rule demands on a path both sides changed, which is FAIL `landing-conflict-unresolved` (v2 sec. 13.2, "both changed"; `landing-drops-main-change` is the outcome only for a path that `main` alone changed) |
| N5 | an `L` whose `AGENTS.md` also changes one byte of §A.49 | R9 fails; FAIL `landing-conflict-unresolved` |
| N6 | `M′` that also changes one byte of another ledgered file (for example `papers/Main.md`) | R10 fails; `base-drift` on that path, which the record does not cover |
| N7 | landing `M` whose `AGENTS.md` blob differs from `blobs.M` | R2 fails; the record does not apply; `base-drift` |
| N8 | the record with `reviewer` = `author`; a review naming another blob; an authorization naming the path without a hash; an authorization naming the record at another path (relocation) | FAIL `record-invalid` (design controls O1, O2, O4, and the relocation case of sec. 4.1) |
| N9 | the record with a non-empty `changes_decisions_on_X` | FAIL `record-invalid` (design control N2) |
| N10 | the trial-workflow class record pinning `H`'s workflow blob (5c767c9f...e747) instead of `W`'s | REVIEW `side-change-unclassified` on the workflow path |
| N11 | any draft record of sec. 8 as it stands (no review, no authorization) | FAIL `record-invalid` |
| N12 | the run's ledger with D296's `new` text changed | R13 fails; the record does not apply; `base-drift` |
| N13 | the run's ledger with the AGENTS.md `expected_sha256` changed | R13 fails; `base-drift` |
| N14 | the run's ledger with D296's span shifted by one byte | R13 fails; `base-drift` |
| N15 | the run's ledger with a second AGENTS.md splice | R13 fails; `base-drift` |
| N16 | the run's edit list with the D296 record changed (its `reason` only) | R13 fails; `base-drift` (conservative: any change to the AGENTS.md edit records needs a superseding record) |
| N17 | the run's ledger without an AGENTS.md `files` entry | R13 fails; `base-drift` |
| N18 | the run's ledger with `base` other than `H` | R13 fails (and the configuration fails its own base check, sec. 16.6) |

P5 to P7 and N12 to N18 test the binding function. They were run in memory by the generator on
mutated copies of the ledger and edit list at `P`: all ten gave the expected result, with 0
mismatches (`r3-work/gen_records_r3.M.out`). In the tool they become controls with the rule ids its
implementation fixes.

## 5. Expected Stage 1 result and the sec. 13.4 safeguard (review-r1 correction 4)

**Stage 1** is authorized by the owner, recorded in c.7099655517. It is local only, with no push.
Its predicted-main check runs RT-L2 in memory against a predicted `M` = 4fb2c1ee plus the tool's
landing paths. It uses the A1 configuration without reviewed and authorized records, which do not
exist in Stage 1. The expected result is:

| Side change | Expected |
|---|---|
| `AGENTS.md` | FAIL `base-drift` (exit 20) |
| `.claude/settings.json` | REVIEW `side-change-unclassified` |
| `.github/workflows/a1exit-trial-verify.yml` | REVIEW `side-change-unclassified` |
| **each of the tool's own landing paths** (`tools/ledger_coverage.py`, `tools/ledger_coverage/`, the audit directory, and any draft records placed there) | REVIEW `side-change-unclassified`, since no reviewed class record covers them |
| overall | FAIL |

This result is correct. It is reported as measured and not suppressed, and no baseline is changed
to avoid it. If a draft record from sec. 8 is placed in the predicted tree as a fixture, it must give
FAIL `record-invalid` (N11), never a pass. Stage 1 exercises the reconciliation mechanism through
the synthetic controls of sec. 4.4 and the design's R7/R8 pair, not through authorized A1 records.

**How sec. 13.4's requirement is met.** Before the tool lands, RT-L2 against a predicted `M` that
contains the tool's landing paths must show "every side change classified and no `base-drift`". It
is met as follows:

1. **Authorized records in the tool's landing commit.** The reconciliation record, the two class
   records and a class record for the tool's own landing paths are written, independently reviewed
   and owner-authorized by exact `{path, blob_sha256}`. With their review and authorization
   records, they are committed in the tool's audit directory as part of the tool's landing commit
   (sec. 4.1). The tool-landing class record is outside this proposal.
2. **The safeguard run.** RT-L2 reads the predicted `M` (today's `main` plus that landing commit)
   from the object store, with a predicted configuration that references those records by the same
   `{path, blob_sha256}`. The expected result:
   - `AGENTS.md`: reconciled (R13 and R1 to R12 hold; reported as reconciled drift, not `base-drift`);
   - the settings file, the workflow and the tool's landing paths: classified;
   - no `base-drift`.
3. **Freeze unchanged.** At `F`, `retirement-config.json` references the same paths and blobs, now
   on `M_F`. R13 and R1 to R12 are re-run against `M_F` with the ledger and edit list frozen at `F`; if the amendment changed any AGENTS.md entry, R13 fails and a superseding record is needed before `F`. If `AGENTS.md` or any ledgered or corpus path
   changed between the safeguard run and `F`, the record is superseded (new record, review and
   authorization, landed by its own reviewed change) and RT-L2 is re-run before `F`. A record that
   no longer holds is never carried into `F`.

**Owner decision still needed.** Step 1 needs the owner to authorize the records before the tool
lands. Comment 7099655517 does not grant that. Because the records sit in the tool's audit
directory, authorizing them is not itself an amendment or freeze of the plan. Whether it falls under
§A.50 item 2 if PR #1553 merges is for the owner to say. The alternative, the owner amending sec.
13.4's wording, is named and not proposed.

## 6. PR #1553 and further drift

PR #1553 is an open draft based on `M`. Its current head is `Q` = 47e23023; its description still
names 6a547791. It has three commits on `M`:

- 4e375f6e "footer rule in §A.49; §A.50 standing owner approvals";
- 6a547791 "apply the independent review's required corrections";
- 47e23023 "§A.49 rule 2: footer handling observed per operation".

It changes only `AGENTS.md` (+27 / -6). If it merges before the re-freeze, re-derived from `Q`:

- **`AGENTS.md` changes.** It becomes git 2503bb8d, sha256 702dbf57...ac0e (105492 bytes, 1572
  lines).
  - The first byte that differs from `M` is 103702 (line 1542), inside §A.49 rule 2.
  - `M` lines 1542-1546 are replaced by 8 lines.
  - The adoption line (`M` line 1551) is replaced by 19 lines: the amended adoption line, a `***`
    rule and a new §A.50.
- **D296's span is untouched.** The `old` text occurs exactly once, at bytes 2332 to 2382 (lines
  37-38), and lines 37-38 are identical to `M`'s. The common prefix with `H` is still 46677 bytes,
  so the translation is the identity.
- **§A.49 itself changes.** At `Q` it spans [102610, 104848), sha256
  7601f051ed8b4baf00aa98b8a90429c1cb26f81923a47567bb09e5c100ca2ce3. §A.50 starts at 104853. R9 is
  evaluated on §A.49 as it stands at the resolved `main`. At `Q`, D296 leaves every byte after the
  splice unchanged, §A.49 and §A.50 included.
- **Nothing else changes.** No other ledgered file and neither classified file changes, so the
  workflow and settings blobs at `Q` are `M`'s.
- **Plan patterns.** On the 27 added lines, `PTR`, `REPO_PAT`, `IDENT` and `CRIT5` give 0 hits, and
  so do the other module-level patterns of `edits_check.py` at `P` except `CAPS`. `CAPS` matches
  "REST" and "API", but it is applied only to the replacement text of ledger edits (`edits_check.py`
  lines 377-379), never to tree content. The whole-file count at `Q` is unchanged: one occurrence,
  line 38. The PR's own review, which is reported to find zero hits, is not on GitHub and was not
  checked.
- **Owner approval.** If merged, §A.50 item 2 requires the owner's approval each time for
  "amending, freezing or executing the posit-retirement plan of #1169".

The record is computed against `main` as resolved at the run, and must hold at `F`. A change to
`AGENTS.md` after `F` and before landing was not foreseeable at `F`. Sec. 13.3 admits a new post-`F`
record for it, under the same chain, and that record never changes a decision on `X`.

## 7. Would merging PR #1553 require regenerating each record?

Each record was regenerated with `Q` standing in for `main`
(`r3-work/variant-pr1553-head/`, `r3-work/gen_records_r3.Q.out`) and compared field by field.

| Record | Regenerate? | Why |
|---|---|---|
| `a1exit-scc-tool-configuration-1.json` | **No** | `.claude/settings.json` has the same blob at `Q` (git b7f9b0a6, sha256 ad4130d0...5b9b). The record names no `main` commit. The regenerated file is byte-identical (sha256 e4895e0f9c45660178e62f2ca4618e47c4f47fd85534dd10d99f787a5531e4b5). |
| `a1exit-scc-trial-workflow-1.json` | **No** | The workflow has the same blob at `Q` (git bca44ac0, sha256 f8c36855...1646). The regenerated file is byte-identical (sha256 67561f97f4fd0236c437468e36c3ee3a5d60d69f5dbb161890357df9847b112f). |
| `a1exit-recon-agents-md-1.json` | **Yes** | `AGENTS.md` at `main` changes, so R2 fails against the record computed at `M`. The record must be superseded: a new id (for example `a1exit-recon-agents-md-2`) with `supersedes` naming the first, and a new review and authorization. |

**Fields of the reconciliation record that change** (values computed now, with `Q` standing in):

| Field | At `M` (draft) | With PR #1553 merged |
|---|---|---|
| `main.computed_at` | 4fb2c1eed350edf95da2b316abcca93717246589 | the actual `main` commit after the merge (unknown now; `Q` in the dry run) |
| `paths[0].side_change_commits` | [4fb2c1ee...] | [4fb2c1ee..., `<the commit on main's first-parent chain that merges #1553>`]: for a merge commit or squash commit that id is unknown now; in the dry run with `Q` as `main`, the three PR commits 4e375f6e, 6a547791, 47e23023 appear instead |
| `paths[0].blobs.M` | git 4a348007, sha256 f75e0d58...eb80, 104517 bytes | git 2503bb8d38c01c907ac2348af91be19f6344e9a8, sha256 702dbf573955cde535f26bc87efd62564f90945af825358558d3746ff6e8ac0e, 105492 bytes |
| `paths[0].main_changes[1]` | insert, bytes [102604, 104517), lines 1524-1551 | insert, bytes [102604, 105492), lines 1524-1572 (the first range [46677, 47031) is unchanged) |
| `paths[0].protected[0]` | §A.49 [102610, 104517), sha256 07c69d0b...107e | §A.49 [102610, 104848), sha256 7601f051ed8b4baf00aa98b8a90429c1cb26f81923a47567bb09e5c100ca2ce3 |
| `paths[0].expected.L` | git 4075b78a, sha256 31bf9ac2...d720, 104494 bytes | git 3ce53ebb93a91a4e1fc6577ed114670226cbe42b, sha256 b7fdda74933ffff369d8550b71b4755b20e3ad6c78eba7469f454f18f907a29a, 105469 bytes |
| `id`, `supersedes` | `a1exit-recon-agents-md-1`, null | a new id; `supersedes` = `{path, blob_sha256}` of the first |

**Fields that do not change:** `scientific_base`, `ledger`, `edits`, `ledger_binding` (PR #1553 touches no ledger), `blobs.H`, the splice entry
(2332 to 2382 at `H` and at `main`, identity translation, counts 1 and 1), `expected.X`,
`length_delta`, `unchanged_ledgered` (43), `side_change_classes` and the item checks.

The dry-run regenerated file has sha256
e2a4b1a377ae5e63c24791077bf2871f4dc68d49799e4d89b5fdf8a90d586d63. That is not the hash a real
regeneration would have, for two reasons:
- `main.computed_at` and `side_change_commits` would name the real merge commit;
- **the dry-run file deliberately keeps the draft's `id` (`a1exit-recon-agents-md-1`) and
  `supersedes` (null).** It is a computation of the changed values, not a superseding record. A real
  regeneration changes both, as the table says: a new id, and `supersedes` naming the first
  record's `{path, blob_sha256}`.

Since none of the drafts was ever reviewed or authorized, an r3 draft that replaces an r2 draft
keeps the same id. The drafts are not records, and no id has been used by a record.

## 8. Draft records

Directory: `records-draft-r3/`, which replaces `records-draft/` (r2, kept as written). The file names are those the records would have in the tool's audit
directory, `verification/audits/<TOOL-AUDIT-DIR>/`. The directory name is a placeholder, since Stage
1 fixes it. Every field is filled from git objects and every hash is computed, except:

- the owner-authorization fields and the review reference, which are explicit `<PLACEHOLDER: ...>`
  values;
- `author`;
- the audit-directory part of the paths in `side_change_classes`.

Each record states inside, in `draft_status`, that it is an unreviewed and unauthorized draft whose
field names follow this proposal and must be reconciled with the implemented schema before review.

| File | sha256 | git blob id | Bytes |
|---|---|---|---|
| `a1exit-recon-agents-md-1.json` | dd725be9004bc47672b90af749d204d3d70175e83d687bdd766a5e7ceb4aec19 | ccb4a1f7b2cb0f3436d621ebdff2a7dda0b06cb7 | 9930 |
| `a1exit-scc-tool-configuration-1.json` | e4895e0f9c45660178e62f2ca4618e47c4f47fd85534dd10d99f787a5531e4b5 | e6f43d4dbb6504424e8289bc656dd5b8f46ec3f2 | 2093 |
| `a1exit-scc-trial-workflow-1.json` | 67561f97f4fd0236c437468e36c3ee3a5d60d69f5dbb161890357df9847b112f | a24eb4f85198cfda67e511f1b30d637168a26d98 | 2507 |

The class records differ from r2's only in `draft_status`, which now names r3. Every other field is
identical. The reconciliation record gains `ledger_binding`, R13 and `edits.git_blob`, and has the
corrected wording of `item_text.R1`, `R6`, `R8`, `R10` and `main.applies_while`. Its
`side_change_classes` pins the r3 class drafts.

**Before review, each draft changes in three ways**, so none of these hashes is final:

- `draft_status` and the `ownership_chain` placeholder block are removed. The review and the
  authorization are separate records that name the record's blob. An authorization cannot sit
  inside the record it authorizes.
- `author` is filled in.
- The placeholder directory is replaced. Because the reconciliation record references the class
  records by path and blob, the class records are finalized first and the reconciliation record
  last.

## 9. Optional points of review-r1 and review-r2

| Point | Decision | Where |
|---|---|---|
| Self-reference of a class record for the tool's own landing paths | **Adopted as a requirement on that record, which is outside this proposal.** It cannot pin its own blob if it lies inside the set it classifies. It must exclude record files from its class: every record, review and authorization file in the audit directory is matched instead by the configuration's `records` list, by `{path, blob_sha256}`, and that class record lists itself nowhere. | 4.1; 5 |
| R11 and the plan amendment; `R`'s tree | **Adopted.** R11 names the plan amendment's own paths, if they are on `main` before `F`, as needing a reviewed class. The `R` pin note is added. | 4.3 |
| Reported form of reconciled drift | **Adopted.** It is reported as a distinct item naming the record, never as `base-drift`. The exact name is left to the implementation. | 4.3; 4.4 P3; 5 |
| PR #1553's current head beside the stale description head | **Adopted.** | 0; 6 |

**Optional points of review-r2:**

| Point | Decision | Where |
|---|---|---|
| Sec. 7: note that the dry-run file keeps `id` and `supersedes` | **Adopted.** The instruction made it required. | 7 |
| Class records: also record the path's first-parent commit list | **Not adopted.** The blob pin already fails closed on any content change, as the review notes. A commit-list pin would also void a class record whenever another commit touched and restored the file, with no change in what is classified. The records keep `introduced_by_first_parent_commit` as provenance. | 2; 8 |
| Manifest count | **Corrected.** `MANIFEST-r2.sha256` has 11 entries, and r2's report wrongly said 13. `MANIFEST-r3.sha256` covers every new r3 file, with the count stated in the report. | `DRIFT-CHANGES-r3.md` |

## 10. What this proposal does not do

- It amends no plan, re-freezes nothing, and designates no `F`.
- It does not move `H` or `W`. It changes no `base_sha256`, `expected_sha256`, splice, pin or
  checker constant.
- It does not suppress `base-drift` or `side-change-unclassified`, and it weakens no check.
- It writes no record into the repository. The files in `records-draft-r3/` (and r2's `records-draft/`) are unreviewed and
  unauthorized drafts that the tool must reject (N11). It writes no review, authorization or
  `retirement-config.json`.
- It does not authorize writing, reviewing or authorizing the records before the tool lands
  (sec. 5). That needs an owner decision.
- It performs no repository, git or GitHub write. It dispatches nothing, rebuilds no trial, executes
  no retirement and merges nothing. It takes no position on whether PR #1553 should merge.
- It decides no scientific question and no row disposition.

The tool outcomes it predicts are the design's stated behaviour. The tool does not exist, so none
is a measured tool result. Every figure is as of `M` = 4fb2c1ee and `Q` = 47e23023.
