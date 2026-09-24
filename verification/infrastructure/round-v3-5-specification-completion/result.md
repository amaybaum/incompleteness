# Verifier round V3-5 — V3 specification completion: the gaps G8–G12: RESULT

Executed on #733 from the certified execution base and from nothing else, under `AGENTS.md` §A.37:
the control plane #732, then this execution pull request, which also carries the landing.

- **`D`** — `f639af0abf67fb252f048e631e6237f84a25df24`.
- **`B`** — `c7ca4a89ef969f3aaaf4e9a3d9fbde5ea5c7acbe`, the merge of #732. Its parents are `D` and the
  reviewed control-plane head `971a5e58b52cb481032061fe5712b559f17fbf3d`, and its tree is that
  head's. Push run 36006252324 was green on all six jobs, the control-plane base check in mode `B`
  with 13 rows and 3 frozen blobs.
- **Preregistration** — blob `c20deafdd92e408675075a62b437f3efa853929f` at `B` and at `E`.
- **Shape** — non-sealing, `E` → `L`, no `P`: no guard clause, manifest record, round certificate or
  attestation (reading `R5`).
- **Status** — COMPLETE: every target reached its passing outcome. For `V35-7` the repository-wide
  conditions (the guard, `V2`, the release gate) are established by the exact-head run on `E`,
  which the `E` certification record on #733 identifies; they were not run locally.

| target | outcome | predicted |
|---|---|---|
| `V35-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V35-1` | `SPECIFICATION-SETTLED`; `architecture.md` blob `12cff3f2` | the same, strong |
| `V35-2` | `STATUS-CURRENT`; `verification/README.md` blob `50c39016` | the same, strong |
| `V35-3` | `CORPUS-CONFORMING`; digests `2a0cc7d8` (modified), `b0f3db22` (added) | the same, strong |
| `V35-4` | `DEPARTURES-DEMONSTRATED`; digest `8d2209b6` | the same, strong |
| `V35-5` | `SETTLEMENTS-SATISFIABLE` | `SETTLEMENTS-SATISFIABLE`, strong |
| `V35-6` | `ALTERNATIVES-EXCLUDED` | `ALTERNATIVES-EXCLUDED`, strong |
| `V35-7` | `SHADOW-UNCHANGED` | `SHADOW-UNCHANGED`, strong |
| `V35-8` | `SCOPE-HELD` | `SCOPE-HELD`, strong |

`SETTLEMENTS-SATISFIABLE` and `ALTERNATIVES-EXCLUDED` are consistency findings about the settlements
and their vectors, made with code by the author of the settlements; they are not evidence that the
settlements are right (hazard `H1`).

The shadow verifier `tools/v3_verifier.py` is unchanged and gates nothing. `V1` and `V2` remain
authoritative. V3 is not operative.

***

## `V35-0` — the base: BASE-HOLDS

The execution branch was created at exactly `B`, after `B`'s push run was green. At `B` the
preregistration's blob is the frozen `c20deafd`, and `architecture.md`, `tools/v3_verifier.py` and
`verification/README.md` have the frozen blobs `3326bf30`, `883122c4` and `690f841e`. The
control-plane base check in mode `B` holds at `B`: 13 rows and 3 frozen blobs, no failure. At `B`
the corpus held 105 vectors and ran exact and as expected on the shadow, and none of
`verification/infrastructure/v3/conformance-pending/`, `verification/receipts/` and
`verification/v3-seals/` existed.

***

## `V35-1` and `V35-2` — the normative text and the README paragraph

Stage 1, commit `69642699e5188677ce72f1d40b5a4163b00abe75`, whose only parent is `B`. The
twenty-five edits `N1`–`N25` and the README replacement were read back from the preregistration as
it stands at `B` and applied, in order, to the two files' blobs at `B`.

- **`C6`:** `architecture.md`'s blob is `12cff3f2c9b2cb7803ed1572c98bccba7590c707`, the predicted
  one, and it is the file's blob at `E`. **SPECIFICATION-SETTLED.**
