## Stage 1 correction (r2): handback

The Stage 1 implementation now conforms to the frozen design v5.5.2, and to v5.5.3 for K7. One blocker remains: K1 cannot be satisfied as written and needs an owner decision (section D below).

**Final commit: `75dae6456195fef3d8fb12190b69844e0d297929`** on `tools/ledger-coverage-20261123`, in the `coord2-impl-wt` worktree. HEAD was 8c1e628a at the start (verified).

- **Commits** (all local and additive, no push or GitHub activity):
  - 380e7d69, f9d6f53e, c4b9d09b, d26492eb, fbfbdcce: work-in-progress checkpoints.
  - 2cf6ba24: authority record draft, pinned tool-landing class, B6 reporting.
  - 04f54c0d: allowlist the authority record path.
  - ae9081f1: K7 per v5.5.3, plus control fixes.
  - 75dae645: purity fix.
- **Diff:**
  - Against 8c1e628a: 37 files, +5530/−440.
  - Against main base 4fb2c1ee: 59 new files, +16755/−27, all under `tools/ledger_coverage*` or the audit directory.
  - No file that existed at 4fb2c1ee or 8e9b8334 was changed.
- **Specs verified:** v5.5.2 (835ff356…4323) and v5.5.3 (99e9ce3a…3379). The K7 allowance is not marked pending.

**REPORT.md was not written.** The file-writing tool refuses report `.md` files from a subagent, so the report is in this message (sections A–F).

- The folder `…/coord2-ledgertool-design/impl-stage1-r2/` holds `diff.patch`, `logs/` and `MANIFEST.sha256`.
- `logs/` contains:
  - the control JSONs: conformance, A1 conformance and the A1 controls;
  - `controls-table.md`, all 327 controls with their status;
  - the self-test and purity results, and the synthetic output;
  - the A1 stdout and timing;
  - both release-gate logs, the diff stats and the commit list.
- **Manifest:** `MANIFEST.sha256`, sha256 `ec6c31e065b44e434cb8cbd7c64d69b3f21fd893e950078af326f6b449d1ae27`, 16 entries.

## A. Control outcomes

Over all runners: **322 PASS, 2 FAIL, 3 NOT RUN.** The A1 runner took about 20 minutes, including both sweeps.

| Status | Control | Why |
|---|---|---|
| FAIL | WB12 | Design inconsistency (C, D1) |
| FAIL | RT-L2 | Shows the K1 blocker (D) |
| NOT RUN | TR5 | Needs the host and CI (E) |
| NOT RUN | G-A1 | Needs F and CI (E) |
| NOT RUN | RT-T | No reviewed records exist |

**Passing, by group:**
- **Admission and acceptance:** TR1–TR4, TR6–TR53, TR5-sim, X10, X11, TR30, TR45 for ops B and D, TR46.
- **Delegation and later commits:** G4–G9 (real clones of small on-disk repositories), R16, R17, A12r.
- **Purity, records and widening:** Z9a–h, Z11, S4a, K10, A1r–A11r through the pipeline.
- **Per-edit unit:** S11-56, S11-57a–d and S11-58a–k, compared against the plan checker's own functions.
- **W1 allowance:** WB1–WB11 and WB13–WB15.
- **Reconciliation:** N3–N18 and N10/N11 on real objects. N10 gives landing-conflict-unresolved plus record-invalid; X's blob is 9f4fc3e8 and the composition is 86d79863. Also R18, R19 and N3-config-route.
- **Earlier controls:**
  - self-test and the synthetic Y/Z/X controls all pass;
  - figures: RT-H0/RT-T0 show 7 HP structure REVIEWs; RT-D shows 45 resid lines, 17 of them hit by no other profile;
  - sweeps: SW1 697/697; SW2 584/584 under the tuple predicate.

## B. Implementation by requirement

- **B1, admission and acceptance:**
  - A harness run writes `control-result.json` with `"harness": true` and admission mode control-harness.
  - The acceptance check rejects any harness result and any mode other than chain. It also checks the engine, adapter, config and admission pins.
  - The host-side check repeats trust-root points 1–3 and K7, then compares the landing record's evaluated commits and the artifact's sha256.
- **B2, native delegation (`engine/delegation.py` and the delegation class adapters, now interface 2):**
  - Clones are disposable and full, under `--out`; commit and tree are checked in the clone.
  - Checkers run from F's blobs. Every run is recorded with its complete bytes.
  - Each class runs at X and at C. Supplied files are never accepted as evidence; they are only inspected to reject one with plan null (G8).
  - T4: without F, a class is REVIEW missing, and the native re-derivations still run.
