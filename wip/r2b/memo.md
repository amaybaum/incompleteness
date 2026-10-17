# R2-B: keeping cited off-main objects reproducible from `main` — survey and design memo

Status: a read-only survey and a proposal for the owner. It is not a decision, and nothing was pushed, dispatched,
commented, tagged or branched. `main` is `66a981d5`; the audit base is `fc5abade`. Every number below is in
`offmain-inventory.json` beside this memo. The scripts that produced them are in `src/`, and their raw outputs are in
`runs/`, `scan/` and `mech/`.

## 1. Summary

- **Control: green.** At `fc5abade`, in a repository holding exactly the remote branches' objects, `offmain_audit.py`
  reproduces its recorded output byte for byte: 107 commits and 75 objects (71 blobs, 4 trees).
- **At `66a981d5` the off-main set is unchanged.** It holds the same 107 commits and 75 objects. None became
  reachable and none was added.
  - Every new citation is in the evidence-retention archive itself, which the audit's rules class as mutable. The
    audit output alone cites them 211 times; `audit.md`, `README.md`, `build_archive.py`, `manifest.json` and the four
    `bg3/*.json` add 12 more.
  - There are 12 new unresolved 40-hex tokens. All are action and toolchain SHAs inside the retained BG-3 design log.
- **The 107/75 is a lower bound** (§2.2). The audit counts only the cited ids whose objects happen to be in the clone.
  Three wider universes, at `66a981d5`:

  | universe | what it adds | commits | objects |
  | --- | --- | --- | --- |
  | U2 | GitHub pull-request heads | 121 | 76 |
  | U4 | objects in the shared clone that no ref holds | 184 | 83 |
  | U5 | objects GitHub still serves when asked by full SHA | 202 | 90 |

  - The ids beyond U1 are cited at 155 locations, 53 of them in legacy records.
  - A second byte-pinned citation exists: `RepresentativeNaturality.lean:147` cites `52b64009`, which no ref holds.
  - Ten cited in-repository ids are not served by GitHub at all.
- **Excerpt hazard: none.** None of the 194 R1 excerpt blobs is in the ancestry of any cited commit, in any carrier of
  any cited object, or in any cited object, in any universe. The test was checked against positive and negative
  controls (§3.4).
- **Recommendation, mixed per class (§5).**
  - **Blobs:** copy the bytes (ii-a). This restores the blob ids themselves on `main`. A probe shows it revives OG-1's
    frozen self-test.
  - **Commits:** store raw git objects (ii-c): the commit object, plus those of its trees and blobs that `main` lacks.
    No history is imported.
    - For the 53 cited commits whose parents are all on `main`, this reconstitutes the exact commit, fully connected,
      in any clone of `main`. A probe shows this for K2-GUARD-1's predicted tree, whose recorded check and verdict
      reproduce.
    - For the other 45, the commit id and the full tree are verified. The parents are named but not retained.
  - **The two OI-CHANNEL-1 sources (`78aa5b25`, `e7d380fc`):** commit-anchored inclusion proofs (ii-b). That is 31
    objects and about 100 KB, instead of 27 commits and 262 MB of research history.
  - **Bundles (i) and merges (iv):** rejected. Neither can carry the needed commits without carrying their off-main
    ancestry: 241 commits, 280 MB uncompressed and 374 raw logs for U1.
  - **A separate archive repository (iii):** acceptable only as extra provenance. It does not meet §A.42 on its own.

## 2. Re-running classes C and O

### 2.1 Method and control

`src/scan.py` reimplements the audit's class C and O code verbatim: the same file selection and skip list, the same
7–40-hex token regex, `cat-file --batch-check` resolution, `merge-base --is-ancestor` for commits, `rev-list --objects`
reachability for blobs and trees, and the same receipt / native-record / legacy-record / mutable classifier. It also
prints the audit's C and O sections, without the branch holdings, so it can be diffed against the audit's own output.

The audit's result depends on which objects the clone holds. I therefore froze the ref state at 20:18:29Z and built
universes from it. U1–U4 are self-contained repositories made with `git repack -a`, with the alternates removed. U5 is
U4 plus the objects fetched from GitHub:

