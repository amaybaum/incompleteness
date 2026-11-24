# Q10: provenance disposition of the off-`main` citations in the ledger coverage tool landing (AGENTS.md §A.42 item 8)

Prepared locally and read-only on 2026-11-24 for the owner decision of 2026-11-24 (owner `amaybaum`, Q10, narrow
option (c)). No repository file was changed, nothing was committed or pushed, and nothing was written to GitHub.
This document records each reference and what depends on it. It changes no recorded value and does not amend the
frozen plan. It decides nothing: classifications are findings for the owner, and escalations need the owner's
separate decision.

## 0. Inputs and method

| Item | Value |
|---|---|
| Tool landing tree | worktree `coord2-impl-wt` at `443e871f225a414f69bef3f1e3cab45cb30d6594` (clean; 55 landed paths, identical to the S1 review's `landed-files.txt`) |
| `main` | `9deb69568d8231210c7f39cb65be943dea566371` (`origin/main`, re-fetched by branch name, unchanged) |
| P | `4c79be642ca631573f06b444903be75ec4f5e2b6`, frozen A1 plan; refs `research/a1exit-deletion-20261121`, `refs/pull/1477/head` |
| T1′ | `14ac71b4b0a0c0aa2d7068d6799a73f474097060`, "Trial T1′: T0′ with the nine CI-built PDFs"; single parent H; ref `trial/a1exit-T1prime-4c79be64` |
| H | `53c6601a10419b6b333cc992474272501ab542af` (on `main`) |
| Design | `DESIGN-v5.5.9.md`, sha256 `cdfbe08c…7df9` |
| Staged A1 configuration (draft, outside the repository) | `impl-stage1-s1/staging/…/a1exit-deletion-20261121/retirement-config.json`, sha256 `75558ee3a32c6c3c1efa396e155d87db09e2ce3d3398ffd1da7aa8521fed7c99` |

**Reachability, re-verified against `9deb6956`** by GitHub compare GET (`compare/<c>...9deb6956`). The local clone is
shallow (boundary around 2026-10-31), so a local `git merge-base --is-ancestor` gives a false negative for
`ca3a5bb2` (it returned 1). The host compare is authoritative here.

| Commit | Status vs `9deb6956` | Reachable from `main` |
|---|---|---|
| `14ac71b4…` (T1′) | diverged, ahead 21, behind 1, merge base H | **no** |
| `4c79be64…` (P) | diverged, ahead 111, behind 50, merge base `1c7eedc4` | **no** |
| `53c6601a…` (H), `413b0bb8…` (W), `e837e3db…` (E), `8e9b8334…` (M), `4fb2c1ee…`, `ca3a5bb2…` | ahead, behind 0 | yes |

**Completeness.** I scanned all 55 landed files at `443e871f` for 40-hex ids: 89 occurrences of 64 distinct ids.
The only commits not reachable from `main` are T1′ and P. Of the blob ids, 54 lie in the landing tree and `12a9281f`
lies in H's tree. Two do not: `9f4fc3e8…` (T1′'s `AGENTS.md`, which exists in the repository only off `main`) and
`86d79863…` (a computed value that is no object, sec. 4). Files citing T1′ or P by full id: the six records, plus
`controls.json`, `a1_controls.py` and `README.md` (sec. 3). `a1_conformance.py` reaches T1′ and P through
`a1_controls`' constants and holds the two blob ids. This agrees with the S1 review's sec. 5 and `hex-objects.tsv`.

**Is the true set six?** Yes. Six *records* (rule or record files read by the engine under the configuration) cite T1′
or P: the six the owner named. A seventh JSON file, `controls.json`, also cites T1′. It is the preregistered control
set, not an `oi-*` record of sec. 6.3, and no admission reads its T1′ input (sec. 3.4). The code trace below does not
confirm the S1 writer's label "load-bearing" for all six. Mechanically, the engine reads off-`main` content when it
admits two of them (`w1-w2-allow`: T1′; `register-infinity-params`: P, through the configuration rather than the
record's own field). Two others carry claims whose support is off `main` (`repo-scope`: P; `gr58`: T1′). In the last
two (`dr-deny`, `resid`) the T1′ citation is not used. The engine reads no file's top-level `recorded_at` (checked by
grep of `engine/` and `adapters/`: only the per-rule `rule['recorded_at']` of allow rules is read, at `rules.py:118`,
`:155` and `pipeline.py:719`).

