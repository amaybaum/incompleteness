# Verifier round V3-14 — retirement: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #746. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/V3-14.json`, and on the pull request.

- **`D`** — `378073fa9c3ad7a5c6327aa0163dec3619a40d84`, the head of `main` after `V3-13`'s landing,
  certified by push run 36201832097.
- **`F`** — `d0dde3a9efe2e424a0d32fce4e2bed9564a73674`, whose only parent is `D` and which adds the
  preregistration alone, blob `b7a763aeae2270c29e540bce430ddae3aa2abad7`.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or `V2` certificate.

| target | outcome at `E` | predicted |
|---|---|---|
| `V314-0` | `F-DESIGNATED` | the same, strong |
| `V314-1` | `GUARD-RETIRED` | the same, strong |
| `V314-2` | `AUTHORITY-SWAPPED` | the same, strong |
| `V314-3` | `VERIFIER-SETTLED` | the same, strong |

`V314-4` to `V314-6` are measured at or after `E` and recorded in the receipt and on the pull
request.

***

## `V314-0` — `F`: F-DESIGNATED

The branch was held at `F` and the workflow dispatched on it. Run 36215374582 is a
`workflow_dispatch` run whose `head_sha` is `F`, and all six of its jobs are green:
- the guard reports 105 PASS and 0 FAIL, with its verdict map identical to `D`'s, tag for tag and
  in order;
- `Foundations probes` passes;
- the release gate passes 20 of 20, with `control-plane-lint` OK, `V2` authoritative OK with 0
  failures and `v3-receipts` holding on four receipts.

That run is `F`'s `check-run` attestation, recorded on the pull request in comment 5842973274. The
`pull_request` run 36215375425 on the same head is green on all six jobs as well. The owner then
designated `F` in comment 5842974310, which is `F`'s `owner-designation` attestation.

***

## The execution

Each stage commit took its expected blobs from the preregistration as it stands at `F` and refused
on any mismatch. Each commit has exactly one parent.

| stage | commit | what it does |
|---|---|---|
| 1 | `03a5f36b67f18fb41096f485c9ca7b2a94acfc65` | adds `retire.py`, `messages.json`, `headers.json`, `controls.py`, `preserve.py` and `ledger.json` to the record directory |
| 2 | `ba1743e44ff922350077d25bcc0b199a4430bd0f` | the guard, written by `retire.py` |
| 3 | `7a5b038880a0b120ee85dad507ee6578f8377d29` | `legacy-records` in; `V2`, the control-plane tools and the diagnostics job out; `v3-self-test` and `v3-corpus` in; the depth-1 probes checkout |
| 4 | `f6c71279191ee6de0cc2206ec43659781f1178c0` | the verifier, its corpus and the specification |
| 5 | `115866033a4412e2485a7ebae85fd22de0ceec9b` | `AGENTS.md` and `verification/README.md` |

Every one of the twenty-one stage files has its frozen blob. This note, whose only parent is the
stage 5 commit, is `E`.

***

## `V314-1` — the guard: GUARD-RETIRED

- **`C1`:** the six record-directory files have their frozen blobs; `controls.py --self-test`
  prints `controls: self-test OK`.
- **`C2`**, the transformation: `retire.py`, run at the stage 1 commit under CPython 3.11.15,
  printed the five frozen lines:
  - `1616 predicates retired, 1610 as the census classes them and 6 by the amendment; 2486 retained`;
  - `structural rows: 15 removed with the emptied checks, 85 kept`;
  - `2 statement(s) kept inside surviving module-level blocks`;
  - `91 checks remain`, with the 14 emptied checks named;
  - `retained predicates missing: 0`.

  The ledger it wrote is `ledger.json` byte for byte. The guard has blob
  `8dad60d0aac870fced7deeec44c0dbdfcb3d45de`, 14,816 lines, and compiles.
- **`C2`**, the preservation checker: `preserve.py` holds on every check.
  - `L1` and `L2`: 556 splices, and the guard at `D` with them applied is the stage 2 guard.
  - `S1`: 1,616 predicates retired and 2,486 retained.
  - `S2`: 257 retained functions untouched.
  - `S3`: of 1,635 control-flow statements, 1,228 removed with their governing block.
  - `S4`: the ten regression sites preserved.
  - `S5`: 452 surviving module-level blocks with no dead code removed from them.
  - `S6`: 49 removed in-place changes, none to an object a survivor reads.
  - `S7`: 2,088 removed bindings, none still resolved by surviving code.

  `preserve.py --self-test` prints `preserve: self-test OK`, all sixteen mutants failing as
  required.
