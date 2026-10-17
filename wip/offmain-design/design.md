# Retaining the off-main evidence on `main`: proposed PR design (R2-B, tranche 2 of the archive)

Status: design and local prototype only. Nothing was pushed, dispatched, commented or branched on the host, and no
file under `/home/user/incompleteness` was changed. `main` is `66a981d5`. Every number below is in `manifest.json`
beside this file, and the scripts that produced it are in `src/`; raw outputs are in `work/`.

## 1. What is preserved

The owner's scope is the union of five inputs. Each is wholly in the manifest (`input_reconciliation`):

| input | members | in the manifest |
| --- | --- | --- |
| R2-B survey, universe U5 | 292 (202 commits, 83 blobs, 7 trees) | 292 |
| run-inventory heads, host-unreferenced | 116 | 116 |
| run-inventory heads, branch-only | 93 | 93 |
| run-inventory heads, pull-ref-only | 5 | 5 |
| package b1 / b2 (the 107 SHA-only commits) | 84 + 23 | 107 |
| package b3 | 13 commits, 6 blobs | 19 |
| R3 pair `78aa5b25`, `e7d380fc` | 2 | 2 |
| BG-3 temporary heads `3218e8d0`, `6c160ad2`, `e3ef9358` and blob `1b5c4489` | 4 | 4 |

Deduplicated, that is **342 cited objects: 252 commits, 7 trees, 83 blobs**. Add the trees and blobs those objects
need that `main` lacks, and the manifest holds **1,725 objects: 252 commits, 1,008 trees, 465 blobs**.

**Holders**, from the host's ref list at 2026-10-17T03:34:45Z and a by-SHA fetch at 03:41:07Z:

| | branch | pull-ref only | host-unreferenced | local-only | on main |
| --- | --- | --- | --- | --- | --- |
| cited commits | 108 | 14 | 130 | 0 | 0 |
| cited trees | 4 | 1 | 2 | 0 | 0 |
| cited blobs | 71 | 0 | 12 | 0 | 0 |
| all 1,725 | 903 | 71 | 751 | 0 | 0 |

- All 144 cited objects that no host ref reaches were requested by SHA in one read-only fetch, and the host served
  all 144. Their closure came back as 1,080 objects, each hash-verified by git.
- Every object is also present locally (shared clone, survey scratch repositories or the packages). None is
  local-only.
- The host's ref list barely moved since the run inventory's listing (2026-10-16T20:36Z): no ref was deleted, and
  no branch holding a cited object moved. `draft/evidence-retention-r1-20261016` was already absent from that
  listing; the survey saw it only as a stale remote-tracking ref. It held no cited object.

## 2. Mechanisms

| mechanism | objects | what it gives a reviewer |
| --- | --- | --- |
| commit `raw:connected` | 201 | the exact commit, fully connected in any clone of `main`. 81 have every parent on `main`; 120 reach `main` through retained connected parents |
| commit `raw:tree` | 39 | commit id and complete tree verified; a parent is off `main` and not connected. 15 name a parent that is not retained; 24 have a retained but unconnected parent |
| commit `raw:partial-tree` | 5 | commit and every tree verified; the withheld blobs (raw logs, build PDFs) are named by id |
| commit `inclusion-proof` | 3 | `78aa5b25`, `e7d380fc` (R3) and `5f4089a4` (the B4 notes link): commit, root tree, the trees on each cited path, and what lies under it. Path trees name their other entries; their contents are not retained |
| commit `identity-anchor` | 4 | `4dc0321c` (its citation "I3 and I4" names no path), and `a163b924`, `9430c463`, `8508d172` (chronology: identity, parents and dates are the claim) |
| tree `raw` | 996 | trees of retained commits and the 7 cited trees |
| tree `raw:proof-path` | 12 | trees on an inclusion path |
| blob `byte-copy` | 400 | the blob, unmodified |
| blob `withheld:raw-log` | 58 | not committed (§A.42 item 1); named by id and size. 2.38 MB |
| blob `withheld:build-pdf` | 7 | build outputs whose bytes no record freezes; named. 6.01 MB. Four are CONSC-2's cited PDFs |

Why these and not others:
- **Raw objects, not bundles or merges.** This is as the survey recommended. A bundle verifiable from `main` needs all
  off-main ancestry, and merges import history. Neither is needed here: no object enters `main`'s history.
