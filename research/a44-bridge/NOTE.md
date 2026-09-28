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

***

Everything below was written after the probe ran. `bridge_probe.py` (this directory) reproduces
every exact claim marked **X**; its output is `bridge_probe.log` (64 `PASS`, 0 `FAIL`, about 50 s on
one core, Python standard library only). Evidence levels: **K** a landed kernel theorem, cited; **X** exact computation in
this thread (not frozen, not in CI); **P** a proof written in this note; **A40p** act 40's
exact-computation layer; **H** heuristic.

## 1. Inventory

The question is which OI-side objects are *already defined* on a static `H3` realization. The only
certified maps out of a point `H = H3(u)` are:

- `pad H := Matrix.of fun p q => H p.1 q.1` on `(Fin 4 × Fin 4) × (Fin 1 × Fin 1)` — unitary by
  `a35_shared_pad_unitary` (`DitaHull.lean:122`) and an `AdmissibleDilationAt` of `Γ = Γ₀ ⊗ Γ₀`
  inside `a35_shared_gram_realizable` (`DitaHull.lean:140`), which A39 applies on the whole torus;
- the Gram family `i ↦ (conj(H i j) · H i k)_{jk} = FibreGram 0 (pad H)` (the `hG` step of
  `a35_shared_gram_realizable`), realizable, whose feature vector A39 places in the product
  normalized set;
- `H` itself as a square matrix on the carrier `Fin 4 × Fin 4`, to which predicates on matrices
  apply directly.

