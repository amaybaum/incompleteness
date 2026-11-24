# Independent review: Stage 1 correction (r3) of the ledger coverage tool, commit 6babcea4

Reviewer: independent (not the writer, not the r2 reviewer). Read-only on the subject. All runs were in my own
detached worktrees under `review-stage1-r3/` (`wt` at 6babcea4, `wt-mut` for one mutation, `wt-75` at 75dae645
for before/after), removed at the end with `git worktree remove`. Scripts: `scripts/`; outputs: `out/`.

## 0. Inputs verified

- `DESIGN-v5.5.3.md` sha256 99e9ce3a...3379: matches.
- `review-stage1-r2/review.md` sha256 9dd390c4...2cdd: matches.
- Writer evidence `impl-stage1-r3/MANIFEST.sha256` sha256 4b61c895...: matches; `sha256sum -c` passes (44 entries).
- Staged draft configuration sha256 afeb237a...a710 (same as the writer's `staged-config.sha256`).
- Subject: 6babcea4 descends from 4fb2c1ee with no merges (3 commits after 75dae645: 075d205a, 937bc78d, 6babcea4).
- Frozen plan branch `research/a1exit-deletion-20261121` = 4c79be642ca631573f06b444903be75ec4f5e2b6, both the
  local remote-tracking ref and `git ls-remote origin`: unchanged.

## 1. Scope

- `git diff --name-status 4fb2c1ee 6babcea4`: 58 entries, all `A`, all under `tools/ledger_coverage*` or
  `verification/audits/foundations/ledger-coverage-tool-20261123/`. 16,544 insertions, 0 deletions. No
  pre-existing file is modified.
- Added lines contain no `<tmp>/`, `/home/`, `workspace`, e-mail address, `noreply` or model id (grep, empty).
- `authority.json`: only pin values changed since 75dae645. 44 engine pins equal the 45 tool files minus
  `authority.json`, every hash matching. The workflow draft hashes to `A.workflow.content_sha256` (05bd76fa...).
- The configuration is not in the landing: `6babcea4:verification/audits/foundations/a1exit-deletion-20261121/
  retirement-config.json` does not exist, and the old `ledger-coverage-tool-20261123/a1exit-retirement-config.json`
  is deleted relative to 75dae645.

## 2. Reproduction (writer's steps 1-7, my run: `scripts/repro.sh`, `out/repro/`)

| Step | My outcome | Same as writer? |
|---|---|---|
| 1 self-test | 87/87 PASS, exit 0 | yes |
| 2 staged purity lint | PASS, 0 findings, exit 0 | yes |
| 3 synthetic fixture | 36/36 PASS, exit 0 (the missing-dir crash of r2 is fixed) | yes |
| 4 conformance | 68 PASS, 2 NOT RUN (TR5, G-A1), exit 0 | yes, control by control |
| 5 A1 conformance | 47 PASS, exit 0 | yes |
| 6 A1 controls (about 20 min) | 90 PASS, 1 NOT RUN (RT-T); exit 1 | yes, control by control |
| 7 release gate | 5 FAIL: lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles; every other step PASS | same step results as the writer and r2 |

Totals: **328 PASS, 0 FAIL, 3 NOT RUN** (TR5, G-A1, RT-T), reproduced. Notes:

- Step 6 exits 1 only because `a1_controls.main` treats RT-T (`passed: False`, status NOT RUN) as failed. Its
  status field is NOT RUN. NON-BLOCKING (N4).
- Step 7's five failures are the shallow-repository and missing-Lean-toolchain conditions already seen in r2. The
  diff adds files only under the two tool prefixes. I did not rerun the gate on `main`.

Comparison with the r2 control set (`out/control-comparison.txt`): no control removed; none went from PASS to
non-PASS. Added: R3-F1, R3-F2, R3-F3, K1-GRAPH. Changed: WB12 FAIL to PASS, RT-L2 FAIL to PASS, and RT-DR, RT-I7,
RT-I7A, V3-countercontrol now carry status and predicate. Predicate or expected text changed only for WB12,
RT-T0 (adds 215), RT-L2 (stronger, below), RT-T (placeholder predicate) and the four records given predicates.

## 3. The seven confirmations

### 1. F1, owner transitions: NOT CONFIRMED (BLOCKING finding B1)

`engine/authority.py:159-177` `in_force`: the A in force for a ledger change is the latest verified A merged
strictly before it on the first-parent chain. A merged in the same commit governs only when nothing earlier
exists. My probes ran on the simulated host: `scripts/f1_probe.py`, `out/f1.txt`, and the same probes at 75dae645
in `out/f1-at-75dae645.txt`. Every case ran in both comment forms.

| Case | 6babcea4 | 75dae645 |
|---|---|---|
| P1 owner change 4242->5555 in the same commit as a ledger change, approved by 4242 | passes the ledger history | passes |
| P2 same, approved only by 5555 | refused | passes |
| P3 4242->5555->4242, ledger change in between approved by 4242 | refused | **accepted** |
| P4 same, approved by 5555 | accepted | accepted |
| P5 after the change-back, approved by 5555 | refused | **accepted** |
| P6 after the change-back, approved by 4242 | accepted | accepted |
| P7 5555 approves a ledger change merged before the owner change | refused | passes |
| P8 approval created after a recorded PR merge | refused | refused |
| P11 A and the empty ledger landing together | accepted | accepted |
| P12 same, ledger approved by 31337 | refused | refused |

So former owners lose authority, and approvals by the then-current owner stay valid. The same-commit case is
decided unambiguously: the outgoing owner, who is in force until that merge, approves. The new owner has
co-approved the A change in the same merge. This follows the r2 fix wording, "latest verified A merged before it".

**B1 (BLOCKING): an approval is not bound to one ledger change, so it can be replayed.** `find_approval` matches
only on author, form and `from`/`to` hashes, with creation before the merge. Nothing makes an approval comment
single-use, and nothing checks that a new ledger version extends the previous one (append-only).
`scripts/f1_replay.py`, `out/f1_replay.txt`:

- **R1.** A (4242) approves L0->L1, which merges. Then A->B, B approves the revert L1->L0, and B->A. A new change
  L0->L1 merges with **no new approval**. Result: **ACCEPTED, exit 0**. A's comment from before the first owner
  change authorizes a new ledger change merged after the change-back. This is the case the coordinator asked
  about.
- **R2.** The same with no owner change: L0->L1, L1->L0, then L0->L1 again with no approval. **ACCEPTED, exit 0.**
- **R3.** A different change L1->L2 with no approval is refused, so the replay needs matching hashes.

Both comment forms give these results. Both behaviours are pre-existing (identical at 75dae645).

- **Requirement violated.** Sec. 6.3, "The freeze ledger": the ledger is "an append-only list"; "No append takes
  effect ... without its own explicit owner approval comment"; and the approval must be "created before the merge
  that lands the append" (TR47).
- **Fix.**
  - Refuse a ledger version whose events are not a strict extension of the previous version's.
  - Refuse any approval comment id already consumed by an earlier ledger or authority change.
  - Add R1 and R2 as controls.

**B2 (BLOCKING, small): with no merge record, the approval-time check is skipped.**
- **Counterexample.** P9 in `out/f1.txt`: a ledger change pushed directly, with no pull request, has
  `merged_at = None`. An approval by the then-current owner created **after** the push is accepted (exit 0), in
  both forms.
- **Code path.** For the ledger kind, `verify_history` never requires a merge record, while the authority kind
  does (`merged_by_id`). `RestHost.file_history` gives `merged_at: None` for any commit with no merged PR
  (`host.py:233-237`), so the same path exists on the real host. That last point comes from reading the code and
  was not executed against GitHub.
- **Requirement violated.** Sec. 6.3: "be created before the merge that lands the append"; "Every change lands
  through the authority-change procedure", whose merge "is a pull request into main".
- **Pre-existing:** identical at 75dae645.
- **Fix.** Refuse a ledger change with no merge record (`merged_at` None), as the authority kind does.

Status: tested by me on the simulated host. Real-host behaviour (TR5) is NOT RUN.

### 2. F2, records consumed in op C: NOT CONFIRMED (BLOCKING finding B3)

`cli.py:1016-1039` now runs `lint_chain` over every configuration-referenced `side-change-classes` and
`reconciliation` record. A record that fails is `record-invalid` and is not used. `--classify` records go through
`RecordSet.admit`, which also lints. `scripts/f2_probe.py`, `out/f2.txt`, with 75dae645 in
`out/f2-at-75dae645.txt`:

| Case | 6babcea4 | 75dae645 |
|---|---|---|
| C0 reviewed and authorized | classified, exit 10 | classified |
| C1 reviewer = author | record-invalid, unclassified, exit 20 | classified |
| C2 verdict `reject` | record-invalid | classified |
| C3 verdict for the record id only, not for class `notes` | record-invalid | classified |
| C4 authorization names another review blob | record-invalid | classified |
| C5 authorization owner differs | record-invalid | classified |
| C6 / C7 review / authorization not referenced by the configuration | record-invalid | classified |
| C10 unreviewed record also given with `--classify` | record-invalid, unclassified | classified |
| **C9** one class with `id` `notes`, a second class with no `id`; one verdict, on `record_id` | **classified, exit 10, no record-invalid** | classified |
| C8 every class without `id` | uncaught `KeyError: 'id'` in `reconcile.classify_side` | same |

**B3 (BLOCKING, small): the per-item verdict requirement can be bypassed.**
- **Cause.** `records.item_ids` falls back to `record_id` whenever any entry of `classes` lacks `id`
  (`records.py:16-26`).
- **Effect.** A single verdict on the record id then validates the record, and the class `notes`, which has an
  id, classifies the side change without its own verdict. A class with a missing `id` is also not refused as a
  field error.
- **Requirement violated.** Sec. 6.3: verdicts "one entry per item id of the reviewed record", and record-invalid
  on "a schema or field error, or a missing field". This is exactly the "per-item accept verdicts" of the owner's
  confirmation.
- **Pre-existing**, and not introduced by the `item_ids` change. That change only replaced the final `['*']` with
  `[]`, which tightens it.
- **Fix.** When a list key is present and non-empty, `item_ids` must return its ids only if every entry carries
  the id field, and otherwise yield no ids, which is record-invalid. The same applies to `rules`, `sites`,
  `entries` and `classifications`. C8's KeyError then disappears as well.

**Other record kinds in op C.**
- Reconciliation records share the lint path. The A1 control RT-L2 shows the harness route.
- The ledger and edit list are adapter inputs pinned by blob in the configuration.
- The delegation contract is read via `cfg['delegation']` with no chain lint. Sec. 6.3's list of kinds does not
  name it, and it is pinned by the reviewed configuration. NON-BLOCKING, carried from r2 (N5).

### 3. F3, consumer check: CONFIRMED

`checker.py:81-86` reads `authority.json` at `head_sha` and requires it present and sha256-equal to
`pins['authority_blob_sha256']` (a `None` pin also refuses). My `scripts/consumer_bind.py`
(`out/consumer_bind.txt`): absent gives False, different gives False, present and equal gives True. Simulated
host only.

### 4. F5, RT-T0: CONFIRMED

- **My run.** RT-T0 PASS with `region_lines = {count: 215, segment: 53c6601a..14ac71b4}`, and every other count
  as designed.
- **Definition.** `segments.py:191-203` gives `[first, last]` as the T1' lines of the replacement image of the
  region. That region is the LF-inclusive site span united with its overlapping splices, mapped from H. Removed
  sites contribute none. This matches sec. 14, "215 region lines with the LF-inclusive site span of sec. 5 (203
  without the LF)", and sec. 0.3 D4.
