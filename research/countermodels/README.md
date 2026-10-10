# research/countermodels — the analysis of the exotic composite cones

**Question.** What is the space of composite cones that satisfy every premise at L (closed, self-dual,
`cnot`-invariant cones on `W 3` with single-token slices the ball — H1, H2, H3), what structure do the exotic ones
share, and which additional principle — if any — excludes all of them without restating (b)? Stages 3–6
(archived) established: exotic cones exist at levels (i) K(E0) and (ii) K(Z_F) (explicit), and as existence
results from exact cap seeds for every node of the stage-4 lattice; UNIQUE holds iff the compact group generated
by the node's operations carries the products to every pure state; (b) with H1–H3 for {flow, J} forces Q3; a
single off-frame order-3 rotation forces Q3; every one-parameter local rotation moves K(Z_F) out (flow law
`−sin(t)/8`). Open: the classification of all such cones (stage-4 obligation M1 names this gap), whether
extreme-ray transitivity T excludes every exotic cone (UNDECIDED for the existence-only alternatives), an
explicit κ-invariant cone, the torus explicit cone (the surgery cone K_T refuted), and the row-by-row reassessment
of the stage-3 cones `K({F, cnot F})` and `K(e_c)` (not covered by stage 6's R6).

**Starting checkpoint.** Branch `research/countermodels` from commit `4dc0321c` (= L `9f9f8257` +
`research/archive/`). Read first: `research/archive/pt/INTEGRATION-NOTE-STAGE4.md`, `…/pt/INTEGRATION-NOTE-STAGE6.md`
§2–§3, `…/pt/R6/REASSESSMENT.md` (§1 definitions, §3 tables, §7), `…/pt/T6/TEST.md` §3 (the self-duality proof,
the flow law), `…/pt/audit/X/AUDIT-X.md` and `…/pt/X/RESULT.md` (the stage-3 constructions SD1/SD2, EBF, the K2-guard
cones), `…/pt/Y/RESULT.md`, `…/pt/Z/RESULT.md` (the dichotomy, the seeds, T as EXCLUDES-KNOWN), `…/pt/C5/RESULT.md`
(the census of native subsets and the orbit counts 48/192/768). Kernel at L: `verification/lean-mathlib/OIBridge/
CompositeDimension.lean`, `K2Guard.lean`.

**Research plan (depth-first).**

- **C1 — the two unreassessed cones.** Reassess `K({F, cnot F})` and `K(e_c)` row by row against the 199
  applicable items (R6's Table A2 as the template, `research/archive/pt/audit/stage6-inputs/T-audit/r6_rows.tsv` as
  the reference rows) with exact scripts; confirm or refute the covering argument of AUDIT-R §4.
- **C2 — structure of K(Z_F).** Its full symmetry group inside the local-unitary-and-swap group (order 64 known
  at level (ii)); its extreme rays and their orbits (48 / 192 / 768 at the known levels); its facial structure;
  whether it is the unique exotic cone with its symmetry group. Exact computation, written proofs.
- **C3 — extreme-ray transitivity T.** Decide whether T (the pair's reversible operations act transitively on
  the extreme rays) excludes every exotic cone, not only the known ones. Route: show every exotic cone has an
  extreme-ray invariant (the known cones have `c = 15` on defects and `9` on products) that a transitive group
  cannot have, or construct an exotic cone with a transitive group. If T excludes all: run the disguise test
  (does T restate (b)? what sources T?) and state it as a candidate principle for a governed round.
- **C4 — the classification.** Classify the closed self-dual `cnot`-invariant cones with H1 at level (ii)
  (invariant under G16 and SWAP), or a well-defined subfamily (defect cones `(Q3 ∩ Z*) + cone Z` for finite
  defect sets Z): parametrize, find the invariants, and locate Q3 and K(Z_F) in the family. Every step exact.
- **C5 — explicit κ and torus cones.** Construct an explicit κ-invariant exotic cone (existence known by EBF
  over the Bell seed on the invariant circles) or prove no defect-surgery cone is κ-invariant; the same for the
  torus node (K_T refuted; what survives).
- **C6 — realization-facing structure.** Record every property of K(Z_F) that a hidden-level realization would
  have to reproduce (extreme rays, symmetry, the failure of every local flow), as input for `research/bridge`'s
  realization question (handoff proposal).

**Rules.** Exact arithmetic only (`fractions` / `sympy`); `python3 -I -B`; `.out` / `.err` with the exit marker;
decision rules in headers before the first run; failed runs kept; byte-identical replays; every claim in
`RESULTS.md` labelled CERTIFIED / CONDITIONAL (named item) / CONJECTURE / FAILED / OPEN. Q3 and `pauliW` are
comparison and construction tools, never premises. A favourable exclusion (a principle that kills every exotic
cone) is pressure-tested hardest.

**Governance.** Write only under `research/countermodels/` on this branch; never touch `main`, `papers/`, `book/`,
`verification/` or any certification record. Lean work on disposable `dev/countermodels/<topic>` branches
(modules under `verification/lean-mathlib/OIBridge/` there, CI via `workflow_dispatch`), incorporated here as [D]
design modules under `research/countermodels/lean/` with commit and run id. Push only to
`origin research/countermodels`. `LOG.md` records every commit's purpose.

**Coordination.** Handoff proposals in `research/countermodels/handoff-proposals/`; received handoffs in
`inbox/`, acknowledged in `LOG.md` before use. Other threads' branches are not read.
