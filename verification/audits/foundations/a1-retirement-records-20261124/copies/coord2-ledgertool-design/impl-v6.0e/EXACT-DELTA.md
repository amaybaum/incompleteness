# v6.0e: the implementation delta on 443e871f (local only)

Writer: v6.0e implementation writer, 2026-11-24. Worktree `coord2-impl-wt`, branch `tools/ledger-coverage-20261123`.
Base 443e871f225a414f69bef3f1e3cab45cb30d6594 (verified HEAD and clean before work). Final commit
**67bae482b5842ede9e8430da841bd78563b0f97d**, tree 1689ac2e9a222a40ccc28302654e15d210ec4e6b. Eight single-parent
commits, additive; no amend, rebase, reset, force, push, pull request, GitHub write, dispatch or CI. No host read was
made (every host read has an in-memory control). Nothing was fetched, and no gc, prune, worktree prune or
merge-tree ran in the shared object store; it was read only (`git cat-file`, `git archive`, `git show`).

Inputs verified by sha256 before use: `DESIGN-v6.0e.md` 4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131,
`INVENTORY-v6.0e.md` ce3abd51df3ce12b9ee05accf4eb235869c4745556a73ca7c850db771a2720f0, `coord2-q10/DISPOSITION.md`
7ae4448024bd04256cf585b722f4b97a2a9ba3dc9b449ad40fc4865bd9345f89, `impl-stage1-s1/CORRECTION-Q10.md`
44fb8665e7f1ab3663ed0a742e713208c6688fd458e5056abbfbe24c49830c86.

Owner authorization (owner `amaybaum`, 2026-11-24, in session, relayed by the coordinating session; no comment id held
by this writer): "Adopt DESIGN-v6.0e.md, exact SHA-256: 4024a31c…5131" and "Authorize local implementation of v6.0e on
the existing tool branch. …" (quoted in full in the task).

## Commits (`logs/commits.txt`)

| Commit | Content |
|---|---|
| d62441c29915f188337daeffe2775fbeebe3d610 | the v6.0e engine, entry point and adapters (inventory 3a, 3b) |
| 4d864dbd586cedd02f03cfe01b46db34f329d535 | workflow text, `controls.json` (GV1-GV7, EI1-EI15), README (v6.0e and ESC-6) |
| 43906a2bf347998800ba34adc0e66aabc9edfb5e | re-pin the tool-landing class record |
| 0e14261cdf72b9ccb69d4e522d88001c89809737 | engine wording outside the A1 term profiles (staged purity lint findings); the `PREREG.md` allowlist entry (D-3) |
| 3da175d1e48a6ea28d80f0d23fe1c68e4f872a96 | re-pin the class record |
| 1c6dcd09618c205b3d15d08d2f20740c6ef619aa | controls test their stated reasons (mutation run 1 findings; the TR14 duplicate id) |
| ad0d83bf44a36d73e207e6eba2e39c9ece55bb31 | Z9h wired into the A1 runner (never called at 443e871f); TR3 and X11 reasons |
| 67bae482b5842ede9e8430da841bd78563b0f97d | re-pin the class record (final) |

The two follow-up groups came from this writer's own checks: the staged purity lint failed (18 findings) after the
first re-pin, and the first mutation run left mutants alive that showed weak predicates and a control reported under
one id twice (`TR14`: the consumer half's PASS masked the tool half's FAIL under mutant I01). Only the final run's
logs are the evidence; the earlier runs' mutation results are kept (`mut/run1`, `mut/run2`, `mut/run3`).

## Every changed file (`git diff --name-status -M 443e871f 67bae482`, `diff.patch`)

