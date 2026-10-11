# Reconstruction round KTRANS-SEP-1 — boundary transitivity is not implied by the other single-system seams: PREREGISTRATION (draft for owner review)

**Status: research draft, not a control plane.** Written by the research thread `research/equivalence` (node E8) and
held on that branch under `research/equivalence/preregistration-drafts/` for owner review. No round is opened, no pull
request exists, nothing under `verification/` is written, no `D` is designated and no `F` exists. If the owner opens
the round, this text moves to the record directory below on a pull request from the designated `D`; every measurement
marked *(at L)* is re-taken at `D`; `controls.py` is generated; the predicted execution tree is built and dispatched;
and this file may change before `F` (`G9`). Measurements were taken at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`.

**Readiness (round 3).** Checkpoint `C0` is measured and met: the proof-only repair of the module's two failing terms
was built in design run 38096511360 with all fifteen prints standard (below), so every predicted output of the three
cells is generated from a measurement. The draft is ready for owner review on the same footing as S1–S3: what remains
unmeasured is what every draft lists — the predicted execution tree at a designated `D` (the module under its
predicted name `TransSeparation`, a rename of the measured text; the census family; `controls.py`; the probe shard).
One optional pre-`F` revision item, warnings only: the deprecated names `Set.mem_setOf_eq` and `push_neg` may be
replaced by `Set.mem_ofPred_eq` and `push Not`.

```v3-round
round KTRANS-SEP-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/
record AM verification/receipts/KTRANS-SEP-1.json
execution A verification/lean-mathlib/OIBridge/TransSeparation.lean
execution A verification/lean/ktrans_sep1_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

**No manuscript, no built artifact, `verification/ROADMAP.md`, no landed kernel module and no other round's record
change under any outcome.**

## The objects

- **`D`** — to be designated by the owner. Drafting measurements: L. **`F`**, **`E`**, **`Λ`**, **`Q`** as §A.39.

## What the round is

K∞-Trans (ROADMAP :1018–1022) is `BoundaryTransitive Ω G` (OrbitGeneration.lean:79), which TRB-1 consumes for the ball
(`exists_affine_image_eq_eball`, TransitiveBody.lean:602); KTRANS-DENSE-1 weakened it to `DenseBoundaryOrbit`
(DenseOrbit.lean:53) for eleven consumers. The ROADMAP records that a drive's flow is not boundary transitive on the
ball (`not_boundaryTransitive_flow`, OrbitGeneration.lean:620) and that "no theorem derives transitivity from
`ElementaryDrivability` on a general body". The round asks:

- **Q-SEP (kernel).** Is there a compact convex body with interior in `ℝ⁴` that is drivable (`ElementaryDrivability`,
  KInfFoundations.lean:264), carries a sharp seed (`SharpSeed`, OrbitGeneration.lean:65), is relatively strictly
  convex (`RelStrictConvex`, KInfFoundations.lean:144) and centrally symmetric (:160), and on which no body-preserving
  family is boundary transitive or has a dense boundary orbit? The witness is Ω₄ = {(x, s) ∈ ℝ³ × ℝ : ‖x‖⁴ + s⁴ ≤ 1}.
- **Q-NONELL (kernel, the decisive step).** Is Ω₄ an affine image of `eball 4`?
- **Q-EXACT (exact layer).** Do the exact checks hold as stated — including supporting-effect completeness of the full
  effects on Ω₄, through an exact sum-of-squares identity for the gradient gap of `F`, which the kernel layer does not
  prove — and do the Euclidean 4-ball controls pass the same checks with a consistent section system?

## The kernel declarations the round would add (frozen surface, module `OIBridge/TransSeparation.lean`)

Import `OIBridge.DenseOrbit`; namespace `OIBridge.TransSeparation`. The statement surface is the design module
`EqvOmega4` (copies: `research/equivalence/lean/EqvOmega4.run38090924005.lean`, the built blob `ee870649`, and
`research/equivalence/lean/EqvOmega4.lean`, the repaired blob `9030f471`, which differs from it in two proofs and one
unused simp argument only). Its declarations, in order:

