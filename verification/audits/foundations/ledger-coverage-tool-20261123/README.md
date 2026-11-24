# Ledger and terminology verification tool: records (unreviewed drafts)

Status: implementation of design v6.0e (sha256
4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131), adopted by the owner on 2026-11-24. **Every record
in this directory is an unreviewed draft.** None has an independent review record, and no plan commit `F` exists.

The tool verifies which exact plan was executed and what actually ran: the plan commit `F`, the pin table and the
configuration it admits, the tool commit `T` with every tool file and the workflow, the repository and event of the
producing CI run, and the evaluated commits. It makes no claim about authorization: the owner's approvals of the
configuration, of `F` and of a landing are procedural (AGENTS.md sec. A.45 rule 3, A.50, A.51) and are quoted with
author and time in the record that relies on them (sec. A.42 item 7). The tool neither reads nor checks them. The
class identifiers `authorized-replacement`, `authorized-removal`, `unauthorized-edit` and `unauthorized-change` keep
the fixed technical meanings of design sec. 5 ("Class meanings"), which every result carries as `class_meaning`.

A configuration is admitted only from `F`: it is read from `F`'s tree at the path `--config F:PATH` names, and only
if the last `Record pins` subsection of the `PREREG.md` beside it lists it and its review record with their sha256
(design sec. 6.3, configuration admission). An admission reaches `"chain"` only inside a host CI job of the
configuration's pinned workflow, in the repository its `repository_id` names, with event `push` or
`workflow_dispatch`, head branch `main`, and `T`'s tool files, the workflow and the checkout equal to the
configuration's `tool` pins (execution identity). Every other run is refused with ERROR `CONFIG_UNREVIEWED` (exit 65).
The real-tree controls run through the control harness, which writes `control-result.json` with `"harness": true`; a
harness result is evidence about the implementation and is never acceptable.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This directory decides no
scientific question and no row disposition.

## Files

| Path | Kind | What it holds |
|---|---|---|
| `controls.json` | A1 control set | the preregistered A1 controls with the design's expected outcomes, the tool-level controls GV1-GV7 and EI1-EI15, and the control-only inputs (DR-3's witness `AGENTS.md` at `H`) |
| `delegation-draft.json` | `oi-delegation/1` | a draft of the delegation contract; the contract itself belongs in the amended plan's record directory at `F` |
| `rules/dr-deny-v1.json` | `oi-term-rules/2` | deny rules DR-1 (a, b, c), DR-3, DR-4, DR-5 with examples and real-tree countercontrols |
| `rules/resid-v1.json` | `oi-term-rules/2` | the review pattern `resid` (resid-a, resid-b, resid-c) |
| `rules/w1-w2-allow-v1.json` | `oi-term-rules/2` | the seed allow rules W1 (four sentences) and W2 (two sentences), each fingerprinted at the commit its `recorded_at` names |
| `records/gr58-hit-classification-v1.json` | `oi-hit-classification/1` | the classification of the line papers/GR.md:58 of the retirement candidate |
| `records/repo-scope-v1.json` | `oi-scope/1` | the scope of the `repo` profile (item 11) |
| `rules/register-infinity-params-v1.json` | `oi-term-rules/2` | the per-edit parameters of items 5 and 6 that are not extractable assignments of the plan's checker (kind `params`), linted against the checker the configuration pins |
| `records/side-change-classes-v1.json` | `oi-side-change-classes/1` | the class `tool-landing` only: every path this tool's landing adds, each with its exact blob |

The A1 configuration `retirement-config.json` (`oi-retirement-config/1`) is not part of this landing. It belongs in
the retirement plan's record directory, `verification/audits/foundations/a1exit-deletion-20261121/`, frozen with the
plan at `F` beside the `PREREG.md` whose last `Record pins` subsection lists it and its review (design sec. 6.3,
16.2); it pins the class record above, the tool's files and workflow (`tool`) and the repository id
(`repository_id`). Until then it exists only as an unreviewed draft outside the repository, and the A1 controls read
it with `--staged-config`.

## The pinned workflow

The tool's landing may add paths only under `tools/`, its audit directory, and the one file
`.github/workflows/ledger-coverage.yml`, the workflow that `tool.workflow` pins. This is the owner's decision on
design sec. 12.3 (`amaybaum`, 2026-11-24). The class record lists that file as one exact path with its blob, not as a
prefix. It is `workflow_dispatch` only, so landing it starts no run.

