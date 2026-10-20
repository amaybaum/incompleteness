# Independent review: PR #882 tranche-2 minimality pilot (head `0004afc9`)

Reviewer: independent agent. I did not write the pilot. Read-only toward `/home/user/incompleteness` and GitHub.
Pilot under review: `scratchpad/a882/` (PILOT.md, PREREG.md, PREREG.sha256, closure.py/json, regen.sh, omit.py,
controls.sh, controls-out/). My work area is `scratchpad/rev882/`. My code is `tools/rev_closure.py` (selection and
object decode, independent of closure.py) and `tools/n3.py` (an N3 edit written independently of omit.py). My
check outputs are in `out/`.

Environment: `df -h /tmp` showed 28G free at the start. I made one independent clone,
`git clone --no-local --no-hardlinks /home/user/incompleteness clone`, set origin to GitHub and ran
`git fetch --unshallow origin '+refs/heads/main:refs/remotes/origin/main'`. The result: `is-shallow-repository`
false, `rev-list --count 92de3143` = 3368, no `objects/info/alternates`. The LIVE and N3 clones were each made
with `git clone --no-local --no-hardlinks clone <v>`, are not shallow, have no alternates, and hold neither
`dda14af0` nor `0004afc9` in their stores. All three clones were deleted at the end.

## Verdict: **CHANGES NEEDED** (narrow: one text correction; no re-measurement needed for the classification)

Every number checked reproduces exactly: the selection, the citation, the closure counts and bytes, the regeneration
result, and the LIVE and N3 outputs (byte-identical to the author's). The per-object classification (10 required,
0 redundant) stands. One stated conclusion about the checker is wrong: §6 item 4 and, through it, item 5. It is
contradicted by the pilot's own K1 result, and it bears directly on the extrapolation step, so it blocks.

***

## Blocking

### B1. §6 item 4 is false for byte-copy blobs. H3 is not "in effect the regeneration criterion"

PILOT §6.4 says: *"H3 is in effect the regeneration criterion: it accepts an unretained name only if `main` reaches
it. A narrowing that respected H3 could therefore drop only objects `main` holds."*

H3 counts as "on main" everything reachable from **any** tranche base, unioned. That includes tranche 5's base
`ec36234c`, whose history contains the archive's **own** plain-file copies of byte-copy blobs. K1 explicitly
rejects that route as circular. H3 does not.

Code (`check_objects.py` at `92de3143`):
```
1529:    main_objs = set(l.split()[0] for l in gitok(['rev-list', '--objects', base], root)...
1616-1619:  for b, (o2, c2, k2, _) in per_base.items(): if b != base: main_objs = main_objs | o2 ...
1631-1633:  for x in sorted(external): if x not in main_objs: F('H3 ... is not on main')
```
H4's "held" set is `set(content) | main_objs` (line 1621), so H4 is no stricter. The self-test's only
"file and entry removed" case, `drop_object` at line 1811, drops a **zlib tree** (`ztree`), so it never exercises
this case.

Measurement, in my full-history clone:
```
$ git rev-list --objects ec36234c... | sort -u > base-ec36.txt;  comm -23 tree-distinct.txt base-ec36.txt
23ddaf02… 4151e7c6… dda14af0… e5e70bc5… f7042861…        # 5 ids: 016e5428 is NOT among them
$ (same against 49ba3297, tranche 2's own base)
016e5428… 23ddaf02… 4151e7c6… dda14af0… e5e70bc5… f7042861…   # 6 ids
$ git log 92de3143 -m --format= --name-only --find-object=016e542872383b296bb0255d8e9ff1561d36fbcc | sort | uniq -c
      4 verification/audits/evidence-retention/objects/blob/01/016e542872383b296bb0255d8e9ff1561d36fbcc
```
So for H3, the pilot head's own required blob `016e5428` (`ProductStrictLift.lean`, cited at `:490`) counts as
"held by main", but only through the archive's own path. K1, in the pilot's §5 and regen.txt, says it has **no**
regeneration route from `main`. The two criteria disagree on this pilot's own head.

Scope across the archive (my count over stored entries at `92de3143`):
```
((2, 'blob', 'raw'), 'in_latest_base') 25        # all 25 are mechanism byte-copy, all cited
(every other stored entry: absent from main)
```