**Which admission decisions exist** (design v5.5.9 sec. 6.3, 15 item 0a, 16.2; traced in code):

1. **Authority admission** (`A`, `engine/authority.py`) and **freeze-ledger admission**: these read `A`, the
   plan thread, the freeze ledger and snapshots. They read none of the six (no reference to the audit directory or
   to `rules/`/`records/` in `authority.py`).
2. **TR5**: `NOT RUN` (`conformance_controls.py:139`). TR5-sim runs on the in-memory host with a synthetic world
   (`conformance_controls.py:125-138`) and reads none of the six.
3. **A1 controls** (`a1_controls.py`, `a1_conformance.py`): control harness only, `"admission": "control-harness"`,
   never acceptable (design sec. 5, 10.4; X11). Their results are evidence about the implementation, not admission.
4. **The A1 retirement's own runs at `F`.** The configuration `retirement-config.json` is frozen with the plan and
   pins records by `{path, blob_sha256}`. The staged draft pins all six with sha256 equal to the bytes at
   `443e871f`. The engine reads each pinned record at `F` (`config.py:185-188`), admits allow, deny and pattern rule
   files only if their lint passes (`cli.py:196-246`), admits scope and classification records only through the
   chain (`cli.py:165-193`, `records.lint_chain`), and uses them in op D (`terms`: item 7, item 11, items 5/6) and in
   RT-T/RT-D. **All six are therefore essential to A1 retirement decisions once `F`'s configuration references
   them. None is essential to an admission decision of the tool landing itself (points 1-3).**

## 1. Disposition table

Classification column, per §A.42 item 8: **prov** = provenance (the claim does not use the content); **main** = support
on `main`; **gap** = support off `main`.

