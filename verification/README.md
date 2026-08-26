# Verification suite

Machine-checked certificates for the finite and algebraic core of the OI papers, in two
layers: **Lean 4 proof files** (self-contained, zero dependencies — no Mathlib, no lake
project) and **numerical probes** (Python 3) that instantiate every hypothesis and
conclusion on the concrete lattice operators, exactly in integer arithmetic where the
statements are integer identities.

One statement in the roadmap contains the word *dimension* and so cannot be finite arithmetic
at all. It lives apart, in `lean-mathlib/`, which is the **only** part of this suite that
depends on Mathlib — its own lake project, its own pinned toolchain, and its own CI job, so
that a breakage there can never be mistaken for a verdict on the zero-import files. The two
kernel verdicts are always reported separately.

Contents (`lean/`):

- `OI_Gauge_Certificates.lean` — telescoping/plaquette triviality for arbitrary abelian
  alphabets; central-sign collapse for every odd q; the kernel-checked cubic counting
  layer (24 / 72 / 288 / 144) behind the local-gauge closure argument of `papers/SM.md`;
  and the character layer above it — the five irreducible characters of O given as
  functions on the group elements rather than as a trusted class table, their
  orthonormality, and the multiplicities of V₆, End(V₆) and the broken restriction.
- `OI_Regulator_Symmetry.lean` — the regulator-symmetry certificates: the character sums
  of the induced action on quadratic forms, over the 384-element hypercubic group and the
  96-element native group, for both the metric sector Sym²(ℝ⁴) and the field-strength
  sector Sym²(Λ²ℝ⁴), together with the invariance of the named basis forms and the
  countercontrol showing the electric form is not hypercubic-invariant.
- `OI_Structural_Core.lean` — Theorem 1a of `papers/SM.md` at operator level (exact
  projected evolution and kernel equivariance), the Susskind factorization's cancellation
  mechanism, Theorem 3's chirality algebra, and the quadratic boost-Ward identity.
- `OI_Staggered_Relations.lean` — the staggered generator relations (phase involutions,
  commuting shifts, and the axis-order sign pattern) imply pairwise anticommutation and
  the squares, and hence the factorization for **any number of axes** — by structural
  induction over a list of pairwise-anticommuting summands, with the three- and four-axis
  statements as corollaries. Axes are indexed by natural numbers, so one structure serves
  every dimension.
- `OI_Structural_Chain.lean` — the detailed-balance lemma stated without the exponential
  (edgewise balance plus connectivity forces proportionality, in a commutative monoid, with
  no division and no spectral argument), and the cubic quadratic invariant: the character of
  the induced action on Sym²(ℝ³) sums to 48 over the signed permutation group and 24 over its
  rotations, with δ exhibited invariant and a direction-singling form shown not to be.
- `gauge_certificates_probe.py`, `structural_core_probe.py`, `staggered_relations_probe.py`
  — companion checks for the proof files, including exact certification that the concrete
  lattice operators satisfy every hypothesis the Lean proofs use. Every integer the Lean
  files submit to `decide` is recomputed here by an independent construction.
- `structural_chain_probe.py`, `representation_bridge_probe.py` — numerical verification
  of the planned formalizations (see `lean/ROADMAP.md`): Theorems 1a/2/3 and the GR
  detailed-balance lemma; the representation-theoretic bridge (character table, isotypic
  decompositions, invariant dimensions).
- `VERIFYING.md` — how to run everything; `ROADMAP.md` — planned extensions.

Contents (`lean-mathlib/`):

- `OIBridge.lean` — the two classical identities the counting layer consumes, both *derived*
  from Mathlib rather than reproved there: the averaging identity `|G| · dim V^G = Σ χ(g)` and
  the equivariant-map dimension formula, each restated with the group order cleared to the
  left, which is the shape the kernel-checked integer sums are in. Above them, the transport
  itself (ROADMAP §A10): V₆ built as the permutation representation of S₄ on the two-element
  subsets of a four-set, its character identified with the fixed-face count via
  `Matrix.trace_permutation`, and the counting layer's 72 divided by 24 to give a genuine
  `Module.finrank` — `dim Hom_G(V₆, V₆) = 3`, with `dim V₆^G = 1` alongside. The
  identification of this model with the signed-permutation V₆ is *not* asserted in Lean; it is
  mirror-checked in `representation_bridge_probe.py` (B4) on the full character multiset.
- `lakefile.toml`, `lean-toolchain` — pinned to mathlib4 `v4.33.0`. Kernel check:
  `cd verification/lean-mathlib && lake exe cache get && lake build`.