| universe | contents | C at `fc5abade` / `66a981d5` | O at `fc5abade` / `66a981d5` |
| --- | --- | --- | --- |
| U1 | the remote branches (`refs/remotes/origin/*` without `pull/*`) and the five local `refs/remotes/pr/*`, as the audit describes | 107 / 107 | 75 / 75 |
| U2 | U1 plus GitHub PR head refs (`refs/pull/*/head`) | 121 / 121 | 76 / 76 |
| U4 | U2 plus every object in the shared clone's store, including ones on no ref | 184 / 184 | 83 / 83 |
| U5 | U4 plus what GitHub serves by SHA for each full-length cited token that resolved nowhere | 202 / 202 | 90 / 90 |

Control results:
- The audit itself, run in U1 at `fc5abade`, is **byte-identical** to `offmain_audit-output.txt`.
- The reimplementation's C and O sections diff empty against the audit's output in all four universes, at both
  commits.

**Provenance note (§A.26).** While this survey ran, a concurrent session wrote to the shared clone's `.git`:
- at 20:14:06Z it fetched `+refs/pull/*/head:refs/remotes/origin/pull/*` (852 refs);
- at 20:14:44Z it fetched cited commits by SHA.

I wrote nothing to the shared clone and moved, deleted or adopted nothing. My first re-run had straddled the fetch, so
its branch groupings picked up `pull/*` refs while its C/O counts did not. That is why every measurement uses the
frozen universes above, and why the objects that session brought in are reported separately (U4), not mixed into the
control. Git objects are content-addressed, so their identity is self-verifying. They were used read-only.

### 2.2 The inventory is a lower bound

The audit's rule "hex tokens that resolve to no object are not reported" silently drops every cited commit whose branch
was deleted before the clone was made. Its sentence "every one is held by at least one branch; none is yet
unreachable" is therefore true of the 107 it could see, and of nothing else. Beyond U1, at `66a981d5`:

- **14 commits and 1 tree, held only by PR head refs.** These are GR-1 (legacy record: attempt-2 stages and its
  certified head `5e59122e`), act 25's first execution attempt (legacy record), and V3-14's five rehearsals with its
  predicted tree `a31642ac`. V3-14's rehearsals are the execution evidence §A.39 requires for a destructive round.
- **63 commits and 7 blobs/trees, held by no ref at all.** These are the design and countercontrol heads of acts 30–45
  and NB-1. They are present in the shared clone only because the concurrent session fetched them by SHA. Among them
  is `97a8805f`, which act 40's preregistration names as the argument of the replay control
  `tools/probe_replay_check.py 97a8805f …`.
- **18 commits and 7 blobs, held by nothing local, which GitHub still serves by full SHA.** These include act 19's
  closure chain (`ae983580`, `52b64009`, `5103154a`, `1dd963ba`). The closure (a legacy record) says of it: "The
  execution branch … is preserved and is not merged". No branch holds it now.
  - Also here are SI-3's stage commits and head, CV-2's blobs, act 42's research originals and the countercontrols of
    acts 30, 31, 32, 38 and 39.
  - The sweep probed 49 full-length tokens. GitHub served 25 (17 commits, 8 blobs) and refused 24.
- **Not recoverable.** Ten cited in-repository ids resolve nowhere and GitHub refuses them ("not our ref"):
  - GR-1's `d5178e2f`, `70e34e82`, `2a67dfca` and `73f50597`;
  - act 35's `2ae4dbee` and probe blob `52009e08`;
  - act 33's `4c4155da` and `cff3c156`;
  - act 45's predicted head `ad64b60319e1…`. Its tree `12a695df` survives through a re-commit `ad64b603b7a1…`,
    which shares the same 8-hex prefix;
  - CV-2's `46fb79d1`, "committed in scratch".

  The other 14 refused tokens are external (Mathlib, action and toolchain SHAs), a prefix constant, and other
  repositories' ids in the retained log. Abbreviated tokens that resolve nowhere cannot be probed, so the true count
  may be higher.
- **A second byte-pinned "mutable" citation.** `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean:147`
  cites `52b64009` ("the exact shape act 19's execution committed at `52b64009`").
  - The audit classes the file as mutable.
  - Its blob `4c1137f3` is pinned by the preregistrations of acts 21–24, so, like `oi_channel1_check.py:2`, the
    citation cannot be edited.
  - Its target is held by no ref and survives only as long as GitHub keeps the unreferenced object.

