# NOTES-E14 — the infinite-volume passage from H-DYN at every finite stage to a global finite-range configuration bijection

Base L = `9f9f8257`. Source of the question: NOTES-E9 §2 and §5 (H-DYN, "the automorphism maps every stage matrix unit
to a stage matrix unit", gives at a finite lattice exactly the conjugations by configuration permutations, R-E9.4; the
passage to infinite `ι` was left OPEN). Kernel objects at L: `QuasilocalSystem` (QuasilocalCharacterization.lean:168),
`OISystem` (Target A, :463: `α (st Λ X) = st (hat Φ Λ) (transported Φ Λ X)`), `LocalityPreserving` (:475),
`phaseQ_ne_heisQ` (:792); `CouplingGraph` (RegionTower.lean:254), `FiniteRange` (QuasilocalAlgebra.lean:919: a finite
dependence neighbourhood and a finite influence set per site — no metric), `ReversibleDynamics` (:956: a configuration
bijection with `FiniteRange` both ways), `hat` (:1040), `transported` (:1109).

## S0 (written 2026-10-11T01:29Z, before the probe)

**Productivity test (§A.31, fixed now).** A finding counts if it (a) proves the passage under a hypothesis that OI's own
Target A systems satisfy, or (b) shows that a reading of "H-DYN at every finite stage" is false for OI's own dynamics or
does not glue, with an exact finite instance, and names the reading that works; a mere restatement of NOTES-E9 §5's gap
is a non-gem.

**Analysis before computation (written).** "H-DYN at every finite stage" has three readings in infinite volume.
- *(R-lit) the literal one*: `α` maps every matrix unit `E^Λ_{c,c'}` of every finite stage to a matrix unit of some finite
  stage. Claim: then `α` maps each single-site stage onto a single-site stage by a relabeling of `Q`, the induced site
  map is a bijection, and `α` is a site permutation composed with on-site relabelings. Proof sketch: the unique tracial
  state is `α`-invariant, so the image of a unit of `M_Λ` is a unit of a stage of the same size; the images of the
  orthogonal projections `E^{i}_{a,a}` are pairwise orthogonal single-site projections, and single-site projections at
  two different sites have a non-zero product, so all lie at one site `π(i)`; the off-diagonal units follow; `π` is onto
  because `α` is. So (R-lit) gives a global configuration bijection, but it excludes every interacting reversible
  dynamics: OI's own Target A systems (e.g. the CNOT update) violate it. On a metric lattice it does not give a bounded
  range either (the reflection `i ↦ −i` of `ℤ` satisfies it).
- *(R-01) the transport reading*: `α` and `α⁻¹` map every matrix unit of every finite stage to a matrix with entries in
  `{0, 1}` in the configuration basis of some finite stage, and both are `LocalityPreserving`. Claim (the passage, written
  proof): then `α` is the Target A automorphism of a `ReversibleDynamics` (up to the canonical isomorphism). Sketch: a
  self-adjoint idempotent `{0,1}`-matrix is diagonal (its diagonal entry is its row count), so `α(D) = D` for the
  diagonal subalgebra `D ≅ C(Q^ι)`; Gelfand duality gives a homeomorphism `G` of `Q^ι` with `α|_D = (· ∘ G)`; a
  `{0,1}` partial isometry `V = α(E^Λ_{c,c'})` satisfies `V α(f) V* = α(E f E*)` for diagonal `f`, which forces
  `V` to implement `G⁻¹ τ G` (`τ` the substitution `c' → c` on Λ) with no phase; `V ∈ M_{Λ'}` makes that substitution
  local, so `G` preserves finite differences; continuity on the compact `Q^ι` gives each output site a finite
  dependence set, and `LocalityPreserving` for `α` and `α⁻¹` gives finite influence sets — `FiniteRange` both ways.
  This reading includes every Target A system (the transported matrix of a matrix unit is a `{0,1}`-matrix) and
  excludes the phase automorphism (`phaseQ_ne_heisQ`).
