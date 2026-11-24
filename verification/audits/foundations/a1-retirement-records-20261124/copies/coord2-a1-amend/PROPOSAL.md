# A1 plan amendment proposal: the ESC-1 to ESC-4 evidence gaps, the dependency on P, and items P1 to P5 and P8

## 0. Status

**Provisional.** This proposal depends on the reduced tool design. That design, v6.0c, is a draft still under
review, and its implementation does not exist yet. The proposal stays provisional until the final tool design is
adopted and its implementation verified. Every statement below about engine behaviour was read from the S1
implementation (`443e871f`), which predates v6.0c, and has to be re-checked against the final implementation.

**Paper-only.** No repository file was changed. Nothing was committed, pushed, opened, dispatched, commented on or
merged. The frozen plan `P` and every trial record were only read, never written. This proposal does not amend, freeze
or re-freeze the plan. It runs no trial, changes no premise and authorizes nothing (§A.45 rule 3; §A.50 items 1, 2, 5
and 6). Adopting any part of it needs the owner's per-time approval under §A.50 item 2.

**Owner instruction** (owner `amaybaum`, 2026-11-24, in session; not yet recorded on GitHub), quoted: "Authorize a
writer to prepare a bounded amendment proposal covering: ESC-1–ESC-4 [...]; The wider dependency on P [...]; P1–P5 and
P8 [...]; Identify any consequences for the frozen plan, trial procedures and acceptance criteria. Provide an exact
proposed change inventory and obtain independent review. Prefer preserving existing scientific values, edits and
evidence rather than regenerating them unnecessarily. Keep the frozen plan and original trial evidence unchanged. The
proposal must remain provisional until the final tool design is adopted and its implementation verified. No plan
amendment, re-freeze, trial execution, premise change or merge is authorized." And: "The priority is completing A1
retirement, not expanding its scope or building additional infrastructure."