These are equally "cited on `main`, not reachable from `main`". Whether R2-B covers them is a scope question (§6, Q1).
They are also the time-critical part. The U1 set is on branches. The U4/U5 set depends on GitHub not garbage-collecting
unreferenced objects. U4 depends as well on this session's scratch repositories (`u4.git`, `probe.git`), which are not
durable.

## 3. What the U1 objects are

### 3.1 Roles

Roles were assigned from the citing lines in three steps:
1. the cue phrase nearest before the token, if one is close enough;
2. otherwise, the first line rule that matches;
3. 55 explicit overrides, each recorded in `role_basis` with its reason.

Archive self-citations are ignored. The brief's "other" is split by what the citation does.

| role | commits | blobs/trees | what the record does with it |
| --- | --- | --- | --- |
| frozen-source | 7 | 10 | takes it as input: the OI-CHANNEL-1 rule and source files; OI-PAIR-MAXCONE-1's proof bodies (`f0c36cf9`, `bbcdbab5`); OI-FINITE-PROTOCOL-1's proof body (`70815342`); OG-1's design-validated module (`40025649`); KT4-PREM-1's audited design modules (`ff9c3a35` and six blobs); OG-1's two blobs its `controls.py --self-test` reads with `git cat-file`; KINF-1's reference blob; act 35's original frozen probe |
| drafting-snapshot | 3 | 14 | the drafting revision of a preregistration, pinned by blob (14); the disposable branch that held a frozen `controls.py` before any outcome was read (3). No off-main commit is cited as a round's `D`: every `D` is on `main` |
| design-tree-r1-recorded | 2 | 0 | BG-3's design trees `6c160ad2` and `e3ef9358`, whose results R1's `bg3/results-*.json` record. These are the only off-main commits among the 98 commit ids in R1's JSON |
| other: predicted-tree | 27 | 6 | a predicted execution tree whose `delta(D, ·)`, `controls.py check`/`verdict` output and run the record states |
| other: design-run | 60 | 29 | a design or development commit, or the module blob it carried, with its run and outcome |
| other: countercontrol | 1 | 1 | a deliberately defective head whose failure is a control |
| other: outcome-blob | 0 | 10 | the expected `ROADMAP.md` blob rehearsed for an outcome the round did not reach; recomputable from `D` and the stated sentence |
| provenance-only | 7 | 5 | no computational claim rests on it: what preceded what (`a163b924`, `9430c463`, `8508d172`; chronology, for which the raw commit object is itself the evidence), the research-archive inventory (`4dc0321c`), the B4 notes link (`5f4089a4`), an advisory audit's head, act 42's research originals whose landed copies are on `main` with a stated one-line edit, and CONSC-2's build PDFs, whose bytes its control B does not freeze |

Of the 342 U1 citing locations outside the archive, 341 are in native-round records and 1 in a mutable file
(`oi_channel1_check.py:2`).

### 3.2 Holdings

- Every U1 object is held by at least one remote branch: 76 branches in all.
- 7 U1 commits are also PR heads.
- BG-2's and BG-3's four predicted trees also have local `refs/tags/archive/*` tags, dated 06:42Z. They are not on
  the remote, which is consistent with the host's 403 on tags.
- No cited object is held by `archive/r1-evidence-retention-drafting-20261016` or by any `tmp/r1-reproduce-proof-*`
  branch.
- The two OI-CHANNEL-1 commits are held only by `research/overview` and `research/round7-channel-audit`.

### 3.3 Drag (naive reachability)

**Commits.** The drag of a commit is `rev-list --count <c> --not main`, the commit itself included. For U1:
- 54 commits have drag 1, which means every parent is on `main`;
- 20 have drag 2, 12 have 3, 7 have 4, and 9 have 5–13;
- 5 have drag 26–75: `78aa5b25` 26, `e7d380fc` 27, `a163b924` 73, `9430c463` 74, `8508d172` 75.
- The union over all 107 commits is 239 commits, 132 of them uncited. With the least-drag carriers of the 75 objects
  added, it is 241 commits, 134 of them uncited.