- *(R-ring) a family of finite-volume dynamics* (rings of `N` sites) from one uniform finite-range rule: a configuration
  permutation on *every* ring iff the rule is a reversible cellular automaton on `Q^ℤ` (one dimension: injectivity on
  periodic points implies injectivity, by the pair-graph argument [L: Hedlund 1969; Amoroso–Patt 1972]); on *some* rings
  is not enough.

**Predictions for `experiments/e14_hdyn_rings.py`.** Ring of 3 qubits, all 8! = 40320 configuration permutations: (R-lit)
holds for exactly 48 = 3!·2³, the site permutations with relabelings; the top-stage H-DYN of NOTES-E9 and (R-01) hold
for all 40320. Ring of 4: the 384 site-permutation-relabelings satisfy (R-lit); the CNOT on sites (0, 1) satisfies the
top-stage H-DYN and (R-01) at every stage and violates (R-lit) (the image of `E^{0}_{0,1}` is a two-site operator); the
two-site shift `T²` (translation by two sites) satisfies all three on both rings (control). The rule `x_i ⊕ x_{i+1} ⊕
x_{i+2}` is a permutation on the ring of 4 and not on the ring of 3, and on `ℤ` the configurations `(110)^∞` and `0^∞`
have the same image; its pair graph has a cycle through a non-diagonal vertex, `T²`'s has none. Countercontrols fail as
stated: a 3-cycle on three configurations passes (R-lit); the phase automorphism `diag(i^{x_0})` passes (R-01).

**Prediction for the node.** Outcome (a)+(b): (R-lit) is the wrong infinite-volume form of H-DYN (it excludes OI's
own interacting dynamics); (R-01) gives the passage (CONJECTURE, written proof); (R-ring) holds on every ring and fails
on some rings.

## 1. Measurement (probe run 1)

`experiments/e14_hdyn_rings.py` run 1 (started 01:30:40Z, after commit `3c10fb14`): 7/7, `COUNTER XR1 fails as stated`,
`COUNTER XR2 fails as stated` (first unit with a phase: `E^{0}_{0,1}`), `VERDICT E14-HDYN-READINGS-SEPARATED`; replay
byte-identical (py `1db6a11b…`, out `cfd9aa1f…`). Ring of 3, exhaustively: (R-lit) holds for exactly 48 of the 40320
configuration permutations, the site permutations with relabelings; NOTES-E9's top-stage H-DYN holds for all 40320.
Ring of 4: the 384 site permutations with relabelings satisfy (R-lit) on all 624 units. The CNOT update (rings of 3
and 4) satisfies the top-stage H-DYN and (R-01) at every stage and violates (R-lit): the image of `E^{0}_{0,1}` has
4 (resp. 8) pairs, each also flipping site 1. The two-site shift `T²` satisfies all three readings on both rings and
carries site-0 units to site-2 units. The rule `x_i + x_{i+1} + x_{i+2}` is a permutation on the ring of 4 (16
images), not on the ring of 3 (2 images); `(110)^∞` and `0^∞` collide on `ℤ`; its pair graph has a cycle through a
non-diagonal vertex, `T²`'s has none. (That (R-01) holds for every configuration permutation needs no run: conjugation
by a permutation keeps every entry in `{0, 1}`.) Every S0 prediction held.

## 2. The three readings (written arguments, checked against the instances)

- **(R-lit) collapses to site permutations.** For a star automorphism `α` of a `QuasilocalSystem` (any `ι`, `|Q| ≥ 2`)
  sending every matrix unit of every finite stage to a matrix unit of some finite stage: the unique tracial state is
  `α`-invariant, so a unit of `M_Λ` goes to a unit of a stage of size `|Λ|`; the `E^{i}_{a,a}` go to pairwise orthogonal
  single-site projections, which must sit at one site (projections at two sites have non-zero product); the off-diagonal
  units follow (`E_{ab} = E_{aa}E_{ab}E_{bb}`); the site map is injective and, `α` being onto, surjective. So `α` is a
  site permutation with on-site relabelings — exactly the 48 of R1 at `N = 3`. It is a global configuration bijection, but
  (i) it excludes OI's own interacting dynamics (R4: the CNOT update is a `ReversibleDynamics` whose Target A
  automorphism violates (R-lit)), and (ii) on a metric lattice it does not bound the range (the reflection of `ℤ`).
  **So "H-DYN at every finite stage", read literally, is the wrong infinite-volume form of H-DYN**; NOTES-E9's H-DYN is a
  top-stage condition, and an infinite lattice has no top stage.
