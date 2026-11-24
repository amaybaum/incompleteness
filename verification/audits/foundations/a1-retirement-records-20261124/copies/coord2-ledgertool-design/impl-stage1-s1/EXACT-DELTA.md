# S1: the pre-landing corrective delta on 9da5dd5f (local only)

Writer: S1 implementation writer, 2026-11-24. Worktree `coord2-impl-wt`, branch `tools/ledger-coverage-20261123`.
Base `B0` = 9da5dd5f415654050afce40f689d55a13b66bad3 (verified HEAD and clean before work). Final commit
**443e871f225a414f69bef3f1e3cab45cb30d6594**, tree 93e612bb1e7660c4a6993da108194644b0aec326. Nine single-parent
commits, additive; no amend, rebase, force, push, PR, GitHub write or dispatch. GitHub was read only with `gh api`
GET (probe and reachability checks). Design v5.5.9 (cdfbe08c...79df9) unchanged; no normative rule changed.

Inputs read: DESIGN-v5.5.9.md (sha256 verified), PLAN.md 5339898c... sec. 1 (P1-P6) and sec. 2 step 2,
OWNER-DECISIONS-Q.md (0a71f4e3...), AGENTS.md at origin/main 8e9b8334 (sec. A.42, A.46, A.50).

## Commits (`logs/commits.txt`)

| Commit | Item |
|---|---|
| f8f13fcb5ed92c63ae85a0c403dbd1339cc60398 | P1, Q1, Q2: remove the four files; purity.py comment |
| 29ae4f809a6f049331f0df82f675190c17775161 | P2, Q3: history reader; rest fixture; S1-P2-* and S1-Q8 controls |
| fadca141dab433c45d4178cd1f4a015567aecaae | P6: `--main` required in the A1 control runner |
| 4ffbaedb2797d67a3b49d19c01337450187ba439 | README (P1, Q2, P2, P5/Q11, P6, Q8, Q10) |
| 25b82113a31b2b0880e7d4e0df0ff70a08b3c981 | re-pin class record |
| 5c1a5b1859c2c5d35d373889da48a9724f281135 | P2 follow-up: docstring wording (purity lint, register-caps); symlink control |
| 45fb957e1acf3e7c5dc7c88ee214026599175dbc | re-pin class record |
| 7b8222e05c801033c00ed3df09e3ece1167b4266 | P2 follow-up: S1-P2-SQUASH covers a path present in the root commit |
| 443e871f225a414f69bef3f1e3cab45cb30d6594 | re-pin class record (final) |