- **`C2`**, the countercontrol: `controls.py v313`, on `V3-13`'s stage 2 commit
  `0811754da89dd5e3674ec913c0c89a24462a88fd`, finds `L1`, `L2`, `S1` and `S7` holding and `S2` to
  `S6` failing, with `S4` naming all ten sites, and prints `v313: the checker rejects V3-13's guard,
  naming all ten sites`.
- **`C2`**, the history control: `controls.py history` reports 56 files run by the probes job, all 56
  named, with 213 history sites at `D` and 0 at stage 2.
- **`C2`**, the amendment's controls, at their frozen outcomes:
  - `controls.py pc4s . D`: the four `R7-PC4S` rows hold; 35 files read, 34 of them legacy records;
    one directory listed; a one-byte change to `verification/seals/PC4.json` makes line 17854 fail.
  - `controls.py vacuity . <stage 2> D`: both predicates hold whatever the rest of the 1,610 guard
    says, and the three countercontrols fail.

## `V314-2` — the authority: AUTHORITY-SWAPPED

- **`C3`:** the four stage 3 files have their frozen blobs, and the manifest's blob at stage 3,
  `9e48bd31797e1673f03807e699a10ae4a0b960c7`, is `V3-12`'s.
  - `legacy_records_check.py` reports `303 record(s) in 75 closed namespace(s), all intact` at
    stage 3 and `manifest-absent` at stage 2.
  - The same commit deletes `tools/certificate_verifier.py`, `tools/control_plane_base_check.py`,
    `tools/control_plane_lint.py` and the 90 files of `verification/certificates/conformance/`.
  - `controls.py callers` reports 0 at stage 3; the V3 self-test passes and the corpus reports
    `135 vector(s), exact and as expected`.

## `V314-3` — the verifier: VERIFIER-SETTLED

- **`C4`:** the eight stage 4 files have their frozen blobs; the V3 self-test passes; the corpus
  reports `140 vector(s), exact and as expected`; `controls.py callers` reports 0, with
  `ATTESTATION_DIR`, `AXES`, `SETTLED`, `_axis`, `_strong`, `_v3only` and `project` removed.
- **`C5`:** the two stage 5 files have their frozen blobs.

***

## Checks up to `E`

- **`C6`:** `--receipts` holds on four receipts at each of the five stage commits;
  `legacy_records_check.py` passes at stages 3, 4 and 5.
- **`C7`:** `git diff --no-renames --name-status D <stage 5>` lists 116 paths: 15 added, 7
  modified, 94 deleted. Each is governed by the block at `F` with its change authorized, and none
  is a record of the legacy-records manifest. This note adds one more path under the record
  directory.
- **`C9`:** the retained anchors hold.
  - `verification/README.md` keeps every string literal of the stage 2 guard it carried at `D`,
    the anchor "`.github/workflows/verify.yml` runs" among them. The slices `R7-A6P` and `R7-A6I`
    scan carry no over-reading by those checks' own scanner functions.
  - `.github/workflows/verify.yml` keeps `repertoire_lie` and has no `lake build OIBridge.` or
    `lake env lean OIBridge/` line.
  - `AGENTS.md` keeps the §A.35 heading and "updates the registry in the same commit".
  - `tools/release_gate.py` keeps `"lean-manuscript"`.
- **`C11`:** the tree of `E` with the preregistration and this note removed is
  `a31642acd97065d990c28d2b5a01e30501da452b`, the tree rehearsal 5 ran in both event modes.
- At stage 5, `duplicate_check`, `claims_check`, `artifact_placement_check`,
  `baseline_label_check`, `ci_gate_presence_test` and `voice_scope_test` pass.

`C8`, the dispatch run at `E`, and `C10`, the receipt commit, follow this note.

The scripts that applied the stages, rehearsed the round and checked the evidence, none of which is
landed:

| script | SHA-256 |
|---|---|
| `exec314.py` (applies the five stages, reading every blob back from the preregistration at `F`) | `7b5f5927072bf2ad50019d3d3dbc0daa97e2a6fd948e4d8c903263e988ebaf49` |
| `sim314.py` (the drafting-time rehearsal, 94 of 94 as predicted) | `b3cae16411be1fb712b79cf055f06aa2a3659f0e4b588d90bf8c7b38da3f6186` |
| `readme_control.py` (the `R7-A6P` and `R7-A6I` scanners, extracted from the guard) | `257129b0e9c973fc630faa458956056cd248a3b05b3a04975417f79562f62093` |
| `echecks.py` (`C7`, `C9` and `C11` at a commit) | `29c7d6b35a848b907f30427c2bd4754c2fba0d4a1352faa49e65e8ef7d96e4fa` |
| `cmpmap.py` (the guard's verdict map in a run's log against `D`'s) | `eb0fe81ed82e4ddd1281acb5fa76b6e44b239ef164e4ed846046b8472b7fbe11` |

***

## Discrepancies

None against the freeze.
