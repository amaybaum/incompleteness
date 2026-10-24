# Reconstruction round KTRANS-SEP-2 — Ω₄, a convex body in ℝ⁴ with the named kernel properties on which no body-preserving family is boundary transitive: PREREGISTRATION (draft for owner review)

**Status: draft control plane for owner review; not a candidate `F`.** This file is the control plane of a native
round under `AGENTS.md` §A.39, to be drafted on its guiding pull request from `D`. Only the owner designates `F`; an
instruction to proceed is not a designation. `F` has the preconditions listed under *Preconditions of `F`* at the end;
conditions 1 and 2 are met and condition 3 is open. Nothing is executed.

**Provenance: the successor of KTRANS-SEP-1.** KTRANS-SEP-1 (#824) froze its control plane at `F` =
`7e9aef691f47edaec9111ef5923ed9e946854737` (preregistration blob `7af918b1`), whose exact-head run 39940836089 was
green on every job. Its control P required `F`'s own run result to record the module's build line and fifteen reports
(its preregistration, lines 315–322); `F`'s tree is `D` plus the control plane, so that run carries no module, and the
requirement could not hold at stage 1 or at `E`. The control plane cannot change after `F`, so that round halts under
its own rules (#824 comment 6363883710). This was a control-plane defect, not a mathematical counterexample. This
round keeps that round's mathematics, frozen surface, module and probe byte for byte, and changes only what the
defect requires, the anchors that moved with `D`, and the safeguard and negative controls below. KTRANS-SEP-1's
control plane, its `F`, that run, its predicted tree `bd579bf8db6065f6667511ee0a02fa31effc1f5b` and that tree's design
run 39173554213 are provenance.

**The reused implementation bytes.** This round reuses KTRANS-SEP-1's implementation bytes as they stand in that
round's predicted tree `bd579bf8`: the module `verification/lean-mathlib/OIBridge/TransSeparation.lean` (blob
`ba7431915e7ab6e8f7bdfb6ab980f16067e9331b`) and the probe `verification/lean/ktrans_sep1_probe.py` (blob
`19e19f28fa7644de0bcc3089a354317310de3e41`), byte-identical and at the same paths. The module's header and the probe's
docstring name round KTRANS-SEP-1; those labels identify where the bytes were designed and frozen, which is their
provenance, and they are kept unchanged so that the blobs, the frozen surface and the probe's frozen output are the
ones KTRANS-SEP-1 froze. Of KTRANS-SEP-1's runs, only its predicted tree's run 39173554213 built these exact module
bytes; design runs 1 and 2 built the module's earlier text under the namespace `EqvOmega4` (*Design evidence*). This
round's own predicted-tree run (*Preconditions of `F`*, condition 1) builds the same bytes at this `D`. This round's
identity is carried by its record directory, its controls, its shard, its census family and its receipt.

```v3-round
round KTRANS-SEP-2
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-ktrans-sep-2-omega4/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-ktrans-sep-2-omega4/
record AM verification/receipts/KTRANS-SEP-2.json
execution A verification/lean-mathlib/OIBridge/TransSeparation.lean
execution A verification/lean/ktrans_sep1_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

The record directory holds this preregistration, the round's frozen controls `controls.py`, the retained evidence under
`evidence/` (the pinned files below and `evidence/f-run/results.json`), any amendments under `amendments/`, and the
result note `result.md`. The receipt path is `verification/receipts/KTRANS-SEP-2.json`. Every other path the round
changes is an execution path listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, no landed
kernel module and no other round's record change under any outcome.**

## The objects

- **`D`** = `48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29`, the head of `main` after #895.
  Its push run, run 39766586077, is recorded in `evidence/d-push-run.json`, derived from the runs and jobs APIs as
  KTRANS-SEP-1's was.
- **`F`** — the commit carrying this file that the owner designates; `delta(D, F)` is this file and any amendments.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

**Drift from the design base to `D`, measured.** The module was designed and built on `main` at
`9f9f8257a980a1819fbbc1dc0019917cf8678626` (the design base `L`), and KTRANS-SEP-1 measured it unchanged to that
round's `D` `ec36234c`. From `ec36234c` to this `D`: all 31 modules of `OIBridge.DenseOrbit`'s import closure and the
two build files `lakefile.toml` and `lean-toolchain` under `verification/lean-mathlib/` are byte-identical, so every
kernel line reference below holds at `D` and the design builds bear on the module at `D`. The K∞-Trans block of
`verification/ROADMAP.md` is still `:1031–1035`, byte-identical. Three anchors moved, because KTOKEN-MAXCONE-1 landed
after `ec36234c`: the last import line of `OIBridge.lean` is `import OIBridge.KTokenMaxCone` (`:270`), the last census
family is KTOKEN-MAXCONE-1's (modules `["KTokenMaxCone"]`), and in `verify.yml` its shard `probes_ktokenmaxcone1`
directly precedes the Act 42 comment (`:483`). The import line, the census family and the workflow splices below are
anchored there. KTOKEN-MAXCONE-1 also added a step to the Mathlib bridge job after the release gate ("KTOKEN-MAXCONE-1
check A3 …"), the job's last step at `D`; this round's four bridge steps follow it (*The workflow edit*).

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

The statement is about Ω₄. It is not a statement about other compact convex bodies with these properties, and the
round does not claim that the Euclidean 4-ball has all of them. What it uses about the 4-ball is this
(countercontrol CX1): the kernel gives `eball 4` a sharp seed (`sharpEff_sharpSeed`, EffectSpace.lean:118) and a
body-preserving boundary-transitive family (`preservesBody_fullAut`, EffectSpace.lean:230;
`boundaryTransitive_fullAut`, EffectSpace.lean:337), and CX1 checks the drive's maps, central symmetry and strict
midpoints at 1281 exact states. The kernel has no `ElementaryDrivability (eball 4)` and no `RelStrictConvex
(eball 4)` theorem, so CX1 is a finite exact check, not a theorem. Drivability fails on the interval `[−1, 1]`
(`not_drivable_Icc`, KInfFoundations.lean:529), and nothing is stated for dimension 2. The round says nothing about
chart dimension 3, and nothing about K∞-Stage, K∞-Act, K∞-V4 or K∞-Copy, whose kernel objects do not occur in it.

## The kernel declarations the round adds (frozen surface, module `OIBridge/TransSeparation.lean`)

The module is blob **`ba7431915e7ab6e8f7bdfb6ab980f16067e9331b`**, KTRANS-SEP-1's bytes from its predicted tree
`bd579bf8`; its header names that round as their provenance (*The reused implementation bytes*). It imports
`OIBridge.DenseOrbit` only; namespace `OIBridge.TransSeparation`; one `open` line,
`open Set KInfFoundations OrbitGeneration TransitiveBody DenseOrbit`.
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
`import OIBridge.KTokenMaxCone` (`:270` at `D`).

**Census family**, inserted directly before KTOKEN-MAXCONE-1's family (modules `["KTokenMaxCone"]`), which stays the
last, in `D`'s two-space
JSON layout: name "Ω₄, the ℓ⁴-sum of the Euclidean 3-ball and the segment, is compact, convex, with interior, drivable,
with a sharp seed, relatively strictly convex and centrally symmetric, is no affine image of the Euclidean ball, and
admits no body-preserving family that is boundary transitive or has a dense boundary orbit (round KTRANS-SEP-2,
reconstruction)", `modules: ["TransSeparation"]`, `status: "kernel-only"`, `manuscript: []`.

## The exact layer

**The frozen probe** `verification/lean/ktrans_sep1_probe.py`, blob **`19e19f28fa7644de0bcc3089a354317310de3e41`**
(the path and bytes KTRANS-SEP-1 froze, reused from its predicted tree `bd579bf8`; its docstring names that round as
the bytes' provenance; see *The reused implementation bytes*),
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

- **CX1 (non-ellipsoidality dropped: the 4-ball).** On the Euclidean 4-ball the seed `(1 + s)/2`, central symmetry,
  the drive's rotation and cyclic map, and strict midpoints hold at 1281 exact states; the sixteen-point system with
  the ball's own states is feasible (the witness `α = β = 1`, the rest `0`); and a state of Ω₄'s certificate is not a
  ball state. S3 freezes the kernel's support at `D`: `sharpEff_sharpSeed` (a sharp seed of `eball d`),
  `preservesBody_fullAut` and `boundaryTransitive_fullAut` (a body-preserving boundary-transitive family on
  `eball d`). The kernel has no `ElementaryDrivability (eball 4)` or `RelStrictConvex (eball 4)` theorem, so CX1 is a
  finite exact check of those two properties, not a theorem: it shows that the sixteen-point step is what separates Ω₄
  from the ball, not that the ball has every named property.
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

Every fact the verdict reads about a CI run comes from the host's structured records, never from log text. `RUN` is
the runs API answer for the exact-head run at `E` (`GET /repos/{owner}/{repo}/actions/runs/{id}`), and `JOBS` the jobs
API answer for it (`GET /repos/{owner}/{repo}/actions/runs/{id}/jobs?per_page=100`), which lists every job of the run in
one answer, each with its steps' names and conclusions. `controls.py verdict E --freeze F --run-api RUN --jobs-api
JOBS` derives the run result from them with the frozen recipe `derive-run` (*Retained evidence*), which refuses the
answers unless every job carries the run's id, attempt and commit, first runs every control of `check E --freeze F`,
and prints the cells only from complete evidence; otherwise it prints
`VERDICT  VOID` with the reason, prints no token, and exits 1. **VOID is not an outcome.** A tooling failure or
incomplete evidence never yields a `NOT-ESTABLISHED` token: the evidence is taken again (the answers fetched again,
the run repeated) or the round halts under `S12`.

**The run.** The run result must be the exact-head run at `E`:
- the completed `workflow_dispatch` run of `.github/workflows/verify.yml`, in the repository `amaybaum/incompleteness`,
  from a branch of that repository (its head repository);
- at `E`'s full commit;
- with positive integer run id, attempt and bridge job id, and a completed Mathlib bridge job.

A pull-request run is not one: it runs on a synthetic merge, whose workflow and tree no control checked. Nor is a push
run, or a run of another repository or workflow path. A missing or malformed identity field makes the result not that
run.

**The bridge steps L0, L, A and M.** The kernel cells read the module's reports through four steps the round adds at
the end of the Mathlib bridge job (the sixth splice of *The workflow edit*), and only through their conclusions:

- **L0**, `KTRANS-SEP-2 build the imports of the module`, runs `lake --rehash build OIBridge.DenseOrbit`, the module's
  one import, under a 30-minute limit, and succeeds exactly when that build does. It brings the module's import
  closure up to date with its sources: `--rehash` recomputes the sources' hashes rather than trusting stored ones, and
  Lake rebuilds every artifact whose trace differs from them and reuses the rest. That L0 rebuilds a stale closure
  restored from the build cache rests on Lake's trace semantics, on which the `Build` step relies too; no run of this
  round observes it.
- **L**, `KTRANS-SEP-2 elaborate the module`, runs `lake env lean OIBridge/TransSeparation.lean` into a file and
  succeeds exactly when `lean` exits 0.
- **A**, `KTRANS-SEP-2 axiom reports within the three axioms`, prints that file and runs `controls.py axioms` on it.
  The gate reads the module's fifteen reports, which `lean` prints without file positions and wraps across lines when
  long, and classes them:
  - `standard` when each of the fifteen prints is reported exactly once, in print order, within
    `[propext, Classical.choice, Quot.sound]`, with no other report of the namespace, no report that does not parse,
    no error line and none of `sorryAx`, `Lean.ofReduceBool` and `Lean.trustCompiler`;
  - `complete-nonstandard` when the fifteen are each reported exactly once, in print order, every report parses,
    there is no other report, and some report names an axiom outside the three;
  - `incomplete` otherwise.

  It records the class as the step output `reports` and succeeds exactly when the class is `standard`.
- **M**, `KTRANS-SEP-2 marker complete reports with an axiom outside the three`, runs only when A recorded
  `complete-nonstandard`, and is otherwise skipped.

L0, L and A run whenever the job was not cancelled, so they run after a failed build too. Their conclusions are in
the jobs answer whole, whatever the build cache made the earlier steps print. When L0 succeeded, L elaborates the
module's exact bytes at `E` against its import closure as L0 left it, which Lake's trace semantics make current with
`E`'s sources. Every reading, positive or negative, requires L0 `success`, so no reading rests on a dependency build
that failed, was cancelled, skipped or timed out, or did not run. Were Lake to reuse a stale artifact, a reading could
rest on it, and a tooling negative is not excluded in that case; the predicted tree's run, whose L0 follows a `Build`
step that has just brought the closure up to date, does not exercise it.

**VOID** when any of these holds:
- a required control failed or never ran;
- `RUN` and `JOBS` do not describe one complete run with one Mathlib bridge job and its steps, or a job does not
  carry the run's id, attempt and commit, so `derive-run` refuses them;
- the run is not the exact-head run at `E` as *The run* defines it: another commit, repository, head repository,
  workflow path or event; a run or bridge job not completed; an identity field missing or malformed;
- its bridge job does not carry `Build`, `Release gate`, L0, L, A and M each exactly once, with L0, L, A and M
  consecutive, in that order, after the release gate;
- the step conclusions are neither positive nor negative as the table defines. Among them:
  - L0 anything but `success`, beside any other conclusions;
  - L failed beside a passing A;
  - A failed with M skipped, which is an incomplete output or a tooling failure;
  - A and M both succeeded;
  - A skipped or cancelled;
  - M failed;
  - `Build` or `Release gate` failed beside positive steps;
- sympy `1.14.0` is not importable;
- the probe does not run to completion (non-zero exit, no `checks:` line, or no final `VERDICT` line);
- or its output differs from the frozen output with no failing check.

| Cell | Outcome | Rule |
|---|---|---|
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-PROVED` | S1 holds for `not_affine_eball_omega4`, and in the run result at `E` the bridge steps `Build`, `Release gate`, L0, L and A concluded `success` and M `skipped`: `lean` elaborated the module, and its fifteen reports, among them `not_affine_eball_omega4`'s, are each within `[propext, Classical.choice, Quot.sound]`, with no error line and no `sorryAx`, `Lean.ofReduceBool` or `Lean.trustCompiler` |
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-NOT-ESTABLISHED` | complete evidence of a failure in the module: L0 concluded `success`, A `failure` and M `success`, with L `success` or `failure`: the fifteen reports complete and parsed, one outside the three axioms |
| Q-CEX | `KTRANS-SEP-COUNTEREXAMPLE-PROVED` | S1 holds for `omega4`, `not_affine_eball_omega4`, `not_boundaryTransitive_omega4`, `not_denseBoundaryOrbit_omega4` and `kinfTrans_separation`, and the step conclusions are as for Q-NONELL |
| Q-CEX | `KTRANS-SEP-COUNTEREXAMPLE-NOT-ESTABLISHED` | as for Q-NONELL |
| Q-EXACT | `KTRANS-SEP-INSTANCES-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I -B` under sympy `1.14.0`, prints exactly the frozen output (sha256 `d6f6d298d3ed57081f4e81bef267771fc81d8083a111c0414a69216c772a2940`), which contains the twelve `PASS` lines, `COUNTER XW1 fails as stated`, `COUNTER XW2 fails as stated`, `checks: 12, failures: 0` and `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS`; and X1–X3 and CX1–CX4 hold |
| Q-EXACT | `KTRANS-SEP-INSTANCES-NOT-ESTABLISHED` | a complete probe run in which a check failed (`FAIL`, `DID NOT FAIL` or `NOT RENDERED`) |

No rule reads another cell's outcome. Q-EXACT reads the probe's output as `controls.py` captures it when it runs the
probe itself, complete, by digest and line; it reads no CI log. `#print axioms` reports every axiom of a declaration's dependency closure, so a
`sorry` anywhere beneath a printed theorem shows in its report; N3 also rejects one in the module's text. The outcome
is `KTRANS-SEP-2-READ` when the three cells are assigned and the exact-head run at `E` is green on every job
(*Stages and outcomes*); the tokens are those `controls.py verdict E` prints.

**No vacuous verdict, and no tooling negative.** Every VOID condition above, and each negative route, is driven by a
self-test case. These give VOID:
- run results at another commit or at none;
- run results of a `push`, `pull_request` or `schedule` event, of another repository, from a fork's head repository,
  of another workflow path (a path ending in `verify.yml` among them), not completed, with a bridge job not
  completed, with a zero or non-integer run id or attempt, without a bridge job id, or with an identity field of the
  run missing (a zero or non-integer bridge job id is VOID under the same rule; no self-test case drives it);
- run results without a bridge job, with each of L0, L, A and M missing, with a step twice, or with the steps reordered,
  placed before the release gate or split by another step;
- `Build` missing, `Release gate` twice, a step without a conclusion, and text that is not JSON;
- each step-conclusion combination listed above, and L0 failed, cancelled, skipped, timed out or unknown beside steps
  that otherwise read negative or positive;
- jobs answers that `derive-run` refuses: incomplete; without a bridge job; with a job twice (the bridge job or
  another); with a job of another run, of another attempt or at another commit, or without its run id, attempt or
  commit; with no bridge steps; with a step number twice; and a runs answer without its repository;
- a probe that crashes, a probe whose import fails, sympy absent or of another version, a probe output cut before its
  verdict or reduced to its summary, and a changed non-check line.

These give the negative tokens, which `verdict` prints and a halted round's result note records (*The negative
readings and the outcome*):
- L0 succeeded, A failed and M succeeded, whether L succeeded or failed;
- a complete probe run with a failing check.

