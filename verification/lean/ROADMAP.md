# Roadmap — planned formalizations

The four core proof files are deliberately dependency-free, and stay that way. A single
separate file under `lean-mathlib/` binds to Mathlib, for the one classical bridge that
genuinely needs finite-dimensional linear algebra. Statements below are fixed; the companion
probes verify every concrete number they assert.

## A. Representation-theoretic bridge — mostly DELIVERED

The section split in two on contact with the work. Most of it is finite arithmetic and needed
no dependency at all: it is now kernel-checked in the zero-import layer. Only the averaging
identity itself, and the "≅" upgrades that quantify over representations, need Mathlib.

A1. **Delivered** (`lean-mathlib/OIBridge.lean`). The averaging identity: for a finite group
G and a finite-dimensional representation over a field in which |G| is invertible,
|G| · dim(fixed subspace) = Σ_g χ(g), by identifying the group average with the projection
onto the invariant subspace and taking its trace. This is the identity the counting layer
defers; it is what converts every character sum below into a dimension.
A2. **Delivered** (`OI_Gauge_Certificates.lean`, `irr_orthonormal`), and in a stronger form
than specified: rather than a class table with weights (1,8,6,6,3) entered as data, the five
irreducible characters are given as functions on the group elements — A₁ constant, E and T₁
the pieces χ₆ already uses, A₂ the validated parity, T₂ = T₁ ⊗ A₂ — and orthonormality is
summed over the actual 24 rotations. No separate claim that the class census is correct is
then needed.
A3. **Delivered** (`mult_V6`): ⟨χ₆, χᵢ⟩ = 24 · (1,0,1,1,0), multiplicity-free on {A₁, E, T₁}.
A4. **Delivered** (`mult_End`, `mult_End_dims`): 24 · (3,1,4,5,3), accounting for all 36
dimensions of End(V₆).
A5. **Delivered** as arithmetic, given A1: the sums 72 / 288 / 144 are kernel-checked and A1
divides them by 24. What remains is A10 — carrying them across to a Mathlib `Representation`
so the quotient is literally a `finrank`.
A6. **Delivered at character level** (`mult_broken`, `mult_broken_dims`): 24 · (0,0,2,4,2)
over 22, so the broken restriction carries no A₁ or A₂ and no equivariant scalar survives on
it. The explicit idempotent isotypic projectors (traces 0, 0, 4, 12, 6) remain for the
Mathlib phase; they are 22×22 matrix algebra, not a `decide` target.
A7. **Delivered** (`OI_Regulator_Symmetry.lean`): Σχ over Sym²(ℝ⁴) is 384 = 1 · 384 for the
hypercubic group and 192 = 2 · 96 for the native group, and the fixed basis
{diag(1,0,0,0), diag(0,I₃)} is exhibited as invariant under the native group by direct check
rather than inferred from a dimension count. The hypercubic countercontrol is included.
A7b. **Delivered** (same file): Σχ over Sym²(Λ²ℝ⁴) is likewise 384 and 192, with
{Σ_i F₀ᵢ², Σ_{i<j} Fᵢⱼ²} exhibited invariant under the native group and the electric form
shown *not* invariant under the hypercubic group. Electric and magnetic normalizations are
therefore independent under the native symmetry and are locked to each other only by the
Euclidean regulator — the gauge-sector counterpart of A7.
A8. **Delivered** (`sqTrivial_odd`, `sqTrivial_four`). Note the general statement for every
odd q was already proved by `eq_one_of_sq_of_odd`; what was missing, and is now present, is
the q = 4 countercontrol showing the oddness hypothesis is load-bearing.
A9. **Open.** The Schur sign theorem: −B D⁻¹ Bᵀ ⪯ 0 for D ≻ 0, with an indefinite-D witness
for necessity. Analytic rather than finite, and unrelated to the counting machinery — it
shares nothing with A1 and is better taken as its own piece of work.
A10. **Open, and now the substantive remainder.** Transport lemmas aligning the in-file
character and element data with the Mathlib vocabulary: a group instance on the 24 elements,
a `Representation` whose character is `chi6`, and the bijection carrying `rots` onto it. Only
then do A5's quotients become `finrank` statements about the actual cubic representation
rather than integer arithmetic beside a general theorem. Nothing numerical is missing; this
is bookkeeping, and it is what the two halves of the section are still waiting on.

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