- **Mutation** (`wt-mut`, `range(first, last)`, which drops each region's last line, run with `--only coverage`;
  `out/f5-mutation.*`): count 18, and **RT-T0 FAIL**. The control tests the count.

### 5. WB12: CONFIRMED

- The profile set is item7 less DR-3: `ptr,count-grep,resid,DR-1,DR-4,DR-5`. That is V7a: V2's set without
  DR-3.
- Result: exit 20; the line has `rule-negative-match` of W1-c and no `deny-match`. PASS.
- `engine/rules.py` and `engine/profiles.py` are unchanged since 75dae645 (empty diff). `apply_allow` still
  returns `deny-match` before the negative matcher.

### 6. F4 / K1: CONFIRMED

- **RT-L2 PASS** at the predicted main (8e9b8334 plus the tool landing):
  - all 58 landed paths are bound to exact blobs: 57 `tool-landing` and 1 `class-record`, with `landed_unbound`
    empty;
  - **without** the reconciliation record, MAIN shows `base-drift AGENTS.md`, exit 20: the drift is not
    suppressed;
  - with the record, `AGENTS.md` is `base-drift`, reconciled, and no MAIN item remains;
  - with the landing composed, exit 10 and no MAIN items;
  - chain admission of the staged draft refuses with `CONFIG_UNREVIEWED`.
