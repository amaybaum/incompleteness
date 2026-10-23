# Reconstruction round KTRANS-SEP-2 — Ω₄, a convex body in ℝ⁴ with the named kernel properties on which no body-preserving family is boundary transitive: PREREGISTRATION (draft for owner review)

**Status: draft control plane for owner review; not a candidate `F`.** This file is the control plane of a native
round under `AGENTS.md` §A.39, to be drafted on its guiding pull request from `D`. Only the owner designates `F`; an
instruction to proceed is not a designation. `F` has the preconditions listed under *Preconditions of `F`* at the end;
none is met yet. Nothing is executed.

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
  Its push run is recorded in `evidence/d-push-run.json` (pending: derived before `F` from the runs and jobs APIs, as
  KTRANS-SEP-1's was).
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
anchored there.

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

The module is blob **`ba7431915e7ab6e8f7bdfb6ab980f16067e9331b`**. It imports `OIBridge.DenseOrbit` only; namespace
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
`import OIBridge.KTokenMaxCone` (`:270` at `D`).

**Census family**, inserted directly after KTOKEN-MAXCONE-1's family (modules `["KTokenMaxCone"]`), in `D`'s two-space
JSON layout: name "Ω₄, the ℓ⁴-sum of the Euclidean 3-ball and the segment, is compact, convex, with interior, drivable,
with a sharp seed, relatively strictly convex and centrally symmetric, is no affine image of the Euclidean ball, and
admits no body-preserving family that is boundary transitive or has a dense boundary orbit (round KTRANS-SEP-2,
reconstruction)", `modules: ["TransSeparation"]`, `status: "kernel-only"`, `manuscript: []`.

## The exact layer

**The frozen probe** `verification/lean/ktrans_sep1_probe.py`, blob **`19e19f28fa7644de0bcc3089a354317310de3e41`**
(the path and bytes KTRANS-SEP-1 froze; its docstring names that round, which designed it),
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

`LOG` is the served text of the Mathlib bridge job of the exact-head run at `E`, and `META` the tool's line counts for
it (`{"original_lines": N, "served_lines": M}`). `controls.py verdict E --freeze F --log LOG --log-meta META` first
runs every control of `check E --freeze F`. `--log-meta` is mandatory for the round's verdict: `controls.py` accepts
a call without it, and such a call is not the round's verdict (*Stages and outcomes*). It prints the cells only from
complete evidence; otherwise it prints
`VERDICT  VOID` with the reason, prints no token, and exits 1. **VOID is not an outcome.** A tooling failure or
incomplete evidence never yields a `NOT-ESTABLISHED` token: the evidence is taken again (the log served again, the run
repeated) or the round halts under `S12`.

**VOID** when any of these holds: a required control failed or never ran; `LOG` is empty, or `META` does not describe
it; a frozen report is missing, duplicated, at another source line or unparsable; the line
`Built OIBridge.TransSeparation` is not in the served window before the first report (the window may begin inside the
report block); the build line or the release-gate block is missing, or the gate fails at a step outside the module;
sympy `1.14.0` is not importable; the probe does not run to completion (non-zero exit, no `checks:` line, or no final
`VERDICT` line); or its output differs from the frozen output with no failing check. When `META` shows the full log
(`served_lines = original_lines`) the window is complete by construction; when it shows a tail, the build-line rule is
what establishes that the report block lies inside it.

| Cell | Outcome | Rule |
|---|---|---|
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-PROVED` | S1 holds for `not_affine_eball_omega4`, and the complete `LOG` has the build line, the release gate's PASS verdict, no build error in the module, and exactly one report for each of the fifteen prints at its `#print axioms` line, each within `[propext, Classical.choice, Quot.sound]` (among them `not_affine_eball_omega4`) |
| Q-NONELL | `KTRANS-SEP-NONELLIPSOID-NOT-ESTABLISHED` | complete evidence of a failure in the module: every frozen report present, some report outside the three axioms, and either the gate failing at `lean-axioms` alone or a build error in the module |
| Q-CEX | `KTRANS-SEP-COUNTEREXAMPLE-PROVED` | S1 holds for `omega4`, `not_affine_eball_omega4`, `not_boundaryTransitive_omega4`, `not_denseBoundaryOrbit_omega4` and `kinfTrans_separation`, and the same `LOG` facts as for Q-NONELL hold |
| Q-CEX | `KTRANS-SEP-COUNTEREXAMPLE-NOT-ESTABLISHED` | as for Q-NONELL |
| Q-EXACT | `KTRANS-SEP-INSTANCES-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I -B` under sympy `1.14.0`, prints exactly the frozen output (sha256 `d6f6d298d3ed57081f4e81bef267771fc81d8083a111c0414a69216c772a2940`), which contains the twelve `PASS` lines, `COUNTER XW1 fails as stated`, `COUNTER XW2 fails as stated`, `checks: 12, failures: 0` and `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS`; and X1–X3 and CX1–CX4 hold |
| Q-EXACT | `KTRANS-SEP-INSTANCES-NOT-ESTABLISHED` | a complete probe run in which a check failed (`FAIL`, `DID NOT FAIL` or `NOT RENDERED`) |

No rule reads another cell's outcome. `#print axioms` reports every axiom of a declaration's dependency closure, so a
`sorry` anywhere beneath a printed theorem shows in its report; N3 also rejects one in the module's text. The outcome
is `KTRANS-SEP-2-READ` when the three cells are assigned; the tokens are those `controls.py verdict E` prints.

**No vacuous verdict, and no tooling negative.** Every VOID condition above, and each of the two negative routes, is
driven by a self-test case: an empty log, a log cut before the build line and one cut inside the report block, a
missing, duplicated, misplaced or wrapped report, a missing gate verdict, a gate failing outside the module, an
incomplete build, `sorryAx` beside a passing gate, `META` that does not match the text, a probe that crashes, a probe
whose import fails, sympy absent or of another version, a probe output cut before its verdict or reduced to its
summary, and a changed non-check line all give VOID; `sorryAx` with the gate failing at `lean-axioms` alone, `sorryAx`
with a module build error, and a complete probe run with a failing check give the negative tokens.

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

`.github/workflows/verify.yml` at `E` is `D`'s with five splices, each anchored once at `D`:

- the shard `probes_ktranssep2`, `Numerical probes / KTRANS-SEP-2 Omega4 counterexample`, inserted directly before the
  Act 42 comment (`:483`), after KTOKEN-MAXCONE-1's shard. It checks out with `fetch-depth: 0` (the controls read `D` through git),
  sets up Python 3.11, installs `sympy==1.14.0`, and runs three steps: the probe from `verification/lean` with
  `python3 -I -B`, its output kept and the step failing unless the line
  `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS` is present (the probe itself exits 0); `controls.py exact`; and
  `controls.py --self-test`;
- in the aggregate `Numerical probes` job: `probes_ktranssep2` after `probes_ktokenmaxcone1` in `needs` (`:578`);
  `KTRANSSEP2_RESULT: ${{ needs.probes_ktranssep2.result }}` after `KTOKENMAXCONE1_RESULT` (`:599`);
  `echo "ktranssep2=${KTRANSSEP2_RESULT}"` after the KTOKEN-MAXCONE-1 echo (`:621`);
  `test "${KTRANSSEP2_RESULT}" = success` after the KTOKEN-MAXCONE-1 test (`:642`).

The exact text is embedded in `controls.py` (control W).

## The controls (in `controls.py`)

`controls.py` imports nothing from the repository and changes nothing; it reads `D` and the commits it is given with
read-only git commands and embeds every frozen text. Its codes:

- **G** governed paths: `delta(D, commit)` is exactly the five execution paths with their statuses, plus record files.
- **R** record: only the permitted files; `evidence/f-run/results.json` required with `--freeze`; the result note
  required at `E` and absent at `S1`.
- **P** pins: every file pinned in *Retained evidence* is present with its sha256; the table names the four required
  files; with `--freeze` no pin is pending. Each pinned file is a structured result (`schema`, `version`, a stated
  `form` of `complete` or `derived`, a source digest when derived) with no timestamp or duration field. Each run
  result is checked for what its stage validates (*Stage requirements*):
  - the predicted tree's run result (`evidence/predicted-tree-run.json`) names the commit in *The predicted execution
    tree*, is a green `workflow_dispatch` run, and records in `observed.transseparation_window` the served line of
    `Built OIBridge.TransSeparation`, of each of the fifteen reports and of the gate block's start and end, all inside
    the served window and in that order, with the fifteen reports within the three axioms and the gate passing
    (`run_window_ok`);
  - `F`'s run result (`evidence/f-run/results.json`, with `--freeze`) names `F`, is a green `workflow_dispatch` run
    with every job `success`, a successful build and a passing gate, and records the module **absent**: status
    `absent`, no report, and an empty window (`frun_ok`). A result recording any module evidence fails: `F` carries
    the control plane only.
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
  three cells are positive, the non-inference rule always; `--log` is required there, and a VOID reading fails V.

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
family reduced to `{id}` (CX4 alone); the probe and log cases of *No vacuous verdict, and no tooling negative*, among
them a real crashing probe and a real failing import; the evidence-file cases of P (no form, an unknown form, a derived
result without a digest, a timestamp field, a duration field; for a run result another head, a push event, a failed
job, no jobs, a report past the window, the build line after a report, a missing report, the gate inside the
reports, a gate past the window, a non-standard axiom, a failed gate); the verdict gate with each required
control failed or missing; the note with an extra token, an altered earned reading, no non-inference rule, the earned
reading under a negative cell, and a frozen phrase (a neutral addition passes); and the pure cores of I, C, W, G, R, P
and T, including a merge, a re-cut `F` and an `F` not on `D`. Positive controls: the frozen module, the landed ball
control, the exact layer, the frozen probe run, a proof-only repair, a complete log with every frozen report standard,
and log metadata showing a full and a tail window.

It adds, against the defect:
- **regression (real evidence):** `frun_ok` accepts KTRANS-SEP-1's real `F` run result (run 39940836089, head
  `7e9aef69`, the module absent), embedded verbatim with its sha256
  `d2ac295647dfb593a09026de51ad145102645dcc98dee1bd7d25988c6623ca8f`, which the old rule rejected; and rejects
  another head, a push event, a failed job, no jobs, a failed build, a failed gate, and a result recording a build
  line, a report or the module complete;
