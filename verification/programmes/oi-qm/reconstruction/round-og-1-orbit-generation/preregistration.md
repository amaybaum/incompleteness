# Reconstruction round OG-1 — conditional orbit-generation infrastructure: PREREGISTRATION

**Status: drafting.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted on its
pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls and the evidence ledger below are fixed, and the design runs are recorded below.

```v3-round
round OG-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-og-1-orbit-generation/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-og-1-orbit-generation/
record AM verification/receipts/OG-1.json
execution A verification/lean-mathlib/OIBridge/OrbitGeneration.lean
execution A verification/lean-mathlib/OIBridge/OrbitNormalization.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/OG-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, and no other round's record
change under any outcome.**

## The objects

- **`D`** = `6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a`, the head of `main` after `CI-PERF-1` landed (push run
  36896981080, every job green; the act 42 exclusion matrix skipped on push). The owner designated it as this round's
  `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is: conditional orbit-generation infrastructure

The round lands kernel infrastructure for the reduced orbit-generation theorem and nothing that sources its premises.
Its strongest permitted conclusion is:

> given the stated seed/effect, drive, dimension and V4′ hypotheses, the normalized 3-ball route reaches the existing
> Lorentz bridge; the normalization and generated-action steps themselves require no additional physical premise.

**No outcome says that OI implies the one-system theorem**, that any hypothesis below is sourced, or that the round
reconstructs an elementary system.

### In scope

1. **`OrbitGeneration`** — the module validated in design (branch `claude/l-orbitgen-design`, commit `40025649`, run
   36945912933: built, 64 theorems with `[propext, Classical.choice, Quot.sound]` only), landed at exactly its
   design-validated theorem interface. The green design run is design evidence, not this round's attestation. Its
   named hypotheses stay hypotheses: P1 `SharpSeed`, V4′ `SeedOrbitAvailable`, K∞-R `BoundaryTransitive`, and the body
   premise `PreservesBody` (G-AUT).
2. **G-AUT under words** — generator preservation of the body extends to every word the generators generate. No new
   premise.
3. **Normalization / transport** — restriction to the affine span and affine coordinates ellipsoid → `ball3`, with
   states, effects, seed, drive and reversible action transported together, and the orbit equality and the Lorentz
   bridge stated invariantly, so that coordinate-independence downstream is explicit.
4. **`ball3Drive` transitivity** — the words of the landed control drive act transitively on the boundary of `ball3`;
   in the same frozen proposition family, the **4-ball countercontrol**: a body of affine dimension four whose
   automorphisms act boundary-transitively, so boundary transitivity does not source dimension three.
5. **F's parked lemmas, premise-free only**: B1 (`flow_zero` follows from `flow_add`) and B5 (a body each of whose
   points has a finite orbit under the affine automorphisms of the body admits no elementary drive).

   **B6 is excluded from OG-1 because inspection shows that it is a dimension-exclusion step.** B6 states that no
   body of affine dimension at most two admits an elementary drive. The layered NB-1 argument, which is not a kernel
   theorem, restricts balls to dimension one or three, and drivability already excludes the interval
   (`not_drivable_Icc`). B6 is the remaining step by which drivability would select dimension three, and dimension-3
   sourcing is frozen out. Its proof is not premise-free in this round's interface either: beyond finite automorphism
   groups (B5) it needs an inner product invariant under a compact group of affine automorphisms, which nothing
   landed supplies.
6. The census family entry for the new modules, `kernel-only`, carried by no manuscript.

### Frozen out

SC∞ (stage consistency) and the completion body; ELEM (the binary-visible scope premise); any source of the drive;
dimension-3 sourcing; V4′ adoption; the ellipsoid theorem (a drive on a three-dimensional body forces an ellipsoid);
K2 and the composite; TR, CAR and SCL; B6; NB-1 and any change to it; any manuscript or roadmap edit.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement or hypothesis without a new preregistration revision and new design theorem identity.

A design theorem identity is the pair below — the `OrbitGeneration` blob and the `OrbitNormalization` statement
surface — together with the `controls.py` blob that embeds them. A repair may change proofs only.