- **The 107 SHA-only commits are all retained, all in tranche 1**: 77 `raw:connected`, 29 `raw:tree` and 1
  `raw:partial-tree`. These are b1's 84 and b2's 23. The 9 range-only ancestors b2 also holds are `raw:connected`.
- **BG-3's temporary heads** `3218e8d0`, `6c160ad2` and `e3ef9358` are `raw:connected`. Each has its parent on
  `main`.
- **Research-archive commits** carry a 236 MB tree with more than 330 logs. They get proofs or anchors, never the
  full tree.
- **The excerpt guard is by construction and by check.**
  - None of R1's 194 excerpt blobs is in the stored set, and no stored tree names one (§6).
  - The deny-list in the objects manifest holds sha256 digests of the excerpt ids, not the ids. So it cites no
    off-main object itself, and the audit's 7–40-hex rule cannot read it as one.

**Ids recorded wrongly in frozen records (new finding).** Four full-length ids that the survey listed as
unrecoverable have no object behind them. In each case the cited run's head, as the host's runs API reports it,
shares the first eight hex digits and has the subject the citing line describes. The host also resolves the
eight-digit prefix to that head.

| citing location | cited id | retained id (run head) | run |
| --- | --- | --- | --- |
| act-35 `result.md:218` | `2ae4dbeef5d9…` | `2ae4dbeeceae…` | 36310787113 |
| act-33 `preregistration.md:710` | `4c4155da7ccc…` | `4c4155da0593…` | 36257341185 |
| act-33 `preregistration.md:711` | `cff3c1560f4c…` | `cff3c1566228…` | 36257659584 |
| act-45 `preregistration.md:400` | `ad64b60319e1…` | `ad64b603b7a1…` (its tree `12a695df…` matches in full) | 36612901341 |

These records cite full ids whose last 32 digits name nothing. A shared 32-bit prefix arising by chance four times
is implausible, so the full ids were most likely written out wrongly from eight-digit abbreviations.
- The evidence is retained under its true id.
- The objects manifest records each mapping in `id_discrepancies`, with its basis.
- The frozen records are not edited (§A.42 item 4).
- This is an identification by prefix, run id and subject, and is stated as one. It does not establish that the
  record's wording was correct.

## 3. Placement

`verification/audits/evidence-retention/objects/` holds the data, and
`verification/audits/evidence-retention/check_objects.py` its checker. The objects form tranche 2 of the existing
archive.
- §A.42 item 3 puts frozen records' evidence in `verification/audits/evidence-retention/`, under a manifest that maps
  each citing `file:line` to its retained copy. Every cited object here is cited by a frozen record, and in one case
  by a byte-pinned mutable file.
- §A.36 puts audit artifacts inside their audit's directory and never at the `verification/` root;
  `artifact_placement_check.py` passes on the prototype.
- The directory is not a closed legacy namespace, and it is not a round record, so `G13` does not apply.
- A sibling directory would avoid touching R1's checker. It would also split one archive in two, against item 3's
  wording. Q1 asks the owner to choose.

## 4. File layout and naming

```
verification/audits/evidence-retention/
  check_objects.py                 the checker (new)
  objects/
    manifest.json                  schema oi-evidence-objects v1: every object, its citations, mechanism, form, digests
    commit/<aa>/<oid>              raw commit object content (text), 252 files, 212 KB
    blob/<aa>/<oid>                raw bytes of each cited blob, 79 files, 4.9 MB
    loose/<aa>/<38 hex>            git loose objects: zlib("<type> <size>\0" + content), 1,329 files: every tree and
                                   every dependency blob, 13.0 MB (89 MB of content)
```

- **Names.** Files are named by object id, with no extension, so no `.gitignore` rule, build, test runner or
  extension-keyed scanner matches them. Two-digit fan-out keeps every directory under GitHub's 1,000-entry listing
  limit.
- **Cited blobs are plain bytes.** Committing them makes those blob ids reachable from `main`. A frozen control that
  reads them with `git cat-file` then works in any clone, with no extra step. Shown in §7 for OG-1.
- **Commits are plain text.** They stay diffable and greppable. Their ids are verified by hashing.
- **Trees and dependency blobs are loose objects.**
  - This keeps the checkout at 19.4 MB instead of 95 MB.
  - Disposable sources are not present on `main` as readable files (§5).
  - The files drop straight into `.git/objects`.