| carrier (repo name) | definition | input type | applicable to `H3`? |
| --- | --- | --- | --- |
| visible slice `𝒪₀`: `readback a₀ (‖U ·‖²)` | `DilationChoice.lean:86`, `AdmissibleDilationAt` `:134`; carrier table `ThreadingObservability.lean` docstring | one dilation | yes, via `pad` |
| any act-9 admissible readback `R.map` | `ReadbackRobustness.lean:95`, `AdmissibleReadback` `:120` | one dilated real matrix | yes, on `‖pad H‖²` |
| `IsUnistochastic` of the visible slice | `BarandesTuple.lean:430` | real matrix | yes, on `𝒪₀` |
| `FibreGram` (raw, representative-level) | `TwoSidedGauge.lean:95` | one dilation | yes (A35/A39) |
| `GramPhaseEquiv` class; `mixedTriple`; `featureVec`; product normalized set | `TwoSidedGauge.lean:102`; `OrbitGeometrySelector.lean:79`; `OrbitGeometryRigidity.lean:99` (the product set is written inline in A39's statement) | Gram tuple | yes (A39) |
| act 12 cross invariant `G i₀ i₁ i₀ · G i₁ i₀ i₁` | `gramPhaseEquiv_cross_invariant`, `TwoSidedGauge.lean:870` | Gram tuple | yes |
| act 35 cross coordinates `G_{(a,b)}((c,d),(c',d)) · G_{(a,b')}((c',d),(c,d))`, and the identity "all equal `1/256`" | `a35_shared_cross_core`, `DitaHull.lean:236` | Gram tuple | yes |
| act 34 product-stratum membership | inline in `ProductStratum.lean` statements | feature vector | yes |
| act 35 column / row hull membership (product index) | inline in `DitaHull.lean` statements | feature vector | yes |
| act 24/26 distance `d`, `dist ∘ featureVec` | `OrbitGeometrySelector` frozen equation; `dist_featureVec`, `OrbitGeometryRigidity.lean` | pair of Gram tuples | yes, against the certified point `SIG` (the reference is a parameter) |
| `𝒪₁`: `AnchoredChannel a₀ M`; `CrossFibreGram a₀ M` | `ThreadingObservability.lean:144`, `:158` | one dilation | yes, via `pad` |
| `diagClass`, `permClass` (`IsScaledPartialPerm`), `IsMonomial`, `PreservesNonneg ∘ conjChannel`, `Realized` by a bijection-level class | `LieRankSource.lean:88`; `SubstratumInterfaceAudit.lean:231,236,505,536`; `SubstratumInterface.lean:75`; `MonoidalCompletion.lean:360` | square matrix / channel | yes, on `H` |
| `RepUnitary`, `repAugmented` | `OperationalSourcing.lean:819,830` | square matrix | yes, on `H` |
| `CoherentLift`, `GaugeRelated`, `TwoSidedRelated`, `CrossGram`, `FibreCrossGram`, `ConstLeft/RightRelated`, `ThreadingRelated` | `CoherentLiftGauge.lean:124,135`; `TwoSidedGauge.lean:84`; `CrossTimeInvariants.lean:101–123`; `ThreadingObservability.lean:171` | `ℕ`-indexed lift | **NOT APPLICABLE** |
| `𝒪₂` `RelativeCandidate`, `𝒪₃` `ReanchoredChannel` | `CancellationFork.lean:123`; `ReanchoredChannelScope.lean:119` | `ℕ`-indexed lift, time pair | **NOT APPLICABLE** |
| `MovesVisibleCandidate`, `VisibleInvariance`, `PreservesDivergence`, `JointlyReproducingAnchor`, `AnchorInvariantDivergence` | `DilationChoice.lean:271,284`; `ReadbackRobustness.lean:220`; `AnchorRobustness.lean:103,116` | a visible pair with two pairs of dilations | **NOT APPLICABLE** (no certified pairing of a static point) |
| `GramTrajEquiv`, `SelectsAt`, `PointwiseLaw`, `DeterminesTraj`, `ProperAt`, `PropagatesFrom`; the orbit-law ladders of acts 19–23, 27–31 | `GramTrajectorySelection.lean:121,131`; `IntermediateCrossTimeStructure.lean:133–186` | Gram trajectories, laws | **NOT APPLICABLE** |
| `PDivisible`, `C4e`, `C4r`, `PDivisibleCol`, `PPer`, `FiniteRootedRealizable`, `BarandesTuple`, `tupleP`, `SingletonT0Divisible`, `DirectBranch`, `ContinuousExtension.Extends` | `CausalReadback.lean:54–67`; `TransposeBridge.lean:110`; `RootedClassification.lean:27–115`; `BarandesTuple.lean:100–226,478`; `ContinuousExtension.lean:95` | visible families `ℕ → Matrix` | **NOT APPLICABLE** |
| `RootedRealization`/`rootedMap`; `QfbData` (`born`, `bornPow`, `rooted`, `QStar`); `candidateOf`; `padData` | `CausalReadback.lean:178,190`; `QuantumRepresentation.lean:60–165`; `CandidateSelection.lean:60`; `OperationalSourcing.lean:259` | realizations and representations with `init`, `read` | **NOT APPLICABLE** (no certified `init`/`read` for a static point) |
| `FiniteOperationalTheory` availability, `HasCompositeUnitaryControl`, `DenseUnitaryControl`, `NonnegBounded`, `PhasesAvailable`, `InstAvail`, `IsGenInstrument`; the operational audits (`verification/audits/operational/`), the C4 causal-readback audit, the rooted observer-family sourcing | `OperationalAssembly.lean:594,665`; `DiscreteCompletion.lean:45`; `FrozenSourcing.lean:65`; `RouteB.lean:128`; `InstrumentRealization.lean:57` | theories, instruments, visible families | **NOT APPLICABLE** |

**Finding N (the absence).** Every carrier the repository treats as multi-time, probabilities-only or
operational in the instrument sense — `𝒪₂`, `𝒪₃`, rooted families, the C4 forms, divisibility, the
Barandes tuple, anchor and readback robustness, instrument availability — takes a lift, a trajectory,
a visible family, a pair of dilations or a theory. The repository certifies no map from a static
single-slice realization such as `H3(u)` into any of those domains. Act 39's family is a family of
single-time objects; nothing makes `u` a time or pairs a point with a reference. So every carrier
on which a Diţă distinction could acquire a multi-time operational reading lies behind a map the
repository does not contain. Assumption-watch marker **AW-static**: any future claim that Diţă
status is operationally meaningful must supply that map, and its verdicts are relative to it.

## 2. Invariance lemmas

**I1 (Diţă status).** The relaxed Diţă status — some shape, index map and orientation, up to
`D₁ · _ · D₂` — is invariant under `H ↦ D₁ H D₂` (the relaxation is by a group), under independent
row and column permutations (index maps are arbitrary bijections), under transposition (both
orientations are quantified) and under entrywise conjugation (the conjugate of a Diţă form is one).
**P**. On `H3` the strict and relaxed loci coincide (**A40p**), so `L` is the locus of either.

**I2 (the invisible gauge at `|A| = 1` is diagonal equivalence).** On `(Fin 4 × Fin 4) × (Fin 1 × Fin 1)`
a `LeftFibreGroup` element has `L p q = 0` unless `p.1 = q.1`, and the ancilla has one point, so `L`
is diagonal unitary; a `WeakAnchorStabilizer` element has every column anchored, so it is diagonal
unitary. Hence act 12's two-sided relation on single slices is exactly `pad H' = pad (D₁ H D₂)`. **P**
(definitions at `TwoSidedGauge.lean:78`, `CoherentLiftGauge.lean:114`). With I1, Diţă status is a
function of the two-sided class. Assumption-watch marker **AW-|A|=1**: this coincidence of the
invisible gauge with the Hadamard diagonal equivalence is special to the trivial ancilla; at
`|A| > 1` the left group is `∏ U(A)` and no such alignment is established.

**I3 (the feature vector is a complete class invariant on flat unitaries).** For flat unitaries `H`,
`H'` at the product configuration: `featureVec(G(H)) = featureVec(G(H'))` iff `H' = D₁ H D₂`.
(⇐) `featureVec_gauge` / `mixedTriple_gauge` (**K**, `OrbitGeometryRigidity.lean:133`,
`OrbitGeometrySelector.lean:88`) with `fibreGram_left_mul` (**K**). (⇒) `geo1_separation_product`
(**K**, `OrbitGeometrySelector.lean:425`), realizability from `a35_shared_gram_realizable` (**K**),
`twoSided_slice_iff` (**K**, `TwoSidedGauge.lean:826`), then I2. Checked exactly at one point with
Gaussian-rational `D₁`, `D₂` on all 65 536 four-cycle coordinates (**X**, §5 of the probe).

