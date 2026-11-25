# A1 plan reconciliation, Stage A: findings (WIP / UNVERIFIED, awaiting independent review)

Work package: Stage A of the A1 plan reconciliation, authorized by the owner (amaybaum, 2026-11-25, coordinating
session): "Authorize Stage A as proposed". Scope: read-only questions O-9, item 2's context record, O-4/N2 and
P1-P5/P8, and a resource estimate for Stage B. No run against `T1'`, no dispatch, no scientific change, no amendment.
Writer: Claude. Independent reviewer: ChatGPT, through the owner.

Goal link (sec. A.47): A1-EXIT (#1169). This note decides which preconditions of the amended plan are met by the tool
as landed and which need further work before `F`; it decides no scientific question.

Sources read: the tool on `main` at `e2e2a623265187a28ebec604ab8bcc672742888f` (merge of PR #1557); the adopted design
v6.0e (preserved copy, design sha256 `4024a31c...5131`); the frozen plan `P` `4c79be642ca631573f06b444903be75ec4f5e2b6`;
the amendment proposal r5 and its reviews r1-r5; the staged configuration (sha256 `5072a3b0...a0`); all as preserved on
branch `records/a1-retirement-preservation-20261124` at `b9a03dc3434e0c1e5d1c88116648dea69d35d8ce`.

## 1. O-9: classification of the plan directory's files at `M`

**Finding: not resolved by the adopted design or the landed tool. It needs a tool change.**

- Design v6.0e sec. 13.1: every path changed between `H` and `M` is a side change, classified only by a reviewed
  side-change class whose pin equals its blob at `M`; the one exemption is the class record itself, pinned by the
  configuration. The landed code implements exactly this (`tools/ledger_coverage/engine/reconcile.py`,
  `classify_side`; `engine/execution.py`, `_side_class`); no provision covers the plan's record directory. An
  unclassified side change is REVIEW_REQUIRED `side-change-unclassified`, which the acceptance predicate does not
  accept.
- The design's `record-dir` class (sec. 7.3, adapter `deleg_record_dir.py`) governs the plan directory in `X` and `C`
  against `H`, not side changes on `M`.
- The plan directory is absent from `main` and from `H`; PR #1477's branch adds only that directory (7 files at `P`).
  The side changes arise because arrangements A and C' (proposal r2 sec. 5) merge the plan into `main` before `L`, as
  sec. A.42 items 2, 3 and 8 require for `F` to be reachable when the execution lands.
- No record-only arrangement exists: a class frozen at `F` cannot pin `retirement-config.json` (which pins the class
  record) or `PREREG.md` (whose `Record pins` list the configuration), since each would close a hash cycle; a record
  written after `F` is not admissible (design sec. 13.3; the tool admits only records the frozen configuration
  references). Arrangement B (merge the plan after `L`) was rejected in proposal r1 under sec. A.42.
- The rule proposed in r2 is cycle-free and small: a path under the configuration's directory is classified when its
  blob at `M` equals its blob at `F` (the run already names `F`). It requires a design amendment, an implementation with
  positive and negative controls, independent review, CI validation and a new landing of the tool before `F`.

## 2. Item 2: is a context record needed?

**Finding: yes, and with it further records; the item-2 workflow arm cannot pass them as landed.**

- Design sec. 3.5 and 4.4: at `T1'`, 7 unchanged sites carry an `E..H` meaning-context change (FULL:4895, 4905, 4919;
  ch18:164, 174, 188; papers/Main.md:332), each a FAIL `context-meaning-unverified` until a context adjudication
  (`oi-context-adjudication/1`) resolves it. These sites are unchanged, not HP sites, so `hp.json` cannot carry them.
  `H..X` adds RET cases (5 at `T1'`), and sec. 4.4 lists 7 + 3 structure REVIEW items resolved by indicator
  adjudications. Counts at the amended candidate may differ.
- The coverage command reads HP records only from `--hp` and hit-classification and context records only from
  `--classify` (`engine/cli.py`, coverage; arguments at lines 62-63). The workflow's `item2-coverage` arm passes
  `--hp "$F:$D/hp.json"` and one `--classify`, the GR.md:58 record. The context adjudications and the hit
  classifications for hits outside HP regions (design sec. 8.2) therefore cannot reach item 2.
- This is the case the owner's reconciliation obligation 4 foresaw: the arm must name further fixed record paths in
  the plan directory (for example `$F:$D/context-adjudications.json` and `$F:$D/hit-classifications.json`), which is a
  new workflow blob, re-pinned by the tool-landing class record and the configuration, landed on `main` before `F`.
- Item 1 (`terms`, profile `ptr`), the amended item 7 and item 11 need no new arm: their records are named already, and
  item 11's rules come through the configuration's rule files.

## 3. O-4/N2: must the predecessor v1 pass its fingerprint lint at `T1'`?

**Finding: no, under the landed tool.** Fingerprints are linted only for the rule files the configuration references
(`engine/cli.py`, the rule loop calling `rules.lint_rule`). A predecessor named by `supersedes` is resolved for the
widening comparison and checked for its own review chain (`engine/records.py`, `supersedes_problems`,
`predecessor_problems`), not re-linted. v1 still needs its own review record, as amendment sec. 32.5 already requires.
The object store must hold v1 at or before `F`, so `F`'s tree must contain the tool's audit directory (proposal r2's
requirement).

## 4. P1-P5/P8: configuration pins

**Finding: met at the current `main`.** The staged configuration pins 43 tool files, all equal to `main` at
`e2e2a623`; its workflow pin equals `main`'s `.github/workflows/ledger-coverage.yml`; its `repository_id` is
1156244443, this repository's id. These pins change if the tool lands again (sections 1 and 2). Still to be added
before `F` (Stage C): the class-record pin `81af5033...` -> `4b28d3d2...`; the records for `hp.json`, context and hit
classifications; the delegation contract in the plan directory (now the tool directory's `delegation-draft.json`);
the side-change classes for `.claude/settings.json` and the trial workflow and the `AGENTS.md` reconciliation
(review r2, focus 7), none of which the staged configuration references yet.

## 5. Consequences for the sequence

Sections 1 and 2 both need a tool revision before `F`: the O-9 rule (code, design text, controls) and a new item-2
workflow arm. The two can share one revision, review, CI validation and landing. This reopens the tool for these two
changes only; it is not a redesign.

## 6. Stage B estimate

Load, from design sec. 8.2 at `T1'` (the amended candidate's counts may differ):

| Records | Count |
|---|---|
| HP site adjudications (`hp.json`), with walk steps, `own_lines` for 22 merged sites, classification, splice attribution, hit classifications | 113 sites |
| Context adjudications | 12 (7 `E..H`, 5 `H..X`) |
| Indicator adjudications | 10 |
| Hit-line classifications outside HP regions | about 226 lines in all, less those inside HP regions |
| `repo`-profile exact-path rules (item 11) | 176 lines |

The tool computes walks, regions and splice attribution; classification is judgment. Estimate: one writer agent in
batches of about 20 sites or 50 lines, one independent review per batch, about 15 to 20 batches, all local, no CI.

**Open for the owner.**
1. Whether to open the tool revision of section 5, and in which order relative to Stage B.
2. Drafts generated at `H` need no candidate. Drafts against an amended candidate built from `H` and the amended
   ledger, for splice attribution and the `H..X` items, need that candidate; whether building it locally for drafting
   is a trial under sec. A.50 item 2 is for the owner. Amendment sec. 32.6 states that a diagnostic run is not a trial
   run.
