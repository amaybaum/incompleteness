# NOTES-E9 — the Level III converse: its exact statement, its countermodels, its repair at one finite level

Base L = `9f9f8257`. Evidence: [K] kernel at L; [D] design module `research/equivalence/lean/EqvLevel3.lean` (branch
`dev-equivalence/split-l3`, commit `8c92343e`, run 38091534622 — see §6 for its measured result); [X]
`experiments/e9_level3.py` (7/7) and `experiments/e9_dyn_finite.py` (3/3); [W] written here; [L] literature inputs
named, not checked here.

**Productivity test (fixed before the probes, §A.31).** A finding counts only if it is strictly stronger than "Level III
is a uniqueness, not an iff" (NOTES-E6 §3, HINF-REVIEW point 4) and either (a) gives an exact countermodel to a stated
converse, (b) proves a stated converse at a finite level, or (c) names a hypothesis whose addition turns a false converse
into a true one, with the false and true forms both checked.

## 1. What Level III proves, and what "the converse" could mean

Proved at L [K]: the target class `QuasilocalSystem ι Q` (QuasilocalCharacterization.lean:168) is a C*-algebra with,
for every finite region Λ, an injective unital star homomorphism `st Λ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ →⋆ₐ[ℂ] A`,
compatible along `inclObs` (`X ↦ X ⊗ 1`), with commuting disjoint regions and dense union. `oiSystem` (:187) is a member;
`canon_unique` (:359) makes the canonical map the unique continuous stage-compatible map; `systemEquiv` (:369) makes any
two members canonically isomorphic; Target A systems (`OISystem` :463) carry an automorphism acting on stages as
`st (hat Φ Λ) ∘ transported Φ Λ` for a `ReversibleDynamics Φ` (QuasilocalAlgebra.lean:956: a bijection of global
configurations with finite range both ways); `systemEquiv_dyn` (:497) intertwines two Target A systems with one `Φ`.
Target B: `phaseEquiv i₀` is a locality-preserving star automorphism of the OI completion (`phase_localityPreserving`
:769) different from every `heisQ Φ` (`phaseQ_ne_heisQ` :792).

"The OI_Q conditions follow from the existence of a quasilocal system carrying the stages and dynamics" has three exact
readings, which this node separates. The OI_Q conditions are: (O1) per finite region the operational theory satisfies
OI⁺ (equivalently exact finite QM, `oiPlus_iff_qm` CarrierGeneralOIPlus.lean:207); (O2) the stages are the matrix
algebras of the substratum's configurations with `X ↦ X ⊗ 1` inclusions, one site type `Q`; (O3) the dynamics is the
transport of a reversible finite-range configuration map.

### (C-REG) the per-region converse relative to the class — TRUE, by transfer along the stage map

```lean
theorem kraus_iff_of_member (S : QuasilocalSystem ι Q) {n : ℕ} (Λ : Finset ι)
    (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    (∑ k, star (S.st Λ (K k)) * S.st Λ (K k) = 1) ↔ ∑ k, (K k)ᴴ * K k = 1      -- [D], EqvLevel3 §C
```

For every member and every region, the finite-support instrument families supported on Λ (elements of `range (S.st Λ)`
with the instrument normalization) are exactly the Kraus families of `Matrix (Conf Λ Q)`: the landed Q1 of the instrument
audit (`finiteSupport_iff_kraus`, InstrumentCompletion.lean:195, for the OI completion) holds for **every** member,
because only injectivity and the star-homomorphism property of `st Λ` are used. With `oiPlus_of_qm`
(CarrierGeneralOIPlus.lean:198) for any finite operational theory on `Conf Λ Q` whose instruments are exactly the
Kraus instruments, (O1) holds at every region of every member [W: the interface definition building that theory from a
member is not written in the kernel; NOTES-E6 §3]. **Reading:** (O1) follows from membership — and it follows *because*
the class contains (O2) in its definition. This is the iff "between two descriptions that both carry the quantum
kinematics" of NOTES-E6 §3, now with its region-level step a theorem in a design run. Label: CONJECTURE ([D] pending
§6; [W] for the OI⁺ link).

### (C-DYN) the naive dynamical converse — FALSE