**I4 (`𝒪₀` is constant on every flat unitary).** `readback 0 (‖pad H‖²) = Γ = J/16` for every flat
unitary `H`, and every act-9 admissible readback returns `Γ` on `‖pad H‖²` by its own clause `R-2`.
**K** (admissibility inside `a35_shared_gram_realizable`; `R-2` is a defining clause) and **X**.

**I5 (`𝒪₁` carries the Gram data as output probabilities).** `𝒪₁(pad H)(E_{jk})_{ii} = G_i(k, j)`
(`anchoredChannel_eq_trace` with `crossFibreGram_diag`, **K**; all `i, j, k` at one point, **X**), and
at `|A| = 1`, `𝒪₁(pad H)(ρ) = H ρ Hᴴ`, which determines `H` up to one global phase (**P**). `𝒪₁` is
moved by `D₁` (as act 14's `pq1b_constant_left_physical_anchoredChannel` records for constant left
moves, **K**) and by `D₂` (**X**).

**I6 (monomial structure on the torus).** Every Gram, feature, cross-invariant, act-35 and `𝒪₁`
coordinate of `H3(u)` equals its value at `SIG` times a character `u^m`, `m ∈ ℤ³`, because
`H3(u) = SIG ∘ u^E`. Exact by construction; spot-checked on 1500 random full feature coordinates at
three points (**X**).

## 3. Two lemmas used for the verdicts