- **negative control, missing module evidence where it is required:** that real result, offered as a module-bearing
  run result (the predicted tree's or `E`'s), is rejected by `run_window_ok`;
- **negative control at `E`:** a complete, green, gate-passing log with no module build line and no report — the shape
  of a run whose tree lacks the module, as `F`'s did — is VOID, never a token.

The regression cases test the corrected rule; they are not the safeguard. The safeguard is condition 3 of
*Preconditions of `F`*, run on this round's own candidate `F`. It passes 90 checks.

`controls.py` is the draft generated from KTRANS-SEP-1's blob `412802eb` by `make_controls.py` (asserted
replacements only; the draft notes list them); its blob is pinned when this draft is reviewed.

## Stage requirements (what each run validates)

| stage | its tree | its run validates | evidence | control that reads it | negative control |
| --- | --- | --- | --- | --- | --- |
| `F` | `D` plus the control plane; no module | the control plane: every job green, build success, gate PASS; the module **absent** | `evidence/f-run/results.json`, added at stage 1 | P (`frun_ok`) at S1 and `E` | a result recording a build line, a report or the module complete fails `frun_ok` |
| predicted tree | `D` plus the predicted execution files | the proposed implementation: the module built, its fifteen reports within the three axioms, gate PASS | `evidence/predicted-tree-run.json`, pinned before `F` | P (`run_window_ok`) | KTRANS-SEP-1's real `F` run (no module), offered here, fails |
| `E` | the actual execution | the actual execution: the module built at `E`, the fifteen reports, gate PASS | `E`'s served bridge log (`LOG`, `META`) | `verdict`: VOID unless the build line and every report are in the window | a complete green log without the module's lines is VOID |

