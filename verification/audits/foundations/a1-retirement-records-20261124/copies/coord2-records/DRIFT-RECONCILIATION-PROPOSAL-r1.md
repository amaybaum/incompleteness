# A1 plan: reconciliation of `main` drift after the scientific base (revision 1, for review)

## 0. Status, authority and goal link

This is a paper-only proposal. It changes no plan, record, ledger or baseline, writes nothing to the
repository or to GitHub, and authorizes nothing.

- It supersedes `DRIFT-RECONCILIATION-PROPOSAL.md` (sha256
  f870c7630b41ecf0cd218a2a525ae4a7941d1942978633b654d8040628aa2c2d), which stays as written. It
  applies the required corrections 1 to 6 for document B of the independent review
  `review/review-records.md` (sha256
  1ef18f194efa1c2055874f0ccac51ef55b902e1dcd2e6420af05859ef256a5f8, verdict on B: REVISE).
  `DRIFT-CHANGES-r1.md` maps each correction and owner decision to the sections below.
- Design: `DESIGN-v5.1.md` (sha256
  0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe), accepted as the final reviewed
  design. The sections used are 6.3 (records and the ownership chain), 13 (four trees) and 16.2
  (configuration). Section 13 opens with "The v2 sec. 13 rules stand, with the corrections below";
  the content list of a reconciliation record is therefore v2 sec. 13.3, read with v5.1 sec. 13.1.
- Owner decisions:
  - #1169 comment 7093128173 (`amaybaum`, 2026-11-23T06:13:50Z): the exception-free verification
    route. It keeps `H` as the immutable scientific base: "No change to the ledger base H ... is
    authorized".
  - #1169 comment 7099655517 (`amaybaum`, 2026-11-23T11:26:50Z; author and time read with `gh api`
    GET). It records Stage 1's authorization, and it treats the §A.49 merge as a real baseline change. The drift failure is not suppressed
    and no baseline is updated silently. `H` is kept unchanged. `.claude/settings.json` is
    classified as tool configuration and `.github/workflows/a1exit-trial-verify.yml` as the trial
    workflow. The owner chose "a reconciliation record frozen together with the re-frozen plan".
    That record must show that splice D296 still identifies exactly one location, yields the
    approved text and changes no byte of §A.49. The comment approves an approach only: "no plan
    amendment, re-freeze, trial rebuild, CI dispatch, retirement execution or merge is authorized".