**Lemma M (monomial carriers).** Let `κ(u) = c ∘ u^M` with all `c_p ≠ 0`, `Λ = ℤ⟨rows of M⟩`,
`K = {k ∈ T³ : k^m = 1 ∀ m ∈ Λ}`. Then `κ(u) = κ(u')` iff `u'/u ∈ K`; `κ` is injective iff `Λ = ℤ³`;
and `κ` determines membership in `L` iff `K ⊆ S := {±1} × {1} × {±1}` iff `Λ ⊇ 2ℤ × ℤ × 2ℤ`.
*Proof.* The first two are immediate. If `K ⊆ S`, `u ∈ L ⇒ uk ∈ L` for every `k ∈ K` since
`(u₁k₁)² = u₁²`, `u₂k₂ = u₂`, `(u₃k₃)² = u₃²`. If `k ∈ K ∖ S`: when `k₂ ≠ 1` take
`u = (v₁, 1, v₃)` with `(v₁k₁)², (v₃k₃)² ≠ 1`; when `k₂ = 1`, `k₁ ∉ {±1}`, take `u = (1, v₂, v₃)`,
`v₂ ≠ 1`, `(v₃k₃)² ≠ 1` (symmetrically for `k₃`); then `u ∈ L`, `uk ∉ L`, `κ(u) = κ(uk)`. The dual of
`S` as a subgroup of `T³` is `2ℤ × ℤ × 2ℤ`, which gives the lattice form. ∎

**Lemma T (continuous scalar carriers).** `L` is connected (every face meets the face `u₂ = 1`) and
has empty interior. If `κ : T³ → ℝ` is continuous and determines membership in `L`, then `κ` is
constant on `L`. *Proof.* If `κ(x) < κ(y)` for `x, y ∈ L`, then `κ(L) ⊇ [κ(x), κ(y)]`; the open set
`κ⁻¹((κ(x), κ(y)))` is nonempty and meets the dense complement of `L` at some `y'`, whose value is
taken on `L`. ∎ Under the amendment a collision proved this way is not yet BLIND; §4 exhibits one.

## 4. Separation tests and classification

Test points (exact Gaussian-rational units `v₁ = (3+4i)/5`, `v₂ = (5+12i)/13`, `v₃ = (8+15i)/17`,
`v₄ = (7+24i)/25`, `v₅ = (20+21i)/29`, `v₆ = (12+35i)/37`): seven in `L` — `(1,1,1)`, `(±1, v₂, v₃)`,
`(v₁, 1, v₃)`, `(v₁, v₂, ±1)`, `(−1,−1,−1)` — and six off it — `(v₁, v₂, v₃)`, the absent face
`(v₁, −1, v₃)`, `(i, i, i)`, `(v₄, v₄, v₄)`, `(v₅, v₆, v₄)`, `(−v₁, v₂, v₃)`; all flat unitary (**X**).
Membership of the seven face points is kernel (A40-1). **Off-`L` status of every point used in a
collision is certified independently of act 40** (§9 of the probe, **X**): at each such point, for
every shape `4×4`, `8×2`, `2×8` and both orientations, no partition of the rows into classes whose
pairwise ratio vectors have level sets of size `≥ n` survives the requirement that a common block
partition refine them — a necessary condition for a Diţă form strictly or up to `D₁ · _ · D₂`. The
same test passes at all seven face points.

### Controls

| control | required | result |
| --- | --- | --- |
| `C+1` `1_L` | DETECTOR | images `{True}` / `{False}` — DETECTOR |
| `C+2` `(u₁², u₂, u₃²)` | DETECTOR, specific | `Λ = 2ℤ × ℤ × 2ℤ`, index 4 — DETECTOR, not injective |
| `C−1` `∑ᵢ Gᵢ = 1`; feature norm `= 1` | BLIND by collision | equal at `(1, v₂, v₃)` and `(v₁, v₂, v₃)`; norm `1` everywhere — BLIND |
| `C−2` `u₁u₂u₃` | BLIND | `(1, v₂, v̄₂)` vs `(v₂, v₂, v̄₂²)` — BLIND |
| `C−3` `(u₁², u₂², u₃²)` | BLIND | `(v₁, 1, v₃)` vs `(v₁, −1, v₃)` — BLIND |
| toy `u₁` | separates a pair, not DETECTOR | `(1, v₂, v₃)` ≠ `(v₁, v₂, v₃)`; `(v₁, 1, v₃)` = `(v₁, v₂, v₃)` — BLIND |
| A40 consistency | `(0,1,0) ∈ Λ_featureVec` | holds (the class separates `u₂ = 1` from `u₂ = −1`) |