**Goal link (§A.47).** A1-EXIT (#1169), the exception-free verification route of #1169 c.7093128173. This proposal
decides nothing on its own. It prepares the exact changes the owner would need to approve so that the plan's checks can
run through the tool at a new freeze `F`, with every record they read supported from `main`.

**Independent review.** Not yet obtained. This writer cannot review its own work, and no reviewer was available in
this run. §9 lists what the review must check.

### Inputs (each verified before use)

| Input | Identity |
|---|---|
| Q10 disposition `DISPOSITION.md` | sha256 `7ae4448024bd04256cf585b722f4b97a2a9ba3dc9b449ad40fc4865bd9345f89` |
| Q10 owner decision record `OWNER-DECISION-20261124.md` | sha256 `39521663157964a9e227b952a32bb6cd9efed96202c647a6da5fa535754b423b` |
| Tool design `DESIGN-v6.0c.md` (draft, under review) | sha256 `dd72ee5b9f1ed3718b5f1584bf88b957dbb481b0c9ac9dca3d6ff784389aa594` |
| `INVENTORY-v6.0c.md` (table 6: P1–P8) | sha256 `86cbe962381a3a25fdaba9387cbf37922fa51d0e892ed075bff2cb76a4eb914c` |
| Staged A1 configuration draft `retirement-config.json` | sha256 `75558ee3a32c6c3c1efa396e155d87db09e2ce3d3398ffd1da7aa8521fed7c99` |
| S1 tool implementation | commit `443e871f225a414f69bef3f1e3cab45cb30d6594` (clean) |
| Frozen plan `P` | `4c79be642ca631573f06b444903be75ec4f5e2b6`; `PREREG.md` blob `6931e3be…`, sha256 `bc05340f5974f5990a7c863100a82b8446009c2c9f000e7610decc2fce6fe928` |
| `H` | `53c6601a10419b6b333cc992474272501ab542af` (on `main`) |
| T1′ | `14ac71b4b0a0c0aa2d7068d6799a73f474097060` (not on `main`) |
| `main` | `9deb69568d8231210c7f39cb65be943dea566371` (re-read by REST GET on 2026-11-24, unchanged) |
| `AGENTS.md` at `main` | sha256 `43a28e2653843e8a8ba87e38778cacd6815b71ee54d7977af945303d1783ce27` |
| #1169 c.7093128173 | `amaybaum`, 2026-11-23T06:13:50Z, never edited (REST GET); the four passages quoted in the proposed §32 match its body |
| Stage 2 owner decisions Q1–Q14 (`OWNER-DECISIONS-Q.md`) | sha256 `0a71f4e3845dbc175b258c90e3fc603d9482aedea9dbdd6bc900b378d9e550d6` |

## 1. Summary

| Item | Recommendation | Recorded values changed |
|---|---|---|
| ESC-1 `w1-w2-allow-v1` | A superseding file `w1-w2-allow-v2.json` in the plan's record directory. It moves `recorded_at` from T1′ to `H` and changes nothing else. All 11 fingerprints lint at `H` (§2). | none (only `recorded_at`) |
| ESC-2 `register-infinity-params-v1` | No record change. The configuration reads the checker companion at `F`, where it is the same blob as at `P`. The gap closes when `F`, and with it `P`, become reachable from `main`. | none |
| ESC-3 `repo-scope-v1` | No record change. The record's reviewer checks it against `edits_check.py` at `F`, the same blob as at `P`. The gap closes when `F` and `P` become reachable. | none |
| ESC-4 `gr58-hit-classification-v1` | No record change. The reviewer re-derives the line from `H` plus `ledger.json` splices D040 and D041. That rebuild is byte-identical to T1′'s `papers/GR.md` (§2), so the support is on `main` once `F` is reachable. | none |
| The dependency on `P` | Every `P` artifact is read at `F`, from the unchanged plan directory. Before `F`, the plan branch takes in a `main` that holds `T`. After `F` is designated and before the execution landing `L`, the plan's pull request is merged by a merge commit, which makes `F` and `P` reachable. | none |
| P1–P5, P8 | One appended section, PREREG §32 (`diffs/PREREG-append-s32.diff`), and the field changes to the staged configuration in `diffs/CONFIG-staged-draft-to-proposed.diff` | none |

The ledger (399 splices), the edit list (401 records), the checkers, the fixture, `H`, every scientific value, every
fingerprint, every matcher and every classification stay as they are.

## 2. Facts established for this proposal (read-only; nothing in the repository was written)

| # | Check | Result |
|---|---|---|
| V1 | The 11 W1/W2 fingerprints, recomputed with the S1 engine's splitter (version 2, the staged abbreviations) at T1′, `H` and `main` (`work/fpcheck.py`) | At T1′ all 11 reproduce with sentence and context. At `H` and at `main`, 9 reproduce with sentence and context. W1-d's two (`ch19-open-problems.md`, `FULL.md`) reproduce the sentence only. This matches the disposition. |
| V2 | The S1 `rules.lint_rule` on all six allow rules, with `recorded_at` set to T1′ (control), to `H` and to `main`. Profiles were built from the staged configuration, and every `pattern_sha256` was confirmed (`work/lintcheck.py`). | 0 problems in each case |
| V3 | Design D1 self-pass for W1-d at `H` with `H`'s own neighbours (the S1 lint skips this when the context differs) | `pass` for both fingerprints. W1-d has `context_required: false`, no `negative_allowance`, and a context literal ("of the bijection") that lies inside the sentence. |
| V4 | S1 `rules.file_widening`: v1 against the proposed v2 | `[]`, so no widening. As a first file, v1 itself has 6 items ("new allow rule without supersedes"), so its widening review is needed in any case. |
| V5 | `H` plus `P`'s `ledger.json` splices, rebuilt and compared with T1′ (`work/recon.py`) | Equal for `papers/GR.md` (blob `c4a320e2…`), `papers/SM.md` (`c358068f…`), `book/ch09-universality.md` (`289d1710…`), `book/ch19-open-problems.md` (`f2c14959…`) and `FULL.md` (`c9313316…`). `appendix-b-derivations.md` has 0 splices (`f91b596d…`). `GR.md:58` is `H` line 58 with splices D040 and D041. |
| V6 | How the S1 engine reads records (`config.py:29-36`, `:185-230`; `records.py:160-310`) | A reference without a `commit` is read at `F`. A `supersedes` predecessor is resolved from `F`'s tree and must pass the chain lint, which needs its own review record. The ambiguous-ancestry scan covers the configuration's directory and the referenced records' directories at `F`. So `F`'s tree must contain the tool's audit directory. |
| V7 | `P`'s `preserve_check.py` (`read_pins`, `verify_pins`, `compare`) | It reads the last `Record pins` subsection and checks only its six `PINNED` files. Its row pattern `[\w.]+` skips hyphenated names. The candidate's record directory must equal the plan's, apart from `execution/`. Any new file in the plan directory therefore enters T0″, T1″ and `X`. |
| V8 | The proposed `PREREG.md` (P plus §32) | Its last `Record pins` heading is `### 32.9`. `preserve_check`'s pattern finds 6 rows and the S1 tool's finds 6, before the placeholders are filled. `tools/duplicate_check.py` (from `main`) reports OK. |
| V9 | REST GET | Repository id 1156244443, not a fork. `main` = `9deb6956`. `P` compared with `main`: diverged, merge base `1c7eedc4`. |
| V10 | `git diff --name-only 1c7eedc4 P` | Only the 7 files of the plan directory. |
| V11 | The S1 landing check (`execution.py:365-410`) | A path that `M` and `C` both change to the same blob must equal it in `L`. `main_role` requires every path changed between `H` and `M` to be classified as a side change. |
| V12 | The `H`-based sources of the configuration (`sitemap.json`, `rows.json`, `sites.json`, `ledger_check.py`) | The blobs at `main` equal those at `H`. |

## 3. ESC-1 to ESC-4

Common rule (owner, Q10): no option lands `P` or T1′ just to satisfy a citation, and no option changes a recorded
scientific value.

### ESC-1: `rules/w1-w2-allow-v1.json` (the engine reads T1′ by commit id)

| Option | What it preserves | New review | What it affects |
|---|---|---|---|
| **(b1) v2 at `H`, superseding v1 (recommended)** | Every rule, matcher, example and fingerprint value, the record id `a1-allow-w1-w2-v1` and the rule ids. Only `recorded_at` (top level and per rule), `supersedes`, `status` and `author` change (`diffs/ESC1-w1-w2-allow-v1-to-v2.diff`). | One ordinary review of v2, with no widening (V4). As the predecessor, v1 needs its review and widening review, which it needed anyway. That review can re-derive v1's fingerprints from `H` plus the ledger (V5) without reading T1′. | §11 item 1 (the 4 W2 `ptr` lines), item 7 (the 7 W1 lines), RT-D, RT-I7A. `rule-stale` is also evaluated at `H`, because `H` is no longer a proper ancestor of `recorded_at`. No item results there, since every fingerprint is present at `H` and W1-c's located context reproduces (V1). |
| (b2) v2 at `main` | As (b1) | As (b1) | As (b1). Rejected because `main` moves and `H` is already a fixed role. |
| (b3) v2 at `H`, with W1-d's two context values recomputed at `H` | Everything except two context hashes | Review plus a widening review (the fingerprint set changes) | As (b1). Needed only if the final design reads "fingerprint reproduced at `recorded_at`" as including the context when `context_required` is false (owner question O-4). |
| (d) a new lineage without `supersedes` | v1 untouched | Review plus a widening review | It reuses the rule ids W1-a to W2-b, against "`id` (never reused)" (design sec. 6.2). Renaming the ids would change the controls that cite them. Rejected. |
| (a) or (c) an owner exception, or T1′ reaching `main` | — | — | (a) leaves items 1 and 7 unable to pass. (c) is barred by Q10 unless T1′ lands for its own sake. |

Placement: in the plan's record directory, frozen with `F` (design sec. 12.1: "rule files frozen with the plan live in
the amended plan's record directory"). Placing v2 in the tool's audit directory would need its own change to `main`
before `F`.

### ESC-2: `rules/register-infinity-params-v1.json` (its lint needs P's `edits_check.py`)

- **Recommended: no record change.** The configuration's checker companion and the profiles `ptr`, `repo`, `register`,
  `register-caps` and `infinity` are read at `F` (configuration diff), from the unchanged blob `1153e039…`
  (sha256 `2856e58c…`). The record's own `P` fields (`recorded_at`, `lint.checker.commit`) are not read, and `P` is an
  ancestor of `F`. The gap closes when `F` becomes reachable (§4). Review: the record's ordinary review, which it needed
  anyway, done against `F`'s `edits_check.py`. Affects §11 items 5 and 6 (the per-edit unit fails closed without the
  record).
