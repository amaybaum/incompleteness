# Reconstruction round KTRANS-SEP-1 — Ω₄, a body with the named single-system properties on which no body-preserving family is boundary transitive: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** This file is the control
plane of a native round under `AGENTS.md` §A.39, drafted on its pull request from `D`. Only the owner designates `F`;
an instruction to proceed is not a designation. Before `F` the predicted execution tree must have its design run and
that run's retained result must be pinned below (one pin is pending), and the owner decisions listed at the end must be
made. Nothing is executed.

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

The record directory holds this preregistration, the round's frozen controls `controls.py`, the retained evidence under
`evidence/` (the pinned files below and `evidence/f-run/results.json`), any amendments under `amendments/`, and the
result note `result.md`. The receipt path is `verification/receipts/KTRANS-SEP-1.json`. Every other path the round
changes is an execution path listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, no landed
kernel module and no other round's record change under any outcome.**

## The objects

- **`D`** = `ec36234cb98a30ecb4681e118ff9ccb82e19aa6d`, the head of `main` after #877.
  Its push run 39163508631 (head `ec36234cb98a30ecb4681e118ff9ccb82e19aa6d`) concluded `success`: 22 of its 23 jobs
  `success` and the Act 42 exclusion job `skipped`, as on every push (`evidence/d-push-run.json`).
- **`F`** — the commit carrying this file that the owner designates; `delta(D, F)` is this file and any amendments.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

**Drift from the design base to `D`, measured.** The module was designed and built on `main` at
`9f9f8257a980a1819fbbc1dc0019917cf8678626` (the design base `L`). From `L` to `D`: all 31 modules of
`OIBridge.DenseOrbit`'s import closure, `lakefile.toml`, `lean-toolchain` and `lake-manifest.json` under
`verification/lean-mathlib/` are byte-identical, so every kernel line reference below holds at `D` and the design
builds bear on the module at `D`. At `D` the K∞-Trans block of `verification/ROADMAP.md` is `:1031–1035`, the last
import line of `OIBridge.lean` is `import OIBridge.TurnpikePremiseOrientation` (`:269`), the last census family is
BG-2's, and in `verify.yml` BG-2's shard `probes_bg2` directly precedes the Act 42 comment (`:462`); the import line,
the census family and the workflow splices below are anchored there.

## What the round is

K∞-Trans (ROADMAP `:1031–1035`) is `BoundaryTransitive Ω G` (OrbitGeneration.lean:79), which TRB-1 consumes for the
ball (`exists_affine_image_eq_eball`, TransitiveBody.lean:602); KTRANS-DENSE-1 states it in the weaker form
`DenseBoundaryOrbit` (DenseOrbit.lean:53, with `exists_affine_image_eq_eball_of_dense`, DenseOrbit.lean:174). The
ROADMAP records that a drive's flow is not boundary transitive on the ball (`not_boundaryTransitive_flow`,
OrbitGeneration.lean:620) and that "no theorem derives transitivity from `ElementaryDrivability` on a general body".

The round proves one existential statement in the kernel. The witness is
Ω₄ = {(x, s) ∈ ℝ³ × ℝ : ‖x‖⁴ + s⁴ ≤ 1} ⊂ ℝ⁴. The named properties are the kernel predicates:

| property | kernel predicate | where |
|---|---|---|
| compact convex body with interior | `IsCompact`, `Convex ℝ`, `(interior _).Nonempty` | Mathlib |
| drivability (the kernel object of K∞-Drive) | `ElementaryDrivability` | KInfFoundations.lean:264 |
| a sharp seed (the kernel object of K∞-Seed) | `SharpSeed` | OrbitGeneration.lean:65 |
| relative strict convexity | `RelStrictConvex` | KInfFoundations.lean:144 |
| central symmetry | `CentrallySymmetric` | KInfFoundations.lean:160 |

`RelStrictConvex` gives `SingletonFaces` for every effect family (`singletonFaces_of_relStrictConvex`,
KInfFoundations.lean:590), the singleton-face content the ROADMAP names under K∞-Geom; the ROADMAP records that a
corrected K∞-Geom statement is not frozen, and this round states the property only as `RelStrictConvex`.

- **Q-NONELL (kernel, the decisive step).** Is Ω₄ an affine image of `eball 4`?
- **Q-CEX (kernel).** Does Ω₄ have every property of the table while no body-preserving family on it is
  `BoundaryTransitive` or has a `DenseBoundaryOrbit`? A positive answer makes Ω₄ a counterexample to the implication
  from those properties, for body-preserving families, to `BoundaryTransitive` and to `DenseBoundaryOrbit`.
