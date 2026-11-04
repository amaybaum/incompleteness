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

## Results (unreviewed)

These are mathematical verdicts only. Physical standing is in `PROOF-ATTEMPT.md`, Q4, where no
hypothesis is derived for native OI.

- **Q1, proved under H-pre.** Under H-pre, H-rule, H-torus and H-access with its record dictionary,
  the pre-cut history has the same law under both settings, with `K0` mass retained.
  - H-pre states that the setting bank `b5` and port 5's pre-cut bank triples `f_5(t)`,
    `S+4 < t ≤ L+3`, are uniform given everything else.
  - The history_v11 bank law implies it. H-prior's sourcing sentence retains that law, so under H-prior's
    sourced reading H-pre holds.
- **Q1, counterexample to H-prior as its displayed equation.** Read without its sourcing sentence, the
  displayed equation lets `D′` be a point mass.
  - For the all-zero point mass, the public pre-cut record `(R.B, R.D, U_{S+6}(port 5))` determines
    the setting exactly (TV 1). The proof is by hand from `H`'s 8-entry table.
  - The all-zero law is not the original preparation.
  - No source specifies an original law with non-uniform `V5`.
- **Q2, valid under the parent's prior.** The parent forward-kernel proof is valid under its prior,
  given its recorded geometry. K3's cardinality step, K4′ and K7′ are supplied here. K6′ diagnoses
  where the LA gap enters.
- **Q3, proved under H-prior ∧ H-pre.** LA-EQUAL holds under H-prior ∧ H-pre, which is equivalent to
  H-prior⁺. This is one direction only. Under H-prior's sourced reading it holds conditionally.

## Plan

1. Q0: state LA-EQUAL with every hypothesis, including the history_v11 bank law (H-bank).
2. Q1: pre-cut equality under both settings, as a proof under stated hypotheses or a counterexample.
3. Q2: audit of the parent forward-kernel proof (`native-random-setting-test.md:95–112`).
4. Q3: composition of the tail, pre-cut and kernel factors into LA-EQUAL.
5. Q4: for each hypothesis, mathematical role and physical standing (derived, posited or open).
