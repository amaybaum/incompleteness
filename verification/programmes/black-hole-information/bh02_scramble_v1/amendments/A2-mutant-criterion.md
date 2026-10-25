# Amendment A2 — mutant criterion (before any code was run)

Made before `checks.py` existed or any program was run. PLAN §3 says a mutant counts as caught
only if its targeted control fails *and every other control passes*. Several controls share a
component (the eigensolver feeds K-eig, K-page-mc and the Haar attainability control CT1; the
permutation sampler feeds K-bij and the `|+^n⟩` invariance control K-plus; the exact rank feeds
K-rank and K-tight). A fault in a shared component correctly trips every control that depends
on it, so the second clause cannot hold for those mutants without weakening a control.

Replacement criterion: a mutant is caught iff the run fails cleanly (prints VOID, exits 2) and
its targeted control is among the failed controls. `mutants.py` prints, for every mutant, the
full list of failed controls, so collateral failures are visible rather than hidden.