- **The manifest.** Each entry has its id, type, mechanism, form, file, size and sha256 of the stored file and of the
  content, and its tranche. It also has its citations (`location`, `class`, `role`, `via` token / run / run-range,
  `tokens`), `needed_by`, parents, `parents_not_retained`, `withheld_blobs` and `inclusion_paths`. It contains no
  local path and no e-mail address: identities are sha256 digests.

## 5. Not adopted as certified code

The retained objects are evidence of what disposable heads contained. They are not code that `main` runs.
- **They are inert on `main`.**
  - Nothing is under a path that a build, the release gate or CI picks up. There are no `.lean`, `.py` or `.yml`
    names, and nothing under `OIBridge/`, `tools/` or `.github/`.
  - 1,329 of the 1,660 files are compressed, so not even a content grep reads them as source.
  - The 79 cited blobs in plain form are exactly the bytes the frozen records name by id.
- **The checker never executes retained content.**
  - It hashes, parses tree and commit headers, and scans text.
  - Reconstitution writes objects into a temporary repository whose object store is the checkout's, read-only.
  - `--materialize` writes into the checkout's own object store and creates no ref.
- **Running a retained tree is reproduction of a historical claim, not certification.** It happens in a worktree of
  the reconstituted commit, as R1's `reproduce.py` already does for on-`main` commits. As there, the verifier is
  `main`'s checkout; the retained commit supplies only its sources.
- **Retention changes no verdict.** No retained object is a `check-run` attestation (§A.39, §A.42 item 6).
  `tools/v3_verifier.py` is unaffected, and no claim's status changes because its object is retained.
- **Retention never strengthens a claim (§A.42 item 4).**
  - A `raw:tree` commit is recorded as having unretained parents.
  - A `raw:partial-tree` commit is recorded with its withheld blobs.
  - An inclusion proof retains the cited paths only.
  - The four id discrepancies are recorded as discrepancies.

## 6. Recovery check (`check_objects.py`, prototype)

Tree mode needs no git: rules O1–O7. History mode (`--reconstitute`) adds H1–H6. Both are listed in the script's
docstring. In summary:
- **O1:** every stored file has its sha256, and its content hashes to its id with git's header.
- **O2:** no unlisted file.
- **O3:** the manifest is well formed.
- **O4:** closure. The checks are:
  - every id a retained object names is retained, withheld or expected on `main`;
  - inclusion paths walk;
  - parent and withheld lists are exact;
  - `raw:connected` is not claimed for an unconnected commit.
- **O5:** the excerpt deny-list. It covers ids in the manifest, ids named by trees and commits, and every file's own
  blob id.
- **O6:** the secrets scan, with exemptions (§8).
- **O7:** every citation's line still holds its token, and every id discrepancy is consistent.
- **H1:** the base is an ancestor of HEAD.
- **H2:** git itself writes every object with its id. `hash-object` also checks commit and tree format.
- **H3:** everything named and not retained is on `main`.
- **H4:** `git fsck --connectivity-only`.
  - Refs are set at every `raw:connected` and `raw:tree` commit and every complete cited tree.
  - The `raw:tree` commits are the shallow boundaries.
  - Each `raw:connected` commit's history must reach `main` only through retained connected commits.
  - Partial-tree commits must miss exactly their withheld blobs.
  - Inclusion paths must resolve.
- **H5:** every identity digest is an address already in `main`'s history.
- **H6:** no deny-listed id is reachable from HEAD, or from any reconstituted object.
- **`--materialize`:** runs history mode, then adds the objects to the checkout's object store.

Results on the prototype, which is `main` plus the layout, committed locally as `6439257c` and never pushed:

| run | result |
| --- | --- |
| tree mode | OK: 1,725 entries, 1,660 stored and verified, 65 withheld, 933 ids expected on `main` (16–23 s) |
| history mode | OK: those 933 verified on `main`; 246 refs, 39 shallow boundaries, fsck clean (23–33 s). It names the 22 parents not retained and the 5 partial trees with their withheld counts |
| self-test | OK, 21 cases (9 min 40 s): each mutation fails with the rule named below, and the unmutated copy passes in both modes |

**Mutation table**: a copy of `objects/` is mutated, then checked; the rule shown is the one that must fire.