| # | Record (under `verification/audits/foundations/ledger-coverage-tool-20261123/`) | git blob @443e871f | sha256 | Off-`main` citation (field → id) | What reads it (file:line) and what it does with the commit | §A.42 item 8 | Required admission evidence? | Reproducible from `main` alone? |
|---|---|---|---|---|---|---|---|---|
| R1 | `rules/w1-w2-allow-v1.json` (`a1-allow-w1-w2-v1`; allow rules W1-a…d, W2-a, W2-b; 11 fingerprints) | `bf1882fb74938164d67602f5d482f9dd2d09ff49` | `0cbb97c98725cba618598650b0cd9c687c97e280b3422c4ad6e62794a222b171` | top-level `recorded_at` → T1′ (line 6; not read); `rules[0..5].recorded_at` → T1′ (lines 41, 92, 149, 200, 250, 301; **read**) | `cli.py:236` → `rules.lint_rule` `rules.py:118`, `:155`: every fingerprint must be reproduced by a sentence of its file **at T1′** (sentence and context sha256; self-pass). A failure makes the file `record-invalid` (`cli.py:243-246`) and its allow rules are not admitted. `pipeline.py:719-720`: `is_ancestor(commit, T1′)` decides whether `rule-stale` is evaluated | **gap** (the per-rule `recorded_at` values) / **prov** (top-level `recorded_at`) | **Yes**, for A1 decisions: its admission as a rule file depends on reading T1′. The W1/W2 PASS of the 7 W1 lines and 4 W2 lines in RT-D, item 7 (`--final`) and RT-I7A depends on it. Not for the tool landing | **No.** Missing from `main`: commit and tree T1′, and T1′'s blobs `papers/SM.md` `c358068f31be6d0a1f4f1a97f00fe2d394dc0904`, `book/ch09-universality.md` `289d171045cad1775a56abc6c0753bf901ce24bc`, `book/ch19-open-problems.md` `f2c149599ff7aa0d56b5f6b58a7118612a31f53e`, `book/The-Incompleteness-of-Observation-FULL.md` `c931331635dd8de7da180f6dcd00efe80192ca2b` (`book/appendix-b-derivations.md` `f91b596d…` is on `main`). See note R1 |
| R2 | `rules/dr-deny-v1.json` (`a1-deny-v1`; DR-1, DR-3, DR-4, DR-5) | `3f06edffb2bfb21a1d1d6d13ecfc5208d0154d15` | `daf3a8e231ace391f0037447d1266d1255df8dc015baaaa601fcc79b63cec6ae` | top-level `recorded_at` → T1′ (line 6) | **Nothing reads it.** Deny rules have no per-rule `recorded_at` (`rules.deny_fields`). The lint (`rules.py:168-206`) reads only the examples (literals in the record) and the countercontrols: H lines (on `main`) and control input `agents-md-at-H` (H blob `12a9281f`, on `main`) | **prov** | Yes for A1 decisions (deny profiles DR-1…DR-5 of item 7). The T1′ citation plays no part in that admission | **Yes** (H and `controls.json`'s H input). The design's measurement "0 matches at T1′" is not stated in the record |
| R3 | `rules/resid-v1.json` (`a1-resid-v1`; review pattern resid-a/b/c) | `ba1cc9117103f11d0cd8c39d0c33e52529fea226` | `7aa1412206f7bf5fec1d3573d76e1b91c0f6bc8f67704a1dcb75344d09aac221` | top-level `recorded_at` → T1′ (line 6) | **Nothing reads it.** A `review-pattern` rule is linted on its patterns and examples only (`rules.pattern_fields`, `rules.py:168-189`; the countercontrol branch at `:190` is deny-only) | **prov** | Yes for A1 decisions (the `resid` review profile). The T1′ citation plays no part | **Yes** |
| R4 | `rules/register-infinity-params-v1.json` (`a1-register-infinity-params-v1`; kind `params`) | `229877fdf25c16e33295ba2ac2fa8614340bc993` | `05149ba694dd4017ad27dd60c02810403ec7351036776bea212768ba9ebc509f` | top-level `recorded_at` → P (line 6; not read); `rules[0].lint.checker.commit` → P (line 38; **not read** by the engine) | `cli.py:224-233` → `peredit.lint_params` (`peredit.py:132-158`): each parameter must equal a literal of the plan checker's `static_new`/`inf_key`, and the splitter must equal `sentences`' `re.split` argument. The checker source is **the configuration's `adapters.ledger.companion[role=checker]`** (`cli.py:517-523`), which the staged configuration pins to P's `edits_check.py` (commit P, sha256 `2856e58c…`). It is not the record's `lint.checker` field. The admitted params then drive the per-edit unit of items 5/6 (`peredit.evaluate`) over P's `ledger.json`/`edits.json` | **gap** (the parameters' claimed equality to P's checker); **prov** for the record's own two P fields as the engine reads them | **Yes**, for A1 decisions: without an admitted params rule the per-edit unit fails closed (`peredit.py:111-114`). Not for the tool landing | **No.** Missing: `verification/audits/foundations/a1exit-deletion-20261121/edits_check.py` @P, blob `1153e039d7223742de56a54ed201e8358324c742`, sha256 `2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c` (the plan directory does not exist on `main`). See note R4 |
| R5 | `records/repo-scope-v1.json` (`repo-scope-v1`; `oi-scope/1`) | `70ff5ac6f7e1b3c6e2127840081a84ac176ba7b7` | `32afecca8e371a1f51217a70058676144e874b24526ca0becddea04e2c12df42` | `source.commit` → P (line 9), with `source.path` = P's `edits_check.py` and `names` | `cli.py:870-878` → `scope_from_record` `cli.py:924-947` reads only the exclude/include lists and applies them to the run's commit. **`source` is not read**; the engine extracts nothing from P | **gap** for the record's statement ("as the frozen plan checker classifies them"); the engine's computation needs nothing off `main` | **Yes**, for A1 decisions (scope of the `repo` profile, item 11, `--final`). The sec. 6.3 independent review must re-derive the record from the object store, and that requires P | Engine computation: **yes**. Verification of the record's content against its stated source: **no**. Missing: the same blob `1153e039…` (lines 786-788, 856, 859-863 of P's `edits_check.py`). See note R5 |
| R6 | `records/gr58-hit-classification-v1.json` (`gr58-v1`; `oi-hit-classification/1`) | `f37662df6787fd1aea08769df6c44c221de07c95` | `8177b0923a7eddf09c473ce541e4c23de53067429a31d52260aa35f0bafa8410` | `classifications[0].tree` → T1′ (line 12) | `pipeline.py:625-646` matches hits by `(file, line_sha256)`, requires the line to be unique and its profiles to be covered, and then gives PASS. **`tree` is not read** | **gap** (the semantic classification is a judgement about a line that exists only at T1′) | **Yes**, for A1 decisions (GR.md:58 PASS in RT-D and item 7; otherwise REVIEW/`final-unclassified`). The sec. 6.3 review must read "the sentence and its context at the stated tree" (T1′) | Engine matching: needs a tree that contains the line. The line (sha256 `3a7c1098…`) occurs at T1′ `papers/GR.md:58` (blob `c4a320e264d596629700548407496e9f31282dbb`) and **not** at H or at `9deb6956` (blob `e0b3b70f…`). Missing: that blob. See note R6 |