- §A the body: `omega4 : Set (Fin 4 → ℝ) := {v | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1}`, `mem_omega4`,
  `vec4_ext`, `omega4_isCompact`, `conv_core`, `omega4_convex`, `abstract_strict`, `omega4_strictConvex :
  StrictConvex ℝ omega4`, `relStrictConvex_omega4`, `singletonFaces_omega4 (avail) : SingletonFaces omega4 avail`,
  `omega4_interior_nonempty`, `omega4_centrallySymmetric : CentrallySymmetric omega4 0`;
- §B the seed: `seed4 : (Fin 4 → ℝ) →ᵃ[ℝ] ℝ` (`v ↦ (1 + v 3)/2`), `seed4_apply`, `sharpSeed_omega4 : SharpSeed omega4
  seed4`;
- §C the drive: `rotFun4`, `rotFun4_apply`, `rotFun4_zero`, `rotFun4_add`, `rotFun4_mem_omega4`, `rotLin4`,
  `rotEquiv4`, `rot4`, `rot4_apply`, `cycEquiv4`, `cyc4`, `cyc4_apply`, `cyc4_symm_apply`, `cyc4_mem_omega4`,
  `cyc4_symm_mem_omega4`, `omega4Drive : ElementaryDrivability omega4` (flow: rotations of the first two coordinates;
  NOT: the half-turn; `J`: the cyclic permutation of the first three coordinates), `omega4_drivable`;
- §D the decisive step: `not_affine_eball_omega4 : ¬ ∃ A : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ), A '' omega4 = eball 4`;
- §E the separation:

```lean
theorem not_boundaryTransitive_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}
    (hG : PreservesBody omega4 G) : ¬ BoundaryTransitive omega4 G
theorem not_denseBoundaryOrbit_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}
    (hG : PreservesBody omega4 G) : ¬ DenseBoundaryOrbit omega4 G
theorem kinfTrans_separation :
    IsCompact omega4 ∧ Convex ℝ omega4 ∧ (interior omega4).Nonempty
      ∧ Nonempty (ElementaryDrivability omega4) ∧ SharpSeed omega4 seed4
      ∧ RelStrictConvex omega4 ∧ CentrallySymmetric omega4 0
      ∧ ∀ G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ)), PreservesBody omega4 G →
          ¬ BoundaryTransitive omega4 G ∧ ¬ DenseBoundaryOrbit omega4 G
```

The proof of `not_affine_eball_omega4`: for an affine `A` with `A '' Ω₄ = eball 4`, membership transfers in both
directions, and on the points `(u, 0, 0, s)` the sum `∑ j (A x j)²` is `u²α + s²β + 2usγ + 2ub₀ + 2sb₃ + P`; the eight
states `(±1, 0), (0, ±1), (±5/6, ±5/6)` give `≤ 1` and the eight points `(±1, ±1/2), (±1/2, ±1)` outside Ω₄ give `> 1`;
these sixteen linear inequalities in `(α, β, γ, b₀, b₃, P)` are infeasible (`linarith`; certificate: the eight outer
facts with weight `14/9`, the four axis states with weight `10/9`, the four diagonal states with weight `2`). The
separation then follows from TRB-1's `exists_affine_image_eq_eball` and KTRANS-DENSE-1's
`exists_affine_image_eq_eball_of_dense` by contraposition, with `omega4_isCompact`, `omega4_convex` and
`omega4_interior_nonempty`. `#print axioms` lines: fifteen, as in the design module.

**Census family:** "boundary transitivity is not implied by the other single-system seams: the l4-sum of the Euclidean
3-ball and the segment is a compact convex body with interior, drivable, with a sharp seed, relatively strictly convex
and centrally symmetric, is no affine image of the Euclidean ball, and admits no body-preserving family that is boundary
transitive or has a dense boundary orbit (round KTRANS-SEP-1, reconstruction)", `modules: ["TransSeparation"]`,
`status: "kernel-only"`, `manuscript: []`. **Import line** after `import OIBridge.RelcSelectC5`.

## The exact layer (frozen probe `verification/lean/ktrans_sep1_probe.py`)

The probe is the design probe `research/equivalence/experiments/e8_ktrans_probe.py` (sha256 `c32afda9…`; exact sympy
and rational arithmetic), frozen byte for byte. Its checks D1–D9 and C1, with their code, are those of
`e2_drive_trans.py` (sha256 `394850c8…`): D1–D5 (the drive's fields), D6 (the seed), D7 (central symmetry), D8 (exact
midpoints strictly inside), D9 (the section `{u⁴ + v⁴ ≤ 1}` is no conic `{Au² + 2Buv + Cv² ≤ 1}` through its exact
boundary points), C1 (the Euclidean 4-ball passes D1–D5 and its section system is consistent, `B = 0`). It adds:

