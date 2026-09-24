# Verifier round V3-6 — V3 final implementation conformance: RESULT

Executed on #735 from the certified execution base and from nothing else, under `AGENTS.md` §A.37:
the control plane #734, then this execution pull request, which also carries the landing.

- **`D`** — `a6efb46745e059c9c138cc7c420186521d331562`.
- **`B`** — `bace2e070c6e621c3314b9363ea56314b414f736`, the merge of #734. Its parents are `D` and
  the reviewed control-plane head `3f2e28459e63bddbce4fe01195375f4c8901aa69`, and its tree is that
  head's. Push run 36027800996 was green on all six jobs, the control-plane base check in mode `B`
  with 13 rows and 3 frozen blobs.
- **Preregistration** — blob `32c1169e5f4e5b0be451a7fe1ef5d35cdfd7596f` at `B` and at `E`.
- **Shape** — non-sealing, `E` → `L`, no `P`: no guard clause, manifest record or round
  certificate (reading `R8`).
- **Status** — COMPLETE: every target reached its passing outcome. For `V36-5` the
  repository-wide conditions (the guard, `V2`, the release gate) are established by the exact-head
  run on `E`, which the `E` certification record on #735 identifies; they were not run locally.

| target | outcome | predicted |
|---|---|---|
| `V36-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V36-1` | `G10-CONFORMS`; tool blob `db23329d` | the same, strong |
| `V36-2` | `G12-CONFORMS`; tool blob `5bd01380` | the same, strong |
| `V36-3` | `SELF-DESCRIPTION-CURRENT`; tool blob `21ea4097`, README blob `08cb7962` | the same, strong |
| `V36-4` | `CONTROLS-HOLD` | `CONTROLS-HOLD`, strong |
| `V36-5` | `SHADOW-ONLY` | `SHADOW-ONLY`, strong |
| `V36-6` | `SCOPE-HELD` | `SCOPE-HELD`, strong |

Every stage's tool blob and the README blob are the predicted ones, so no stage diverges from the
predicted replacement text, and there is no divergence for the owner's review. The controls show
that the tool implements what the vectors encode; they are not evidence that the settlements are
right (hazard `H1`).

The shadow verifier `tools/v3_verifier.py` now implements every settlement
`verification/infrastructure/v3/architecture.md` carries, and the corpus has no pending part. It
gates nothing. `V1` and `V2` remain authoritative. V3 is not operative.

***

## `V36-0` — the base: BASE-HOLDS

The execution branch was created at exactly `B`, after `B`'s push run was green, with `main` still
at `B`. At `B` the preregistration's blob is the frozen `32c1169e`, and `tools/v3_verifier.py`,
`verification/README.md` and `architecture.md` have the frozen blobs `883122c4`, `50c39016` and
`12cff3f2`. The control-plane base check in mode `B` holds at `B`: 13 rows and 3 frozen blobs, no
failure. At `B` the corpus held 116 vectors and `conformance-pending/` seventeen, and neither
`verification/receipts/` nor `verification/v3-seals/` existed.

***

## `V36-1` — `G10`: G10-CONFORMS

Stage 1, commit `0977cca56e79d43de5d9fbb2a26524a56d434277`, whose only parent is `B`. The frozen
sites `s1.1` and `s1.2`, read back from the preregistration as it stands at `B`, were applied to the
tool at `B`, and the six vectors of the frozen row moved from `conformance-pending/` into
`conformance/` unchanged.

- **Tool blob:** `db23329d43c0aeafac054a556a64f5a4c364dfcb`, the predicted one.
- **`C1`:** `CORPUS  122 vector(s), exact and as expected`.
- **`C2`:** each of `g10-reject-indented-opener`, `g10-reject-longer-backtick-fence`,
  `g10-reject-near-miss-in-amendment`, `g10-reject-opener-with-cr`,
  `g10-reject-opener-with-trailing-text` and `g10-reject-tilde-fence` runs not as expected under
  the tool at `B` and as expected under the stage-1 tool.
- **`C6`:** the self-test passes.

The commit changes the tool and moves the six vectors, and nothing else.

***

## `V36-2` — `G12`: G12-CONFORMS

Stage 2, commit `0940adb469c7a265c00495d6243bd7a64b77554e`, whose only parent is `0977cca5`. The
frozen sites `s2.1` to `s2.16` were applied to the stage-1 tool, and the eleven vectors of the
frozen row moved into `conformance/` unchanged.

- **Tool blob:** `5bd01380dd301bad6ddfc0569ec90369905ff881`, the predicted one.
- **`C1`:** `CORPUS  133 vector(s), exact and as expected`.
- **`C2`:** each of the eleven `g12-reject-` vectors runs not as expected under the stage-1 tool
  and as expected under the stage-2 tool.
- **`C6`:** the self-test passes.
- `conformance-pending/` holds no file at stage 2 and so does not exist in the tree.

The commit changes the tool and moves the eleven vectors, and nothing else.

***

## `V36-3` — the self-description: SELF-DESCRIPTION-CURRENT

Stage 3, commit `e3b6b4a244b67a10901141818bfee5c5e6143260`, whose only parent is `0940adb4`. The
frozen sites `s3.1` and `s3.2` were applied to the stage-2 tool, and the frozen README paragraph
replaced the paragraph at `B`.

- **Tool blob:** `21ea40977655d4a36c6e387b496ec5e353e9196b`, the predicted one.
- **README blob:** `08cb79621b1c0e85d4180d8a00081906f35f11f9`, the predicted one.
- **`C1`:** `CORPUS  133 vector(s), exact and as expected`.
- **`C6`:** the self-test passes.

