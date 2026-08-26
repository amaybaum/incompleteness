# Roadmap — planned formalizations

The five core proof files are deliberately dependency-free, and stay that way. A single
separate file under `lean-mathlib/` binds to Mathlib, for the statements that genuinely need
finite-dimensional linear algebra — the ones containing the word *dimension*, which finite
arithmetic cannot reach. Statements below are fixed; the companion probes verify every concrete
number they assert.

## A. Representation-theoretic bridge — mostly DELIVERED

The section split in two on contact with the work. Most of it is finite arithmetic and needed
no dependency at all: it is now kernel-checked in the zero-import layer. What genuinely needs
Mathlib turned out to be smaller still — the averaging identity and the Hom-dimension formula
are both already *in* Mathlib, so all that had to be built was the transport of the cubic data
onto a `Representation`. That is A10, and it is now delivered. Two of A5's three quotients are
dimensions on the strength of it. What remains open in this section is A9, which shares nothing
with the counting machinery, and A5-B22, which needs the broken sector built as a representation
in its own right — a construction, not more plumbing.

A1. **Available — from Mathlib, not from this layer.** The averaging identity
|G| · dim(fixed subspace) = Σ_g χ(g) is `Representation.card_inv_mul_sum_char_eq_finrank` in
`Mathlib/RepresentationTheory/Character.lean`. An earlier round reproved it here from
`isProj_averageMap` and `IsProj.trace` without checking that the assembled statement already
existed; it did, by the same proof. `lean-mathlib/OIBridge.lean` now only restates it with the
group order cleared to the left, which is the shape the kernel-checked integer sums are in.
The same file also restates `card_inv_mul_sum_char_mul_char_eq_finrank`, the equivariant-map
dimension formula — the engine behind A5 and B1, likewise already supplied by Mathlib.
A2. **Delivered** (`OI_Gauge_Certificates.lean`, `irr_orthonormal`), and in a stronger form
than specified: rather than a class table with weights (1,8,6,6,3) entered as data, the five
irreducible characters are given as functions on the group elements — A₁ constant, E and T₁
the pieces χ₆ already uses, A₂ the validated parity, T₂ = T₁ ⊗ A₂ — and orthonormality is
summed over the actual 24 rotations. No separate claim that the class census is correct is
then needed.
A3. **Delivered** (`mult_V6`): ⟨χ₆, χᵢ⟩ = 24 · (1,0,1,1,0), multiplicity-free on {A₁, E, T₁}.
A4. **Delivered** (`mult_End`, `mult_End_dims`): 24 · (3,1,4,5,3), accounting for all 36
dimensions of End(V₆).
A5. **Split into A5-End (delivered) and A5-B22 (open).** The sums 72 / 288 / 144 are
kernel-checked in the zero-import layer and A1 divides them by 24. Two of the three are now
`Module.finrank` statements rather than integer quotients:

- `72 / 24 = 3` — `Cubic.finrank_commutant : finrank ℚ (IntertwiningMap rho rho) = 3`, with
  `Cubic.finrank_invariants : finrank ℚ (invariants rho) = 1` beside it.
- **A5-End**, `288 / 24 = 12` — `Cubic.finrank_hom_end`. `End(V₆)` needed no construction:
  Mathlib's `Representation.linHom` is the conjugation action and `char_linHom` gives its
  character, so the transport is one decidable sum plus the same division.

**A5-B22, `144 / 24 = 6`, is open, and it is a different kind of step.** An earlier round called
both remaining quotients "mechanical given the pattern A10 establishes"; that was too coarse and
is corrected here. There is no `B₂₂` object in the bridge for a `Hom` to target, and building
one is a construction, not plumbing. The target is at least canonical now: opposite faces give
the intrinsic invariant split `V₆ = T₃ ⊕ E₂ ⊕ A₁`, and `B₂₂` is exactly the off-diagonal part
of `End(V₆)` —
`Hom(E,T) ⊕ Hom(T,E) ⊕ Hom(A,T) ⊕ Hom(T,A) ⊕ Hom(A,E) ⊕ Hom(E,A)`, dimension 22, character
`2(χ_T χ_E + χ_T χ_A + χ_E χ_A)`, which is the core layer's `chiBrk`. The Mathlib pieces exist
(`Subrepresentation.toRepresentation`, `linHom`, representation products); the work is
describing the three submodules to Lean, and it deserves its own round.
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
A10. **Delivered** (`lean-mathlib/OIBridge.lean`, namespace `Cubic`). The transport onto a
Mathlib `Representation`. Two things once believed to be part of this item never were: Mathlib
already proves the averaging identity (`card_inv_mul_sum_char_eq_finrank`) **and** the
equivariant-map dimension formula (`card_inv_mul_sum_char_mul_char_eq_finrank`), so A1 and A5's
engine were never missing. And the group need not be built as a subgroup of `Perm (Fin 6)`:
**V₆ is the permutation representation of S₄ on the two-element subsets of a four-set**,
mirror-checked in `representation_bridge_probe.py` (B4) by comparing the full character
multisets, so `Equiv.Perm (Fin 4)` serves directly — `Fintype.card_perm` gives the order 24 and
`Matrix.trace_permutation` gives the character as a fixed-point count, with no new trace theory.

