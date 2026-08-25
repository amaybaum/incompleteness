# Roadmap — planned formalizations

The current proof files are deliberately dependency-free. The next layer binds to Mathlib
and closes the remaining classical bridges. Statements below are fixed; the companion
probes already verify every concrete number they assert.

## A. Representation-theoretic bridge (probe: `representation_bridge_probe.py`)

A1. The averaging identity: for a finite group G and finite-dimensional real (or rational)
representation, |G| · dim(fixed subspace) = Σ_g χ(g). This is the one classical identity
the counting layer of `OI_Gauge_Certificates.lean` defers.
A2. The O character table over classes [e, 8C₃, 6C₂′, 6C₄, 3C₂] with weights (1,8,6,6,3),
entered as a `decide`-checked row-orthonormality certificate, not trusted data.
A3. V₆ multiplicities (1,0,1,1,0): multiplicity-free with constituents {A₁, E, T₁}.
A4. End(V₆) ≅ A₁³ ⊕ A₂¹ ⊕ E⁴ ⊕ T₁⁵ ⊕ T₂³ (36 dims).
A5. Hom dims 3 / 12 / 6 from the kernel-checked sums 72 / 288 / 144 via A1.
A6. broken₂₂ ≅ E² ⊕ T₁⁴ ⊕ T₂² with explicit idempotent isotypic projectors
(traces 0, 0, 4, 12, 6).
A7. The regulator-symmetry theorem by the same machinery: dim Sym²(ℝ⁴) invariants — 1 for
the 384-element hypercubic group, 2 for the 96-element native spatial-B₃ × T group, with
fixed basis {diag(1,0,0,0), diag(0,I₃)}.
A7b. The same statement on the field strength: quadratic invariants of an antisymmetric
F over Sym²(Λ²ℝ⁴) number **1** under the 384-element hypercubic group and **2** under the
96-element native spatial-B₃ × time-reflection group, with fixed basis exactly
{Σ_i F₀ᵢ², Σ_{i<j} Fᵢⱼ²}. Electric and magnetic normalizations are therefore independent
under the native symmetry and are locked to each other only by the Euclidean regulator —
the gauge-sector counterpart of A7.

A8. ZMod censuses: for odd q every additive character with χ² = 1 is trivial (instances
q ∈ {3,…,13}); the q = 4 witness shows Odd is necessary.
A9. The Schur sign theorem: −B D⁻¹ Bᵀ ⪯ 0 for D ≻ 0, with an indefinite-D witness for
necessity.
A10. Transport lemmas aligning the in-file character/hom classes with the Mathlib
vocabulary, so the certificate theorems restate without change of content.

## B. Structural chain completions (probe: `structural_chain_probe.py`)

B1. The V₆-instance corollaries of Theorems 1a/2/3 that require A1 (the operator-level
forms are already proved in `OI_Structural_Core.lean`).
B2. The GR detailed-balance lemma: on a finite connected transition graph with
W(m→n)/W(n→m) = e^{−τ(ω_n−ω_m)}, the stationary state is Gibbs, unique up to scale;
disconnected necessity witness.
B3. The exact harmonic dispersion cos ω = (1/d) Σ cos kⱼ of the second-order update, and
Corollary 1a's algebraic core (dim Sym²(ℝ³)^{B₃} = 1) as an instance of A1.

## C. Generator-relations layer — DELIVERED for three and four axes

`OI_Staggered_Relations.lean` derives the anticommutation and square hypotheses of
`susskind3` from the staggered generator relations (η involutions; commuting shifts; η_μ
anticommutes with the shifts of strictly earlier axes and commutes with those of later
axes) and concludes the factorization at three and four axes with no remaining hypotheses.
The relations are quantified over `Nat`-indexed axes, so the structure already covers every
dimension; what remains is the arbitrary-n conclusion, which needs a sum over an index
family (a list- or `Finset`-induction, natural to add with the Mathlib bridge of section A)
rather than the per-dimension expansions used now.

C1 is now also delivered: `Staggered.factorization` proves `(∑_{i<n} A_i)² = ∑_{i<n} S_i²`
for every `n` by structural induction over a list of pairwise-anticommuting summands, with
the three- and four-axis theorems kept as explicit corollaries. Section C is closed.

## D. Conventions and statement forms

- `papers/SM.md` states D² = −¼□_lat without displaying the □ sign convention; the
  factorization is exact with □_lat := −Σ_μ (T_μ − T_μ⁻¹)², and the probes pin this
  constructively. A future text revision should display the convention beside the theorem.
- The abstract relations are dimension-free, but a *periodic* lattice realizes the staggered
  phase pattern only for **even extent**: at odd L the wrap from L−1 to 0 does not flip the
  parity phase, and η_μ fails to anticommute with the shifts of earlier axes
  (`staggered_relations_probe.py`, S6, with the countercontrol at L = 3 and 5). Any statement
  of the factorization on a periodic lattice should carry the even-extent hypothesis.
- Theorem 3 is formalized at operator level: {D + m·ε + p₀·1, ε} = 2m + 2p₀·ε, so center
  independence of the diagonal of D_st is equivalent to exact chirality. Per the SM
  remark, the second-order update's self-term C = 2(1−d) is the Laplacian diagonal, not a
  mass term; the statement encodes this scope.

## E. Further targets

Polynomial identities from the results ledger; interval-arithmetic certification of quoted
numerical constants; axiomatized statements of the conditional interfaces (modular/KMS
inputs) so the conditional theorems can be checked relative to explicitly named
assumptions.