```lean
def NaiveConverseDyn (ι Q) … : Prop :=
  ∀ (S : QuasilocalSystem ι Q) (α : S.A ≃⋆ₐ[ℂ] S.A), LocalityPreserving S α →
    ∃ Φ : ReversibleDynamics ι Q, ∀ Λ X, α (S.st Λ X) = S.st (hat Φ Λ) (transported Φ Λ X)
theorem phase_not_oiInduced [Nontrivial Q] (i₀ : ι) (Φ : ReversibleDynamics ι Q) :
    ¬ ∀ Λ X, phaseEquiv i₀ (stage Λ X) = stage (hat Φ Λ) (transported Φ Λ X)      -- [D], EqvLevel3 §A
theorem not_naiveConverseDyn [Nontrivial Q] (i₀ : ι) : ¬ NaiveConverseDyn ι Q    -- [D]
```

The countermodel is the kernel's own Target B witness: (oiSystem, phaseEquiv i₀) is a quasilocal system with a
locality-preserving dynamics that does not arise from OI_Q dynamics. The kernel at L already proves the automorphism-level
statement (`phaseQ_ne_heisQ` :792 with `phase_localityPreserving` :769) — CERTIFIED [K at L] as a statement about
automorphisms of the quasilocal algebra; the stage-level form above (no Φ reproduces it on the stages) follows by
continuity and density (`canon_unique`'s argument) and is [D]. **At the finite-stage level** the obstruction is on one
single-site matrix unit: the phase stage map sends `E_01` to `i·E_01`, while every permutation transport of `E_01 ⊗ 1`
has entries in {0, 1} (`e9_level3` P1 [X]). It is not about complex phases: conjugation by `Z = diag(1, −1)` at one
site is real, preserves the configuration (diagonal) algebra, is compatible with `X ↦ X ⊗ 1`, preserves locality, and
sends `E_01` to `−E_01`, which no permutation transport produces (P2 [X]). So neither reality nor diagonal preservation
is the missing hypothesis.

### (C-KIN) the naive kinematic converse — FALSE

Stated over an abstract net (not in the kernel):

```lean
structure QuasilocalNet (ι : Type) where          -- CANDIDATE vocabulary, not in the kernel
  A : Type
  [inst : CStarAlgebra A]
  loc : Finset ι → StarSubalgebra ℂ A
  mono : ∀ {Λ Λ'}, Λ ⊆ Λ' → loc Λ ≤ loc Λ'
  local_comm : ∀ Λ Λ', Disjoint Λ Λ' → ∀ a ∈ loc Λ, ∀ b ∈ loc Λ', a * b = b * a
  finiteDim : ∀ Λ, FiniteDimensional ℂ (loc Λ)
  dense : closure (⋃ Λ, (loc Λ : Set A)) = Set.univ
-- naive converse: every net is presented by some QuasilocalSystem ι Q with range (st Λ) = loc Λ.
```

False, with exact finite-stage countermodels:
- **K1, the classical lattice** (`e9_level3` K1 [X]): the diagonal algebras (functions of configurations) form an isotone,
  commuting, generating net with a locality-preserving automorphism (the site swap; any classical reversible cellular
  automaton). No member of `QuasilocalSystem ι Q` with `|Q| ≥ 2` has a commutative algebra: `not_comm_of_system` [D,
  EqvLevel3 §B] (injectivity of `st {i₀}` and `[E_01, E_10] = diag(1, −1) ≠ 0`); for `|Q| = 1` every stage is `ℂ` and the
  dense union is `ℂ·1`, which is not the classical algebra of two or more states. So the classical lattice is a
  quasilocal system carrying stages and a dynamics that does not arise from OI_Q stages.
- **K3, non-uniform sites** ([X]): a qubit site beside a qutrit site gives single-site stage dimensions 4 and 9; every
  member has `|Q|²` at every site. (Presented as one 6-level site it is a member, but with different regions.)
- **K2, graded locality** ([X], a boundary case, not a counterexample to a commuting net): the Jordan–Wigner two-site
  net satisfies the CAR exactly, its site algebras are `M_2` and generate `M_4`, and `a0 a1 = −a1 a0`, so it fails
  `local_comm` (its even parts commute). The physically standard fermionic quasilocal system is therefore not a member
  with its own regions; `local_comm` is a real restriction of the class.

## 2. The missing hypotheses, and the converse at one finite level

| reading | missing hypothesis | with it, at a finite level | evidence |
| --- | --- | --- | --- |
| (C-KIN) | **H-FAC**: each single-site algebra is a full matrix algebra (a factor) | — | excludes K1 |
| (C-KIN) | **H-UNIF**: one site dimension | — | excludes K3 |
| (C-KIN) | **H-GEN**: each region's algebra is generated by its site algebras | with H-FAC, H-UNIF and `local_comm`, `loc Λ ≅ ⊗_{i∈Λ} M_q = Matrix (Conf Λ Q)` compatibly with inclusions | [L] the tensor-product theorem for commuting finite-dimensional factors; instance T1 [X] (twisted commuting copies of `M_2` in `M_4`: commute, unital, multiplicative, rank 16); commutation load-bearing: T2 [X] (the fermionic copies span `M_4` but the multiplication map is not multiplicative, the two sides differ by a sign) |
| (C-DYN) | **H-DYN**: the automorphism maps each stage matrix unit to a stage matrix unit | at finite `ι`: H-DYN ⟺ the automorphism is conjugation by a configuration permutation, i.e. OI-induced (finite range is automatic on a finite lattice) | [W] (Skolem–Noether; minimal projections to diagonal units; phases forced equal); exhaustive monomial instance at `N = 4` over fourth-root phases: `e9_dyn_finite` M1–M3 [X] (6144 cases; exactly the 24 permutation conjugations satisfy H-DYN; a rational Householder conjugation violates it on all 16 units) |

So the converse at one finite level is **true relative to H-FAC, H-UNIF, H-GEN (kinematics) and H-DYN (dynamics)**
([W] + [L] + exact instances), and false without them (K1, K3; P1, P2). The decisive missing hypothesis is H-FAC: it is
the quantum kinematics at the site level, the content of the K row (LEDGER Part A). H-UNIF and H-GEN are structural;
H-DYN restates (O3) on the stages (a dynamics permuting configurations), and Target B shows locality preservation does not
supply it. For infinite `ι`, the passage from H-DYN on every finite stage to a global configuration bijection with finite
range is not attempted here (OPEN).

**What the converse cannot be.** A Level III "iff" whose right-hand side is membership of `QuasilocalSystem` gives (O1) by
(C-REG) and nothing about the kinematics, because (O2) is in the class's definition. An "iff" whose right-hand side is an
abstract quasilocal net is false without H-FAC, and with H-FAC it derives (O2) from (O2)'s site-level form. Either way
the converse moves no kinematics; the scope-correct Level III statement of NOTES-E6 §3 stands, now with its converse
bounded on both sides: (C-REG) holds, (C-DYN) and (C-KIN) fail with exact finite countermodels, and the repaired forms
name exactly what is assumed.

## 3. Pressure test (§A.31; the favourable reading is "the converse holds")

- (C-REG) is favourable to the framework and is applied maximum skepticism: its truth is entirely a property of the
  class's definition (an injective unital star homomorphism transfers Kraus normalization both ways); it would hold for
  any C*-algebra receiving those stages. It is recorded as a transfer lemma, not as evidence for OI.
- The tensor-product step (H-FAC + H-GEN + commutation ⇒ tensor form) is literature [L], checked on one twisted
  instance; the instance cannot certify the general theorem, and the round that would land it must use a kernel proof
  or cite the theorem as an input.
- The dynamics repair H-DYN is close to restating (O3); the finding is that the obvious weaker candidates (reality,
  diagonal preservation, locality preservation) each fail (P1, P2 and Target B).

## 4. Classification (§A.31)

- **NEW** (scoped): the separation of the three readings of the Level III converse with an exact countermodel to each
  false one at the finite-stage level (classical lattice K1, sign automorphism P2 — P1 being the landed Target B witness
  read at one stage), and the identification of the repairing hypotheses H-FAC, H-UNIF, H-GEN, H-DYN with H-FAC as the
  kinematic content. Strictly stronger than "uniqueness, not iff": it says which iff is true (C-REG), which are false
  (C-DYN, C-KIN), and what each false one lacks.
- **CONFIRMING**: NOTES-E6 §3 and HINF-REVIEW point 4 (the matrix stages are in the class's definition).
- Assumption-watch marker (cross-propagation): any manuscript or ROADMAP sentence reading Level III as "OI_Q ⟺
  quasilocal lattice QM" must name its right-hand side; with an abstract net it is false (K1), with the target class it
  is (C-REG) and carries the kinematics in the premise.

## 5. Not decided here

The infinite-volume passage from H-DYN to a global finite-range configuration bijection; a kernel proof of the
tensor-product step; the interface definition building a `FiniteOperationalTheory (Conf Λ Q)` from a member.

## 6. Design run of `EqvLevel3` (run 38091534622)

Recorded in LOG and RESULTS when measured.
