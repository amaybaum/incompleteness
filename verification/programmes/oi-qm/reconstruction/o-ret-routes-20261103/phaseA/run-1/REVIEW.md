# O-RET Phase A, run 1: independent result review

Reviewer: independent result reviewer (read-only). Date: 2026-11-04.
Method: host API records (public REST), the downloaded artifact and logs (preserved, unmodified), and frozen
inputs read with `git show 49f0bd41:<path>`. The frozen §4 decision rule was re-applied by a separate script
to the recorded JSON fields only. No workflow was dispatched, re-run or cancelled, and no tool function or
physics computation was run.

## VERDICT: CONFIRMED PASS

All four frozen PASS signals hold, and an independent re-application of the frozen rule found 0 mismatches across 49/49 tuples.

## 1. Frozen PASS rule (PREREG-PHASE-A.md at F = 49f0bd41, blob 11492996)

Lines 483–487:
> **PASS.** A run passes iff all four of these hold:
> - the host's conclusion for the Phase A job is `success`;
> - the job's check step exits 0;
> - `summary.json` has `verdict = PASS`;
> - the `verdict_text` regenerated from `summary.json` equals the stored one byte for byte.

Lines 489–498: the reviewer reads the job conclusion from the host API. Within a pass every tuple's row and
every compared field equal their frozen values. Any other combination is void. There is no partial pass and no rerun.
Lines 562–567: the verdict reads the exit status, the host job and step conclusions, and `summary.json`, and never log text.

## 2. Evidence table

