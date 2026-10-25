BLOCK — 70faede0bc6c2318697306aa7fab82686ab58b6a (overall, a97c852a..70faede0). The block comes from commit 1 alone: its output depends on the environment it runs in.

| commit | verdict |
| --- | --- |
| 12058945cdeb94233a79afad57ceab300d22e92d (package: record-length and plan-pin checks) | **BLOCK** — `result.json` now depends on the environment |
| 96342d306af65b0efb9f76e0022f40ebb6f65aaa (review retention) | **ACCEPT WITH NITS** |
| 70faede0bc6c2318697306aa7fab82686ab58b6a (CURRENT-HANDOFF) | **ACCEPT WITH NITS** — two wording edits needed (§3) |

Overall verdict on 1dfec979721336cc9f0ce703b544f9d6be8e906c..70faede0bc6c2318697306aa7fab82686ab58b6a: **BLOCK** until the §1
fix lands. It is a few lines. Every result value is unchanged, and none is wrong.

Focused, read-only re-check; `python3 -I -B` from empty directories. No full mutant campaign was run (§A.40). What
I did run:
- the author's three targeted mutants, once in the clone and once in a git-less export;
- three replays (clone normal, clone `-O`, export normal).

Outputs are in `work/` and `leafdiff.out`.

## Changed-file inventory

| commit | files |
| --- | --- |
| 12058945 | 7 under `a2_memory_v8/`: `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, `checks.py`, `result.json`, and new `mutants/targeted_r4.py` and `mutants/targeted_r4.out` |
| 96342d30 | 53 under `a2_memory_v8/`: `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, new `review/SHA256SUMS`, `review/round1`–`round5/` (39 files) and `review/author_reruns_a97c852a/` (10 files) |
| 70faede0 | `states-dynamics-audit-20261024/CURRENT-HANDOFF.md` only |

Nothing else changed in `a97c852a..70faede0`. `PLAN.md` is byte-identical (b7f7eaae…a275). `result.json` is identical
at all three commits (sha256 d10a5c15…). The audit root's `SHA256SUMS` does not list the handoff.

## 1. Commit 1: the PLAN-pin cross-check makes `result.json` environment-dependent

`plan_pin_crosschecks()` does two things:
- it reads `PROVENANCE.json`, an in-package file, which is deterministic;
- it runs `git -C HERE show 1dfec979:./PLAN.md`.

It then writes `matches` or `unavailable` for each source into `result.json`. The committed `result.json` records
`plan_commit_blob: matches`.

**Demonstrated:**
- From the clone's worktree, normal and `-O` runs are byte-identical to `result.json`.
- From a git-less export (`git show` of each file into a plain directory, the setup these reviews use), the run
  exits 0 but writes `plan_commit_blob: unavailable`. `cmp` then fails at char 50725, so the documented replay
  breaks.
- The same happens in a tarball, an `export-ignore` archive, or a shallow CI checkout without 1dfec979 (the default
  `actions/checkout` depth is 1). Any CI replay of this package would go red.

**The control degrades silently in that setup.** The author's targeted runner, run in the export, shows it:
- T3 and MT2 are caught on their named controls.
- MT3 rescopes PLAN.md to k=1..15 and updates both pins. It is still VOID, but only because a hard-coded member count
  fails ("scope: preregistered set has 48 members"). The runner reports this as NOT CAUGHT.
- A rescoping that keeps 48 members would pass every in-package check when git is absent.

**Side effect.** The subprocess also escapes `-I` isolation. In a blobless partial clone where the blob is absent it
would fetch from the network: the side effect re-check 3 hit. Here the blob is present because it equals HEAD's
PLAN.md.

**Fix:**
- Remove `plan_pin_crosschecks` from `result.json` altogether. `result.json` must be a function of the package
  inputs only.
- Keep the PROVENANCE cross-check, which is in-package, as a plain check.
- Run the git-blob cross-check only when the plan commit is reachable. VOID on a mismatch, and print nothing to
  stdout when the blob is unavailable (a note on stderr at most).
- Better still, move it to an optional mode (`--verify-plan-commit`) or to a separate check that review and CI run
  with full history. In either form, state in REPORT that the blob check needs the full history.
- The named record-length check (T3) is fine and is caught on its label in both environments.

## 2. Commit 2: review retention

**Byte identity.** I compared the sha256 of all 39 files in `review/round1`–`round5` against my originals: all
byte-identical. That includes the renamed `REVIEW.md` → `REPORT.md` and `work/m6/*.out` → `m6_*.out`.
- `review/SHA256SUMS` verifies.
- PROVENANCE `review_retention.files` has 49 entries. Each `retained_sha256` and `original_sha256` equals the
  file's hash. Every retained file is listed; only `review/SHA256SUMS` is unlisted, which is right, since its digest
  is recorded separately and `SHA256SUMS` lists it.
- No absolute paths, scratch paths, e-mail addresses, IP addresses or tokens.

**Necessity (§A.42 item 8).**
- The reports are required: PROVENANCE and the handoff cite the reviews.
- The scripts and summary outputs are what those reports cite.

