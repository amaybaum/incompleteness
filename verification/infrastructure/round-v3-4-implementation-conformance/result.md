# Verifier round V3-4 — V3 implementation conformance: RESULT

Executed on #731 from the certified execution base and from nothing else, under `AGENTS.md` §A.37:
the control plane #730, then this execution pull request, which also carries the landing.

- **`D`** — `c021f12b2564a07adf9142032a0fc371d5b9c6e3`.
- **`B`** — `ac5122b0b9a7282d2698832cbed79a10de4d8011`, the merge of #730. Its parents are `D`
  and the reviewed control-plane head `579916cfebf7db23c5d087d4e3eced896425fbef`, and its tree is
  that head's. Push run 35987289037 was green on all six jobs, the control-plane base check in mode
  `B` with 11 rows and 3 frozen blobs.
- **Preregistration** — blob `85db2f70afd39e7260e76c2e26ef2cf64ce02529` at `B` and at `E`.
- **Shape** — non-sealing, `E` → `L`, no `P`: no guard clause, manifest record, round certificate or
  attestation (reading `R5`).
- **Status** — every target reached its passing outcome. For `V34-7` the repository-wide conditions
  (the guard, the release gate, `V2`) are established by the exact-head run on `E`, which the `E`
  certification record on #731 identifies; they were not run locally.

| target | outcome | predicted |
|---|---|---|
| `V34-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V34-1` | `K2-CONFORMS`; tool blob `27f74108` | the same, strong |
| `V34-2` | `K4-CONFORMS`; tool blob `14768bfc` | the same, strong |
| `V34-3` | `G6-CONFORMS`; tool blob `42b2d61c` | the same, strong |
| `V34-4` | `K1-REPAIRED`; tool blob `2fbbf9ba` | the same, strong |
| `V34-5` | `SELF-DESCRIPTION-CURRENT`; tool blob `883122c4`, README blob `690f841e` | the same, strong |
| `V34-6` | `CONTROLS-HOLD` | `CONTROLS-HOLD`, strong |
| `V34-7` | `SHADOW-ONLY` | `SHADOW-ONLY`, strong |
| `V34-8` | `SCOPE-HELD` | `SCOPE-HELD`, strong |

**Divergences from the predicted implementation text: none.** At every stage the edit was the
frozen site's drafting-time replacement, read back from the preregistration at `B`, and the tool's
blob equals the predicted one; there is no divergence for the owner's review.

The vectors show that the tool implements what they encode; they are not evidence that the
settlements are right (hazard `H1`). The shadow verifier gates nothing. `V1` and `V2` remain
authoritative. V3 is not operative.

***

## `V34-0` — the base: BASE-HOLDS

The execution branch was created at exactly `B`, after `B`'s push run was green. At `B` the
preregistration's blob is `85db2f70`, and `tools/v3_verifier.py`, `verification/README.md` and
`verification/infrastructure/v3/architecture.md` have the frozen blobs `2c34d4d7`, `052dfa27` and
`3326bf30`. The control-plane base check in mode `B` holds at `B`: 11 rows and 3 frozen blobs, no
failure. At `B` the corpus held 93 vectors and `conformance-pending/` eleven.

***

## Stages 1 to 5

Each stage is one commit whose only parent is the one before it, the first `B`. Each applies that
stage's frozen sites, read back from the preregistration at `B`, to the tool as the previous stage
left it. `C2` runs each vector the stage moves or adds under the tool at the stage's parent and
under the stage's tool.

| stage | commit | tool blob | vectors | `C1` corpus | `C2` under the parent's tool |
|---|---|---|---|---|---|
| 1 `K2` | `137814f3eded6b2d31089835df550df222e1cf82` | `27f74108` | 2 moved | 95, as expected | both `HOLDS`, not as expected |
| 2 `K4` | `325548af7d9c05c17d12c2944e9f5e8e37054193` | `14768bfc` | 3 moved | 98, as expected | `HOLDS`, `HOLDS`, and `FAILS s10:` for the unreadable superseded receipt, not as expected |
| 3 `G6` | `a96d52ef78842b3d005401abf93cb7f79c337dfd` | `42b2d61c` | 6 moved | 104, as expected | all six `HOLDS`, not as expected |
| 4 `K1` | `d3f7a5f050bd9331125288d0d9af23cd55d47fbe` | `2fbbf9ba` | 1 added | 105, as expected | `FAILS t1:record-directory`, not as expected |
| 5 text | `c1dde15993f79b2043954b9db4f3996ac11b30eb` | `883122c4` | — | 105, as expected | — |

