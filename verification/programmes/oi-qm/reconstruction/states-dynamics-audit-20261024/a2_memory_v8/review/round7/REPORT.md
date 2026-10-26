ACCEPT WITH NITS — 3ca0d8ba15dac3c4c2df9df7a9b8fa931c06d74d (overall, 70faede0..3ca0d8ba)

| commit | verdict |
| --- | --- |
| 03a31cf9029582162bc82508a4eacf28e098701f (package: output independent of the environment) | **ACCEPT WITH NITS** |
| 12863de803e58d8d33ea33f20aed271bde52f68a (retention nits) | **ACCEPT WITH NITS** |
| 3ca0d8ba15dac3c4c2df9df7a9b8fa931c06d74d (handoff wording) | **ACCEPT WITH NITS** — the named author head should be 12863de8, see §4 |

Overall verdict on 1dfec979721336cc9f0ce703b544f9d6be8e906c..3ca0d8ba15dac3c4c2df9df7a9b8fa931c06d74d: **ACCEPT WITH NITS**.
- The re-check-5 block is resolved.
- No value in `result.json` changed.
- The remaining items are wording plus one git-version caveat.

Focused, read-only, targeted checks only (§A.40):
- four default replays;
- three opt-in-mode runs;
- the author's targeted runner.

Every run used `python3 -I -B` from empty directories. Outputs are in `work/`; the leaf diff is in `leafdiff.out`; the
retained-number check is `check_pmn.py`.

## Changed-file inventory

| commit | files |
| --- | --- |
| 03a31cf9 | `a2_memory_v8/`: `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, `checks.py`, `mutants/targeted_r4.py`, `mutants/targeted_r4.out`, `result.json` |
| 12863de8 | `a2_memory_v8/`: `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, `review/SHA256SUMS`, new `review/per_mutant_numbers.json`, removed `review/round2/rev_mutants.py` |
| 3ca0d8ba | `CURRENT-HANDOFF.md` only |

Nothing else changed. `PLAN.md` is byte-identical. `result.json` and `checks.py` are identical at all three commits
(result.json ac397dca…, checks.py 4f8e0361…).

## 1. The default output no longer depends on the environment (03a31cf9)

**Export.** I exported the audit subtree at 3ca0d8ba through a temporary index:
- `GIT_INDEX_FILE=<scratch>` with `read-tree`, then `checkout-index --prefix=<scratch>/`;
- the clone's index and worktree stayed untouched (`status` is empty).

Both `SHA256SUMS` files verify in the export.

**Default runs.** I made four, with a logging fake `git` first on `PATH`:

| run | result |
| --- | --- |
| clone, normal | byte-identical to `result.json` |
| clone, `-O` | byte-identical to `result.json` |
| export, normal | byte-identical to `result.json` |
| export, `-O` | byte-identical to `result.json` |

The clone and export outputs also equal each other. The fake-git log stayed empty across all four, so the default run
starts no git process. The only git calls in `checks.py` are the two in `verify_plan_commit()`.

**Leaf diff 70faede0→03a31cf9:**
- 2 leaves removed: `plan_pin_crosschecks` ×2.
- 1 changed: `schema` v6→v7.
- No other value changed.

The PROVENANCE pin check is now a plain check that VOIDs if the file is unreadable or the pin differs.

## 2. The opt-in `--verify-plan-commit` mode

| setting | result |
| --- | --- |
| clone, real git | exit 0; stdout byte-identical to `result.json`; stderr "plan commit 1dfec979: PLAN.md blob equals the pinned SHA-256"; the object store is unchanged (`count-objects` the same before and after, so nothing was fetched) |
| git-less export | exit 2, "VOID: plan commit: 1dfec979 and its PLAN.md reachable (needs full history)" |
| failing git (fake) | exit 2, the same VOID |
| no git on `PATH` | exit 2, "VOID: plan commit: git available for --verify-plan-commit" |

**Targeted mutants in the clone.** `mutants/targeted_r4.py` reproduces `targeted_r4.out` byte for byte. Each mutant is
caught on its named control:
- T3: the record-length check;
- MT2: the PROVENANCE pin check, in the default run;
- MT3: the plan-commit blob check, under the opt-in mode.

Nits:
- (a) `GIT_NO_LAZY_FETCH` exists only in git 2.44 and later. This container has git 2.43.0, where it is ignored. In a
  blobless clone that lacks the PLAN.md blob, the opt-in mode could still fetch lazily. Here the blob is present,
  because it equals HEAD's PLAN.md. Either state "git ≥ 2.44" or check the blob's presence without fetching.