`mock-s1` (condition 3 of *Preconditions of `F`*) runs the stage-1 acceptance on candidate `F`'s own actual run result
before `F` is designated, so that a requirement `F`'s run cannot meet fails before the freeze.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F`; `T` in `controls.py check E --freeze F` |
| the controls, module and probe are the frozen ones | `C2`: `git rev-parse <commit>:<path>` equal to the frozen blobs, for `controls.py` at stage 1 and all three at `E`; `B`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms; no `sorryAx` | `C3`: the exact-head run at `E`, every job `success`; the fifteen reports read by `controls.py verdict E --freeze F --log LOG` |
| the decisive step is the module's own construction | `C5`: X3 in `check E --freeze F` |
| the exact layer replays; its countercontrols fail as stated | `C3`: shard `probes_ktranssep1` green; `verdict` re-runs the probe blob at `E` against the frozen output digest |
| no positive token over a failed or missing control | `C5`: the verdict gate; its self-test cases run in the shard at `E` |
| a tooling failure or incomplete evidence never yields a token, positive or negative | `C5`: the VOID rules of `verdict`; their self-test cases (log, probe, sympy, metadata) run in the shard at `E` |
| the served `LOG` is complete for the fifteen reports | `C5`: `verdict` with `--log-meta`, the build-line-before-reports rule; `C8`: `evidence/predicted-tree-run.json` records the window, checked by P (`run_window_ok`) |
| `F`'s run validates the control plane only: green, gate PASS, the module absent | `C5`: P (`frun_ok`) on `evidence/f-run/results.json` at S1 and `E` |
| every stage-1 requirement can be met by `F`'s own run (no control `F`'s run can never satisfy) | `C9`: `controls.py mock-s1 <candidate F> --f-run <result derived from candidate F's actual exact-head run> --predicted <P> --evidence evidence/predicted-tree-run.json=<pinned file>` prints `controls: OK`, before designation; its output and the derived file's sha256 are recorded on the pull request with the designation request (*Preconditions of `F`*, condition 3); reviewers check that stage 1's `evidence/f-run/results.json` has that digest |
| the corrected `F` rule accepts a real `F` run without the module (regression) | `C5`: the self-test's real-evidence cases (KTRANS-SEP-1's `F` run, digest pinned in `controls.py`), run in the shard at `E` |
| missing module evidence is rejected where the module is required | `C5`: `run_window_ok` and the verdict's VOID rule; the self-test's two negative controls, run in the shard at `E` |
| the module is registered; no manuscript or ROADMAP changes | `C4`: the release gate at `E` passing every step, `lean-manuscript` included; `C5` (C, G) |
| the change stays inside the governed paths, with exactly the frozen import, census and workflow edits | `C6`: `git diff --no-renames --name-status D E`; `C5` (G, I, C, W) |
| the pre-`F` evidence is retained and unchanged (§A.42 item 2) | `C5` (P) at `E` against the digests below; reviewers check that each pin resolves to retained content |
| `F`'s exact-head run result is carried by the first execution commit | `C8`: `evidence/f-run/results.json` at stage 1, naming `F`, its run, job and the served log's digest; `C5` (P, R) |
| `E`'s claims are re-established from `main` (§A.42 item 7: `E` is on `main` once the round lands, and its workflow run re-establishes them; no separate retention pull request) | `C7`: the receipt's candidate entry for `E` and `v3_verifier --verify-round Q`; the workflow run at `E` |
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