- **`OrbitGeneration.lean`** lands as blob `0673321f2920b38674685a1494c1cdbf42e0d2d1`, whole. Its principal theorem is
  statement-identical to the design-validated module of Thread L. This is checked mechanically: the SHA-256 of the
  file's bytes from its first `import` line to the end is
  `843c68c1a4d2dffff9b595475c710b960201c3ba8e218b71af1bfc50291415d9`, and it equals the same digest of the module
  built green at `40025649` (run 36945912933). Only the header comment differs.
- **`OrbitNormalization.lean`** is frozen by its statement surface, not by its blob. The surface has four parts:
  - the preamble (imports, namespaces, `open`, `variable`);
  - the 83 declarations, in order and by kind;
  - every theorem's signature up to `:=`;
  - every definition, whole.

  It also carries 20 frozen `#print axioms` lines. The reference blob is `bf627dfe3563fb9361e41fe7e633ea49168be95e`;
  proofs may differ from it.
- **`OIBridge.lean`** is `D`'s, with `import OIBridge.OrbitGeneration` and `import OIBridge.OrbitNormalization`
  inserted after `import OIBridge.KInfFoundations`.
- **The census** is `D`'s, with one family inserted after the KINF-2 family. The family is titled "conditional
  orbit-generation infrastructure", covers modules `OrbitGeneration` and `OrbitNormalization`, has status
  `kernel-only` and is carried by no manuscript. Its text is embedded in `controls.py`.

### The frozen proposition family

The principal statements, quoted from the frozen surface (V, W are real normed spaces):

| Row | Identifier | Statement |
|---|---|---|
| G-AUT | `preservesBody_words` | `PreservesBody Ω S → PreservesBody Ω (words S)`, `words S` the subgroup closure of `S` |
| G-AUT | `preservesBody_driveWords` | for `D : ElementaryDrivability Ω`, `PreservesBody Ω (words (range D.flow ∪ {D.J}))` |
| B1 | `flow_zero_of_add` | `(∀ s t, flow (s + t) = (flow t).trans (flow s)) → flow 0 = refl` |
| B5 | `isEmpty_drivability_of_finite_orbits` | every point of `Ω` has a finite orbit under the affine automorphisms of `Ω` (with inverse) → `IsEmpty (ElementaryDrivability Ω)` |
| NORM | `hypotheses_tr` | for `T : V ≃ᵃ W`, `PreservesBody`, `SharpSeed`, `BoundaryTransitive`, `SeedOrbitAvailable` of `(Ω, G, r, avail)` give the same four of `(T '' Ω, conjTr T '' G, effTr T r, effTr T '' avail)` |
| NORM | `seedOrbit_eq_of_normalization` | for `T : V ≃ᵃ ℝ³` with `T '' Ω = ball3`, under `PreservesBody`, `SharpSeed`, `BoundaryTransitive`: `seedOrbit G r = {(ballEffect b) ∘ T : ‖b‖ = 1}` |
| NORM | `lorentz_of_normalization` | under the same hypotheses, positivity of `conePair (effTr T e)` on the seed orbit gives `0 ≤ x0 ∧ ‖v‖² ≤ x0²` |
| NORM | `affineSpan_preserved`, `range_preserved` | a map of `Ω` into `Ω` preserves `affineSpan ℝ Ω`; under `PreservesBody` each member and its inverse preserve a chart range equal to the span |
| NORM | `hypotheses_restrict` | for an injective chart `w ↦ L w + p0` whose range is the affine span of `Ω`, every member of `G` restricts to a member of `autR L p0 G`, and the four hypotheses hold for `(bodyR, autR, effR r, effR '' avail)` |
| T3 | `boundaryTransitive_ball3Drive` | `BoundaryTransitive ball3 driveWords3`, `driveWords3 = words (range ball3Drive.flow ∪ {ball3Drive.J})` |
| T3 | `seedOrbit_ball3Drive` | `SharpSeed ball3 r → seedOrbit driveWords3 r = directionalFamily` |
| T4 | `boundaryTransitive_ball4` | `BoundaryTransitive ball4 isom4`, `ball4` the closed unit ball of `EuclideanSpace ℝ (Fin 4)` and `isom4` its linear isometries |
| T4 | `finrank_E4` | `Module.finrank ℝ E4 = 4` |
| core | `og1_infrastructure_core` | the conjunction of G-AUT, B1, the normalized orbit equality, T3 with `PreservesBody ball3 driveWords3`, T4 with `PreservesBody ball4 isom4`, and `finrank_E4` |

