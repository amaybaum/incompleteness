# Reconstruction round ORD-1 — iterated operation data and finite or infinite order on the completed body: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #788.

- **`D`** — `afa66d16d7adaffe94fb9bac391e6039c51dad8a`, the head of `main` after round TRB-1 landed, certified by push
  run 37231625458.
- **`F`** — `cf3509e8bccb284a70932846922ce07f962788cf`, parent `931142a42ffcdf5b9459221d59bc8f19b269e428`;
  `delta(D, F)` is the preregistration alone, blob `301cccc078bbea81b0368f77451b6b8ec8bfd904`. Its exact-head
  `workflow_dispatch` run 37233878948 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F` (comment 5984450815). That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `ORD-1-COMPOSITION-ORDER-PROVED`

The round proves the order side of the architecture on its own spine, OPACT composition → iterated operation data →
finite or infinite order on the completed body, consuming nothing of the geometry of round TRB-1. It states no
implication between transitivity and order in either direction.

In the kernel, for a directed system of finite stages, its completed body and a completion chart
(`StageCompletion`, `CompletionAction`):

- **the order predicates** (`InfiniteOrderOn`, `FiniteOrderOn`, `OrdInf`, `MulClosed`): infinite order on a set of
  states means every positive power moves some state, finite order that some positive power fixes every state; ORD∞ is
  the predicate on a set of automorphisms that some member has infinite order; composition closure is named
  separately. Finite and infinite order exclude each other, one theorem per direction
  (`finiteOrderOn_of_not_infiniteOrderOn`, `not_infiniteOrderOn_of_finiteOrderOn`);
- **iterated composition** (`idDatum`, `iterAfter`, `affineRespect_iterAfter`, `induced_iterAfter`,
  `coe_induced_iterAfter`): the `m`-fold composite of a datum with itself through the landed law `after` respects
  affine relations, and the map it induces on the chart is the `m`-fold composite of the induced map;
- **infinite order keeps every power nontrivial** (`iterate_eq_id_of_fix`, `exists_moved_of_infiniteOrderOn`): a
  reversible datum whose induced automorphism has infinite order on the chart body has, for every `m ≥ 1`, a
  preparation that its `m`-fold composite moves;
- **finite order from stage preservation** (`exists_finset_affineSpan_eq_top`, `exists_return`,
  `exists_common_period`, `finiteOrderOn_of_stagePreserving`): a reversible datum that carries each stage's
  preparations to preparation vectors of the same stage induces an automorphism of finite order on the chart body; a
  finite affinely spanning subset of the chart generators exists, each generator returns under some positive power, a
  common period exists, and an affine map fixing a spanning set is the identity. Reversibility and finite rank, through
  the chart, are load-bearing;
- **the closure control** (`not_ordInf_of_finite_of_mulClosed`, `ordInf_singleton_rot3`): a finite
  composition-closed set of affine automorphisms has no member of infinite order; the singleton of the one-radian
  rotation of the ball, finite and not composition-closed, has one, so finiteness of a listed family does not stand in
  for closure;
- **the ball controls** (`infiniteOrderOn_rot3_one`, `not_ordInf_householder3`, `ordInf_fullAut3`,
  `ordInf_range_rot3`, `finiteOrderOn_hh3`): the rotation by one radian has infinite order on the ball, since π is
  irrational; every Householder reflection has order two and the Householder set has no member of infinite order; the
  affine automorphisms of the ball and the rotation family each have a member of infinite order;

joined in the verdict `ord1_core`.

The stage-preservation theorem carries exactly the hypotheses of two data respecting affine relations, the two inverse
clauses, and stage preservation, on a completion chart. The module contains no transitivity predicate, no ball theorem,
no dimension, drive, flow, continuity or compactness statement, and imports nothing of `TransitiveBody` or
`InvariantInnerProduct`. Whether a composition-closed boundary-transitive family in dimension ≥ 2 has a member of
infinite order remains open; its known proofs pass through Jordan–Schur or Cartan's closed-subgroup theorem. Nothing
here supplies an operation datum, finite rank, a completion chart or stage preservation from an OI construction. The
round edits no manuscript and no roadmap row.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `cf3509e8` | the preregistration | 37233878948 | `success`, all 32 jobs; release gate PASS, `lean-axioms` 5517, as at `D` |
| `C1` = `507a596e` | stage C1: `controls.py`, blob `6cb4471b` | none required | `controls.py --self-test`: `controls: OK -- 29 checks` |
| `S1` = `4aa2d979aa018a1cd17de96cf102fd36cc04356f` | stage S1: `CompositionOrder` blob `d8e04d32`, the import line (`OIBridge.lean` blob `6f94ffa3`), the census family (blob `d975aa8d`) | 37235405513 | `success`, all 32 jobs |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `eada246c`
outside the preregistration. `controls.py check S1 --freeze F` prints `controls: OK -- 18 checks`.

Run 37235405513 is a `workflow_dispatch` run whose `head_sha` is `S1`, run to completion with no job cancelled:

- the Lean kernel check (job 111533388807), the Mathlib bridge (job 111533389002), the 29 numerical-probe shards (act
  42's dispatch-only exclusion shards included) and the probe aggregate (job 111538769043) each concluded `success`;
- the Mathlib bridge built `OIBridge.CompositionOrder` (3630 build jobs);
- each of the 35 frozen `#print axioms` lines of `CompositionOrder` reports `[propext, Classical.choice, Quot.sound]`;
- the release gate passed every step: `lean-axioms` 5552 named results, the 5517 at `D` and the 35 new prints, no
  `sorryAx`; `lean-manuscript` OK with the new census family; 303 legacy records intact; 30 receipts holding.

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| order predicates | `coe_affPow`, `finiteOrderOn_of_not_infiniteOrderOn`, `not_infiniteOrderOn_of_finiteOrderOn`, `not_infiniteOrderOn_iff`, `finiteOrderOn_refl`, `finiteOrderOn_of_iterate_eq` | proved; controls S4, S7 |
| closure | `not_ordInf_of_finite_of_mulClosed`, `ordInf_singleton_rot3` | proved; control S5 |
| finite extraction | `exists_return`, `exists_common_period`, `exists_finset_affineSpan_eq_top` | proved; control N2 |
| iteration | `affineRespect_idDatum`, `induced_idDatum`, `affineRespect_iterAfter`, `induced_iterAfter`, `coe_induced_iterAfter`, `coe_inducedEquiv` | proved; control N2 |
| infinite order | `iterate_eq_id_of_fix`, `exists_moved_of_infiniteOrderOn` | proved; controls N2, S1 |
| stage preservation | `nonempty_prep`, `exists_gen_finset`, `mem_stageGen`, `mapsTo_stageGen`, `finiteOrderOn_of_stagePreserving`, `not_infiniteOrderOn_of_stagePreserving`, `not_stagePreserving_of_infiniteOrderOn` | proved; controls S2, S3 |
| controls | `hh3_hh3`, `finiteOrderOn_hh3`, `not_ordInf_householder3`, `rot3_mem_fullAut3`, `rot3_one_iterate`, `infiniteOrderOn_rot3_one`, `ordInf_fullAut3`, `ordInf_range_rot3` | proved; control S6 |
| verdict | `ord1_core` | proved; controls S1–S3 |

## Design evidence

The design runs before `F` are recorded in the preregistration: run 37226093756 (one `noncomputable` repair), run
37226273423 on the module from `7c821261`, run 37232152756 on the same module rebased onto `D` (all 32 jobs `success`
in the latter two), and the predicted execution tree `eada246c` with run 37232501743 (all 32 jobs `success`). The order
predicates and the rotation and reflection controls were first drafted inside round TRB-1's design module and moved
here by the owner's scope cut. They are design evidence, not attestations, and the pull-request runs on this branch
are not attestations.

## What stays open

Whether a composition-closed boundary-transitive family in dimension ≥ 2 has a member of infinite order; a source of
reversible operation data, of finite rank or of stage preservation in an OI construction; the drive and its
continuity; the composite interface; the dimension selector.