- Alternative: a superseding record without the `P` fields. It gains nothing the engine reads, and it adds a record
  and a review. Not recommended.

### ESC-3: `records/repo-scope-v1.json` (its statement rests on P's checker)

- **Recommended: no record change.** The engine applies only the lists. Their equality with `HISTORICAL_PREFIX`,
  `HISTORICAL_FILE`, `ACTIVE_IN_RECORDS` and the generated-artifact rule (`edits_check.py` lines 786-788, 856 and 862)
  is checked by the record's reviewer at `F`, against the same blob. `source.commit` names `P`, which becomes reachable
  as an ancestor of `F`. Review: the ordinary review, needed anyway. Affects §11 item 11 and `--final`.
- Alternative: a superseding record whose statement rests on its stated lists alone. That is a change to a scope record,
  hence a widening review (design sec. 16.2), and it drops the traceable link to the checker. Not recommended.

### ESC-4: `records/gr58-hit-classification-v1.json` (the classified line exists only at T1′)

- **Recommended: no record change.** The engine matches the line by `(file, line_sha256)` at `X` and never reads
  `tree`. The line is `H`'s `papers/GR.md` line 58 with splices D040 and D041 applied. The rebuild from `H` and the
  plan's `ledger.json` is T1′'s blob `c4a320e2…` exactly (V5), and `X` carries the same blob. The record's reviewer
  re-derives the line and its context from `H` and the ledger at `F`, and states the equality. §32.5 classifies the
  `tree` reference under §A.42 item 8 as support on `main`, with the difference stated. Affects §11 items 1 and 7, and
  RT-D.