The 3-ball transitivity row and the 4-ball countercontrol row belong to one frozen proposition family. Boundary
transitivity holds for the drive words on `ball3` and for the isometries of a four-dimensional ball, so transitivity
does not select dimension three. No theorem in either module derives the affine dimension from transitivity.

### Semantic guards (in `controls.py`)

- **S1.** The 4-ball result is a kernel theorem: `boundaryTransitive_ball4` and `finrank_E4` are theorems with
  `#print axioms` lines, not probe output.
- **S2.** No theorem infers dimension three from transitivity. Only `finrank_E4` and the verdict mention `finrank`,
  and no theorem has `BoundaryTransitive` among its hypotheses and `finrank` in its conclusion.
- **S3.** G-AUT closes only the generated-word action from generator preservation. `preservesBody_words` has exactly
  one hypothesis, `PreservesBody` on the generators, and `words` is the subgroup closure.
- **S4.** Normalization transports everything together. `hypotheses_tr` and `hypotheses_restrict` conclude all four
  named hypotheses, each of the transported body, seed, automorphisms and available-effect family.
- **S5.** There are no sourcing claims:
  - no theorem concludes `SharpSeed`, `SeedOrbitAvailable` or `ElementaryDrivability` (other than its emptiness)
    without the same predicate among its hypotheses;
  - only the two named controls conclude `BoundaryTransitive` without it, and only the three named controls conclude
    `PreservesBody` without it;
  - no declaration name or header claims a source for the ellipsoid, the drive, dimension three, SC∞, ELEM or V4′.
- **L.** `OrbitGeneration` is the frozen blob, and its suffix digest is the design-validated one.

`controls.py` is blob `6a700bd7a554d152e4ccedd963942f263cf75668` (SHA-256
`9e9dd188c004a26a77d8e0451951bbf4d9925c296251c4227a2dc8359cc85034`, 788 lines).

- It was frozen before the outcome of design run 36961561241 was read.
- `controls.py --self-test` passes 30 checks. Its 14 mutation controls must each fail with their named code: the
  body byte and the header of `OrbitGeneration` (L); a removed declaration (N1); a strengthened statement, a changed
  binder context and a changed definition (N2); a `sorry` (N3); a transitivity-to-dimension theorem (S2); a sourcing
  conclusion and a sourcing name (S5); a stronger G-AUT premise (S3); the 4-ball control demoted to a definition
  (S1); a dropped import line; a changed census status.
