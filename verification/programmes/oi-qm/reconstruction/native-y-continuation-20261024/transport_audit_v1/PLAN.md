# Proof audit of native extrusion and chronological frontier masking

Scope fixed before new computation, 24 October 2026. Separate-author internal
audit within the #910 research effort; this is not an external proof review or
formal certification. Publication is on the existing #910 draft, whose starting
head is `71d291297d0a662cbb9377ab48eef7aa4b839e77`. #885 remains read-only.

## Sources and questions

The inherited general theorem is sections 3 and 5 of
`oi_native_transfer_v1/REPORT.md` in the retained combined handoff
`88f805670fe329c1dea9ca48604348a880d3758ea1c4fcf91d5f57eeaf304227`.
Its report SHA-256 is
`11f66eb63492b1b563b3f83c51929fa1d2104f91a88b6a6bbb0216bdde3bfcf0`.
The target is the stated one-sided boundary-source extrusion theorem,
not arbitrary transport of a dirty native measurement output. The compiler
application audit under `oi_followup_20261024/compiler_audit/` and the present
`checkpoint_v10/history_v9/`, `six_source_v5/period/`, and `herald_v10/`
are related proof dependencies or separately scoped extensions.

Audit the following statements separately:

1. The global second-order update is bijective, independently of whether H is.
2. One-sided source geometry gives the finite staggered-front recurrence.
3. That finite recurrence is a triangular permutation on all abstract fronts.
4. The exponent `12*840^R` follows for all R, and its radius-185 application
   really uses a depth at most 185. No arbitrary dirty strip inherits it.
5. A unique axial first arrival is a permutation in its initial triple in any
   fixed dirty background, retaining all six neighbors and the old-local term.
6. A chronological multi-port frontier map is bijective only with distinct
   independent unpinned bank coordinates and an acyclic same-time graph.
7. Finite cones and integer distances transfer to the specified torus only
   when no wrap-around alternative path lies in the time window.
8. The arbitrary finite wing-program source formula, including its terminal
   row, follows from first-front geometry and an invertible Pascal transform.

## Productivity test and bounded controls

Produce a complete re-derivation with explicit hypotheses, or a concrete
counterexample to a stated theorem. A restatement or replay alone does not
meet the test. Identify any misuse that would infer transport of the actual
post-Y dirty boundary from a theorem requiring a clean rear shell.

Use a new standard-library checker importing no author engine. Bounded native
backward-cone evaluation checks (a) complete eight-value first-arrival maps in
fixed dense backgrounds; (b) staggered-front recurrence at small radii; and
(c) source-wing words at small deadlines. Algebraic tests check H, inverses,
small complete front permutation and exponent induction. Controls remove a
geometric premise, duplicate a frontier resource, add a shortest competing
path, or omit the terminal wing row, and must detect the resulting defect.

Run one normal and one optimized replay with explicit exceptions active in
both modes. All verdicts read structured measured values. Mathematical
all-radius conclusions rest on the written proofs, never bounded extrapolation.
Do not launch heavy enumerations, full torus campaigns, Lean, release gates,
special workflows, merges or designations. Root alone publishes checkpoints.

## Deliverables and status boundary

`REPORT.md`, `checks.py`, `result.json`, `PROVENANCE.json`, and `SHA256SUMS`
will separate ACCEPT/REVISE findings by statement. Accepted local transport
lemmas do not establish calibration selection, native readiness, a clock,
observer-access closure, reusable instruments, composites or full equivalence.
Coordinator-independent or external review remains a separate review level.