Each of the gate's classes is driven by cases:
- `complete-nonstandard`: `sorryAx`, another axiom, or a trust token in one report's list, with or without a module
  error line;
- `incomplete`: an empty or cut output; a missing, duplicated, extra or reordered report; a report cut inside its
  wrapped axiom list; clean reports beside an error line or a stray forbidden token; and a non-standard report beside
  a missing or duplicated one.

The `axioms` command writes the class it computed, under the output name M's condition reads.

**The negative readings and the outcome.** A negative reading is complete evidence of a failure, never the round's
`READ` outcome. A kernel NOT-ESTABLISHED needs A failed, which fails the bridge job. Q-EXACT's NOT-ESTABLISHED needs a
probe check that failed, which fails the shard's `VERDICT` step. `READ` requires the exact-head run at `E` green on
every job. Either reading therefore halts the round (`S12`), and its result note states the tokens `verdict` printed.
A literal `sorry` in the module fails N3, which voids the verdict before any cell is read. The kernel's negative route
reads the kernel's own report of a failure, such as the `sorryAx` that Lean's error recovery records at a term that
does not elaborate.

## The earned reading and the non-inference rule (frozen)

> Earned reading: Omega4 = {(x, s) in R^3 x R : |x|^4 + s^4 <= 1} is compact, convex and has nonempty interior,
> satisfies ElementaryDrivability, carries the sharp seed seed4, and is RelStrictConvex and CentrallySymmetric about 0;
> no body-preserving family of affine equivalences of R^4 is BoundaryTransitive or has a DenseBoundaryOrbit on Omega4
> (kinfTrans_separation). Omega4 is therefore a counterexample to the implication from these properties, for
> body-preserving families, to BoundaryTransitive and to DenseBoundaryOrbit.