- **(R-01) gives the passage** (CONJECTURE, written proof). Hypotheses: `α` maps every stage matrix unit to a stage
  matrix with entries in `{0, 1}` in the configuration basis, and `α`, `α⁻¹` are `LocalityPreserving` (:475). Steps:
  (1) a self-adjoint idempotent `{0,1}`-matrix is diagonal (its diagonal entry equals its row count), so `α` maps the
  diagonal subalgebra `D` into itself, and onto it because `α(D)` is maximal abelian inside the abelian `D` (`D` is a
  maximal abelian subalgebra [L]); (2) `D ≅ C(Q^ι)` and Gelfand duality give a homeomorphism `G` of `Q^ι` with
  `α(f) = f ∘ G` on `D`; (3) a `{0,1}` partial isometry has at most one `1` in each row and column, so `α(E^Λ_{c,c'})`
  implements a partial bijection of `Conf Λ'`, and `V α(f) V* = α(E f E*)` for `f ∈ D` forces it to be `G⁻¹τG` with `τ`
  the substitution `c' → c` on Λ, with no phase; (4) `α` therefore agrees with the transport along `G` on every stage unit,
  hence everywhere; `G` changes finitely many coordinates when its argument does (the partial bijection lives in a finite
  stage); (5) each output coordinate of `G` and of `G⁻¹` depends on finitely many input coordinates (continuity on the
  compact `Q^ι`, or the diagonal half of `LocalityPreserving`), and each input coordinate influences finitely many output
  coordinates (the off-diagonal half of `LocalityPreserving` for `α` and `α⁻¹`): `FiniteRange` (QuasilocalAlgebra.lean:919)
  both ways, i.e. a `ReversibleDynamics` (:956), and `(S, Φ, α)` is an `OISystem` (:463) up to the canonical isomorphism.
  (R-01) holds for every Target A system (`transported` of a matrix unit is a `{0,1}`-matrix, :1109) and fails for the
  phase automorphism of `phaseQ_ne_heisQ` (:792; XR2 on the ring of 3).
- **(R-ring), a finite-volume family from one uniform rule.** A window rule on `Q^ℤ` is a permutation on every ring iff
  it is a reversible cellular automaton: if `F(x) = F(y)`, `x ≠ y`, then either they are asymptotic (excluded by the
  Garden-of-Eden theorem, since bijectivity on all rings makes `F` surjective, the periodic points being dense) or a
  non-diagonal vertex of the pair graph recurs, giving distinct periodic preimages of one configuration [W; L: Hedlund
  1969, Amoroso–Patt 1972]; the inverse has finite range by Curtis–Hedlund–Lyndon [L]. Permutation on *some* rings is not
  enough (R6, R7: bijective on the ring of 4, not on the ring of 3, not injective on `ℤ`).

## 3. Outcome (§A.31)

- Productivity test met: (b) with an exact instance — the literal reading of "H-DYN at every finite stage" is false for
  OI's own dynamics (R4) and collapses to site permutations (R1, exhaustively at `N = 3`); (a) the reading that works,
  (R-01), carries the passage to a `ReversibleDynamics` by a written proof whose hypotheses every Target A system meets.
  **NEW** (scoped): the infinite-volume form of H-DYN is the `{0,1}` (transport) condition, not the matrix-unit
  condition, and with locality preservation of `α` and `α⁻¹` it yields the global finite-range configuration bijection.
- Skepticism on the favourable branch (R-01): its strength is that of NOTES-E9's H-DYN — it restates (O3) on the stages
  in operator language (a dynamics permuting configurations), so it repairs the converse without deriving the
  dynamics; the written proof uses three standard facts not checked here (the diagonal is maximal abelian; Gelfand
  duality for `C(Q^ι)`; the identification with the kernel's `transported` through the canonical isomorphism).
- Not decided: a kernel proof of (R-01)'s passage; whether `LocalityPreserving` of `α` alone (without `α⁻¹`) suffices.