- **Q-EXACT (exact layer).** Do the exact checks of the frozen probe and of the controls' independent exact layer hold
  as stated, with their positive controls and countercontrols?

The statement is about Ω₄. It is not a statement about every compact convex body with these properties: the Euclidean
4-ball has all of them and is boundary transitive under its full automorphism family (`boundaryTransitive_fullAut`,
EffectSpace.lean:337), which is countercontrol CX1. It says nothing about chart dimension 3, and nothing about
K∞-Stage, K∞-Act, K∞-V4 or K∞-Copy, whose kernel objects do not occur in it.

## The kernel declarations the round adds (frozen surface, module `OIBridge/TransSeparation.lean`)

The module is blob **`9093a86e0dec96dd1217613520c2ba0666292935`**. It imports `OIBridge.DenseOrbit` only; namespace
`OIBridge.TransSeparation`; one `open` line, `open Set KInfFoundations OrbitGeneration TransitiveBody DenseOrbit`.
It is the repaired design module of the design runs below with three changes and no other: the namespace
`EqvOmega4` renamed `TransSeparation` (in the `namespace` and `end` lines and the fifteen `#print axioms` lines), the
header comment rewritten, and the docstring of `kinfTrans_separation` rewritten. No statement, definition, binder or
proof changed. Its 36 declarations, in order:

- §A the body: `omega4 : Set (Fin 4 → ℝ) := {v | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1}`, `mem_omega4`,
  `vec4_ext`, `omega4_isCompact`, `conv_core`, `omega4_convex`, `abstract_strict`, `omega4_strictConvex :
  StrictConvex ℝ omega4`, `relStrictConvex_omega4`, `singletonFaces_omega4 (avail) : SingletonFaces omega4 avail`,
  `omega4_interior_nonempty`, `omega4_centrallySymmetric : CentrallySymmetric omega4 0`;
- §B the seed: `seed4 : (Fin 4 → ℝ) →ᵃ[ℝ] ℝ` (`v ↦ (1 + v 3)/2`), `seed4_apply`,
  `sharpSeed_omega4 : SharpSeed omega4 seed4`;
- §C the drive: `rotFun4`, `rotFun4_apply`, `rotFun4_zero`, `rotFun4_add`, `rotFun4_mem_omega4`, `rotLin4`,
  `rotEquiv4`, `rot4`, `rot4_apply`, `cycEquiv4`, `cyc4`, `cyc4_apply`, `cyc4_symm_apply`, `cyc4_mem_omega4`,
  `cyc4_symm_mem_omega4`, `omega4Drive : ElementaryDrivability omega4` (flow: rotations of the first two coordinates;
  NOT: the half-turn; `J`: the cyclic permutation of the first three coordinates), `omega4_drivable`;
- §D the decisive step: `not_affine_eball_omega4 : ¬ ∃ A : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ), A '' omega4 = eball 4`;
- §E the counterexample:

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
facts with weight `14/9`, the four axis states with weight `10/9`, the four diagonal states with weight `2`, which
controls X1–X3 check exactly against the module's own points). The negative clauses then follow from TRB-1's
`exists_affine_image_eq_eball` and KTRANS-DENSE-1's `exists_affine_image_eq_eball_of_dense` by contraposition, with
`omega4_isCompact`, `omega4_convex`, `omega4_interior_nonempty` and the hypothesis `PreservesBody omega4 G`.

**Design-run rule.** A repair may change theorem proofs only. No repair may strengthen or weaken a frozen statement,
definition, binder, docstring or context line; control N2 compares the module with its proofs elided against the frozen
skeleton embedded in `controls.py`. A statement mismatch returns the round to design; it is never repaired in execution.

**`#print axioms` lines:** fifteen, `:532–546` of the module, naming `omega4_isCompact`, `conv_core`, `omega4_convex`,
`abstract_strict`, `omega4_strictConvex`, `relStrictConvex_omega4`, `singletonFaces_omega4`,
`omega4_interior_nonempty`, `omega4_centrallySymmetric`, `sharpSeed_omega4`, `omega4_drivable`,
`not_affine_eball_omega4`, `not_boundaryTransitive_omega4`, `not_denseBoundaryOrbit_omega4` and
`kinfTrans_separation` under `OIBridge.TransSeparation.`. None of the fifteen short names occurs in a `#print axioms`
line at `D`.

