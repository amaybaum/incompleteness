# Thread A — successor foundations design (design only; becomes the next governed round only by owner decision)

Read first: threads/PROTOCOL.md; k-infinity/K-INF-DESIGN.md (§7–§17); the halted KINF-1 result note
(wt-threads/verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/result.md) and preregistration;
the design module wt-kinf1/verification/lean-mathlib/OIBridge/KInfFoundations.lean (reference only, never authoritative).

Tasks:
1. Corrected vocabulary. Define *proper* effect on Ω (∃ y ∈ Ω, e y < 1). Restate SEC (every frontier point certain
   for some proper available effect) and SF (every proper available effect has a subsingleton certain face). Check by
   hand that the unit may remain available, that Lemma C's proof goes through, and that KInf1 is no longer vacuous
   under avail = fullEffects. Look for any OTHER degenerate effect that trivializes the definitions (e.g. effects
   constant on Ω but not 1, effects certain only off Ω, empty Ω, singleton Ω, Ω not full-dimensional in V).
2. Route neutrality. Draft the geometric premise so the round can carry either corrected SF or a self-duality /
   homogeneity premise without committing to one (coordinate with Thread D's findings via dependencies only).
3. Controls, each stated as an exact computation the probe would run: square gbit (flat faces, capacity 2),
   torus orbitope, Stiefel orbitope, Bloch ball / 3-ball (SF holds with full effects), SIC ball on 4 ontic states.
   For each: which corrected predicate holds or fails, and why that is the intended verdict.
4. A one-page preregistration skeleton: declarations to freeze (names + exact Lean statements as candidates),
   theorems, probe sections, what is explicitly NOT claimed.
Deliver threads/A/RESULT.md per the merge rule.
