# K1-RDY-1: execution record

**Status: halted (architecture `S12`).**
- S0 and P0 are evaluated (§§2–3).
- P1 and P3 are not evaluated (§§4–5).
- No `E` is designated and no P1 class token is issued. The halt is recorded in §8.

This file is the round's execution log and result note (architecture `K1`). It is written linearly from `F` and records
only what has been done. Nothing in it is a designation of `E`, a receipt, or a promotion of any scientific conclusion.

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

### 1.6 A4: referenced historical heads at the P1 boundary

Read between 2026-11-05T13:29:54Z and 2026-11-05T13:30:05Z with the same instrument. All six `head.sha` values are
identical to the table of §1.5 and to A4's table, so there is no mismatch. A `get_commits` call made in the same
interval returns a pull request's commit list, not its head, and is not counted as a reading.

### 1.7 Computation (A11 item 3)

No computation was performed. No tool, program, script, notebook, computer-algebra system or other machine
computation was applied to the model, its states, cycles or measures. Each derivation under `derivations/` was
written by hand by the session its header names. The tools used were: `git` reads, `sha256sum` of the protected
lines, `grep`, the repository's static checks, JSON syntax and A9 key-set validation of `gate-table.json`, and GitHub
MCP reads. Signed: `writer-k1rdy1-exec`, for every file it wrote.

This statement is a declaration by the executor. By itself it is not independent proof that no computation occurred
(A11).

## 2. S0: the 11 controls (base lines 186–187, 196–216)

Each control was derived by hand at its own instance, on the gate it tests, in isolation (§9). The outcomes are read
from `gate-table.json` (`controls`):

| Control | Gate under test | Outcome | Derivation |
|---|---|---|---|
| CC-ABS | G4 | pass | `derivations/S0-CC-ABS.md` |
| CC-EXACT | G4 | pass | `derivations/S0-CC-EXACT.md` |
| CC-SCOPE | G4 | pass | `derivations/S0-CC-SCOPE.md` |
| CC-LEDGER | G3/G4 | pass | `derivations/S0-CC-LEDGER.md` |
| CC-IMP | G2, G3 | pass | `derivations/S0-CC-IMP.md` |
| CC-IMP′ | G2(a) | pass | `derivations/S0-CC-IMP-prime.md` |
| CC-IMP″ | G2(a); T1; T2's no-image disjunct | pass | `derivations/S0-CC-IMP-dprime.md` |
| CC-PASS | G2(b) | pass | `derivations/S0-CC-PASS.md` |
| CC-T2 | G2(b) T2 | pass | `derivations/S0-CC-T2.md` |
| POS-X | G3, G4, G7 | pass | `derivations/S0-POS-X.md` |
| CC-BLIND | G4 | pass | `derivations/S0-CC-BLIND.md` |

All 11 controls pass, so VOID[stage] is not issued and row evaluation proceeds (base line 188). One reading is
marked in `derivations/S0-CC-IMP.md`: when both G2(a) and G2(b) flag, the subtype is taken from (a). Its grounds:
- §5.4 defines row tokens with a single subtype only; A2's set of subtypes is a field of the P1 class token, not of a
  row token.
- G2 decides (a) first (lines 126–135).
- CC-IMP's frozen pass condition, Z1-VOID[IMPORTED], is written for a fixture whose rule part names `E`, so T1 fires
  by construction.

CC-IMP's pass condition is attained under that reading. Lines 39–40 of `derivations/S0-CC-IMP.md` add that carrying
both subtypes would also attain it. No two-subtype row token is defined, so that remark is unsupported; the file is
left as executed, and this paragraph supersedes those lines.

POS-X is run in isolation (§9): its gates not under test (G1, G2, G5, G6) are not run, and its `Λ` is the fixture's
stated set.

The values recorded in the base from hand checks (HC-1, HC-A to HC-D) were not used as grounds (A6). Each pass
condition is decided by the derivation named.

## 3. P0 (base line 188; rows in `gate-table.json`)

Each row was derived by hand through G1–G7. The tokens are quoted from `gate-table.json` (`rows`):

| Candidate | Branch | Token | Derivation |
|---|---|---|---|
| P0 | B-pl | ABSENT[π_0; B-pl; H-cur (declared)] | `derivations/P0-B-pl-d1.md` |
| P0 | B-eq | ABSENT[π_0; B-eq; H-cur (declared), H-2s (declared)] | `derivations/P0-B-eq-d1.md` |
| P0 | B-ct | ABSENT[π_0; B-ct; H-cur (declared), H-2s (declared), H-ret] | `derivations/P0-B-ct-d1.md` |