- `controls.py check <commit> --freeze F` runs checks P, L, N1–N3, S1–S5, I, C and F.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`. The levels are
kept apart: the kernel build, the axiom report and the controls' text checks do not substitute for one another.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| L continuity | `OrbitGeneration` whole; principal `seedOrbit_ball3_eq`, `lorentz_of_available`, `orbit_generation_core` | blob `0673321f`; suffix SHA-256 `843c68c1…` equal to the module built green at `40025649`; built at `E` with every printed axiom set within `[propext, Classical.choice, Quot.sound]` | L |
| G-AUT word closure | `preservesBody_words`, `preservesBody_driveWords` | built at `E`; both printed axioms within the three standard axioms | S3, N2 |
| Normalization | `hypotheses_tr`, `isBoundaryState_tr`, `seedOrbit_eq_of_normalization`, `lorentz_of_normalization`, `affineSpan_preserved`, `isBoundaryState_restrict`, `chart_restrictEquiv`, `hypotheses_restrict` | built at `E`; printed axioms within the three standard axioms | S4, N2 |
| 3-ball transitivity | `boundaryTransitive_ball3Drive`, `seedOrbit_ball3Drive`, `euler_apply_pole`, `exists_euler_angles` | built at `E`; printed axioms within the three standard axioms | N2, S5 |
| 4-ball countercontrol | `boundaryTransitive_ball4`, `isBoundaryState_closedBall_iff`, `finrank_E4`, `preservesBody_isom4` | built at `E`; printed axioms within the three standard axioms (`preservesBody_isom4` through the print of `og1_infrastructure_core`, which carries it as a conjunct) | S1, S2 |
| B1 | `flow_zero_of_add` | built at `E`; printed axioms within the three standard axioms | N2 |
| B5 | `isEmpty_drivability_of_finite_orbits` | built at `E`; printed axioms within the three standard axioms | N2, S5 |
| B6 | none | excluded (§ In scope, item 5); no declaration | S2, S5 |
| verdict | `og1_infrastructure_core` | built at `E`; printed axioms within the three standard axioms | S2 |

## Design evidence

- **Run 36945912933** (`claude/l-orbitgen-design`, `40025649`): `OrbitGeneration` built green, with 64 theorems
  reporting only the three standard axioms. Its import suffix is the frozen suffix.
- **Run 36961561241** (`claude/og1-dev`, `052afbef`): the tree is `D` plus the two modules (`OrbitNormalization` at the
  reference blob `bf627dfe`), the import lines and the census family, without this record directory. The outcome was
  read after `controls.py` and the frozen surface were committed (`99c917ee`). `OrbitGeneration` built. `OrbitNormalization`
  failed with one error: the identifier `le_or_lt`, absent from this Mathlib, at line 646 in the proof of
  `exists_euler_angles`. Through it, `sorryAx` reached `exists_euler_angles`, `boundaryTransitive_ball3Drive`,
  `seedOrbit_ball3Drive` and `og1_infrastructure_core`. Every other printed axiom set was the three standard axioms.
- **Repair 1** replaces `le_or_lt` with `le_or_gt` in that proof, and nothing else. The repaired module is blob
  `ea397e69bbc8af512cbd1474b2fa0b83063d55fa`. The module checks of `controls.py` (L, N1–N3, S1–S5) pass on it, so the
  frozen statement surface is unchanged.
- **Run 36962242718** (`claude/og1-dev`, `a133b06d`, the repaired module): the Mathlib bridge job built both modules
  with every printed axiom set within `[propext, Classical.choice, Quot.sound]`, all twenty frozen prints of
  `OrbitNormalization` included. The release gate passed every step (`lean-axioms` 5439 named results, no `sorryAx`;
  `lean-manuscript` OK; 22 receipts hold).

Stage S1 lands `OrbitNormalization` as the repaired blob `ea397e69`.

These runs are design evidence, not attestations.

## Stages

1. **C1** adds `controls.py`, blob `6a700bd7`, to the record directory. Acceptance: the blob is the frozen blob.
2. **S1** adds both modules (`OrbitGeneration` blob `0673321f`, `OrbitNormalization` blob `ea397e69`), the two import
   lines and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green: the Mathlib bridge builds both modules, the axiom check passes with
     no `sorryAx`, and the release gate passes, `lean-manuscript` included.
3. **Repairs**, if the build at S1 fails, change proofs only. Each repair commit passes `controls.py check` at that
   commit. A failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance:
   - `controls.py check E --freeze F` passes;
   - the exact-head run at `E` has every job green.

## Outcomes

The label is decided mechanically at `E`.

- **`OG-1-INFRASTRUCTURE-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the exact-head run at
  `E` is green on every job. That includes:
  - the Mathlib bridge building `OrbitGeneration` and `OrbitNormalization`;
  - every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]`;
  - the release gate passing.

  The result note states the strongest permitted conclusion above and nothing stronger.
- **`OG-1-HALTED`** — anything else. The round halts under the specification's `S12`, and the result note names the
  failing check or job and the frozen statement that could not be proved as stated.

No outcome changes a manuscript, the roadmap, NB-1 or any hypothesis's status. No outcome says that OI implies the
one-system theorem.