**Import line:** `import OIBridge.TransSeparation`, inserted in `OIBridge.lean` directly after
`import OIBridge.TurnpikePremiseOrientation` (`:269` at `D`).

**Census family**, inserted directly after BG-2's family (modules `["TurnpikePremiseOrientation"]`), in `D`'s two-space
JSON layout: name "Ω₄, the ℓ⁴-sum of the Euclidean 3-ball and the segment, is compact, convex, with interior, drivable,
with a sharp seed, relatively strictly convex and centrally symmetric, is no affine image of the Euclidean ball, and
admits no body-preserving family that is boundary transitive or has a dense boundary orbit (round KTRANS-SEP-1,
reconstruction)", `modules: ["TransSeparation"]`, `status: "kernel-only"`, `manuscript: []`.

## The exact layer

**The frozen probe** `verification/lean/ktrans_sep1_probe.py`, blob **`19e19f28fa7644de0bcc3089a354317310de3e41`**,
imports `sys`, `itertools`, `fractions` and `sympy` (pinned `1.14.0` in its shard) and reads no file. Exact
arithmetic only. Its checks:

- D1–D5, the drive's fields; D6, the seed; D7, central symmetry; D8, exact midpoints of nine rational boundary points
  strictly inside; D9, the section `{u⁴ + v⁴ ≤ 1}` is no conic `{Au² + 2Buv + Cv² ≤ 1}` through its boundary points;
- C1, positive control: the Euclidean 4-ball passes D1–D5 and its section system is consistent (`B = 0`);
- W5, supporting-effect completeness for the full effects on Ω₄: the Euler identity `∇F(p)·p = 4F(p)` and the gradient
  gap of `F` as an explicit sum of squares, identically in `(y, p)`,
  `F(y) − F(p) − ∇F(p)·(y − p) = (|y_x|² − |p_x|²)² + 2|p_x|²|y_x − p_x|² + (y_s − p_s)²((y_s + p_s)² + 2p_s²)`,
  with exact instances at eleven boundary points and on a grid of 1669 exact states;
- C2, positive control: the same identities on the Euclidean 4-ball, whose gap is `|y − p|²`, the form of the kernel's
  `supportingEffectComplete_ball3` (KInfFoundations.lean:1053);
- XW1, XW2, countercontrols that must fail as stated: the sum of squares without its middle term is not an identity;
  at an irrational boundary point the Euclidean-normal functional is certain there and exceeds `1` at an exact state of
  Ω₄.