The workflow is the text of design sec. 6.3 point 5. It is dispatched with `F`, the configuration path, the plan
check and the role commits that check needs, as inputs that reach the shell only through `env:`. The check is a
choice among fixed values, and each value selects one fixed command in a `case` block, with every expansion quoted;
a value with no arm exits 64. The arms are the commands of design sec. 11 as the amended plan's sec. 32.4 states
them, one per plan check, each record read at `F` from the path the configuration names (the ledger, the edit list
and the HP record in the configuration's directory; the delegation contract, the scope record and the hit
classification record in this directory); the amended plan states the commands of record, and a changed arm is a new
workflow blob, pinned again by the configuration frozen at `F`. The workflow fetches `F` with
`git fetch --no-tags -- origin "$F"`. Its step `pre-run pin check` runs one inline program with
`python3 -I -S -B -c`, which refuses unless `GITHUB_REF` is `refs/heads/main` and `F` a full lowercase 40-hex id, and
compares the entry point and every file under `tools/ledger_coverage/` on disk with the configuration's `tool.files`
before any file of the checkout runs; the tool then runs with `python3 -I -S -B`, so neither `site` nor the runner
image's installed packages load (the tool uses the standard library only). Every `uses:` line names an action of a
GitHub account, `<owner>/<repo>[/<path>]`, by a full commit id; a local or parent path (`./`, `../`) is refused even
with a 40-hex suffix.

## Host reads

The tool and the consumer read from the host only the REST records of GitHub Actions runs, jobs and artifacts, each
with a GET: the producing run's record (repository, head repository, event, head branch, workflow path, `head_sha`)
and its artifact list, and, for the host-run delegation classes, the runs on the evaluated commit with their jobs.
A failed or incomplete read is never a fallback to another source. Every repository object is read from a local git
object store and verified against its id (design sec. 6.3, object integrity).

## Limitations (stated, not closed)

The tool verifies coverage and provenance. It does not establish complete semantic detection, and a PASS
says nothing about the meaning of any replacement text (design sec. 1).

- Deny rules close only forms with a fixed lexical anchor. Paraphrases without one are, at best, REVIEW
  through `resid`, and only for the classes design sec. 1 lists.
- Accepted residuals that PASS when added (design sec. 15 items 2 and 3), each kept as a control with that
  expected outcome: "the framework's sixth structural property, finiteness of the bijection" (V4); "The
  framework's sixth structural property is finiteness of the substratum" (V27); "the substratum's sixth axiom,
  finiteness" is REVIEW only (V15); "the six posits of the substratum", "six assumptions about the
  substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and "$A_1$–$A_6$" match no
  deny rule and no `resid` alternative. The original literal item-7 check misses each of them too.
- Context rules and S0 indicators are preregistered heuristics. Rule fingerprints recognize identical text
  only. The tool checks that role fields differ, not who wrote the records.
- Which directory of `F` is the plan's record directory is identified by the configuration path, a run input that
  the result records and the consumer compares with the landing record (design sec. 6.3, flag F-2).

## Reproduction

From the repository root, inside a host job of the pinned workflow, with a plan commit `F` whose `PREREG.md` beside
the configuration lists the configuration and its review in its last `Record pins` subsection:

    python3 -I -S -B tools/ledger_coverage.py coverage --freeze F --config F:PATH --commit REV --out DIR

The control runs:

    python3 -I -S -B tools/ledger_coverage.py self-test --out DIR
    python3 -I -B tools/ledger_coverage/adapters/synthetic_fixture.py DIR .
    python3 -I -B tools/ledger_coverage/adapters/conformance_controls.py DIR

With `CFG=HEAD:verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json` and `STAGED` the
staged draft (the runners read it into an in-memory stand-in for `F`, `HEAD`'s tree plus that file at its plan
path):

    python3 -I -B tools/ledger_coverage/adapters/staged_purity_lint.py --repo . --config $CFG --staged-config STAGED --out DIR
    python3 -I -B tools/ledger_coverage/adapters/a1_conformance.py --repo . --config $CFG --staged-config STAGED --out DIR
    python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo . --config $CFG --staged-config STAGED --main MAIN --out DIR

`MAIN` is the `main` commit against which the sequencing safeguard (design sec. 13.4, control RT-L2) predicts `main`
plus this landing; the runner exits with status 2 without it. The runners resolve the revisions they are given; the
tool itself reads every role commit by its full id only.