- **Own check of the pins.** The class record pins all 57 landed paths other than itself; sha256 and `git_blob`
  both match at 6babcea4, and no extra pins exist. The draft configuration pins the class record's blob
  (cd231be2...), and the class record does not mention the configuration.
- **K1-GRAPH PASS.**
  - The actual layout is acyclic. The configuration, its review, its authorization and the class record's review
    and authorization are placed in the plan directory, and F's pin table points to the configuration and its
    review and authorization.
  - Countercontrol 1 (configuration landed) gives the cycle config -> class auth -> class review -> class record
    -> config.
  - Countercontrol 2 (the class record's review landed) gives a cycle.
- **Self-authentication.** The configuration is admitted only from F's pin table plus `A`.
  - CHAIN-REFUSAL: with no `--freeze`, `CONFIG_UNREVIEWED`.
  - The staged draft carries `notes: "UNREVIEWED AND UNAUTHORIZED DRAFT, NOT ADMITTED..."` and only three
    record references (scope, class record, GR-58), with no review or authorization records. It cannot be
    admitted as-is.
- The plan branch is unchanged (sec. 0).

### 7. Nothing weakened: CONFIRMED

- **Engine diff from 75dae645**, every hunk read:
  - `authority.py`: an exact in-force owner replaces the any-verified-owner set, which tightens it;
  - `checker.py`: an added A-at-head check;
  - `cli.py`: the lint is extended to class records, and `region_lines` is output;
  - `pipeline.py`: region-line bookkeeping only;
  - `records.py`: `item_ids` gives `[]` instead of `['*']`, and records with no ids are record-invalid.
  - No check was removed or loosened.
- **Records with ids.** Every reviewable record in the landing still has item ids: rules, class, scope, GR-58
  and delegation draft. The reconciliation draft carries `record_id`.
- **Pins.** The regenerated pins were checked in sec. 1.
- **Controls.** The control-by-control comparison is in sec. 2.

## 4. GITHUB_API_URL (coordinator point 2): NON-BLOCKING (deferred improvement)

- **The route into the tool.** `RestHost.detect` (`host.py:145-149`) takes the API base from the environment. A
  local caller who sets `GITHUB_ACTIONS`, `GITHUB_RUN_ID`, `GITHUB_TOKEN` and `GITHUB_API_URL` can point the
  tool's own admission at a fake host. It then writes a `result.json` with `admission.mode = "chain"` and forged
  designation and identity data. `native_env` (`cli.py:985`) likewise enables the native clone path.
- **What that forged result does not get past.** It does not reach acceptance, because:
  - the consumer predicate `checker.accept_with_host` reads nothing from the environment and takes the consumer's
    own host;
  - it requires a real run id in the pinned repository, not a fork, with the pinned workflow, a `head_sha` on
    `main` carrying the pinned blobs and `A`, admission pins equal to the consumer's own, and the run's uploaded
    artifact hash equal to `landing.result_sha256`.
- **A partial gap I found in the predicate.** `accept_with_host` does not hash the result it is given. It compares
  the artifact hash only with `landing.result_sha256`.
  - In `scripts/consumer_bind.py`, a forged document (`items` emptied, `covered_paths` changed) is **accepted**
    when the landing record quotes the genuine artifact's hash.
  - Sec. 5's landing check closes this in composition: "the sha256 of the uncompressed bytes decides" (TR46,
    `verify_compressed`), so a committed result whose bytes differ from the quoted hash fails there.
  - No landing check exists in this landing to wire the two together; that is NOT RUN (it needs CI).