**Consequence.** By code reading, deleting one of these 25 entries in a coordinated way (file, entry and evidence-
manifest pin together, as in N3) passes O2/O4 in tree mode and passes H3/H4 in history mode. H7 checks only entries
that are still present. I did **not** run such an N4. It is outside this review's limit of LIVE and N3 only. So it
is undetermined whether some other rule, such as an O7 or check_retention citation rule, would catch the omission of
a *cited* byte-copy blob. Either way, the pilot's sentence that a narrowing respecting H3 "could drop only objects
`main` holds" overreaches. For these 25 objects, "main holds it" means "main's history holds the archive's own
copy". K1 treats that as not redundant.

**Required change:**
- Restate §6.4 to cover only objects that are neither byte-copy nor reachable from a tranche base through the
  archive's own paths.
- Name the H3/K1 divergence for the 25 byte-copy entries, with `016e5428` as the in-pilot example.
- Scope §6.5 accordingly.
- Before extrapolating, record this as an assumption-watch item. Optionally add an N4 on `016e5428`, or on an
  uncited-by-others byte-copy blob, run in CI or under explicit owner approval.

***

## Notes (non-blocking; fix before extrapolating where marked)

### N1. Preregistration: hash verified, but its precedence rests only on local mtimes
```
$ sha256sum PREREG.md          -> 37a472102dbc839322d1d1948139a5bb9ad1b7358b85678380f23317f9825cca   (= PREREG.sha256)
$ stat -c '%n %y' ...           PREREG.md 01:21:09, PREREG.sha256 01:21:13 (contains 2026-10-20T01:21:13Z),
                                closure.py 01:22:07, closure.json 01:22:11, out/live_* 01:23:11–01:26:16,
                                omit.py/controls.sh 01:28, regen.sh 01:43:50, controls-out/* 01:45:22
```
- The order is consistent with "fixed before measurement". It is self-attested only: nothing was pushed, and
  `origin/audit/retention-minimality-20261019` carries no pilot file. A pushed checkpoint (§A.43) would make it
  checkable.
- The author discloses that rule S was written after seeing manifest entry 0. Rule S is mechanical and
  reproduces (below), so this does not void it, but the selection was not blind.

### N2. N3 was not preregistered
PREREG defines N1 and N2 only. PILOT §6 says *"every variant meets the preregistered pass criterion"*. N3 has no
preregistered criterion, so N3 should be labelled as an added, post-hoc control.

### N3. The scope of the tree-mode finding (§6.2/§6.5) vs the release gate
- The release gate step is `check_retention.py --gate` (`tools/release_gate.py:189-190`). It calls `objects_gate`,
  which runs `check_objects.py --reconstitute` (lines 1137-1142), and `good` requires `obj_ok`.
- By code reading, therefore, the gate fails N3 through the same H3 line I reproduced. PILOT records this as "not
  determined", which understates it. Recommended restatement: "caught by the release gate's history mode, by code
  inspection plus the standalone `--reconstitute` run; gate not executed."
- "Tree mode passes a coordinated tranche-2 omission" is the checker's **documented** design. The docstring at
  lines 20-27 reads "from tranche 5 on (EXACT_FROM) every pinned id has its entry", and line 744 reads "Tranches 2
  and 4 keep the rule they were cut under". It elaborates a known limitation and is not a new blind spot. (B1 is
  the new one.)

### N4. Per-head attribution of the three history entries under G-claim (fix before extrapolating)
- §5 gives `17de29c2`, `e8e9a726` and `a2a2a776` G-claim "required" on grounds `:489`/`:501`. Those are
  **`17de29c2`'s** citations, not the pilot head's (`:502`).
- Under PREREG's G-claim for h, meaning h's surviving claims only, verifying `0004afc9`'s identity and its tree's
  content does not need the parent objects. §4 itself says "7 entries either way", and §5's counts say 10.
- Their archive-level status is still **required**: by H4 for h under G-full, and by `17de29c2`'s own citations.
  Only the per-head ground is wrong. Aggregating per-head counts across heads would double-count them.
- Manifest check: `e8e9a726` and `a2a2a776` have `needed_by` = [`17de29c2`] only. `17de29c2` has `needed_by` = []
  and is cited at `:489` and `:501` (×2).

### N5. The G-full "required" argument for the history entries is correct
- H4 (lines 1647-1680) creates a ref at every raw:connected commit and runs `fsck --connectivity-only`.
- It requires `rev-list <c> --not <base>` to pass only through retained raw:connected commits. From `0004afc9`,
  that walk reaches `17de29c2` and its trees `e8e9a726` and `a2a2a776`.