The step that had stalled was the last one in `character_eq_fixCount`: `trace_permutation`
delivers a `Set.ncard`, and routing it through `Set.ncard_eq_toFinset_card'` selects a `Fintype`
instance that `Set.mem_toFinset` then does not match. The route that works is the one Mathlib's
own proof of `trace_permutation` takes — exhibit the fixed-point set as a **coerced `Finset`**
and finish with `Set.ncard_coe_finset`, which carries no `Fintype` instance at all.

## B. Structural chain completions (probe: `structural_chain_probe.py`)

The section split on the A10 dependency, and the split is kept here so that neither half gets
reported closed on the strength of the other. A10 landed, and B1 is now closed on the strength
of it. B3 remains split, and its two halves are still unrelated to each other.

B1. **Delivered** (`Cubic.equivariant_kernel_lives_in_finrank_three`, in
`lean-mathlib/OIBridge.lean`). The
operator-level forms are proved in `OI_Structural_Core.lean` — `mz_identity`,
`kernel_equivariant`, `susskind3`, `center_anticommutator`, `mass_square` — and the missing step
was from "K_m commutes with every R_g" to "K_m lies in a space of dimension 72/24 = 3". Every
kernel satisfying the cubic equivariance equation is now shown to lie in a **fixed**
three-dimensional operator space, the dimension being `Cubic.finrank_commutant`. The confinement
is the physical content, not the classification: the symmetry does not merely reduce a parameter
count, it pins every admissible kernel into one space.

The hypothesis is in composition form, `K ∘ₗ ρ g = ρ g ∘ₗ K`, which is definitionally the
`isIntertwining'` field — so the bundling is a structure literal — and is the closer reading of
`kernel_equivariant`, which is an operator identity rather than a pointwise statement.

The architectural point is worth keeping on record: this corollary **cannot** live in
`OI_Structural_Core.lean`. That file is zero-import and stays that way, and the word *dimension*
is not available in it at all. The split between the two files is exactly the split between the
implication and its dimensional reading.
B2. **Delivered** (`OI_Structural_Chain.lean`, `path_prop`). The detailed-balance lemma,
stated without the exponential. The `exp` in W(m→n)/W(n→m) = e^{−τ(ω_n−ω_m)} does one job —
making the edge ratio a gradient g_n/g_m — so cross-multiplying gives a multiplicative cocycle
in a commutative monoid, with no division, no field inverse and no spectral theory. Perron–
Frobenius is neither used nor needed: uniqueness up to scale comes from connectivity and
invertibility. The statement proved is stronger than the mirror's, which recovers a stationary
vector as a null space; here every edgewise-balanced p is proportional to g along any path.
Connectivity is shown load-bearing by a two-component witness whose bridging edge is
unbalanced.
B3. **Split.** The algebraic core — Corollary 1a's `dim Sym²(ℝ³)^{B₃} = 1` — is **delivered at
character level** (`sum_trSym_b3`, `sum_trSym_rot`): Σχ = 48 = 1·48 over the 48-element signed
permutation group and 24 = 1·24 over its rotations, with `δ` exhibited invariant and
`diag(1,0,0)` shown not to be. As with A7/A7b the closing division by the group order is A1.
The *dimension* statement is **not blocked any more but not delivered either**: A10 supplies
the pattern, and applying it here needs a second representation — the 48-element signed
permutation group acting on Sym²(ℝ³) — built the way `Cubic.rho` is. The harmonic dispersion
cos ω = (1/d) Σ cos kⱼ
is **open and genuinely analytic**: it needs `Real.cos`, the range side-conditions on `arccos`,
and a Taylor expansion for the O(a²k²) form. Its algebraic skeleton — that in any commutative
ring `u_t = z^t` solves the second-order recursion exactly when z + z⁻¹ = α Σ_μ (c_μ + c_μ⁻¹)
— is core-expressible and is what the probe now verifies constructively on the lattice.

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