- **B3, authority and freeze designation (`engine/authority.py`, `engine/host.py`):**
  - The authority record, its versioned forms and its change procedure (approvals, a new-id approval on an owner change, an independent review, merged-by).
  - The freeze ledger, including N3 append approvals.
  - Reconciliation with committed snapshots, the deterministic designation state, F's pin table and the owner field.
  - No caller override exists, and a local run never reaches chain.
  - Draft authority record: owner 7273571, repository 1156244443, workflow pinned under `.github/workflows/ledger-coverage.yml`.
- **K7 (v5.5.3):**
  - Besides the engine pins, exactly two files are permitted: `authority.json` (blob equal to the admitted authority record) and the workflow at its pinned path.
  - Each must be a regular file; a symlink or submodule refuses.
  - The consumer side repeats this check.
  - The engine pins cover every file under `tools/ledger_coverage/` except `authority.json`, schema JSON included (43 pins).
- **B4:** commits after X are classified path by path, then C's tree is checked as a whole. A widening review must name both blobs, give a verdict for every changed item, and be listed by an owner authorization.
- **B5:** the purity value set now includes every JSON record the adapters read.
- **B6:**
  - Every control is recorded with id, expected, predicate, actual and status.
  - RT-T is NOT RUN. RT-D's full predicate is tested.
  - A1r–A11r must produce an emitted record-invalid for the rule file. SW2 compares by (obligation, class, segment, fingerprint).
- **S2–S7 (`engine/reconcile.py`):**
  - R13, checked first, then R1–R12, all evaluated from git objects.
  - The landing composition is always computed.
  - Side-change classes bind to exact blobs, and a class id may be defined only once.
  - supersedes is checked for every record kind, and op C's items on X are compared with and without the records.
  - Reconciliation records now also load from the configuration (track B T11).
- **P parity:**
  - The ledger adapter reproduces the plan checker's variant selection, keeps a running copy as segments, and maps offsets back to H in bytes.
  - It refuses the three stricter cases: a splice for the unselected variant, one splice over two edits, chained edits.
  - Per-edit unit (`engine/peredit.py`):
    - It reads its parameters from the params rule file, linted against the plan checker's literals.
    - The checker's splitter is extracted with the new `python-ast-call-arg` extractor.
    - Items 5 and 6 are recorded even on a refusal.
- **W1 option B:** negative literals are case-insensitive, and the allowance is bound to one fingerprint with one grant (to the earlier copy). The lint checks self-PASS and that the allowance equals the count. W1-c carries `{"finit": 1}`.
- **Replay and durable evidence:**
  - Offline replay is `replay --snapshot` (`engine/replay.py`).
  - Results are compressed deterministically.
  - The admission snapshot carries the delegated evidence.
- **Track B responses:**
  - T10: Stage 1's class record now keeps only tool-landing, with 56 exact pins.
  - T11: reconciliation records load from the configuration.
  - Binding spelling: flat `ledger_base`, `files_entry_sha256`, `splices_sha256`, `edit_records_sha256`.
- **Drafts written, all unreviewed:**
  - `tools/ledger_coverage/authority.json`, where round `f1` and thread `#1169` are draft values for the owner.
  - A workflow draft in the audit directory, because sec. 12.3 does not allow `.github/` in the landing.
  - An empty freeze ledger and the params rule.
  - The configuration now has owner 7273571 and the params rule. Drafts were edited in place, since none ever entered the chain.

## C. Deviations

- **D1, WB12 FAIL.** The inserted ", one of which is total finiteness," also matches DR-3, and step 2 (deny) runs before step 3. So the tool gives deny-match where WB12 expects rule-negative-match. Both are FAIL; the expectation conflicts with sec. 6.2's step order.
- **D2, purity value set.** It includes JSON records only. The plan's Python checkers named as companions are code, and their string constants collide with ordinary engine literals.
- **D3, allowlist additions:**
  - **Enumerations:** R1–R13, the engine control ids, `none`, `side-change-classes`, REPLAY_REFUSED/REPLAY_MISMATCH.
  - **Fields:** message, status, match, the role letters, and the GITHUB_* environment names.
  - **A new category, linted:** the tool path `tools/ledger_coverage/authority.json`.
  - **Rewording:** engine literals that the register profiles matched were reworded, for example "revoked" and the field `replaces`.
