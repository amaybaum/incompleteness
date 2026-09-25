# Verifier round V3-11 — authority cutover: RESULT

Run under `AGENTS.md` §A.39 as it stood at `D`, as a provisional V3 pilot, in one pull request,
#742. This note is part of `E`, so it records what was measured up to `E`. The attestations for `E`,
the reconciliation, the verdict on the receipt commit and the gate's check of this round's own
receipt are recorded in the receipt, `verification/receipts/V3-11.json`, and on the pull request.

- **`D`** — `76a2c4dd82f0bf0dc8113256bf76bc02171e1337`, the head of `main` after `V3-10`'s
  landing, certified by push run 36109549145 with all six jobs green.
- **`F`** — `f5e316fedb9211f1973e8f5d9b2d40b145e68268`, whose only parent is `D` and which adds the
  preregistration alone, blob `eb51e0627a5dc1b37fa0b9d5cb8f9149806bcc3b`.
- **Shape** — non-sealing: no guard clause, seal, manifest record or `V2` certificate.

| target | outcome at `E` | predicted |
|---|---|---|
| `V311-0` | `F-DESIGNATED` | the same, strong |
| `V311-1` | `RECEIPTS-MODE-INSTALLED` | the same, strong |
| `V311-2` | `GATE-WIRED` | the same, strong |
| `V311-3` | `RULE-CUT-OVER` | the same, strong |

`V311-4` to `V311-7` are measured at or after `E` and recorded in the receipt and on the pull
request.

***

## `V311-0` — `F`: F-DESIGNATED

The branch was held at `F` and the workflow dispatched on it. Run 36112231466 is a
`workflow_dispatch` run whose `head_sha` is `F`, and all six of its jobs are green: the guard
reports 105 PASS and 0 FAIL, with its top-level verdict map identical to `D`'s; the release gate
passes 19 of 19 steps, `V2` authoritative OK with 0 failures; the V3 job's self-test passes and its
corpus is 135 vectors, exact and as expected. That run is `F`'s `check-run` attestation, recorded
on the pull request in comment 5830169084. The owner then designated `F`, which is `F`'s
`owner-designation` attestation.

***

## The execution

Each stage commit applied that stage's edits, read back from the preregistration as it stands at
`F`, to the files at its parent. Every text at the parent occurred exactly once, and every file
reached its predicted blob. Each commit has exactly one parent.

| stage | commit | path | blob |
|---|---|---|---|
| 1 | `37eb82764a4c0553ab0e26a865799a0ad6788c6d` | `tools/v3_verifier.py` | `b63add13bd519df3ec1d6a33323c2aac8eca611e` |
| 2 | `e17616b9371f4f8eb04b6219360d79fc7c0c3a5d` | `tools/release_gate.py` | `346192312603df4edf705e1d65c38e998af5afa3` |
| 2 | | `.github/workflows/verify.yml` | `fb2072b6cd8e323399d5748fd303d90c399a2cd6` |
| 3 | `91c49706c23f0a1c21a9ca7b94c3d90f14b34837` | `AGENTS.md` | `59896fa5738ae117bf6726a19c05156a78a17c0e` |
| 3 | | `verification/infrastructure/v3/architecture.md` | `ac9c3ec4aeb4294bda3efc671ac8e626f0bcc88f` |
| 3 | | `verification/README.md` | `e1bbd08aa68c50812fd56cd78f48b9fea2121202` |

This note, whose only parent is the stage 3 commit, is `E`.

***

## `V311-1` — the verifier: RECEIPTS-MODE-INSTALLED

At the stage 1 commit:

- **`C1`:** `--self-test` passes; `--corpus` prints `CORPUS  135 vector(s), exact and as
  expected`.
- **`C2`:** `--receipts` on the stage 1 commit exits 0 and prints
  `RECEIPT  verification/receipts/V3-10.json  Q 4a6e67e4cb097ae49d4e2d9f303b29c3b66ea952  HOLDS`
  and `RECEIPTS  1 receipt(s), all hold`.
- **`C3`:** `--receipts 92683262a67190d7468a31a0c2f1dfdbc391778e` exits 0 and prints
  `RECEIPTS  0 receipt(s), all hold`.
- **`C4`:** `--receipts HEAD` exits 2 and prints `v3_verifier: refused (input:not-an-object-id)`.
- **`C5`:** on a child that rewrites `V3-10.json` with its execution delta digest zeroed,
  `--receipts` names the child as the receipt commit and reports it `FAILS` with
  `s10:q-parent-not-landing-object, s4:execution-delta-digest, s9:landing-base`, ends
  `NOT ALL HOLD` and exits 1.
