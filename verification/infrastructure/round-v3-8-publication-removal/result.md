# Verifier round V3-8 — publication leaves the V3 validity model: RESULT

Executed from the certified execution base and from nothing else, under `AGENTS.md` §A.37: the
control plane #737, then the execution pull request, which also carries the landing.

- **`D`** — `f557b1ccbdf9e441b33f5f70fa163823fc2ca10a`.
- **`B`** — `8ad53333226ccf425847b187c51f85b2f4966994`, the merge of #737. Its parents are `D` and
  the reviewed control-plane head `63a79eb420e282a5d280b7a4667ab4f739edb2a3`, and its tree is that
  head's. Push run 36057340925 was green on all six jobs, the control-plane base check in mode `B`
  with 11 rows and 3 frozen blobs.
- **Preregistration** — blob `b1043a0a820b3aa0edf62a0029a67f67a4c85e82` at `B` and at `E`.
- **Shape** — non-sealing, `E` → `L`, no `P`: no guard clause, manifest record or round
  certificate (reading `R8`).
- **Status** — COMPLETE: every target reached its passing outcome. For `V38-5` the
  repository-wide conditions (the guard, `V2`, the release gate) are established by the exact-head
  run on `E`, which the `E` certification record identifies; they were not run locally.

| target | outcome | predicted |
|---|---|---|
| `V38-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V38-1` | `PUBLICATION-REMOVED`; `architecture.md` blob `db36dbd1` | the same, strong |
| `V38-2` | `DIAGNOSTIC-INSTALLED`; tool blob `0b3bd87f` | the same, strong |
| `V38-3` | `SELF-DESCRIPTION-CURRENT`; tool blob `ccfbe813`, README blob `55aba15b` | the same, strong |
| `V38-4` | `CONTROLS-HOLD` | `CONTROLS-HOLD`, strong |
| `V38-5` | `SHADOW-ONLY` | `SHADOW-ONLY`, strong |
| `V38-6` | `SCOPE-HELD` | `SCOPE-HELD`, strong |

Every stage's blobs are the predicted ones, so no stage diverges from the predicted replacement
text, and there is no divergence for the owner's review. The controls show that the tool
implements what the vectors encode; they are not evidence that the amended specification is right
(hazard `H1`).

The specification's lifecycle ends at T7, when the final receipt commit `Q` is receipted; how a
round's commits reach `main` is outside it. The shadow verifier reports whether `Q` is an ancestor
of a given commit through `--reachable`, a diagnostic that no verdict reads. It gates nothing.
`V1` and `V2` remain authoritative. V3 is not operative.

***

## `V38-0` — the base: BASE-HOLDS

The execution branch was created at exactly `B`, after `B`'s push run was green, with `main` still
at `B` and the checkout not shallow. At `B` the preregistration's blob is the frozen `b1043a0a`,
and `architecture.md`, `tools/v3_verifier.py` and `verification/README.md` have the frozen blobs
`12cff3f2`, `21ea4097` and `08cb7962`. The control-plane base check in mode `B` holds at `B`: 11
rows and 3 frozen blobs, no failure. At `B` the corpus held 133 vectors, and neither
`verification/receipts/` nor `verification/v3-seals/` existed.

***

## `V38-1` — the specification: PUBLICATION-REMOVED

Stage 1, commit `b969cc9eae98d4c18c3b333219998b1f5ffc88d0`, whose only parent is `B`. The frozen
edits `N1` to `N21`, read back from the preregistration as it stands at `B`, were applied in order
to `architecture.md` at `B`, each located block occurring exactly once when applied.

- **`architecture.md` blob:** `db36dbd1ee4f779eff13525ffd3dc11d9041ab36`, the predicted one.
- **`C7`:** the file no longer contains `PUBLISHED`, `T8`, ``tip of `main` when``,
  `publication makes`, `publication is a fast-forward` or ``live tip of `main` is publication``.
- **`C1`:** `CORPUS  133 vector(s), exact and as expected`.
- **`C6`:** the self-test passes.

The commit changes `architecture.md`, and nothing else.

***

## `V38-2` — the diagnostic: DIAGNOSTIC-INSTALLED

Stage 2, commit `f3ea6f63b19a01e87ad0702c572977e217c44143`, whose only parent is `b969cc9e`. The
frozen sites `s2.1` to `s2.5` were applied to the stage-1 tool, and the corpus was changed as
frozen: `mc2-counter-host-merge.json` deleted, the final step of `mc2-pass-base-drift.json`
converted to `reachable(Q2, Q)` expecting `true`, and the three `reach-` vectors added. The bytes
of the converted and three added files, concatenated in path order, have SHA-256
`729ac7598d9d3f28a91be1c0f939d38c426ae6b0d8480767c3947e962f38ce49`, the predicted value.

- **Tool blob:** `0b3bd87fe52b269e9d7cf0fdb7f47653301ce8fd`, the predicted one.
- **`C1`:** `CORPUS  135 vector(s), exact and as expected`.
- **`C2`:** each of `reach-true-host-merge-contains-q`, `reach-false-moved-base-lacks-q`,
  `reach-undecidable-shallow-history` and `mc2-pass-base-drift` runs not as expected under the
  stage-1 tool and as expected under the stage-2 tool; the retired vector is absent; the stage-2
  tool contains no `publication(` and no `s10:not-q-itself`.
- **`C6`:** the self-test passes.

The commit changes the tool and the five corpus files, and nothing else.

***