| mutation | rule | result |
| --- | --- | --- |
| none, tree mode / history mode | — | passes / passes |
| a corrupted byte in a raw blob / a raw commit / a zlib tree / a zlib blob | O1 | fails ×4 |
| a missing object file, entry kept | O1 | fails |
| a missing object, file and entry removed | H3 | fails |
| an unlisted file | O2 | fails |
| an excerpt: a stored blob whose id is deny-listed | O5 | fails |
| an excerpt: a retained tree that names a deny-listed id | O5 | fails |
| an excerpt: a new stored blob on the deny-list | O5 | fails |
| an excerpt: a deny-listed blob reachable from HEAD | H6 | fails |
| a secret pattern / an e-mail address in a stored blob | O6 | fails ×2 |
| a commit identity whose digest is not listed | O6 | fails |
| a listed identity absent from `main`'s history | H5 | fails |
| a `raw:tree` commit relabelled `raw:connected` | O4 | fails |
| a withheld blob dropped from its commit's list | O4 | fails |
| a citation whose line lacks its token | O7 | fails |
| an id discrepancy mapped to another commit | O7 | fails |

The self-test's excerpt cases use synthetic deny-list entries, because a real excerpt must never reach `main`. The
real excerpts are exercised by the controls below, in scratch only.

**An independent control, without the checker's code** (`src/independent_control.py`):
- **Setup:** copy the loose files unread into a fresh repository seeded only with `main`; write the raw files with
  `git hash-object`; run `git fsck --full`.

| case | result |
| --- | --- |
| A: refs at the 201 `raw:connected` commits, no shallow file | rc 0, 1,660/1,660 objects present, 0 missing |
| B: refs at the 39 `raw:tree` commits, no shallow file (countercontrol) | rc 2, 15 missing parents reported |
| C: A and B together, `raw:tree` commits shallow | rc 0 |
| D: the 5 partial-tree commits (countercontrol) | rc 2, exactly the 61 withheld blobs reported missing |
| E: BG-3's three temporary heads | present, full trees, parent on `main` |

**Reproduction from `main` plus the objects:**

| probe | result |
| --- | --- |
| OG-1's frozen `controls.py --self-test`, which reads blobs `e9722042` and `bf627dfe` with `git cat-file` | rc 1 on `main` alone; `controls: OK -- 30 checks`, rc 0, with the layout committed. No materialize step is needed |
| BG-3's recorded local check `controls.py check e3ef9358 --freeze f0a9ee7c` | fails on `main` alone (no such commit). After `check_objects.py --materialize`, the frozen checker from that tree prints C1, C2, L0, L, P, R, S and G PASS and `controls: OK (0 failure(s))`, as the preregistration records |

**Excerpt check, with the real R1 excerpts** (`src/excerpt_controls.py`, `src/inject_real_excerpt.py`). Hits are
deny-list matches among the objects each ref reaches:

| case | result |
| --- | --- |
| host branch `archive/r1-evidence-retention-drafting-20261016` (positive) | 194 |
| `tmp/r1-reproduce-proof-20261016` and `-2`, `-3` (positive) | 194 each |
| `tmp/r1-reproduce-proof-20261016-4`, `-5`, `draft/evidence-retention-r1-hardening-20261017` (negative) | 0 |
| `main` (negative) | 0 |
| the simulated PR commit, `main` plus the layout | 0 |
| a real excerpt added as a raw byte copy | fails O5 |
| a real excerpt added as a loose object | fails O5 |
| a real excerpt's bytes added as an unlisted file | fails O5 (and O2) |
| a retained tree naming a real excerpt | fails O5 |
| a real excerpt committed anywhere in HEAD's tree | fails H6 |

## 7. The audit rule: a `retained` class

`offmain_audit.py` reports C and O for every cited id that resolves to an object not reachable from `main`.
1. **A `retained` class.**
   - A C or O token whose id is in `objects/manifest.json`, and which `check_objects.py` verifies, is reported as
     `retained`. It is not off-main.
   - The report names the mechanism: exact (`raw:connected`), tree (`raw:tree`), partial, inclusion-proof, anchor or
     withheld.
   - Resolution must use the manifest, not only `cat-file`. A main-only clone does not hold the retained commits
     unless they are materialized, and the audit silently drops tokens that resolve to nothing.
2. **The object store is data, not citing records.** Files under `objects/` are excluded from the token scan.
   Without that exclusion, the raw commit texts' `tree` and `parent` lines would become new C citations.