| Status | File | Why | Design / inventory |
|---|---|---|---|
| M | `tools/ledger_coverage.py` | isolation check before any import (exit 65), wrapper, package loaded by location, no `sys.path` insert; INTERNAL result with `class_meaning` | sec. 5 wrapper, 6.3 point 5 (EI6, N-g); 3a row 1 |
| D | `tools/ledger_coverage/engine/authority.py` | the authority record, forms, thread, freeze ledger, owner timeline removed; `read_pin_table`, `admitted_by_table` moved to `config.py` | Status "What v6.0 removes"; 3a |
| M | `engine/host.py` | only Actions runs, jobs and artifacts through REST; `head_repository_id`, `event`, `head_branch`; incomplete records refuse; GraphQL and repository reads removed; `MemoryHost` reduced | sec. 6.3 host reads; 3a |
| M | `engine/gitobj.py` | the verified reader: full ids, ids recomputed, replacement disabled, no lazy fetch, parsed parents, trees and modes, regular files only, ancestry from parsed parents | sec. 6.3 object integrity; 3a |
| M | `engine/cli.py` | parser without `--plan`, `--round`, `--config-sha256`; `admission`, `freeze_admission`, `disk_checkout`, `execution_identity`; no owner in records lint; host-run reads in `repository_id`; result annotation | sec. 6.3, 5; 3a |
| M | `engine/config.py` | `tool`, `repository_id` required and linted; `retirement` = name, issue; no owner timeline or authorization; undefined record kinds `CONFIG_INVALID`; non-regular record entries not read; pin-table reader and admitted table | sec. 16.2, 16.6, 6.3; 3a |
| M | `engine/records.py` | the authorization layer and owner parameters removed; review lint and lineage kept | sec. 6.3; 3a |
| M | `engine/checker.py` | acceptance on `/5`; consumer predicate with execution identity, `T` on `M`'s first-parent chain; `uses_line_problems`; `resolve_main` | sec. 5, 6.3 point 4-6, 13.4; 3a |
| M | `engine/replay.py` | admission re-derived from `F` against the snapshot; annotation | sec. 5; 3a |
| M | `engine/delegation.py` | host-run evidence filtered by event and repository ids, failures as missing; clones without global or system git configuration | sec. 7.2 (N-6), open item 8 (O-3); 3a |
| M | `engine/purity.py` | schema ids; `tool_paths` removed; fourth category `interface_names` | sec. 16.1; 3a; D-3 |
| M | `engine/controls_engine.py` | O-controls without authorization; O4 removed | sec. 10.2; 3a |
| D, A | `engine/schemas/oi-ledger-coverage-4.schema.json` -> `-5` | output schema `/5` with `class_meaning` | sec. 5; 3a |
| M | `engine/outcome.py`, `engine/schema.py`, `engine/selftest.py` | `/5`, `class_meaning` and its quotation; schema file name; self-test annotated | sec. 5 B-4; D-10 (beyond 3a's "retain") |
| D | `adapters/rest_fixture.py` | the host-history reader's fixture | 3b |
| M | `adapters/host_fixture.py` | reduced to `F` with a pin table, `T`, a run record and artifacts | 3b |
| M | `adapters/synthetic_fixture.py` | no authorization records or owner; `tool`, `repository_id`; simulated chain through the reduced fixture | 3b |
| M | `adapters/conformance_controls.py` | TR, GV, EI groups; retained groups without authorization; removed groups per 3b; implementation controls ADM-CONFIG-AT-F, ACCEPT-SCHEMA, CONFIG-LINT, B4-MEANING; duplicate-id check | 3b; sec. 10 |
| M | `adapters/a1_controls.py` | `k1_graph` without authorization records; CHAIN-REFUSAL also with the stand-in `F`; `rev_parse`; Z9h | 3b |
| M | `adapters/a1_conformance.py`, `adapters/staged_purity_lint.py` | package loading; WB wording "fingerprinted" (N-3) | 3b |
| M | `.../ledger-coverage-tool-20261123/README.md` | v6.0e; ESC-6 per-reference classification | 3c; sec. 15 item 11 |
| M | `.../controls.json` | GV1-GV7, EI1-EI15; header DESIGN-v6.0e | 3c; D-4 |
| M | `.../records/side-change-classes-v1.json` | re-pinned (53 pins = `git ls-files -s` of the landing paths less the record) | 3c; D-8 |
| A | `.../workflow/ledger-coverage.yml` | the workflow text `tool.workflow` pins (pre-run pin check, fetch of `F`, `uses:` by id) | 3d; D-1, D-2 |

No path outside `tools/ledger_coverage*` and the audit directory changed. Added lines checked for "workspace", local
paths, model ids, e-mail addresses and closing keywords: none. No file contains a comment form; schema ids only.

## Generators and staged configuration (outside the repository)

`gen/gen_final_v60e.py` (re-pins the class record from the working files, asserts no removed path is landed, then
calls `gen/gen_config_v60e.py`), derived from the S1 generators; `gen/gen_controls_v60e.py` (adds GV/EI rows verbatim
from the design); `gen/gen_workflow.py` (the workflow text from the readable pre-run program). Staged A1 configuration
`staging/verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json`, sha256
**5af8f07e5bf5073e5126ab3a03792f34600ae6c0354f7b8453bd6d7d221f9c6d**: no `retirement.owner`; `tool` pins every file
of the final commit's tool and `tool.workflow = {.github/workflows/ledger-coverage.yml, sha256 of the workflow text}`;
`repository_id` 1156244443; otherwise as S1's 75558ee3…7c99 (class-record and controls pins updated).

## Reproduction (`logs/repro.sh`; outputs in `logs/full/`; table `logs/controls-table.md`)

Head 67bae482 (clean); staged configuration 5af8f07e…9c6d; `--main 9deb6956` (`origin/main` in the local store, not
fetched). Run 2026-11-24, 12:49-14:09 UTC, on this container (4 cores, 15 GB).

| Step | Exit | Result | Wall time |
|---|---|---|---|
| 1 self-test | 0 | all PASS | ~1 s |
| 2 staged purity lint | 0 | PASS, 0 findings | ~1 s |
| 3 synthetic | 0 | 36 PASS | ~1 s |
| 4 conformance | 0 | 74 PASS, 2 NOT RUN (TR5, G-A1) | ~8 s |
| 5 A1 conformance | 0 | 47 PASS | ~61 s |
| 6a A1 controls without `--main` | 2 | refused: "--main is required" | <1 s |
| 6 A1 controls `--main 9deb6956` | 1 | 91 PASS, RT-T NOT RUN (exit 1 as at S1) | **4647 s** (groups: record 47, coverage 31, terms 31, v 101, rules 26, exec 162, trees 66, z9g 1, **sweeps 4182**) |
| 7 release gate | 1 | failing rows identical to S1 (lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles: shallow clone, no Lean toolchain) | |

`logs/controls-table.md`: **334 PASS, 3 NOT RUN (TR5, G-A1, RT-T), 0 FAIL**. Against S1 at 443e871f (397 controls):
PASS there and not PASS here: none; status changed: none; absent here only the ids design v6.0e retires and the
implementation ids of the removed machinery (listed in the table); added GV1-GV7, EI1-EI15 (with consumer halves),
TR14-tool, TR28-tool/-consumer, TR29-tool, ADM-CONFIG-AT-F, ACCEPT-SCHEMA, CONFIG-LINT, B4-MEANING, Z9h. RT-L2:
54 landed paths (53 tool-landing + the class record), no unbound path, `AGENTS.md` base-drift reconciled as at S1.

### Runtime and memory (owner request of 2026-11-24)

- **Total runtime** of `logs/repro.sh`: about 79 minutes (12:49:13 to about 14:08), of which the A1 control step took
  4647 s (77.5 min) and its sweeps SW1/SW2 4182 s; S1's same step took 1208 s in total. **Peak memory** of the A1
  step: 1,197,568 kB VmHWM (about 1.2 GB, `logs/full/6-peak-memory.txt`, sampled every 10 s from /proc); the other
  steps are short.
- **Are identical objects re-read and re-hashed?** No. `GitRepo._batch` caches every verified object by id in
  `_objs` for the life of the reader (with `_commits`, `_trees`, `_entries`, `_blobs` on top), so each object is
  requested and hashed once per reader instance; the A1 runner uses one reader for all its runs. Measured: reading H's
  whole tree hashes 691 objects and caches 691; 200 repeated reads hash nothing more; during the sweeps the
  reader's `git cat-file` child requested no new object over a 30 s sample. The cost is elsewhere: `GitRepo.paths()`
  builds a new `{path: blob id}` dict from the cached entries on every call (3,605 entries at H), and `blob_id()`
  calls it; the previous reader cached that dict. In a profile of the A1 coverage group (separate process,
  `logs/perf/`), `paths` took 10.7 s of 35.8 s over 46,940 calls, second only to profile matching; the sweeps, which
  re-run coverage per site, multiply it. The retained cache keeps every object read, which explains the memory.
- **CI budget.** The workflow text sets no `timeout-minutes`, so a GitHub-hosted job's default limit of 360 minutes
  applies; the design states no other limit. 79 minutes on 4 local cores fits that limit with margin; a hosted runner
  (ubuntu-24.04: 4 vCPUs, 16 GB) is of the same order, so the A1 controls should fit one job, and 1.2 GB is well within
  its memory. The sweeps are the controls sec. A.40 assigns to CI, and this run was the local evidence run requested,
  not a repeated campaign. No optimization was made (owner: correctness first). If it becomes a CI blocker, the simple
  fix that keeps the guarantees is to cache the per-commit `paths()` dict as the entries already are (both derive from
  verified, immutable objects); no integrity check would change.

## Mutation (`mut/`)

Harness `mut/scripts/mutate.py` (copy of the final tool and audit directory per mutant; self-test, synthetic and
conformance runners; a control's status compared with the unmutated base), mutants `mut/scripts/mutants.py`: 67
mutants over the new and changed code (verified reader, admission, pin table, configuration lint, execution
identity, `uses:` rule, consumer, landing, host-run filter, class meanings, entry point, allowlist, review lint).

| Run | Source commit | Killed | Survived |
|---|---|---|---|
| 1 | 3da175d1 | 38 | 29 |
| 2 (controls strengthened) | 1c6dcd09 | 59 | 8 |
| 3 (A04, C02, P01) | ad0d83bf | A04, C02 killed; P01 survives the harness and is killed by the A1 runner's Z9h (`mut/run3/P01-a1-z9.json`) | |

Final: 62 killed, 5 surviving, each equivalent or redundant: V05 (overlay ancestry shortcut: the base walk gives the
same answer), I06 (a non-regular entry at `T` is also refused by the read that follows), C08 (an extra tool file at the
consumer raises KeyError, caught as non-acceptance), C16 (an unreadable `M` cannot equal `L`'s first parent, which is
read), H03 (an empty list is also no evidence). Bounded: run 2 took 192 s (3 workers); the A1 runners (20+ minutes per
run) were not part of the mutation harness, by sec. A.40; P01 was checked against the A1 Z9 group alone.

## Not run locally (by design or environment)

TR5 (CI positive control: a run of the pinned workflow in repository 1156244443); G-A1 (native A1 classes in clones at
`X`/`C`, host-run classes from the host); RT-T (no reviewed records); TR45's op-C part (D-9); Y8 as a single CI job
running the A1 and synthetic configurations; EI14's real branch dispatch (simulated by `GITHUB_REF`); O-3's filter
driver (D-11); every real-host REST read (`RestHost` against GitHub); the CI double run of sec. 16.7. The release
gate's environment-bound rows are listed with the results.

## Records written beside this file

`IMPLEMENTATION-INVENTORY.md` (design row -> code -> control), `DISCREPANCIES.md` (D-1 to D-11, readings R-1 to R-5),
`ESC6-REVIEW.md` (the README correction mapped to the disposition; findings on `CORRECTION-Q10.md`, which is not
edited), `diff.patch`, `logs/`, `mut/`, `gen/`, `staging/`, `MANIFEST.sha256`.