> Non-inference rule: the round concerns Omega4 alone, in R^4. It states nothing about other compact convex bodies,
> about chart dimension 3, about K-infinity-Stage, K-infinity-Act, K-infinity-V4 or K-infinity-Copy, about the
> composite, or about which bodies OI supplies. The Euclidean 4-ball is countercontrol CX1: the kernel gives it a
> sharp seed (sharpEff_sharpSeed) and a body-preserving boundary-transitive family (preservesBody_fullAut,
> boundaryTransitive_fullAut), and CX1 checks its drive maps, central symmetry and strict midpoints at finitely many
> exact states; the kernel has no ElementaryDrivability (eball 4) or RelStrictConvex (eball 4) theorem, so CX1 is a
> finite exact check, not a theorem. Drivability fails on the interval [-1, 1] (not_drivable_Icc), and nothing is
> stated for dimension 2. RelStrictConvex is the form in which the kernel gives singleton faces for every effect
> family; it is not a frozen statement of K-infinity-Geom. Supporting-effect completeness of the full effects on
> Omega4 is an exact identity with a written step, not a kernel theorem of this round. The exact layer is an exact
> computation, not a Lean kernel proof.

The result note states the earned reading in these words exactly when all three cells are positive, and the
non-inference rule in these words under every outcome (control V, whitespace-normalized).

**Premise this round does not source:** boundary transitivity and its dense form; and none of drivability, the seed,
strict convexity or symmetry for any OI object.

## The ROADMAP wording the round would license (row K∞-Trans; not applied by the round)

At `D`, ROADMAP `:1031–1035` ends: "K∞-Drive does not give it: a drive's flow preserves the ball and a sharp seed and is
not boundary transitive (`not_boundaryTransitive_flow`), and no theorem derives transitivity from
`ElementaryDrivability` on a general body." Under `KTRANS-SEP-2-READ` with all three cells positive, a later edit may
add: "On Ω₄, a compact convex body in ℝ⁴ that satisfies `ElementaryDrivability`, carries a sharp seed and
is relatively strictly convex and centrally symmetric, no body-preserving family is boundary transitive or has a dense
boundary orbit (`kinfTrans_separation`)." K∞-Trans stays open under every outcome.

## The workflow edit (frozen)

`.github/workflows/verify.yml` at `E` is `D`'s with six splices, each anchored once at `D`:

- the four bridge steps L0, L, A and M (*The decision rules*), inserted directly after KTOKEN-MAXCONE-1's check A3 step,
  the Mathlib bridge job's last step at `D`, so that they are the job's last steps.
  - L0, L and A run with `if: ${{ !cancelled() }}` in `verification/lean-mathlib`.
  - L0 runs `lake --rehash build OIBridge.DenseOrbit` with `timeout-minutes: 30`, and nothing else.
  - L runs `lake env lean OIBridge/TransSeparation.lean > "$RUNNER_TEMP/ktrans-sep2-axioms.log" 2>&1` and nothing
    else.
  - A, under the id `ktrans_sep2_axioms`, runs `set -euo pipefail`, prints the file, and runs `controls.py axioms` on
    it as its last command.
  - M runs with `if: ${{ !cancelled() && steps.ktrans_sep2_axioms.outputs.reports == 'complete-nonstandard' }}` and
    prints one line.
  - No step continues on error or overrides the shell;

- the shard `probes_ktranssep2`, `Numerical probes / KTRANS-SEP-2 Omega4 counterexample`, inserted directly before the
  Act 42 comment (`:483`), after KTOKEN-MAXCONE-1's shard. It checks out with `fetch-depth: 0` (the controls read `D` through git),
  sets up Python 3.11, installs `sympy==1.14.0`, and runs three steps: the probe from `verification/lean` with
  `python3 -I -B`, its output kept and the step failing unless the line
  `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS` is present (the probe itself exits 0); `controls.py exact`; and
  `controls.py --self-test`;
- in the aggregate `Numerical probes` job: `probes_ktranssep2` after `probes_a42_witness` in `needs` (`:578`);
  `KTRANSSEP2_RESULT: ${{ needs.probes_ktranssep2.result }}` after `KTOKENMAXCONE1_RESULT` (`:599`);
  `echo "ktranssep2=${KTRANSSEP2_RESULT}"` after the KTOKEN-MAXCONE-1 echo (`:621`);
  `test "${KTRANSSEP2_RESULT}" = success` after the KTOKEN-MAXCONE-1 test (`:642`).

The exact text is embedded in `controls.py` (control W).

