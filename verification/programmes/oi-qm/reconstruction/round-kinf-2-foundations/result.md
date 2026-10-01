# Reconstruction round KINF-2 — the corrected field-neutral foundations of the pre-quantum completion: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #777.

- **`D`** — `d6b6458010a6d2812bd3215a8bb6f8a1bab37f00`, the head of `main` after pull request #776, certified by
  push run 36830862465.
- **`F`** — `aa43e2d24d72634b8f3dd2e1e5ce4461d98eee08`; `delta(D, F)` is the preregistration alone, blob
  `d4620610aa5131ba6a289d2049a6fe570c05fe43`. Its exact-head `workflow_dispatch` run 36841329495 concluded `success` with all 31 jobs
  succeeded and none cancelled, its `check-run` attestation; the owner designated `F`.
- **Shape** — non-sealing; three execution stages and this note.

**Outcome:** `KINF-2-FOUNDATIONS-PROVED`

> In the kernel, at evidence level 2, over a real normed space and with no field, matrix carrier or substratum object, for the corrected vocabulary in which an effect is proper when some state gives it a value below one and a boundary state is read in the body alone: a non-proper effect, the unit among them, changes neither supporting-effect completeness nor singleton faces (`supportingEffectComplete_insert_iff`, `singletonFaces_insert_iff`); a convex body with supporting-effect completeness and singleton faces is relatively strictly convex (Lemma C, `relStrictConvex_of_supporting_singleton`), and a relatively strictly convex body has singleton faces for every effect family (`singletonFaces_of_relStrictConvex`), the two directions proved separately; each premise holds and fails on named bodies — singleton faces on every closed ball of a strictly convex space and not on the sup-norm square with its full effects, supporting-effect completeness on the segment `[-1, 1]` with its full effects and not with the unit alone, elementary drivability on the unit ball of `ℝ³` and not on the classical bit, and hypothesis K∞-1 for that ball with its full effects and not with the unit alone (`kInf1_ball3_full`, `not_kInf1_ball3_unit`); a centrally symmetric body admits at most two perfectly distinguishable states with any effects (Lemma D); a compact convex body with `0` in its interior whose frontier lies on the unit sphere is the closed unit ball (Lemma B); a finite stage exposes at most as many states as it has preparations, and a body on `N` ontic states meeting each coordinate facet in at most one point exposes at most `N` states by response effects (Theorem F2); joined in the verdict `kinf2_kernel_core`. The qubit certain face is a theorem of the imported matrix kinematics (`qubit_certain_face`), and hypothesis K∞-1 is the definition `KInf1`, proved for no physical family. In exact arithmetic replayed in CI, and not in the kernel, the round's probe instantiates the controls: the square gbit, the torus and Stiefel orbitopes and the regular pentagon violate singleton faces, the pentagon while strongly self-dual, transitive on ordered frames and of capacity two; the 3-ball satisfies every premise together; the SIC ball fails supporting-effect completeness with its response effects; the Carathéodory orbitope `C₂` has capacity three. Nothing here derives drivability, supporting effects, singleton faces or copy naturality from any OI construction; that corrected drivability excludes the square gbit and the rebit disk is a written argument and not a kernel statement; and nothing here is a reconstruction theorem.

**THE CLAUSE, carried at this mention — the result.**

> Round KINF-2 fixes the corrected field-neutral vocabulary of the pre-quantum operational completion — finite stages, effects, proper effects and certain faces, boundary states read in the body, supporting-effect completeness and singleton faces over proper effects, relative strict convexity, full effects, perfect distinguishability, central symmetry, elementary drivability as a group flow of automorphisms of the body, and copy naturality — in place of the vocabulary of the halted round KINF-1, and proves the lemmas that vocabulary supports together with a holding and a failing instance of each premise. It states hypothesis K∞-1 as a definition over compact convex bodies and proves it for no physical family. It sources none of its premises: it does not derive drivability, supporting effects, singleton faces or copy naturality from any OI construction, it does not decide which effects the completion makes available, it does not prove in the kernel that corrected drivability excludes the square gbit or the rebit disk, it freezes no self-duality or homogeneity premise, and it contains no reconstruction theorem. It edits no manuscript and no roadmap row.