- **W5** (supporting-effect completeness for the full effects): the Euler identity `∇F(p)·p = 4F(p)`, and the gradient
  gap of `F` as an explicit sum of squares, identically in `(y, p)`:
  `F(y) − F(p) − ∇F(p)·(y − p) = (|y_x|² − |p_x|²)² + 2|p_x|²|y_x − p_x|² + (y_s − p_s)²((y_s + p_s)² + 2p_s²)`;
  at the nine rational boundary points of D8 and two irrational ones, `p₁ = (√15/5, 0, 0, 2√5/5)` and
  `p₂ = (2^(−1/4), 0, 0, 2^(−1/4))`, the effect `e_p = (1 + ∇F(p)·y/4)/2` is `1` at `p` and `0` at `−p`; on a grid of
  1669 exact states the nine rational `e_p` take values in `[0, 1]`. With the written step in the probe's header (the
  boundary states of Ω₄ in the sense of `IsBoundaryState`, KInfFoundations.lean:130, are the points with `F = 1`; the
  identity gives `∇F(p)·y ≤ 4` on Ω₄; central symmetry gives `e_p ≥ 0`), every boundary state is certain for a proper
  full effect.
- **C2** (positive control): the same two identities on the Euclidean 4-ball, whose gap is `|y − p|²` — the form of
  the kernel's `supportingEffectComplete_ball3` (KInfFoundations.lean:1053).
- **XW1, XW2** (countercontrols, each must fail as stated): the sum of squares without its middle term is not an
  identity; at `p₁` the Euclidean-normal functional is certain at `p₁` but exceeds `1` at the exact state
  `(21/25, 0, 0, 21/25)` of Ω₄ (the sign of `(3/25)(√15 + 2√5) − 1` decided in rationals).

With the full effects, supporting-effect completeness holds on every compact convex body in finite dimension by the
supporting-hyperplane theorem [L] — recorded in the archive (`research/archive/threads/A/RESULT.md`, and
`research/archive/threads/F/LEDGER.md` row B8, the kernel candidate `supportingEffectComplete_fullEffects` [A]); W5 is
an explicit instance on Ω₄ and says nothing about an available effect family (K∞-1's content, `KInf1`
KInfFoundations.lean:1013). The coordinator's independent check X1 (the four zero curvatures of the quartic
section at its axis points; controls: the circle and an ellipse) is cited, not frozen.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Outcome | Rule |
|---|---|---|
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-PROVED` | `not_affine_eball_omega4` has its frozen statement, resolves `eball` to TRB-1's (TransitiveBody.lean:518), and is built at `E` with its `#print axioms` line within `[propext, Classical.choice, Quot.sound]` |
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-NOT-ESTABLISHED` | otherwise |
| Q-SEP | `KTRANS-SEP-SEPARATED` | `kinfTrans_separation` and every declaration it depends on in the module have their frozen statements, resolve to the landed objects, and are built at `E` with every frozen print within the three axioms |
| Q-SEP | `KTRANS-SEP-NOT-ESTABLISHED` | otherwise |
| Q-EXACT | `KTRANS-SEP-INSTANCES-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I`, prints `PASS` for D1–D9, W5, C1 and C2, no `FAIL`, `COUNTER XW1 fails as stated`, `COUNTER XW2 fails as stated`, `checks: 12, failures: 0` and `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS` |
| Q-EXACT | `KTRANS-SEP-INSTANCES-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `KTRANS-SEP-1-READ` when the three cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule (frozen)

> Earned reading (only when all three cells are positive): on a general body the other single-system seams do not give
> boundary transitivity or a dense boundary orbit: a compact convex body with interior in R^4 that is drivable, carries
> a sharp seed, is relatively strictly convex and centrally symmetric admits no body-preserving family that is boundary
> transitive or has a dense boundary orbit.