## 2. Per-record notes

**R1.** I recomputed each fingerprint with the engine's splitter (version 2, the staged configuration's
abbreviations; script `work/fp.py`). All 11 reproduce sentence and context at T1′. At H and at `9deb6956`, 9 of 11
reproduce sentence and context, at the same lines or shifted by 2 in `FULL.md`. W1-d's two fingerprints
(`ch19-open-problems.md:212`, `FULL.md:5282`) reproduce the sentence only, with a different context. The fingerprinted
text is thus largely present on `main`, but the engine reads by the commit id T1′, so T1′'s commit and tree objects
are needed. A copy of the text elsewhere does not satisfy the lint, and copying files to `main` does not make T1′
reachable (§A.42 item 8). Behaviour without T1′: `gitobj.paths` raises `Unresolvable` (`gitobj.py:85`). By code
reading (not executed), the run therefore cannot admit the rule, and the dependence fails closed rather than passing.
The top-level `recorded_at` (line 6) is not read and is provenance.

**R2, R3.** EXACT-DELTA's row "load-bearing (same mechanism)" is not borne out by the code. Neither file has an
allow rule, so no fingerprint is reproduced at `recorded_at`. The countercontrols DR-1a/b/c, DR-4 and DR-5 read H
(`53c6601a`), which is on `main`. DR-3 reads `controls.json`'s `agents-md-at-H` (H, blob `12a9281f…`, on `main`).
`resid`'s lint reads nothing from git. The T1′ id in each is provenance: no claim in the record uses T1′ content.
Both records are still inputs to A1 decisions (sec. 0 point 4), and under the owner's literal condition that alone
makes them "essential to an admission decision" (sec. 5).

