# Recurrence and record-fibre recovery

This ordinary research branch starts at `20ca05fe9e7e460de29e08f7a21029042fa45b12`.
PR #982 remains held independently. Source corrections in SC-35 #973 already
propagate the kernel overlap/identity-return theorem; this branch does not
repeat or merge that source correction.

## First proof candidate: P24.5(i) core

`OIBridge/RecordFibreIdentification.lean` defines an actual passive record from
powers of the known permutation and a preparation-supported fibre. On a
nonempty fibre a quantity is determined iff it is constant. Initial/current
state determination is equivalent to a singleton fibre. For a product carrier,
visible projection and word of length n+1, current-hidden determination has the
same criterion. The proof uses the recorded last visible coordinate and
permutation injectivity. A two-record swap and an empty-word counterexample
protect the inference and nonempty-record boundaries.

This is a candidate until ordinary PR CI compiles it and independent review
accepts the exact declarations. The whole manuscript P24.5 remains GAP. The
Bayesian positive-support bridge, finite N−1 partition-refinement bound and
physical storage/intervention mechanisms are not asserted as formalized here.
No manuscript, coverage ledger or publication artifact is changed.

## Remaining recurrence obligations

`RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap` already
proves the final overlap/return composition. The full Main history-readback
statement still needs the common-endpoint history to non-permutation bridge,
periodicity and identity return on the actual rooted law, and their composition.
These require exact hypotheses and must retain the distinction between a whole
recurrence-cycle verdict and an accessible short-time witness.

Local work uses bounded source/static checks only under AGENTS A.40. Full
Mathlib compilation and release/probe suites run in normal draft PR CI. No native
round, F/E designation, special dispatch or merge is authorized by this branch.

## Actual rooted-return bridge candidate

`RootedRecurrenceBridge.lean` proves from the actual iterate-return hypothesis
that the existing rooted map is the identity, using the realization's common
normalized hidden prior. It composes this with the existing overlap/identity-return
kernel theorem. Uniformity and full support are not needed for this implication.
This is a separate partial bridge, not the full history-readback theorem: the
history/common-endpoint implication and finite-order existence still have their
own obligations. No short-window P-indivisibility statement is introduced.

The first P24.5-core checkpoint, `4f962b61aca490cec326542be0cbaee201c82796`,
compiled successfully in ordinary PR CI run 40724655067: the Mathlib Build and
Release gate steps succeeded. Independent mathematical/declaration acceptance
remains separate. A later bridge candidate needs its own compilation verdict.