Under each stage's own tool every vector it moved or added runs as expected. Every moved vector has,
at `E`, the blob it had under `conformance-pending/` at `B`. After stage 3,
`conformance-pending/` holds no file and does not exist in the tree. The added `K1` vector has
SHA-256 `3c323ab012884fd8a6950354b666df58563544d26d126c5d394ab2e483284951`, the predicted bytes.
Its verdict under the tool at `B` is the frozen one, `FAILS t1:record-directory`: the tool's pattern
reads `<R>amendments/` as a second record directory.

`C6`: the self-test passes at every stage's commit.

`C5`, at stage 5: the tool contains none of `provisional`, `reading` and `gap G`
(case-insensitive); the shadow report prints `settled rules
(verification/infrastructure/v3/architecture.md):` followed by `K1`–`K4`; and the paragraph of
`verification/README.md` is the frozen text, blob `690f841ec02dbafbed972667a426cf41fc4ca741`.

***

## `V34-6` — the controls at `E`: CONTROLS-HOLD

`C3`: from the tool at `E`, with one stage's frozen sites reverted and the rest in place, every
vector of the 105-vector corpus was run. Reverting stage 1 breaks exactly its two vectors, stage 2
exactly its three, stage 3 exactly its six and stage 4 exactly its one; no other vector breaks.

`C4`: `tools/v3_verifier.py --project` over the subject `B` gives, under the tool at `E`, output
identical to the tool at `B` over the same subject: 68 lines, 126 cells. `V3-2`'s `census.json`
therefore still describes the shadow's comparison with `V2`.

The scratch scripts, none of which is landed:

| script | SHA-256 |
|---|---|
| `stages.py` (the drafting-time edits, cumulative) | `a993212d88a28b76baa8420d00fdb612c7db3d812fea8153bc7fd2746ee6b873` |
| `gen_v34.py` (builds the `K1` vector) | `07fa96e1a1c4ec4dc55b0b741d55545026360beb87247b8e9378602e67da3a21` |
| `measure.py` (the drafting-time verdict table) | `0920c22e679d2690a0111a53a425564ef2da29b5150d59b89c79ca12464f8fc7` |
| `ownrule.py` (the drafting-time own-rule control) | `3daca4bc4e419f05d4fad90536ccceb3d0538379f5157a31fbf8fab2a07d9a31` |
| `apply_stage.py` (applies a stage's frozen sites from the preregistration) | `1794f9375bc4f2c363b75e59820c7be30af79145e5c0a30dfa21cb5bd7024a62` |
| `c3_e.py` (`C3` at `E`) | `ab181805f14a008c71a720cf8c83b7e690b14d8aeced352238b714f0775cdcf0` |

***

## `V34-7` — non-authority: SHADOW-ONLY

At `E`, `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`,
`verification/lean/edge_rigidity_probe.py`, `AGENTS.md` and
`verification/infrastructure/v3/architecture.md` have their `B` blobs. No `verification/receipts/`
directory exists, the shadow has no authoritative mode, and no required check was touched. The
shadow report opens `SHADOW ONLY: this report gates nothing; V1 and V2 remain authoritative`.

The guard's verdict (105 PASS, 0 FAIL, with `D`'s verdict map), `V2` authoritative OK, the release
gate's 19 of 19 steps and the shadow job's self-test and 105-vector corpus at `E` are taken from the
exact-head run on `E`, not run locally.

***

## `V34-8` — scope: SCOPE-HELD

`git diff --no-renames --name-status B E`:

| status | path |
|---|---|
| `M` | `tools/v3_verifier.py` |
| `M` | `verification/README.md` |
| `A` | the eleven moved vectors under `verification/infrastructure/v3/conformance/` |
| `A` | `verification/infrastructure/v3/conformance/k1-admit-amendment-named-preregistration.json` |
| `A` | `verification/infrastructure/round-v3-4-implementation-conformance/result.md` |
| `D` | the eleven files of `verification/infrastructure/v3/conformance-pending/` |

This is exactly the mutation budget: 2 modified, 13 added, 11 deleted. Nothing on the budget's
never-written list changes. With rename detection on, Git shows each moved vector as a rename.

***

## Discrepancies

None.

***

## Chronology

The execution's commits after `B` are six: the five stages and this note, which is `E`. Each has
exactly one parent, the first `B`. None changes the preregistration, and the branch absorbed no
later `main`. Nothing has been merged.