- `48450428` (act-30's `D`, preregistration line 48) is an ancestor of `49ba3297`.

### N6. Process: a local `--gate` run
- `controls-out/N3.gate.txt` shows that `check_retention.py --gate`, which includes the full self-test, ran locally
  and was killed at 10m0s.
- §A.40 places self-test batteries in CI, and the owner's pilot instruction did not ask for a gate run. It ran once,
  was disclosed, and was not repeated. It should not be repeated locally; use `retention-tests` with owner approval
  if a gate verdict on N3 is wanted.

### N7. Minor text precision
- PREREG says "a legacy/receipt class". closure.py uses `('native-record','legacy-record')`. The manifest's classes
  are `native-record` 280, `legacy-record` 66, `archive-self` 37 and `mutable` 4, with no receipt class, so the
  selection is not affected.
- §6.4 says "main reaches it". The checker's actual criterion is "some tranche base reaches it" (see B1).

### N8. Representativeness, so extrapolation stays barred (the author already disclaims it)
- Rule S's candidate set has 137 tranche-2 commits: raw:connected 102, raw:tree 31, raw:partial-tree 2,
  inclusion-proof 2.
- For a raw:connected head, "archive set under G-claim = under G-full" is close to structural. H7 forbids storing
  anything `main` reaches, so the stored set is the main-absent part of the tree. The two coincide whenever every
  main-absent blob is asserted by some claim. Here both main-absent blobs (`016e5428`, `4151e7c6`) are asserted.
- This head is therefore a weak test of over-retention. PILOT §7 correctly names raw:tree, partial-tree and
  unasserted-blob heads as untested.

***

## What I verified, with commands and outputs

**(1) PREREG hash.** See N1. The hash matches.

**(2) Citation on `main` `92de3143`:**
```
$ git -C /home/user/incompleteness rev-parse 92de3143:verification/programmes/oi-qm/track-b/act-30-product-strict-lift/preregistration.md
c637999c884328cb085cb9dbbf27a39bb44e6643
$ git -C /home/user/incompleteness show 92de3143:<that path> | sed -n '486,504p'
489: `verification/lean-mathlib/OIBridge/ProductStrictLift.lean` at `17de29c27ed43d7f105aa8518451d8ed61c59937`,
490: blob `016e542872383b296bb0255d8e9ff1561d36fbcc`. ...
496-497: ... Its census family and import line exist only on that branch.
501: | 36222012214 | `17de29c2…` | the elaboration file, its import line, a disposable census family | all three jobs green ...
502: | 36222326658 | `0004afc9360117ba61523b72854de1aaf63705f0` | the above, the retired guard (blob `0475fe3d…`) and the
     `A30-0-ADMITS` cell (`ROADMAP.md` blob `e6779380…`) | all three jobs green. The guard reports 91 PASS and 0 FAIL,
     its verdict map `D`'s tag for tag and in order; its diff from `D` is 12 lines added and 133 removed |
503: | 36222347638 | `62ad3a5f…` | ...
$ git grep -n -I -e '0004afc' -e '36222326658' 92de3143 -- . ':!verification/audits/evidence-retention/objects/*'
  check_objects.py:221 (tranche-2 membership pin), manifest.json:15683 (tranche3.remaining run), preregistration.md:502
```
The only line outside the archive is `:502`. Both runs, `36222326658` and `36222012214`, are in `tranche3.remaining`
(indices 57 and 56). `62ad3a5f`'s parent is `0004afc9`.

**(3) Independent closure** (`python3 -I -B tools/rev_closure.py clone`, then git):
```
selected candidates: 137 first: 0004afc9360117ba61523b72854de1aaf63705f0 index 0
stored objects written and id-verified: 993            # every stored file sha256- and id-checked
$ git ls-tree -r -t 0004afc9 | wc -l  -> 1155 (+ root = 1156 rows);  1016 blob, 139 tree, 0 commit (no gitlinks)
distinct ids incl. root: 1151;  content bytes (cat-file --batch-check): 36039783
withheld entries among head tree ids: 0
not reachable from main 92de3143: e5e70bc5, dda14af0, f7042861, 23ddaf02, 4151e7c6    (+016e5428 only via archive path)
head entries (commit + needed_by): 7, manifest bytes 150943 = actual stored file bytes 150943, content 380798
with history sub-closure: 10, 152668 = 152668, content 382624
$ git diff --numstat 48450428 0004afc9  -> ROADMAP.md 1/1, census 9/0, OIBridge.lean 1/0, ProductStrictLift.lean 443/0,
                                          edge_rigidity_probe.py 12/133      (five files; guard 12/133 regenerated)
shared: 17de29c2 and 62ad3a5f name 4151e7c6 f7042861 23ddaf02 016e5428; 6c30c613 names 4151e7c6
e6779380, 0475fe3d, 7a6aaa6c, 08464957: reachable from 49ba3297 and from main
```
All PILOT §3 figures match. (Their `out/h_not_base.txt` lists `e6779380`, `7a6aaa6c` and others as not on base.
That reflects `rev-list --not`'s approximate object exclusion. The exact set comparison above shows they are on
base, so §3's text is right.)

**(4) Regeneration claim** (in my unshallowed clone, packed objects only, before materialization):
```
0004afc9 packed=0 reach_main=0   e5e70bc5 0/0   dda14af0 0/0   f7042861 0/0   23ddaf02 0/0
016e5428 packed=1 reach_main=1   4151e7c6 0/0   17de29c2 0/0   e8e9a726 0/0   a2a2a776 0/0
016e5428 paths in main history: only verification/audits/evidence-retention/objects/blob/01/016e5428… (4 commits incl. merges)
```
Confirmed: 9 of 10 are absent, and the 10th is present only at the archive's own path. No entry is redundant under K1.

**(5) Controls rerun** (LIVE and N3 only; `python3 -I -B`; no `--self-test`, no `--gate`). N3 was applied with my
own `tools/n3.py`. The new `objects/manifest.json` is 727173 bytes, sha256 `a83ea514…cbb45e`, identical to the
author's.
```
LIVE tree exit=0 12s          check_objects: OK
LIVE reconstitute exit=0 14s  check_objects: OK
LIVE retention exit=0 2s      RETENTION  HOLDS (0 failure(s), 84 gap(s))
N3 tree exit=0 11s            check_objects: OK
N3 reconstitute exit=1 14s    FAIL  H3 dda14af07f86 is named by a retained object, is neither retained nor withheld, and is not on main
                              check_objects: FAILED (1)
N3 retention exit=0 1s        RETENTION  HOLDS (0 failure(s), 84 gap(s))
$ cmp rev882/out/{LIVE,N3}.{tree,hist,ret}.txt a882/controls-out/...   -> all six identical to the author's
```
N3's claim holds as stated for `dda14af0`, a zlib tree.

**(6) Overreach:**
- B1 (blocking), plus N2, N3, N4 and N8.
- PILOT §7 explicitly disclaims extrapolation beyond this head, and I found no extrapolating sentence other than
  §6.4–6.5.
- The "required" argument for the history-connectivity entries is correct under G-full (N5). Its G-claim ground is
  misattributed (N4).

## Cleanup
The `clone`, `LIVE` and `N3` clones were deleted after this review. `tools/` and `out/` were kept as the review's
trail. Nothing in `/home/user/incompleteness` was changed. There were no GitHub writes and no dispatches.

***

## Re-review of the corrected pilot (PILOT.md `b03d2204…`, CORRECTIONS.md `8239a34a…`)

I ran no checker, self-test or gate, and made no repo or GitHub writes.

### Verdict: **CHANGES NEEDED** (one scope word, at five sites; everything else closed)

### Unchanged files, confirmed
```
$ sha256sum PREREG.md closure.py closure.json omit.py controls.sh regen.sh PILOT.original.md
37a47210…825cca  e6b0b51d…f7ed1 (closure.json)  5a26028a…0708d (closure.py)  966723e0…6bca3 (omit.py)
9455a10c…251d1d (controls.sh)  4ca00d3b…a533 (regen.sh; mtime 01:43:50, unchanged)  eabdacb6…0f6f (PILOT.original.md)
```
- These match the hashes in the original PILOT's table, which I reviewed.
- PILOT.original.md has the original's size (17375) and mtime (01:45:14), and its text is the one quoted in my
  first pass.
- controls-out/ is unchanged (mtimes are all 01:45:22). `cmp` of my LIVE/N3 outputs against
  controls-out/{LIVE,N3}.{objects-tree,objects-history,retention}.txt: all six are still identical.

### (4) The ec36 listing is correct
```
$ git -C /home/user/incompleteness cat-file -t ec36234c…   -> commit      (shallow clone: is-shallow-repository = true)
$ git -C /home/user/incompleteness ls-tree -r ec36234c -- verification/audits/evidence-retention/objects/blob/ | wc -l  -> 25
  every file's blob id equals its filename (no mismatch)
  manifest @92de3143, stored blobs by (mechanism, form): byte-copy/zlib 227, byte-copy/raw 25
  sorted(raw-form blob entries) == sorted(ec36 blob ids): True     (016e5428 included)
```
Author's `out/ec36_blobfiles.txt` lists the same 25 paths.

### (1) B1: substantively closed, with one scope error remaining (blocking)
These parts are now right:
- §6.4 states the H3 union over tranche bases with correct line references (`:1529`, `:1614–1619`,
  `:1631–1633`, `:1621`).
- §6.4 gives `016e5428` as the in-pilot example, and the K1/H3 disagreement on it.
- §6.4 gives the count of 25, and identifies them as exactly the raw-form blob entries.
- §6.5 marks the consequence as code-reading only, says it is open whether another rule catches the omission, and
  marks N4 as **not run**. Tree mode and H3 are scoped correctly ("only for objects outside the 25").
- The CORRECTIONS.md row for B1 is accurate.

**R1 (blocking): "byte-copy" is used where "raw-form (plain-file) byte-copy" is meant.**
- The manifest has **252** byte-copy blobs. Only the **25 raw-form** ones are reachable through the archive's own
  paths. The 227 zlib-stored byte-copy blobs are not, because a loose-object file's blob id differs from the object's
  id, so H3 behaves for them as it did for `dda14af0`.
- The overbroad sites:
  - PILOT.md:236, "H3 does **not** match K1 for the archive's byte-copy blobs";
  - :252, "N4 (a coordinated omission of a byte-copy blob such as `016e5428`)". An N4 on a zlib byte-copy blob
    would be caught by H3, so N4 must name a raw-form one;
  - :267, the assumption-watch item: "The archive's own plain-file copies make **every** byte-copy blob reachable
    from tranche bases". This is false for 227 of 252;
  - :269, "H3 cannot serve as the redundancy criterion for byte-copy blobs";
  - :292, "the H3/K1 divergence for byte-copy blobs".
- Fix: at each site, write "raw-form (plain-file) byte-copy blobs", or "the 25 plain-file blobs". In the
  assumption-watch item, say "every blob the archive stores as a plain file under `objects/blob/` is reachable from
  every tranche base whose history contains that file".
- My own B1 heading ("false for byte-copy blobs") introduced this imprecision, and the correction inherited it.

### (2) The notes are applied correctly
- **N2:** N3 is labelled "added; not preregistered". Pass criteria are claimed only for LIVE, N1 and N2.
- **N3:** the gate result is given by code reading via `objects_gate` (`check_retention.py:1137–1142`). The
  `EXACT_FROM` design is cited as documented (line 744).
- **N4:** G-claim(h) is 7 and G-full(h) is 10. The three history entries carry the ground "required by
  `17de29c2`'s own claims". §4 and §5 are reconciled, and a no-summing note is added.
- **N6:** the single gate run is recorded and is not to be repeated locally.
- **N7:** the class-name note sits in Fixed inputs and PREREG is untouched. The wording is now "some tranche base
  reaches it", and §4 says "own tranche base" for H7.
- **N8:** a weak-test paragraph is added to §4.

### (3) The diff from PILOT.original.md
- The diff contains only the listed corrections and the status/§7/file-table updates.
- No new overclaim apart from R1.
- Minor, non-blocking: §6.4's second bullet says "That is what N2 and N3 show". N2 and N3 show it for `dda14af0`
  only; the general statement rests on code reading.
- The status line "the corrected text has not been re-reviewed" will need updating after this re-review.

***

## Third pass (PILOT.md `7c3eed73…`, coordinator-applied R1 fix): **ACCEPT WITH NOTES**

- **Edits checked.** I reversed the seven stated edits (lines 235, 236, 252, 267, 269, 291 and 292) in memory, and
  the result hashes exactly to `b03d2204158f8a3a7817651f07a1322638b31c7e787b7d8db7fdd4d5b402bb61`. So no other byte
  of PILOT.md changed.
- **Wording.** Every changed line now reads "the 25 raw-form (plain-file) byte-copy blobs" or "the 25 raw-form
  byte-copy blobs" where it said "byte-copy blobs". That covers the H3/K1 statement, the N4 description, the
  assumption-watch item and the open-items line. Line 235 now confines the N2/N3 evidence to `dda14af0` and says
  the general statement rests on code reading. The status line (291) is accurate.
- **R1 is closed.** No new overclaim.
- **Other files.** PREREG.md (`37a47210…`) and closure.json (`e6b0b51d…`) are unchanged.
- **Cosmetic notes, non-blocking:**
  - Line 255's "outside the 25 byte-copy blobs" is correct, because "the 25" is defined at line 244, but it could
    say "raw-form" for uniformity.
  - Several edited lines now run past the file's ~120-column wrap.