**Placement beside KTOKEN-MAXCONE-1.** KTOKEN-MAXCONE-1's self-test runs in its shard on every build and reads the
live workflow, root and census: it requires each of its own workflow splices verbatim (among them
`probes_bg2, probes_ktokenmaxcone1, probes_a42_witness` in `needs`), its import line directly after
`import OIBridge.TurnpikePremiseOrientation`, and its census family last. The edits above are placed so that each of
these holds: the census family stands before its family, the shard joins `needs` after `probes_a42_witness`, and every
other insertion follows its lines. With the edits applied to `D`'s files, KTOKEN-MAXCONE-1's self-test and every other
round self-test present at `D` print OK; with the placement of this round's first draft (the family after its family,
the shard after `probes_ktokenmaxcone1`), its self-test fails, and the predicted tree's run could not be green.

**Reconciliation.** `main` has moved since `D`: PRESERVE-INDUCT-1 (#880) added, at the same anchors, its own bridge
step after KTOKEN-MAXCONE-1's check A3, two import lines after `import OIBridge.KTokenMaxCone`, two census families
before KTOKEN-MAXCONE-1's, and its shard and aggregate lines. The round keeps `D`; its execution and its `E` run on
`D`'s workflow, so its verdict reads a bridge job whose last steps are this round's. The conflicts this leaves for the
reconciliation are resolved there by merits (§A.39): every round's lines are kept, this round's four bridge steps
stay the job's last steps, and the placement keeps KTOKEN-MAXCONE-1's live requirements; before the reconciliation is
pushed, every round self-test that reads the live files is run on the reconciled tree.

## The controls (in `controls.py`)

`controls.py` imports nothing from the repository and changes nothing; it reads `D` and the commits it is given with
read-only git commands and embeds every frozen text. It also carries the round's recipe for its run results,
`controls.py derive-run` (*Retained evidence*), and the safeguard `controls.py mock-s1` (*Preconditions of `F`*,
condition 3).

`check`, `--self-test`, `verdict` and `mock-s1` read the commits' trees through git with paths relative to the
repository root, and are run from the repository root, as the workflow runs the self-test. Run from another
directory of the checkout they fail closed: `check` fails R, the self-test fails, `mock-s1` fails R and B, and
`verdict`, which runs `check`'s controls first, prints `VERDICT  VOID` and no token. Outside the checkout `check` and
the self-test fail further checks. `exact` reads the module through git and runs from any directory inside the
checkout; outside one it fails X3. `derive-run` and `axioms` read only their own inputs and run from any directory;
the workflow runs `axioms` in the bridge job's directory.

Its codes:

- **G** governed paths: `delta(D, commit)` is exactly the five execution paths with their statuses, plus record files.
- **R** record: only the permitted files; `evidence/f-run/results.json` required with `--freeze`; the result note
  required at `E` and absent at `S1`.
- **P** pins: every file pinned in *Retained evidence* is present with its sha256; the table names the four required
  files; with `--freeze` no pin is pending. Each pinned file is a structured result (`schema`, `version`, a stated
  `form` of `complete` or `derived`, a source digest when derived) with no timestamp or duration field. With
  `--freeze`, *The predicted execution tree* names its commit in the frozen form: the section's first line, directly
  after its heading, is `- **`<40-hex commit>`**`. Each run result is checked for what its stage validates (*Stage
  requirements*):
  - the predicted tree's run result (`evidence/predicted-tree-run.json`) names the commit in *The predicted execution
    tree* as its `head_sha`. It is that commit's run as *The decision rules* define the run, and green: the
    completed `workflow_dispatch` run of `.github/workflows/verify.yml` in `amaybaum/incompleteness`, positive integer
    run id, attempt and bridge job id, conclusion `success`, every job and the bridge job `success`. Its bridge steps
    read positive under *The decision rules*: `Build`, `Release gate`, L0, L and A `success` and M `skipped`, each
    once, L0, L, A and M consecutive after the release gate (`run_ok`);
  - at `F` (with `--freeze`) three checks, kept separate:
    - **absence, from `F`'s tree** (`ftree_ok`): read through git at `F`:
      - the trees `verification/lean-mathlib` and `verification/lean` are exactly `D`'s;
      - neither the module's path `verification/lean-mathlib/OIBridge/TransSeparation.lean` nor the probe's path
        exists;
      - `F`'s `OIBridge.lean`, which must be readable, has no import line naming `OIBridge.TransSeparation`, alone or
        beside other modules.

      Together with T (`delta(D, F)` is the control plane alone) and `D`'s own content, which carries no such module,
      this is why `F` carries no module. A run record is not.
    - **identity, success and workflow, from `F`'s run result** (`frun_ok`, on `evidence/f-run/results.json`, against
      the predicted tree's run result). The run is the completed, green `workflow_dispatch` run of
      `.github/workflows/verify.yml` in `amaybaum/incompleteness` at `F`, as above.
      Its jobs are exactly the predicted tree's run's jobs less the round's shard (`Numerical probes / KTRANS-SEP-2
      Omega4 counterexample`), each once. Its bridge steps are exactly the predicted tree's run's bridge steps less L0,
      L, A and M, in order, `Build` and `Release gate` among them once each, every one `success`. Both runs are
      `workflow_dispatch` runs of `D`'s workflow, the predicted tree's with the round's edits. So their job sets differ
      by the shard alone and their bridge steps by L0, L, A and M alone. `D`'s push run is no reference, since on a push
      the A42 exclusion matrix is skipped.
    - **consistency** (`frun_consistent`): the same result has none of the round's bridge steps (no step named
      `KTRANS-SEP-2 …`) and not its shard, as a run of `D`'s workflow on a tree without the module must. A failure
      here is a failed control; a pass is not evidence of absence.
- **T** chain (with `--freeze`): `D..commit` is one chain of single-parent commits through `F`; `delta(D, F)` is the
  control plane; the preregistration at the commit is `F`'s. The check is on commit identity: a re-cut `F` with the
  same bytes is not on the chain and fails.
- **B** blobs: the probe is the frozen blob; `controls.py` at the commit is the file running, and its blob is the one
  this file pins (*The frozen `controls.py`*); with `--freeze` the pin may not be pending.
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
- **S3** the kernel's support for CX1 at `D`: `sharpEff_sharpSeed` (EffectSpace.lean:118), `fullAut`,
  `preservesBody_fullAut` (EffectSpace.lean:230) and `boundaryTransitive_fullAut` (EffectSpace.lean:337) have their
  frozen texts.
- **S4** phrases, in the module header and, at a commit carrying it, in the result note outside its two frozen texts
  (case-insensitive, backticks removed, whitespace-normalized): "other single-system seams", "single-system",
  "chart dimension 4", "single-system seams",
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
  three cells are positive, the non-inference rule always; `--run-api` and `--jobs-api` are required there, and a
  VOID reading fails V.

**Self-test** (`controls.py --self-test`, run in the shard). It reads the frozen module and probe by blob id and
drives a mutation through every control, each failing with its code, and alone where marked:
- **N1–N3:** an extra declaration (N1); a changed `conv_core` hypothesis (N2 alone), a changed `seed4` constant, `J`
  replaced by a rotation (N2); a `sorry` (N3 alone), `native_decide` (N3).
- **S1:** the exponent of the last coordinate in `omega4` 4 → 2, so that the body becomes the ball;
  `RelStrictConvex` dropped from `kinfTrans_separation`; nonempty interior dropped; `PreservesBody` dropped from
  `not_boundaryTransitive_omega4`; `eball 4` → `eball 3`.
- **S2–S5:** a local `eball`, `DenseOrbit` dropped from the `open` line, a second import, a landed statement
  differing at `D` (S2, the last alone); a landed ball control differing (S3 alone); three header phrases (S4); a
  sixteenth and a duplicated print (S5).
- **The exact layer:** an outer point moved inside (X1); a changed or zero weight (X2 alone); a module point changed
  (X3 alone); the ball's witness zeroed (CX1 alone); the translations replaced by the identity (CX2 alone); a
  half-space translation with a nonzero last coordinate (CX3 alone); the segment family reduced to `{id}` (CX4
  alone).
- **The cells and the probe:** the run-result and probe cases of *No vacuous verdict, and no tooling negative*, among
  them a real crashing probe and a real failing import.
- **The evidence files and run results:**
  - files with no form, an unknown form, a derived result without a digest, a timestamp field or a duration field;
  - for the predicted tree's run result: another head, another workflow path, another repository, a push event, a
    run not completed, a failed run conclusion, no run id, attempt 0, a failed job, no jobs, a failed bridge job, no
    bridge job id, negative or VOID steps, a timestamp field, and text that is not JSON.
- **The rest:**
  - the verdict gate with each required control failed or missing;
  - the note with an extra token, an altered earned reading, no non-inference rule, the earned reading under a
    negative cell, or a frozen phrase (a neutral addition passes);
  - the pure cores of I, C, W, G, R, P and T, including a merge, a re-cut `F` and an `F` not on `D`.

Positive controls: the frozen module, the landed ball control, the exact layer, the frozen probe run, a proof-only
repair, and run results whose steps read positive, as a dict, as JSON text and as bytes.

It adds, against the defect and for the structured evidence:
- **regression (real evidence):** `frun_ok` and `frun_consistent` accept KTRANS-SEP-1's real `F` run (run
  39940836089, head `7e9aef69`) against its predicted tree's run (run 39173554213, head `bd579bf8`). Both are derived
  by `derive-run` from the runs and jobs API answers and embedded verbatim with their sha256. The predicted tree's run
  rule `run_ok`, which requires the round's steps, rejects that `F` run.
- **the run half:** `frun_ok` rejects each of these:
  - another head, another workflow path, another repository, a run not completed, no run id, a push event, no attempt
    or attempt 0;
  - a failed run conclusion, a failed bridge job, no bridge job id, any failed job, or no jobs;
  - a job list cut to one entry, a job dropped, a job added, or a job listed twice (in place of another or beside all
    the others);
  - a bridge step dropped, added or renamed;
  - a failed `Release gate` or `Build` step;
  - a reference without the shard.

  `frun_consistent` flags the round's steps or its shard in `F`'s run. With a predicted run that carries the round's
  steps, `frun_ok` still accepts `F`'s run without them.
- **the tree half, negative control:** scratch commits on `D` (temporary objects, no ref) each fail the F-stage check:
  one adding the module at its path or at another; one adding only the import line, alone or beside another module
  on one line; and one adding only the probe. They fail even though the run result offered with them names them, is
  green and has none of the round's steps. A commit adding only a control-plane file passes, and an unreadable commit
  fails. Those commits fail through the Lean-directory clause, which decides on a real tree. Each other clause is
  tested alone with the directories held equal: the probe's path, the module's path, an import line, an unreadable
  `OIBridge.lean`, and an unreadable directory.
- **end to end, on scratch commits:**
  - `derive-run` records, from the runs and jobs answers alone, the run's identity (repository, head repository,
    workflow path, run id, attempt, event, status), every job's conclusion and the bridge job's status and steps in
    step order. It drops every host timestamp, url and head-commit field, reads an answer wrapped under `"jobs"` the
    same but for its digest, and gives the same bytes for the same inputs. It records another workflow path, another
    repository, a fork head, a push or pull-request event and a run not completed as given, and the cells and run
    rules read each as VOID or failed; attempt 2 is recorded as 2.
  - It refuses: an incomplete jobs answer; no bridge job; a job listed twice (the bridge job or another); a job of
    another run, of another attempt or at another commit; a job without its run id, attempt or commit; a runs answer
    without its repository; a bridge job without steps; and a step number listed twice.
  - Its results feed the rules: positive steps pass `run_ok` and negative steps read negative.
  - A predicted tree and a candidate `F` built as the round builds them pass `check` and `mock-s1`, which runs every
    required control and the three F-stage checks.
  - `mock-s1` fails, at the named check, for each of these:
    - an `F` run naming another head;
    - an `F` run whose bridge job carries the round's steps;
    - an `F` run missing a job of the predicted run;
    - an `F` run whose conclusion, bridge job, other job or `Release gate` step failed, each carried through
      `derive-run`;
    - an f-run file that is not `derive-run`'s output over the answers given;
    - a predicted tree other than the one `F` names;
    - a predicted-tree section in this round's first draft's form;
    - a candidate `F` carrying the module (T and P);
    - a candidate `F` pinning another `controls.py` blob or leaving the pin pending (B);
    - a stage-1 `controls.py` other than the file running, though the pin names the running file (B);
    - a pinned file that differs from its pin;
    - a predicted-tree run result naming another commit, or whose steps read negative.
  - **The chain itself, through `verdict` and `check`.** On scratch commits `F` → C1 → S1 → `E`:
    - a positive run at `E` with the positive note prints the three positive tokens and no failure;
    - with `W` changed, `verdict` prints `VERDICT  VOID` and no token;
    - a negative run with the negative note prints the negative kernel tokens;
    - a pull-request run at `E`, and a run without the round's steps, print `VERDICT  VOID` and no token;
    - `check` at `E` passes the positive run and note, and fails V with no run evidence, with VOID run evidence and
      with a negative run under the positive note;
    - `check` at S1 does not read the note.
- **the in-job gate and the steps' shape:**
  - `controls.py axioms`, run as a command, exits 0, ends with the OK line and writes `reports=standard` on the
    fifteen standard reports. It exits 1 and writes `reports=complete-nonstandard` on complete reports with `sorryAx`,
    and exits 1 and writes `reports=incomplete` on a cut output. Without `GITHUB_OUTPUT` it writes nothing.
  - Each of its clauses is killed by a case, and none of its labels names a forbidden token or a report.
  - W's cases pin the steps:
    - their names, in the order the verdict reads them, as the job's last steps directly after check A3;
    - L0's, L's and A's `if: ${{ !cancelled() }}` and working directory, and A's id;
    - L0's single command (`lake --rehash build OIBridge.DenseOrbit`, the module's one import, which S2 checks) and its
      30-minute limit;
    - M's condition on the class `complete-nonstandard`;
    - L's single command with nothing masking its status;
    - A's commands (`set -euo pipefail`, then the file printed, then the gate last);
    - no `continue-on-error`, no `shell:` override and no `||`.
- **negative control, missing module evidence where it is required:** KTRANS-SEP-1's real `F` run, offered as a
  module-bearing run result (the predicted tree's or `E`'s), is rejected by `run_ok`, and its cells are VOID.
- **negative control at `E`:** a green run result without the round's steps is VOID, never a token. That is the shape
  of a run whose workflow lacks the steps or whose tree lacks the module, as `F`'s did.

The regression and end-to-end cases test the corrected rule and its wiring; they are not the safeguard. The safeguard
is condition 3 of *Preconditions of `F`*, run on this round's own candidate `F`. The self-test passes 120 checks.

`controls.py` is KTRANS-SEP-1's `controls.py` (blob `412802eb`) with this round's changes, drafted on the branch
`draft/ktrans-sep-2-staging-controls`, which this round's pull request links; its blob is pinned below once it is
final (*The frozen `controls.py`*).

## Stage requirements (what each run validates)

| stage | its tree | its run validates | evidence | control that reads it | negative control |
| --- | --- | --- | --- | --- | --- |
| `F` | `D` plus the control plane; no module | that `D`'s workflow passes on `D` plus this file: the run's identity (`F`, `amaybaum/incompleteness`, `.github/workflows/verify.yml`, `workflow_dispatch`, completed, run and bridge job ids, attempt, every job carrying the run's id, attempt and commit), every job `success` and exactly the predicted tree's run's jobs less the round's shard, and exactly its bridge steps less L0, L, A and M, each `success`, `Build` and `Release gate` among them. It runs none of the round's controls, which first run at stage 1 and in `mock-s1`. The module's absence is **not** a run result: it is read from `F`'s tree | absence: `F`'s tree through git (the Lean directories, the module and probe paths, the import line); identity, success, workflow: `evidence/f-run/results.json`, derived by `controls.py derive-run` and added at stage 1 | P: `ftree_ok` (absence), `frun_ok` (run), `frun_consistent` (consistency only), at S1 and `E` | a tree containing the module, the import line or the probe fails although its run has none of the round's steps; a run with a failed job or step, a missing job or step fails |
| predicted tree | `D` plus the predicted execution files | the proposed implementation: L0, L and A `success`, M `skipped`, `Build` and `Release gate` `success`, every job green, the run's identity as at `E` | `evidence/predicted-tree-run.json`, pinned before `F` | P (`run_ok`) | KTRANS-SEP-1's real `F` run (no module, none of the round's steps), offered here, fails |
| `E` | the actual execution | the actual execution: the same step conclusions at `E` | `E`'s runs and jobs answers (`RUN`, `JOBS`) | `verdict`: VOID unless the run is the exact-head run at `E` (*The decision rules*, *The run*) and its bridge job carries L0, L, A and M in place with positive or negative conclusions | a green run result without the round's steps is VOID |

`mock-s1` (condition 3 of *Preconditions of `F`*) runs the stage-1 acceptance on candidate `F`'s own tree and its own
actual run result before `F` is designated, so that a requirement `F` cannot meet fails before the freeze.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F`; `T` in `controls.py check E --freeze F` |
| the controls, module and probe are the frozen ones | `C5`: B, `controls.py` at the commit equal to the running file and to the blob this file pins (*The frozen `controls.py`*), the probe at its frozen blob, at S1 and `E`; N1–N3 for the module; `C2`: `git rev-parse <commit>:<path>` equal to the frozen blobs, for `controls.py` at stage 1 and all three at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms; no `sorryAx` | `C3`: the exact-head run at `E`, every job `success`; L0, L, A and M read by `controls.py verdict E --freeze F --run-api RUN --jobs-api JOBS` |
| the decisive step is the module's own construction | `C5`: X3 in `check E --freeze F` |
| the exact layer replays; its countercontrols fail as stated | `C3`: shard `probes_ktranssep2` green; `verdict` re-runs the probe blob at `E` against the frozen output digest |
| no positive token over a failed or missing control | `C5`: the verdict gate; its self-test cases, and the chain case in which `verdict` with `W` changed prints VOID and no token, run in the shard at `E` |
| a tooling failure or incomplete evidence never yields a token, positive or negative | `C5`: the VOID rules of `verdict`; their self-test cases (run results, step conclusions, jobs answers, probe, sympy) run in the shard at `E` |
| the verdict reads only structured records, complete whatever the build cache did | `C5`: `derive-run` reads only `RUN` and `JOBS`; `verdict` reads only the step conclusions it records; W pins L0, L, A and M as the bridge job's last steps, L0, L and A running whenever the job is not cancelled; `C8`: the predicted tree's run result records them, checked by P (`run_ok`) |
| the in-job gate turns the reports into A's and M's conclusions faithfully | `C5`: `controls.py axioms`, whose self-test cases (every clause, every class, the command's exit status and its `reports=` output, with and without `GITHUB_OUTPUT`) run in the shard at `E`; W's cases pin M's condition on the class A writes and A's id. Observed in a run: `C8`, the predicted tree's run, shows only the positive path (L0, L and A `success`, M `skipped`) on the module's real output. Not observed in any run: that M runs after A fails, and that the output A writes before failing reaches M's condition. Those rest on GitHub's documented `!cancelled()` and step-output semantics and the runner's source; the steps running after a failed step and a skipped step's `skipped` conclusion were also observed in this repository's run 39638156685. If either unobserved behaviour did not hold, a genuine negative would read VOID, never a token, and the round would halt either way |
| no reading rests on a dependency build that did not succeed | `C5`: `kernel_state` requires L0 `success` for both readings; its self-test cases (L0 failed, cancelled, skipped, timed out, unknown or absent beside negative-looking and positive-looking steps, each VOID); W pins L0's command and limit; `C8`: L0 `success` in the predicted tree's run. That the closure L0 builds is current with the sources, a stale restored closure included, rests on Lake's trace semantics and is not measured: `C8` shows L0 `success` only after `Build` has brought the closure up to date |
| the evidence is the exact-head run at `E` and no other | `C5`: `identity_problem` (repository, head repository, workflow path, `workflow_dispatch`, completed run and bridge job, integer ids and attempt) and `derive-run`'s refusal of jobs of another run, attempt or commit; their self-test cases: through `derive-run` from synthetic answers, another workflow path (one ending in `verify.yml` among them), another repository or head repository, a `push` or `pull_request` event, a run or bridge job not completed, and `derive-run`'s refusals; on derived results, also a `schedule` event, a zero or non-integer run id or attempt, a missing bridge job id, and each identity field of the run missing; the chain case in which a pull-request run at `E` prints VOID |
| the predicted tree's run, S1's and `E`'s can be green beside KTOKEN-MAXCONE-1's live self-test | `C5`: the self-test checks each of KTOKEN-MAXCONE-1's live requirements on `D`'s files with the frozen edits (`ktoken_live_ok`), and that the first draft's placement breaks them; `C8`: the predicted tree's run green on every job |
| the steps fail closed | `C5`: W's cases (L's single command, nothing masking its status; A under `set -euo pipefail` with the gate its last command; no `continue-on-error`, no `shell:` override, no `||`); the gate exits 1 on every class but `standard`; `C3`: A green in `E`'s run |
| the reconciliation keeps every round's live requirements | the reconciliation (§A.39 item 3): before it is pushed, every round self-test that reads the live workflow, root or census is run on the reconciled tree and prints OK; after it is pushed, the run of `verify.yml` on the reconciled head, which runs each of those self-tests in its shard, is green on every job |
| a negative reading halts the round, never reads as `READ` | *Stages and outcomes*: `READ` requires every job green, and a negative reading fails a job; `C3` |
| `F` carries no module | `C5`: T (`delta(D, F)` is the control plane) and P (`ftree_ok`) at S1 and `E`, reading `F`'s tree through git: its Lean directories equal `D`'s, no module path, no probe path, no import line naming `OIBridge.TransSeparation` in `F`'s `OIBridge.lean`; `C9` on candidate `F` |
| `F`'s run shows `D`'s workflow passing on `D` plus this file: it is `F`'s `workflow_dispatch` run of `verify.yml`, its jobs are the predicted tree's run's less the shard, its bridge steps the predicted tree's run's less L0, L, A and M, every job and step `success` | `C5`: P (`frun_ok`) on `evidence/f-run/results.json` against `evidence/predicted-tree-run.json` at S1 and `E`; `C8` |
| `evidence/f-run/results.json` is derived from `F`'s actual run, by the frozen recipe | `C9`: `mock-s1` requires the file to be `controls.py derive-run`'s output over the runs and jobs answers of candidate `F`'s exact-head run, and prints its digest; the digests of those answers are in the file; reviewers check that stage 1's file has the digest recorded with the designation request |
| `evidence/predicted-tree-run.json` is derived from the predicted tree's actual run, by the frozen recipe | reviewers, before `F` (*Preconditions of `F`*, condition 1): the captured answers, kept byte for byte and supplied to them (not committed); the command, the answers' digests and the file's sha256 recorded on the pull request with the pin; and `derive-run` over the captured answers reproducing the pinned bytes, which answers fetched again need not do; no control reads the derivation, and P checks the file's digest and `run_ok` |
| the predicted tree is the one this file names, in the form P reads | `C5`: P with `--freeze` (the section's first line names a commit); P (`run_ok`) against that commit; `C9`: `mock-s1` requires `--predicted` to be the commit candidate `F` names |
| the predicted tree's push starts no workflow | `C10`: before that push, the push-triggered workflows at `D` and their branch and path filters are listed against the tree's branch and paths, with the result recorded on the pull request |
| `F`'s run is consistent with the absence (none of the round's steps or its shard); never the proof of it | `C5`: P (`frun_consistent`) at S1 and `E` |
| every stage-1 requirement can be met by `F`'s own tree and run (no control `F` can never satisfy) | `C9`: `controls.py mock-s1 <candidate F> --f-run <result derived from candidate F's actual exact-head run> --predicted <P> --run-api RUN --jobs-api JOBS --evidence evidence/predicted-tree-run.json=<pinned file>` prints `controls: OK`, before designation; its output and the derived file's sha256 are recorded on the pull request with the designation request (*Preconditions of `F`*, condition 3); reviewers check that stage 1's `evidence/f-run/results.json` has that digest |
| the corrected `F` rule accepts a real `F` run without the module (regression) | `C5`: the self-test's real-evidence cases (KTRANS-SEP-1's `F` run and predicted-tree run, digests pinned in `controls.py`), run in the shard at `E` |
| missing module evidence is rejected where the module is required | `C5`: `run_ok` and the verdict's VOID rule; the self-test's two negative controls, run in the shard at `E` |
| module presence in `F`'s tree is rejected whatever its run shows; a failed job or step in `F`'s run is rejected | `C5`: the self-test's tree-half negative control (scratch commits with the module, the import line or the probe) and its run-half cases, run in the shard at `E` |
| the module is registered; no manuscript or ROADMAP changes | `C4`: the release gate at `E` passing every step, `lean-manuscript` included; `C5` (C, G) |
| the change stays inside the governed paths, with exactly the frozen import, census and workflow edits | `C6`: `git diff --no-renames --name-status D E`; `C5` (G, I, C, W) |
| the pre-`F` evidence is retained and unchanged (§A.42 item 2) | `C5` (P) at `E` against the digests below; reviewers check that each pin resolves to retained content |
| `F`'s exact-head run result is carried by the first execution commit | `C8`: `evidence/f-run/results.json` at stage 1, naming `F`, its run, its bridge job and the answers' digests; `C5` (P, R) |
| `E`'s claims are re-established from `main` (§A.42 item 7: `E` is on `main` once the round lands, and its workflow run re-establishes them; no separate retention pull request) | `C7`: the receipt's candidate entry for `E` and `v3_verifier --verify-round Q`; the workflow run at `E` |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

`RUN` and `JOBS` bind to `E` through the run's identity (*The decision rules*, *The run*). That the run is the one dispatched for the
exact-head attestation is the host attestation `C3`, which the receipt records and no control reads.

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

- **The predicted tree's design run.** Workflow run 39173554213, `workflow_dispatch`, attempt 1, head `bd579bf8db6065f6667511ee0a02fa31effc1f5b`.
  Conclusion `success`; 38 of 38 jobs `success`. In its Mathlib bridge job 117811475147 the Build and Release gate
  steps concluded `success`; its log showed the module built with warnings only, all fifteen reports
  `[propext, Classical.choice, Quot.sound]`, and the release gate passing all 22 steps. That tree's workflow carries
  none of this round's bridge steps, so this round's rules do not read that run's cells. Its runs and jobs API answers,
  with those of KTRANS-SEP-1's `F` run 39940836089, are the self-test's real regression fixtures, derived by
  `derive-run` and embedded in `controls.py`.

- **An earlier predicted tree, read through its log.** Commit `8c48a1e371312449f2e5cf097abb70ae82ee4fe9`, a child of
  `D` carrying this round's module, probe, import line and census family, and a workflow whose bridge job ended in a
  single step that printed the module's reports and ran the gate in the job log. It was dispatched twice on one
  branch: runs 40000328438 and 40002599527, `workflow_dispatch`, each green on all 39 jobs, with that step `success`.
  - The jobs API listed every job and every bridge step of both runs with its conclusion.
  - The job-log tool served only the last 5000 lines of each bridge log, of 41945 and 41873. The session's network
    policy refused the full log's download.
  - In the second run, which restored the first run's build cache under the same primary key
    (`oibridge-Linux-324962b2…-330fe661…`), the served lines held neither a `Built` nor a `Replayed` status line for
    the module.

  Whether a run had rebuilt the module could not be read from its log. The step conclusions were complete in both
  runs. This round's verdict reads only step conclusions (*The decision rules*), and those runs are provenance.

**Retained evidence (§A.42).** Each file is a structured expected result in §A.42 item 1's form, and states its
form:

- `evidence/design-run-1.json`, `evidence/design-run-2.json` — KTRANS-SEP-1's files, byte for byte, `derived` then
  from the served job logs and the runs and jobs APIs, and record-only here. They give build success, the release
  gate's steps and verdict, the module's `#print axioms` reports with their axioms, the build errors, the failure
  markers, and every job's conclusion. No control of this round reads their content;
- `evidence/exact-replay.json` — `complete`: the round's own local replays of the probe and of `controls.py exact`,
  with their output digests and lines;
- `evidence/d-push-run.json` — `derived` from the runs and jobs API answers: the identity and job outcomes of `D`'s
  push run, without its timestamps;
- `evidence/predicted-tree-run.json`, pinned, and `evidence/f-run/results.json`, added at stage 1 — `derived` by this
  round's frozen recipe, `controls.py derive-run --run-api RUN --jobs-api JOBS`, from the runs and jobs API answers
  for the run (`RUN`, `JOBS`; the jobs answer lists every job of the run in one answer, `per_page` 100, or the recipe
  refuses it). The result is a function of those two answers alone. It records:
  - the run's identity (repository, head repository, workflow path, run id, attempt, event, status, conclusion,
    branch, `head_sha`);
  - every job's name and conclusion, after checking that every job carries the run's id, attempt and commit;
  - the Mathlib bridge job's id, status, conclusion and steps, each with its name and conclusion, in step order;
  - in `source`, the digests of the two answers.

  It drops every timestamp, url and head-commit field the host returns. The answers are not retained (§A.42 item 4).

