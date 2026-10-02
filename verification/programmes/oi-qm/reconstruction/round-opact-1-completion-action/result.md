# Reconstruction round OPACT-1 — completion-valued operation data and the action they induce on the completed body: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #783.

- **`D`** — `254ad0a7f19b3cf6f6ce28e1a7b955f18e4337e4`, the head of `main` after `CMP-1` landed, certified by push
  run 37005559751.
- **`F`** — `149b2b2864acc762a61d82f9bd161361d9465447`, parent `07266ae779ac73cc4955c75f760883ba05a1221a`;
  `delta(D, F)` is the preregistration alone, blob `ac0b671930a3b530eb58764767a40eca887a2c03`. Its exact-head
  `workflow_dispatch` run 37021207087 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F`. That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `OPACT-1-COMPLETION-ACTION-PROVED`

The round proves the completion action of an operation datum. It does not source any operation: the datum is the
premise the round exposes.

In the kernel, for a directed system of finite stages and its completed body (`StageCompletion`):

- **the two respect conditions** (`stateRespect_of_affineRespect`, `midOp_stateRespect`, `midOp_not_affineRespect`):
  an operation datum carries each stage preparation to a point of the completed body; `AffineRespect` (every finite
  affine relation among preparation vectors holds among the images) implies `StateRespect` (equal preparation
  vectors have equal images), and not conversely: on a one-stage system with readings `0`, `1/2` and `1`, the
  exchange of the first preparation and the midpoint respects states and breaks `x₀ − 2 x_m + x₂ = 0`;
- **the affine extension** (`sum_smul_affine`, `exists_affine_of_relations`): a family satisfying every finite affine
  relation of another family is its image under an affine map;
- **the chart** (`exists_completionChart`, `chartBody_subset`, `affineSpan_gen`): a nonempty completed body of finite
  rank has a chart of its affine span; the chart body lies in the closed convex hull of the chart generators, and the
  generators affinely span the chart;
- **the induced action** (`existsUnique_induced`, `affineRespect_of_induced`, `induced_mem`): under `AffineRespect`
  exactly one affine map of the chart extends the datum, an affine extension forces `AffineRespect`, and the induced
  map carries the chart body into itself;
- **composition** (`induced_after`, `comp_eq_id`): the map induced by one datum after another is the composite of the
  induced maps;
- **reversibility** (`preservesBody_inducedEquiv`): a datum with an inverse datum, in both directions, induces an
  affine equivalence of the chart with `PreservesBody` in the sense of `OrbitGeneration`;
- **effect pullback** (`isEffectOn_pullback`): a stage effect read after the induced map is an effect on the chart
  body;

joined, for the respect conditions, the chart, the induced action and reversibility, in the verdict `opact1_core`.

`StateRespect` is strictly weaker than `AffineRespect` and occurs in no load-bearing statement. Inverse availability
and finite rank enter as hypotheses where they are used; neither is sourced. The round supplies no operation, no flow
or one-parameter group, no gate or phase, no transitivity, no invariant inner product, no dimension and no ball, does
not use SC∞, and claims no closure of `stageEffects` under any operation. It edits no manuscript and no roadmap row.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `149b2b28` | the preregistration | 37021207087 | `success`, all 32 jobs; release gate 21 of 21, `lean-axioms` 5475, as at `D` |
| `C1` = `ff1f73cd` | stage C1: `controls.py`, blob `7a622a8b` | none required | `controls.py --self-test`: `controls: OK -- 27 checks` |
| `S1` = `d2cebd15f0c210fbc2e28e57627f37014e4e13d5` | stage S1: `CompletionAction` blob `8bcab4a5`, the import line, the census family | 37024002953 | `success`, all 32 jobs |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `ca2daeeb`
outside the preregistration. `controls.py check S1 --freeze F` prints `controls: OK -- 16 checks`.

Run 37024002953 is a `workflow_dispatch` run whose `head_sha` is `S1`, run to completion with no job cancelled:

- the Lean kernel check (job 110893910015), the Mathlib bridge (job 110893909713), the 29 numerical-probe shards (act
  42's dispatch-only exclusion shards included) and the probe aggregate (job 110900880657) each concluded `success`;
- the Mathlib bridge built `OIBridge.CompletionAction` (3624 build jobs);
- each of the 16 frozen `#print axioms` lines of `CompletionAction` reports `[propext, Classical.choice, Quot.sound]`;
- the release gate passed all 21 steps: `lean-axioms` 5491 named results, the 5475 at `D` and the 16 new prints, no
  `sorryAx`; `lean-manuscript` OK with the new census family; 303 legacy records intact; 25 receipts holding.

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| respect conditions | `stateRespect_of_affineRespect`, `midOp_stateRespect`, `midOp_not_affineRespect` | proved; controls N2, S1, S2 |
| affine extension | `sum_smul_affine`, `exists_affine_of_relations` | proved; controls N2, S1 |
| chart | `exists_completionChart`, `chartBody_subset`, `affineSpan_gen` | proved; controls N2, S3 |
| induced action | `existsUnique_induced`, `affineRespect_of_induced`, `induced_mem` | proved; controls N2, S1 |
| composition | `induced_after`, `comp_eq_id` | proved; controls N2, S1 |
| reversibility | `preservesBody_inducedEquiv` | proved; controls N2, S1, S3 |
| effect pullback | `isEffectOn_pullback` | proved; controls N2, S1, S4 |
| verdict | `opact1_core` | proved; controls S1–S5 |

## Design evidence

The design runs before `F` are recorded in the preregistration: runs 37011255825, 37011853989 and 37012251866 with
three proof-only repairs and the re-indexed countermodel, run 37013353037 on the reference blob `8bcab4a5` (all 32
jobs `success`), and the predicted execution tree `ca2daeeb` with run 37018873171 (all 32 jobs `success`). They are
design evidence, not attestations, and the pull-request runs on this branch are not attestations.

## What stays open

A source of operation data satisfying `AffineRespect` in an OI construction; inverse availability; finite rank of
the completed body; the drive and its continuity in the chart; the effect-generation family of completed effects;
SC∞; transitivity, dimension three and the ellipsoid normalization.