Its written steps (W1–W5) are stated in its own docstring. The probe exits 0 in every case; its verdict is read from its
output. With the full effects, supporting-effect completeness holds on every compact convex body with interior in
finite dimension by the supporting-hyperplane theorem; W5 is an explicit instance on Ω₄ and concerns no available
effect family (K∞-1's content, `KInf1`, KInfFoundations.lean:1013).

The probe is the research thread's design probe with its docstring replaced by a self-contained one: the design
probe's docstring deferred its written steps to a second research script that `main` does not carry. With the
docstrings removed the two files are byte-identical, and both print the same output byte for byte (sha256 `d6f6d298…`,
recorded in `evidence/exact-replay.json`).

**The independent exact layer** is in `controls.py` (`controls.py exact`, standard library and rationals only, sharing
no code with the probe):

- **X1** the eight states of the decisive step lie in Ω₄ and the eight points lie outside it, exactly;
- **X2** the sixteen inequalities are infeasible: the frozen positive weights cancel every coefficient and the
  constant (a Farkas certificate);
- **X3** those sixteen points are the ones the module's proof of `not_affine_eball_omega4` states, read from the module
  at the commit under check, so the exact check is about the module's own construction.

**Countercontrols where a credited hypothesis is dropped.** Each exhibits a countermodel on which the conclusion fails
once the hypothesis is removed; each must hold as stated.

- **CX1 (non-ellipsoidality dropped: the ball).** On the Euclidean 4-ball the seed `(1 + s)/2`, central symmetry, the
  drive's rotation and cyclic map, and strict midpoints hold at 1281 exact states; the sixteen-point system with the
  ball's own states is feasible (the witness `α = β = 1`, the rest `0`); and a state of Ω₄'s certificate is not a
  ball state. With S3 (the landed `fullAut`, `preservesBody_fullAut`, `boundaryTransitive_fullAut` at `D`), a body with
  every named property carries a body-preserving boundary-transitive family. The decisive step is what makes Ω₄ a
  counterexample.
- **CX2 (`PreservesBody` dropped).** Translations carry each of nine boundary points of Ω₄ to each other, and each
  nonzero translation moves an exact state of Ω₄ out of it: the translations are boundary transitive on Ω₄ and not
  body-preserving.
- **CX3 (`IsCompact` dropped).** The half-space `{s ≤ 1}` with the translations of zero last coordinate: they preserve
  it and carry each of 25 boundary points to each other; it is unbounded, so no affine image of `eball 4`.
- **CX4 (nonempty interior dropped).** The segment `[−e₀, e₀]` with `{id, −id}`: `−id` preserves it and exchanges its
  two endpoints; it has empty interior, so no affine image of `eball 4`.

CX2–CX4 are exact instances with written steps (that the listed points are the boundary states, and the general
pair). No countercontrol is recorded for `Convex`: none was sought. `ElementaryDrivability`, `SharpSeed`,
`RelStrictConvex` and `CentrallySymmetric` are properties Ω₄ is shown to have; the negative clauses do not use them,
so dropping one has no countermodel to exhibit.

## The decision rules (frozen; implemented by `controls.py verdict`)

`LOG` is the served text of the Mathlib bridge job of the exact-head run at `E`. `controls.py verdict E --freeze F
--log LOG` first runs every control of `check E --freeze F`; it prints `VERDICT  VOID` and no token unless every
required control ran and passed.

| Cell | Outcome | Rule |
|---|---|---|
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-PROVED` | S1 holds for `not_affine_eball_omega4`, and `LOG` has the build line, the release gate's PASS verdict and exactly one report of `not_affine_eball_omega4` at its `#print axioms` line, within `[propext, Classical.choice, Quot.sound]` |
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-NOT-ESTABLISHED` | otherwise |
| Q-CEX | `KTRANS-SEP-COUNTEREXAMPLE-PROVED` | S1 holds for `omega4`, `not_affine_eball_omega4`, `not_boundaryTransitive_omega4`, `not_denseBoundaryOrbit_omega4` and `kinfTrans_separation`, and `LOG` has the build line, the gate's PASS verdict and exactly one report for each of the fifteen prints at its line, each within the three axioms |
| Q-CEX | `KTRANS-SEP-COUNTEREXAMPLE-NOT-ESTABLISHED` | otherwise |
| Q-EXACT | `KTRANS-SEP-INSTANCES-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I -B`, prints exactly the frozen output (sha256 `d6f6d298d3ed57081f4e81bef267771fc81d8083a111c0414a69216c772a2940`), which contains the twelve `PASS` lines, `COUNTER XW1 fails as stated`, `COUNTER XW2 fails as stated`, `checks: 12, failures: 0` and `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS`; and X1–X3 and CX1–CX4 hold |
| Q-EXACT | `KTRANS-SEP-INSTANCES-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `#print axioms` reports every axiom of a declaration's dependency closure, so a
`sorry` anywhere beneath a printed theorem shows in its report; N3 also rejects one in the module's text. The outcome
is `KTRANS-SEP-1-READ` when the three cells are assigned; the tokens are those `controls.py verdict E` prints.

**No vacuous verdict.** An empty or truncated `LOG`, a log without the build line or with a failed gate, a missing,
duplicated or misplaced report, a report with an axiom outside the three, a probe output reduced to its summary lines,
and a required control that failed or never ran each withhold the positive token they bear on; the self-test drives
each case.

## The earned reading and the non-inference rule (frozen)

> Earned reading: Omega4 = {(x, s) in R^3 x R : |x|^4 + s^4 <= 1} is compact, convex and has nonempty interior,
> satisfies ElementaryDrivability, carries the sharp seed seed4, and is RelStrictConvex and CentrallySymmetric about 0;
> no body-preserving family of affine equivalences of R^4 is BoundaryTransitive or has a DenseBoundaryOrbit on Omega4
> (kinfTrans_separation). Omega4 is therefore a counterexample to the implication from these properties, for
> body-preserving families, to BoundaryTransitive and to DenseBoundaryOrbit.

> Non-inference rule: the round concerns Omega4 alone, in chart dimension 4. It states nothing about other compact
> convex bodies, about chart dimension 3, about K-infinity-Stage, K-infinity-Act, K-infinity-V4 or K-infinity-Copy,
> about the composite, or about which bodies OI supplies; on the Euclidean ball every one of the named properties holds
> and the full automorphism family is boundary transitive (boundaryTransitive_fullAut). RelStrictConvex is the form in
> which the kernel gives singleton faces for every effect family; it is not a frozen statement of K-infinity-Geom.
> Supporting-effect completeness of the full effects on Omega4 is an exact identity with a written step, not a kernel
> theorem of this round. The exact layer is an exact computation, not a Lean kernel proof.

The result note states the earned reading in these words exactly when all three cells are positive, and the
non-inference rule in these words under every outcome (control V, whitespace-normalized).

**Premise this round does not source:** boundary transitivity and its dense form; and none of drivability, the seed,
strict convexity or symmetry for any OI object.

## The ROADMAP wording the round would license (row K∞-Trans; not applied by the round)

At `D`, ROADMAP `:1031–1035` ends: "K∞-Drive does not give it: a drive's flow preserves the ball and a sharp seed and is
not boundary transitive (`not_boundaryTransitive_flow`), and no theorem derives transitivity from
`ElementaryDrivability` on a general body." Under `KTRANS-SEP-1-READ` with all three cells positive, a later edit may
add: "On Ω₄, a compact convex body of chart dimension 4 that satisfies `ElementaryDrivability`, carries a sharp seed and
is relatively strictly convex and centrally symmetric, no body-preserving family is boundary transitive or has a dense
boundary orbit (`kinfTrans_separation`)." K∞-Trans stays open under every outcome.

## The workflow edit (frozen)

`.github/workflows/verify.yml` at `E` is `D`'s with five splices, each anchored once at `D`:

- the shard `probes_ktranssep1`, `Numerical probes / KTRANS-SEP-1 Omega4 counterexample`, inserted directly before the
  Act 42 comment (`:462`), after BG-2's shard. It checks out with `fetch-depth: 0` (the controls read `D` through git),
  sets up Python 3.11, installs `sympy==1.14.0`, and runs three steps: the probe from `verification/lean` with
  `python3 -I -B`, its output kept and the step failing unless the line
  `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS` is present (the probe itself exits 0); `controls.py exact`; and
  `controls.py --self-test`;
- in the aggregate `Numerical probes` job: `probes_ktranssep1` after `probes_bg2` in `needs` (`:557`);
  `KTRANSSEP1_RESULT: ${{ needs.probes_ktranssep1.result }}` after `BG2_RESULT` (`:577`);
  `echo "ktranssep1=${KTRANSSEP1_RESULT}"` after the BG-2 echo (`:598`); `test "${KTRANSSEP1_RESULT}" = success`
  after the BG-2 test (`:618`).

The exact text is embedded in `controls.py` (control W).

## The controls (in `controls.py`)

`controls.py` imports nothing from the repository and changes nothing; it reads `D` and the commits it is given with
read-only git commands and embeds every frozen text. Its codes:

- **G** governed paths: `delta(D, commit)` is exactly the five execution paths with their statuses, plus record files.
- **R** record: only the permitted files; `evidence/f-run/results.json` required with `--freeze`; the result note
  required at `E` and absent at `S1`.
- **P** pins: every file pinned in *Retained evidence* is present with its sha256; the table names the four required
  files; with `--freeze` no pin is pending; `F`'s retained run names `F`, is a `workflow_dispatch` run and is green on
  every job.
- **T** chain (with `--freeze`): `D..commit` is one chain of single-parent commits through `F`; `delta(D, F)` is the
  control plane; the preregistration at the commit is `F`'s. The check is on commit identity: a re-cut `F` with the
  same bytes is not on the chain and fails.
- **B** blobs: the probe is the frozen blob, and `controls.py` at the commit is the file running.
- **N1** the 36 declarations in order and by kind; **N2** the frozen skeleton (the module with each theorem's proof
  elided); **N3** hygiene (no `sorry`, `admit`, axiom or opaque declaration, `native_decide`, `implemented_by`,
  `extern`, `unsafe`).
- **S1** the load-bearing statements: `omega4`, `not_affine_eball_omega4`, `not_boundaryTransitive_omega4`,
  `not_denseBoundaryOrbit_omega4`, `kinfTrans_separation`.
- **S2** resolution: `BoundaryTransitive`, `PreservesBody`, `SharpSeed` (OrbitGeneration), `DenseBoundaryOrbit`,
  `exists_affine_image_eq_eball_of_dense` (DenseOrbit), `ElementaryDrivability`, `RelStrictConvex`, `SingletonFaces`,
  `CentrallySymmetric`, `IsBoundaryState`, `relStrictConvex_of_strictConvex`, `singletonFaces_of_relStrictConvex`
  (KInfFoundations), `eball`, `exists_affine_image_eq_eball` (TransitiveBody) have their frozen texts at `D` and are
  each declared exactly once in the module's 31-module import closure; the module imports only `OIBridge.DenseOrbit`,
  has the frozen `open` line, and declares no name its import closure declares. Mathlib names are compared as text
  and resolved by the build.
- **S3** the kernel's positive control at `D`: `fullAut`, `preservesBody_fullAut` (EffectSpace.lean:230) and
  `boundaryTransitive_fullAut` (EffectSpace.lean:337) have their frozen texts.
- **S4** phrases, in the module header and, at a commit carrying it, in the result note outside its two frozen texts
  (case-insensitive, backticks removed, whitespace-normalized): "other single-system seams", "single-system seams",
  "every compact convex body", "all compact convex bodies", "every body", "all bodies", "any compact convex body",
  "is not implied by", "are not implied by", "OI supplies", "OI provides", "K∞-Trans is false", "transitivity fails for
  OI", "replaces K∞-Trans", "K∞-Trans is not needed", "K∞-Trans is independent", "independent of K∞-Trans",
  "K∞-Stage", "K∞-Act", "K∞-V4", "chart dimension 3", "in dimension three", "kernel proof of", "design module", "not
  for merge", "not adopted", "disposable branch", " iff ", "if and only if", "is equivalent to", "are equivalent",
  "exactly when". The equivalence phrases keep §A.34's rule: the round states one direction and displays no
  equivalence.
- **S5** exactly the fifteen frozen `#print axioms` lines, in order and distinct, each naming a module theorem.
- **X1–X3** and **CX1–CX4**: the independent exact layer above.
- **I** imports, **C** census, **W** workflow: `D`'s files with exactly the frozen edits.
- **V** note: at a commit carrying the result note, exactly the computed tokens, the earned reading exactly when all
  three cells are positive, the non-inference rule always; `--log` is required there.

**Self-test** (`controls.py --self-test`, run in the shard): it reads the frozen module and probe by blob id and drives
a mutation through every control, each failing with its code, and alone where marked: an extra declaration (N1); a
changed `conv_core` hypothesis (N2 alone), a changed `seed4` constant, `J` replaced by a rotation (N2); a `sorry` (N3
alone), `native_decide` (N3); the exponent of the last coordinate in `omega4` 4 → 2, so that the body becomes the ball,
`RelStrictConvex` dropped from `kinfTrans_separation`, nonempty interior dropped, `PreservesBody` dropped from
`not_boundaryTransitive_omega4`, `eball 4` → `eball 3` (S1); a local `eball`, `DenseOrbit` dropped from the `open`
line, a second import, a landed statement differing at `D` (S2, the last alone); a landed ball control differing (S3
alone); three header phrases (S4); a sixteenth and a duplicated print (S5); an outer point moved inside (X1), a changed
or zero weight (X2 alone), a module point changed (X3 alone), the ball's witness zeroed (CX1 alone), the translations
replaced by the identity (CX2 alone), a half-space translation with a nonzero last coordinate (CX3 alone), the segment
family reduced to `{id}` (CX4 alone); the probe output with a `PASS` turned `FAIL`, with a countercontrol that did not
fail, reduced to its summary, or empty; the log cases of *No vacuous verdict*; the verdict gate with each required
control failed or missing; the note with an extra token, an altered earned reading, no non-inference rule, the earned
reading under a negative cell, and a frozen phrase (a neutral addition passes); and the pure cores of I, C, W, G, R, P
and T, including a merge, a re-cut `F` and an `F` not on `D`. Positive controls: the frozen module, the landed ball
control, the exact layer, the frozen probe run, a proof-only repair, and a log with every frozen report standard. It
passes 71 checks.

`controls.py` is blob **`05793664e1c01d9186fae62fada2f77638b5102d`** (1423 lines), generated from the frozen module,
the frozen probe and its output, and `D`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F`; `T` in `controls.py check E --freeze F` |
| the controls, module and probe are the frozen ones | `C2`: `git rev-parse <commit>:<path>` equal to the frozen blobs, for `controls.py` at stage 1 and all three at `E`; `B`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms; no `sorryAx` | `C3`: the exact-head run at `E`, every job `success`; the fifteen reports read by `controls.py verdict E --freeze F --log LOG` |
| the decisive step is the module's own construction | `C5`: X3 in `check E --freeze F` |
| the exact layer replays; its countercontrols fail as stated | `C3`: shard `probes_ktranssep1` green; `verdict` re-runs the probe blob at `E` against the frozen output digest |
| no positive token over a failed or missing control | `C5`: the verdict gate; its self-test cases run in the shard at `E` |
| the module is registered; no manuscript or ROADMAP changes | `C4`: the release gate at `E` passing every step, `lean-manuscript` and `evidence-retention` included; `C5` (C, G) |
| the change stays inside the governed paths, with exactly the frozen import, census and workflow edits | `C6`: `git diff --no-renames --name-status D E`; `C5` (G, I, C, W) |
| the pre-`F` evidence is retained and unchanged (§A.42 item 2) | `C5` (P) at `E` against the digests below; reviewers check that each pin resolves to retained content |
| `F`'s exact-head run is retained by the first execution commit (§A.42 item 2) | `C8`: `evidence/f-run/results.json` at stage 1, naming `F`, its run, job and the served log's digest; `C5` (P, R) |
| `E`'s exact-head run reaches `main` through its own evidence-retention pull request before reconciliation, and the receipt names each retained file's digest (§A.42 item 2) | `C8`: reviewer check of that pull request and of the receipt's candidate entry for `E`; `evidence-retention` at `Q` |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

`LOG` binds to `E` only through the run that served it: that it is the bridge job of the exact-head run at `E` is the
host attestation `C3`, which the receipt records and no control reads.

## Design evidence

The design runs dispatched `verify.yml` on the research branch `dev-equivalence/omega4`, whose two commits main does
not reach; each is also held by a `preserve/` ref of the same repository. They are design evidence, not `check-run`
attestations. Their module is `EqvOmega4`, the frozen module's text under its earlier namespace.

- **Design run 1.** Workflow run 38090924005, `workflow_dispatch`, attempt 1, head `195dfbeeca73fea4a7f7b529f8b7375a38e73869`.
  Conclusion `failure`; 32 of 33 jobs `success`. Its Mathlib bridge job 114327010280 failed at the Build step on two
  terms, `EqvOmega4.lean:157:16` and `:215:16` (`Type mismatch`), and its Release gate step was skipped; seven of the
  fifteen reports carried `sorryAx` from error recovery at those terms.

- **The repair.** The commit after run 1 replaced each failing term by
  `by simp only [Set.mem_setOf_eq] at hv; rw [mem_omega4]; exact le_of_lt hv` and dropped one unused simp argument.
  No statement changed.

- **Design run 2 (checkpoint `C0`).** Workflow run 38096511360, `workflow_dispatch`, attempt 1, head `95beab2b48ab9a07dac820e1df7d0850828f5bec`.
  Conclusion `failure`; 32 of 33 jobs `success`. In its Mathlib bridge job 114343410536 the **Build step passed**
  (`Build completed successfully (3644 jobs)`), with all fifteen reports `[propext, Classical.choice, Quot.sound]`
  and warnings only in the module, and the **Release gate step failed** at `lean-manuscript` alone (one problem: the
  design module carried no census family). Every other gate step passed: `lean-axioms` 5875 named results with no
  `sorryAx`, 303 legacy records intact, 43 receipts holding. The bridge job therefore concluded `failure`; what was
  green is the build and every gate step but one.

- **Exact replays.** The frozen probe and `controls.py exact` were each run twice locally at the frozen blobs, with
  byte-identical output (`evidence/exact-replay.json`).

- **The predicted execution tree** has not had its design run. Its retained result is pinned below as pending.

**Retained evidence (§A.42).** Each file is a structured expected result in §A.42 item 1's form: build success, the
release gate's steps and verdict, the module's `#print axioms` reports with their axioms, the build errors and the
failure markers for a bridge job; every job's conclusion; the output digests and lines for the exact layer; the
identity and job outcomes for `D`'s push run. Each names
its commit, run, job and recipe and, as provenance, the digest of the text it was read from. The two design-run files
are `derived` from the served job logs (the session's job-log tool serves the last 5000 lines; every report the
files record lies in the served text) and from the runs and jobs APIs; `compare_result.py` requires a passing gate,
which neither run had, so their recipes compare by hand. The files are committed to the record directory by the first
execution commit, outside `amendments/`, and pinned here before `F`. `F` is not designated with a pending pin.

| path | sha256 |
| --- | --- |
| `evidence/design-run-1.json` | `0c8d5db0c6bf42c361714f4f2b700394a9c9222704ff4666063244cc7307cb71` |
| `evidence/design-run-2.json` | `c78096d0f8dba0281da28d1fc9363f47d2108d840a0abfbf88d87625ffb38e40` |
| `evidence/exact-replay.json` | `499cf0c0d37a3acf67471778ef4e2170cfef8f5142ab257e8723de30dc7dd77e` |
| `evidence/d-push-run.json` | `efa254e6699a0a0a3e788776b73629cceb6927346aafd333767023a8d84c7a7d` |
| `evidence/predicted-tree-run.json` | pending |

**The design commits.** The two design-run heads are named in full in their run entries above. Their trees are not
reachable from `main`; until the evidence-retention archive retains them, each run file's recipe fetches its head
from its `preserve/` ref. Retaining them in the archive is an archive change outside this round.

### The predicted execution tree

- **`d61ab64a9a375f8e7a87fc6aa1fdd9997b916379`** (local branch `ktrans-sep-1-predicted`, a single-parent child of `D`, tree `fc98813581ce2dd9788a711b5b4f6ebec056c6b2`) is the
  execution tree less the result note and `evidence/f-run/`. Its files and blobs:
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/preregistration.md`, blob `0d56bdda1bcbaefb16c85c2c64fcd229e044eb36`: this preregistration in its drafting revision, which differs from this revision only in this section;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/controls.py`, blob `05793664e1c01d9186fae62fada2f77638b5102d`: `controls.py`;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/design-run-1.json`, blob `233944b16f89ec281569d4728f85714ceb30c898`: retained evidence;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/design-run-2.json`, blob `5502655422602efc907623e06fd0e58ee796e19c`: retained evidence;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/exact-replay.json`, blob `695a897d4f344578e4b188ddf22e94bd1637fbe1`: retained evidence;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/d-push-run.json`, blob `7774c62747255c4a2e3336f09ecf9439365d6ef4`: retained evidence;
  - `verification/lean-mathlib/OIBridge/TransSeparation.lean`, blob `9093a86e0dec96dd1217613520c2ba0666292935`: the module;
  - `verification/lean/ktrans_sep1_probe.py`, blob `19e19f28fa7644de0bcc3089a354317310de3e41`: the probe;
  - `verification/lean-mathlib/OIBridge.lean`, blob `ffff5cdeb7ab2c3cfff48099165aeb2b1acbc4c9`: `OIBridge.lean`, `D`'s with the import line;
  - `verification/lean-manuscript-census.json`, blob `5a914412b80f6287181dbe33be9c89ad0de7329d`: the census, `D`'s with the family;
  - `.github/workflows/verify.yml`, blob `3b30ced43df0bb7aa0c0a994bf7184837c0445ad`: the workflow, `D`'s with the five splices.
- `delta(D, d61ab64a)` is exactly those eleven paths: six record files and the five execution paths.
- At that commit `controls.py check d61ab64a`, run from the tree's own `controls.py`, passes all 23 checks, and
  `controls.py --self-test` passes 71 checks.
- Its design run is not yet dispatched. A `workflow_dispatch` of `verify.yml` on exactly this commit is the
  design evidence this draft still needs; its expected result is `evidence/predicted-tree-run.json`, pending above.
- On a branch push this commit starts no workflow: `verify.yml` runs on `push` to `main` only, on
  `pull_request` and on `workflow_dispatch`; the three path-filtered workflows match none of its eleven paths; and
  `reproduce-evidence.yml` is dispatch-only.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and its run are design evidence, not
attestations.

## Stages and outcomes

**Stages.**
1. **C1** adds `controls.py` at its frozen blob, the five pinned evidence files and `evidence/f-run/results.json`, the
   structured expected result of `F`'s exact-head run. Acceptance: each blob is the frozen blob or matches its pin.
2. **S1** adds the module, the probe, the import line, the census family and the workflow edit in one commit.
   Acceptance: `controls.py check S1 --freeze F --stage S1` passes; the exact-head run at S1 has every job green.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F --log
   LOG` passes and the exact-head run at `E` has every job green.

**Outcomes.**
- **`KTRANS-SEP-1-READ`**: `controls.py check E --freeze F --log LOG` prints `controls: OK`; `controls.py verdict E
  --freeze F --log LOG` prints one token for each of the three cells; the exact-head run at `E` is green on every job;
  the result note states each cell's token, the earned reading in its frozen words exactly when all three cells are
  positive, and the non-inference rule.
- **`KTRANS-SEP-1-HALTED`**: anything else (`S12`); the result note names the failing check or job.

No outcome sources boundary transitivity or its dense form, adopts either as a premise, or edits the ROADMAP or a
manuscript. Correctness bands are unchanged by either outcome: the round is consistency-axis work.

## Open before `F`

- The predicted execution tree's design run, and the pin of its retained result.
- The owner's decision on retaining the two design-run heads in the evidence-retention archive before `F`.
