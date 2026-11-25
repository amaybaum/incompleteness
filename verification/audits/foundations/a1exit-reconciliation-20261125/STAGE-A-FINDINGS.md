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
- The command line needs no change for this: `--classify` is repeatable (`engine/cli.py:63`, `action='append'`) and
  already routes a record of schema `oi-context-adjudication/1` to the context collection and every other admitted
  record to the hit classifications (`engine/cli.py:845-852`). The demonstrated deficiency is the workflow invocation
  only; any further executable change needs its own demonstrated need.
- Item 1 (`terms`, profile `ptr`), the amended item 7 and item 11 need no new arm: their records are named already, and
  item 11's rules come through the configuration's rule files.

## 3. O-4/N2: must the predecessor v1 pass its fingerprint lint at `T1'`?

**Finding: no fingerprint re-lint at `T1'`, under the landed tool; every other predecessor obligation stands.**
Fingerprints are linted only for the rule files the configuration references (`engine/cli.py:238`, the rule loop
calling `rules.lint_rule`). A predecessor named by `supersedes` is read for the widening comparison, and the chain
checks of `engine/records.py:136-224` (`supersedes_problems`, `predecessor_problems`) still require of it a valid
lineage id and schema, presence in the object store at or before `F`, no cycle and no ambiguous ancestry, its own
review record and, where it widens its predecessor, a widening review. v1 therefore needs its own review record, as
amendment sec. 32.5 already requires.
The object store must hold v1 at or before `F`, so `F`'s tree must contain the tool's audit directory (proposal r2's
requirement).

## 4. P1-P5/P8: configuration pins