- **Recommendations** (NON-BLOCKING, N1 and N2):
  - pin the API base, or take it from `A`;
  - have `accept_with_host` take the result's raw bytes and require
    `sha256(raw) == artifact == landing.result_sha256`.
- **What a landing records.** The snapshot written by a forged-host run would carry forged identity. It is
  accepted only through the predicate above, so it cannot land as accepted.
- **Conclusion.** No demonstrated route to acceptance.

## 5. NON-BLOCKING

- N1, N2: sec. 4.
- N3: the README inserts its new paragraph in the middle of the files table (README lines 28-33). The two rows
  after it (`freeze/freeze-ledger.json`, `workflow-draft/...`) lose the table header.
- N4: `a1_controls.py` exits 1 when the only non-PASS control is NOT RUN (RT-T). Its JSON status is correct. RT-T
  also gets the placeholder predicate "the boolean computed for this id...".
- N5: the delegation contract is not chain-linted (carried from r2).
- N6: C8, a class with no `id`, raises an uncaught `KeyError` instead of `record-invalid`. The fix for B3 removes
  it.
- N7 (§A.42 / §A.46 pre-landing note): the A1 controls, and the README's run instructions, need the staged draft,
  which exists only outside the repository. Before the tool lands, either put the draft on a reachable research
  branch or plan, or state that the A1 control evidence is not reproducible from `main`.

