# Design run of the drafted orbit-generation module (design evidence only)

Branch claude/l-orbitgen-design from 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a; commit
40025649be77cd4d510a865137d6e8c2788f8fda adds verification/lean-mathlib/OIBridge/OrbitGeneration.lean
(blob e9722042c2fc076ef292cbdb6d800a591ff71eb4, identical to threads/L/OrbitGeneration.lean) and one import line in
OIBridge.lean. Run 36945912933 (workflow_dispatch). No census, ROADMAP, freeze or round material.

## Interpretation rule (owner, 2026-10-02)
- Green Mathlib bridge + acceptable `#print axioms` output (standard axioms only, no sorryAx) = L's conditional theorem
  is Lean-valid at 40025649.
- `lean-manuscript` census failure = expected and irrelevant (no census disposition by rule).
- A42 shard outcomes = irrelevant to L and do not affect the conclusion.
- Repairs: elaboration/tactic only. Any theorem-statement or hypothesis change breaks continuity with L's result; the
  repaired version is then a new design theorem, reviewed separately.
- If Thread M changes the interface (ball3 normalization, dimension 3, G-AUT), a green run here remains evidence for
  this conditional theorem only.

## Result (run 36945912933, Mathlib bridge job 110647885791)
- Build: `Built OIBridge.OrbitGeneration (8.8s)`; `Build completed successfully (3615 jobs)`. One linter warning
  (OrbitGeneration.lean:631, unnecessary `<;>`), no errors.
- `#print axioms`: 64 lines (OrbitGeneration.lean:755–818), every one `[propext, Classical.choice, Quot.sound]`; includes
  seedOrbit_ball3_eq, kInf1_ball3_of_orbit, lorentz_of_seedOrbit, lorentz_of_available, orbit_generation_core, and the
  countermodel theorems (not_boundaryTransitive_flow, not_seedOrbit_unsharp_eq, not_isEffectOn_ballEffect_cubeCorner).
- Release gate: lean-axioms PASS (5419 named results = 5355 at D + 64, no sorry); lean-manuscript FAIL (1 problem:
  the new module has no census disposition — expected, excluded by rule); every other step PASS.
- Verdict under the interpretation rule: L's conditional theorem is Lean-valid at 40025649. No repair was made.
- Remaining jobs of the run (A42 shards etc.) cancelled after the bridge result; irrelevant by rule.