**Commit count understates bytes.** Seven commits carry the whole `research/` tree: about 4,300–4,500 files not on
`main`, 236–238 MB uncompressed, 330+ of them `.log` files. They are `4dc0321c`, `78aa5b25`, `e7d380fc`, `5f4089a4`
and the three `research/equivalence` registrations.
- `research/archive`'s tip `4dc0321c` has drag 1 but drags 259 MB.
- **For 42 of the 75 cited blobs/trees, the least-drag carrier is that commit.** For 10 of them no other commit
  introduces the object, so the research archive is their only carrier.

### 3.4 Excerpt hazard

The test intersects the 194 excerpt blobs with `rev-list --objects <tip> --not main`.

Controls:
- Positive: `archive/r1-evidence-retention-drafting-20261016` and `tmp/r1-reproduce-proof-20261016`, `-2` and `-3`
  each yield all 194.
- Negative: `main`, `tmp/r1-reproduce-proof-20261016-4` and `-5`, and `draft/evidence-retention-r1-20261016` yield 0.
  This agrees with the owner's statement of where the excerpts live.
- Local copies: five commits hold excerpts in their trees. All are on those branches or their local copies. One
  unreferenced local commit, `38c96f9e`, descends from three of them.

Result: for every cited commit's ancestry, every cited object's carrier ancestry, every cited tree and every raw
closure or bundle measured below, the intersection is empty. The hazard is procedural, not in the cited set. It would
arise only if someone preserved by merging or bundling a branch tip, or "everything unreferenced", instead of the exact
cited ids.

## 4. Mechanisms compared

Sizes are measured in `mech/` from the U5 scratch repository. "Uncompressed" means object content bytes; "pack" means
an actual `git pack-objects` or bundle file.

### (i) A git bundle committed to `main` as a blob, with a recorded digest

- **Preserves:** commit identity, tree, and parentage within the bundle.
- **Imports into `main`:** no history, but the bundle bytes carry the entire off-main ancestry of every tip.
  - A bundle verifiable from `main` must contain everything `rev-list <tips> --not main` lists, because each
    prerequisite must already be in the reviewer's repository.
  - "Exactly the needed commits" is therefore possible only for commits whose parents are on `main`.
  - Measured: a thin bundle of `78aa5b25` alone (2,999 bytes, prerequisite `78aa5b25^`) fails `git bundle verify` in a
    main-only clone: "Repository lacks these prerequisite commits: 5d3ccb3e".
- **Sizes:**

  | bundle | file size | commits | uncompressed | other contents |
  | --- | --- | --- | --- | --- |
  | U1, complete | 35.6 MB | 241 | 280 MB | 374 `.log` files; 5,707 `research/` paths |
  | OI-CHANNEL-1 pair | 34.2 MB | 27 | 262 MB | 332 logs |
  | U1 without the seven research commits | 0.94 MB | 129 (29 uncited) | 22 MB | 43 logs |
  | BG-3's two design trees | 2,663 bytes | 2 | — | — |

  All verify in a main-only clone.
- **Reviewer verification:** needs git and history. The steps are `git bundle verify`, a fetch into a scratch clone and
  the digest check. The content is an opaque binary in the GitHub UI and in diffs.
- **Failure modes:**
  - It commits raw logs inside a blob, against §A.42 item 1, without the secret scan of item 5.
  - Every later addition rewrites a large binary.
  - It is easy to build from a branch tip by mistake, which would import excerpts or more history.
  - A check-run of the bundle proves only that the pack is well formed.
- **§A.42 fit:** reproducible from `main`, yes. "Without importing irrelevant historical commits", no, except for
  commits whose parents are on `main`.

### (ii) File contents copied into a record's `objects/` directory, with digest verification

LOC-1 proposes this form for P0/P2's frozen objects (`objects/`, blobs and research commits recorded, checked by
K-repro). It comes in three forms of increasing scope, worth separating.

**(ii-a) Bytes only.** The cited files are copied byte for byte, with sha256 and blob id recorded.
- *Preserves:* more than "bytes only". A blob id is the hash of its bytes, so committing the unmodified bytes under any
  path makes the original blob id reachable from `main`. `git cat-file -p <id>` then works in any clone, and class O
  drops the object automatically.
- *Probe:*
  - OG-1's frozen `controls.py --self-test` runs `git cat-file -p` on `e9722042` and `bf627dfe`. In a clone holding
    only `main` it crashes (rc 1).
  - After a scratch commit adds the two blobs' bytes as ordinary files, both ids resolve and the self-test prints
    `controls: OK -- 30 checks` (rc 0).
  - Nothing frozen was edited.