3. **Forward only.**
   - Add the rule behind a flag such as `--retained objects/manifest.json`. Without the flag, the script must still
     reproduce `audit/offmain_audit-output.txt` at `fc5abade` byte for byte. That is a control, and the survey
     confirmed it holds today.
   - Record the new output at the tranche's base beside the old one. Do not rewrite the old output.
   - The script's manifest entry is re-pinned.
4. **Effect, from the prototype's manifest:**
   - U1: 107 of 107 commits and 71 of 75 blobs/trees become `retained`; the 4 others are CONSC-2's PDFs, `withheld`.
   - U5: 202 of 202, and 86 of 90 plus the same 4.
   - Tokens that resolve to nothing are not reported by the audit, and still are not. Its unresolved-token count
     drops only by the four id discrepancies.

## 8. Secrets scan of every byte copy

Every stored object was scanned before the layout was built (`src/secret_scan.py`):
- the patterns of R1's `check_retention.py` R5 (token shapes, key headers, signed-URL parameters, passwords, API
  keys, IPv4 addresses, e-mail addresses);
- plus four more token shapes (`xox?-`, `sk-`, `AIza`, SSH/PGP private-key headers).

| match | count | treatment |
| --- | --- | --- |
| author and committer header lines | 504 lines, 4 distinct addresses, all present in `main`'s history | exempt when the address digest is listed (H5 verifies the list against `main`) |
| `gpgsig` signature blocks (235 SSH, 1 PGP) | 236 commits | exempt: a signature, not a key; part of the commit id |
| `Co-Authored-By:` trailers | 218 lines, address in `main`'s history | exempt as identities |
| `user.email=…@example.invalid` git-config fixtures in old versions of `edge_rigidity_probe.py` | 26 lines in 9 blobs | exempt: RFC 2606/6761 reserved domains |
| anything else | 0 | — |

- Nothing was redacted. A redacted copy would not keep its id; §A.42 item 5 would give it its own digest, and it
  could not be a byte copy.
- Logs and PDFs are withheld, not scanned for commit, since they are not committed.
- O6 re-runs the scan, with the same exemptions, on every check.
- R1's R5, unchanged, flags all 252 raw commits, on their header address (measured on the prototype). That is
  integration point 9.2.

## 9. Integration points (not drafted: PR #854 is changing `check_retention.py`, `reproduce.py` and `README.md`)

1. **`check_retention.py`, R6.**
   - `check_objects.py` joins `FIXED`.
   - Files under `objects/` are accounted for by `objects/manifest.json`, and O2 enforces that.
   - On the prototype, R1's check today reports 1,662 R6 failures: the 1,660 objects, the manifest and the checker.
2. **`check_retention.py`, R5.** The `objects/` subtree is delegated to O6, which decodes loose objects and applies
   the narrow identity, signature and reserved-domain exemptions. On the final prototype R1's check reports 252 R5
   failures, one per raw commit header, and nothing else: 1,914 failures in all, every one R5 or R6. The checker's
   own source was rewritten so that R5 does not match it.
3. **`check_retention.py` manifest (R1, R7).** The tranche-1 manifest gains a tranche-2 record. It pins
   `objects/manifest.json` and `check_objects.py` as `complete` files by sha256, so the objects are pinned
   transitively through their own manifest.
4. **`--gate` and the release gate.**
   - The `evidence-retention` step also runs `check_objects.py --reconstitute` and `--self-test`, in the same step;
     no new gate step is needed.
   - The Mathlib bridge job already checks out full history.
   - §A.42 item 7 and `release_gate.py`'s docstring need a sentence each. That is an owner edit.
5. **`reproduce-evidence.yml` and `reproduce.py`.**
   - Before `reproduce.py`, the workflow runs `check_objects.py --materialize`. `reproduce.py` checks that the commit
     is in the repository, so with that step the two BG-3 design-tree entries (`6c160ad2`, `e3ef9358`) and any
     retained connected commit can be rebuilt.
   - `reproduce.py` itself needs no change, but its README sentence that design-tree results are "reproducible only
     while those commits are kept" changes.
6. **`README.md`.**
   - A "Tranche 2" section.
   - "Not yet retained" changes: 107 commits and 75 objects become the withheld and unrecoverable lists.
   - A statement of the not-adopted-as-code rule (§5).