## 6. Control status

- **Tested by me** on real git objects:
  - all of steps 1-7;
  - the RT-T0 mutation.
- **Simulated only**, on the in-memory host:
  - TR1-TR53, X11, R3-F1, R3-F2, R3-F3;
  - my probes P1-P12, R1-R3, C0-C10 and consumer_bind.
- **NOT RUN** (they need GitHub or CI, or reviewed records):
  - TR5, G-A1, RT-T;
  - the landing check and acceptance composition;
  - B2 on the real host.

## 7. Verdict

**REJECT.** The five r2 findings are fixed as specified, and all 328 controls reproduce. But three demonstrated,
reproducible counterexamples violate sec. 6.3:

- **B1:** a ledger approval can be replayed for a new ledger change, including across an owner change and
  change-back (R1, R2), and append-only is not enforced;
- **B2:** with no merge record, an approval created after the push is accepted (P9);
- **B3:** one record-level verdict can stand in for per-item verdicts on a side-change class record (C9).

All three are pre-existing: they are present at 75dae645 and were missed by both earlier reviews. Each fix is
local: a single-use, append-only check in `verify_history`, `merged_at` required for ledger changes, and strict
`item_ids`.

Counts: 3 BLOCKING (B1, B2, B3), 0 DESIGN-ISSUE, 7 NON-BLOCKING (N1-N7).