- *Imports:* only the cited files.
- *Size:* the 71 U1 blobs are 7.9 MB uncompressed. 3.3 MB of that is CONSC-2's four build PDFs, which are
  provenance-only.
- *Failure modes:* any normalization changes the id, whether line endings, a `.gitattributes` filter or an editor. The
  repository has no `.gitattributes`. A file name matched by `.gitignore` would be dropped silently; naming files by
  their oid avoids it. The bytes carry no binding to the commit they came from.

**(ii-b) Commit-anchored inclusion proof.**
- *What is stored:* the raw commit object, the root tree, the tree objects along each cited path, and the cited blobs.
- *Preserves:* commit identity as a verifiable hash, and the path→bytes binding inside that commit. It does not keep
  the rest of the tree or any parent.
- *The checker:* recomputes `sha1("<type> <len>\0" + content)` for every stored object, then walks commit → tree → … →
  blob. It is pure Python and works from the tree alone.
- *Sizes:*
  - `78aa5b25`'s `research/round7-channel/PREREGISTRATION.md`: 5 objects, 5,459 bytes.
  - `e7d380fc`'s `research/round7-channel/` (15 files, 3 already on `main`), `research/AUDITS/2026-10-11-round6/` and
    `research/archive/pt/R6/NOTES.md`: 26 objects, 132,849 bytes, of which 93,327 are not on `main`.
  - Neither proof contains an excerpt.
- *Failure modes:* the stored tree objects name sibling entries by name and id. The names are visible, the contents are
  not.

**(ii-c) Raw objects with reconstitution.**
- *What is stored:* the raw commit object, every tree object of its tree that `main` lacks, and every blob of its tree
  that `main` lacks.
- *Preserves:*
  - **when the commit's parents are on `main`:** the exact commit with full connectivity. A reviewer writes the objects
    with `git hash-object -w`, and the commit exists exactly as it did, so the recorded commands run unchanged.
  - **otherwise:** the commit id and the complete tree, verified. The parents are named only. `git checkout` and
    `git show <c>:<path>` work; `git log` stops at the missing parent.
- *Probe on K2-GUARD-1's predicted tree `01d97371` (parent `D` on `main`):*
  - It needs 8 objects, 24,400 bytes: the commit, 6 trees and the drafting preregistration blob. Its other blobs are
    already on `main`.
  - In a main-only clone, all 8 recomputed ids matched and `fsck --connectivity-only` passed.
  - The tree's own `controls.py` then printed `controls: OK -- 19 checks` and the verdicts
    `K2-ORIENTATION-OBSTRUCTION-PROVED` and `K1-ENTANGLING-WEAKENED`, exactly as the preregistration records.
  - Without the objects, the same check fails (`P N1 I C`).
- *Further cases:*
  - BG-3's two R1-recorded design trees need 15 objects, 32 KB. `reproduce.py`, which requires the attested commit to
    be in the repository, can then rebuild them from `main`.
  - Chain claims need only the raw commit objects of the chain, without trees, because those carry the parents and
    dates. Examples are act 19's "the chain is linear from the mandated base" and BG-2's stage 1 → stage 2.
- *Imports:* no commit enters `main`'s history; the objects are file content.
- *Proposed plan (§5), U1:* 708 objects, 18.8 MB uncompressed, 7.8 MB as zlib loose objects. Without the four PDFs it
  is 15.6 MB, or 4.6 MB as zlib.
- *Failure modes:*
  - The audit keeps reporting a retained commit under class C, because a raw commit stored as a file is not reachable.
    The audit needs a "retained-object" rule.
  - Tree objects are binary in the GitHub UI.
  - b9ef8b8e's tree holds 38 raw logs (1.6 MB), so its tree identity cannot be kept without committing those logs.
  - CONSC-2's predicted tree contains the four PDFs (3.3 MB), so its tree identity costs those bytes.

**(ii) as a whole fits §A.42 items 3, 4 and 7:**
- the archive's bytes match their hashes;
- each citing `file:line` maps to retained files;
- nothing frozen is edited;
- no history is imported.

### (iii) A separate archive repository

