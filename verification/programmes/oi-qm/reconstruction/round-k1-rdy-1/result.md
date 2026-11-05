# K1-RDY-1: execution record

**Status: execution in progress (WIP / UNVERIFIED).** This file is the round's execution log and result note
(architecture `K1`). It is written linearly from `F` and records only what has been done. Nothing in it is a
designation of `E`, a receipt, or a promotion of any scientific conclusion.

## 1. Execution log

### 1.1 Gate-3 authorization (base line 252)

amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6658964414 (2026-11-05T13:16:45Z):

> I accept the focused feasibility review in #1031 c.6658841280.
> **Q1: Decline exhaustive handwritten enumeration.** Writing out all 156 cycles and evaluating 1,024 states manually is still enumeration. Calling it a paper derivation does not change its nature. Do not authorize that exhaustive stage under the current F.
>
> **Gate 3 — Limited execution approved.** Authorize the paper-only work permitted by the frozen sequence: 1. Evaluate all 11 S0 controls first. 2. If S0 passes, evaluate P0 through G1–G7. 3. Complete the required independent written derivations and adversarial review for any positive P0 row. 4. Stop before the P1 exhaustive member stage.
> If S0 produces VOID[stage], follow the frozen stage-void procedure instead.
> If execution reaches P1 and the required per-member information cannot be established without unauthorized enumeration, use the **S12 halt procedure**. Do not fabricate member rows, issue a class token from an incomplete list, or manufacture E.
> **P3 must not be evaluated as a completed stage of this frozen round before P1.** Its paper analysis can be proposed separately.
>
> **Permitted tools and writers.** Replace `gh api` A4 reads with GitHub MCP pull-request reads, comparing the same six historical heads. Permit JSON syntax and A9 schema/key-set validation only. No model calculations or enumeration through JSON tooling. Designate `writer-k1rdy1-exec` as the sole branch committer. Use `writer-k1rdy1-d2` for independent second derivations and `writer-k1rdy1-adv` for adversarial notes when required. W2 independently derives the relevant hypotheses. W1 commits delivered files byte-identically, recording their provenance and hashes. Maintain one branch writer at a time and preserve the frozen F control plane.
> Authorized tools are limited to the paper procedures and static repository, verification and administrative tools enumerated in the reviewed gate-3 plan, with the MCP substitution above. No scientific enumeration, CAS, scripts operating on model states, new workflow dispatch or new execution path is authorized.
>
> **Next round — Option C.** Authorize **planning and drafting only** for a new, separately reviewed round that permits exact computational treatment of P1. It must have a new D, a preregistered enumeration procedure, full countercontrols, independent verification and separate F and execution authorizations. Do not modify K1-RDY-1's frozen F or retroactively broaden its execution authorization.

The plan it refers to is #1031 comment 6658598399; the feasibility review is #1031 comment 6658841280.

### 1.2 The frozen control plane

- `D` = `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be`.
- `F` = `d9b3de012e393262adb20f91ad49627bad48de43`, designated by the owner in #1031 comment 6658423367
  (2026-11-05T12:50:29Z), with `verify.yml` run 42026370642 (`workflow_dispatch`, `head_sha` = `F`, 40 of 40 jobs
  successful) as its check-run.
- Every execution commit is a single-parent descendant of `F` and changes only files in this record directory.
  `preregistration.md` and `amendments/` are not changed after `F` (architecture `G7`).

### 1.3 Drafting log (A6)

The drafting log of this round is the commit history `D..F` of branch `round/k1-rdy-1-20261105` with the comments on
its pull request, PR #1126:

| Commit | Content |
|---|---|
| `6f26bb1bf7ea97f532f6c7add5eae70c10d904b1` | the #1114 drafts carried byte for byte |
| `dfe80bc16718f61137a7964d5f6b4dc9e6fb0152` | the drafts updated where `main` had moved |
| `52ae69fb9731901dac8af228fbe1f930adc23fd1` | R1–R5 of review c.6656052333 under #1031 c.6656166518 |
| `9fa37d0a1aa69e7cebcced971b6fb627e8724d96` | F1/F2 of delta review c.6656432806 under #1031 c.6656645169 |
| `d9b3de012e393262adb20f91ad49627bad48de43` | A10's third recording item under #1031 c.6657384912 (`F`) |

PR #1126 comments: reviews 6656052333 (with correction 6656066995), 6656432806, 6656892864 and 6657687217; checkpoints
6656280750, 6656700538 and 6657426112; the exact-head verification record 6658263188. The drafting log lists reads,
paper derivations and the repository's static checks only.

### 1.4 Writers and instruments

- **W1, executor and sole branch committer:** `writer-k1rdy1-exec`. Every derivation file below records its author
  or producing session, its access to other derivations, and its dependencies (A10's three items).
- **A4 instrument:** the GitHub MCP pull-request read (`pull_request_read`, method `get`), field `head.sha`, for
  pulls 1009, 1023, 1011, 1003, 918 and 1025, as the gate-3 authorization directs in place of `gh api`.
- **Gate table:** JSON syntax and A9 schema/key-set validation only.

### 1.5 A4: referenced historical heads at the start of execution

Read between 2026-11-05T13:20:43Z and 2026-11-05T13:21:46Z with the instrument of §1.4, and compared with A4's table
(read there at 2026-11-05T11:58:40Z):

| Pull | `head.sha` read | A4 table | Match |
|---|---|---|---|
| 1009 | `d4a80fc871473285a7c848a4984940d52817ff8c` | `d4a80fc871473285a7c848a4984940d52817ff8c` | yes |
| 1023 | `af1e9be2ceabd5f6181b8d56b537b7ce1a4a3bba` | `af1e9be2ceabd5f6181b8d56b537b7ce1a4a3bba` | yes |
| 1011 | `947761dd40c17e4fdedcd8972a0b4e53e8bfba42` | `947761dd40c17e4fdedcd8972a0b4e53e8bfba42` | yes |
| 1003 | `0efd67a630fc80ac55fde1ca49fe8c5cbdbf10c3` | `0efd67a630fc80ac55fde1ca49fe8c5cbdbf10c3` | yes |
| 918 | `44236326976d2c9ad743f52595365b64ceb86d35` | `44236326976d2c9ad743f52595365b64ceb86d35` | yes |
| 1025 | `e02544d54b365b6a123ee284bd16442fb617c0b2` | `e02544d54b365b6a123ee284bd16442fb617c0b2` | yes |

No mismatch.

### 1.6 Computation (A11 item 3)

No computation was performed. No tool, program, script, notebook, computer-algebra system or other machine
computation was applied to the model, its states, cycles or measures. Each derivation under `derivations/` was
written by hand by the session its header names. The tools used were: `git` reads, `sha256sum` of the protected
lines, `grep`, the repository's static checks, JSON syntax and A9 key-set validation of `gate-table.json`, and GitHub
MCP reads. Signed: `writer-k1rdy1-exec`, for every file it wrote.

This statement is a declaration by the executor. By itself it is not independent proof that no computation occurred
(A11).
