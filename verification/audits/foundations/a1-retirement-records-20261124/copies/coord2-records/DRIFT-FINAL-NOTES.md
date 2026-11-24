# A1 drift records: final-form drafts at `main` 8e9b8334 (unreviewed, unauthorized)

## 0. Status, limits and inputs

These notes go with the three draft records in `records-final/`. **Every record is an unreviewed and
unauthorized draft.** Each says so in its `status` field, and each carries explicit placeholders for
the author, the review record and the owner authorization. Nothing here was written to the
repository, to the Stage 1 worktree or to GitHub. The records specify; they authorize nothing, and no
plan, configuration or baseline is changed.

**Inputs**

- **Proposal r3:** `DRIFT-RECONCILIATION-PROPOSAL-r3.md` (sha256 c16ecbb7…2cff) and its drafts in
  `records-draft-r3/`.
- **Review r3:** `review-r3/review-drift-r3.md` (sha256
  d2c78270df3b374e5e8fac2844df2460064154916d00448c4a00048bc0cec021, verdict ACCEPT). Its hash was
  checked before use.
- **Design:** `DESIGN-v5.1.md` (sha256 0c4ff0e6…4fe), which governs meaning.
- **Stage 1 implementation:** commit 8c1e628a08272ad9414929fa8e003020e1cc2234. It is a local commit,
  read through the shared object store of `<repo>`. The worktree was read only and
  not modified. Its audit directory is `verification/audits/foundations/ledger-coverage-tool-20261123/`,
  with schemas and loaders under `tools/ledger_coverage/`. Stage 1 is itself under independent review.

**Commits**

| Name | Commit |
|---|---|
| main | 8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d, the merge of #1553. Parents 4fb2c1ee and a969af58. Read-only `git ls-remote` shows `refs/heads/main` at this commit. The object was already in the local store, so no fetch was run. |
| H | 53c6601a |
| P | 4c79be64 |
| W | 413b0bb8 |
| T1' | 14ac71b4 |

## 1. The final files

The files live in `records-final/` locally. In the tool's audit directory they would be named
`verification/audits/foundations/ledger-coverage-tool-20261123/records/<file>`, following the Stage 1
`records/<topic>-v<N>.json` convention.

| File | sha256 | git blob id | Bytes |
|---|---|---|---|
| `reconciliation-agents-md-v2.json` | 92de0690fee259c1deab6bb13ecd2d958443793e414a00e9c90f4c43f833df85 | 1e235694377fe0c7ac10e6fcd9b13de412151078 | 10313 |
| `side-change-classes-tool-configuration-v1.json` | 9c22394b88702f15b4e8bbc99ff5ef55fc771bc538e2e9c6bafb7bd81ad319cd | 8964e13e65383e4a813eba07881946251ee0c5b3 | 2286 |
| `side-change-classes-trial-workflow-v1.json` | 74fa640d4d18d75b292537f8ee469c8be23aa0be60905c40653e0c5f8bd112ee | 76c00564f7990a27268e59cca6247432fbcc6eb7 | 2691 |

None of these hashes is final. Before review, three things change:

- `status` and the `ownership_chain` block are removed. The block exists only in the draft, because
  an authorization cannot sit inside the record it authorizes.
- `author` is filled in.
- The reconciliation record's `side_change_classes` is updated to pin the finalized class files.

**Generation.** `records-final/work/gen_records_final.py` (sha256 6ff4fe0f…14c8) reads only git
objects and computes git blob ids in memory. It asserts R1 to R13 against `main` while generating and
runs the R13 binding controls in memory. Its output is `work/gen_records_final.out` (sha256
36ae2ebe…94a2).

## 2. The reconciliation record, regenerated at 8e9b8334

**Identity.**
- `record_id` is `reconciliation-agents-md-v2`. This is the new id required by r3 sec. 7. In r3's
  naming it is `a1exit-recon-agents-md-2`; the spelling follows Stage 1 (sec. 4).
