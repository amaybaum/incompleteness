# Tranche-2 pilot: head `0004afc9`, closure, classification and omission controls

Status: **WIP / UNVERIFIED — awaiting independent review.** This is one head's measurement. It does not change
the archive, it does not show that any object can be removed, and it supports no extrapolation to other heads.

## Fixed inputs

| item | value |
| --- | --- |
| archive | `verification/audits/evidence-retention/` at `main` `92de3143046b26d7fa2ce3b13ce3ea4b1e18a37a`. No diff from baseline `D` `6fe84106e842465f086c9bf301c82781421c0bfd` in that directory |
| object manifest | `objects/manifest.json`, blob `2ee4fbb95118115b4fb874b3c59c65e1b155aec9` |
| evidence manifest | `manifest.json`, blob `191d16654d8b98d33e0ffe57c2986677d76e0b11` |
| tranche-2 base | `49ba3297111acaf4d70cf3b932f44b3cc2129a2c` (the manifest's `base`, `TRANCHE_BASE_PINS[2]`) |
| preregistration | `PREREG.md` beside this file, sha256 `37a472102dbc839322d1d1948139a5bb9ad1b7358b85678380f23317f9825cca`, written before the closure, citations and regeneration were measured |

The selection rule was fixed after the manifest's first array element had been displayed while inspecting the
manifest's schema. The rule is mechanical, and anyone applying it to the pinned manifest gets the same head.

## 1. Selection

**Rule S:** take the first element of `objects/manifest.json`'s `objects` array that has `tranche == 2`,
`type == "commit"`, a non-empty `cited`, and at least one `cited` location of class `native-record` or
`legacy-record`, given as `path:line`.

Result: array index 0, **`0004afc9360117ba61523b72854de1aaf63705f0`**, `raw:connected`, parent
`17de29c27ed43d7f105aa8518451d8ed61c59937`, which is itself a retained `raw:connected` commit whose parent
`48450428f528fe489d454458e21c9394aef6a02f` is on `main` (act-30's `D`). Commit message: "A30 pre-freeze
rehearsal: retired R7-PFR/R7-PRA ROADMAP legs with the ADMITS P0 cell (disposable)", 2026-09-26.

Reproduce: `python3 -I -B closure.py <archive-dir> closure.json`.

## 2. Surviving `file:line` claims

The citing file is `verification/programmes/oi-qm/track-b/act-30-product-strict-lift/preregistration.md`, blob
`c637999c884328cb085cb9dbbf27a39bb44e6643` at `92de3143`, a frozen native-round preregistration. `git grep` on
`main` for `0004afc9` and `36222326658` finds no line outside the archive other than line 502. Each line below
was read at `92de3143`, and `check_objects.py` O7 passes on it in the live control (§6).

| location | cites | what the line asserts | evidence the archive holds for it |
| --- | --- | --- | --- |
| `:502` (the pilot head's only citation; two manifest records, token and run) | `0004afc9…` as head of run `36222326658` | (a) identity: the run's head is `0004afc9`; (b) content: the head carries "the above" (row `:501`: the elaboration file, its import line and a disposable census family), the retired guard (blob `0475fe3d…`) and the `A30-0-ADMITS` cell (`ROADMAP.md` blob `e6779380…`); (c) outcome: "all three jobs green. The guard reports 91 PASS and 0 FAIL, its verdict map `D`'s tag for tag and in order; its diff from `D` is 12 lines added and 133 removed" | (a) and (b): the head's objects (§3). (c): **no run evidence is retained.** Run `36222326658` is in `tranche3.remaining` (created 2026-09-26, log expiry 2026-12-25, tier B) |
| `:501` (history sub-closure) | `17de29c2…`, run `36222012214` | the parent head carries the elaboration file, its import line and a census family; the run's outcome | the parent's objects. Run `36222012214` is likewise in `tranche3.remaining` |
| `:489`–`:490` (history sub-closure) | `17de29c2…`; blob `016e5428…` | `OIBridge/ProductStrictLift.lean` at `17de29c2` is blob `016e5428…` | the blob, stored as a plain file, and the trees on its path in both commits |
| `:503` (dependent, not part of this closure) | `62ad3a5f…` | a third head | `62ad3a5f` is a retained `raw:connected` child of `0004afc9`, so `0004afc9` is also on its H4 history path |

**One content claim regenerated from retained and `main` objects.** Claim (c)'s "its diff from `D` is 12 lines
added and 133 removed":

```
git diff --numstat 48450428f528fe489d454458e21c9394aef6a02f:verification/lean/edge_rigidity_probe.py \
                   0004afc9360117ba61523b72854de1aaf63705f0:verification/lean/edge_rigidity_probe.py
12      133     (the guard file)
```

This was run in a disposable clone after `check_objects.py --materialize`. Both blobs are held by `main`
(`8dad60d0…` at `D`, `0475fe3d…`). This regenerates the stated diff. It does not regenerate the run's output.

**Not regenerated:** the guard verdict (91 PASS, 0 FAIL, verdict map identical to `D`'s), which needs `numpy` and
`scipy` (`scipy` is absent here), and "all three jobs green", which needs the Mathlib bridge build. Running the
guard at the head would regenerate the guard's output from the retained tree. It would **not** reconstruct run
`36222326658`, whose log is not retained, and a newer green run would not reconstruct it either.

## 3. Closure at the pinned snapshot

Measured in an isolated disposable full-history clone of `main` after `check_objects.py --materialize`.
Reproduce: `git ls-tree -r -t 0004afc9…` and `git cat-file --batch-check='%(objectsize)'`.

**Full root tree of `0004afc9`:**
- 1,156 tree rows (the root tree, 139 trees, 1,016 blobs);
- 1,151 distinct ids, 36,039,783 content bytes;
- no withheld blob and no gitlink.

The full tree's ids fall into four groups:

| group | ids | archive entries |
| --- | --- | --- |
| stored by the archive for this head (`needed_by` names `0004afc9`) | 6: root tree `e5e70bc5`, `verification/` `dda14af0`, `verification/lean-mathlib/` `f7042861`, `…/OIBridge/` `23ddaf02`, blob `016e5428` (`…/OIBridge/ProductStrictLift.lean`), blob `4151e7c6` (`verification/lean-manuscript-census.json`) | yes |
| held by `main` (reachable from the tranche-2 base; `check_objects.py` H3 passes) | 1,145, among them `verification/ROADMAP.md` `e6779380`, `verification/lean/` `08464957`, `…/edge_rigidity_probe.py` `0475fe3d` and `…/OIBridge.lean` `7a6aaa6c` | no |
| withheld | 0 | — |
| the commit itself | `0004afc9` | yes |

The head differs from act-30's `D` in exactly five files (`git diff --numstat D 0004afc9`):
- `ROADMAP.md`, the census, `OIBridge.lean`, `ProductStrictLift.lean` and the guard;
- three of their blobs later reached `main` through later rounds;
- the census and `ProductStrictLift.lean` blobs did not.

**History sub-closure (H4).** `0004afc9`'s history reaches the base only through `17de29c2`, so `17de29c2`
itself, its root tree `e8e9a726` and its `verification/` tree `a2a2a776` complete the connectivity. Its
`lean-mathlib/`, `OIBridge/`, `ProductStrictLift.lean` and census entries are the same ids as the head's.

**Archive cost:**

| set | entries | stored bytes | content bytes |
| --- | --- | --- | --- |
| the head's own entries (commit + 6) | 7 | 150,943 | 380,798 |
| with the history sub-closure (+ `17de29c2`, `e8e9a726`, `a2a2a776`) | 10 | 152,668 | 382,624 |

**Shared entries.** Four of the head's six tree and blob entries are also named by other retained cited commits:
- `f7042861`, `23ddaf02` and `016e5428` by `17de29c2` and `62ad3a5f`;
- `4151e7c6` by those two and by `6c30c613`.

No entry in the closure is withheld.

## 4. Full-tree restoration versus the claim-specific hypothesis

- **G-full** is the guarantee in force: the exact commit with its complete root tree restorable by
  `--materialize`, and history connectivity per H4. It needs all 1,151 tree ids plus the commit and its retained
  ancestor. The archive stores the 10 entries above, and `main` supplies the other 1,145 tree ids. G-full therefore
  also depends on `main` continuing to hold those 1,145 objects, which H3 checks at every run.
- **G-claim** is the hypothesis: an inclusion-proof package carrying only what lines `:501`–`:502` assert. That is
  the commit, plus the trees on the paths to `ProductStrictLift.lean`, `OIBridge.lean` (the import line), the
  census, `ROADMAP.md` and the guard, plus the blobs whose content is asserted. The archive stores 7 of these
  ids: the commit, `e5e70bc5`, `dda14af0`, `f7042861`, `23ddaf02`, `016e5428` and `4151e7c6`. `main` holds the
  other four: `e6779380`, `08464957`, `0475fe3d` and `7a6aaa6c`.
- **Measured consequence for this head:** the archive's stored set under G-claim equals its stored set under
  G-full, 7 entries either way. The two guarantees differ only in objects `main` holds, which cost the archive
  nothing. This head shows no over-retention by the archive.
- **Not measured:** whether the outcome claims (guard verdict, three green jobs) could be re-run from anything
  less than the full tree. A guard run and a Lean build read files across the tree. This question bears only on
  `main`-held objects, not on archive entries.

## 5. Classification (rule K, preregistered)

**Regeneration test (K1).**
- Setup: a full-history clone holding only `main`'s objects, with the archive not materialized. Command:
  `sh regen.sh <clone>` (output: `controls-out/regen.txt`). The clone has 24,490 objects reachable from `main`.
- Result:
  - 9 of the 10 ids are absent from the clone's object store and unreachable from `main`.
  - `016e5428` is reachable from `main` only at the archive's own path
    `verification/audits/evidence-retention/objects/blob/01/016e5428…` (added in `a3020cf0`), which K1 excludes.
- Consequence: no id has a regeneration route from `main`, so no byte comparison was possible and no entry is
  redundant.
- Not attempted: rebuilding a tree from its entries. The entry list exists only in the tree object itself, and a
  commit's text (author, dates, message) exists only in its stored copy.

| id | kind, path | stored / content bytes | G-full | G-claim | grounds |
| --- | --- | --- | --- | --- | --- |
| `0004afc9360117ba61523b72854de1aaf63705f0` | commit | 741 / 741 | **required** | **required** | cited by id at `:502`; no other bytes carry the id; on the H4 path of `62ad3a5f` (`:503`) |
| `e5e70bc53a1c23a7b83ed902d9879868292cf5d9` | root tree | 374 / 392 | **required** | **required** | G-full: the head's tree. G-claim: on every inclusion path. Not on `main` |
| `dda14af07f862ee459a803e4e888c286b1f6bd57` | `verification/` | 595 / 678 | **required** | **required** | on the paths to `ROADMAP.md`, the census and the guard. Not on `main` |
| `f7042861b741c353e989fc0f390a525bd1604a45` | `verification/lean-mathlib/` | 158 / 159 | **required** | **required** | on the paths to `OIBridge.lean` and `ProductStrictLift.lean`. Not on `main` |
| `23ddaf02eb50809f4d87cf426c20c81a8e30cf18` | `…/OIBridge/` | 5,678 / 8,984 | **required** | **required** | on the path to `ProductStrictLift.lean`. Not on `main` |
| `016e542872383b296bb0255d8e9ff1561d36fbcc` | `ProductStrictLift.lean` | 43,639 / 43,639 | **required** | **required** | cited by id at `:490`; asserted at `:501`/`:502` ("the elaboration file"). Not on `main` outside the archive |
| `4151e7c65fbb9ceb331636cb5becce876eddacfa` | `lean-manuscript-census.json` | 99,758 / 326,205 | **required** | **required** | asserted at `:501`/`:502` ("a disposable census family", stated to exist only on that branch); no other carrier of these bytes; not on `main` |
| `17de29c27ed43d7f105aa8518451d8ed61c59937` | commit (history) | 756 / 756 | **required** | **required** | G-full: H4 connectivity of the head. G-claim: cited by id at `:489` and `:501` |
| `e8e9a726ad688afc447214cbdc52b96675513307` | `17de29c2` root tree | 374 / 392 | **required** | **required** | G-full: the parent's tree. G-claim: on `:489`'s inclusion path. Not on `main` |
| `a2a2a7762446225c91ef1bfa17af98d14ecece26` | `17de29c2` `verification/` | 595 / 678 | **required** | **required** | likewise |

**Counts:**
- G-full (primary): 10 required, 0 redundant, 0 optional, 0 undetermined.
- G-claim (hypothesis): 10 required, 0 redundant, 0 optional, 0 undetermined among archive entries.
- G-claim, objects `main` holds: undetermined. These are not archive entries.

## 6. Controls

Command (one run, recorded): `sh controls.sh <empty-dir> /home/user/incompleteness dda14af07f862ee459a803e4e888c286b1f6bd57`.

Setup:
- The script clones `main` with `--no-hardlinks --no-local --single-branch` and unshallows it from the public
  repository, because the source checkout is shallow.
- It makes one independent `--no-hardlinks --no-local` clone per variant, checked out detached at `92de3143`.
- It asserts that there is no `objects/info/alternates`.
- Each variant runs `python3 -I -B` on `check_objects.py`, `check_objects.py --reconstitute` and
  `check_retention.py`.
- No checker file is modified in any variant (`git diff --stat -- '*.py'` empty).

The omitted object is `dda14af0`, the head's `verification/` tree. It is classified required, has no citation of
its own, and is named only by the pilot head.

| variant | change in the disposable clone | `check_objects` tree | `check_objects --reconstitute` | `check_retention` |
| --- | --- | --- | --- | --- |
| LIVE | none | exit 0, `check_objects: OK` | exit 0, `check_objects: OK` | exit 0, `RETENTION  HOLDS (0 failure(s), 84 gap(s))` |
| N1 | delete `objects/loose/dd/a14af07f…` | exit 1, `FAILED (3)` | exit 1, the same 3 | exit 0 (it leaves `objects/` to `check_objects.py`) |
| N2 | N1 + delete the manifest entry | **exit 0, `OK`** | exit 1, `FAILED (1)` | exit 1, 2 failures |
| N3 | N2 + update the evidence manifest's size and sha256 for `objects/manifest.json` | **exit 0, `OK`** | exit 1, `FAILED (1)` | **exit 0, `HOLDS`** |

Failure lines, verbatim:

```
N1  FAIL  O1 dda14af07f86: stored file loose/dd/a14af07f862ee459a803e4e888c286b1f6bd57 is missing
N1  FAIL  O4 0004afc93601: tree dda14af07f86 is broken
N1  FAIL  O4 e5e70bc53a1c: tree dda14af07f86 is broken
N2  FAIL  H3 dda14af07f86 is named by a retained object, is neither retained nor withheld, and is not on main
N2  FAIL  R1 tranche-record: objects/manifest.json sha256 differs
N2  FAIL  R1 tranche-record: objects/manifest.json size 727173, recorded 727711
N3  FAIL  H3 dda14af07f86 is named by a retained object, is neither retained nor withheld, and is not on main
```

Every failure line names the omitted object, the commit or tree that names it, or the manifest that recorded it.
The live control is green, so every variant meets the preregistered pass criterion.

**What the controls show about the checker:**
1. A plain file omission (N1) fails tree mode at once, on that object alone.
2. A coordinated omission of a tranche-2 dependency entry (N2, N3) passes tree mode:
   - O3 does not require every pinned tranche-2 id to have an entry (`EXACT_FROM = 5`);
   - O4 treats an unretained name as "expected on main".
3. It is caught by `check_retention` R1's manifest pin (N2) and, once that pin is also updated (N3), only by
   history mode H3.
4. H3 is in effect the regeneration criterion: it accepts an unretained name only if `main` reaches it. A
   narrowing that respected H3 could therefore drop only objects `main` holds.
5. Tree mode alone, `check_objects.py` without `--reconstitute`, is not sufficient protection against a
   coordinated omission.

**Not determined:**
- `check_retention.py --gate` on N3, which would run H3 inside the release-gate step, was stopped by a 600 s
  timeout during its self-test phase. It reached no verdict, and it was not re-run (§A.40 sends repeated
  self-test runs to CI).
- History mode run in the shallow source checkout (377 commits) fails spuriously with 161 failures, for example
  `H3 …: parent … is neither retained, nor on main, nor named`. All history-mode results above come from
  full-history clones (3,368 commits).

## 7. Limits of this pilot

- One head. Its result is that the archive's stored set is no larger than the claim-specific package, because
  the head's tree differs from `main`-held content only along the five changed files' paths. Whether this holds for
  other heads is a **hypothesis for the next step, not a finding**. In particular, it is untested for `raw:tree`
  heads, for `raw:partial-tree` heads, and for heads whose `main`-absent blobs include files no claim names.
- The claims' outcome evidence (runs `36222326658` and `36222012214`) is not retained. It is part of
  `tranche3.remaining`, so the bulk-extraction question in #862 covers it.
- No archive object, ref, manifest, pin or record was changed. All modifications were made in disposable clones,
  which have since been deleted. No workflow was dispatched.
- This pilot has not been independently reviewed.

## Files beside this note

| file | sha256 | role |
| --- | --- | --- |
| `PREREG.md` | `37a47210…825cca` | selection, closure and classification rule, fixed before measurement |
| `closure.py` | `5a26028a…0708d` | applies rule S and computes the closure from the archive's own files |
| `closure.json` | `e6b0b51d…f7ed1` | its output |
| `regen.sh` | see the file | regeneration test K1 against a `main`-only full-history clone |
| `omit.py` | `966723e0…6bca3` | applies N1/N2/N3 to a disposable clone, after verifying that each manifest serialization round-trips byte-for-byte |
| `controls.sh` | `9455a10c…251d1d` | builds the isolated clones and runs the live and omission controls |
| `controls-out/` | — | the controls' and the regeneration test's raw outputs |