- **Preserves:** everything: identity, trees, full history.
- **Imports into `main`:** nothing.
- **Reviewer verification:** needs network access to a second repository. It cannot be checked from `main`'s tree;
  `main` could hold only digests or ids, which "name such content but neither retain nor establish it" (§A.42).
- **Failure modes:**
  - The host's refusal of tags and the non-durability of branches presumably apply there too; this is untested.
  - Pushing the research history publishes 374+ raw logs unscanned, unless the repository is private.
  - Its ids remain off-`main` for every audit.
- **§A.42 fit:** not on its own. It serves as a provenance mirror behind (ii).

### (iv) Merge commits making the cited commits ancestors of `main`

**Preserves:** everything, and the audit's classes C and O empty out naturally.

**What it imports, measured:**

| merged | commits | objects | uncompressed | other contents |
| --- | --- | --- | --- | --- |
| U1, complete | 241 (134 uncited) | 6,901 | 280 MB | 374 logs, 4 PDFs, 5,707 `research/` paths |
| the OI-CHANNEL-1 pair alone | 27 (24 uncited, plus `4dc0321c`) | 5,207 | 262 MB | 332 logs |
| U1 without the research commits | 129 (29 uncited) | 1,014 | 22 MB | 43 logs |

No excerpt blob is in any of these sets.

**Failure modes:**
- It is irreversible on a working draft whose history is never rewritten.
- With `-s ours`, the pull request's diff is empty, so review would have to read 241 commits.
- It merges raw logs into `main`'s history without the item-5 scan.
- It is one wrong ref away from importing the excerpts: a merge of an R1 branch tip instead of the exact ids.
- The V3 tooling's path-limited lookups (`rev-list -n 1 C -- <receipt>`) follow the TREESAME first parent and would be
  unaffected. Any tool that walks all of `main`'s commits would meet 241 foreign ones.

**§A.42 fit:** reproducible, yes. It violates the owner's "without importing irrelevant historical commits" and, for
the research commits, §A.42 items 1 and 5.

### Comparison

| mechanism | commit identity | tree | history | imports into `main` | checked from the tree alone | excerpts in the cited set | U1 size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (i) bundle | yes | yes | all off-main ancestry | 241 commits as packed bytes, 374 logs | no (needs git) | none | 35.6 MB |
| (ii-a) bytes | — (blob ids: yes) | — | no | the cited files | yes | none | 7.9 MB (blobs) |
| (ii-b) inclusion proof | yes (hash) | the cited paths | no | about 31 objects for OI-CHANNEL-1 | yes | none | 0.1 MB |
| (ii-c) raw objects | yes; exact and connected when the parents are on `main` (53) | complete | parents named | about 708 objects | yes (ids); history mode to reconstitute | none | 18.8 MB (7.8 zlib) |
| (iii) archive repository | yes | yes | yes | nothing | no | none | — |
| (iv) merges | yes | yes | yes | 241 commits into history | n/a | none | 280 MB uncompressed |

## 5. Recommendation (a proposal for the owner)

Use a mixed scheme, by class, in one evidence-retention tranche (§A.42 item 3) under
`verification/audits/evidence-retention/objects/`, with a manifest mapping each citing `file:line` to retained objects
in the R1 style.

1. **Blobs (U1: 67): (ii-a) byte copy, stored by oid.** This restores the blob ids on `main` and revives frozen controls
   that read them (OG-1, proven). CONSC-2's four build PDFs (3.3 MB, provenance only) wait on the owner (Q4).
