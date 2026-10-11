# Round 5 — interruption of 2026-10-11 (08:33–10:07 UTC) and resumption

All four round-5 threads stopped mid-round. Three stopped on the session's usage limit; the fourth (origin) stopped at
the same time without a closing message, consistent with the container restart that followed. This note records the
state each thread left, the provenance check made before resuming, and how the threads were resumed. It is a
coordinator record; nothing in it changes a label.

## Timeline (UTC, from the threads' own transcripts)

| thread | round-5 start | last entry before the stop | how it stopped |
|---|---|---|---|
| `research/bridge` | 07:18:18Z | 08:34:33Z | usage-limit message ("resets 10am (UTC)") |
| `research/countermodels` | 07:18:55Z | 08:34:53Z | usage-limit message |
| `research/origin` | 07:19:34Z | 08:33:36Z (a tool result: the append to `OriginDrive.lean`) | no closing message |
| `research/equivalence` | 07:20:11Z | 08:34:15Z | usage-limit message |

The coordinator surveyed the working trees at 10:05Z and resumed each thread at 10:07Z as the same agent instance,
with its own transcript (not a fresh spawn), so each thread keeps the record of what it had done and why.

## State at the survey (10:05Z)

| thread | branch head | pushed? | dispatches used (of 3) |
|---|---|---|---|
| bridge | `b0b2378a` | yes (`origin/research/bridge` = `b0b2378a`) | 2 |
| countermodels | `23d32bc5` | yes | 2 |
| origin | `acc5fce0` | **no** — `origin/research/origin` = `6a71b2be`; one local commit unpushed | 0 |
| equivalence | `3715857c` | yes | 1 |

### Dispatches (read from `GET …/actions/runs/{id}` and `…/jobs` at 10:10Z; all completed, none cancelled)

| run | branch @ head | created | Mathlib bridge job | failing step | jobs |
|---|---|---|---|---|---|
| 38123860471 | `dev-bridge/r5-bridge` @ `36083b22` | 08:10:11Z | 114424007491, 08:10:14Z–08:13:04Z | Build | 33: 32 success, 1 failure |
| 38124442150 | `dev-bridge/r5-bridge2` @ `16e75fbe` | 08:20:16Z | 114425761656, 08:26:22Z–08:29:36Z | Release gate (Build success) | 33: 32 success, 1 failure |
| 38124380741 | `dev-countermodels/c22-compact` @ `6cb76f96` | 08:19:12Z | 114425574221, 08:19:15Z–08:22:07Z | Build | 33: 32 success, 1 failure |
| 38125067948 | `dev-countermodels/c22-compact` @ `e4ef2e46` | 08:30:53Z | 114427630399, 08:45:44Z–08:48:15Z | Build | 33: 32 success, 1 failure |
| 38124464622 | `dev-equivalence/r5-design` @ `7dd71a7e` | 08:20:37Z | 114425828153, 08:33:16Z–08:36:07Z | Build | 33: 32 success, 1 failure |

Three runs completed after their threads had stopped; the threads read them on resumption. On a research branch the
release gate is red by construction (`lean-manuscript` refuses an unregistered design module), so 38124442150's gate
failure is the expected one until its log is read; the four Build failures are design-run repairs owned by the
threads.

### Uncommitted files (sha256, mtime)

`M` modified, `??` untracked, relative to each worktree's head.

**bridge** (`/home/user/wt-research/bridge`, `research/bridge/experiments/`)

| st | sha256 (first 16) | mtime | file |
|---|---|---|---|
| M | `d17f6c111d34a665` | 08:32:37Z | `b18_reclass.out` |
| M | `8ee362947abea560` | 08:32:31Z | `b18_reclass.py` |
| M | `d17f6c111d34a665` | 08:32:37Z | `b18_reclass.replay.out` |
| ?? | `28d3b9e880a77975` | 08:09:47Z | `b18_reclass.run1.err` |
| ?? | `034bf1b2fcb3aab9` | 08:09:47Z | `b18_reclass.run1.out` |
| ?? | `d7f5e52c106944e1` | 08:08:09Z | `b18_reclass.run1.py` |
| ?? | `28d3b9e880a77975` | 08:26:44Z | `b21_torus.err` |
| ?? | `bfc68a01b8bdfd2f` | 08:26:44Z | `b21_torus.out` |
| ?? | `1692ede4f572b5c7` | 08:26:36Z | `b21_torus.py` |
| ?? | `28d3b9e880a77975` | 08:26:52Z | `b21_torus.replay.err` |
| ?? | `bfc68a01b8bdfd2f` | 08:26:52Z | `b21_torus.replay.out` |
| ?? | `28d3b9e880a77975` | 08:24:46Z | `b21_torus.run1.err` |
| ?? | `64b12c17849a4674` | 08:24:46Z | `b21_torus.run1.out` |
| ?? | `3413c00c5caa54a4` | 08:24:46Z | `b21_torus.run1.py` |
| ?? | `28d3b9e880a77975` | 08:26:36Z | `b21_torus.run2.err` |
| ?? | `64b12c17849a4674` | 08:26:36Z | `b21_torus.run2.out` |
| ?? | `ec0b7f52d58f97b7` | 08:26:36Z | `b21_torus.run2.py` |