**R4.** Two separate facts. (a) The record's own P fields are not read: `lint.checker` is metadata, and the engine
lints against whatever checker companion `F`'s configuration pins. (b) The A1 configuration pins that companion to P's
`edits_check.py`. In substance the record states that its literals equal P's checker, so its admission lint needs
P's bytes. The same bytes are needed independently by the profiles `ptr`, `repo`, `register`, `register-caps` and
`infinity`, and by the ledger adapter (P's `ledger.json` `ba37c1cd…`, `edits.json` `ec384fdf…`). These are pinned in
the configuration, not in this record (sec. 6).

**R5.** I compared the record's lists read-only with P's `edits_check.py`. `exclude_prefixes` equals
`HISTORICAL_PREFIX` (line 786-787), `exclude_files` equals `HISTORICAL_FILE` (line 788),
`include_patterns_within_excluded` equals the `ACTIVE_IN_RECORDS` pattern (line 856), and `exclude_patterns` restates
`classify`'s generated-artifact rule (line 862). They match. This check needs P, so it is support off `main`. The
engine never performs it, so a reviewer must.

**R6.** `papers/GR.md:58` at T1′ reads "…under H-count.** For a finite total system, restrict it to…". At H the
same paragraph reads "…under H-count.** Under A1, restrict the finite total system to…". The classified line is a
product of the retirement edits: it is the H line with P's ledger applied. It is reconstructible from H plus P's
`ledger.json`, which is also off `main`. `segment: "H..X"` is likewise not read by the engine.

## 3. Descriptive and control references already narrowed (each reference classified separately)

The README's narrowing paragraph (lines 99-105) applies one label to the group. §A.42 item 8 makes provenance a
finding about each reference, so each is listed here.

### 3.1 `README.md` (blob `e339072b12d66631b3afb83e5612f88020223603`, sha256 `e8cdbe64…7cf7`)

| Line | Reference | Claim it is attached to | Classification |
|---|---|---|---|
| 27 | "fingerprinted at T1'" (W1/W2 file row) | describes R1 | **prov** for the README sentence (descriptive). The fingerprints it describes are R1's gap |
| 28 | "classification of papers/GR.md:58 at T1'" | describes R6 | **prov** (descriptive). R6's gap is separate |
| 102 | P `4c79be64…` | "the A1 controls and the draft records … read the frozen plan P" | **prov** for the narrowing statement. Its blanket conclusion ("every … extraction those records take at P or T1′ is provenance only") is accurate for R2, R3, the record-field reads of R4 and R5, and the A1 control results. It does not capture R1's per-rule `recorded_at` or the admission-time dependence of R4, R5 and R6, which are gaps (sec. 1) |
| 103 | T1′ `14ac71b4…` | same | as line 102 |

### 3.2 `tools/ledger_coverage/adapters/a1_controls.py` (blob `65467b97f99ffa206e8043ded7a6f0e04a67e07e`, sha256 `cdbd1e26…8e80`)

| Line | Reference | Use | Classification |
|---|---|---|---|
| 42 | `T = 14ac71b4…` | the X of the real-tree controls (RT-T0, RT-C, RT-D, RT-I7, RT-I7A, RT-DR3W countercontrol, RT-L2's candidate) | **prov**: control-harness results, never admission (sec. 0 point 3) |
| 43 | `P = 4c79be64…` | `LEDGER`/`EDITS` (lines 45-46) = P's `ledger.json`, `edits.json`; the configuration route | **prov** (same) |
| 347-371, 374, 849 | reads R5, R6 at the tool revision for RT-D / RT-D-gr58 / item 11 | harness | **prov** |
| 677 | `rulemod.lint_rule` on the rule files | harness lint (it reproduces R1 at T1′) | **prov** for the control. The lint it repeats is R1's gap under a real run |

Other constants (`E`, `H`, `WM = 413b0bb8`) are on `main`. This module is not an adapter of the A1 configuration (the
staged configuration pins only `a1exit_exact_edit`, `a1exit_sitemap`, `python_frozen_replay` and the five `deleg_*`
modules), and the engine does not import it.

### 3.3 `tools/ledger_coverage/adapters/a1_conformance.py` (blob `ddd9680fafa133b6eb1060c3b28c9c793969fb11`, sha256 `dbf65c59…68ce`)

| Line | Reference | Use | Classification |
|---|---|---|---|
| 27 | `H, T, P, E = a1c.…` | T1′ and P by import | **prov** (harness controls WB1-WB15, S11-56/57/58, N3-N18) |
| 254-271 | S11-56: `terms --commit T1′ … --ledger P:ledger.json`; P's `edits.json`, `edits_check.py` | harness comparison with P's `static_new` | **prov** |
| 493-494, 504 | `x_blob = blob_id(T, AGENTS.md)` asserted to be `9f4fc3e830707c90ffc105842d26d5b51f01760b` | N10 expectation | **prov**. The blob exists in the repository (host GET 200, size 102227) but is not reachable from `main` |
| 505, 514, 541 | `86d79863821f3f8cdad86771008b2df89fd1961a` | N10, N11, N3-config-route expectations | **prov**. A computed id that is no object (sec. 4) |
| 29 | `M = 8e9b8334…` | N10/N11 fixture | on `main` (not an off-`main` reference) |

### 3.4 `controls.json` (blob `f01f5a99819d211342a2c4bc898087f2b1ddcf03`, sha256 `23b48072…226a`)

| Line | Reference | Use | Classification |
|---|---|---|---|
| 19-22 | control input `agents-md-at-T1p` (commit T1′, `AGENTS.md`, sha256 `59b68984…`) | read only by control RT-DR3W (the harness) | **prov**. No deny rule's countercontrol names it: DR-3 names `agents-md-at-H`, which is on `main` |
| 93, 126, 140, 224, 240, 701, 1226, 1242 (cases) and 164, 216, 232, 249 (references) | "at X = T1'" / "at T1'" | preregistered case descriptions and expected figures | **prov** (descriptive; harness controls) |

Under a real run the configuration pins `controls.json` (`config.py:188`, `:329-339`: CONFIG_NO_CONTROLS if an
operation lacks a positive and an adversarial control), and the deny-rule lint reads its `agents-md-at-H` input. Both
need only content on `main` once the file lands. Its header still names design v5.1. That is a preregistered record,
not edited, and it is outside Q10.

## 4. The value `86d79863821f3f8cdad86771008b2df89fd1961a`

- **What it is.** The Git blob id (SHA-1 of `"blob <len>\0"` + bytes) that a particular byte string *would* have. The
  bytes are `AGENTS.md` at M = `8e9b8334` (blob `6b1280fa92fa30e36555e9afd30cc0d6e992f5bb`, 105602 bytes), with
  splice D296 of P's `ledger.json` applied. The 50 old bytes (H offset 2332-2382, sha256 `8711166b…`) occur exactly
  once at M, at offset 2332, and are replaced by `"including\n  linearity (A5),"` (sha256 `532c5919…`). This is the
  reference landing composition of `AGENTS.md` that `reconcile.compose` (`engine/reconcile.py:87-109`) builds in
  memory for N10, N11 and N3-config-route.
- **Recomputed independently** (`work/compose.py`, reading H, M and P's `ledger.json` with `git show`, with no write):
  105579 bytes, sha256 `3c334a42cb3d984c9aec5f308c53fb457e747469e200972a1660da392c8fee1b`, blob id
  `86d79863821f3f8cdad86771008b2df89fd1961a`. `git hash-object --stdin` (without `-w`) gives the same id. The bytes
  differ from M's and from T1′'s `AGENTS.md`.
- **Not an existing Git object.** `git cat-file -e 86d79863821f3f8cdad86771008b2df89fd1961a` in
  `<repo>` exits 1, and `git cat-file -t 86d79863` fails ("Not a valid object name"). GitHub
  `GET repos/amaybaum/incompleteness/git/blobs/86d79863…` returns 404, and so does `git/commits/86d79863…`. As
  positive controls the same GET returns 200 for `6b1280fa…` (size 105602) and `9f4fc3e8…` (size 102227).
- **Reproducibility from `main` alone: no.** M and H are on `main`, but D296's bytes come from P's `ledger.json`
  (blob `ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e`), which is off `main`.
- **Status.** The id is a control expectation in code, not a governed record's citation. It must not be described as
  an object in the repository. If it were copied into a governed record, §A.42 item 3's first clause (ids name objects
  that exist) would be violated.

## 5. Escalations

Every item below needs the owner's separate decision. Per the owner's conditions, the narrow (c) exception cannot by
itself let any of them serve an admission decision. No option listed changes a recorded value or amends the frozen
plan, and the options are not ranked.

**Common finding.** None of the six is read by any admission decision of the tool landing (authority `A`, the freeze
ledger, TR5). All six are pinned by the A1 configuration draft and are inputs to A1 retirement decisions at `F`.
Under the owner's literal condition ("essential to an admission decision"), all six therefore need separate approval
before any of them is used for an A1 decision. In four of them the dependence carries a normative evidence gap:

- **ESC-1, R1 `w1-w2-allow-v1` (normative gap).** The engine reads T1′ by commit id when it admits the rule
  (`rules.py:118`, `:155`; `pipeline.py:720`). T1′ is off `main`, and the four T1′ blobs of sec. 1 are absent from
  `main`'s objects. Options that leave recorded values unchanged:
  - (a) Keep the record as an unadmitted draft. Record the gap under §A.42 item 8 with the owner's quoted decision,
    naming the claim it leaves unsupported (W1/W2 PASS). The record is not used for any A1 decision until the gap is
    closed.
  - (b) Close the gap with new content: a superseding record (a new file; v1 untouched; same `record_id`;
    `supersedes` v1) fingerprinted at a commit reachable from `main`, with its own review and the widening review
    that W1-d's context change requires. 9 of 11 fingerprints already reproduce at H and `9deb6956`.
  - (c) Make the content reachable from `main` through the A1 programme's own landing, if one is authorized for its
    own sake. Keeping the trial branch does not close the gap (§A.42 item 8).
- **ESC-2, R4 `register-infinity-params-v1` (normative gap).** Its admission lint needs P's `edits_check.py`
  (`1153e039…`), supplied by `F`'s configuration rather than by the record. Items 5/6 fail closed without the record.
  Options: (a) as ESC-1(a); (b) the dependence ends when the frozen plan's content reaches `main` through its own
  authorized course (not landed to satisfy a citation). Note that this dependence on P is shared by the configuration
  itself (sec. 6), so it is not specific to this record.
- **ESC-3, R5 `repo-scope-v1` (normative gap in its support; engine computation self-contained).** The engine never
  checks the content against P, so a pass at run time would rest on an unverified premise unless the sec. 6.3
  reviewer verifies it against P's checker, which is off `main`. Options: (a) as ESC-1(a); (b) a superseding record
  whose statement rests on stated content alone, without "as the frozen plan checker classifies them". That is new
  content needing review and, as a scope change, a widening review (design sec. 16.2).
- **ESC-4, R6 `gr58-hit-classification-v1` (normative gap).** The classified line exists only at T1′ (blob
  `c4a320e2…`). Its review needs that tree, and the classification decides GR.md:58 in RT-D and item 7. Options:
  (a) as ESC-1(a); (b) defer the classification until a tree containing the line is reachable from `main` (the
  executed retirement), without landing T1′ for the citation's sake.
- **ESC-5, R2 `dr-deny-v1` and R3 `resid-v1` (no evidence gap).** Their T1′ citation is provenance, and their
  admission reads only `main` content. They are listed only because the owner's condition covers any affected record
  essential to an admission decision: the approval sought concerns the provenance label, not missing evidence.
- **ESC-6, correction of the S1 classification.** EXACT-DELTA's Q10 table labels R2 and R3 "load-bearing (same
  mechanism)", R4 "linted against P's `edits_check.py`" (through the record's field) and R5 "scope names extracted from
  P's `edits_check.py`". The code shows: R2/R3 not read; R4 linted against the configuration's companion; R5's
  `source` never read or extracted. The README's group label "provenance only" (S1 review nit N3) remains a group
  label. Any landed per-reference text should follow sec. 1 and 3 rather than EXACT-DELTA. Correcting the README
  would be a change to a landed file and is not made here.