All controls came out as required, so the verdicts below stand.

### Per-carrier pipeline

`Λ` is the exponent lattice of Lemma M (computed exactly; for the feature vector over all `16⁶`
coordinates through their exact exponent distribution, 27 distinct exponents, every
`|m_k| ≤ 1`). "Ω⁺" is the two-sided closure; "flat" is every flat unitary at the product
configuration.

| carrier | applicable | invariant under (proof) | cross-boundary collision (exact pair) | separates a pair | determines membership | verdict | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `𝒪₀` visible slice; every act-9 admissible readback; `IsUnistochastic` of it | yes | everything: constant on all flat unitaries (I4) | `(1,v₂,v₃)` / `(v₁,v₂,v₃)`, both `J/16` | no | no | **BLIND** (strong) | K, X |
| `FibreGram` raw | yes | left fibre group (`fibreGram_left_mul`); covariant under weak right | none: `Λ = ℤ³`, injective on Ω | yes | yes on Ω; on Ω⁺ and flat (rows up to phase ⇒ class ⇒ I1) | **DETECTOR by completeness** | K, X, P |
| `GramPhaseEquiv` class = `featureVec` = point of the product normalized set | yes | two-sided gauge (I3), complete on classes (I3) | none: `Λ = ℤ³` | yes | yes on Ω, Ω⁺ and flat (I1 + I3) | **DETECTOR by completeness** | K, X, P |
| act 12 cross invariant (256 values) | yes | `GramPhaseEquiv` (**K**) | none: `Λ = ℤ³` | yes | yes on Ω and Ω⁺; flat: undetermined (completeness of these 256 values on all flat unitaries unknown) | **DETECTOR by completeness** on the family | K, X |
| act 35 cross coordinates (4096 values) | yes | `GramPhaseEquiv` (**P**, **X**) | `(v₁, 1, v₃)` / `(v₁, v̄₄³, v₃)`: `Λ = ⟨(1,0,1), (0,0,1)⟩` has rank 2 and misses `u₂` | yes | no | **BLIND** | X |
| act 35 identity (Boolean) and act 34 stratum membership | yes | `GramPhaseEquiv` | `(−1, v₂, v₃)` / `(v₁, v₂, v₃)`: identity fails at both, so both are off the stratum (`a35_shared_cross_core` + I3) | yes (`SIG` vs off) | no | **BLIND** | K, X |
| act 35 column / row hull membership (product index) | yes | `GramPhaseEquiv` | `(1, v₂, v₃)` / `(v₁, v₂, v₃)`: both fail the hull's necessary conditions | yes (`SIG` vs off) | no | **BLIND** | X |
| `dist(featureVec ·, featureVec SIG)` | yes | two-sided gauge; `u₁ ↔ u₃` and `u ↦ ū` (exponent-distribution symmetries, **X**) | `(v₁, 1, v₃)` / `(v₁, Q̄/Q, v₃)` with `Q = Q(v₁, v₃)`, `16⁶d² = 463945728/85` at both | yes | no (also by Lemma T) | **BLIND** | X, P |
| single-fibre feature coordinates | yes | constant | any pair | no | no | **BLIND** (strong) | X |
| `𝒪₁` `AnchoredChannel`; `CrossFibreGram` | yes | global phase only (moved by `D₁`, `D₂`) | none: `Λ = ℤ³` | yes | yes on Ω, Ω⁺, flat (determines `H` up to phase, I5) | **DETECTOR by completeness**, under `𝒪₁`'s recorded presupposition | K, X, P |
| `diagClass`, `permClass`, `IsMonomial`, `PreservesNonneg ∘ conjChannel`, `Realized` by a bijection-level class | yes | constant `False` (flatness; `h₀₁ conj(h₂₁) = −1` for every `u`) | `(1,v₂,v₃)` / `(v₁,v₂,v₃)` | no | no | **BLIND** (strong) | X, K (`preservesNonneg_of_realized`) |
| `RepUnitary`, `repAugmented` | yes | constant `True` on every unitary (`consequence_augmentedAll`, `repAugmented_allUnitaries`) | any pair | no | no | **BLIND** (strong) | K |
| every carrier in the NOT APPLICABLE rows of §1 | no | — | — | — | — | **NOT APPLICABLE** | inventory |