| Check | Source | Result |
|---|---|---|
| Runs of `oret-phasea.yml` | API `workflows/oret-phasea.yml/runs` | total_count **1**: run 41813302146 |
| All runs at `71a07fa5` / on tool branch | API `runs?head_sha=` / `?branch=` | 1 / 1 (same run). No other workflow ran there |
| Run record | API `runs/41813302146` | run_number 1, run_attempt 1, previous_attempt_url null, event workflow_dispatch, head_sha 71a07fa579c4…, actor/triggering_actor amaybaum, conclusion success |
| Jobs | API `runs/…/jobs?filter=all` | total_count 1: `phase-a` (id 126517678385), conclusion **success**, attempt 1 |
| Steps | same | 15/15 success, including Launch guard (2), Record run identity (5), Self-test (7), Verify four frozen inputs (8), **Phase A check (9)**, Regenerate verdict_text + re-apply §4 (10), Marker PASS (11), upload (12) |
| Signal 1: job conclusion | API | success ✔ |
| Signal 2: check step exit 0 | step 9 conclusion success (bash `run:`, nonzero exit ⇒ failure); `summary.json` `exit: 0` | ✔ |
| Signal 3: `verdict = PASS` | `summary.json`; marker step 11 success | ✔ |
| Signal 4: verdict_text regenerated, byte-equal | step 10 success; `check.json` `verdict_text_regenerated_equal: true`; my own regeneration from the frozen template (PREREG l.542) is byte-equal | ✔ |
| Artifact | API `runs/…/artifacts` | 1 artifact, id 13312689701, `oret-phasea-out`, 87823 B, digest sha256:1eed06f6…117ac, not expired. Local zip sha256 matches |
| Logs zip | local | sha256 4308ebb9a61e2b16974e824c3da3abf158e6d2c47d2f670a687e1d2783be9ea0 |
| `summary.json` digest | local | sha256 1cdc055a7741d1a8b0d526095f0ce20168081a5b603d1d4b206ca5f2180cf394 |
| Artifact contents | local | 52 files = 49 tuple records (47 window/noext + `R1-readback`, `R3-readback`) + `summary.json`, `check.json`, `run-identity.json`. No unexpected file |
| run-identity.json | artifact | event workflow_dispatch; ref research/o-ret-phasea-tool-20261104; sha = confirm_commit = checkout_head = 71a07fa579c4c159cdc3b38fa13e3dc917bbd3d5; run_id 41813302146; run_attempt 1; F 49f0bd41c532…; all 5 checks true; launch_conditions_hold true |
| confirm_commit | run-identity + launch-guard env | equals the authorized `71a07fa579c4c159cdc3b38fa13e3dc917bbd3d5` |
| F constant | workflow `PHASEA_F` (l.39); `run.F` in summary and every record | 49f0bd41c5323d2191b580460c8703740dd01b30 |
| Workflow file | git | main 27dc3443 (#1087 merge) blob 4bcb9337 = tool branch blob 4bcb9337. The tool branch is still at 71a07fa5 |
| F → run commit | git | F is an ancestor of 71a07fa5. The diff F..71a07fa5 adds only the workflow, `phaseA/phasea.py` and `IMPLEMENTATION-NOTES.md` |

### Frozen inputs (blob ids)

| File | at F | at 71a07fa5 | summary `blob_at_F` / `blob_read` | every record |
|---|---|---|---|---|
| PREREG-PHASE-A.md | 11492996f061… | same | same / same | same |
| DESIGN-PULSE.md | 0c1205da34a8… | same | same / same | same |
| PHASEA-TUPLES.json | f915e7b9cc8a… | same | same / same | same |
| PHASEA-EXPECTED.json | f4773e70547a… | same | same / same | same |

Full ids: 11492996f061c5721f889b219514cb2eb6d7da9e, 0c1205da34a8d4da1e1d6a22b9eb634d9697d053,
f915e7b9cc8ab3ab8d3d640324c641743fe4a98e, f4773e70547af2c336e47fa704e02794c4199ca7.

## 3. Independent re-application (data only)

The script read the frozen `PHASEA-TUPLES.json` and `PHASEA-EXPECTED.json` from `git show 49f0bd41:` and the 49 records. It checked:
- `summary.tuples_evaluated` equals the frozen `order` sequence (1–49) exactly. The HC-SK orders 32–49 follow the frozen `(n_bits, k)` rule.
- `first_failure` null; verdict PASS; exit 0; `eps_star` "1/20"; `w_star`/`T_star` null; `tuples_frozen` 49; run = {F, 71a07fa5, attempt 1}.
- Per record, the identity fields equal the frozen tuple: schema `oret-phase-a/1`, id, order, mode, params, T, P, f, law and read_cells, plus the fixed strings (kappa, independence_law, support_conditioning, B_def, rd_test, access). `match` is true. `injective` is true for all 43 full / full+sequential tuples and null for the 6 sequential tuples, as PREREG §2.0 and §5 specify.
- **Every compared field for its mode equals PHASEA-EXPECTED exactly.** JSON equality covers every key set, every rational string and null.
- Each record's `comparisons` list and embedded `expected` agree with the frozen file, and each `summary.tuples[*]` entry agrees with its record.
- Every probability is a lowest-terms rational string matching the frozen regex. No floats appear.
- §4 was re-implemented from PREREG l.454–481 and applied to the recorded fields. The checks were:
  - the recurrence flags;
  - noext step 1, with T′ = null for I-9;
  - T′ = max(T, τ), and T′ = T when τ = inf;
  - the tick sets for W_T, W_T′, H_T and H_T′;
  - step 2: J-1 on H_T′;
  - step 3: TR iff G_status_Tprime = empty;
  - step 4;
  - step 6: ST with DIL∃ or the Lemma H bound, then SCH for 5 versus 6;
  - steps 7 and 8;
  - the Lemma H bound rebuilt from `eta` and `eps_max(t0+1)`;
  - η = 1 when G* is empty;
  - TR/EX only with an observed ε > ε*;
  - no flagged tuple in row 5 or 6.
- The reapplied row equals the frozen expected row, and the tool's `reapplied_row`, for 49/49 tuples.
- Frozen-input consistency: the HC-SK expected values (ε, TV, w, w_chg, η, bound, τ, T′, D) equal the PREREG §3.3 formulas for all 18 tuples. The rows equal the PREREG §3.2/§3.3 tables.

**Mismatches: none (0).**

## 4. Structured signals (§A.44)

The PASS rests on four structured signals: the host job and step conclusions (API), `summary.json`, `check.json` (schema `oret-phase-a-check/1`, all six checks true) and the per-tuple schema files. No log text is needed.

Flag (diagnostic only, not a defect): the self-test count **33/33** (`"ok": true` ×33, `"ok": false` ×0, `"self_test": "pass"`) appears only in the step-7 log. The self-test JSON is not in the artifact. Structurally, the evidence is the step-7 conclusion success. This is adequate, because the self-test is not one of the four PASS signals.

## 5. Control validity

The controls are not vacuous. Ten distinct row codes occur:

| Row | Count | Tuples |
|---|---|---|
| 1 (RS) | 6 | HCP-h, SC, R1-T4, R2 ×2, R3-T5 |
| 2a (TR) | 6 | |
| 2b (EX) | 14 | |
| 3 | 1 | MD-xor |
| 5 | 7 | |
| 6 | 4 | |
| 7 | 1 | CX-4b |
| 8 | 3 | |
| I-3 | 2 | |
| I-9 | 5 | TS ×2, TM ×2, TMP noext |

The rejecting and inconclusive rows (1, 2a, 2b, 3, 7, 8, I-9) make up 36 of the 49 rows. Boundary cases are present:
- SC has ε(t₀+1) = 1/20 = ε* (the exact `≤`) and write_min_eps 1/20, and it is rejected only by J-ii.
- HC-SK crosses the boundary at k = 4/5/6: row 8 against row 5 against 2b.
- Recurrence flags are nonempty for R1-T4 and R3-T5.
- MD-xor has sweep 1/2 against write_min_eps 0.

Coverage limits are stated at F (PREREG §9) and are unchanged by the run:
- row 4 (I-8) is a declared constant and is not exercised;
- row 3 is reached only via ε > ε*;
- there is no J-1 failure in H_T′∖H_T and no row-1 branch of noext step 1;
- exit 4 is exercised in the self-test only.

Logs contain no `error`, `Traceback`, `skipped` or `"ok": false`. The warnings are runner-level only:
- Node.js 20 deprecation for the pinned checkout, setup-python and upload-artifact actions (forced onto Node 24);
- `punycode` / `url.parse` DeprecationWarnings from node;
- a git `hint:`.

None of these is in the verdict path.

## 6. Scope

- One job, `phase-a`. The 49 evaluated ids are exactly the frozen §3 set.
- There is no Phase B, K1, nonlinear or native-dynamics tuple. `w*`/`T*` are null.

**What PASS establishes.** On the frozen toy control set, under the §2 conventions (ε* = 1/20; preparation conditioning μ(·|σ∈P); B = Par(A)∖A; DESIGN decoders), the tool's exact enumeration reproduces every frozen hand-derived value. The implemented §4 precedence also assigns every frozen expected row. This calibrates the tool against frozen expected rows and sits on the consistency axis (§A.23).

**What PASS does not establish:**
- any retention mechanism, or O1, O3 or O4;
- that the criteria classify correctly outside the control set;
- anything about native OI dynamics, K1 or nonlinear rules;
- any premise adoption, claim promotion or correctness-band movement.

All verdicts are conditional on the declared preparation sets P (owner interpretation (b), #1032 c.6623962802).

## 7. Provenance notes (§A.42)

- F (49f0bd41) and the run commit (71a07fa5) are **not reachable from `main`**. They live only on `research/o-ret-phasea-tool-20261104` and `research/o-ret-routes-20261103`.
- `summary.json` and the artifact (retention 90 days) are provenance until they land on `main`. PREREG §7 says the same.
- Before any branch deletion, the frozen inputs, the tool and `summary.json` (with its digest) must reach `main` if a surviving claim rests on them.
- The owner's dispatch go is not yet recorded on #1032: the latest owner-decision comment, c.6627833402 at 09:52Z, lists it as a remaining gate. The record should quote it with author and time (§A.42 item 7).

## 8. Proposed record text for #1032

```
**O-RET Phase A, run 1: result (independent review).**

Owner authorization (chat, 2026-11-04 — author/time to be quoted): exactly one dispatch,
`oret-phasea.yml --ref research/o-ret-phasea-tool-20261104 -f confirm_commit=71a07fa579c4c159cdc3b38fa13e3dc917bbd3d5`;
scope Phase A only, the 49 frozen calibration tests.

- Run 41813302146 (run_number 1, attempt 1, workflow_dispatch); the only run of `oret-phasea.yml`.
- head_sha `71a07fa579c4c159cdc3b38fa13e3dc917bbd3d5`; F `49f0bd41c5323d2191b580460c8703740dd01b30`.
- Artifact `oret-phasea-out` id 13312689701, sha256:1eed06f6466d31f4aae1c307081c635b4727ae120bc66e8c0b52b60aefe117ac;
  `summary.json` sha256 1cdc055a7741d1a8b0d526095f0ce20168081a5b603d1d4b206ca5f2180cf394.
- Four frozen inputs: blob ids at F equal the bytes read (PREREG, DESIGN-PULSE, PHASEA-TUPLES, PHASEA-EXPECTED).
- Four-signal PASS (PREREG §4): job conclusion success; check step exit 0; `verdict = PASS`;
  regenerated `verdict_text` byte-equal. Verdict: **PASS**.
- Independent re-application of §4 to the 49 records: every row and compared field equals its frozen value; 0 mismatches.

Established: on the frozen control set and under the §2 conventions (ε* = 1/20, conditioning on P),
the tool reproduces the hand-derived values and expected rows — a calibration result on the consistency axis.
Not established: any retention mechanism; O1, O3, O4; classification outside the control set; anything
about native OI dynamics, K1 or Phase B; any premise or claim status. Correctness bands unchanged.
F and the run commit are off `main`; these outputs are provenance until they land there.

---
_Generated by [Claude Code](https://claude.ai/code)_
```
