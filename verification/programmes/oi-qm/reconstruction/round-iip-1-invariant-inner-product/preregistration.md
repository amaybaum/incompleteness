# Reconstruction round IIP-1 — the invariant inner product of a convex body's affine automorphisms: PREREGISTRATION

**Status: drafting.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted on its
pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
Sections marked *to be frozen* are completed before `F` from the design runs recorded below.

```v3-round
round IIP-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-iip-1-invariant-inner-product/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-iip-1-invariant-inner-product/
record AM verification/receipts/IIP-1.json
execution A verification/lean-mathlib/OIBridge/InvariantInnerProduct.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/IIP-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, and no other round's record
change under any outcome.**

## The objects

- **`D`** = `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`, the head of `main` after `OG-1` landed (push run
  36973928206, every job green; the act 42 exclusion matrix skipped on push). The owner designated it as the common
  base of this wave.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them. A sibling round of this wave
  (`CMP-1`) is drafted from the same `D`; whichever lands second reconciles against the `main` the first produced.

## What the round is

A small, premise-free, reusable lemma: a common fixed point and a positive-definite invariant inner product for the
affine automorphisms of a compact convex body, stated on the translation space of the body's affine span.

The construction needs no compactness of any group and no Haar measure. For a compact body `Ω` with nonempty
interior in coordinates `Fin n → ℝ`, with Lebesgue measure:

- the change of variables along an affine automorphism `g` with `g '' Ω = Ω` forces `|det g| = 1`, so integrals
  over `Ω` are invariant under `g`;
- hence `g` fixes the centroid `c` of `Ω`;
- hence the second-moment matrix `S = ∫_Ω (x − c)(x − c)ᵀ` satisfies `A S Aᵀ = S` for the linear part `A` of `g`;
- `S` is symmetric and positive definite because `Ω` has interior, so `⟨u, v⟩ = uᵀ S⁻¹ v` is a positive-definite
  inner product preserved by every such `A`.

Through `OrbitNormalization`'s affine chart `w ↦ L w + p0` of the affine span (`chart`, `bodyR`), the restricted body
of a compact convex body has nonempty interior, and the restriction of every affine automorphism of the body fixes
the restricted centroid and preserves the restricted inner product.

### In scope

1. `InvariantInnerProduct`, a new module: the change of variables along an affine automorphism preserving `Ω`; the
   centroid and its fixedness; the second-moment form, its symmetry, positivity and transpose-invariance; the inverse
   matrix as the invariant inner product; the restriction to the translation space of the affine span; and a control
   showing that interior is needed (the second moment of a point vanishes).
2. The census family entry for the module, `kernel-only`, carried by no manuscript, inserted directly after the
   landed `OG-1` family ("conditional orbit-generation infrastructure …").
3. The import line `import OIBridge.InvariantInnerProduct`, inserted directly after the landed line
   `import OIBridge.OrbitNormalization`.

### Frozen out

Any ellipsoid statement; any orthogonality of a drive's flow or `J`; any closure, density or finite-word statement
about rotation groups; boundary transitivity and K∞-R; any dimension statement; the drive and its source; V4′; SC∞
and the completion; any manuscript or roadmap edit. The round claims no compactness of the automorphism group and
uses none.

## The declarations, the controls, the stages and the outcomes

*To be frozen* from the design runs: the module text (its declaration list with frozen statements and definitions),
the `controls.py` blob and its checks, the execution stages and their acceptance, and the outcome labels with their
mechanical rule.