- **The predicted tree's design run.** Workflow run 39173554213, `workflow_dispatch`, attempt 1, head `bd579bf8db6065f6667511ee0a02fa31effc1f5b`.
  Conclusion `success`; 38 of 38 jobs `success`. In its Mathlib bridge job 117811475147 the Build step passed
  (`Build completed successfully (3653 jobs)`, `Built OIBridge.TransSeparation` with warnings only), all fifteen
  reports at `TransSeparation.lean:532–546` are `[propext, Classical.choice, Quot.sound]`, and the release gate
  passed all 22 steps (`lean-axioms` 6004 named results with no `sorryAx`, `lean-manuscript` OK, 303 legacy records
  intact, 48 receipts holding, `evidence-retention` holding). The served window is the last 5000 of 38670 lines; in
  it the module's build line is at 4896, the reports at 4909–4923 and the gate block at 4951–4976
  (`evidence/predicted-tree-run.json`). Read by `controls.py`'s cell rules, this log and the frozen probe give the
  three positive tokens.

**Retained evidence (§A.42).** Each file is a structured expected result in §A.42 item 1's form, and states its
form:

- `evidence/design-run-1.json`, `evidence/design-run-2.json` — `derived` from the served job logs (the session's
  job-log tool serves the last 5000 lines; every report the files record lies in the served text, at the served lines
  they record) and from the runs and jobs APIs: build success, the release gate's steps and verdict, the module's
  `#print axioms` reports with their axioms, the build errors, the failure markers, and every job's conclusion.
  `compare_result.py` requires a passing gate, which neither run had, so their recipes compare by hand;
- `evidence/exact-replay.json` — `complete`: the round's own local replays of the probe and of `controls.py exact`,
  with their output digests and lines;
- `evidence/d-push-run.json` — `derived` from the runs and jobs API answers: the identity and job outcomes of `D`'s
  push run, without its timestamps;