P0's report is the tuple of these three branch tokens; no aggregate verdict is formed (line 184). No P0 row is
positive, so no second derivation or adversarial note was required (line 150; gate-3 authorization item 3), and
`writer-k1rdy1-d2` and `writer-k1rdy1-adv` were not engaged. The B-pl and B-eq rows are among the rows the base lists
as fixed in advance (lines 233–234); they record the rule's consequences and are not independent tests (line 238).

Two readings are marked in the P0 derivations:

1. **G5–G7 after a G4 token.** A row takes the token of the first gate that issues one (line 183). Here G4 issues
   ABSENT, so G5, G6 and G7 are recorded as `not-reached`.
2. **The `hypotheses` field of a row that stops at G4.** For these three rows the field holds the declaration's
   hypotheses and the §2 access labels that the token's access field names. It is not `Λ`, which is written at G5
   (lines 148–149). By line 56 and the recorded fields, `Λ` would add H-law (each row has `w_certified` false) and
   would not add H-sel (each row's `g2.hsel_content` is empty). No token carries `Λ` for these rows. The G5
   paragraphs of `derivations/P0-B-pl-d1.md` (lines 64–65), `derivations/P0-B-eq-d1.md` (lines 61–62) and
   `derivations/P0-B-ct-d1.md` (lines 60–61), which say that H-law and H-sel are not evaluated, are left as executed;
   this paragraph supersedes them.

## 4. P1: not evaluated

Execution stops before the P1 member stage.
- §5.3 and A9 require one row per member: `π_0` plus each cycle-uniform `u_c`, identified by its cycle's least state.
  §9 ("No post-selection") requires the cycle sizes to sum to `|S|`. Each row also needs per-member content (`sharp_w`,
  `weak`, `nb`, `g2.hsel_content`).
- Proposition CYC (`PROOFS.md` §2) gives the number of cycles and their lengths, not the cycles themselves.
- The gate-3 authorization (§1.1) declines the exhaustive member stage: "Writing out all 156 cycles and evaluating
  1,024 states manually is still enumeration. Calling it a paper derivation does not change its nature. Do not
  authorize that exhaustive stage under the current F." It directs: "If execution reaches P1 and the required
  per-member information cannot be established without unauthorized enumeration, use the **S12 halt procedure**."
- The owner's halt decision (§8.1) fixes the reason recorded for the halt: "P1 requires exhaustive evaluation outside
  the authorized paper-only scope."

Hence:
- no member row is written;
- no P1 class token is issued, and `class_tokens` in `gate-table.json` is empty;
- `E` is not designated.

The round is halted under `S12` (§8).

## 5. P3: not evaluated

The gate-3 authorization states: "P3 must not be evaluated as a completed stage of this frozen round before P1." No P3
row is written.

## 6. Operational-usefulness reports

None. No evaluated row is positive (lines 144–147).

## 7. Scope and non-claims

- The tokens of §3 are scoped to (`π_0`, branch, access, the fixed instance), as base §7 states (lines 220–230). No
  token states that a ready supply cannot exist.
- No P1 or P3 token is issued, so nothing here bears on K-17(a)'s class or on P3.
- Nothing here is physical sourcing of a ready state, access, renewal, memory, observer emergence or complete QM. No
  correctness band moves, and no manuscript, Lean or probe file is changed.
- Each derivation is a written paper derivation. None is a computational or kernel-checked result.

Every file below is in this record directory, has mode `100644` and is a written derivation in Markdown (A11):

- `derivations/S0-CC-ABS.md`
- `derivations/S0-CC-EXACT.md`
- `derivations/S0-CC-SCOPE.md`
- `derivations/S0-CC-LEDGER.md`
- `derivations/S0-CC-IMP.md`
- `derivations/S0-CC-IMP-prime.md`
- `derivations/S0-CC-IMP-dprime.md`
- `derivations/S0-CC-PASS.md`
- `derivations/S0-CC-T2.md`
- `derivations/S0-POS-X.md`
- `derivations/S0-CC-BLIND.md`
- `derivations/P0-B-pl-d1.md`
- `derivations/P0-B-eq-d1.md`
- `derivations/P0-B-ct-d1.md`

## 8. S12 halt

### 8.1 Owner authorization

amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6659415927 (2026-11-05T13:38:21Z), quoted
in the parts that govern this halt:

> I approve (a) the independent review now, followed by (b) a conditional S12 halt once that review passes.
>
> ### B. S12 halt — Conditionally approved
> If the independent review returns ACCEPT, or ACCEPT WITH CHANGES with all changes independently rechecked:
> - Re-read the six A4 heads through the authorized MCP interface.
> - Confirm that no material scientific dependency has changed.
> - Have the designated sole branch writer create W as a single-parent child of the last execution commit, changing only the permitted halt record.
> - Record the reason: P1 requires exhaustive evaluation outside the authorized paper-only scope.
> - Record the final A4 readings, all candidate heads and the exact authorization.
> - Preserve the reviewed S0/P0 outcomes, label the round **halted**, and explicitly state that P1 and P3 were not evaluated.
> - Do not designate E.
>
> Obtain an independent exact-head review of W.
>
> **If the S0/P0 review is blocked, identifies a material defect, or requires changes to frozen rules, stop and return for a new owner decision.**

The execution it halts was authorized by #1031 comment 6658964414 (2026-11-05T13:16:45Z), quoted in §1.1.

### 8.2 Independent review of the S0/P0 execution

An independent, read-only, model-authored review of the execution at `da1d939e52e71110008cd6534a672897c64c3339`
against `F`, by a reviewer that wrote none of the work under review, under part A of the decision above, returned
**ACCEPT WITH CHANGES**. Its report is recorded on PR #1126. Its findings:
- all 11 S0 controls pass on its own derivations, and the three P0 tokens are correct, including the values 153/160,
  1/256, 1/8, 1/2 and 1/4;
- there is no material scientific disagreement, no defect in S0 or P0, and nothing that requires a change to frozen
  rules;
- its requested changes are wording and record-accuracy fixes that change no outcome, value or token.

The requested changes are applied in this file only: the grounds of CC-IMP's subtype reading (§2), the scope of the
`hypotheses` field of rows that stop at G4 (§3), and the grounds of the P1 stop, which rest on the owner decisions
quoted in §1.1 and §8.1 (§4). §2 also states that POS-X's gates not under test are not run. The derivation files and
`gate-table.json` are unchanged from `da1d939e`. The independent recheck of these changes is part of the exact-head
review of `W` that §8.1 requires.

The S0 and P0 outcomes of §§2–3 are preserved unchanged.

### 8.3 A4: referenced historical heads at the halt

Read at 2026-11-05T13:46Z (UTC clock readings 13:46:10Z as the reads were issued and 13:46:12Z after the last returned)
with the instrument of §1.4:

| Pull | `head.sha` read | A4 table | Match |
|---|---|---|---|
| 1009 | `d4a80fc871473285a7c848a4984940d52817ff8c` | `d4a80fc871473285a7c848a4984940d52817ff8c` | yes |
| 1023 | `af1e9be2ceabd5f6181b8d56b537b7ce1a4a3bba` | `af1e9be2ceabd5f6181b8d56b537b7ce1a4a3bba` | yes |
| 1011 | `947761dd40c17e4fdedcd8972a0b4e53e8bfba42` | `947761dd40c17e4fdedcd8972a0b4e53e8bfba42` | yes |
| 1003 | `0efd67a630fc80ac55fde1ca49fe8c5cbdbf10c3` | `0efd67a630fc80ac55fde1ca49fe8c5cbdbf10c3` | yes |
| 918 | `44236326976d2c9ad743f52595365b64ceb86d35` | `44236326976d2c9ad743f52595365b64ceb86d35` | yes |
| 1025 | `e02544d54b365b6a123ee284bd16442fb617c0b2` | `e02544d54b365b6a123ee284bd16442fb617c0b2` | yes |

All six heads equal A4's table and the readings of §§1.5–1.6. No scientific dependency of the round has changed.

### 8.4 Candidate heads

Measured heads of this round, none of them certified as `E`:

| Commit | Role |
|---|---|
| `d9b3de012e393262adb20f91ad49627bad48de43` | `F` |
| `3efb92332daafe6103cc316d496d39b04e452e18` | execution commit 1: the execution log opened |
| `291925dacccc949bae57d465b932aac3fd8d1a25` | execution commit 2: S0 |
| `da1d939e52e71110008cd6534a672897c64c3339` | execution commit 3: P0 and the stop at P1; last execution commit and parent of `W` |

`W` is the single-parent child of `da1d939e` that adds this section and the changes listed in §8.2, and changes only
this file.

### 8.5 The halt

- **Status:** halted.
- **Reason:** P1 requires exhaustive evaluation outside the authorized paper-only scope (§4).
- **Evaluated:** S0, with all 11 controls passing (§2), and P0, with the three branch tokens of §3.
- **Not evaluated:** P1 and P3. No P1 member row is written and no P1 class token is issued; no P3 row is written.
- **`E`:** not designated.
- **Withdrawal invariant:** the round's `v3-governed-paths` block at `F` has `record` entries only, so the invariant
  constrains no path. The derivation files and `gate-table.json` lie within the record directory and are kept.
- Nothing here is a receipt, a reconciliation or a promotion of any scientific conclusion. The P0 tokens are scoped
  negative results as §7 states, not a general impossibility result.