> Non-inference rule: this round says nothing about which bodies OI supplies, nothing about chart dimension 3, and
> nothing about the composite. It does not show that boundary transitivity or a dense boundary orbit is false for the
> bodies OI would supply; it shows only that the other single-system seams, in the form the kernel states them, do not
> imply it. Supporting-effect completeness of the full effects on the body is checked as an exact identity with a
> written step, holds with the full effects on every compact convex body in finite dimension, and is not a kernel
> theorem of this round. The probe is an exact computation, not a Lean kernel proof.

**Premise this round does NOT source:** boundary transitivity and its dense form themselves — the round is a separation,
it shows they must come from their own source; and none of drivability, seed, strict convexity or symmetry for any OI
object.

## The ROADMAP wording the round would license (HP-1, row K∞-Trans; not applied by the round)

At L, ROADMAP :1018–1022 ends: "K∞-Drive does not give it: a drive's flow preserves the ball and a sharp seed and is not
boundary transitive (`not_boundaryTransitive_flow`), and no theorem derives transitivity from `ElementaryDrivability`
on a general body." Under `KTRANS-SEP-1-READ` with all three cells positive the last clause may be replaced by: "and on
a general body the other single-system seams do not give it: a strictly convex, drivable, centrally symmetric body of
chart dimension 4 with a sharp seed admits no boundary-transitive family and no dense boundary orbit
(`kinfTrans_separation`)." HP-1's further phrase "and supporting-effect completeness" is licensed **only** if a later
revision moves W5 into the kernel layer; under this draft it is not, and it is better omitted in any case: with the full
effects the property holds on every compact convex body in finite dimension (the supporting-hyperplane theorem; thread
F's B8 [A]), so it adds nothing about Ω₄, and K∞-1's content lies in the available effect family. K∞-Trans stays OPEN
under every outcome.

## The controls (in `controls.py`)

- **S1 surface**: preamble, every declaration in order and by kind, every theorem's signature, every definition whole
  (`omega4`, `seed4`, `rotFun4`, `rotLin4`, `rotEquiv4`, `rot4`, `cycEquiv4`, `cyc4`, `omega4Drive`), fifteen prints.
  Mutations, each failing with its code: the exponent 4 of the last coordinate in `omega4` replaced by 2 (the body
  becomes the Euclidean ball — then `not_affine_eball_omega4` is false, and the frozen statement check fails first);
  `RelStrictConvex` dropped from `kinfTrans_separation`; `PreservesBody` dropped from `not_boundaryTransitive_omega4`;
  `J` replaced by `rot4 (π/2)` in `omega4Drive` (then `J_off_axis` fails — the build control); a sixteenth print.
- **S2 resolution**: `ElementaryDrivability`, `SharpSeed`, `RelStrictConvex`, `SingletonFaces`, `CentrallySymmetric`,
  `PreservesBody`, `BoundaryTransitive`, `DenseBoundaryOrbit`, `eball`, `exists_affine_image_eq_eball`,
  `exists_affine_image_eq_eball_of_dense`, `relStrictConvex_of_strictConvex`, `singletonFaces_of_relStrictConvex`
  resolve to the landed declarations at `D`. Mutation: a local `eball`.
- **S3 positive control (exact layer)**: the Euclidean 4-ball passes D1–D5 and its section system is consistent (C1),
  so the non-ellipse step is not vacuous; C2 gives the ball's gradient-gap identity, and XW1, XW2 show that W5 can
  fail. The kernel form of the positive control is landed at every dimension, `d = 4`
  included: `boundaryTransitive_fullAut : BoundaryTransitive (eball d) (fullAut d)` (EffectSpace.lean:337); S2 reads its
  statement at `D`, so the separation's negative clauses are checked against a body on which the same clauses are
  positive.
- **S4 phrases** (header, result note): "OI supplies", "K∞-Trans is false", "transitivity fails for OI", "replaces
  K∞-Trans", "K∞-Trans is not needed", "chart dimension 3", "every body", "kernel proof of" (for the probe), "design
  module", "not for merge".
- **P, W, V, I, C, R, G** as KINF-COPY-1.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the module was built before `F` (this draft's open hazard) | `C0`: a design run of the repaired module, green at the Mathlib bridge build with all fifteen prints standard, recorded in this file before `F` — **measured: run 38096511360 (job 114343410536), met**; the predicted tree's run at `D` remains with every draft's unmeasured items |
| the controls and the probe are the frozen ones | `C2`: blobs at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job `success`; the fifteen prints, none with `sorryAx` |
| the exact layer replays and renders | `C3`: shard `probes_ktranssep1` green with `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS`; the aggregate job green |
| the module is registered; no manuscript changes | `C4`: the release gate at `E` passing every step |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design evidence and the predicted outputs

| run | commit | workflow run | measured |
|---|---|---|---|
| 1 | `195dfbee` (`dev-equivalence/omega4`, based on L; module `EqvOmega4`, blob `ee870649`) | 38090924005 | Mathlib bridge job 114327010280: **build failed** at two terms only, `EqvOmega4.lean:157:16` and `:215:16` (`fun v hv => le_of_lt hv` elaborated against `v ∈ omega4`: Type mismatch). Prints `[propext, Classical.choice, Quot.sound]` for `omega4_isCompact`, `conv_core`, `omega4_convex`, `abstract_strict`, `omega4_centrallySymmetric`, `sharpSeed_omega4`, `omega4_drivable`, `not_affine_eball_omega4`; `sorryAx` (error recovery at the two terms) for `omega4_strictConvex`, `relStrictConvex_omega4`, `singletonFaces_omega4`, `omega4_interior_nonempty`, `not_boundaryTransitive_omega4`, `not_denseBoundaryOrbit_omega4`, `kinfTrans_separation` |
| repair | `95beab2b` (blob `9030f471`) | — (not dispatched in round 2: that round's one dispatch for this draft was run 1) | each failing term replaced by `by simp only [Set.mem_setOf_eq] at hv; rw [mem_omega4]; exact le_of_lt hv`; one unused simp argument dropped; no statement changed |
| 2 (`C0`, round 3) | `95beab2b` (`dev-equivalence/omega4`, blob `9030f471`) | 38096511360 | Mathlib bridge job 114343410536: `Build completed successfully (3644 jobs)`; `EqvOmega4` built with warnings only (deprecated `Set.mem_setOf_eq`, `push_neg`; one `unnecessarySeqFocus` lint); **all fifteen prints** (`EqvOmega4.lean:530–544`) `[propext, Classical.choice, Quot.sound]`; release gate every step PASS except `lean-manuscript` (1 problem: the unregistered module), `lean-axioms` 5875, no sorry, 303 legacy records intact, 43 receipts hold |
| exact (round 1) | `research/equivalence` | `e2_drive_trans` (local; replayed by the coordinator; decisive step independently confirmed as X1) | 10 checks, 0 failures, `VERDICT DRIVE-SEED-GEOM-CAP2-NOT-TRANS` |
| exact (the probe to freeze) | `research/equivalence` | `e8_ktrans_probe` run 1 (local, `python3 -I -B`; replay byte-identical; py `c32afda9…`, out `d6f6d298…`) | 12 checks, 0 failures; `COUNTER XW1 fails as stated`, `COUNTER XW2 fails as stated`; grid of 1669 states; `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS` |

**Predicted outputs, generated from those measurements by the rules:** Q-NONELL `KTRANS-SEP-NONELLIPSOID-PROVED`
(runs 1 and 2: `not_affine_eball_omega4` built with standard axioms). Q-SEP `KTRANS-SEP-SEPARATED` (run 2:
`kinfTrans_separation` and every declaration it depends on in the module built, all fifteen prints within the three
axioms; in run 1 its dependants had printed `sorryAx`). Q-EXACT `KTRANS-SEP-INSTANCES-EXACT` is generated from the run
of `e8_ktrans_probe` (`checks: 12, failures: 0`, both countercontrols failing as stated, the verdict token), the frozen
probe being that blob (checkpoint `C2`). The rules, not this reading, are what a frozen file would fix; the predicted
execution tree at `D` (the module renamed `TransSeparation`, the census family, `controls.py`, the probe shard) is
not yet measured.

## Stages and outcomes

Stages as KT4-PREM-1, preceded by `C0` (met in design run 38096511360). **`KTRANS-SEP-1-READ`**: `controls.py check E --freeze F` OK, three tokens
printed, the exact-head run at `E` green on every job. **`KTRANS-SEP-1-HALTED`**: anything else (`S12`). No outcome
sources boundary transitivity or edits the ROADMAP or a manuscript; correctness bands unchanged (consistency axis).