- `evidence/predicted-tree-run.json`, pending, and `evidence/f-run/results.json`, added at stage 1 — `derived` from
  the bridge job's served log and the runs and jobs APIs. Beyond a design-run file's content each records, in
  `source`, the log's `original_lines` and `served_lines`, and in `observed.transseparation_window` the served line of
  `Built OIBridge.TransSeparation`, of each of the fifteen reports and of the gate block's start and end; P requires
  them inside the window and in that order.

Each file names its commit, run, job and recipe and, as provenance, the digest of the text it was read from, and no
file carries a timestamp or duration. `verification/audits/evidence-retention/check_retention.py` reads the archive,
not round record directories, so it does not check these files; the round's own control P does (digest, schema,
form, no run-varying field, and for a run result its head, outcome and window). The files are committed to the record
directory by the first execution commit, outside `amendments/`, and pinned here before `F`. `F` is not designated
with a pending pin.

| path | sha256 |
| --- | --- |
| `evidence/design-run-1.json` | `2a9f30ca1a85d3bc5e728a98edfc047d6d8bbde3c1c5d387c2043038f9962d49` |
| `evidence/design-run-2.json` | `32045681fb4749a5ec95a49db5cb95c852b0652021b38b072da55001413c4a03` |
| `evidence/ktrans-sep-1-predicted-tree-run.json` | `58fcf6fec66e8c695c923810b67d20040d801f5c8b71adfad561b42855e21ef7` |
| `evidence/exact-replay.json` | pending |
| `evidence/d-push-run.json` | pending |
| `evidence/predicted-tree-run.json` | pending |

`evidence/design-run-1.json`, `evidence/design-run-2.json` and `evidence/ktrans-sep-1-predicted-tree-run.json` are
KTRANS-SEP-1's files, byte for byte; the last is the run of KTRANS-SEP-1's predicted tree `bd579bf8` (run 39173554213),
which built this same module blob green with the fifteen reports standard. `evidence/exact-replay.json` is re-derived
because it names `controls.py`'s blob and path; the exact layer's output is unchanged (sha256 `daba6b7b…`, measured on
the draft). `evidence/d-push-run.json` is derived for this `D`. `evidence/predicted-tree-run.json` is this round's
predicted tree's own run (*Preconditions of `F`*, condition 1).

**The design commits.** The two design-run heads and KTRANS-SEP-1's predicted tree are named in full in their run
entries above. Main reaches none of them; under `AGENTS.md` §A.42 items 1–2 they are provenance, held under
`preserve/ktrans-sep-824-design-195dfbee`, `preserve/ktrans-sep-824-design-95beab2b` and
`preserve/ktrans-sep-824-predicted-bd579bf8`. The round's claims rest on the files pinned below, carried into the record,
and on the module and probe its execution lands. The evidence-retention archive is frozen (§A.42 item 8) and is not
used.

### The predicted execution tree

This round's predicted tree is built on this `D` when the draft is reviewed, and recorded here with its blobs. The
entry below is KTRANS-SEP-1's, kept as the template and as provenance; its `controls.py`, `OIBridge.lean`, census and
workflow blobs are that round's, and the module and probe blobs are this round's too.