- **`C6`:** on a child that adds `verification/receipts/notes.txt`, `--receipts` reports that path
  `FAILS  s10:receipt-path` and exits 1.
- **`C7`:** in a depth-1 clone, `--receipts` prints
  `RECEIPTS  UNDECIDABLE  undecidable:shallow-repository` and exits 1.
- **`C8`:** the three scratch mutants exit 0 on at least one of `C5`'s and `C6`'s commits: the
  verdict ignored exits 0 on `C5`'s; the non-receipt path accepted exits 0 on `C6`'s; the exit
  status dropped exits 0 on both.

***

## `V311-2` — the gate and the workflow: GATE-WIRED

At the stage 2 commit:

- **`C9`:** the release gate's `v3-receipts` step, run alone with every other step stubbed, prints
  `PASS  v3-receipts      RECEIPTS  1 receipt(s), all hold`; `tools/ci_gate_presence_test.py`
  passes; the guard's conditions on the workflow and the gate hold (the `Certificate verifier` job
  in shadow mode and never authoritative, the `certificate-verifier` authoritative step, the
  `lean-manuscript` step, `repertoire_lie`); the `Mathlib bridge` job checks out with
  `fetch-depth: 0`; the job is named `V3 verifier diagnostics` and `V3 shadow verifier` is gone.
- **`C10`:** with the stage 2 files on `C5`'s child, the step prints
  `FAIL  v3-receipts      RECEIPTS  1 receipt(s), NOT ALL HOLD` and the gate exits 1.

***

## `V311-3` — the rule: RULE-CUT-OVER

At the stage 3 commit:

- **`C11`:** `voice`, `claims`, `duplicate`, `artifact-placement` and `control-plane-lint` pass.
- **`C12`:** the guard's own tests of `AGENTS.md` for `R7-SI2` and `R7-SI3`, taken from the guard
  file, hold on the new `AGENTS.md`, and the `R7-MSP` phrases are present.
- **`C13`:** `AGENTS.md` has one `## §A.39 ` heading, and neither `provisional V3 pilot` nor
  `Provisional native` remains in it.

***

## Scope and unchanged state up to `E`

`git diff --no-renames --name-status D E`:

| status | path |
|---|---|
| `M` | `.github/workflows/verify.yml` |
| `M` | `AGENTS.md` |
| `M` | `tools/release_gate.py` |
| `M` | `tools/v3_verifier.py` |
| `M` | `verification/README.md` |
| `A` | `verification/infrastructure/round-v3-11-authority-cutover/preregistration.md` |
| `A` | `verification/infrastructure/round-v3-11-authority-cutover/result.md` |
| `M` | `verification/infrastructure/v3/architecture.md` |

Every path is in the governed set. At `E` the preregistration keeps its `F` blob. The guard
`verification/lean/edge_rigidity_probe.py`, `tools/certificate_verifier.py`,
`tools/v3_receipt.py`, `tools/control_plane_lint.py`, `tools/control_plane_base_check.py`, the
conformance corpus, `verification/seals/`, `verification/certificates/`, `verification/receipts/`,
`papers/` and `book/` keep their `D` blobs; no Lean file changes and `verification/v3-seals/` does
not exist.

The scripts that applied the stages, ran the checkpoints and rehearsed the round, none of which is
landed:

| script | SHA-256 |
|---|---|
| `exec311.py` (applies one stage's edits, read back from the preregistration at `F`) | `fec96e275bcf8ec81241af5256da01d481c98ed090bef28f5ee3f14e1377f332` |
| `ctl311.py` (runs one stage's checkpoint at its commit) | `9b898fff9bc5d729ac42847df8560027376e9158022d715e25448bac8a91ab60` |
| `edits311.py` (the edits, as rendered into the preregistration) | `6bf6da9df245c2ffb8d22cd41c58a78d0c4035a81a8f560c2f5974dd48f9563a` |
| `sim311.py` (the drafting-time rehearsal) | `c768939ef184711b87b393d30c8566ea9dcc51edb3f23fc659cb1a0f76272372` |
| `render311.py` (renders the preregistration) | `ef8d62f464a98b85685e0de82261f7805810e15cda8a317aff37906583eb3f59` |

***

## Discrepancies

None against the freeze.