No carrier is UNDETERMINED on the torus. The one open cell is the act 12 cross invariant on all flat
unitaries.

### The explicit form of the feature-vector detector

Three single four-cycle coordinates of `featureVec`, `ψ_q = G_a(b, b') · G_{a'}(b', b) · G_{a'}(b, b)`
with `(a, a', b, b') = (0, 7, 0, 4)`, `(0, 8, 0, 1)`, `(0, 1, 0, 2)`, carry the characters `u₁⁻¹`,
`u₂⁻¹`, `u₃⁻¹`, so on the torus

`1_L(u) = [ψ_{q₁}(u) = ±ψ_{q₁}(SIG)] ∨ [ψ_{q₂}(u) = ψ_{q₂}(SIG)] ∨ [ψ_{q₃}(u) = ±ψ_{q₃}(SIG)]`,

exact for every `u` by I6 and checked at the thirteen points (**X**). Read skeptically, this is a
readout of the torus coordinates, not a Diţă criterion: it refers to `SIG`'s values and to the
parametrization, and says nothing about a flat unitary off the family.

## 5. What the results say, and what they do not

1. **Relative to `𝒪₀`** — the only carrier the repository records as the visible, probabilities-only
   single-time datum — Diţă status is redundant: `𝒪₀` and everything built on it is constant on
   every flat unitary of the product configuration, not only on the family.
2. **Relative to the lift-space coordinates** (`FibreGram`, the Gram class, `featureVec`, the product
   normalized set) and to `𝒪₁`, Diţă status is not redundant: the formal map exists. It is
   `featureVec(G(H)) ↦` the relaxed Diţă status, well defined on the product normalized set by I1–I3,
   and it separates every face point from every off-face point. The map has no Diţă-specific
   content: every detector found resolves the whole two-sided class on the family (`Λ = ℤ³`), so it
   detects any class-invariant property equally. The repository records `FibreGram` as "a coordinate
   on the lift space, not a physical quantity" (act 12), the feature geometry as named objects of
   test not adopted as physical (act 24), and `𝒪₁` as a carrier whose status as observation is a
   recorded presupposition (act 14). The bridge obtained is therefore formal, to those objects, and
   no physical identification follows.
3. **Every named carrier coarser than the class is blind.** The act 35 product test is blind to the
   whole `u₂` direction — `B = [a = 2][d = 1]` cancels on every same-row-block, same-column-in-block
   four-cycle — which is exactly the direction separating the face `u₂ = 1` from the absent face
   `u₂ = −1`. The stratum and hull predicates are single-structure or product-aligned conditions,
   strictly smaller than `L` (I1: Diţă status is invariant under all independent relabellings, the
   product stratum is not, per act 35). No repository carrier realizes a *specific* detector such as
   `C+2`, though such monomial detectors exist mathematically.
4. **Scalar summaries cannot detect unless constant on the whole locus** (Lemma T). Any continuous
   real-valued readout of the normalized geometry — a distance, a norm, a scalar cross-ratio
   summary — that differs between two face points is not a detector; the distance to `SIG` is an
   instance with an exhibited collision.
5. **The operationally substantive carriers are not applicable** (Finding N). The repository
   contains no certified map from a static realization into lifts, trajectories, visible families,
   pairs of dilations or operational theories. "No tested carrier separates" is not the result here;
   the result is that the only carriers that separate are lift-space coordinates or `𝒪₁`, and the
   carriers that would give a separation multi-time operational meaning are not defined on these
   objects.

None of this changes act 40's verdict, and none of it adopts a carrier, a map or a locus.

## 6. Gem-finding record (§A.31)