- Alternative (b): a superseding record that names `H` plus the splice ids instead of T1′. It adds a record and a
  review, and the engine reads neither field. Not recommended.
- Alternative (c), deferring the classification until the executed retirement: not valid. Records written after `F`
  never decide on `X` (design sec. 6.3), so `GR.md:58` would be `final-unclassified` and items 1 and 7 would fail.

## 4. The wider dependency on P

### 4.1 What a run at F reads that P now holds

| Artifact (plan directory) | Blob at P / sha256 | Read by | How it becomes available from `main` |
|---|---|---|---|
| `ledger.json` | `ba37c1cd…` / `2055e68f…` | `adapters.ledger`; `preserve_check --plan`; `X`'s record directory | at `F`; `F` reachable (4.3) |
| `edits.json` | `ec384fdf…` / `528f146d…` | ledger companion `edits` | same |
| `edits_check.py` | `1153e039…` / `2856e58c…` | companion `checker`; profiles `ptr`, `repo`, `register`, `register-caps`, `infinity`; support for ESC-2 and ESC-3 | same |
| `preserve_check.py` | `84b1939b…` / `101ecdf4…` | delegation classes `tex` and `pdf` (`checker_sha256` in the delegation draft); trial workflow `--plan` | same |
| `guards_check.py` | `6b6e403b…` / `ef89e1c7…` | `--predict` and `--mutants` (gate and trials; item 12 through `ci`) | same |
| `t0_jobs_44939798305.json` | `f62d01bf…` / `8c5edab3…` | `preserve_check` `PINNED` fixture | same |
| `PREREG.md` | `6931e3be…` at P | the pin table (last `Record pins`) for both the tool and `preserve_check`; the procedure | at `F` with §32 appended |
| New at F: `retirement-config.json`, its review, `w1-w2-allow-v2.json`, review records | — | configuration admission; records | at `F` |