The two follow-ups: the first repro run's step 2 (staged purity lint) found `engine/host.py:140: string literal
matched by profile register-caps` (the word "GET" in my new docstring), so the run was stopped, the wording fixed and
the run restarted; the second added coverage for two mutants (S1-09, S1-11) before the mutation run. Only the final
run's logs are kept.

## Every changed file (`git diff --name-status 9da5dd5f 443e871f`, `diff.patch`)

| Status | File | Why | Item |
|---|---|---|---|
| D | `tools/ledger_coverage/authority.json` | a draft `A` landed with the tool becomes an unapproved first version that can never be repaired; it lands later, first, in its own merge | P1, Q1 |
| D | `.../freeze/freeze-ledger.json` | a ledger merged before any `A` can never be approved; it lands after `A` (sec. 15 item 0a); its draft also carried a `status` field (Q8) | P1, Q1, Q8 |
| D | `.../evidence/stage1-controls.json` | stale (written at 8c1e628a, 88/91 A1 controls, superseded engine) | P4, Q2 |
| D | `.../workflow-draft/ledger-coverage.yml` | removed from the landing (it also needs the P3 corrections before `A` pins its hash) | Q2 |
| M | `tools/ledger_coverage/engine/host.py` | `RestHost`: injectable `transport` and a `max_calls` bound; `first_parent_chain` (unfiltered commit listing of `main`, followed by first parents to the root, fail-closed on an early end or the page bound); `on_first_parent_chain` uses it (was one read per commit, limit 5000); `file_history` compares each first-parent commit's blob id of the path with its first parent's via the trees API (cached), merge commits included, checks the bytes read against the tree entry's blob id, refuses a non-regular entry; same output fields as before | P2, Q3 |
| A | `tools/ledger_coverage/adapters/rest_fixture.py` | fake rest transport over a `MemoryHost` whose path listing simplifies history as GitHub's does; `HybridHost`; the pre-correction reader as a countercontrol (`old_file_history`); `as_merge_landings` | P2 |
| M | `tools/ledger_coverage/adapters/conformance_controls.py` | group `S1-P2` (S1-P2-LISTING, -OLD, -NEW, -ADMIT, -SQUASH, -REVERT, -CHAIN, -FAILCLOSED) and S1-Q8; registered in `main` and in the must-be-reported list; module docstring | P2, Q8 |
| M | `tools/ledger_coverage/adapters/a1_controls.py` | hardcoded `MAIN` removed; `--main REV` required, resolved, exit 2 when absent or unresolvable; used by `drift_classes` and RT-L2; RT-L2's finding text names the given main | P6 |
| M | `tools/ledger_coverage/engine/purity.py` | comment only: the authority path is no longer named by the landing's class record; it lands after the tool | P1 |
| M | `.../README.md` | cites v5.5.9; `A`, the empty ledger and the acceptance workflow land later in the sec. 15 item 0a order; empty ledger = `schema` and `events` only; "Host reads" (P2); "Comments in governed threads" (guard); `--main MAIN`; "References to commits not on `main`" (Q10 narrowing); file-table rows of the removed files dropped | P1, Q2, P2, P5/Q11, P6, Q8, Q10 |
| M | `.../records/side-change-classes-v1.json` | class `tool-landing` re-pinned: 57 -> 54 pins (four removed paths out, `rest_fixture.py` in, changed blobs updated); pins == `git ls-files -s` of the landing paths less the record itself (checked); blob 6ef7c891..., sha256 416f4685...0fbf | P1 |

No path outside `tools/ledger_coverage*` and the audit directory changed. Committed text checked for model ids,
emails, local paths and "workspace": none.

Generator: `gen/gen_final_s1.py` + `gen/gen_config_s1.py` (copies of the r8 generators, parameterized). Baseline mode
on an extraction of 9da5dd5f reproduced 9da5dd5f's `authority.json` and class record byte for byte and r8's staged
configuration (sha256 83c81a65...cd79). S1 mode writes no `A` and asserts no removed path is landed.
Staged A1 configuration (outside the repository): `staging/.../retirement-config.json`, sha256
**75558ee3a32c6c3c1efa396e155d87db09e2ce3d3398ffd1da7aa8521fed7c99**; it differs from r8's only in the class-record
pin (`roles.side_change_classes` and `records[kind=side-change-classes]`: 534e96bd... -> 416f4685...).

## Q2 and AGENTS.md sec. A.50 (checked before removal)

sec. A.50 item 3 ("deleting branches, Issues, pull requests or evidence") read at origin/main 8e9b8334, with sec. A.42
items 5-6 and sec. A.46 item 6 (which govern removal of evidence *from `main`*). Determination: not a deletion of
evidence. The files were never on `main` or pushed; the removal is a new commit on an unpushed local branch, so the
originals stay reachable at 9da5dd5f (no history rewritten); and both were copied byte-identically first to
`coord2-stage1-evidence-archive/` (`evidence/stage1-controls.json`, git blob 544f8bc9622273fb04bb709161083d808957eded,
sha256 7ed1e624...2758; `workflow-draft/ledger-coverage.yml`, git blob 597fd397590e19e5b63a1009497a9fd68fa127dc,
sha256 05bd76fa...f461; `BLOBS.txt`; `MANIFEST.sha256` sha256 75239934...7197). This is the scope correction Q2
describes, not a deletion; if the owner reads it otherwise, the removal commit f8f13fcb is the one to revisit.

## P2: real-host probe (read-only, GET via `gh api`; `logs/probe/`)

Script `scripts/real_host_probe.py` runs the corrected `RestHost.file_history` against GitHub with a transport that
shells out to `gh api --method GET`, `main` pinned to 8e9b8334, path `AGENTS.md`. Deviation: the session proxy refuses
numeric-id paths (`/repositories/{id}/...`, HTTP 403), so the probe transport rewrites them to
`/repos/amaybaum/incompleteness/...`; the reader's logic is unchanged. Result (`real-host-probe.json`, call log
`real-host-probe.json.calls.json`):

- GitHub's commits-by-path listing at 8e9b8334: 133 commits; **contains 8e9b8334: false; contains 4fb2c1ee: false**;
  only one listed commit (47365b03) is on `main`'s first-parent chain.
- First-parent walk: chain of 1181 commits to the root a3e1f097; 60 versions of `AGENTS.md`; **contains 8e9b8334 and
  4fb2c1ee: true**; newest version's bytes sha256 05bbb27f...893f = local `8e9b8334:AGENTS.md` (blob 6b1280fa);
  merge records: both merged by id 7273571, merge commit = the commit.
- Local cross-check over the 145 first-parent commits the shallow local clone holds: the walk's changes equal the
  local first-parent blob comparison (11 commits), in order.
- **Cost: 1417 rest reads** (59 listing pages, 1176 trees, 60 contents, 60 + 60 pull reads), 2 for the path listing.
  The GITHUB_TOKEN rest limit is of the order of 1,000 requests per hour per repository, so one admission reading
  `A` and the ledger (shared chain and tree cache, so of the same order) would likely hit the limit and refuse
  (fail-closed, `HostUnavailable`). Exact but probably not usable under the job token as is. Not addressed here: a
  cheaper exact reader (e.g. graphql `Commit.file(path:)` batched, about chain/100 queries) needs a graphql probe
  (POST), which this task's GET-only rule excluded. The plan's step 7 host-api job measures the real budget. Owner
  decision needed before `A` pins the engine.

Regression controls (fake rest transport, A and the ledger landed by two-parent merges): the listing omits the merges
(S1-P2-LISTING); the pre-correction reader returns no version (S1-P2-OLD) and the admission refuses ERROR
CONFIG_UNREVIEWED "the authority record on main has no verified history" (S1-P2-ADMIT); the corrected reader equals
the in-memory host's first-parent history (S1-P2-NEW, -SQUASH incl. a root-commit version, -REVERT incl. revert and
deletion) and the admission passes; chain membership (S1-P2-CHAIN); fail-closed for listing end, page bound, call
bound, truncated tree, host errors, byte mismatch, symlink, and the admission (S1-P2-FAILCLOSED).

## Reproduction (`logs/repro.sh`, r7/r8 steps 1-7 adapted; outputs in `logs/full/`)

Head 443e871f; staged config 75558ee3...; `--main 8e9b8334` (= GitHub `main` at the time, read by GET).

| Step | Exit | Result |
|---|---|---|
| 1 self-test | 0 | all PASS |
| 2 staged purity lint | 0 | PASS, 0 findings |
| 3 synthetic | 0 | all PASS |
| 4 conformance | 0 | 134 PASS, 2 NOT RUN (TR5, G-A1) |
| 5 A1 conformance | 0 | 47 PASS |
| 6a A1 controls without `--main` | 2 | refused: "--main is required" (new, P6) |
| 6 A1 controls `--main 8e9b8334` | 1 | 90 PASS, RT-T NOT RUN (exit 1 as at r8); 1208 s |
| 7 release gate | 1 | failing rows identical to r8 (lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles: shallow clone / no Lean toolchain) |

`logs/controls-table.md`: **394 PASS, 3 NOT RUN (TR5, G-A1, RT-T), 0 FAIL**. Against r8 at 9da5dd5f (388): PASS there
and not PASS here: none; status changed: none; added: S1-P2-ADMIT, -CHAIN, -FAILCLOSED, -LISTING, -NEW, -OLD, -REVERT,
-SQUASH, S1-Q8. No control tested the removed files, so none was lost. Values that changed with the landing, all
expected: RT-L2 landed paths 58 -> 55 (tool-landing 57 -> 54 + class record), still no base-drift or unclassified
side change, AGENTS.md base-drift reconciled; K1-GRAPH 64 -> 61 nodes, 150 -> 82 edges (the removed `A` named every
engine blob), no cycle, countercontrols still cyclic.

## Mutation (`mut/`, harness of r8 with 11 added S1 mutants; compact)

85 mutants, 11 m 20 s. Base: 256 PASS, 2 NOT RUN, 1 FAIL (synthetic/M10, as at r8: the harness copy is not a git
repository). Killed 78 (r8: 68 of 74). Regressions (killed at r8, not now): none. r8 survivors unchanged: M07, M13,
M24, M38, M53, M58. S1-01..S1-09 and S1-11 killed (by S1-P2-*); S1-10 is an equivalent no-op mutant and survives
as intended. `mut/compare-r8.json`, `mut/mutate.stdout`, `mut/mut/results.json`.

## P5 / Q11

README documents the guard (no automated comment beginning with `oi-` in a governed thread; form comments by the
owner by hand). No admission rule changed. Separate proposal: `coord2-stage2-plan/GUARD-PROPOSAL.md` (sha256
1a1f93c0...0bc8e), a pre-write refusal in `gh_write.py` (not modified).

## P6 / Q8 / Q10

- `--main`: done (above). `a1_conformance.py` keeps its constant `M = 8e9b8334` for N10/N11, which the design and the
  controls file pin to that commit as a fixed fixture; it is not the safeguard's main, so it is not parameterized.
- Q8: every ledger the tool's fixtures and controls build is `{"schema": "oi-freeze-ledger/1", "events": [...]}` (no
  other field); S1-Q8 asserts it for the empty one; the README states it; the draft with `status` is removed. The
  engine is unchanged (it already refuses any change to a non-event field).
- Q10, every landed file citing a commit not reachable from `main` (reachability by GitHub compare GET against
  8e9b8334: T1' 14ac71b4 "diverged", P 4c79be64 "diverged"; H 53c6601a, E e837e3db, W 413b0bb8, ca3a5bb2 and
  8e9b8334 reachable):

  | File | Citation | Role | Resolution |
  |---|---|---|---|
  | `adapters/a1_controls.py` (T, P constants; ledger and edits at P; candidates at T1') | T1', P | control inputs | applied: README narrows every A1 control result to provenance until P and T1' content is on `main` (sec. A.42 item 8) |
  | `adapters/a1_conformance.py` (WB1, S11-56, N10/N11 at T1' and P's edits; blob 9f4fc3e8 = T1''s AGENTS.md) | T1', P | control inputs | applied: same narrowing |
  | `controls.json` (`control_inputs` agents-md-at-T1p; cases at T1') | T1' | preregistered control inputs | applied: same narrowing; record bytes unchanged |
  | `rules/w1-w2-allow-v1.json` (7 x `recorded_at` T1') | T1' | load-bearing: the engine reproduces each fingerprint at `recorded_at` (rules.py) | for the owner |
  | `rules/dr-deny-v1.json`, `rules/resid-v1.json` (`recorded_at` T1') | T1' | load-bearing (same mechanism) | for the owner |
  | `rules/register-infinity-params-v1.json` (`recorded_at` P; `lint.checker.commit` P) | P | load-bearing: linted against P's `edits_check.py` | for the owner |
  | `records/repo-scope-v1.json` (`source.commit` P) | P | load-bearing: scope names extracted from P's `edits_check.py` | for the owner |
  | `records/gr58-hit-classification-v1.json` (`tree` T1') | T1' | load-bearing: classification of a line at T1' | for the owner |
  | `README.md` (W1/W2 "fingerprinted at T1'", GR.md:58 "at T1'") | T1' | descriptive | applied: covered by the new section |

  The "for the owner" rows cannot be resolved inside S1 without changing a record's recorded values (which would
  change recorded results). Options: (a) land the content the records read (P's `edits_check.py`, `ledger.json`,
  `edits.json`; T1''s fingerprinted files) on `main` before the tool landing; (b) move these A1-specific records out of
  the tool landing into the A1 plan's record directory, frozen with the plan at `F` like the configuration (design
  sec. 16.2), which would change sec. 12.3's landing content and needs a design decision; (c) land them as drafts
  explicitly labelled provenance-only with a gap recorded under sec. A.42 item 8 by owner decision. Also for the
  owner: `a1_conformance.py` asserts the full blob id 86d79863821f3f8cdad86771008b2df89fd1961a, a composition computed in
  memory that exists in no repository (sec. A.42 item 3 governs ids in governed records; this is a control
  expectation in code); and `controls.json` still names design v5.1 in its header (a preregistered record, not edited).

## Not done / not authorized

TR5, G-A1, RT-T: NOT RUN (unchanged). No push, PR, CI dispatch, comment, `A` or ledger approval, merge. The P3
workflow corrections are not in S1 (the workflow left the landing). The merge-up (step 4) is not done.