**Finding: met at the current `main` (writer's comparison; reproduction in Appendix A, V1).** The staged configuration pins 43 tool files, all equal to `main` at
`e2e2a623`; its workflow pin equals `main`'s `.github/workflows/ledger-coverage.yml`; its `repository_id` is
1156244443, this repository's id. These pins change if the tool lands again (sections 1 and 2). Still to be added
before `F` (Stage C): the class-record pin `81af5033...` -> `4b28d3d2...`; the records for `hp.json`, context and hit
classifications; the delegation contract in the plan directory (now the tool directory's `delegation-draft.json`);
the side-change classes for `.claude/settings.json` and the trial workflow and the `AGENTS.md` reconciliation
(review r2, focus 7), none of which the staged configuration references yet.

## 5. Consequences for the sequence

Sections 1 and 2 both need a tool revision before `F`: the O-9 rule (code, design text, controls) and a new item-2
workflow arm (workflow only; no command-line change is shown to be needed). The two can share one revision, review, CI validation and landing. This reopens the tool for these two
changes only; it is not a redesign.

## 6. Stage B estimate

Load, from design sec. 8.2: historical counts measured at `T1'`, not measurements of the amended candidate, whose
counts may differ:

| Records | Count |
|---|---|
| HP site adjudications (`hp.json`), with walk steps, `own_lines` for 22 merged sites, classification, splice attribution, hit classifications | 113 sites |
| Context adjudications | 12 (7 `E..H`, 5 `H..X`) |
| Indicator adjudications | 10 |
| Hit-line classifications outside HP regions | about 226 lines in all, less those inside HP regions |
| `repo`-profile exact-path rules (item 11) | 176 lines |

The tool computes walks, regions and splice attribution; classification is judgment. Estimate: one writer agent in
batches of about 20 sites or 50 lines, one independent review per batch, about 15 to 20 batches, all local, no CI.
The batch count is a provisional planning estimate, not a measured requirement; it is re-estimated from the amended
candidate's counts when Stage B is considered.

**Open for the owner.**
1. Whether to open the tool revision of section 5, and in which order relative to Stage B.
2. Drafts generated at `H` need no candidate. Drafts against an amended candidate built from `H` and the amended
   ledger, for splice attribution and the `H..X` items, need that candidate; whether building it locally for drafting
   is a trial under sec. A.50 item 2 is for the owner. Amendment sec. 32.6 states that a diagnostic run is not a trial
   run.

## Appendix A. Reproduction of V1 and V2 (independent review, 2026-11-25)

The independent review (ChatGPT, relayed by the owner) returned ACCEPT-WITH-NITS, provisional, with N1-N3 (applied
above) and two verifications outstanding. The commands below need only `git` and Python 3 standard library on a full
clone of the repository; `REC` is `verification/audits/foundations/a1-retirement-records-20261124` and the records
commit is `b9a03dc3434e0c1e5d1c88116648dea69d35d8ce`.

### V1. Staged configuration pins and repository identity

The staged configuration is the preserved copy at
`$REC/copies-2/coord2-ledgertool-design/impl-v6.0e/staging-4f4a9d58/verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json`
on the records commit; its sha256 is `5072a3b0e25e9283acecf4c3df87f820e34464d8d6e2e501ec672615114a96a0`, equal to the
original's (`MANIFEST-2.json`, byte-identical).

```
REC=verification/audits/foundations/a1-retirement-records-20261124
CFGPATH=$REC/copies-2/coord2-ledgertool-design/impl-v6.0e/staging-4f4a9d58/verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json
git show b9a03dc3434e0c1e5d1c88116648dea69d35d8ce:$CFGPATH > cfg.json && sha256sum cfg.json
python3 -I - <<'PY'
import json, hashlib, subprocess
c = json.load(open('cfg.json')); M = 'e2e2a623265187a28ebec604ab8bcc672742888f'
blob = lambda p: subprocess.run(['git', 'show', M + ':' + p], capture_output=True, check=True).stdout
files = c['tool']['files']; items = files.items() if isinstance(files, dict) else [(f['path'], f) for f in files]
bad = [p for p, v in items if hashlib.sha256(blob(p)).hexdigest() != (v['blob_sha256'] if isinstance(v, dict) else v)]
w = c['tool']['workflow']
print(len(items), 'tool files;', len(bad), 'mismatches', bad)
print('workflow', w['path'], hashlib.sha256(blob(w['path'])).hexdigest() == w['blob_sha256'])
print('repository_id', c['repository_id'])
PY
gh api repos/amaybaum/incompleteness --jq .id
```

Writer's result: 43 tool files, 0 mismatches; workflow `.github/workflows/ledger-coverage.yml` True; `repository_id`
1156244443, and the API returns 1156244443.

### V2. Reachability, plan-directory absence and the exclusion of record-only arrangements

Premises, each with where it is checked:

1. **`F` must be reachable from `main` when the execution lands.** AGENTS.md sec. A.42 item 2 (content a claim needs
   from an off-`main` commit lands no later than the claim), item 3 and item 8 (a verdict that depends on commits uses
   those commits; copying their files does not make them reachable). Every acceptance names `F` in its admission
   (`"chain"`, design sec. 6.3). Proposal r1 rejected arrangement B (merge the plan after `L`) on this ground
   (`$REC/copies/coord2-a1-amend/PROPOSAL.md`, line 187).
2. **The plan directory is on neither `H` nor `main`, and the plan branch adds only it.**
   `git ls-tree -r --name-only 53c6601a10419b6b333cc992474272501ab542af verification/audits/foundations/a1exit-deletion-20261121`
   and the same at `e2e2a623...` print nothing;
   `git diff --stat $(git merge-base 4c79be642ca631573f06b444903be75ec4f5e2b6 e2e2a623265187a28ebec604ab8bcc672742888f) 4c79be642ca631573f06b444903be75ec4f5e2b6`
   lists the directory's 7 files only. Hence arrangements A and C' (both merge the plan into `main` before `L`) make
   every file of the directory a side change between `H` and `M`.
3. **What classifies a side change.** `engine/reconcile.py:54-72`: an exact class pin at `M`, or the path is a class
   record the configuration references (`record_refs`, filled only from side-change class records,
   `engine/cli.py:1150-1193`). Nothing else.
4. **Only records the frozen configuration references are used.** Configuration-listed records are admitted by
   reference (`engine/config.py`, `L.admitted`); command-line records only if their sha256 is so referenced
   (`engine/cli.py:182-186`: "a record not referenced by the frozen configuration is never used for a decision"). A
   record written after `F` is therefore never used, and design sec. 13.3 forbids one for a foreseen side change.
5. **The pin dependencies.** The configuration pins each class record by sha256 (`roles.side_change_classes`; the
   staged configuration, lines 17 and 656). `PREREG.md`'s last `Record pins` subsection lists the configuration and its
   review record by sha256 (design sec. 6.3, configuration admission; `engine/config.py:167-203`). A review record names
   the sha256 of the record it reviews (design sec. 6.3, ownership chain). A class pin names the covered path's blob.

From 3-5: class records frozen at `F` can pin the directory's other files, and are themselves classified through the
configuration's pin; but no class record can pin the configuration (configuration -> class record -> configuration),
its review record (review -> configuration -> class record -> review) or `PREREG.md` (PREREG -> configuration -> class
record -> PREREG) without a hash cycle, and no later record is used (4). These three files remain unclassified under
every records-only arrangement that merges the plan before `L`; and by 1 and 2 every admissible arrangement does.
The conclusion is limited to the landed tool and the plan's present record structure (configuration and its review
inside the plan directory, listed in `PREREG.md`'s `Record pins`); a change to either is outside Stage A.