Nits:
- (a) `round2/rev_mutants.py` is byte-identical to `round1/rev_mutants.py` (cbe2d6a1…). It is redundant, so keep one
  copy and point at it.
- (b) Two reports cite per-mutant outputs that were not retained:
  - round4 cites `work/rmut5/*/run/`; its counts (45/207, 32/108, 4/25) rest there;
  - round3 cites W1a/W4 depth-shift tables from `work/rmut3/*/run2/out.json`.

  `not_retained` covers these generically ("full per-mutant JSON outputs"). Either retain the few extracted numbers
  as a small structured file, or record them as not retained but regenerable with the retained script at the named
  commit.

**`author_reruns_a97c852a`.** This passes the necessity test only while REPORT keeps its statement that the
reviewers' scripts were rerun with the stated results. The `.out` files are that statement's evidence, and the
`.py` files are the adapted copies needed to regenerate them.
- REPORT ("The reviewers' scripts were rerun on copies against this revision … Results are given with this
  revision") now sits in a revision whose `checks.py` differs from a97c852a.
- Nit (c): say "against a97c852a" explicitly. Otherwise drop the statement and the directory together.

## 3. Commit 3: the CURRENT-HANDOFF paragraph

Lines 54–67 are unchanged. Each clause of the new paragraph, against REPORT and `result.json`:

| clause | status |
| --- | --- |
| author head 12058945, reviews retained, "five rounds, two of them blocking" | factually true at 70faede0: rounds 3 and 4 blocked |
| "the last … accepts with nits, which the author head addresses and which are not yet re-reviewed" | **process narration** that goes false once reviewed (§A.27, §A.30); replace, see below |
| proves T(h)→1 for finite whole state, time-independent update, B fair fresh bits, any initial law | matches the theorem and `class_verdict` |
| the obstruction is arithmetic; holds for no-private-randomness resets (v7) and finite whole state (v8) | matches REPORT "Attribution" |
| retained-seed reset, granted the cuts, escapes with linearly growing memory | matches REPORT and v7 (bound for B≥2) |
| "Restarted every k reads (B=2,3,4, k<=16) … certified finite failure depth for every tested member" | supported: `RS_FAMILY_FINITE_FAILURE_DEPTH_EVERY_TESTED_MEMBER` under the preregistered rule; finite, correctly scoped. Keep; optionally add "(certified T>1/2 beyond a finite depth)" |
| open: bounded private memory with unbounded public state "(an unbounded clock, time-dependent updates or full-record dependence)", growing blocks, least growth | acceptable, since a time-dependent rule is a rule reading an unbounded clock; REPORT lists time-dependent updates separately, and matching REPORT's list is cleaner |
| "The class result does not cover non-dyadic fresh sources" | matches REPORT "Not covered" |
| "a memoryless fair five-valued source reproduces the quantum agreement law exactly" | **goes beyond the package**; see below |

**The five-valued clause.** The package does not make this all-depth statement. It has:
- K3: a one-state chain with agreement exactly 4/5 gives T=0, computed exactly through h=12;
- K4: the one-state base-5 chain matches (4/5)^n;
- REPORT's remark that for a fair five-valued symbol λ=4 and the argument fails.

The all-depth identity is elementary: i.i.d. Bernoulli(4/5) agreement bits are the quantum record law. But REPORT
does not state it (the earlier "removes it at once" sentence was dropped in fb05dea8), and it is a protocol-specific
sampler. Either drop the clause, or replace it with what the package shows:

> For a fair five-valued source the arithmetic argument fails (λ = 4), and a memoryless sampler that agrees on four
> of five values gives T = 0 (computed exactly through h = 12).

**Proposed timeless replacement for the review sentence:**

> `a2_memory_v8/`, author head `12058945cdeb94233a79afad57ceab300d22e92d`, has internal reviews retained under
> `a2_memory_v8/review/`.

Or, once a final accepting round is retained, add: "the last of which accepts that head". Do not record a pending
state.

## 4. Targeted mutants and replay at 70faede0

**Mutants, in the clone:** `mutants/targeted_r4.py` (TMPDIR inside the review directory) reproduces
`targeted_r4.out` byte for byte. All three are caught on their named controls:
- T3: "scope: block-law record length equals member k";
- MT2: "scope: plan pin equals PROVENANCE plan_sha256";
- MT3: "scope: plan pin equals the PLAN.md blob of 1dfec979".

**Mutants, in the git-less export:** MT3 is NOT CAUGHT on its label (§1).

**Replay:**
- From the repository path, normal and `-O` are byte-identical to `result.json`.
- From an export, the replay is not byte-identical (§1).

**Leaf diff a97c852a→12058945:**
- 2 leaves added: `plan_pin_crosschecks`, `matches` ×2.
- 1 changed: `schema` v5→v6.
- 0 removed; no value changed.

**Repo state:**
- `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py` all pass.
- The clone is clean at 70faede0, and nothing outside `a2_memory_v8/` and the handoff changed.