These are read from `T`, which is on `main` before `F`: the tool files and workflow; the six v1 records,
`side-change-classes-v1.json`, `controls.json` and `delegation-draft.json` in the tool's audit directory.

These are read from `H` or `E`, both on `main`: `sitemap.json`, `rows.json`, Phase-0 `sites.json`, `ledger_check.py`
(V12), `E`, and the six pinned merges.

T1′ is reached only through w1-w2 v1's `recorded_at` (removed from use by ESC-1) and gr58's `tree` (never read).

### 4.2 What v6.0c requires

- **`T` on `main`: yes.** Execution identity point 6. The tool refuses unless the run's `head_branch` is `main`, and the
  consumer requires `T` on `M`'s first-parent chain (TR29).
- **`F` or the configuration on `main`: not required by the tool.** `F` is an explicit full id read through the
  verified reader, and the workflow fetches it by id.
- **§A.42 requires it.** Items 1 to 3 and 8 require every commit that a landed record names as support to be reachable
  from `main` no later than that record. The execution result note under `execution/` is in `C`. It records the
  `preserve_check.py --plan F` outputs (P §25.2, "Evidence"), and it lands with `L`. So `F` must be reachable before
  `L`. Because `L` must have exactly the parents `M` and `C`, `F` cannot arrive through `L`.
- **`F`'s tree must contain the tool's audit directory (V6).** The configuration's record references, the predecessor
  v1 of ESC-1, and the pinned `controls.json` and delegation contract are all read at `F`.

### 4.3 Minimal consistent arrangement (recommended, A)

1. `T` lands on `main` through its own reviewed pull request (outside this proposal).
2. The plan branch takes in a `main` that holds `T`, by an additive merge commit. `P` stays unchanged.
3. The amendment commits follow, append-only: PREREG §32 first, then the configuration, `w1-w2-allow-v2.json` and the
   review records, then §32.9's pins.
4. The pre-freeze gate (§31.12.17-18) runs at the exact candidate head. The candidate head is independently reviewed.
   The owner designates `F` (§A.50 items 2 and 5).
5. T0″ and T1″ are built, plus the tool's run over T1″. Each push and dispatch is approved separately.
6. Outside the T0″–T1″ window and before `L`, the plan's pull request (#1477) is merged into `main` by a merge commit
   that keeps its history (owner approval, §A.50 item 1). The repository's ruleset requires the head to contain
   `main`, which needs an update merge after `F`. That merge leaves `F` as an ancestor.
7. Execution `X..C`, then `L`. The plan directory's paths at `M` (step 6 put them there, byte-equal to `C`'s) are
   classified by a side-change class record written after `F`, as design sec. 13.3 allows for side changes on `M`. The
   landing check accepts identical bytes on both sides (V11).
8. The landing record lands the tool's result. `F` and `P` are already reachable.

Alternatives:

- **(B) Merge the plan after `L`.** Rejected. The execution note in `C` would land relying on an unreachable `F`
  (§A.42 item 2).
- **(C) Merge the plan before freezing and designate a commit on `main` as `F`.** This works. But the gate and the
  review then run on `main`, and any correction after a failed gate needs a further merge to `main`. A keeps
  corrections on the plan branch.

