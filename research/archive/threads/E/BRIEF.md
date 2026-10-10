# Thread E — K2 formalization prep (decomposition only; do not freeze or claim results)

Read first: threads/PROTOCOL.md; k2/K2.0-NOTE.md and its scripts (k20_*.py, k22a_*.py, k23_cocycle.py); NB-1
preregistration (layering model: kernel / exact / written).
Produce a prospective theorem decomposition of the d = 3 composition result: exact propositions (relations force
A diagonal, K antidiagonal; positivity ⇔ σ_max(W(s)) ≤ 1; 32 admissible gates; closure positivity keeps 8
SO-classes; survivors' Lie closure is 15-dim su(4)-image or its PT_B conjugate; failures give so(15) with no cone
between min and max; Q vs PT(Q) orientation is a local gauge on three copies), each with: its layer (Lean / exact /
written), its controls and countercontrols, a dependency graph, and the cheapest exact replay. Re-run the existing
scripts read-only to confirm each figure reproduces; flag any figure that does not, and any step that is currently
numerical rather than exact. Also state the relation to K3 machinery (typed_determined_iff, the antiunitary/CP
bridge) as open obligations. Deliver threads/E/RESULT.md per the merge rule.
