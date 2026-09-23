# C4 causal-readback audit — amendment 1

This is an **append-only clarification** to `verification/audits/physical-realization/c4-causal-readback/preregistration.md`. That file is
unchanged and remains the frozen record of its round. Nothing here revises a result of that audit;
the clarification is forced by a later theorem, and it is recorded separately rather than edited in.

Occasion: frozen control 13 of `verification/programmes/oi-qm/track-i/arc-b-rooted-classification/preregistration.md` (authoritative blob
`1dd761349a9f319fc7e507814b7acdbb85c3eb78`) requires the standing description of the two controls to
be reconciled once periodicity necessity is proved. That necessity is now certified, so the control
has fired.

## What the later theorem establishes

The Arc B classification proves that a complete rooted family over a finite visible carrier is
realizable at the inherited `RootedRealization` interface if and only if it has the identity at the
root time, is row-stochastic at every time, and has a positive finite visible period
(`finiteRootedRealizable_iff_pper`).

Three statements follow, and they are kept apart deliberately. Collapsing them is the misreading this
amendment exists to prevent.

1. **The abstract complete `pdFamily` is nonperiodic**, hence not a member of the inherited class.
   It is the identity at `t = 0` and fully mixing at every later time, so no shift fixes it. Kernel:
   `pdFamily_not_periodicFamily`, `pdFamily_not_finiteRootedRealizable`.

2. **The abstract complete `peFamily` is nonperiodic**, hence not a member either. It mixes only at
   `t = 2` and is the identity everywhere else, so no shift fixes it. Kernel:
   `peFamily_not_periodicFamily`, `peFamily_not_finiteRootedRealizable`.

3. **`build(K)` realizes only the requested finite horizon, and its realization depends on `K`.**
   The construction in `papers/oi_lattice_code/foundations/review4_probes.py` carries a length-`K`
   saturating ledger and exhibits the displayed behaviour through that horizon. What it establishes
   is

   `∀K ∃R_K ∀t ≤ K : rootedMap R_K t = Γ t`,

   which does **not** give

   `∃R ∀t : rootedMap R t = Γ t`.

   The quantifier swap is invalid in general, and statements 1 and 2 show it fails for these two
   families in particular.

## How this reads against the frozen text

The audit's §T6 discussion says the controls' realizations on the frozen visible/hidden layer are the
probe's, that `build` returns a `phi` asserted to be a total permutation with a uniform prior over
padded hidden states, and that `kstep` computes exactly the rooted maps. It also states plainly that
the two controls are **not** instantiated as `rootedMap` of an explicit realization in Lean, and that
the note does not claim they are.

That disclaimer is correct and is preserved.

**For all-time `RootedRealization` semantics, the frozen wording is superseded by this amendment.**
It was defensible in its own local context, where the controls are objects on bounded horizons and no
all-time semantic class had been formalized. Once that class exists, "the controls' realizations on
the frozen visible/hidden layer" acquires a reading it cannot bear: that one fixed finite carrier,
one reversible update and one common prior reproduce `pdFamily` or `peFamily` at every time. No such
realization is exhibited by `build(K)`, and by statements 1 and 2 none exists. What `build(K)`
supplies is a realization for the chosen horizon, and a different one for each horizon.

So the correction is not that the note omitted a qualifier. It is that a sentence which was true of
horizon objects becomes false if read as a claim about the complete families, and the later theorem
is what makes the difference decidable.

Nothing in the C4 audit's own results depends on the distinction. Its controls separate history-level
memory from marginal revival on bounded horizons, which is what they were built to do, and the
theorems there — `pdFamily_pDivisible`, `pdFamily_not_c4e_not_c4r`, `peFamily_c4e`,
`peFamily_pIndivisible`, `control_separation` — are statements about the abstract families and are
untouched by this amendment.

## Scope

Verification-facing surfaces only. `verification/README.md` carries the corrected wording in place, as
a mutable surface. Manuscripts, books, bibliography and publication claims are outside the frozen
authorization of the Arc B round and are not edited.