- `supersedes` is `{path: "(off-repo draft) coord2-records/records-draft-r3/a1exit-recon-agents-md-1.json",
  blob_sha256: dd725be9…ec19}`, as sec. 7's rule requires. See finding S1: this reference cannot
  resolve in the object store.

**Values, all re-derived from git objects:**

| Field | Value |
|---|---|
| `paths[0].side_change_commits` | [4fb2c1eed350edf95da2b316abcca93717246589 (the #1552 merge), 8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d (the #1553 merge)]. The first-parent chain `H..main` is `413b0bb8`, `4fb2c1ee`, `8e9b8334`. |
| `h` / `h_sha256` | 12a9281fb88c14395b6715a3bf4b4f6b030f433c / d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27 (102250 bytes) |
| `m` / `m_sha256` | 6b1280fa92fa30e36555e9afd30cc0d6e992f5bb / 05bbb27fba2b3dbe55c69be80a7dd1594c53aee66f6b2a837ec25cb379d1893f (105602 bytes) |
| `x` / `x_sha256` | 9f4fc3e830707c90ffc105842d26d5b51f01760b / 59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2 (102227 bytes; equal to T1''s blob and to the ledger's `expected_sha256`) |
| `l` / `l_sha256` | 86d79863821f3f8cdad86771008b2df89fd1961a / 3c334a42cb3d984c9aec5f308c53fb457e747469e200972a1660da392c8fee1b (105579 bytes). This is the expected landing blob at this `main`. The Stage 1 composition `compose_landing` produces the same blob id independently (sec. 5). |
| `main_changes` | insert [46677, 47031), lines 715-718, after H line 714; insert [102604, 105602), lines 1524-1573, after H line 1519 |
| `common_prefix_H_M_bytes` | 46677 |
| D296 | bytes 2332-2382 at H and at `main`; identity translation; `old` count 1 at H and 1 at `main`; character offset 2305; lines 37-38 |
| `protected` §A.49 | [102610, 104821), lines 1527-1555, sha256 d2cb32f0b023b79daa1394b365a4984c02faeafaea82bab8d999e8381b401cc3 |
| `protected` §A.50 | [104826, 105602), lines 1558-1573, sha256 8a9ab5f45be8891b73508725f0e15b495e3222dabca8f00e73edfa3a54ba22b8. The owner's condition names §A.49; §A.50 is listed because the same suffix check (R9) covers it. |
| `length_delta` | −23 |
| `ledger_binding` | unchanged from r3 (926eaa8b…, dd0acccd…, fbb374e2…). Neither #1553 nor anything else touched the ledger. |

**Checks.** R13 and R1 to R12 all hold at 8e9b8334. The R13 controls give the same results as in r3:
P5 and P6 hold, N12 to N18 fail, 0 mismatches.

**The plan's term patterns on AGENTS.md at 8e9b8334** (`work/scans_final.py`, `work/scans_final.out`):

- The whole-file result is unchanged: one occurrence, `A1` on line 38.
- On the 27 lines the #1553 merge adds, every pattern gives 0 hits except `CAPS` ("REST", "API"),
  which applies only to ledger-edit replacement text.
- The output is byte-identical to r1's `scans_r1.out`, because every value matches the earlier
  measurement at 47e23023. In that output the labels "M" and "PR1553" both denote 8e9b8334 here.

**Review-r3's optional points**

- **Adopted:** `unchanged_ledgered` now reads `{count_at_P: 43, note: "informational … R10 checks
  every files entry of the run's ledger, whatever their number"}`. R10's check text says "whatever
  their number".
- **Not changed:** the second point, on who said "13". My r2 report did say "covers all 13 new
  files", so the r3 attribution stands.

## 3. The two class records: what changed

`work/compare_class_records.py` and its `.out` compare r3 and final field by field. In both records
every content field is equal:

- the path;
- the class;
- the blob sha256 and git id at `main` (settings b7f9b0a6 / ad4130d0…; workflow bca44ac0 /
  f8c36855…), which is unchanged at 8e9b8334;
- `blob_at_H`;
- `introduced_by_first_parent_commit` (4fb2c1ee; 413b0bb8);
- `ledgered` and `corpus`;
- the reason and basis;
- `scientific_base` and `supersedes` (null).

**Only these changed:**

- **Renamed to the Stage 1 spelling:**
  - `id` → `record_id`: `a1exit-scc-tool-configuration-1` → `side-change-classes-tool-configuration-v1`,
    and `a1exit-scc-trial-workflow-1` → `side-change-classes-trial-workflow-v1`;
  - `draft_status` → `status`;
  - `items[0]` → `classes[0]`, with `item: SC1` removed (the class id is the item id);
  - `path` → `paths[0]`;
  - `class` → `id`;
  - `blob{git,sha256}` → `git_blob`, `blob_sha256`;
  - `blob_at_H{git,sha256}` → `{git_blob, blob_sha256}`.
- **Placeholder text changed:** `author`, `ownership_chain`, and `checks[0]`, which adds a note that
  Stage 1 matches by path only.

The new `record_id` values are fresh identifiers. No r3 draft id is reused for another meaning.

## 4. Schema differences: r3 proposal versus the Stage 1 implementation

The rule applied: the design governs meaning; the implementation governs spelling where it is
faithful to the design; an unfaithful implementation choice is flagged, not adopted. "Stage 1
dependent" marks a choice that changes if the Stage 1 review changes the implementation.

| # | Item | r3 proposal | Stage 1 (8c1e628a) | Governs, and choice made | Stage 1 dependent |
|---|---|---|---|---|---|
| D1 | Record identifier field | `id` | `record_id` (`records.item_ids` reads `config_id`, `record_id`, `site_id`, `id`) | Implementation spelling: `record_id` | yes |
| D2 | Draft label field | `draft_status` | `status` (its own drafts) | Implementation spelling | yes |
| D3 | Audit directory and file names | `verification/audits/<TOOL-AUDIT-DIR>/a1exit-…-1.json` | `verification/audits/foundations/ledger-coverage-tool-20261123/records/<topic>-v<N>.json` | Implementation: `records/reconciliation-agents-md-v2.json` and `records/side-change-classes-{tool-configuration,trial-workflow}-v1.json` | yes |
| D4 | Class record body | `items: [{item, path, class, blob{…}}]` | `classes: [{id, paths, prefixes?, reason}]`; the review item ids are the class ids | Implementation spelling; the blob pins are kept as extra fields `blob_sha256` and `git_blob` in each class | yes |
| D5 | Blob pin of each classified file | required (review-records B3; design sec. 16.2, read as pinning the classified file) | not read: `_side_class` matches by path or prefix only | **Flagged** (finding S3). Design 16.2 can be read either way, so this is not adopted as a weakening. The records keep the pins, and their `checks` say the tool does not yet read them. | yes |
| D6 | Reconciliation per-path blob fields | `blobs.H/M`, `expected.X/L` (git id and sha256) | `paths[].m` (git blob id at `M`, matched by `_reconciled`) and `paths[].l` (git blob id at `L`, matched at landing) | Implementation spelling `h`, `m`, `x`, `l` (git ids, as v2 sec. 13.3 asks), with `*_sha256` and `bytes` beside them | yes |
| D7 | Review item ids of the reconciliation record | `items: [R1…R13]` with `item_text` | item ids come from a list under `rules`, `sites`, `entries`, `classifications`, `records` or `classes`; `paths` is not one of these, so without such a list the record has a single item (`record_id`) | Proposal meaning (design 6.3: one verdict per item id) in implementation spelling: `entries: [{id: R13, check, holds_at_computed_main}, R1…R12]`. With this, Stage 1 requires a verdict for each of R1 to R13 (`work/item_ids.out`). | yes |
| D8 | `roles.side_change_classes` | one `{path, blob_sha256}` per classified file, plus the class records in `records` | one `{path, blob_sha256}` naming one class record; classes reach `execution` through `--classify` | Both readings of design 16.2 exist. The configuration amendment needs either a list there or the class records in `records` with `--classify` (outside these records). | yes |
| D9 | Supersedes chain | broken chain is `record-invalid` for every record (design 6.3) | checked only for rule files (`cli.rule_files`); not for reconciliation or class records | **Flagged** (finding S4) | yes |
| D10 | Ledger binding R13 | the record applies only if R13 holds | not evaluated: `_reconciled` matches only `path` and `m` | **Flagged** (finding S5). R13 rests on the reviewer unless Stage 1 implements it. | yes |
| D11 | Reconciliation and op C | a reconciliation never changes a decision on `X` (design 13.3; control N2) | `Execution.candidate` raises `record-invalid` for **any** reconciliation that names a path the candidate changes | **Unfaithful; flagged, not adopted** (finding S2) | yes |
| D12 | Landing with a reconciliation | `L` must equal `M` with `C`'s splices at `M`-translated offsets (design 13.1); the record states that blob in advance | `landing`: `if rec and rec.get('l') == l: continue`, so the record's `l` is accepted without the composition check | **Unfaithful; flagged, not adopted** (finding S6) | yes |
| D13 | Author and placeholders | `<PLACEHOLDER: …>` | `_person` accepts any string without `/`, a URL or only digits | Placeholders now contain `/` (`<PLACEHOLDER/author: …>`), so the lint reports "author missing or not a person" in addition to "no review record" | yes |
| D14 | Canonical JSON for R13 | `json.dumps(sort_keys, (',',':'), ensure_ascii=False)`, UTF-8 | `util.canonical`, the same function | Identical; no change | no |
| D15 | Schema ids | `oi-reconciliation/1`, `oi-side-change-classes/1` | the same, listed in `records.record_schemas` | Identical | no |

## 5. Running the Stage 1 tool on a copy, with these records as fixtures

- **The copy.** The tool came from commit 8c1e628a through `git archive 8c1e628a tools/ledger_coverage
  tools/ledger_coverage.py`, a read-only command, into `records-final/work/tool-copy/`. Before use the
  copy was compared with the worktree's `tools/ledger_coverage/` (identical). It was deleted after
  the runs, and the same command recreates it.
- **How it ran.** `python3 -I -B` with `PYTHONDONTWRITEBYTECODE=1`, so no `__pycache__` was written.
  Records and trees were in memory, as Overlay commits: 8c1e628a plus the three records at their
  audit-directory paths. Run outputs are under `records-final/work/tool-runs/`, and the summary is
  `work/tool-runs.out` (sha256 8bb4382d…0cac).
- **Driver and probe.** `work/run_tool_fixtures.py` (sha256 1fd3105b…45cb) drives the runs;
  `work/probe_shortcircuit.py` (sha256 451a9fb2…57e0) is the probe.

| Run | Mode | Result | Reading |
|---|---|---|---|
| execution, `--main 8e9b8334` | chain (the real admission rule) | exit 65, ERROR `CONFIG_UNREVIEWED` | **as expected**; the unreviewed configuration is refused before any record is used |
| execution, predicted `main` (8e9b8334 plus the 49 tool and audit paths, including these records) | chain | exit 65, ERROR `CONFIG_UNREVIEWED` | **as expected** |
| `records.lint_chain` on each record | chain lint | each: "author missing or not a person"; "no review record" | **as expected**: `record-invalid` |
| execution, `--main 8e9b8334`, without these records | harness | exit 20: FAIL `base-drift` on AGENTS.md; REVIEW `side-change-unclassified` on `.claude/settings.json` | countercontrol: the drift is reported |
| execution, `--main 8e9b8334`, with these records | harness | AGENTS.md reconciled (`m` matches); settings classified `tool-configuration`; workflow classified `trial-workflow`; no MAIN item. **Also FAIL `record-invalid` "reconciliation AGENTS.md"** | the records load and match. The `record-invalid` comes from S2, not from the missing review. **Finding.** |
| predicted `main`, with these records | harness | as above; all 49 tool and audit paths classified `tool-landing` | as above |
| predicted `main` plus the composed landing (`compose_landing`) | harness | no landing item; `L:AGENTS.md` = 86d79863…, equal to the record's `l`; the S2 `record-invalid` remains | the composition agrees with the record |
| N4: composed landing with AGENTS.md replaced by X's copy | harness | FAIL `landing-conflict-unresolved` on AGENTS.md | **as proposed** (r3 N4) |
| probe: a record whose `l` names X's copy, and a composed landing with AGENTS.md replaced by X's copy (it drops `main`'s change) | harness | **no** landing item for AGENTS.md | demonstrates S6 |

The harness admits the configuration and the records without their chain, and says so in every
result. Its results are evidence about fit and mechanics, never acceptance.

Two outcomes go beyond `record-invalid` or `CONFIG_UNREVIEWED`:

- the `record-invalid` caused by S2, which appears even when the chain is ignored;
- the absence of a landing conflict in the S6 probe.

## 6. Findings

- **S1 (supersedes of a draft).** `supersedes` follows r3 sec. 7's rule, but it names an off-repo
  draft that was never a record and will never be in the object store.
  - Under design 6.3 a broken supersedes chain is `record-invalid`. Stage 1 would not detect it today
    (S4).
  - Before review the owner or reviewer chooses one of two fixes: (a) set `supersedes` to null,
    because no record with id `…-1` ever existed, which keeps id `-2` and is my recommendation; or
    (b) land the r3 draft first, which serves no purpose.
  - This is the one field that departs from what the design would admit.
- **S2 (unfaithful, Stage 1).** `Execution.candidate` marks `record-invalid` for every reconciliation
  whose path the candidate changes.
  - For a ledgered path that `X` splices and `main` also changed, that is exactly the case
    reconciliation exists for (v2 sec. 13.2, "both changed").
  - The design's rule (13.3; control N2) forbids a record that changes a decision on `X`, not a
    record that names such a path.
  - As implemented, no valid reconciliation of AGENTS.md can pass op C. The sec. 13.4 safeguard could
    therefore never hold for this drift.
  - This should go to the Stage 1 review.
- **S3 (weaker reading, Stage 1).** Class matching ignores blob pins, so a later change to the
  workflow or settings file would stay classified. Under PREREG §31.12.7 a workflow blob other than
  W's voids a trial. The records keep the pins.
- **S4 (Stage 1).** Supersedes chains are checked only for rule files.
- **S5 (Stage 1).** R13, along with R1 (the commit list) and R9 (the protected bytes), is not
  evaluated by the tool. `_reconciled` binds only `path` and `m`. These checks rest on the
  independent reviewer unless Stage 1 adds them.
- **S6 (unfaithful, Stage 1).** At landing, a record's `l` short-circuits the composition rule of
  design 13.1. The probe shows a landing that drops `main`'s AGENTS.md change, with no MAIN item,
  under a record that names that blob. The design requires `L` to equal the composition, so `l`
  should be accepted only when it also equals `translate_onto_main`. These records set `l` to the
  composition (86d79863…, confirmed by Stage 1's own `compose_landing`), so they are unaffected.
- **S7 (overlap).** Stage 1's own draft `records/side-change-classes-v1.json` also defines
  `trial-workflow`, by path only, beside `tool-landing`. The configuration should reference one
  trial-workflow class. My recommendation is that Stage 1's record keep only `tool-landing`, and that
  `.claude/settings.json` be covered by the record here. This is Stage 1 dependent.

## 7. Not verifiable

- Whether the Stage 1 review will change any field spelling, S2, S3, S4, S5 or S6. Every "yes" in
  sec. 4 may move.
- The final hashes, which change at finalization (sec. 1).
- Anything merged to `main` after 8e9b8334.
- The owner decision still needed: authorizing these records before the tool lands. At 8e9b8334,
  §A.50 item 2 requires the owner's approval each time for freezing a plan that changes the posit
  ledger, which the A1 plan does. Whether authorizing records before the freeze is such an act is for
  the owner to say.

## 8. Manifest

`MANIFEST-final.sha256` covers every new file:

- these notes;
- the three records;
- `records-final/work/` (scripts, outputs and `tool-runs/`).
