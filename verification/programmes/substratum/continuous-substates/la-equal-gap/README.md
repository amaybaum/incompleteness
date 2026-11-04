# LA-GAP: the LA-EQUAL proof gap (#1007)

**Status: WIP / UNVERIFIED. Not independently reviewed.** This directory records a paper-only
study. It is model-authored by `writer-1007`, a Claude Code subagent, and has had no
independent review. It is not a premise of any established claim (AGENTS.md §A.46 item 7).

## Scope and authorization

- **Unit:** LA-GAP of Issue #1007, the gap recorded in
  `verification/programmes/oi-qm/reconstruction/measurement-record-formation/LA-EQUAL-REVIEW.md`.
- **Activation record:**
  [#1007 comment 6642603567](https://github.com/amaybaum/incompleteness/issues/1007#issuecomment-6642603567)
  (owner authorization amaybaum, 2026-11-04, quoted there). Paper-only: proof and counterexample work.
- **Not done here:** no computation, script, probe, Lean build or enumeration was run. No workflow was
  dispatched. No existing file was edited. N5 and LA-EQUAL are not promoted anywhere.
- **MR-1 N5** (`measurement-record-formation/preregistration.md:109–111`, frozen) is untouched, and
  its status is unchanged: not established, not usable as a premise.

A result here is either a mathematical statement proved under named hypotheses or a counterexample to
an implication. Whether each hypothesis holds for native OI is a separate question, answered in its
own column (`PROOF-ATTEMPT.md`, Q4). A proof under hypotheses is not a physical derivation of them.

## Inputs (all on `main` at `f5c281ae10a913ec68fa41b3b839ad0b164979cd`)

Blob ids are abbreviated to 12 hex digits.

| Blob | Path |
| --- | --- |
| `dcb6cbe5350b` | `verification/programmes/oi-qm/reconstruction/measurement-record-formation/LA-EQUAL-REVIEW.md` |
| `e5af8ee7b2db` | `verification/programmes/oi-qm/reconstruction/measurement-record-formation/README.md` |
| `c36fb14bd776` | `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md` (N5 at 109–111) |
| `41ac4d05aa54` | `verification/programmes/substratum/continuous-substates/later-access-preregistration.md` |
| `4201eeaad950` | `verification/programmes/substratum/continuous-substates/later-access-result.md` |
| `7410f9aaffa9` | `verification/programmes/substratum/continuous-substates/later-access-result.json` (CP-PRECUT record) |
| `a53cfe3e18ac` | `verification/programmes/substratum/continuous-substates/native-random-setting-test.md` |
| `6fde84da4309` | `verification/programmes/substratum/continuous-substates/native_random_setting_probe.py` (read as specification) |
| `b2baf4cbabba` | `verification/programmes/substratum/continuous-substates/native_later_access_probe.py` (read as specification) |
| `ed3a7131939f` | `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/history_v11/REPORT.md` |
| `cbc5d75e9c43` | `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/native_vread_v15/checks.py` (constants and `PORTS`, read as specification) |

Discussion read: #1007 comment 6641543358, #866 comment 6641545083, PR #1109's comments.

## Contents

- `PROOF-ATTEMPT.md`: questions Q0–Q4, each ending in a verdict, and the proposed computation specs.

## Plan

1. Q0: state LA-EQUAL with every hypothesis, including the history_v11 bank law (H-bank).
2. Q1: pre-cut equality under both settings, as a proof under stated hypotheses or a counterexample.
3. Q2: audit of the parent forward-kernel proof (`native-random-setting-test.md:95–112`).
4. Q3: composition of the tail, pre-cut and kernel factors into LA-EQUAL.
5. Q4: for each hypothesis, mathematical role and physical standing (derived, posited or open).