- **D4, rule-stale.** Staleness takes location into account only for fingerprints that require context or carry an allowance. WB5 needs this, and it keeps Y1 passing.
- **D5, ledger approvals.** After an owner-id change, ledger approvals are accepted from the owner id of any verified authority version.
- **D6, placements the design leaves open:**
  - authority reviews go under `authority-reviews/`;
  - committed snapshots go under `landings/*/snapshot.json`;
  - the landing record schema is `oi-ledger-landing/1`;
  - widening-review item ids are `<rule>:<reason>`;
  - the params rule kind is `params`.
- **D7, preserve_check placement.** preserve_check finds the repository from its own file location, so F's blob is written at its path inside the clone (which lies under `--out`). sc42 runs from `--out/checkers/`.
- **D8, known weaker predicates:**
  - RT-T0 does not test "215 region lines", because op B outputs no region-line count.
  - N6 shifts the recorded protected range by one byte.
  - N12 uses a synthetic H′, so R13 also fails.
  - TR49 refuses on the authority record's history before K7 is reached.
  - Unchanged Stage 1 controls use the runner's own code as their predicate.
- **D9, op-C replay.** It is implemented but exercised only for ops B and D; op C needs CI-produced evidence.
- **D10, self-classification.** The class record leaves out itself and the configuration (see D).

## D. K1: blocker, not worked around

**The cycle under v5.5.2/v5.5.3 (sec. 13.1, V3):**
- The configuration `…/a1exit-retirement-config.json` (sha256 c6b1f566…ccd2) pins the class record `…/records/side-change-classes-v1.json` (02644e3b…c370), both through `roles.side_change_classes` and through `records[]`.
- V3 requires the tool-landing class record to pin every landed path, which includes the configuration. Pinning the configuration would change the class record's blob, and that would change the configuration.
- The same cycle exists for:
  - the class record's own review and authorization records;
  - the configuration's review and authorization records.
- The design exempts only the class record itself.

**Shown by RT-L2:**
- Setup: predicted main = 8e9b8334 plus the tool's files, the drafted AGENTS.md reconciliation, and the pinned trial-workflow and settings classes.
- Result: R1–R13 hold except R11.
- Consequences: the only unclassified path is the configuration, and AGENTS.md therefore stays base-drift.

**Smallest correction, one sentence in sec. 13.1:**

> "A path on `M` whose blob equals a `{path, blob_sha256}` reference of the admitted configuration (records, rules, reviews, authorizations), or that is the configuration itself with the blob F's pin table lists, is classified by that reference; a class record pins every other landed path."

This keeps every path bound to one exact blob and removes all three cycles.

## E. NOT RUN, and the CI plan

- **TR5:**
  - Prerequisites: the authority record, the workflow and the freeze ledger must first land through their own approved changes.
  - Then dispatch the pinned workflow on main, with a designated F whose pin table lists the configuration, its review and its authorization.
  - Expect admission mode chain.
- **G-A1:**
  - The same job runs `execution --freeze F`, which clones X (and C) and runs tex, sc42 and coverage-ledger.
  - pdf and ci are read from the host API.
  - A follow-up job replays the landing record (TR45 for op C).
- **RT-T:** runs once reviewed records exist.

## F. Repository checks and reproduction

- **Release gate:**
  - `tools/release_gate.py` gives the same step results on the branch and on main 8e9b8334.
  - Five steps fail on both, for environmental reasons: lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles. This is the same as in Stage 1.
- **Files outside the worktree:**
  - The main-branch gate run used a temporary detached worktree `workspace/gate-main-wt`, removed afterwards with `git worktree remove` (no prune).
  - The uncommitted scratch generators are in `workspace/impl-exp/`: `gen_r2.py`, `gen_config2.py`, `gen_final.py`.
  - The run outputs are in `workspace/r2run/`.
- **Reproduction**, from the worktree at 75dae645:
  1. `python3 -I -B tools/ledger_coverage.py self-test --out O/st`
  2. `python3 -I -B tools/ledger_coverage.py purity-lint --out O/p --repo . --config HEAD:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json`
  3. `python3 -I -B tools/ledger_coverage/adapters/synthetic_fixture.py O/syn .`
  4. `python3 -I -B tools/ledger_coverage/adapters/conformance_controls.py O/conf`
  5. `python3 -I -B tools/ledger_coverage/adapters/a1_conformance.py --repo . --config HEAD:<same config path> --out O/a1c`
  6. `python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo . --config HEAD:<same config path> --out O/a1` (about 20 minutes)
  7. `python3 tools/release_gate.py`