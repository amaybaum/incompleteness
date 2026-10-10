# HP-5 — HO-4's composition-clause proposal tested: the excluding clause is family membership; Stab_loc(K(Z_F)) = V4

From `research/bridge`, node B8 (round 2). The answer to HO-4's request, proposed for the countermodels thread and the
coordinator's manuscript-obligation list (recorded, not applied). The coordinator routes.

**Finding HP-5a.** Clause (4) of the realization theorem (Main.md:552, "`𝓘_a ⊗ 𝓘_b` on the joint branch register") is
the composite action for the instruments it is given.
- For a unitary local instrument, through the dictionary, it is exactly `actC B(U)` / `actT B(U)` on the pair table
  [X b8 X1; dictionary a comparison tool].
- The theorem's input is a fixed quantum experiment with a finite family `𝓕`. So no clause of the theorem makes
  continuous (or any further) local operations joint instruments. K(Z_F) lies outside its range by the hypothesis
  "quantum experiment", not by clause (4).
- B4's realization of K(Z_F) satisfies clause (4) for its own local family.

**Finding HP-5b.** The excluding clause is family membership: "an operation available to a token in isolation is a
joint instrument".
- Its matrix form is `InertSpectatorCompositionality` ⟺ `HasParallelReferenceExtension`. The kernel proves it is not
  implied by the sealed C1–C4 core with exact system QM and full composite unitary control: CERTIFIED [K at L,
  OIRealization.lean:360 `finiteOI_not_implies_inert`].
- With clause (4) it is (b). Disguise test: FAILS.

**Finding HP-5c (exact; for all of `SO(3)` CONDITIONAL on KZ7 [A]).** The single-token rotations preserving K(Z_F) are
exactly `V4 = {I, R_x(π), R_y(π), R_z(π)}` on each token.
- Among the 24 Cliffords: exactly the four Paulis, with 40 certified exclusions [X b8 X2].
- Over all of `SO(3)`: KZ7 plus a group argument [W]. The flow laws for the two A_miss axes are re-derived: `−s`, `+s`
  [X b8 X3].
- So one single-token rotation outside `V4`, discrete or continuous, already excludes K(Z_F). Continuity is needed only
  to force `Q3`; the native discrete Clifford family leaves exotic cones.

Evidence: `NOTES-B8.md`; `experiments/b8_composition.py` (4/4, replay identical); RESULTS rows B8-1 … B8-4.
