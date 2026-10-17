# Tier 1 scratch cleanup, 2026-10-17 (owner-authorized)

**Owner decision, 2026-10-17: CLEANUP-ACCEPTED**, with two exceptions correctly kept.
- `agent-r2b/u4.git`: keep until the three repos that borrow its objects are made self-contained and verified.
- `agent-accept/host.git`: keep its 25 unique commits; a verified git bundle may be considered later.
- Tiers 2 and 3: keep. Storage cleanup is closed.


**Scope:** the 19 Tier 1 paths the owner approved, each named by absolute path. No wildcard or parent-directory
deletion. No `git gc` or pruning, no remote branch, `main` unchanged.

**Pre-checks** (read-only; `precheck.py`, output in `precheck.out`), for each target:
- processes using it, through cwd, root, exe or open files;
- kept repos borrowing its objects (alternates, followed through chains);
- worktrees of the main clone inside it;
- worktrees of its own registered outside it;
- uncommitted changes;
- refs whose objects the main clone lacks.

## Retained, because they differ from the inventory (stop rule)

| Path | Why kept |
| --- | --- |
| `agent-r2b/u4.git` | Three kept repos borrow its objects through alternates: `agent-r2b/probe.git`, `agent-offmain/work/src.git` and `shacheck/all.git`. Deleting it would break them. |
| `agent-accept/host.git` | It holds 25 refs (`refs/pullmerge/820` … `/855`) to GitHub's synthetic PR merge commits. No other kept store has them, and the host has since recomputed those merges. |

## Deleted (17 paths; `ledger.jsonl` has the time and the measured bytes of each)

| Path | Bytes | Reason |
| --- | ---: | --- |
| `agent-r2b/u1.git` | 600,572,260 | R2-B scratch bare repo; every ref object is in the main clone; nothing borrows from it |
| `agent-r2b/u2.git` | 602,102,453 | as above |
| `agent-r2b/u3.git` | 602,132,885 | as above |
| `agent-r2b/probe-k2g` | 605,574,592 | R2-B probe clone of `main` at `66a981d5`; clean |
| `agent-r2b/mech` | 370,238,546 | R2-B storage-mechanism test packs and bundles; results are in `agent-r2b/memo.md` |
| `agent-r2b/probe-og1` | 1,816,663,344 | R2-B OG-1 probe clones; see the note on its one unique commit below |
| `agent-errata-fix/clone-branch2` | 605,642,949 | #855 fixer's test clone at `b2f06c78`, which is pushed |
| `agent-errata-fix/clone-branch3` | 607,176,970 | #855 fixer's test clone at `8021c1fc`, which is pushed |
| `agent-errata-fix/clone-main2` | 605,499,352 | #855 fixer's clone of `main` |
| `agent-errata-fix/clone-sd` | 55,639,022 | #855 fixer's site-deletion clone; see the note on its README below |
| `agent-errata-fix/clone-bd` | 55,634,154 | #855 fixer's branch-deletion clone; clean |
| `agent-accept/restore.git` | 554,633,710 | Inventory validator's restore test; every ref object is in the main clone |
| `bundle/src.git` | 552,183,766 | Scratch repo used to build the R1 drafting bundle; the bundle is kept |
| `bundle/verify.git` | 552,202,271 | Scratch repo used to verify that bundle |
| `review-855b/noobj` | 605,726,919 | #855 reviewer's test clone; its edited files are identical to `8021c1fc` |
| `review-855b/shared` | 55,646,087 | as above |
| `review-855/clone` | 55,107,831 | #855 first-review clone at `0326e56b`, which is pushed |
| **Total** | **8,902,377,111** | |

## Notes on the two items with unique local content

**`agent-r2b/probe-og1`.** Its only object absent from the main clone was commit
`f7c1a1afc6fa77dad170df596af22fcd390dcf00`:
- message "scratch probe: blob bytes only (never pushed)", author `probe`, 2026-10-16 20:55Z, parent `66a981d5`;
- it adds two files, `r2b-probe/objects/bf627dfe3563fb9361e41fe7e633ea49168be95e` and
  `r2b-probe/objects/e9722042c2fc076ef292cbdb6d800a591ff71eb4`, whose contents hash to exactly those blob ids;
- both blobs are in the main clone's object store, and both are stored as raw blobs in the off-main layout
  (`agent-offmain/layout/.../objects/blob/`, listed in `agent-offmain/manifest.json`);
- the commit was referenced nowhere outside `probe-og1`.

It was disposable test material. Its `--stat` is kept in `f7c1a1af-show-stat.txt`.

**`agent-errata-fix/clone-sd`.** Its uncommitted edits were:
- `check_errata.py` and `errata.json`: identical to `8021c1fc`;
- `README.md`: an earlier draft of the same text, which `8021c1fc` only extends and rewords.

The diff is kept in `clone-sd-README-vs-8021c1fc.diff`, with the draft's sha256 in `clone-sd-README.sha256`.

## Space

| | Free bytes |
| --- | ---: |
| Before (`df-before.txt`) | 4,500,852,736 |
| After (`df-after.txt`) | 13,468,491,776 |
| Recovered | 8,967,639,040 |

## Post-checks

- Every alternates path still resolves. The kept repos that borrow objects (`probe.git`, `src.git`, `all.git`) and
  `u4.git` and `host.git` read all their refs, with 0 missing.
- The main clone has 52 registered worktrees, 0 of them prunable.
- Still present: every bundle, the zip, every manifest and the pilot record.
- Unique local work is untouched: `agent-loc1/wt` at `ccbfd9a9` and `wt-hardening-fix` at `e3a44e63`.
- Tiers 2 and 3 are untouched.