- **`C7`:** `verification/README.md`'s blob is `50c390168966980c4ebf590a78c4269089af68c2`, the
  predicted one, and it is the file's blob at `E`. **STATUS-CURRENT.**

The commit changes no other file.

***

## `V35-3` to `V35-6` — the vectors and the controls

Stage 2, commit `dbeeafb9609a4a4cd1989d9956689d53797cdddd`, whose only parent is `69642699`.

- **Modified:** the nine vectors of the frozen table. Each keeps its `id`, `settlements`, `kind` and
  expected verdict; the six seal-record fixtures move to `verification/v3-seals/<round>.json`, and
  `s4-canonical-ex-2`, `s4-seal-in-non-sealing` and `s7-g2-nested` follow edits `N23`–`N25`, the
  last with set G2's new digest `0053d9c8…` as its expected digest. SHA-256 of the nine, concatenated
  in path order: `2a0cc7d8a883c6b1d806721c1fd531ff71f3f937e087c831630f72de1aaf6303`, the predicted
  one.
- **Added to `conformance/`:** the eleven frozen vectors. Digest
  `b0f3db227e5c02370aa83c3f2a7fd5a77d563f6494f145d9fdaa93a62e65c3c6`, the predicted one.
  `conformance/` at `E` holds 116 vectors.
- **Added to `conformance-pending/`:** the seventeen frozen vectors, and nothing else. Digest
  `8d2209b69b5f516d4d1a6ce12d633ece91e18cc4a91fd25dfb3f7ed90a994069`, the predicted one.

The controls, run on the directories in the tree at stage 2:

- **`C1`:** the unchanged shadow runs the 116 vectors of `conformance/` as an exact set, every one
  as expected. **CORPUS-CONFORMING.**
- **`C2`:** the unchanged shadow runs the seventeen vectors of `conformance-pending/`, every one not
  as expected, each returning `HOLDS`. **DEPARTURES-DEMONSTRATED.**
- **`C3`:** the settlement patch, a scratch copy of the shadow changed only where the `G10` and
  `G12` settlements depart from it, SHA-256
  `b63e12d86036e643c3ac250cb8ad0e443fb43e6448ed558baaa06082be40c534`, runs all 133 vectors of the two
  directories as expected.
- **`C4`:** with each of the patch's five rules taken out, exactly the pending vectors that rule owns
  run not as expected and every other pending vector as expected.
  **SETTLEMENTS-SATISFIABLE.**

  | rule taken out | its vectors | the others |
  |---|---|---|
  | near misses (`G10`) | 6, not as expected | 11, as expected |
  | the seal entry at `F` (`G12`) | 5, not as expected | 12, as expected |
  | the receipt names the fixed seal record alone (`G12`) | 2, not as expected | 15, as expected |
  | no change to another round's receipt or seal state (`G12`) | 3, not as expected | 14, as expected |
  | each receipt commit's changes authorized (`G12`) | 1, not as expected | 16, as expected |

- **`C5`:** each of the twelve rejected alternatives, implemented in a scratch copy, runs each of its
  distinguishing vectors not as expected, while the copy it was made from runs them as expected: on
  the unchanged shadow `G8` (c), `G9` (a) and (c), `G10` (b) and `G11` (a); on the settlement patch
  `G10` (d) and `G12` (b), (c), (d), (e), (f) and (h). No control was void.
  **ALTERNATIVES-EXCLUDED.**

The nine modified vectors, taken as they stood at `B`, run under the settlement patch as `F3`
recorded: `k4-admit-sealing-superseded-receipt-commit`, `mc7-counter-seal-record-missing-from-q`,
`mc7-pass-sealing` and `s4-canonical-ex-2` not as expected (`s4:seal`), the other five as expected.

The scratch scripts, none of which is landed:

