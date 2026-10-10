# Thread L — P2 formalization (reduced orbit-generation theorem)
Task: take P1, K∞-R and V4′ as ABSTRACT, named hypotheses (black boxes; do not try to prove them) and draft a Lean 4 /
Mathlib module, in the vocabulary of verification/lean-mathlib/OIBridge/KInfFoundations.lean, proving the reduced
orbit-generation theorem:
  sharp seed (P1) + seed-orbit availability (V4′) + boundary transitivity (K∞-R)
    ⟹ {r ∘ g⁻¹ : g ∈ G} = {(1 + b·x)/2 : b ∈ S²}  on ball3,
and that the RHS is exactly what `lorentz_of_effects` (NativeGateBall.lean:105) consumes (check its hypotheses' exact
shape: indexing, normalization, Fin p, the vector form). Also: SEC for that family (via `ballEffect`, KF ~1030;
`supportingEffectComplete_ball3` KF:1053 as reference) and the general-body version with a COVER hypothesis.
State each hypothesis as an explicit structure or Prop argument — no axioms, no sorry in the claimed theorems.
Because Lean cannot run here, deliver: (1) the draft .lean text (written to threads/L/, not into the repo); (2) a
line-by-line proof plan naming every Mathlib/landed lemma used, checked to exist at 6d0abf6b (grep the tree;
Mathlib names verified against verification/lean-mathlib's pinned Mathlib if present locally, else flagged UNVERIFIED);
(3) exact-arithmetic checks of every concrete identity (e.g. ballEffect b ∘ R = ballEffect (R⁻¹ b) for rotations,
normalization (1 + b·x)/2 at ±b); (4) the list of omitted premises found while formalizing — the main value: if the
three hypotheses do NOT suffice, name what is missing with a countermodel.
Outcome: SUFFICIENT (draft + plan, kernel check pending a CI design run) / INSUFFICIENT (missing premise, countermodel).