- (b) REPORT says a consistent PLAN.md + pin + PROVENANCE edit "is visible against `1dfec979` and the package
  SHA256SUMS". SHA256SUMS would be edited in the same pass, so the independent anchor is the git history at
  `1dfec979`. Drop the SHA256SUMS clause.

The disclosure itself, that the default run alone does not catch such an edit when it keeps 48 members, is accurate.

## 3. Retention nits (12863de8)

**Retained numbers.** `review/per_mutant_numbers.json` matches its sources exactly (`check_pmn.py`, 0 mismatches).
- I recomputed every `source_output_sha256` from my original per-mutant outputs:
  - round3 `work/rmut3/{W1a,W4}/run2/out.json`;
  - round4 `work/rmut5/{L1,L5,L6}/run/out.json`.
- Every extracted value equals the value in those outputs. These are the depth triples for six members under
  W1a and W4, and the members/checks counts 45/207, 32/108 and 4/25.
- It covers every per-mutant number the round 3 and 4 reports cite.
- No paths or secrets.

**Duplicate removed.** `round2/rev_mutants.py` was removed. It was byte-identical (cbe2d6a1…) to the retained
`round1/rev_mutants.py`, and PROVENANCE records the deduplication. Nit (c): this deletes a file retained one commit
earlier. It happens before landing, so no retained-on-main content is lost. If the retention is taken to have begun
at 96342d30, §A.42 item 8 asks for the owner's separate authorization of the removal; record it on the PR.

**Rerun statement.** REPORT now scopes the reviewer-script reruns to `a97c852a`.

## 4. The CURRENT-HANDOFF paragraph (3ca0d8ba), clause by clause

| clause | check |
| --- | --- |
| "author head `03a31cf9…`, has internal reviews retained under `a2_memory_v8/review/`" | **not accurate as worded**, see below |
| proves T(h)→1 for finite whole state, a time-independent update, B fair fresh bits, any initial law | matches the theorem and `class_verdict` |
| the obstruction is arithmetic (dyadic against ratio 4/5) | matches REPORT "Attribution" |
| holds for no-private-randomness resets whatever their record dependence (v7), and for finite whole state (v8) | matches |
| retained-seed reset, granted the cuts, escapes with linearly growing private memory | matches |
| "Restarted every k reads (B=2,3,4, k<=16), that reset is certified to have T>1/2 beyond a finite depth for every tested member" | matches the preregistered part of `family_verdict` ("each k=1..16 certified T>1/2 beyond a finite depth (nc/(1+nc) rule)") for B = 2, 3, 4 |
| open: bounded private memory with unbounded public state (unbounded clock or full-record dependence), time-dependent updates, growing blocks, least memory growth | matches REPORT "Not covered" and "What this does not show"; "on this protocol" is carried by the earlier sentence |
| does not cover non-dyadic fresh sources | matches |
| "For a fair five-valued source the arithmetic argument fails (lambda = 4), and a memoryless sampler that agrees on four of five values gives T = 0 (computed exactly through h = 12)" | matches the REPORT remark and K3 |
| "The h=3 certificate above is unchanged." | unchanged |

There is no process narration left.

**Author head and review coverage.** The handoff names `03a31cf9` as the author head, while the retained reviews end
at `a97c852a`. As worded, this is inaccurate in two ways:
- The last commit that changes `a2_memory_v8/` is `12863de8`, which edits REPORT.md and PROVENANCE.json and adds the
  retained-numbers file. `03a31cf9` is therefore not the package head.
- The retained `review/` holds rounds 1–5, which end at `a97c852a`. Re-check 5 (of 70faede0) and this re-check
  (of 03a31cf9..3ca0d8ba) are not retained. "Has internal reviews retained" is literally true of the directory, but
  it reads as covering the named head, and none of the retained reviews covers `03a31cf9` or `12863de8`.

v7's convention is to name the reviewed package head and to retain the reviews that cover it, including the accepting
round. Fix:
- name `12863de8` (or whichever later commit is the final package head);
- retain re-check 5 and this re-check as `review/round6` and `review/round7`, with their outputs, as rounds 1–5 were.

The sentence is then accurate as is. Alternatively, add a timeless clause: "the last of which reviews `12863de8`".

## 5. Repo checks

- `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py` all pass.
- The clone is clean at 3ca0d8ba.
- Nothing outside `a2_memory_v8/` and the handoff changed in 70faede0..3ca0d8ba.
