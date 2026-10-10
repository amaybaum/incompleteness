# RECORD — proposed Level 3 (NOT run; awaiting owner direction). Prediction written before any computation.

Provenance: motivated by the Level-2 linear result (state space = diamond on the "cross", see RESULT.md), so it
is not a blind extension. It is proposed for all three rules alike, with no per-rule change, and with its
predictions stated here in advance.

## Extension

Add one reversible local action on the visible pair to the Level-2 alphabet, for preparations, effects and the
non-selective generators alike: `c` = CNOT (u_0, v_0) ↦ (u_0 ⊕ v_0, v_0). With `s` and `f` it generates the full
affine group AGL(2, 2) ≅ S_4 on the four pair states (Level 2 generates only the order-8 subgroup). Interface class,
seed, criteria and stages as FREEZE, with L_p = L_e = 3 at Stage A.

## Predictions (decision rule fixed now; numbers are predictions, not criteria)

- **Linear, G:** passes as at Level 2.
- **Linear, R4:** the parity-known states (u_0 ⊕ v_0 determined, both bits fair) become preparable, so the
  pair-marginal state set becomes the octahedron spanned by the three fiducial questions u_0, v_0, u_0 ⊕ v_0
  (Spekkens' toy bit / the six qubit stabilizer states), table rank 4 and C of dimension 4 for some invasive κ —
  *if* no further lattice correlation becomes visible. The falsifier is a certified rank > 4 (the CNOT exposes
  neighbour correlations through the next leap), or a rank-4 space not invariant under the generators.
- **Nonlinear and majority, R4-sector:** fail by orbit growth, as at Levels 1–2.
- **If the linear prediction holds,** the layered reading is: G — all three rules; R4 — linear only, via a
  knowledge-balanced (one fresh bit per pair) polytope, octahedral; Q — not yet tested, and a Q-layer premise
  (strict convexity or continuous reversible transitivity) is exactly what separates the octahedron from the
  Bloch ball. The linear rule would then be a stabilizer-type (Spekkens) elementary system, not a qubit.