**countermodels** (`/home/user/wt-research/countermodels`, `research/countermodels/`)

| st | sha256 (first 16) | mtime | file |
|---|---|---|---|
| M | `918a15bfe7508027` | 08:31:23Z | `LOG.md` |
| M | `5b447af0f9eeeab4` | 08:30:38Z | `lean/CmSprimeCompact.lean` |
| ?? | `b1683d44268e90be` | 08:34:52Z | `NOTES-C23.md` |
| ?? | `d24b7ea86b3d1aee` | 08:29:47Z | `lean/CmSprimeCompact.run38124380741.lean` |

**origin** (`/home/user/wt-research/origin`, `research/origin/`; and the dev worktree `/home/user/wt-research/dev-origin-drive`, branch
`dev-origin/drive` at L `9f9f8257`, never committed or pushed)

| st | sha256 (first 16) | mtime | file |
|---|---|---|---|
| M | `63409ae3a284a1fd` | 08:03:54Z | `research/origin/LOG.md` |
| ?? | `c5ef134fcac34e77` | 08:05:49Z | `research/origin/NOTES-O14.md` |
| M | `883272bf572fbe0a` | 08:20:00Z | dev: `verification/lean-mathlib/OIBridge.lean` |
| ?? | `c75f6467795bd7f1` | 08:17:16Z | dev: `verification/lean-mathlib/OIBridge/BridgeAvail.lean` |
| ?? | `b93a732e39351b93` | 08:17:16Z | dev: `verification/lean-mathlib/OIBridge/BridgeAvailFull.lean` |
| ?? | `b1beafccc966bf4e` | 08:17:16Z | dev: `verification/lean-mathlib/OIBridge/OriginAngle.lean` |
| ?? | `adaf19a2994f5f54` | 08:33:36Z | dev: `verification/lean-mathlib/OIBridge/OriginDrive.lean` |
| ?? | `bdf625995bfc6a23` | 08:17:16Z | dev: `verification/lean-mathlib/OIBridge/OriginTokenOrder.lean` |

**equivalence** (`/home/user/wt-research/equivalence`, `research/equivalence/`)

| st | sha256 (first 16) | mtime | file |
|---|---|---|---|
| ?? | `96e95bc5a024dbe5` | 08:26:43Z | `NOTES-E20.md` |
| ?? | `5743149f9217e3b1` | 08:30:53Z | `experiments/e20_odd_bodies.py` |

The full 64-hex digests are in `INTERRUPTION-MANIFEST.sha256` beside this note.

## Provenance check before resuming (§A.26)

1. **Every uncommitted file is the thread's own write.** For each file above, the thread's transcript holds the tool
   call that wrote it, at a time equal to the file's mtime to the second (bridge 08:08:09Z–08:32:37Z; countermodels
   08:29:47Z, 08:30:38Z–08:31:23Z, 08:34:52Z; origin 08:03:54Z, 08:05:49Z, 08:17:16Z–08:33:36Z; equivalence
   08:26:43Z, 08:30:53Z). No mtime is later than its thread's stop. No file in any worktree lacked a source, so no
   anomaly sweep was triggered and nothing was quarantined.
2. **Nothing was written while the threads were stopped.** No file in the four thread worktrees, the eighteen dev
   worktrees, the archive or the overview (`.git` and `.lake` excluded) has an mtime between 08:34:54Z and 10:06:30Z
   (`find -newermt`, run at 10:12Z). The five runs above were dispatched before the stop and completed on the host.
3. **Check at the round-5 audit.** Each committed version of a file listed here either has the recorded digest or
   descends from it through edits the thread logs after 10:07Z; the audit compares them.

## Resumption

Each thread received its recorded state (head, pushed or not, uncommitted files, dispatches used and their outcomes,
remaining dispatch budget), the pointer to the owner's round-5 directions at overview `51cce8ac`, an instruction to log
the interruption in its own `LOG.md`, and the commit-attribution trailers for commits made after the resumption.
Commits made before the stop keep their trailers and are not rewritten. The thread budgets are unchanged: no
dispatch was spent or refunded by the interruption.
