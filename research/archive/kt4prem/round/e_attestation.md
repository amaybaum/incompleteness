**Candidate `E`: execution evidence (not a designation).**

Executed under the owner's authorization of C1 → S1 → S2 from the designated `F` `7ae032174699190086f1e54b7adb7aeb1a80a726` (designation recorded in comment 6087571713). Every acceptance gate below passed; nothing was retried or repaired.

**The chain** — each commit SSH-signed, GitHub verification `valid`, with a single parent:

| stage | commit | tree | delta from the previous commit |
|---|---|---|---|
| `F` | `7ae032174699190086f1e54b7adb7aeb1a80a726` | `aed3b1c6bdad1ff93b35dff393e74d735e764601` | the preregistration (blob `708feac0`); parent `D` `bcbc516f` |
| C1 | `2bf1c4863d6b63e386de506c312558b5fc7ae5cf` | `9471b670385166124eb4283c4b8fe78ff5c631ac` | `controls.py`, blob `7a691bca95232e1dbe289f57d8b9e458b9732b76` |
| S1 | `a14f2e731dfa855d4bf9fc4faa531488074bbadd` | `dd3acc6e51b86eaf15ecdf1829c88b77bec1affb` | probe `5609d96a`, independent check `94159768`, workflow `6207ec57` |
| S2 = candidate `E` | `86f26c87c750601583f382ed00baeb8fee32ef26` | `c08a50d1ea74aa1b3dd9424838238dc6ab3481fc` | `result.md`, blob `815633d8e526bbc81b468494d8f2fe00db6746d8` |

- The C1 and S1 trees are the predicted trees computed from `F`'s preregistration (`9471b670`, `dd3acc6e`). S1's tree is the predicted execution tree `df5d6199` with `F`'s revision of the preregistration in place of the drafting revision, and no other difference.
- `delta(D, E)` is exactly the six governed paths: the three record files, the two scripts and `.github/workflows/verify.yml`. The preregistration, `controls.py` and both scripts are unchanged from their frozen blobs.
- `claude/kt4-prem-1` is at exactly `E`; `main` is at `D`.

**Controls** (executor evidence under §A.40):
- C1: the `controls.py` blob is the frozen blob; `controls.py --self-test` passes 47 checks.
- S1: `controls.py check S1 --freeze F` passes 12/12; `--self-test` passes 47; `verdict S1` prints the seven positive tokens with both summary lines.
- `E`: `controls.py check E --freeze F` passes 14/14, the verdict and phrase controls on the result note among them; `--self-test` passes 47; `verdict E` prints exactly:
  ```
  Q1-CL   CLOSEDNESS-FOIL-VERIFIED
  Q1-MAX  MAXCONE-MODEL-VERIFIED
  Q1-IND  INDEPENDENT-REPLICATION-VERIFIED
  Q1-MAP  COUNTERMODEL-MATRIX-VERIFIED
  Q1-NEC  CLASSIFICATION-STEPS-VERIFIED
  Q2      PAIR-ROUTE-GAP-VERIFIED
  Q3      SOURCE-MAP-CITATIONS-VERIFIED
  kt4_prem1_probe: OK -- 79 checks
  FINAL: 124 exact checks, 0 failed; claims AGREE
  ```
- The V3 control-plane, T1 and execution predicates of `tools/v3_verifier.py` at `D`, run on `F`…`E`, report nothing.

**Exact-head run at S1:** [37979649705](https://github.com/amaybaum/incompleteness/actions/runs/37979649705), `workflow_dispatch`, attempt 1, `head_sha` exactly S1, conclusion `success`; all 33 jobs succeeded, each with `head_sha` S1.
- KT4-PREM-1 shard (job 113986613985): 79 `PASS` lines, no `FAIL`, `kinds: identity 38, witness 21, enumerate 3, source 7, sample 2, countercontrol 8`, `kt4_prem1_probe: OK -- 79 checks`; then 124 `  ok   ` lines, no `  FAIL `, the fourteen frozen verdict rows in order (`H (KT4Core)` holds for `M_cl` among them) and `FINAL: 124 exact checks, 0 failed; claims AGREE` with its timing field. The output matches a local run line for line (the independent check apart from its timing fields).
- Mathlib bridge (job 113986613263): `Build completed successfully (3643 jobs)`; release gate PASS on all 21 steps (`lean-axioms` 5860, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 42 receipts hold).
- Lean kernel check (job 113986613581) and probe aggregate (job 113993634941, `kt4prem1=success`) succeeded.

**Exact-head run at `E`:** [37982199559](https://github.com/amaybaum/incompleteness/actions/runs/37982199559), `workflow_dispatch`, attempt 1, `head_sha` exactly `E`, conclusion `success`; all 33 jobs succeeded, each with `head_sha` `E`.
- KT4-PREM-1 shard (job 113995244357): 79 `PASS` lines, no `FAIL`, `kt4_prem1_probe: OK -- 79 checks`; then 124 `  ok   ` lines, no `  FAIL `, the fourteen frozen verdict rows in order and `FINAL: 124 exact checks, 0 failed; claims AGREE` with its timing field. As at S1, the output matches a local run line for line (the independent check apart from its timing fields).
- Mathlib bridge (job 113995244162): `Build completed successfully (3643 jobs)`; release gate PASS on all 21 steps (`lean-axioms` 5860, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 42 receipts hold).
- Lean kernel check (job 113995243479) and probe aggregate (job 114001368180, `kt4prem1=success`) succeeded.

**Pull-request runs** (synthetic merges with `main`; supplementary, not attestations): at S1, 37979649037 `success` (18 jobs succeeded, A42 matrix skipped); at `E`, 37982207491 `success` (18 jobs succeeded, A42 matrix skipped).

**Discrepancies:** none in the evidence: every SHA, tree and blob matches its prediction, and every gate passed at the first attempt. Two notes:
- Besides the factual placeholders (#806, `F`, the preregistration blob, run 37975083454, comment 6087571713, C1, the controls blob, S1, run 37979649705 and job 113986613985), the result note's wording differs from its draft in non-frozen places only. As proposed before execution, its last two evidence lines state the controls result "at this commit" (`controls: OK -- 14 checks`) and the S1 run, because a commit cannot carry its own run; for the same reason the probe's evidence line names the shard of the exact-head run at S1. The `F` line says the owner's designation "is recorded in comment 6087571713". The frozen earned reading, non-inference rule, tokens and summary lines are unchanged: the V and PH controls pass.
- The PR description still describes the state at `F` ("no C1, S1 or S2 exists"); it has not been edited.

**Verification layers.** The probe and the independent check are exact computations, not Lean kernel proofs; no countermodel is kernel-checked. The independent exact verification of `H` for `M_cl` is computational evidence, not a Lean kernel proof of that construction. The written classification argument for `hcl`, with its one standard input from Lie theory, is not kernel-checked. `kt4_forward_ie1` is kernel-checked in a design run and is not certified. The round validates the dependency audit; it does not establish the full equivalence theorem.

**Not done:** no `E` designation, no reconciliation, no `Q` or receipt, no merge, no change to `main`, the ROADMAP, the manuscripts or any Lean module. Whether `Q`'s receipt needs an owner-authored, footer-less designation comment for `F` is open and is not assumed here.

`E` is not designated. Designation is the owner's.

---
_Generated by [Claude Code](https://claude.ai/code)_
