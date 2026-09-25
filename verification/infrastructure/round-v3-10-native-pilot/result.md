# Verifier round V3-10 — the first native V3 round: RESULT

Run under `AGENTS.md` §A.39 as a provisional V3 pilot, in one pull request, #741. This note is part
of `E`, so it records what was measured up to `E` (reading `R4`). The attestations for `E`, the
reconciliation and the verdict on `Q` are recorded in the receipt,
`verification/receipts/V3-10.json`, and on the pull request.

- **`D`** — `92683262a67190d7468a31a0c2f1dfdbc391778e`, the head of `main` after `V3-9`'s landing,
  certified by push run 36099602123 with all six jobs green.
- **`F`** — `19ab627b3c464935751332afe622a6c081eb774c`, whose only parent is `D` and which adds the
  preregistration alone, blob `01c6d6c35a627d79760a25f55b3a108856fda566`.
- **Shape** — non-sealing: no guard clause, seal, manifest record or `V2` certificate.

| target | outcome at `E` | predicted |
|---|---|---|
| `V310-0` | `F-DESIGNATED` | the same, strong |
| `V310-1` | `EXECUTED`; `README.md` blob `e8a5c383` | the same, strong |
| `V310-5` | `AUTHORITY-UNCHANGED` | the same, strong |

`V310-2`, `V310-3` and `V310-4` are measured after `E` and recorded in the receipt and on the pull
request.

***

## `V310-0` — `F`: F-DESIGNATED

The branch was held at `F` and the workflow dispatched on it. Run 36101255630 is a
`workflow_dispatch` run whose `head_sha` is `F`, and all six of its jobs are green: the guard
reports 105 PASS and 0 FAIL, with its top-level verdict map identical to that of `D`'s push run;
the release gate passes 19 of 19 steps, `V2` authoritative OK with 0 failures; the shadow job's
self-test passes and its corpus is 135 vectors, exact and as expected. That run is `F`'s
`check-run` attestation, recorded on the pull request in comment 5827926443. The owner designated
`F` in comment 5828013851, which is `F`'s `owner-designation` attestation.

***

## `V310-1` — the execution: EXECUTED

The two execution commits follow `F` linearly, each with exactly one parent.

1. `41bff5a04850de379285cc53e735abee7f657560`, whose only parent is `F`. The two frozen texts, read
   back from the preregistration as it stands at `F`, were applied to `verification/README.md`: its
   last two lines at `F` were the first text exactly, and were replaced by the second. The file's
   blob went from `55aba15ba3cf57a1fc35232534b6eed810abd920` to
   `e8a5c383c638c75d30324e77739c38c17d583358`, the predicted one. The commit changes that file
   alone.
2. This note, whose only parent is the first execution commit. This commit is `E`.

At the first execution commit `voice`, `claims`, `duplicate`, `artifact-placement` and
`control-plane-lint` pass, and `tools/v3_verifier.py` passes its self-test and reports
`CORPUS  135 vector(s), exact and as expected`.

The script that applied the change, not landed, is `exec310.py`, SHA-256
`d1cd33b7f359d8e00e70571bccf318f8705298aae2004c8f70d47b2d0d62b6bd`; the drafting-time rehearsal
behind the preregistration's measurements is `pilot10.py`, SHA-256
`325ce48fccec1a469e72073140f1fb1f79d78168820b3b61d287a4892d5fe45e`.

***

## `V310-5` — authority: AUTHORITY-UNCHANGED

At the first execution commit, `.github/workflows/verify.yml`, `tools/release_gate.py`,
`tools/certificate_verifier.py`, `verification/lean/edge_rigidity_probe.py`,
`tools/v3_verifier.py`, `tools/v3_receipt.py`, `AGENTS.md` and
`verification/infrastructure/v3/architecture.md` have their `D` blobs, and the trees
`verification/infrastructure/v3/conformance/`, `verification/seals/` and
`verification/certificates/` are unchanged. Neither `verification/receipts/` nor
`verification/v3-seals/` exists. `V1` and `V2` remain authoritative.

`git diff --no-renames --name-status D E`:

| status | path |
|---|---|
| `M` | `verification/README.md` |
| `A` | `verification/infrastructure/round-v3-10-native-pilot/preregistration.md` |
| `A` | `verification/infrastructure/round-v3-10-native-pilot/result.md` |

Each path is in the governed set: the two record paths in the record directory, and the one
execution path, modified.

***

## Discrepancies

None against the freeze.