## 6. Related dependence outside the six (for awareness, not part of Q10's set)

The staged A1 configuration (not landed; it belongs in the plan's record directory at `F`) cites P for
`adapters.ledger` (`ledger.json`, `edits.json`, the `checker` companion) and for the sources of the profiles `ptr`,
`repo`, `register`, `register-caps` and `infinity`. Every A1 decision at `F` therefore depends on P's content,
independently of the six records. This is the plan's own frozen basis, not a citation in the tool landing.

## 7. Limits

- Reachability rests on GitHub compare GETs against `9deb6956` made on 2026-11-24. The local clone is shallow.
  "Blob not on `main`" was checked against the objects reachable from `9deb6956` in the local history (back to about
  2026-10-31, 12231 objects) and against H's and `main`'s trees. A byte-identical blob older than the shallow boundary
  is not excluded, but none of the listed blobs is older than 2026-11-21.
- Code paths were traced by reading, with no tool run. The one exception is that `work/fp.py` imported
  `engine.util`/`engine.rules` from the worktree. That import rewrote the git-ignored bytecode cache
  `tools/ledger_coverage/engine/__pycache__/rules.cpython-313.pyc` in the worktree. No tracked file changed, and
  `git status` is clean.
- "Essential to an admission decision" for A1 decisions assumes `F`'s configuration pins the six as the staged draft
  does. That configuration does not exist yet.
- The owner decisions are quoted as relayed in the task; their comment ids were not available to me.
