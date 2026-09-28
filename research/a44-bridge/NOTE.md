# A44 bridge diagnostic — can a defined OI-side carrier see Diţă status on act 39's family?

Disposable pre-freeze research thread (gem-finding, §A.31). Not a native round: no
preregistration under §A.39, no `F`, no receipt, no pull request. Base: `D41 =
78ea3c39004e97aad027ee6153051c6d372bdd55` (after act 40's landing). Nothing here is adopted,
and nothing here changes any landed verdict.

## 0. The decision rule, fixed before any computation

This section was committed before the probe `bridge_probe.py` existed.

**Objects.** `H3(u) = SIG ∘ u₁^A u₂^B u₃^C` on the sixteen-point product carrier `V = Fin 4 × Fin 4`,
ancilla `Fin 1 × Fin 1`, visible slice `Γ = Γ₀ ⊗ Γ₀ = J/16` (act 39's head). `L ⊂ T³` is act 40's
Diţă locus, `u₁ = ±1 ∨ u₂ = 1 ∨ u₃ = ±1` (kernel for the if-direction, probe for the only-if and
for strict = relaxed).

**Domains.**
- `Ω` — the torus, through `u ↦ H3(u)`.
- `Ω⁺` — the two-sided invisible-gauge closure `{D₁ · H3(u) · D₂}`, `D₁`, `D₂` diagonal unitary.
  At `|A| = 1` this is exactly act 12's two-sided orbit (shown in §2). `L` is extended to `Ω⁺` by
  the relaxed Diţă status, which is invariant under `D₁ · _ · D₂` by its definition.

**Carrier.** Any function `κ` defined in the repository on these objects, or on them through an
embedding that the note names explicitly (an embedding the repository does not supply is marked
as such, and its verdicts are conditional on it).

**Rule D — `κ` detects Diţă status on a domain `X`** iff `κ(L ∩ X) ∩ κ(X ∖ L) = ∅`, i.e. there is a
function `f` with `f ∘ κ = 1_L` on `X`. Established by an explicit `f` checked exactly over the
whole domain, or by a factorization proof (`κ` separates an equivalence under which `L` is
invariant).

**Rule B — `κ` is blind on `X`** iff some `x ∈ L ∩ X`, `y ∈ X ∖ L` have `κ(x) = κ(y)`: exhibited in
exact arithmetic, or proved to exist (lattice-coset lemma or topological lemma, §3). *Strongly
blind*: `κ` constant on `X`.

**Non-constancy is not detection.** A carrier that varies along the torus but has one collision
across `L` is blind.

**Grades of detection.**
- *by completeness* — `κ` separates every pair of points of `X` in distinct two-sided classes (it
  resolves the whole invisible-gauge class), so it detects every class-invariant property, Diţă
  status among them; the detection carries no Diţă-specific content.
- *specific* — `κ` detects but identifies some pair of distinct two-sided classes.

**Exact lemma to be used for monomial carriers (stated here, proved in §3).** If on `Ω` a carrier
has the form `κ(u) = c ∘ u^M` with every `c_p ≠ 0` and integer exponent rows `m_p ∈ ℤ³`, let
`Λ = ℤ⟨m_p⟩`. Then `κ` detects on `Ω` iff `Λ ⊇ 2ℤ × ℤ × 2ℤ`, and `κ` is injective on `Ω` iff
`Λ = ℤ³`.

**Controls — every verdict below is void unless all of these come out as stated.**
- `C+1`: `κ = 1_L` registers DETECTOR.
- `C+2`: `κ = (u₁², u₂, u₃²)` registers DETECTOR (specific: it identifies `u` with `(−u₁, u₂, −u₃)`).
- `C−1`: a manifestly gauge-invariant constant — the realizability sum `∑ᵢ Gᵢ = 1` and the feature
  norm — registers BLIND (strongly).
- `C−2`: the non-constant `κ = u₁u₂u₃` registers BLIND, with an exhibited exact collision.
- `C−3`: `κ = (u₁², u₂², u₃²)` registers BLIND, the collision across the absent face `u₂ = −1`.
- *Consistency control (A40 cross-check, not a verdict):* act 12's two-sided class of `H3(u)` must
  separate `u₂ = 1` from `u₂ = −1` at generic `u₁`, `u₃`, since the kernel's separation theorem and
  the relaxed invariance of Diţă status would otherwise contradict act 40's locus. If it failed,
  the thread halts.

**Interpretation, fixed in advance.** "No tested carrier separates" means only that Diţă status is
redundant relative to the tested carriers. "A carrier separates" means a formal map from that
OI-defined quantity to Diţă status, never a physical identification, unless the repository already
supplies that map. Every carrier keeps the status the repository records for it; none is declared
the physical observable here.

### Amendment 1 (2026-09-28, owner refinement, received before any result was recorded)

The rule above is kept as written; where it differs, this amendment governs.

1. **Two properties, reported separately for every applicable carrier.**
   - *Separates a cross-boundary pair*: some point of `L` and some point off `L` get different
     values. Evidence of sensitivity only; it never earns DETECTOR.
   - *Determines locus membership*: whenever two `H3` points have the same value, both are in `L`
     or both are off it — Diţă status factors through the carrier. Only this earns DETECTOR, and it
     needs a global argument or an exhaustive exact check over the whole torus, never selected
     examples.
2. **BLIND** requires an **exhibited** pair of `H3` points with exactly equal values (exact
   arithmetic) and opposite `L`-status. Cross-boundary collisions are searched for first. A
   collision proved to exist but not exhibited is recorded as such and does not by itself earn
   BLIND.
3. **NOT APPLICABLE is strict.** A carrier defined on trajectories, time-indexed lifts, instruments,
   causal readbacks or any other object type, for which the repository has no already-certified map
   from a static `H3` realization into its domain, is NOT APPLICABLE. No such map is constructed in
   this thread; the absence is recorded as a finding. (This withdraws the rule's allowance for
   embeddings named by the note.)
4. **Pipeline form**, for every carrier: carrier → applicable? → invariant under which established
   equivalence, with proof → cross-boundary collision found? (the exact pair) → separates a
   cross-boundary pair? → global membership determinacy? → evidence level.
5. **Controls, adapted.** The indicator `1_L` must come out DETECTOR; a toy that varies with `u`
   but is not a function of locus membership — the coordinate `u₁` — must come out "separates a
   pair" and not DETECTOR (it is BLIND by an exhibited collision); a gauge-invariant constant must
   come out BLIND by an exhibited collision. `C+2`, `C−2`, `C−3` and the A40 consistency control are
   kept.