Each file names its commit, run and recipe and, as provenance, the digests of what it was read from. No file carries a
timestamp or duration. No archive check reads a round's record directory; the round's own control P checks these
files: digest, schema, form, no run-varying field, and for a run result its head, outcome, jobs and bridge steps. The
files are committed to the record directory by the first execution commit, outside `amendments/`, and pinned here
before `F`. `F` is not designated with a pending pin.

| path | sha256 |
| --- | --- |
| `evidence/design-run-1.json` | `2a9f30ca1a85d3bc5e728a98edfc047d6d8bbde3c1c5d387c2043038f9962d49` |
| `evidence/design-run-2.json` | `32045681fb4749a5ec95a49db5cb95c852b0652021b38b072da55001413c4a03` |
| `evidence/exact-replay.json` | `e033a96a670f6425c9d547f7e0650946ee040f16ecc3dd87ed996de9341921f7` |
| `evidence/d-push-run.json` | `1603fcb20a24e4484a262bfab07e441d48e6aa1caaa69c592a48a01e2d55356f` |
| `evidence/predicted-tree-run.json` | `cccefa27a380494735427a0f9c89b73dab66472400ad9ce45597f52083fb6ecd` |

`evidence/exact-replay.json` is re-derived because it names `controls.py`'s blob and path. The exact layer's output is
unchanged (sha256 `daba6b7b…`). `evidence/d-push-run.json` is derived for this `D`. `evidence/predicted-tree-run.json`
is this round's predicted tree's own run (*Preconditions of `F`*, condition 1).