A adds one reviewed record (step 7's side-change class) and one merge (step 6). It adds no infrastructure.

## 5. P1 to P5 and P8: exact changes

PREREG changes: only the appended §32 (`diffs/PREREG-append-s32.diff`, against `P`'s `PREREG.md`, sha256
`bc05340f…e928`). §32.9 is the new last `Record pins` subsection, and §31.31 stays as `P`'s pins. Configuration changes:
`diffs/CONFIG-staged-draft-to-proposed.diff`, against the staged draft `75558ee3…`, and the resulting
`diffs/retirement-config.json.proposed`. Placeholders are written `<…>`. Each is filled from `T`, the review records or
the owner records before `F`.

| Item | Change | Where |
|---|---|---|
| P1: no reliance on `A`'s plan, round, thread or pin-table values | §32 names no authority record, plan id, round id, comment thread or freeze ledger, and no command takes such an argument. The configuration loses `retirement.owner` (which the S1 engine compared with `A`). | §32.2–§32.4, §32.7; configuration `retirement` |
| P2: which record quotes the owner's designation of `F` | The execution result note under `execution/` and the landing record of the tool's acceptance result, each with author, time and comment id. The tool does not read it. | §32.3 |
| P3: sec. 11 commands with `--freeze` and `--config` | Every command runs as `python3 -I -B tools/ledger_coverage.py <op> --freeze F --config F:verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json --out <dir> …`, with no plan, round or pin-table argument. There is a table for items 1–14. Item 7 is open (O-1). | §32.4 |
| P4: the configuration references records and reviews only; `retirement.owner` informational | `records` holds records and review records only, with no authorization records. `retirement` = `{name, issue}`, as in v6.0c sec. 16.2 (owner removed rather than kept as informational: the simpler form). The draft `notes` text is removed, since it is false at `F` and not a 16.2 field. | configuration; §32.2 |
| P5: no freeze-ledger append or form comment at landing | "The landing names no freeze-ledger append and no form comment"; acceptance is recorded by the landing record. | §32.7 |
| P8: tool and workflow pins and `repository_id` beside the PREREG whose last `Record pins` lists the configuration | `tool: {files, workflow}` added (placeholders until `T`); `repository_id: 1156244443`. §32.9 lists `retirement-config.json`, `review-retirement-config-v1.json`, `w1-w2-allow-v2.json` and the review records, together with the six unchanged `PINNED` digests. The pinned workflow's run steps and inputs are stated. `T` is on `main` before `F`. | configuration; §32.2, §32.7, §32.9 |

The `P` dependency adds one more configuration change: `adapters.ledger.commit` and both companions' `commit` are
removed, and the five profiles' `source.commit` changes from `P` to `null`. All of them are then read at `F`, from the
same blobs. ESC-1 replaces the `rules` entry for v1 with v2.

## 6. Consequences

**The frozen plan.** `P` is unchanged, both as a commit and in all seven of its files. The amendment is append-only,
as §28 and §31 were. §31.31 remains `P`'s pins.

**Trial procedures.**

- Every new file in the plan directory enters the predicted tree (V7). T0′ and T1′ therefore cannot be reused. T0″ and
  T1″ are rebuilt from the candidate head under §31.8's rule, as c.7093128173 also requires.
- The pre-freeze gate items 1-10 run again on the new head. They cover the SC-42 scan of the new record text, the
  duplicate check (§32 alone passes it, V8), the release gate and one CI diagnostic.
- One step is new: a dispatch of the tool's pinned workflow with `F` and the configuration path as inputs and T1″ as
  `X`, for §32.4 items 1–13 and the candidate part of 14. That first real-host run is also TR5's positive control,
  which owner decision Q5 defers to the A1 freeze.
- Every push and dispatch needs its own owner approval (§A.50 item 2).

**Existing evidence.**

- T0′ and T1′ of `P` and their runs (45077568347, 45080985924, 45083256017) remain valid evidence of what they tested,
  `P` at `H`. Per c.7093128173 they are not acceptance evidence for the amended plan. Because the ledger and edits are
  unchanged, they predict the checker steps of T0″ and T1″, but they do not replace them.
- The T0 and T1 evidence of P\* on `main` is unchanged.
- The six v1 records in the tool landing are unchanged.

**Acceptance criteria.**

- Each §11 check passes only through its §32.4 command under the tool's acceptance predicate. The original checkers
  still run inside it, as delegated classes.
- Item 7 as frozen fails at a T1′-style `X` (RT-I7). Unless it is restated (O-1), the amended plan cannot pass as
  written.
- Items 2 and 11 need the HP, context and hit records and the item-11 rules of design sec. 8.2. Those come from the
  records work package, not from this proposal.
- Item 4 reads "seven" re-affirmed fingerprints, which §31.10 already measured.
- The moved `main` (`AGENTS.md` base drift, `.claude/settings.json`, the trial workflow) still needs the
  reconciliation and side-change records of design sec. 15 item 0. Arrangement A adds the plan directory to that set.
- ESC-1 makes `rule-stale` evaluated at `H`, with no expected item (§3).

## 7. Open questions for the owner

| # | Question | Options | Recommendation |
|---|---|---|---|
| O-1 | Item 7 | (a) Restate it as design sec. 11 note 1 proposes, as a separate amendment item before `F` with its own preregistered text and independent review of DR-1/3/4/5, `resid` and W1. (b) Keep the literal check, so that the amended plan fails at item 7. | (a). It is a scientific acceptance-criterion change, outside this bounded proposal, and needs your separate decision. |
| O-2 | How `F` becomes reachable | A (merge the plan PR after `F`, before `L`) or C (designate a commit on `main`) | A. B is invalid (§4.3). |
| O-3 | Where v2 and the A1 review records live | the plan's record directory (frozen with `F`) or the tool's audit directory (a further change to `main` before `F`) | the plan's record directory |
| O-4 | W1-d's context value under the final design | the final design confirms that `context_required: false` fingerprints are reproduced by the sentence alone (b1 as proposed), or it requires the context (b3, with a widening review) | ask the tool-design reviewer to settle it before the v2 file is written. b1 keeps every value. |
| O-5 | Which records quote `F`'s designation | the execution note only, the landing record only, or both | both, since each relies on `F` |
| O-6 | `retirement.owner` | remove it, or keep it as informational | remove it, matching v6.0c sec. 16.2 |
| O-7 | The delegation contract's location (now `delegation-draft.json` in the tool's audit directory; design sec. 12.1 places it in the plan directory) | decide with the final tool design | no change proposed here, because it is outside P1–P5 and P8 |
| O-8 | Independent review of this proposal | name a non-author reviewer | before any amendment is authorized |