- **KTRANS-SEP-1's predicted tree, provenance: `bd579bf8db6065f6667511ee0a02fa31effc1f5b`** (a single-parent child of that round's `D`, tree `ee0298491f43c391dad00e202d895f988d12017d`) is the
  execution tree less the result note, `evidence/f-run/` and `evidence/predicted-tree-run.json` (which records this
  tree's own run). Its files and blobs:
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/preregistration.md`, blob `952be2b011eaa21f58f98150cbb6066bd5809712`: this preregistration in its drafting revision, which differs from this revision in this section, in the design-evidence entry and the pin of the predicted tree's run, in the status line, and in the sentence that makes `--log-meta` mandatory;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/controls.py`, blob `412802eb11e74200734e4ae6511dcbef4d76613e`: `controls.py`;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/design-run-1.json`, blob `efdb93318d07153034d087b34b03a1993443e57f`: retained evidence;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/design-run-2.json`, blob `0e88741075aeabf3fb261612adc4bab149e27256`: retained evidence;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/exact-replay.json`, blob `60dc4a89b5d909e7b1dc432c3849dfd24d547cc7`: retained evidence;
  - `verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/evidence/d-push-run.json`, blob `f72fef3ec7c0df9bdf4429cdb3479d121ebb2879`: retained evidence;
  - `verification/lean-mathlib/OIBridge/TransSeparation.lean`, blob `ba7431915e7ab6e8f7bdfb6ab980f16067e9331b`: the module;
  - `verification/lean/ktrans_sep1_probe.py`, blob `19e19f28fa7644de0bcc3089a354317310de3e41`: the probe;
  - `verification/lean-mathlib/OIBridge.lean`, blob `ffff5cdeb7ab2c3cfff48099165aeb2b1acbc4c9`: `OIBridge.lean`, `D`'s with the import line;
  - `verification/lean-manuscript-census.json`, blob `5a914412b80f6287181dbe33be9c89ad0de7329d`: the census, `D`'s with the family;
  - `.github/workflows/verify.yml`, blob `3b30ced43df0bb7aa0c0a994bf7184837c0445ad`: the workflow, `D`'s with the five splices.
- `delta(D, bd579bf8)` is exactly those eleven paths: six record files and the five execution paths.
- At that commit `controls.py check bd579bf8`, run from the tree's own `controls.py`, passes all 24 checks, and
  `controls.py --self-test` passes 85 checks.
- Its design run is the run of *Design evidence* above; its retained result is `evidence/predicted-tree-run.json`.
  Every blob the run tested is the frozen blob of this file: `controls.py`, the module, the probe and the three edited
  files at `F`'s execution are those listed here.
- On a branch push this commit starts no workflow: `verify.yml` runs on `push` to `main` only, on
  `pull_request` and on `workflow_dispatch`; the three path-filtered workflows match none of its eleven paths; and
  `reproduce-evidence.yml` is dispatch-only.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and its run are design evidence, not
attestations.

## Stages and outcomes

**Stages.**
1. **C1** adds `controls.py` at its frozen blob, the pinned evidence files and `evidence/f-run/results.json`, the
   structured expected result of `F`'s exact-head run (the module absent). Acceptance: each blob is the frozen blob or
   matches its pin, and `evidence/f-run/results.json` has the digest recorded under condition 3 of *Preconditions of
   `F`*.
2. **S1** adds the module, the probe, the import line, the census family and the workflow edit in one commit.
   Acceptance: `controls.py check S1 --freeze F --stage S1` passes; the exact-head run at S1 has every job green.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F --log
   LOG --log-meta META` passes and the exact-head run at `E` has every job green.

**Outcomes.**
- **`KTRANS-SEP-2-READ`**: `controls.py check E --freeze F --log LOG --log-meta META` prints `controls: OK`;
  `controls.py verdict E --freeze F --log LOG --log-meta META` prints one token for each of the three cells, not VOID; the exact-head run at `E` is green on every job;
  the result note states each cell's token, the earned reading in its frozen words exactly when all three cells are
  positive, and the non-inference rule.
- **`KTRANS-SEP-2-HALTED`**: anything else (`S12`); the result note names the failing check or job. A VOID verdict is
  not an outcome: the evidence is taken again, and if it cannot be made complete the round halts.

No outcome sources boundary transitivity or its dense form, adopts either as a premise, or edits the ROADMAP or a
manuscript. Correctness bands are unchanged by either outcome: the round is consistency-axis work.

## Preconditions of `F`

`F` is not designated until all three hold:

1. **The predicted tree's design run.** `verify.yml` dispatched on exactly the commit in *The predicted execution
   tree*, every job green, and its retained result `evidence/predicted-tree-run.json` pinned above in the form P
   requires, its window recording the module's build line, reports and gate inside the served text. Open.
2. **No pin pending.** `evidence/exact-replay.json` and `evidence/d-push-run.json` are derived and pinned, and
   `controls.py`'s blob is pinned. Open.
3. **The mock first-execution check on this round's own candidate `F` (the safeguard).** After candidate `F`'s
   exact-head run is green: `evidence/f-run/results.json` is derived from **that actual run** (the served bridge log,
   read with `D`'s extraction code, and the runs and jobs APIs), never from an invented or edited log; then
   `controls.py mock-s1 <candidate F> --f-run <that file> --predicted <the predicted tree> --evidence
   evidence/predicted-tree-run.json=<the pinned file>` builds a mock stage-1 commit in a temporary object directory
   with no ref and prints `controls: OK`. The command, its full output and the derived file's sha256 are recorded on
   the pull request with the designation request. KTRANS-SEP-1's real evidence passing the corrected rule is a
   regression check of the rule, not this condition. Open.