7. **`offmain_audit.py`:** §7.
8. **Unaffected:** `legacy_records_check` (not a closed namespace); `artifact_placement_check` (prototype: OK); the
   V3 verifier; the census.

## 10. Size budget

All figures are for 1,660 stored objects.

| form | on disk (with the 1.29 MB manifest) | added to a pack, default / `--window=250` |
| --- | --- | --- |
| all raw | 95.3 MB | 12.9 / 5.7 MB |
| all loose (zlib) | 15.6 MB | 14.5 / 13.7 MB |
| **hybrid (proposed)**: raw cited blobs and commits, loose for the rest | **19.4 MB** | **14.5 / 13.1 MB** |
| alternative: one git pack of exactly these objects | 2.75 MB | 2.75 MB |

- **For comparison:** `main`'s checkout is 54.8 MB in 1,641 files; R1's archive is 4.1 MB; `main`'s history packs to
  527 MB.
- **Where the content is.** Most of the 94 MB is versions of four files across design iterations:
  - `OrbitIsometryGroup.lean`: 25 versions, 28.9 MB;
  - `edge_rigidity_probe.py`: 10 versions, 17.6 MB;
  - `DitaTorusLocus.lean`: 15 versions, 15.2 MB;
  - `lean-manuscript-census.json`: 41 versions, 14.6 MB.
- **Why the pack alternative is smallest.** Git's own deltas compress these versions to 2.75 MB. A pack is opaque in
  review, and verifying it from the tree alone needs a pack parser. Q5 asks the owner.
- **Not retained, and why:**
  - withheld logs: 2.38 MB;
  - withheld PDFs: 6.01 MB.
  - The **chain option** (Q4): the 38 uncited off-`main` ancestors of the `raw:tree` commits, with their 186 trees
    and blobs (4.1 MB of content; no logs or PDFs), would close every path to `main`.

## 11. Tranche order (most at risk first)

The tranche is the most at-risk holder among the cited objects that need an object. Stored figures are hybrid-form.

| tranche | holder | entries | stored | stored bytes | content |
| --- | --- | --- | --- | --- | --- |
| 1 | host-unreferenced (lost if GitHub collects unreferenced objects) | 861 | 840 | 9.9 MB | 73.2 MB |
| 2 | pull-ref only | 74 | 74 | 1.7 MB | 6.4 MB |
| 3 | branch only | 790 | 746 | 6.6 MB | 14.4 MB |

- Each tranche is its own PR, and appends to `objects/manifest.json`.
- An earlier tranche's files are never rewritten. An object needed by two tranches is stored once, in the earlier.
- Tranche 1 holds:
  - 98 connected, 30 `raw:tree` and 2 partial-tree commits;
  - the 107 SHA-only commits;
  - SI-3's stage chain and act 19's closure chain, whose last commit `1dd963ba` is `raw:tree` (parent `9f30f01a`
    not retained);
  - the cited CV-2 and act-42 blobs;
  - 6 cited predicted trees.
- Tranche 3 holds:
  - the R3 pair;
  - BG-3's temporary heads;
  - the research-archive commits;
  - 24 of the 35 cited predicted-tree commits. Tranche 2 holds 5.
- The R3 pair and BG-3 are in tranche 3 only because their holders are branches. They could move to tranche 1,
  since the R3 rule file is a byte-pinned citation and R1's two BG-3 results need their commits. They are small:
  - the R3 pair's proofs: 26 objects beyond the two commits, 4 of them withheld logs or outputs;
  - BG-3's three heads: 25 trees and blobs beyond the commits.

## 12. What remains unrecoverable

The host refuses these ids (re-probed by full SHA 2026-10-17, and by eight-digit prefix through the commits API), and
no local store holds them:

| id | citing location | what it was |
| --- | --- | --- |
| `d5178e2fe0f1…` | `round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md:52` | GR-1 stage 1 (legacy record) |
| `70e34e828410…` | same file, `:53` | GR-1 stage 2 |
| `2a67dfcab4ba…` | same file, `:54`; `amendment-2.md:63`; `result.md:16` | GR-1 attempt-1 candidate `E` |
| `73f505974674…` | `amendment-2.md:68`; `result.md:24` | GR-1 attempt-2 candidate landing |
| `52009e086a30…` (blob) | `act-35-dita-hull/preregistration.md:1193`; `amendments/amendment-1.md:128` | act 35's first frozen `controls.py`, superseded by amendment 1 |
| `46fb79d1e2cf…` | `round-cv-2-v1-retirement/amendments/amendment-1.md:82` | CV-2, "committed in scratch" |
| `7de2d549` (abbreviated) | `round-trb-1-transitive-body/preregistration.md:110` | "`claude/trb1-dev` at `7de2d549`". It is not on that branch; the reference blob `31f63583` it names is on `main` |

