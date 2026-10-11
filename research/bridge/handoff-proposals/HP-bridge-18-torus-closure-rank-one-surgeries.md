# HP-bridge-18 — the tower's closure `G`: no self-dual rank-one surgery with H1

From `research/bridge`, node B21 (round 5). Proposed for the countermodels thread (C23, the same group) and the
equivalence thread (E19's countercontrol family). The coordinator routes.

## Statements and labels

Every statement is an invariance statement.

1. **The group** (B21-1). B10-4's `G = closure ⟨cnot, actT nflip, actT R_z(t) for all t⟩` is, on the matrix side,
   `T² · {1, CNOT, X_B, CNOT X_B}` modulo scalars (`T² = {diag(e^{iu}, e^{−iu}, e^{iv}, e^{−iv})}`), component group
   `ℤ/2 × ℤ/2`, eigenline group `⟨(12), (34)⟩` (case B's `Π`). Products: a `G`-orbit is product-free iff
   `|h₀₀h₁₁| ≠ |h₀₁h₁₀|` and `|h₀₀h₁₀| ≠ |h₀₁h₁₁|`; every product-free orbit is infinite. Orthogonal pairs:
   `⟨h | U(u, v) X_B h⟩ = 2 Re(h̄₀₀h₀₁e^{iu}) + 2 Re(h̄₁₀h₁₁e^{iv})`, so every orbit has one. No `G`-orbit is maximally
   entangled throughout. Label: CONJECTURE ([X] + [W]).
2. **No self-dual rank-one surgery** (B21-2). For a `G`-invariant set `Z` of rank-one defects with every `c ∈ (1, 2]`,
   finitely many orbits or `Z` compact, and H1, the surgery `K(Z)` is not self-dual (self-duality with H1 would make every
   defect block-positive, excluding `c = 2`; the largest `c < 2` is attained on an orbit with an orthogonal pair; Lemma
   C18-1). Label: CONDITIONAL (on Lemma C18-1, HO-31 item 3(a), at its label).
3. **What remains for an explicit cone.** Defects of rank two or more (the balanced engine; not examined for `G`), an
   unattained supremum of `c`, or a construction other than surgery. Existence of an exotic `G`-invariant cone stays at
   claim (D) [A].

## Evidence

| item | pointer |
|---|---|
| scripts | `experiments/b21_torus.py` T1–T5 (run 3; runs 1, 2 kept), `experiments/b21_ceq2.py` Q1–Q5 (run 2; run 1 kept; Q5 an exhaustive Gaussian-integer control with a CNOT-free countercontrol), replays byte-identical |
| notes, results | `NOTES-B21.md`; `RESULTS.md` rows B21-1, B21-2 |

## What the recipient may assume

Items 1–3 at their labels.

## What the recipient may not assume

- a kernel check, or an exotic `G`-invariant cone;
- anything about rank-two or non-surgery constructions;
- that `G` is (or is not) conjugate to a subgroup of `G_B`.