- Goal link (AGENTS.md §A.47): A1-EXIT (#1169), the exception-free verification route. This proposal
  decides how the drift of the ledgered file `AGENTS.md` after `H` is reconciled at the plan's
  re-freeze. It decides no scientific question and no row disposition.

| Symbol | Commit |
|---|---|
| `H` | 53c6601a10419b6b333cc992474272501ab542af, the scientific base (ledger base) |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6, the frozen plan (`verification/audits/foundations/a1exit-deletion-20261121/`) |
| `W` | 413b0bb88f39cad901befcf4684355c7ee39480b, the workflow base of PREREG §31.12.7 (Merge #1543) |
| `M` | 4fb2c1eed350edf95da2b316abcca93717246589, `main` today (Merge #1552; `git ls-remote` read-only confirms `refs/heads/main` = `M`) |
| `T1'` | 14ac71b4b0a0c0aa2d7068d6799a73f474097060, the trial tree |
| `F` | the future freeze of the amended plan |
| `M_F` | `main` as resolved at `F` |
| `X`, `C`, `L` | candidate, certified execution head, landing merge (design notation) |
| PR #1553 head | 47e23023450fb8fcbd61b5c776a69ba61897f267 (open draft, not merged) |

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
  - `M + D296` has sha256 31bf9ac238e8017d48e8c03b2aaec396e2f38e3c2f7472fdb5df4d1ab8c5d720.
  - `H + D296` has sha256 59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2. This is
    byte-identical to `AGENTS.md` at `T1'` and equals the ledger's `expected_sha256`.
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

## 2. Classification of each side change (correction 3)

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
- **The class record.** One record, schema `oi-side-change-classes/1`, carries two items:
  - SC1: path, git blob b7f9b0a6, sha256 ad4130d0...5b9b, class `tool-configuration`, first-parent
    commit `4fb2c1ee`, reason as above;
  - SC2: path, git blob bca44ac0, sha256 f8c36855...1646, class `trial-workflow`, first-parent
    commit `413b0bb8`, reason citing PREREG §31.12.7.

  It is referenced with its review and authorization records in `records` as `{kind, path,
  blob_sha256}`.

A later change to either file gives a blob that differs from the pinned one. That file is then
unclassified again (REVIEW) until a new class record covers it. For the workflow this agrees with
§31.12.7, under which a dispatch head whose workflow blob is not `W`'s is void.

A class covers only non-ledgered, non-corpus paths. It never covers `AGENTS.md`.

## 3. The approach for `AGENTS.md` (corrections 4 and 5)

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
The record states that blob in advance as a sha256 and proves that it is the composition the rule
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

### 4.1 Location and ownership chain (sec. 6.3, sec. 16.2)

- **Location.** One immutable JSON file, schema `oi-reconciliation/1` (an engine schema id, sec.
  16.1), in the amended plan's record directory. Records frozen with the plan live there (sec. 6.3,
  sec. 12.1).
- **Writer.** The record's `author` field names the writer, who may not review it.
- **Review.** An independent non-author review record, schema `oi-review-record/1`, has `reviewed` =
  `{path, blob_sha256}` of exactly this record's blob. Its `method` names every object id read, and
  its `verdicts` give one entry per item id (sec. 4.3), each `accept`. A review that cites only a
  passing tool run is invalid.
- **Owner authorization.** An authorization record, schema `oi-owner-authorization/1`, quotes the
  owner's comment with `owner`, `time` and `comment_id`. It lists `authorizes: [{record: {path,
  blob_sha256}, review: {path, blob_sha256}}]`. One authorization may also cover the side-change
  class record and its review (sec. 2).
- **Frozen configuration.** `retirement-config.json` at `F` lists the record, its review and its
  authorization in `records` as `{kind, path, blob_sha256}`. It lists the two classified files in
  `roles.side_change_classes` (sec. 2). Its own sha256 is in `F`'s PREREG pin table, the root of
  trust. A changed record is a new record with `supersedes`, a new review and a new authorization.
  It is never edited in place, and no id is reused.

### 4.2 Content

The design fixes the schema id and the content list (v2 sec. 13.3: `M`, the paths covered, per-path
blob ids and resolution, the splices re-verified against `M` and translated by `M`'s own change,
and the reviewer and owner record). It gives no field-level schema. The fields below are this
proposal's rendering of that list. If the engine's `oi-reconciliation/1` JSON Schema, implemented in
Stage 1, names them differently, the record follows the schema, and the content below stays the
requirement.

A record written before `F` cannot name blob ids of `X`, `C` or `L`, which do not exist yet. It
names their expected sha256 instead, and the landing check compares the real blobs with them.

```text
schema             oi-reconciliation/1
id                 a1exit-recon-agents-md-<n>          (never reused)
supersedes         null | {path, blob_sha256}
author             <writer>
scientific_base    53c6601a10419b6b333cc992474272501ab542af   (= roles.scientific_base)
main               {commit: <M_F>, resolved_by: "git ls-remote origin refs/heads/main", resolved_at: <time>}
ledger             {path: <plan dir>/ledger.json, blob_sha256: <as pinned at F>}
paths: [ {
  path               AGENTS.md
  class              ledgered
  side_change_commits [first-parent commits on H..M_F that change AGENTS.md]   (today: [4fb2c1ee...])
  blobs              {H: {git: 12a9281f..., sha256: d87acac5...7e27},
                      M: {git: <at M_F>, sha256: <at M_F>}}
  main_changes       [byte ranges of M_F not in H, as [start, end) in M_F]
                      (today: [46677, 47031) lessons register; [102604, 104517) §A.49 block)
  splices: [ {id: D296, start_H: 2332, end_H: 2382, start_M: <2332 today>, end_M: <2382 today>,
              translation: "identity" | <offset delta>,
              old_sha256: 8711166b...0e6f, new_sha256: 532c5919...f051,
              old_count_H: 1, old_count_M: 1} ]
  protected: [ {name: "§A.49", header: "## §A.49", start_M: <102610 today>, end_M: <section end at M_F>,
                sha256: <today 07c69d0b...107e>} ]
  expected           {X_sha256: 59b68984...82ce2   (= ledger files.AGENTS.md.expected_sha256 = H + D296),
                      L_sha256: <sha256(M_F + D296); today 31bf9ac2...d720>}
  resolution         "L = M_F with C's splices applied at M-translated offsets (sec. 13.1)"
} ]
unchanged_ledgered  {count: 43, rule: "blob at M_F equals blob at H for every other ledger files entry"}
unchanged_corpus    {rule: "no corpus path (configuration `corpus`) and no generated corpus artifact differs between H and M_F"}
side_change_classes {path, blob_sha256} of the oi-side-change-classes/1 record (sec. 2)
changes_decisions_on_X  []                       (must be empty; sec. 13.3)
items              R1 ... R12 (sec. 4.3)
```

The record asserts exactly these facts:

- the drift on `AGENTS.md` between `H` and `M_F` comes only from the listed first-parent commits;
- D296's `old` text occurs exactly once at `H` and exactly once at `M_F`, and the span translates
  as stated;
- applying D296 at `M_F` yields the approved `new` text in place, and the stated `L` sha256;
- D296 changes no byte of §A.49 as it stands at `M_F`, nor any other byte after the splice;
- every other ledgered path and every corpus path is unchanged from `H` to `M_F`;
- the record changes no decision on `X`.

### 4.3 Checks a verifier runs from git objects

Each check reads only the object store (`git cat-file`, `git rev-list`, `git diff --name-status`)
and the pinned record files. Each is one item id of the record, so the reviewer gives one verdict
for each and the tool evaluates each one. Bytes are compared as bytes, and offsets are byte offsets.

| Item | Check | Result at `M` today |
|---|---|---|
| R1 | `M_F` equals `git ls-remote origin refs/heads/main` at `F`; `H` is on `M_F`'s first-parent chain; the first-parent commits on `H..M_F` that change `AGENTS.md` are exactly `side_change_commits` | `[4fb2c1ee]` |
| R2 | `AGENTS.md` blob at `M_F` has the recorded git id and sha256 | f75e0d58...eb80 |
| R3 | **Uniqueness at `H`:** the number of occurrences of D296's `old` bytes in `H`'s blob, counting overlaps (byte search advancing by one), is 1, at `start_H` = 2332; `sha256(H[2332:2382])` = `old_sha256` | 1 at 2332 |
| R4 | **Uniqueness at `M_F`:** the same count in `M_F`'s blob is 1, at `start_M`; `sha256(M_F[start_M:end_M])` = `old_sha256` | 1 at 2332 |
| R5 | **Translation:** let `p` be the length of the common byte prefix of `H` and `M_F`. If `p ≥ end_H`, the translation is the identity and `start_M = start_H`. Otherwise the record's delta must equal the byte-length change of `M_F`'s edits wholly before `start_H`, and no `main_changes` range may intersect `[start_M, end_M)` | `p` = 46677 ≥ 2382: identity |
| R6 | **Approved text:** `Lx = M_F[:start_M] + new + M_F[end_M:]`; `Lx[start_M : start_M+len(new)] == new`; `sha256(new)` = `new_sha256`; the lines of `Lx` that contain the splice and its sentence (36-39 today) equal those lines of `H + D296` (= `T1'`'s) | holds |
| R7 | **Expected landing blob:** `sha256(Lx)` = `expected.L_sha256` | 31bf9ac2...d720 |
| R8 | **Expected candidate blob:** `sha256(H + D296)` = `expected.X_sha256` = ledger `expected_sha256` | 59b68984...82ce2 |
| R9 | **§A.49 untouched:** `## §A.49` occurs exactly once in `M_F` and once in `Lx`, at byte `a` ≥ `end_M`; with `δ = len(new) − len(old)` (−23), `Lx[a+δ : b+δ] == M_F[a:b]`, where `[a, b)` is §A.49's extent at `M_F` (from its header to the start of the next line that is exactly `***`, or the end of the file); its sha256 is the recorded one. In addition `Lx[end_M+δ:] == M_F[end_M:]` (no byte after the splice changes) | §A.49 = [102610, 104517); equal |
| R10 | **Other ledgered paths:** for each of the 43 other `files` entries of the pinned `ledger.json`, the blob id at `M_F` equals that at `H`, and its sha256 equals `base_sha256` | 43 of 43 |
| R11 | **Corpus:** `git diff --name-status H M_F` lists no corpus path and no generated corpus artifact; every listed path other than `AGENTS.md` is covered by a pinned side-change class (sec. 2) or by another reviewed class record (for example the tool's landing paths) | only the two classified files |
| R12 | `changes_decisions_on_X` is empty, and no item names a candidate or retirement check | empty |

At landing the tool runs the same checks against the `M` it resolves then (sec. 13.4), and also
requires `sha256(L:AGENTS.md)` = `expected.L_sha256`. The record applies only while the landing
`M`'s `AGENTS.md` blob equals the recorded one. Otherwise it does not apply, and the result is
`base-drift` (control N7 below).

### 4.4 Controls in both directions

All controls run in memory: synthetic commit objects held by the tool's reader, as for RT-L and
RT-L2. No commit, ref or merge is created in the repository.

**Positive controls (the record must apply and the composition must PASS):**

| Id | Case | Expected |
|---|---|---|
| P1 | real objects `H`, `M` = 4fb2c1ee, today's figures | R1-R12 hold; `L` sha256 31bf9ac2...d720 |
| P2 | real objects with PR #1553's head 47e23023 standing in for `main` (a dry run of sec. 5, no claim that it merges) | R2-R12 hold against that tree; `L` sha256 b7fdda74933ffff369d8550b71b4755b20e3ad6c78eba7469f454f18f907a29a |
| P3 | an in-memory landing with parents (`M`, an `X` = `H` + all splices, as `T1'`), composed under the record | landing composition PASS; `AGENTS.md` at `L` has sha256 = `expected.L_sha256`; the workflow at `L` equals `W`'s blob |
| P4 | synthetic `M′` with one line inserted before byte 2332, and a record carrying the correct delta | R4-R9 hold at the translated offset (the translation path is exercised) |

**Negative controls (each must fail with the named outcome):**

| Id | Case | Expected |
|---|---|---|
| N0 | `M` today with no reconciliation record | FAIL `base-drift` on `AGENTS.md` (the drift is reported, not suppressed) |
| N1 | `M′` = `M` with a second copy of D296's `old` text added after §A.49 | R4 fails (count 2); record invalid; `base-drift` |
| N2 | `M′` with one byte changed inside [2332, 2382) | R4 fails (`old_sha256`); FAIL |
| N3 | P4's `M′` with a record still claiming the identity translation | R4/R5 fail; FAIL |
| N4 | a record whose `expected.L_sha256` is `H + D296` (59b68984...) | R7 fails; an `L` built to it FAILs `landing-drops-main-change` |
| N5 | an `L` whose `AGENTS.md` also changes one byte of §A.49 | R9 fails; FAIL |
| N6 | `M′` that also changes one byte of another ledgered file (for example `papers/Main.md`) | R10 fails; `base-drift` on that path, which the record does not cover |
| N7 | landing `M` whose `AGENTS.md` blob differs from the recorded one | record does not apply; `base-drift` |
| N8 | the record with `reviewer` = `author`; a review naming another blob; an authorization naming the path without a hash | FAIL `record-invalid` (design controls O1, O2, O4) |
| N9 | the record with a non-empty `changes_decisions_on_X` | FAIL `record-invalid` (design control N2) |
| N10 | the class record pinning the workflow at `H`'s blob (5c767c9f...e747) instead of `W`'s | the workflow path is REVIEW `side-change-unclassified` at `M` |

## 5. Expected Stage 1 result and the sec. 13.4 safeguard (correction 6)

**Stage 1 (authorized by the owner, recorded in c.7099655517; local only, no push).** Its predicted
`main` check runs RT-L2 in memory against a predicted `M` = 4fb2c1ee plus the tool's landing paths.
It uses the A1 configuration as it stands, without the reconciliation and class records, which are
not yet written, reviewed or authorized. The expected result is:

- `AGENTS.md`: FAIL `base-drift` (exit 20);
- `.claude/settings.json` and `.github/workflows/a1exit-trial-verify.yml`: REVIEW
  `side-change-unclassified`;
- overall: FAIL.

This result is correct. It is reported as measured, not suppressed, and no baseline is changed to
avoid it. Unreviewed draft records used as fixtures must give FAIL `record-invalid`, not a pass.
Stage 1 tests the reconciliation mechanism itself through the synthetic controls of sec. 4.4 and the
design's R7/R8 pair. It does not test it through real A1 records.

**Sec. 13.4's requirement.** Before the tool lands, RT-L2 against a predicted `M` that contains the
tool's landing paths must show "every side change classified and no `base-drift`". The tool lands
before `F`. That safeguard is therefore met as follows:

1. **Records before the tool lands.** The reconciliation record and the side-change class record are
   written, independently reviewed and owner-authorized, each by exact blob, before the tool lands.
   A class record for the tool's own landing paths is also needed. It is outside this proposal but
   is required for the same check.
2. **Predicted configuration.** RT-L2 runs against the predicted `M` with a predicted configuration
   that references those records by `{path, blob_sha256}`. The expected result: `AGENTS.md`
   reconciled (R1-R12 hold; no `base-drift`), and the two classified files and the tool's paths
   classified.
3. **Freeze unchanged.** At `F`, the same record blobs are frozen with the amended plan. R1-R12 are
   re-run against `M_F`. If `main`'s `AGENTS.md` or any ledgered or corpus path changed between the
   safeguard run and `F`, the record is superseded (new record, review and authorization), and
   RT-L2 is re-run before `F`. A record that no longer matches is never carried into `F`.

Step 1 asks the owner to authorize the records before the tool lands, and before the plan's
re-freeze. That is an owner act which c.7099655517 does not yet grant. If the owner prefers to
authorize the records only at `F`, the safeguard's wording in sec. 13.4 would need the owner's
amendment. This proposal does not propose that amendment.

## 6. PR #1553 and further drift

PR #1553 (open draft, base `M`, head 47e23023) has three commits on `M`:

- 4e375f6e "footer rule in §A.49; §A.50 standing owner approvals";
- 6a547791 "apply the independent review's required corrections";
- 47e23023 "§A.49 rule 2: footer handling observed per operation".

It changes only `AGENTS.md` (+27 / -6). Its description still names head 6a547791.

**What changes if it merges before the re-freeze** (re-derived from 47e23023 against `M`):

- `AGENTS.md` changes from sha256 f75e0d58...eb80 to 702dbf573955cde535f26bc87efd62564f90945af825358558d3746ff6e8ac0e
  (git 2503bb8d, 105492 bytes, 1572 lines).
- The first byte that differs from `M` is 103702 (line 1542), inside §A.49 rule 2. There are two
  hunks:
  - `M` lines 1542-1546 are replaced by 8 lines (rule 2's expected text and the observed footer
    handling);
  - `M` line 1551, the adoption line, is replaced by 19 lines: the adoption line with "rule 2
    amended the same day (#1169 comment 7099599721)", a `***` rule, and a new §A.50, "Actions that
    need the owner's approval each time".
- **D296's span is untouched.** The `old` text occurs exactly once, at bytes 2332 to 2382 (lines
  37-38), and lines 37-38 are byte-identical to `M`'s. The translation from `H` stays the identity
  (common prefix with `H` is still 46677 bytes).
- **§A.49 itself changes.** At 47e23023, §A.49 spans bytes [102610, 104848) and §A.50 starts at
  104853. "No byte of §A.49 changes" is a property of D296 relative to §A.49 as it stands at `M_F`,
  so R9 is evaluated on that text: D296 at 47e23023 leaves every byte after the splice, §A.49 and
  §A.50 included, unchanged. `47e23023 + D296` has sha256 b7fdda74...a29a.
- No other ledgered file and neither classified file changes. The workflow and settings blobs at
  47e23023 are `M`'s.
- **Plan patterns.** On the 27 added lines, the tree-scan patterns `PTR`, `REPO_PAT`, `IDENT` and
  `CRIT5` give 0 hits. So do `ASSERTS_FINITE`, `INF`, `NEUTRAL`, `REG`, `SCOPED`, `STRONG_ONLY` and
  `WEAK`. `CAPS` matches "REST" and "API", but `edits_check.py` applies `CAPS` and `REG` only to the
  replacement text of ledger edits of certain kinds (line 379), never to tree content, so these do
  not bear on any plan check. On the whole file at 47e23023, `PTR` and `REPO_PAT` still give the one
  occurrence on line 38. The PR's own review is reported to have found zero hits. This proposal could
  not find that review on GitHub (the PR has no reviews and no comments), so it rests on the
  measurement above alone.
- If merged, §A.50 item 2 requires the owner's approval each time for "amending, freezing or
  executing the posit-retirement plan of #1169". The re-freeze that carries this record falls under
  it.

**Consequence for the record.** The record is computed against `main` at freeze time, `M_F`, not
against today's `M`. If #1553 (or anything else touching `AGENTS.md`) merges before `F`:

- `blobs.M`, `side_change_commits`, `main_changes`, `protected` (§A.49's extent and hash) and
  `expected.L_sha256` take their `M_F` values (with #1553 alone, `L` would be b7fdda74...a29a and
  `side_change_commits` would add #1553's merge commit);
- a record already authorized against an earlier `main` is superseded before `F`;
- RT-L2 is re-run as in sec. 5, step 3.

A change to `AGENTS.md` after `F` and before landing was not foreseeable at `F`. Sec. 13.3 then
admits a new post-`F` record for it, under the same chain. That record never changes a decision on
`X`.

## 7. What this proposal does not do

- It amends no plan. It does not re-freeze `P` and does not designate `F`.
- It does not move `H` or `W`, and does not change any `base_sha256`, `expected_sha256`, splice,
  pin or checker constant.
- It does not suppress `base-drift` or `side-change-unclassified`, and does not weaken any check of
  the design or the plan.
- It writes no reconciliation, class, review or authorization record, and no
  `retirement-config.json`. The record content in sec. 4 is a specification for review.
- It does not authorize writing those records before the tool lands (sec. 5, step 1). That needs an
  owner decision.
- It performs no repository, git or GitHub write. It dispatches no workflow, rebuilds no trial,
  executes no retirement and merges nothing. It takes no position on whether PR #1553 should merge.
- It decides no scientific question and no row disposition.

The tool outcomes it predicts are the design's stated behaviour. The tool does not exist yet, so none
of them is a measured tool result. Every figure is as of `M` = 4fb2c1ee and PR #1553's head 47e23023.
Later commits on `main` require the record to be recomputed (sec. 6).