The preregistered prediction, `KINF-2-FOUNDATIONS-PROVED` at strength *very high*, is met.

***

## The layers at `E`

| layer | what it certifies | where |
| --- | --- | --- |
| kernel, evidence level 2 | the frozen definitions; L1–L3 and L6; Lemma C `relStrictConvex_of_supporting_singleton` and its converse `singletonFaces_of_relStrictConvex`, each direction by its own theorem; L7 `relStrictConvex_of_strictConvex`; the semantic controls of the preregistration's Hazard 6, among them `ball3_drivable`, `not_drivable_Icc`, `kInf1_ball3_full` and `not_kInf1_ball3_unit`; Lemma D; Lemma B; the finite-exposure bounds; Theorem F2; `copyNatural_iff_apply`; `qubit_certain_face` (imported kinematics); `KInf1` as a definition with `relStrictConvex_of_kInf1`; the verdict `kinf2_kernel_core` | `verification/lean-mathlib/OIBridge/KInfFoundations.lean` |
| exact computation, replayed in CI | the twelve sections of the probe: the square gbit, the torus and Stiefel orbitopes, the 3-ball and the disk, the SIC ball, the Carathéodory orbitope `C₂`, the regular pentagon, the degenerate bodies, the route-neutrality controls and the countercontrols | `verification/lean/kinf2_foundations_probe.py` |
| written argument | the exclusion of the square gbit and the rebit disk by corrected drivability, which remains an open proof obligation; that strict convexity relative to the affine span gives the facet condition of Theorem F2; the reduction behind the pentagon's capacity bound | the preregistration |

## The kernel layer

The module at `E` is blob `3b8290838f1ee7006996db53a2f1d1a228249a08`, the reference implementation `3b8290838f1ee7006996db53a2f1d1a228249a08`: no departure. It carries the
frozen header and the frozen declarations — two structures, twenty-nine definitions and sixty-seven theorems — each
theorem followed by its `#print axioms` line. In the run at `E`'s predecessor every theorem reports axioms within
`[propext, Classical.choice, Quot.sound]`, and the release gate's `lean-axioms` step reports 5355 named results and
no sorry: the 5288 at `D` and the module's sixty-seven.

## The exact-computation layer

The probe has its frozen blob `3634e3d3b86405f90f7eecc7674d45442b235e7e`. Its summary line in run 36857990743, on `55134fab`, job 110354973691:

`kinf2_foundations_probe: OK -- 192 checks`

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `aa43e2d2` | the preregistration | 36841329495 | `success`, all 31 jobs; release gate 21 of 21, `lean-axioms` 5288 |
| `02a430a4` | stage 1: `controls.py` (`e0f6bb3c`), the probe, the workflow shard | 36850555101 | `success`, all 32 jobs; the KINF-2 shard `OK -- 192 checks` |
| `55b05059` | stage 2: the module without its verdict, the import, the census family | 36855272075 | `success`, all 32 jobs; release gate 21 of 21, `lean-axioms` 5354, no sorry |
| `55134fab` | stage 3: the verdict; the module is `3b829083` | 36857990743 | `success`, all 32 jobs; release gate 21 of 21, `lean-axioms` 5355, no sorry; twenty-one receipts holding and the 303 legacy records intact |

Each run is a `workflow_dispatch` run whose `head_sha` is the commit named, run to completion with no job cancelled,
act 42's dispatch-only exclusion shards included. Each commit has one parent, the row above it. The paths changed
from `D` are exactly the governed ones; no manuscript, built artifact, `verification/ROADMAP.md` or file of the
halted round KINF-1's record changed. `controls.py check E --freeze F` prints `controls: check OK`.

## What stays open

- Field-neutral drivability (K∞-R), supporting-effect completeness for the completion's effects (K∞-1), singleton
  faces (SF) and copy naturality: named here as definitions, discharged by no OI construction.
- That corrected drivability excludes the square gbit and the rebit disk: a written argument, and the proof
  obligation the preregistration records.
- Which effects the completion makes available, and any producer of relative strict convexity other than the
  singleton-face route.
- The passage from strict convexity relative to the affine span to the facet condition of Theorem F2, in the kernel.