2. **Commits whose parents are on `main` (U1: 53, including BG-3's two R1-recorded trees and 23 predicted trees):
   (ii-c) raw objects.** These reconstitute exactly, so a reviewer can rerun `controls.py check <c>` or `reproduce.py`
   as recorded (K2-GUARD-1, proven).
3. **Commits with off-main parents (U1: 45): (ii-c) raw objects of the cited commit only.** The commit id and the full
   tree are verified; the parents are named. Where a record makes a chain claim, the chain's raw commit objects are
   added. That costs about 1 KB each and no trees.
4. **`78aa5b25` and `e7d380fc`: (ii-b) inclusion proofs** of the cited paths.
   - This preserves both ids as verified anchors, so the frozen citation `oi_channel1_check.py:2` ("PREREGISTRATION.md,
     commit 78aa5b25") resolves from `main`. None of the 25 other off-main commits in their ancestry, and none of the
     238 MB research tree, is imported.
   - For R3, the rule document at `78aa5b25` is blob `b507a2c5`. It differs from `PREREGISTRATION.md` at `e7d380fc`
     (blob `89b4b73f`) by one trailing blank line.
   - The three frozen files `channel_check.py`, `native-controls.py` and `predicted-verify.yml` are already on `main`
     byte for byte; their sha256 values match.
5. **Provenance-only commits (U1: 7, including `4dc0321c` and the three research registrations): at most the raw
   commit object.** It anchors the identity. For the three "preceded" claims it also carries the parents and dates the
   claims are about. Do not copy `b9ef8b8e`'s tree, because of its 38 raw logs.
6. **Trees (U1: 4, all root trees of predicted heads): (ii-c)**, through their commits' objects.
7. **Outcome blobs (10):** copy them (1.3 MB) or record the recipe; they are recomputable from `D` plus the stated
   sentence.

Total for U1: about 708 raw objects plus 31 proof objects, about 18.9 MB uncompressed, or about 7.9 MB stored as zlib
loose objects. Without the PDFs it is about 15.7 MB / 4.7 MB.

**Why this mix.**
- It is the only option that meets all three constraints at once: reproducible from `main`, no irrelevant history,
  and no excerpts.
- It keeps commit identity, the property the frozen citations actually name, at the cost of a checker rather than
  of history.
- Its two strongest claims rest on executed probes with negative controls, not on argument.

**Checker sketch** (extending `check_retention.py`, from the tree alone):
- **R-a:** every `objects/<oid>` hashes to its oid as `<type>` (sha1 with the git header) and to its recorded sha256.
- **R-b:** every commit's tree, and every tree's entries, resolve to a stored object, or, in history mode, to an
  object reachable from `main`. Every claimed inclusion path walks to its blob.
- **R-c:** a commit marked "connected" has every parent on `main` (history mode).
- **R-d:** each citing `file:line` still holds its token in a file whose blob id is unchanged.
- **R-e:** a deny-list guard fails on any stored object whose sha256 is one of the R1 excerpt digests. The list holds
  sha256 values, not blob ids, so that it does not itself create class-O citations.
- **R-f:** a self-test mutates one byte, drops a tree, adds a deny-listed blob and adds an unlisted file, and requires
  each failure.

The audit gains one rule: a C/O id that the retained-object manifest holds and R-a/R-b verify is reported as retained,
not as off-main.

## 6. Open questions for the owner

1. **Scope.** Does R2-B cover U1 only (107/75), or every cited off-main id the survey found (U5: 202/90)?
   - The extra 95 commits and 15 objects are held by PR refs only, or by no ref at all.
   - For 81 of those commits and 14 of those objects, survival depends on GitHub keeping unreferenced objects. They are
     held now only in this session's scratch repositories.
   - Capturing them is time-sensitive. Ten cited ids are already gone from GitHub.
2. **Legacy records.** 53 of the extra citations are in legacy records (GR-1, act 19–21 and 25, SI-3, CV-2). §A.42's
   "Forward only" lets a manifest map frozen records. Should R2-B retain their objects, or record them as provenance
   or missing?
3. **The second byte-pinned citation.** `RepresentativeNaturality.lean:147` cites `52b64009`; its blob is pinned by
   acts 21–24. Is retaining the raw object of act 19's chain (4 commits, all GitHub-served) the intended treatment, as
   for `78aa5b25`?
4. **PDFs and logs.** Should CONSC-2's predicted tree keep its tree identity (3.3 MB of PDFs), or is a tree with its
   PDF entries recorded but not retained acceptable? Should `b9ef8b8e`'s logs stay out entirely?
5. **Storage form.** Uncompressed raw objects (diffable for blobs and commits, binary for trees) or zlib loose-object
   files (which drop straight into `.git/objects`)? Either way: one tranche, or one per programme?
6. **Is a raw commit object without its parents enough for the 45 drag>1 commits,** or should their full off-main
   chains also be retained as commit objects only (no trees; for U1 about 29 uncited commits, a few KB)?
7. **Ref namespaces.** Tags return 403 and branches are not durable. Would the host accept another namespace, such as
   `refs/notes/*` or `refs/archive/*`? This is untested here (no pushes). It would still not meet §A.42 by itself.