## References to content not on `main` (sec. A.42 item 8)

Two commits that the files of this landing name are not reachable from `main`: the frozen A1 plan `P`
(4c79be642ca631573f06b444903be75ec4f5e2b6) and the trial candidate `T1'` (14ac71b4b0a0c0aa2d7068d6799a73f474097060).
Each reference is classified below by what reads it and what claim it supports: **provenance** (no claim uses the
content), **support on `main`**, or **gap** (support off `main`). None of these references is read by the tool's own
admission or execution identity; the gaps concern decisions of the A1 retirement once a frozen configuration
references the records, and stay open as the escalations ESC-1 to ESC-4 of the accepted Q10 disposition.

| Reference | Where | What reads it | Classification |
|---|---|---|---|
| `T1'` in each allow rule's `recorded_at` | `rules/w1-w2-allow-v1.json` | the rule-file lint reproduces every fingerprint (sentence and context) at that commit, and the `rule-stale` scoping decides ancestry against it | gap: admitting the rule file needs `T1'`'s objects (ESC-1) |
| `T1'` in the file's top-level `recorded_at` | `rules/w1-w2-allow-v1.json` | nothing | provenance |
| `T1'` in the file's top-level `recorded_at` | `rules/dr-deny-v1.json` | nothing; the deny rules' countercontrols read `H` and the control input at `H`, both on `main` | provenance (ESC-5, administrative) |
| `T1'` in the file's top-level `recorded_at` | `rules/resid-v1.json` | nothing; a review pattern is linted on its patterns and examples only | provenance (ESC-5, administrative) |
| `P` in `recorded_at` and in `lint.checker.commit` | `rules/register-infinity-params-v1.json` | neither field is read; the lint compares the parameters with the checker that the configuration pins as its ledger adapter's `checker` companion, which the staged configuration pins to `P`'s `edits_check.py` | provenance for the two fields; gap for the parameters' stated equality to `P`'s checker, which needs `P`'s `edits_check.py` (ESC-2) |
| `P` in `source.commit` | `records/repo-scope-v1.json` | not read: the run applies only the record's lists | gap: the record's statement that its lists are the plan checker's classification can be verified only against `P`'s `edits_check.py` (ESC-3) |
| `T1'` in `classifications[0].tree` | `records/gr58-hit-classification-v1.json` | not read: the run matches the classified line by file and line hash | gap: the classified line occurs only in `T1'`'s `papers/GR.md`, which the record's review must read (ESC-4) |
| control input `agents-md-at-T1p` (commit `T1'`) | `controls.json` | the control RT-DR3W of the A1 control runner only; no deny rule's countercontrol names it | provenance (a control-harness input; harness results are never acceptable) |
| "at `T1'`" in case texts and expected figures | `controls.json` | the A1 control runner's comparisons | provenance (preregistered control descriptions) |
| the constants `T` (`T1'`) and `P` | `tools/ledger_coverage/adapters/a1_controls.py` | the real-tree controls' candidate and the ledger, edit list and checker the A1 controls read | provenance (control-harness results) |
| `T1'` and `P` through `a1_controls`; the blob id 9f4fc3e830707c90ffc105842d26d5b51f01760b (`T1'`'s `AGENTS.md`) | `tools/ledger_coverage/adapters/a1_conformance.py` | the control expectations of WB1-WB15, S11-56 to S11-58 and N3-N18 | provenance (control-harness results) |
| the id 86d79863821f3f8cdad86771008b2df89fd1961a | `tools/ledger_coverage/adapters/a1_conformance.py` | the expected blob id of the composed `AGENTS.md` (`main` 8e9b8334 with splice D296 of `P`'s ledger) that N10, N11 and the configuration-route control compute in memory | provenance; a computed identifier, not an object in any repository |
| `P` and `T1'` by full id | this README | descriptive | provenance |

The workflow text names two actions by full commit id (`actions/checkout`, `actions/upload-artifact`). These are
commits of other repositories that the workflow runs; the pin fixes their content (design sec. 6.3 point 5), and they
are not references to content of this repository. `tools/ledger_coverage/adapters/host_fixture.py` repeats the first
in its fixture workflow, and `conformance_controls.py` uses the placeholder id 0123456789abcdef0123456789abcdef01234567
in its refused workflow forms; both are fixture data that no claim uses.