**The frozen `controls.py`:** blob `73f356565ce1402b37da80a5d18dddd556df23c5`.

**The design commits.** The two design-run heads, KTRANS-SEP-1's predicted tree and this round's earlier predicted
tree are named in full in their entries above. Main reaches none of them; under `AGENTS.md` §A.42 items 1–2 they are
provenance, held under these refs:
- `preserve/ktrans-sep-824-design-195dfbee`;
- `preserve/ktrans-sep-824-design-95beab2b`;
- `preserve/ktrans-sep-824-predicted-bd579bf8`;
- `draft/ktrans-sep-2-predicted-tree`.

The round's claims rest on the files pinned above, carried into the record, and on the module and probe its execution
lands. The design-run files are KTRANS-SEP-1's, carried byte for byte. This round derives its own run results with
`controls.py derive-run`, and neither reads nor extends the archive.

### The predicted execution tree

- **`79455c44b5d70b0af01668ec34dd2c438808717c`** tree `1a53db4e713506b41704207d259f647ce8094524`, a single-parent
  child of `D`, on `draft/ktrans-sep-2-predicted-tree-r13`. Its files and blobs:
  - `.github/workflows/verify.yml` `27ba2b1bf0127f7c76552cd5ab3011796051a767`;
  - `verification/lean-manuscript-census.json` `d6302d70f4eee1fd2c6cb1e1f71d3d239b7a44e4`;
  - `verification/lean-mathlib/OIBridge.lean` `1c919c5c68b563e700461a8954dd107cf176036d`;
  - `verification/lean-mathlib/OIBridge/TransSeparation.lean` `ba7431915e7ab6e8f7bdfb6ab980f16067e9331b`;
  - `verification/lean/ktrans_sep1_probe.py` `19e19f28fa7644de0bcc3089a354317310de3e41`;
  - in this round's record directory:
    - `controls.py` `73f356565ce1402b37da80a5d18dddd556df23c5`;
    - `evidence/d-push-run.json` `26fc275edd4eab6e3b000fa8abb1a7b0e14722c8`;
    - `evidence/design-run-1.json` `efdb93318d07153034d087b34b03a1993443e57f`;
    - `evidence/design-run-2.json` `0e88741075aeabf3fb261612adc4bab149e27256`;
    - `evidence/exact-replay.json` `6b900d0a682a9cc41ff5c3e75ebe8cabd1f415e5`;
    - `preregistration.md` `b7d0c3e9b3d0b05e97c85d46ce1f9fa79f2f042b`, this preregistration's drafting revision.

  At this commit, `controls.py check 79455c44b5d70b0af01668ec34dd2c438808717c` printed `controls: OK -- 24 checks`
  and `controls.py --self-test` printed `controls: OK -- 120 checks`. Its run is workflow run 40067399041,
  `workflow_dispatch`, attempt 1, green on all 39 jobs, with Build, Release gate, L0, L and A `success` and M
  `skipped` in bridge job 120793426164; its result is `evidence/predicted-tree-run.json` (*Preconditions of `F`*,
  condition 1).

