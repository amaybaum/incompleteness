# Reconstruction round OG-1 — conditional orbit-generation infrastructure: PREREGISTRATION

**Status: drafting.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted on its
pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
Sections marked *to be frozen* are completed before `F` from the design runs recorded below.

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
5. **F's parked lemmas, premise-free only**: B1 (`flow_zero` follows from `flow_add`) and B5 (a body whose automorphism
   orbits are finite is not drivable). B6 (no body of affine dimension ≤ 2 is drivable) is excluded: its proof needs
   compact-group machinery beyond this round's interface.
6. The census family entry for the new modules, `kernel-only`, carried by no manuscript.

### Frozen out

SC∞ (stage consistency) and the completion body; ELEM (the binary-visible scope premise); any source of the drive;
dimension-3 sourcing; V4′ adoption; the ellipsoid theorem (a drive on a three-dimensional body forces an ellipsoid);
K2 and the composite; TR, CAR and SCL; B6; NB-1 and any change to it; any manuscript or roadmap edit.

## The declarations, the controls, the stages and the outcomes

*To be frozen* from the design runs: the module texts (by blob and by declaration list with frozen statements), the
`controls.py` blob and its checks, the execution stages and their acceptance, and the outcome labels with their
mechanical rule.