- **Unresolvable but not missing:**
  - The four id discrepancies of §2. Their evidence is retained under the true ids.
  - `0850281a` in `round-k1-sharp-tests-1/preregistration.md:214`. The run it names, 37494787556, has head
    `08502810 82f0…`, which is retained as a branch-only run head.
- **Refused, but external to this repository** (14 of the 24 full-length tokens the host refuses):
  - 12 action and toolchain SHAs in R1's retained BG-3 design log;
  - Mathlib's `db584cd6`;
  - the prefix constant `e07d4056` in `edge_rigidity_probe.py`.
- **Other abbreviated tokens.** 4,670 hex tokens of 7–39 characters containing a letter resolve to no local object,
  mostly digests. Of these, 79 sit on a line with a commit-like context word. On inspection they are, apart from
  the two above:
  - sha256 prefixes (the L3B round, the census);
  - patch digests;
  - a journal identifier.
  None was probed beyond those listed.

## 13. Open questions for the owner

1. **Placement.** Inside the R1 archive (`evidence-retention/objects/`, recommended, which needs integration points
   9.1–9.4 after #854 lands), or a sibling audit directory that leaves R1's checker untouched?
2. **Raw run outputs.** Some withheld blobs are deterministic program outputs, and no frozen record pins them by
   digest:
   - four inside `e7d380fc`'s inclusion proof: `CI-REPAIR.log`, `CI-FAILED-B23.log`, `channel_check.replay.out`
     (the same blob as `run1.out`) and `native-controls.selftest.final.out`. Empty `.err` files are kept: the empty
     blob carries nothing;
   - the 321-byte `check.run1.out` of the finite-protocol design head `70815342`.
   - Under §A.42 item 1 they are withheld.
   - Retaining `check.run1.out` alone would make `70815342` fully connected.
   - Should deterministic outputs of at most a few KB be treated differently from CI logs?
3. **CONSC-2's four build PDFs** (3.26 MB) and act 45's three PDFs (2.75 MB): withheld as provenance (proposed), or
   retained so that the trees verify in full?
4. **The parent chain.**
   - The 38 uncited off-`main` ancestors of the `raw:tree` commits, with their trees, cost 4.1 MB of content.
   - Commit objects alone cost 39 KB, which gives verifiable chains but no connectivity.
   - Retain them, or keep naming the parents (proposed)?
5. **Storage form.**
   - The hybrid (proposed): 19.4 MB checkout, ~13–14.5 MB packed, per-object files, pure-Python verification.
   - A per-tranche pack: 2.75 MB, opaque, and needs a pack parser or git for tree-mode verification.
6. **Tranche placement of the R3 pair and BG-3:** branch-held, hence tranche 3, or brought into tranche 1 because
   frozen controls and R1's expected results depend on them?
7. **The four id discrepancies.** Is recording the prefix-plus-run identification in the archive manifest enough, or
   should a native round state the correct ids, since frozen records cannot be edited?
8. **The identity exemption.** The objects manifest lists four address digests. It never lists the addresses, which
   are public in `main`'s history. Is that acceptable under §A.42 item 5, or should the raw commit texts move into
   the compressed form, which the scan still decodes?

## 14. What this design does not establish

- That GitHub will keep serving the 751 host-unreferenced objects until tranche 1 lands. They were served at
  2026-10-17T03:41:07Z, and the bundles b1–b3 and this layout are local copies.
- That every claim made about a retained object is carried by it. The manifest maps citations to objects. It does
  not annotate claims the way R1's `claims` do; that is follow-on work per record.
- That the hybrid layout passes the real release gate. Only the steps that run without a Lean build were run locally:
  - `artifact-placement`: OK;
  - R1's `check_retention.py`: fails, for the integration reasons above.
- That the 79 commit-context abbreviated tokens are all non-commits. They were classified by reading, not by
  exhaustive probing.
