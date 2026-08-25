# Verification suite

Machine-checked certificates for the finite and algebraic core of the OI papers, in two
layers: **Lean 4 proof files** (self-contained, zero dependencies — no Mathlib, no lake
project) and **numerical probes** (Python 3) that instantiate every hypothesis and
conclusion on the concrete lattice operators, exactly in integer arithmetic where the
statements are integer identities.

Contents (`lean/`):

- `OI_Gauge_Certificates.lean` — telescoping/plaquette triviality for arbitrary abelian
  alphabets; central-sign collapse for every odd q; the kernel-checked cubic counting
  layer (24 / 72 / 288 / 144) behind the local-gauge closure argument of `papers/SM.md`.
- `OI_Structural_Core.lean` — Theorem 1a of `papers/SM.md` at operator level (exact
  projected evolution and kernel equivariance), the Susskind factorization's cancellation
  mechanism, Theorem 3's chirality algebra, and the quadratic boost-Ward identity.
- `OI_Staggered_Relations.lean` — the staggered generator relations (phase involutions,
  commuting shifts, and the axis-order sign pattern) imply pairwise anticommutation and
  the squares, and hence the factorization for **any number of axes** — by structural
  induction over a list of pairwise-anticommuting summands, with the three- and four-axis
  statements as corollaries. Axes are indexed by natural numbers, so one structure serves
  every dimension.
- `gauge_certificates_probe.py`, `structural_core_probe.py`, `staggered_relations_probe.py`
  — companion checks for the three proof files, including exact certification that the
  concrete lattice operators satisfy every hypothesis the Lean proofs use.
- `structural_chain_probe.py`, `representation_bridge_probe.py` — numerical verification
  of the planned formalizations (see `lean/ROADMAP.md`): Theorems 1a/2/3 and the GR
  detailed-balance lemma; the representation-theoretic bridge (character table, isotypic
  decompositions, invariant dimensions).
- `VERIFYING.md` — how to run everything; `ROADMAP.md` — planned extensions.