The commit changes the tool and `verification/README.md`, and nothing else.

***

## `V36-4` — the controls at `E`: CONTROLS-HOLD

The result note changes no tool, so the tool at `E` is the stage-3 tool. Every run below is of the
committed tool, from the repository.

- **`C3`:** with one rule's behaviour taken out of the tool at `E`, exactly that rule's vectors run
  not as expected and every other vector of the corpus as expected:

  | rule taken out | its vectors | the others |
  |---|---|---|
  | near misses (`G10`) | 6, not as expected | 127, as expected |
  | the seal entry at `F` (`G12` 1) | 5, not as expected | 128, as expected |
  | the receipt names the seal record alone (`G12` 2) | 2, not as expected | 131, as expected |
  | no change to other rounds' state (`G12` 3) | 3, not as expected | 130, as expected |
  | each receipt commit's changes authorized (`G12` 4) | 1, not as expected | 132, as expected |

  With stage 1's sites reverted in the tool at `E`, its six vectors run not as expected and the
  other 127 as expected; with stage 2's sites reverted, its eleven vectors run not as expected and
  the other 122 as expected. No control was void.
- **`C4`:** `tools/v3_verifier.py --project B` at `E` gives output identical to the tool at `B` over
  the same subject: 68 lines, SHA-256
  `1113b183f8e51eda7a406d35e25b3104f7058e6459cb4a9587cd74263f94e279`. `V3-2`'s `census.json` still
  describes the shadow's comparison with `V2`.
- **`C5`:** `python3 tools/v3_verifier.py --mode shadow --subject <stage-3 commit>`, run from the
  repository, exits 0; its first line is the banner `v3_verifier shadow report -- SHADOW ONLY: this
  report gates nothing; V1 and V2 remain authoritative`; it prints the settled rules `K1`–`K4` and
  `G5`–`G12`, in that order, each once, the line `CORPUS  133 vector(s), exact and as expected` and
  the line `PROJECTION  cells 126`; and its last line is `v3_verifier: shadow report complete
  (corpus as expected)`. Neither the tool nor `verification/README.md` contains
  `conformance-pending`, `does not implement` or `remain unsettled`, and the README's paragraph is
  the frozen text. The shadow job of the exact-head run on `E` runs the same report at `E`.
- **`C6`:** the self-test passes at every stage's commit.

The scripts that ran the stages and the controls, neither of which is landed:

| script | SHA-256 |
|---|---|
| `exec36.py` (applies one stage's sites, read back from the preregistration at `B`, and runs `C1`, `C2`, `C6`) | `4c16730ad8461b38ebf7c953b8b3023271a46583b9dfe64b46a0992f23328d12` |
| `close36.py` (`C3`–`C6`, scope and chronology at the stage-3 commit) | `3524a6cd390bf2b11a23257b4340907b9d6267ec694a9573ada88b64cd3d546f` |

***

## `V36-5` — non-authority: SHADOW-ONLY

At `E`, `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`,
`verification/lean/edge_rigidity_probe.py`, `AGENTS.md`, `architecture.md` and the preregistration
have their `B` blobs. Neither `verification/receipts/` nor `verification/v3-seals/` exists, nothing
under `verification/seals/` changed, the shadow has no authoritative mode, and no required check
was touched.

The guard's verdict (105 PASS, 0 FAIL, with `D`'s verdict map), `V2` authoritative OK, the release
gate's 19 of 19 steps and the shadow job's self-test and 133-vector corpus at `E` are taken from
the exact-head run on `E`, not run locally.

***

## `V36-6` — scope: SCOPE-HELD

`git diff --no-renames --name-status B E`:

| status | path |
|---|---|
| `M` | `tools/v3_verifier.py` |
| `M` | `verification/README.md` |
| `A` | the seventeen moved vectors under `verification/infrastructure/v3/conformance/` |
| `D` | the seventeen files of `verification/infrastructure/v3/conformance-pending/` |
| `A` | `verification/infrastructure/round-v3-6-final-conformance/result.md` |

This is exactly the mutation budget: 2 modified, 18 added, 17 deleted. Nothing on the budget's
never-written list changes.

***

## Discrepancies

None against the freeze.

The executor records one event on the host, which no predicate reads. Between drafting and
execution the session's container was replaced, and the fresh checkout was a shallow clone. The
first run of stage 1's `C1` in it reported the three `s8-landed-` vectors
`UNDECIDABLE undecidable:shallow-repository`, as the tool must for a shallow repository. That was a
fact about the local clone, not the tool. The clone was deepened with `git fetch --unshallow`, the
uncommitted stage-1 edits were discarded, and stage 1 was applied again from `B`. Its checkpoint
then held as recorded above. The stage-1 commit was first created on the checkout's default branch
and moved to the execution branch before any push; its identity is unchanged, and no other branch
was pushed. The drafting-time scratch scripts behind the freeze's measurements were lost with the
replaced container. The scripts listed above are the ones that ran the execution.

***

## Chronology

The execution's commits after `B` are four: `G10` (`0977cca5`), `G12` (`0940adb4`), the
self-description (`e3b6b4a2`), and this note, which is `E`. Each has exactly one parent, the first
`B`. None changes the preregistration, and the branch absorbed no later `main`. Stage commits were
pushed without waiting for continuous integration on them. Nothing has been merged.