## `V38-3` — the self-description: SELF-DESCRIPTION-CURRENT

Stage 3, commit `bec0bf8ec4f08232236cd02dc059fd025c45594c`, whose only parent is `f3ea6f63`. The
frozen sites `s3.1` and `s3.2` were applied to the stage-2 tool, and the frozen README paragraph
replaced the paragraph at `B`.

- **Tool blob:** `ccfbe813790e4855f408462449327f32e59d545b`, the predicted one.
- **README blob:** `55aba15ba3cf57a1fc35232534b6eed810abd920`, the predicted one.
- **`C1`:** `CORPUS  135 vector(s), exact and as expected`.
- **`C6`:** the self-test passes.

The commit changes the tool and `verification/README.md`, and nothing else.

***

## `V38-4` — the controls at `E`: CONTROLS-HOLD

The result note changes no tool, so the tool at `E` is the stage-3 tool. Every run below is of the
committed tool, from the repository.

- **`C3`:** with `reachable` replaced by a wrong diagnostic in a scratch copy of the tool at `E`,
  exactly that diagnostic's vectors run not as expected and every other vector of the corpus as
  expected:

  | wrong diagnostic | its vectors | the others |
  |---|---|---|
  | always `true` | 2, not as expected | 133, as expected |
  | always `false` | 3, not as expected | 132, as expected |
  | ancestry reversed | 2, not as expected | 133, as expected |

  No control was void.
- **`C4`:** `tools/v3_verifier.py --project B` at `E` gives output identical to the tool at `B`
  over the same subject: 68 lines, SHA-256
  `fb92b600d3ca0779bec64c31bbafd31f97c3fda01f02fccc7847513961f21d92`.
- **`C5`:** `python3 tools/v3_verifier.py --mode shadow --subject <stage-3 commit>`, run from the
  repository, exits 0; its first line is the banner `v3_verifier shadow report -- SHADOW ONLY: this
  report gates nothing; V1 and V2 remain authoritative`; it prints the rules `K1`–`K4` and
  `G5`–`G12`, in that order, each once, the line `CORPUS  135 vector(s), exact and as expected`
  and the line `PROJECTION  cells 126`; and its last line is `v3_verifier: shadow report complete
  (corpus as expected)`. `--reachable B <B's first parent>` prints `REACHABLE true` and
  `--reachable <B's first parent> B` prints `REACHABLE false`, each exiting 0; `--publication` is
  refused with exit 2 and prints no verdict. Neither the tool nor `verification/README.md`
  contains `--publication` or `not-q-itself`, and the README's paragraph is the frozen text. The
  shadow job of the exact-head run on `E` runs the same report at `E`.
- **`C6`:** the self-test passes at every stage's commit.

The scripts that ran the stages and the controls, none of which is landed:

| script | SHA-256 |
|---|---|
| `exec38.py` (applies one stage's frozen edits or sites, read back from the preregistration at `B`, and runs that stage's checkpoint) | `6744f590fce98b2eb831b5a0e719c6ee7d8406b97151cc24a5574617e08924e8` |
| `gen38.py` (builds the converted and added vectors from the corpus at `B`) | `c77d229bbdf3d5eb970ee64c3f789618bc570f995a2ac88a9e831b95840d519d` |
| `close38.py` (`C3`–`C6`, scope and chronology at the stage-3 commit) | `d493d7b14a9c36e30797edd2b8a5c37dcddfe4a047f964a676a4cf13bcc30365` |

***

## `V38-5` — non-authority: SHADOW-ONLY

At `E`, `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`,
`verification/lean/edge_rigidity_probe.py`, `AGENTS.md` and the preregistration have their `B`
blobs. Neither `verification/receipts/` nor `verification/v3-seals/` exists, nothing under
`verification/seals/` changed, `--reachable` is read by no verdict and wired into no gate, and no
required check was touched.

The guard's verdict (105 PASS, 0 FAIL, with `D`'s verdict map), `V2` authoritative OK, the release
gate's 19 of 19 steps and the shadow job's self-test and 135-vector corpus at `E` are taken from
the exact-head run on `E`, not run locally.

***

## `V38-6` — scope: SCOPE-HELD

`git diff --no-renames --name-status B E`:

| status | path |
|---|---|
| `M` | `verification/infrastructure/v3/architecture.md` |
| `M` | `tools/v3_verifier.py` |
| `M` | `verification/README.md` |
| `M` | `verification/infrastructure/v3/conformance/mc2-pass-base-drift.json` |
| `A` | `verification/infrastructure/v3/conformance/reach-true-host-merge-contains-q.json` |
| `A` | `verification/infrastructure/v3/conformance/reach-false-moved-base-lacks-q.json` |
| `A` | `verification/infrastructure/v3/conformance/reach-undecidable-shallow-history.json` |
| `A` | `verification/infrastructure/round-v3-8-publication-removal/result.md` |
| `D` | `verification/infrastructure/v3/conformance/mc2-counter-host-merge.json` |

This is exactly the mutation budget: 4 modified, 4 added, 1 deleted. Nothing on the budget's
never-written list changes.

***

## Discrepancies

None against the freeze.

***

## Chronology

The execution's commits after `B` are four: the specification (`b969cc9e`), the diagnostic and
corpus (`f3ea6f63`), the self-description (`bec0bf8e`), and this note, which is `E`. Each has
exactly one parent, the first `B`. None changes the preregistration, and the branch absorbed no
later `main`. Stage commits were pushed without waiting for continuous integration on them.
Nothing has been merged.