Productivity test fixed with the rule: a gem must be strictly stronger than the restatement "Diţă
status is a class property" and constrain something or expose an assumption.

| node | branch | check | verdict | class |
| --- | --- | --- | --- | --- |
| 1 | Is any applicable probabilities-only carrier non-constant on flat unitaries? | I4 | no | CONFIRMING |
| 2 | Is the two-sided gauge the Hadamard diagonal equivalence? | I2 | yes, only because `|A| = 1` | NEW, minor (assumption-watch AW-\|A\|=1) |
| 3 | Do the class-level carriers detect, and specifically? | Lemma M, `Λ = ℤ³` | detect, by completeness only | ELABORATING |
| 3a | favorable branch, pressure-tested: is the detection Diţă-specific? | same lattice; explicit formula read against I1 | no — a coordinate readout | POSITIVE (the obvious reading survives, no overclaim) |
| 4 | Does any named coarse invariant detect? | act 12, act 35, stratum, hulls, distance | act 12 injective on the family; the rest blind; act 35 blind exactly on `u₂` | NEW (the product test cannot see the present/absent-face distinction) |
| 5 | Can a scalar geometric summary detect? | Lemma T + exhibited collision | only if constant on the connected locus | NEW (constraint on any scalar detector) |
| 6 | Is there a certified map to the multi-time carriers? | inventory | none | NEW (AW-static) |
| 7 | Does the kernel's A40 only-if carry the BLIND verdicts? | §9 certificate | no — off-face status re-certified independently at every collision point | POSITIVE |

Passes 3a, 4 and 7 produced no further NEW item on a repeat pass; the walk stops.

## 7. Theorem-shaped statements for a future native round

Kernel-ready, small:
- **K1.** For every flat unitary `H` at the product configuration, `readback 0 (‖pad H‖²) = Γ₀ ⊗ Γ₀`
  and every admissible readback returns `Γ₀ ⊗ Γ₀` on `‖pad H‖²`. (Definitions plus A35.)
- **K2.** `u ↦ featureVec(G(H3 u))` is injective on the three-torus, through the three coordinates of
  §4, each a product of six entries evaluated as a monomial — the A40-2 technique.
- **K3.** Every act 35 cross coordinate of `H3` is independent of `u₂`, and the exhibited pair has
  equal coordinates. The BLIND verdict then needs the off-face status of `(v₁, v̄₄³, v₃)`, which is
  probe-grade (A40's only-if, or §9's certificate): a kernel-plus-probe split.
- **K4.** The single-slice two-sided relation at `|A| = 1` is diagonal equivalence (I2).
- **K5.** Lemma T for `L`, from preconnectedness of the union of the five faces and density of its
  complement.

Kernel-feasible, larger: **K6**, relaxed Diţă status factors through the product normalized set.
It needs a Lean definition of Diţă status over every shape, index map and orientation up to
`D₁ · _ · D₂` — the repository has only strict forms at named maps — and then composes I3.

Probe-grade: the distance collision (`16⁶` coordinates through the exponent distribution) and the §9
non-Diţă certificates.

The question with the most leverage is not among these: whether a map from static realizations into
lifts or visible families can be *sourced* (AW-static), and, separately, whether the Diţă locus is
invariant under every surjective isometry of the product normalized set, whose isometries act 34
leaves unclassified. The second decides whether Diţă status is intrinsic to the normalized geometry.
Both are open.

## 8. Caveats

- The probe is research code, not frozen and not run in CI; its exact claims are reproducible
  locally.
- The strict and relaxed loci of `H3` coincide by act 40's probe layer; the kernel has only strict
  forms at twenty named maps.
- The explicit detector formula and every lattice statement are about `H3` only. The class-level
  statements (I3, the flat column) hold for every flat unitary at the product configuration; the act
  12 cross invariant's behaviour off the family is not determined.
- The distance carrier depends on the choice of `SIG` as reference; Lemma T applies to every
  continuous scalar carrier whatever its reference.
- An `𝒪₁` separation is a separation under act 14's recorded presupposition, and a lift-space
  separation is a statement about coordinates the repository does not treat as physical.