## 8. Verification limits

- Engine behaviour was read from, and the lint run on, the S1 implementation (`443e871f`), not a v6.0c implementation.
  The imports used `-B`, and the worktree stayed clean.
- No CI, trial or host run. The local clone is shallow. T1′, `P` and `H` were read locally by `git show`.
- §32.4's commands follow design sec. 11's mapping. Their exact option names depend on the final CLI.
- The placeholders (`T`, tool and workflow pins, review records and their hashes, owner records) cannot be filled until
  those objects exist.
- `retirement-config.json.proposed` is not a valid configuration while it holds placeholders.

## 9. Checklist for the independent review

1. Each V1–V12 result, reproduced from the objects (scripts in `work/`).
2. That no proposed change alters a scientific value, an edit, a ledger entry or a fingerprint. Diff v1 against v2, and
   the staged configuration against the proposal.
3. The §A.42 item 8 classification of every off-`main` reference in §32.5 and §4.1.
4. That §32 contains no reference to an authority record, freeze ledger, plan id, round id or form comment (P1, P5),
   and that §32.9 is the last `Record pins` subsection.
5. That arrangement A satisfies §A.42 at `L` and needs no new infrastructure.
6. That the consequences in §6 are complete. In particular, check whether any T0″ or T1″ expectation of §31.8 changes
   because the predicted tree now holds the new record files.