| script | SHA-256 |
|---|---|
| `edits35.py` (the frozen edits as drafted) | `7714cb729268d22f979a1998b9a2bb321f134571487429b102632b5437b1912a` |
| `frozen35.py` (reads the edits back from the preregistration and applies them) | `30e69ad7ad4a8ecd250fcff2e1b5554aa70e5b87319f27b83a99302337048f6e` |
| `regen35.py` (regenerates the corpus from its recipes) | `b9b03eae5785267da958ddb7ba9d3a0ec036afcad1499413ba282e1e9d3e56b0` |
| `helpers_old.py` (the recipe helpers as they stand) | `8a7d4c8a28a56b7afb663df4cfd1809a6ccb369a33241531359cb8367a2a894a` |
| `helpers_new.py` (the same, with the fixed seal record path) | `fa3c6a7225b7611a44f15c2d0bc027db894a6d3290457a5d87bb1f12d03a28ba` |
| `gen_v35.py` (builds the added and pending vectors) | `08c93a862a57cdc9979aa1d0f83580d619c1db9dae7b91858943f1c01d5dd85d` |
| `settle35.py` (the settlement patch and the alternatives) | `74d9dd131c296baacd007944044eb2e8900d6ab4bb8c797f945971439170f1e2` |
| `measure35.py` (`C1`–`C5`) | `e7fb468b3bd3ffd6710691723bbef8c1696b686a3993b49db376ee42263cf42c` |
| `render35.py` (renders the preregistration from its template) | `167625ec809a5e7c73a9834345399570af46ac98a769ba4bd03f56196deb471a` |

***

## The five items at `E`

| item | settlement | shadow at `E` conforms |
|---|---|---|
| `G8` | (b): no mutable ref or host state is a predicate input | yes |
| `G9` | (b): before `F` the control plane is a draft | yes |
| `G10` | (c): declaration blocks recognized by exact lines; near misses invalid | no |
| `G11` | (b): the round's later objects are those its final receipt commit reaches | yes |
| `G12` | (g): one opaque seal record at `verification/v3-seals/<round>.json`; `verification/seals/` untouchable | no |

The specification has no recorded gap. The seventeen pending vectors are the implementation work of
the next round.

***

## `V35-7` — non-authority: SHADOW-UNCHANGED

At `E`, `tools/v3_verifier.py`, `.github/workflows/verify.yml`, `tools/release_gate.py`,
`tools/certificate_verifier.py`, `verification/lean/edge_rigidity_probe.py` and `AGENTS.md` have
their `B` blobs, and the shadow's self-test passes. No act of `V3-2`'s promotion boundary is
present: neither `verification/receipts/` nor `verification/v3-seals/` exists, nothing under
`verification/seals/` changed, the shadow has no authoritative mode, and no required check was
touched.

The guard's verdict (105 PASS, 0 FAIL, with `D`'s verdict map), `V2` authoritative OK, the release
gate's 19 of 19 steps and the shadow job's self-test and 116-vector corpus at `E` are taken from the
exact-head run on `E`, not run locally.

***

## `V35-8` — scope: SCOPE-HELD

`git diff --no-renames --name-status B E`:

| status | path |
|---|---|
| `M` | `verification/infrastructure/v3/architecture.md` |
| `M` | `verification/README.md` |
| `M` | the nine modified vectors of `verification/infrastructure/v3/conformance/` |
| `A` | the eleven added vectors of `verification/infrastructure/v3/conformance/` |
| `A` | the seventeen vectors of `verification/infrastructure/v3/conformance-pending/` |
| `A` | `verification/infrastructure/round-v3-5-specification-completion/result.md` |

This is exactly the mutation budget: 11 modified, 29 added, nothing deleted. Nothing on the budget's
never-written list changes.

***

## Discrepancies

None.

***

## Chronology

The execution's commits after `B` are three: the normative text and the README paragraph
(`69642699`), the vectors (`dbeeafb9`), and this note, which is `E`. Each has exactly one parent,
the first `B`. None changes the preregistration, and the branch absorbed no later `main`. Stage
commits were pushed without waiting for continuous integration on them. Nothing has been merged.