The entry lists the tree's files with their blobs. The tree is a single-parent child of `D` that carries:
- the record files:
  - this preregistration in its drafting revision, which differs from the revision at `F` in this section, the pin of
    the predicted tree's run, the status line and the preconditions' `Open` markers;
  - `controls.py` at its pinned blob;
  - the pinned evidence files other than the predicted-tree run result;
- the five execution paths: the module and the probe at their frozen blobs, and `OIBridge.lean`, the census and
  `verify.yml` exactly as I, C and W require at this `D`.

`delta(D, <commit>)` is exactly those record files and the five execution paths. Before its run is dispatched,
`controls.py check <commit>`, run from the tree's own `controls.py`, and `controls.py --self-test` both print
`controls: OK`, and their outputs are recorded with the entry. Stage 1 and S1 carry the same `controls.py`, module and
probe blobs and the same three edited files, which B, I, C and W check, so the run tests the bytes the execution
lands. Before the tree is pushed, the push-triggered workflows at `D` are listed with their branch and path filters
against its branch and paths, and the finding that none starts is recorded on the pull request (`C10`).

KTRANS-SEP-1's predicted tree `bd579bf8db6065f6667511ee0a02fa31effc1f5b` (tree
`ee0298491f43c391dad00e202d895f988d12017d`) is provenance: a child of that round's `D` carrying this round's module
and probe blobs, KTRANS-SEP-1's `controls.py` (`412802eb`) and that round's edits of the three files at its `D`.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and its run are design evidence, not
attestations.

## Stages and outcomes

`F` is given to `--freeze` and to `mock-s1` as its full 40-character commit id; an abbreviated `F` fails P and T,
and never passes them.

**Stages.**
1. **C1** adds `controls.py` at its frozen blob, the pinned evidence files and `evidence/f-run/results.json`, the
   structured expected result of `F`'s exact-head run. Acceptance: each blob is the frozen blob or matches its pin,
   and `evidence/f-run/results.json` has the digest recorded under condition 3 of *Preconditions of `F`*.
2. **S1** adds the module, the probe, the import line, the census family and the workflow edit in one commit.
   Acceptance: `controls.py check S1 --freeze F --stage S1` passes; the exact-head run at S1 has every job green.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F
   --run-api RUN --jobs-api JOBS` passes and the exact-head run at `E` has every job green.

**Outcomes.**
- **`KTRANS-SEP-2-READ`**, when all of these hold:
  - `controls.py check E --freeze F --run-api RUN --jobs-api JOBS` prints `controls: OK`;
  - `controls.py verdict E --freeze F --run-api RUN --jobs-api JOBS` prints one token for each of the three cells, not
    VOID;
  - the exact-head run at `E` is green on every job;
  - the result note states each cell's token, the earned reading in its frozen words exactly when all three cells are
    positive, and the non-inference rule.
- **`KTRANS-SEP-2-HALTED`**: anything else (`S12`). The result note names the failing check or job, and the tokens
  `verdict` printed when it read a negative cell (*The negative readings and the outcome*). A VOID verdict is not an
  outcome: the evidence is taken again, and if it cannot be made complete the round halts.

No outcome sources boundary transitivity or its dense form, adopts either as a premise, or edits the ROADMAP or a
manuscript. Correctness bands are unchanged by either outcome: the round is consistency-axis work.

## Preconditions of `F`

`F` is not designated until all three hold:

1. **The predicted tree's design run.** `verify.yml` is dispatched on exactly the commit in *The predicted execution
   tree*. The run is green on every job, and its bridge job's L0, L and A conclude `success` and M `skipped`. Its retained
   result `evidence/predicted-tree-run.json` is derived by `controls.py derive-run` from the run's runs and jobs
   answers and pinned above in the form P requires. The two answers are kept as captured, byte for byte, and supplied
   to the reviewers; they are not committed, because they carry personal data (§A.42 item 4). The command, the sha256
   of each captured answer (which the file's `source` records) and the file's sha256 are recorded on the pull request
   with the pin. Before `F` is designated, reviewers check the captured answers they were given against those digests
   and check that `derive-run` over them reproduces the pinned file byte for byte. The check needs the captured bytes:
   the same answer fetched again can come back in other bytes, since another client can serialize it differently
   (`gh api` prints it compact), and a re-run of the run changes its `run_attempt` and `updated_at`; then its digests,
   and the `source` the file would record, differ. If the captured answers cannot be supplied, no byte-for-byte
   reproduction is claimed. No control reads this derivation; P checks the file's digest and `run_ok`. The dispatch
   needs the owner's authorization. Met.
2. **No pin pending.** `evidence/exact-replay.json` and `evidence/d-push-run.json` are derived and pinned,
   `controls.py`'s blob is pinned (*The frozen `controls.py`*), and *The predicted execution tree* names its commit.
   Met.
3. **The mock first-execution check on this round's own candidate `F` (the safeguard).**
   - After candidate `F`'s exact-head run is green, the runs and jobs API answers for **that actual run** (`RUN`,
     `JOBS`) are taken. `evidence/f-run/results.json` is `controls.py derive-run` over them, never derived from an
     invented or edited answer.
   - Then `controls.py mock-s1 <candidate F, its full 40-character commit id> --f-run <that file>
     --predicted <the predicted tree> --run-api RUN --jobs-api JOBS
     --evidence evidence/predicted-tree-run.json=<the pinned file>` runs. It requires the file to be
     `derive-run`'s output over those answers and the predicted tree to be the one candidate `F` names. It builds a
     mock stage-1 commit in a temporary object directory with no ref, and prints `controls: OK`. That output includes
     P's three F-stage checks: the absence read from candidate `F`'s tree, and the identity, jobs, success and bridge
     steps read from that run's result.
   - The command, its full output and the derived file's sha256 are recorded on the pull request with the designation
     request.

   KTRANS-SEP-1's real evidence passing the corrected rule is a regression check of the rule, not this condition.
   Open.
