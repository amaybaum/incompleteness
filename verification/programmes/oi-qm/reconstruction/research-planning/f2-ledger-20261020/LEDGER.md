# F2-reg dependency ledger, a three-token countermodel test, and the first premise to attack

Research only, consistency axis (§A.23). No premise is adopted, no status changes, no round, F or E, no repository
write. Nothing here is a theorem of the kernel; new mathematics is tagged [W] (written) or [EC] (exact computation,
replayed twice byte-identical).

**Base.** `main` at `ec49d0b41648d8a070179c8fa3aaf20b5c6ff863` (kernel and papers; every [AT] name below was confirmed
by `git grep` of its declaration at this commit, with the `file:line` given). F2 decision memo at `acfef447` (MEMO).
#864 branch `research/x-screen-20261018` at `dcbcae42` (XS: `REPORT.md`; MI+: `mi-plus/`; SC:
`source-search-20261020/SOURCE-CHECKPOINT.md`; thread I: `x-screen-20261018/src/I.md`, a copy of thread I at
`804843f1`). Issues #865–#872, #875. ROADMAP lines (RM:n) and PROGRAMME lines (PG:n) are at `ec49d0b4`. Lean paths are
under `verification/lean-mathlib/OIBridge/`.

**Classes used in the ledger.**
- **(a)** proved in Lean on main: module and theorem, grep-confirmed.
- **(b)** proved conditionally on named hypotheses: the hypotheses are named, and the evidence level is given ([AT]
  conditional, [CD] compiled design not adopted, [W] written, [EC] exact).
- **(c)** supplied by OI itself: a posit or derivation, cited.
- **(d)** open or unsourced.

***

## 1. The target and the frame

F2-reg is the owner-adopted target (MEMO §0 (a), §1.1–1.2): exact (A1) finite operational QM on qubit-power registers
(B1), under the strict criterion and gates G1–G8 (MEMO §2.3), with the monitored law kept on retained protocols (M1).
In thread I's form: `OIStated ∧ Origin ∧ X ∧ Res ⟹ QMfin` with (T6) restricted to local dimension 2^k (I:§1.2–1.4).
The F2 row names the K chain as the assembly route (RM:1130–1132), so the ledger is written for Origin_K; R14 of
thread I records which rows collapse under Origin_M, where the complex matrix kinematics is inherited rather than
derived (I:§4 R14, AW-I4).

***

## 2. The ledger

### 2.0 What OI supplies (class (c), and the barrier)

| id | premise / fact | class | citation |
|---|---|---|---|
| OI-1 | finite visible configuration space; the observer is a proper subsystem; bijective substratum dynamics (Lemmas 1–3) | (c) | `papers/Main.md`:44–56; posit ledger :708 |
| OI-2 | hidden-sector conditions C1–C4 (diagnostics; C4 primitive) | (c) | Main.md:74–80; (C4) primitive :604 |
| OI-3 | the sourced operation class: scaled partial permutations; every permutation of the configuration carrier; the native read-write coupling (CNOT) | (a) | `permClass` SubstratumInterfaceAudit.lean:236; `permClass_permMatrix` :406; `permClass_readWrite` :412; `dict_cnot` BridgeDictionary.lean:71; `obsTheory_eq_permTheory` SubstratumInterfaceAudit.lean:774 |
| OI-4 | native readout is the local Lüders instrument in the configuration basis; reset/attach of a configuration state; discard | (a) | `readout_is_localLuders` OperationalAssembly.lean:658; `instAvail_reset` BridgeFiniteProtocol.lean:111; `pureSeedPrep_available_of_swap` OperationalAssembly.lean:675; `ptraceAnc` :453 |
| OI-5 | the rooted visible class is exactly `PPer` at finite carriers | (a) | `finiteRootedRealizable_iff_pper` RootedClassificationAllTime.lean:192; PG:187–195 (Arc B) |
| OI-6 | the barrier: every observer-theory operation preserves entrywise nonnegativity, so no phases, no `DerivedOI`, no dense unitary control on `Fin 2`; the update rule adds no availability | (a) | `obsTheory_nonnegBounded` FrozenSourcing.lean:84; `frozen_sourcing_verdict` :318; `nonnegBounded_verdict` :327; `sourcing_rule_independent` :295; `obsTheory_rule_independent` SubstratumInterfaceAudit.lean:779 |
| OI-7 | the sourced theory is not QM; relative to `SourcedOI`, QM ⟺ one continuously driven pair per level | (a) | `permTheory_sourcedOI` SubstratumInterfaceAudit.lean:660; `permTheory_not_qm` :716; `permTheory_not_phaseFree` :711; `sourcedOI_qm_iff_phaseFree` :654 (both directions in one iff, relative to `SourcedOI`). `PhaseFreeRichness` (MinimalRepertoire.lean:423) also requires every swap, a conjunct supplied under `SourcedOI` |
| OI-8 | the monomial class (complex scalars allowed) is closed under all four closures and is not QM | (a) | `substratum_residual` StructuralClosure.lean:383 |

### 2.1 K∞ — the single elementary system

| id | premise | class | citation / status |
|---|---|---|---|
| K∞-Stage | `SCInf`, `FiniteRank`, `BinaryVisible`, elementary scope | (d) | `SCInf` StageCompletion.lean:78 (introduced); no predicate for the elementary scope (RM:1023–1026); thread I H1–H4 |
| K∞-Act | `OpDatum` with `AffineRespect` and an inverse | (d); its consequence (b) | `preservesBody_inducedEquiv` CompletionAction.lean:352 [AT, conditional]; label-dual route #871 [W] |
| K∞-Drive | `ElementaryDrivability` | (d); no chain consumer | KInfFoundations.lean:264; QM satisfies it `ball3_drivable` :490; finite-orbit bodies have none `isEmpty_drivability_of_finite_orbits` OrbitNormalization.lean:124; #865 |
| K∞-Trans | `BoundaryTransitive` (the transporting group) | **(d), crosses the barrier** | OrbitGeneration.lean:79; exact form needs an uncountable group `not_boundaryTransitive_of_countable` EffectSpace.lean:858; not implied by a drive `not_boundaryTransitive_flow` OrbitGeneration.lean:620 |
| K∞-Seed | `SharpSeed` | (b) | `sharpSeed_completion` StageCompletion.lean:224 (from SC∞ and one sharp stage effect, which OI supplies as a configuration readout: OI-4) |
| K∞-V4 | `SeedOrbitAvailable` | (d) | OrbitGeneration.lean:74 |
| K∞-Copy | identical copies' NOTs agree (or type covariance) | (c) through H-CAR and `LabelInvariant` [W, I:H16]; type-covariance form (b) [CD #822] | `CopyNatural` KInfFoundations.lean:284; d = 5 countermodels without it (NB-1, RM:1010) |
| K∞-Geom | sharp-update / singleton faces | (d); no consumer in the chain | `SingletonFaces` KInfFoundations.lean:139; false for QM at level ≥ 3 (RM:1058–1062); #867 |
| ball and effects | the cone of available token tests is `maxCone (eball d)`; all affine effects available | (b) on effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, and for `avail_eq_fullEffects` also `hU` (unit effect) and `hM` (mixing-closed) | `maxConeOf_avail_eq` EffectSpace.lean:572; `avail_eq_fullEffects` :727; `sharpFamily_subset_avail` :374 |
| K1 | d ∈ {1,3}; d = 3 with an entangling gate | (b) on `0 < d`, effect soundness, the four K∞ hypotheses, `IsNot`, `NativeGateOf`, `EntanglingOf` | `dim_of_nativeGateOf` K1Bridge.lean:128; `three_of_nativeGateOf` :138; CNOT instances `nativeGate_cnot` CompositeDimension.lean:1160, `entangling_cnot` :1380 (the gate is OI's, OI-3) |

### 2.2 K2 — the pair

| id | premise of `pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153) | class | status |
|---|---|---|---|
| H-CAR / LT | the pair is `W 3` through the Pauli dictionary; local tomography | (d), RES | `Composite.lt` introduced; LT independent of the other composite fields `not_locallyTomographic_paddedBall3` CompositeInterface.lean:912 |
| hH1 | products of all `eball 3` states are states | (d) | non-basis token states need a non-monomial resource (I:H20); the four basis products are OI-4 |
| hadd, hsmul | convex cone | (d), RES | classical mixing; load-bearing (I:H21) |
| hmax | K ⊆ maxCone (product-test validity, X-5) | (d) | `maxCone_bound_of_sharp_available` EqvK2MaxCone.lean:194 (premises `hvalid`, `hsharp`); `hsharp` is (b) via `sharpFamily_subset_avail` |
| hH2 | CNOT preserves K (PC, part of X-4) | (d) | the operation is OI-3; its preservation of K is unsourced (XS C13; MI+ C0/C8) |
| hA-drive | the `rotLin` flow on the target token preserves K | (d), and the operation itself crosses the barrier | `Q3_aMiss` EqvK2Converse.lean:174 (QM satisfies it); #865 |
| hA-cyc | `cycEquiv` on the target token preserves K | (d) | kept separate from the drive (MEMO App. A.1) |
| conclusion | K = Q3 ⟺ hH2 ∧ hA, given hH1, hadd, hsmul, hmax | (a), with one witness per direction | `pairCone_eq_Q3_iff_drive_maxCone` :174 from `pairCone_eq_Q3_of_drive_maxCone` :153 and `driveInvariant_of_eq_Q3` :165 |
| **re-expression** | native three-token premises Σ3 in place of hH2 ∧ hA (§4) | (b) [W + EC]; at the pair, given the domain, equivalent to K₂ = Q3 and hence to hH2 ∧ hA | this ledger §3, §4; not formalized |

### 2.3 Kₙ — registers of every size 2^k

| id | premise | class | status |
|---|---|---|---|
| k-token cone | K = QK k ⟺ CNOTs into later tokens ∧ drive/cyc off token 0, given products, cone, maxConeK | (b) [CD #829] | not on main (MEMO §5.1) |
| REG | register consistency: attach a configuration meter (ρ ↦ ρ⊗\|0⟩⟨0\|) and discard map register cones into each other (H25/FCC) | (d) | no predicate (I:H25); four-copy coherence #869/#870 is a different, stronger condition |
| hpow / synthesis | `DrivesElementaryAt (Fin 2^k)` from token flows, CNOT and closure | (b) [W+L; CD partial] | I:Γ3; KN-DESC `drivesElementary_of_pow` [CD #823] |
| H26 | types of size ≠ 2^k | out of scope for F2-reg | I:Γ11 |

### 2.4 State–operation compatibility, tests, drive, geometry, evolution

| id | premise | class | status |
|---|---|---|---|
| X-4 H-COMPAT | the available operations preserve the physical cones | (d) | MEMO §2.1; availability does not imply it (`bridge-compatibility-audit/result.md` on main, K_B witness −1/4); preservation induction from primitives (b) [CD #831] |
| X-5 H22v | `prep ⊆ maxConeOf avail` (valid tests on joint states) | (d) | MEMO §2.1; #868 |
| G3 identification | native operations act on coherence-level descriptions by Ad_P (not Γ∘Ad_P∘Γ) | (d) | MEMO Fact B; SC §3.3 item 2; reg3 D5a–D5b |
| X-1 / I5 drive | a continuous non-monomial operation (one driven pair per level suffices relative to `SourcedOI`) | **(d), crosses the barrier** | resource: `sourcedOI_qm_iff_phaseFree` (a); unsourced: OI-6, OI-7; exact A1 needs it uncountable: `countable_not_pairFlowSourced` PairFlowEquivalence.lean:218, `mixTheoryR_not_qm` StateMixingCoupling.lean:679, `fixedGateTheory_not_qm` DiscreteCompletion.lean:1948, `uncountable_of_layerFlowExecutable` PolarizationClosure.lean:135 |
| K3 assembly | quantum architecture ⇒ all finite endomorphic QM; typed endpoint | (a) conditional on `QuantumArchitecture` | `genTheory_qm_of_quantumArchitecture` SubstratumSource.lean:136; `typed_determined_iff` TypedCompletion.lean:850; `finite_protocol_available` BridgeFiniteProtocol.lean:236; typed lift Γ5 has no object (I:Γ5) |
| geometry | elementary scope; K∞-Geom | (d) | §2.1; #867 |
| evolution selection | P0 (trajectory and threading freedom) | (d); outside QMfin's scope (I:§1.2, "Excluded") | #866 |
| H0 / H27 / Origin | the observer's states, tests and operations are those of the extended theory | (d), RES, no predicates | I:H0, H27, Γ13; `ensemble_underdetermined` StochasticInterface.lean:118 |

***

## 3. The open obstruction: two irredundant premises

There are two premises, both unsourced. Each is shown to be needed relative to the rest, by an exact or kernel
countermodel. This shows irredundancy, not minimality among all possible decompositions. The two premises are not
independent either: O-B's native form needs non-configuration token states and tests, and those come from O-A.

**O-A. A continuous non-monomial operation on the elementary system** (X-1 = I5, with its images K∞-Trans/H8 and the
test closure H11b).
- It is consumed three times:
  - for the token ball and its non-configuration effects (§2.1 "ball and effects"), which hH1, H1₃ and MAX₃ need and
    on which every exclusion in §4 rests (reg3 D4c);
  - for (T2), availability of all instruments.
- Countermodels without it: the sourced theory itself (`permTheory_not_qm`, `obsTheory_nonnegBounded`) and the
  monomial class (`substratum_residual`).
- New [W], with an exhaustive [EC] instance (`monomial_branch.py`): making **every** product-state preparation
  available does not remove O-A.
  - In any finite native protocol whose instruments are configuration readouts, every Kraus branch has the form
    ⟨c′|M|α⟩, with M a scaled partial permutation and |α⟩ the ancilla preparation.
  - Each row of such a branch has at most one nonzero entry, and that entry is a single term.
  - So an invertible branch is monomial, a unitary channel has to be monomial, and the Hadamard channel is
    unavailable.
  - In short, coherent preparations do not give coherent control.

**O-B. State–operation compatibility and test validity (X-4, X-5), together with the identification G3.**
- The [AT] pair theorem consumes O-B as hH2 ∧ hA.
- Relative to the domain (hH1, hadd, hsmul, hmax), that conjunction is equivalent to K₂ = Q3
  (`pairCone_eq_Q3_iff_drive_maxCone`).
- §4 gives a second sufficient form, Σ3. Its operations are native: CNOTs into a ready meter, configuration readout,
  attach and discard. Relative to the same domain, the existence of a K₃ satisfying Σ3 is **also equivalent to
  K₂ = Q3**. One direction is §4. For the converse, take K₃ = QK₃.
- Hence Σ3 and hH2 ∧ hA have the same content at the pair. Σ3 re-expresses that content in the vocabulary of native
  operations.
  - Its token states and tests are not native. H1₃ and MAX₃ need complex non-configuration states and tests, which
    come from O-A.
  - It adds an unsourced object, K₃, with its own clauses.
  - In the fixed 8×8 Ad_P carrier, Σ3 is exactly pair PSD, restated as validity of three-token product tests read
    through a parity coupling (§4.5 item 1).
- Countermodel without O-B: K(Z_F) satisfies every pair-level premise (§4.2).
  - With K₃ = cone{X⊗τ : X ∈ K(Z_F), τ a token state} together with the three-token products, it also satisfies H1₃,
    MAX₃, RO₃, ATT and DIS, and fails only NC₃ (§4.4, [W]).
  - Beyond three tokens this has not been checked.

The identification layer (H-CAR, H27, Origin) is needed before anything can be stated, and none of it has a predicate. It is recorded
as RES rather than as an obstruction, because no countermodel separates it.

***

## 4. Decisive investigation: is there a non-quantum pair structure satisfying everything OI sources?

### 4.1 Premise sets checked

- **Σ0 (strictly sourced):** OI-1…OI-8.
  - Physical pair states contain the four basis products.
  - Native operations are the 24 pair permutations, configuration readouts, attach and discard.
  - The native laws are OI's.
- **Σ1 = Σ0 + the pair domain:** hH1, hadd, hsmul, hmax. None of these is sourced; MEMO fixes them as the screening
  domain.
- **Σ2 = Σ1 + pair-level native compatibility:** all 24 native permutations preserve K (PC24 ⊇ hH2), together with
  readout closure, discard and MI.
- **Σ3 = Σ2 + one more register token.** All of the following are unsourced:
  - H1₃: products of token states lie in K₃;
  - MAX₃: product tests are nonnegative on K₃;
  - NC₃: K₃ is invariant under the native CNOT₁₃ and CNOT₂₃ (the "CNOT-only" variant), or under every native
    permutation of the 8 configurations (the "S₈" variant);
  - RO₃: the selective readout branch on token 3 maps K₃ into K₃;
  - ATT: ρ ∈ K₂ ⇒ ρ⊗|0⟩⟨0| ∈ K₃;
  - DIS: Tr₃ K₃ ⊆ K₂.

Fixtures:
- K(Z_F) = (Q3 ∩ Z_F\*) + cone(Z_F), with z_{s,t} = (I + sX⊗Z + tY⊗Y − stZ⊗X)/4;
- Γ(Q3), K_Γ, K_B, K_S, K_H\* and maxCone (XS, SC);
- the classical cone.

### 4.2 Verdicts

| set | verdict | evidence |
|---|---|---|
| Σ0 | **countermodel found**: the classical register family (diagonal cones) satisfies every sourced premise and is not QM | The kernel theorems `permTheory_not_qm` and `obsTheory_nonnegBounded` are about the operation class. Reading them at the cone level as diagonal cones is a short [W] step. The family fails only hH1, which is unsourced |
| Σ1 | Γ(Q3), K_Γ, K_B, K_S, K_H\*, maxCone and K(Z_F) all lie in the domain | XS; SC |
| Σ2 | **excluded already at the pair:** Γ(Q3), K_Γ, K_B and K_H\* (each fails PC24 or hH2), and K_S (fails MI). **Countermodel found: K(Z_F)** | Exclusions: SC E2 (Γ(Q3): 16 of 24 native permutations fail); review `pc24_fixtures.out` (K_B under X⊗I; K_Γ under CNOT); SC §3.3 (K_S fails MI); `kh_pc24.py` K3c (K_H\*: CNOT maps its pure state (V⊗V)(\|00⟩+2\|11⟩) outside its pure set; 20 of 24 fail, K4). K(Z_F), per reg3 A1–A4 and indep I1: the 24 native pair permutations permute Z_F exactly, so PC24 holds and hence MI; the defects are block-positive, since their coefficient matrices are orthogonal [EC+W]; configuration readouts and discards map maxCone into SEP [W, as MI+ C1]; its native statistics are OI's, because diagonal entries of maxCone elements are nonnegative and native protocols from sourced preparations stay diagonal [W]; and it is incomparable with Q3, since z has eigenvalue −1/2 while P_m = I/2 − z is a pure state with Tr(z P_m) = −1/2 and z ∈ K(Z_F)\* (A4) |
| Σ3 | **excluded: every pair cone other than Q3**, within the scope stated below. Of the listed fixtures, K(Z_F) is the only one for which Σ3 is needed. (Q3, QK₃) satisfies Σ3 (D1) | two routes, below |

**Scope of the Σ3 statement.**
- **Assumptions.**
  - K₂ is a convex cone in the 4×4 Hermitian carrier (H-CAR). It must be closed only for the lower route under
    CNOT-only NC₃.
  - Some K₃ exists in the 8×8 Hermitian carrier (H-CAR₃) satisfying H1₃, MAX₃, NC₃, RO₃, ATT and DIS.
  - Native permutations act by the fixed Ad_P (G3).
  - The readout branch is the Lüders branch.
  - Token states and tests range over the full Bloch ball, including complex non-configuration ones (O-A).
- **Conclusion.** K₂ = Q3. The converse holds through K₃ = QK₃.
- **Limits.**
  - Real tests do not suffice for complex non-PSD elements: review R5e/R5f gives a non-PSD X whose real part is PSD.
  - Outside this carrier or this identification the statement says nothing. Under the Γ-transported identification,
    Γ(Q3) satisfies the transported clauses by transport of structure (D5; review R5c).

**Upper route: ATT + NC₃ + MAX₃ ⇒ K₂ ⊆ Q3. No closure is needed.**
- B1 [EC, symbolic]: after attaching |0⟩ and applying CNOT₁₃ and CNOT₂₃, the product test a⊗b⊗c reads ⟨u|X|u⟩, with
  u = D_c(a⊗b) and D_c = diag(c₀,c₁,c₁,c₀).
- Density, B2 and [W]: every u with nonzero entries is reached, by choosing c₁²/c₀² = u₀₁u₁₀/(u₀₀u₁₁). Continuity of
  u ↦ ⟨u|X|u⟩ then gives X ⪰ 0.
- Exact reach, B4b [EC, symbolic]: with the non-affine native σ, every u with u₀₀ ≠ 0 is reached exactly. Other u
  are reached after a native pair transposition, under PC24 (review R2d).
- Exact witnesses:
  - z_{1,1} on |+i⟩|−i⟩|+i⟩ gives −2, normalized −1/4 (B3a, indep I2a);
  - z_{1,1} on the real tests (2,1)(1,2)(3,1) gives −47/4, normalized −47/1000 (D4b, indep I2b);
  - over 216 axis tests, all four defects reach −2 (B3b) and Γ(Φ⁺) reaches −1 (B3c);
  - the non-affine route gives −2 = −½|u|² (B4d).

**Lower route: H1₃ + NC₃ + RO₃ + DIS ⇒ pure states in K₂.**
- C1 [EC, symbolic]: the readout-0 branch after CNOT₁₃ and CNOT₂₃, discarded, is |u⟩⟨u| with the same u = D_c(a⊗b).
- CNOT-only variant: vectors such as (0,1,1,1) are not of the form D_c(a⊗b) (review R2b), and permuting entries
  cannot remove a zero. This variant therefore gives Q3 ⊆ cl K₂, and needs K₂ closed.
- S₈ variant together with PC24: σ⁻¹ reaches every u with u₀₀ ≠ 0, and a native pair transposition first handles
  u₀₀ = 0. This gives Q3 ⊆ K₂ exactly, with no closure.
- Exact instances (C2a–e, indep I4):
  - P_singlet;
  - Φ⁺;
  - CZ|++⟩;
  - P_m, the state that witnesses P_m ∉ K(Z_F).

**Fixtures excluded at each level.**
- At Σ2, PC24/hH2 excludes Γ(Q3), K_Γ, K_B and K_H\*, and MI excludes K_S.
- At Σ3, both routes exclude K(Z_F): the upper route because z is not PSD, the lower route because P_m is generated.
- The upper route also excludes maxCone. maxCone fails PC24 at the pair as well: CNOT does not preserve it (MI+ A15;
  KT4 `cnot_idW`).

### 4.3 Controls and mutations

All pass: `reg3_exclusion.run*.out` (53 checks), `indep_check.run*.out` (7 checks), `kh_pc24.run*.out` (10 checks)
and `monomial_branch.run*.out` (5 checks).

- **Positive.** Ad_C is unitary, and a PSD sample stays PSD, with test minimum 0 (D1a–d). Q3 satisfying Σ3 is
  trivial.
- **Classical.** The upper route keeps diagonal states diagonal and nonnegative (D2a). The lower route produces Φ⁺
  (D2b), which merely restates that the classical cone fails H1.
- **Locality.** The extra token as a spectator gives no exclusion (D3a), and neither do the 24 pair permutations
  tensored with the identity on it (D3c); both follow universally from A2 + A3. CNOT₁₃ alone yields product test
  vectors (D3b).
- **Which tests carry the exclusion.**
  - Configuration-only tests give minimum 0 (D4c, indep I3). This control holds by structure: they read diagonal
    entries.
  - x-axis-only ancilla tests give 0 for the axis family (D4a).
  - Real non-axis tests suffice for the real fixture z_{1,1} (D4b), but not in general (review R5e/R5f).
- **Identification.** The Γ(token 2)-transported action agrees with Ad_C on the diagonal and differs off it
  (D5a–b).
- **Independent code paths.** `indep_check.py` uses no SymPy and no shared helpers. The review's `rev_check.py`
  (35 checks) re-derives claim (3) separately.
- **Monomial control.** The Hadamard control now runs through the same branch computation as the scan and is
  flagged (`monomial_branch.py`).

### 4.4 Drop-one models for the Σ3 routes [W; ingredients EC E1–E2]

Each model satisfies the other premises of its route and has K₂ ≠ Q3.

- **Upper route.**
  - Drop ATT: (K₂, K₃) = (maxCone, QK₃).
  - Drop NC₃:
    - (maxCone, maxCone₃). RO₃ holds, because the Lüders branch of a block-positive operator is block-positive.
    - (K(Z_F), cone{X⊗τ : X ∈ K(Z_F), τ a token state} ∪ products₃). Here ATT, DIS, MAX₃, RO₃ and H1₃ hold by the
      product form.
  - Drop MAX₃: (maxCone, cone{g(M⊗τ)g† : M ∈ maxCone, τ a token state, g ∈ ⟨CNOT₁₃, CNOT₂₃⟩}).
    - DIS holds by E1: Tr₃[g(M⊗τ)g†] = ½(1+r)M + ½(1−r)Z_ℓMZ_ℓ, with Z_ℓ a local unitary.
    - MAX₃ fails by B3.
- **Lower route.**
  - Drop RO₃: (SEP, cone{g(ρ₁⊗ρ₂⊗τ)g†}). Its discards are separable by E1, and E2 shows the readout branch is the
    filter D_c.
  - Drop DIS: (SEP, QK₃).
  - Drop NC₃: (SEP, SEP₃).
  - Drop H1₃: (classical, classical).

None of the drop-one models is formalized.

### 4.5 Pressure test of the favourable branch (§A.31)

1. **PSD import.**
   - No competing cone is evaluated in the PSD order, and PSD is not postulated.
   - But in the fixed 8×8 Ad_P carrier, ATT ∧ NC₃ ∧ MAX₃ is equivalent to validity on K₂ of a dense set of entangled
     pure tests C†(a⊗b⊗c). That is pair PSD, restated.
   - The carrier, the 8×8 Hermitian identification of three-token tables (H-CAR₃, `dictK` [CD #829]), carries the
     PSD structure. It is retained and unsourced, and it is of the same kind as `dict_cnot` at the pair.
2. **Where the force comes from.** The force is the parity coupling of both tokens into a meter, read by
   non-configuration tests (D3, D4c). Those tests come from O-A.
3. **Disguise.**
   - NC₃ and RO₃ are memberships of native coherent outputs: class (b) of MI+ §2.
   - MAX₃ is validity S13, extended to three tokens.
   - Each is a compatibility or validity premise, so each fails G2 as a standalone X.
   - The routes establish their exclusion power, not their source.
4. **Relation to records.**
   - MI+ named C10 (MI-3) and C11 (OV-nat at the pair) and computed neither exclusion. C10 alone cannot generate
     CZ|++⟩: its pure outputs are permuted products [W].
   - SC N4/E9 (exchange symmetry within the partial-transpose family) and KT4 (four-copy coherence, #869/#870) are not
     identified with Σ3. No formal map between them is claimed.
5. **Classification: ELABORATING (scoped).**
   - K(Z_F) is the one listed fixture that satisfies every clause of Σ2. It is excluded once native
     protocols reach one ready meter, with three-token validity and register consistency.
   - The other fixtures are already excluded at Σ2 (§4.2).
   - Σ3 is equivalent to K₂ = Q3 relative to the domain (§3), so it re-expresses hH2 ∧ hA and does not weaken it.
   - Cross-propagation marker AW-F1: a fixture that satisfies every clause of Σ2 also survives any non-circular
     derivation that yields only Σ2-type compatibility or validity clauses (no reachable-closure definition of states,
     MEMO R4). A reachable-closure definition from two-token native data would exclude it, but is barred by R4. A source for O-B therefore needs either multi-token native
     protocols, as in Σ3, or non-native operations, as in hA. Of the listed fixtures, this is shown for K(Z_F) only.

### 4.6 What this does not show

- It is not a no-go for extensions, and not a sourcing argument: Σ3 is unsourced.
- K_k = QK_k for k ≥ 3 is stated in written form only. The argument uses 2^k − 1 tokens and the parity (Walsh)
  decomposition, and is not computed here.
- No implication Σ3 ⇒ hA is formalized. It holds through K₂ = Q3 and `Q3_aMiss` [AT].
- At the pair, the existence form is an equivalence, given the domain: (∃K₃ satisfying Σ3) ⟺ K₂ = Q3.
  - The forward direction is §4.2.
  - The converse is K₃ = QK₃ (D1), and it is trivial.
  - The equivalence holds under the closure qualification of §4.2.
- The monomial-branch lemma is [W]. Its exhaustive instance follows from injectivity and is not independent evidence
  of it.

***

## 5. Recommendation: the premise to attack first

**On Σ3 versus hH2 ∧ hA.**
- **Logical content.** Attacking O-B in the Σ3 form instead of hH2 ∧ hA gains **only a change of vocabulary**. Both
  are equivalent to K₂ = Q3, given the domain.
- **Shape of a derivation.** The difference is real but limited.
  - What Σ3 gains: the compatibility clauses concern native operations only, and no clause asks for the drive or the
    cyclic action as operations.
  - What it pays: an extra register, three unsourced three-token clauses, and the same non-configuration states and
    tests, which come from O-A.
- **The one substantive lesson.** A non-circular source for O-B that yields only Σ2-type clauses (no reachable-closure definition, MEMO R4) cannot exclude K(Z_F) (AW-F1).
  That lesson is a control on derivations, not a reduction of the obligation.

**Revised first premise: O-A**, a continuous non-monomial operation on the elementary system. Reasons:
- Every known form of O-B depends on O-A. hA needs the drive and cyclic operations. Σ3 needs complex non-configuration
  states and tests.
- (T2) needs O-A regardless.
- The monomial lemma shows that coherent preparations cannot stand in for it.
- O-B in any known form is no smaller a target than K₂ = Q3 itself.

**What an OI-native derivation of O-A would have to show.**

1. **Content.** An uncountable family of non-monomial reversible operations on the elementary system that are
   available to the observer, and not merely represented.
   - A countable family cannot reach the exact endpoint, by `countable_not_pairFlowSourced`,
     `mixTheoryR_not_qm` and `fixedGateTheory_not_qm`.
   - The family must break `NonnegBounded`, the uniform-ray invariant and the reality invariant (G4; I:§1.6).
   - The present architecture is proved not to supply it (PG:521). It must therefore come from an explicitly named
     principle stated in OI's own terms, with its own sourcing argument.
2. **Non-circularity.**
   - It must not posit the flow, gate or phase (E0, MEMO §2.4).
   - Representability must not stand in for availability (PG §3.12).
   - The monomial lemma is a must-fail control: a construction that adds only preparations, or any other non-operation
     resource, to the native class does not qualify.
3. **Discriminating controls, fixed in advance.**
   - `permTheory` and the monomial class must remain non-QM.
   - The construction should fix how the new operations act on coherence-level descriptions (Ad_U rather than a
     Γ-transport). Then the same source bears on G3, and hA becomes automatic once K₂ = Q3 is otherwise obtained.
   - The construction must keep the rooted law, and the monitored law on retained protocols (M1).
   - If it also claims to settle O-B, it must exclude K(Z_F), which needs content beyond Σ2-type clauses (or a reachable-closure definition, which MEMO R4 bars).
4. **Independent prediction (G6).** At least one consequence beyond the resource, with a preregistered decision rule.
   None was found here, so G6 is OPEN.

***

## 6. What could not be verified

- [CD] objects (#829 k-token, #831, #822, KN-DESC, `dictK`) are cited from MEMO, thread I and XS, not rebuilt.
- Thread I's line references are at `5bfdaba6`/`804843f1`. Every kernel name used here was re-grepped at `ec49d0b4`,
  but thread I's prose rows were not re-audited.
- No Lean was written or compiled.
- The following [W] steps have not been reviewed:
  - the k ≥ 3 extension;
  - the drop-one models, including the K(Z_F) three-token model;
  - the cone-level reading of the Σ0 kernel countermodel;
  - the extreme-ray inference used for K_H\*.
- The density, the monomial lemma and claim (3) were independently re-derived by the review.
- K_H\*'s pure-set description relies on #864 S2. Its ingredients are re-checked here in K1a–c.
- Preservation of K_H\* by the four native permutations that commute with SWAP is not tested.
- MEMO Fact B's [WA] items and #864's [W, new] exclusions (SC §3.2) were taken as recorded.
- The physical meaning of a three-token ready meter in OI (H-CAR₃, and the Ad_P action on 8×8 descriptions) is a
  premise here, not a finding.

***

## 7. Files (this directory)

`LEDGER.original.md` is the uncorrected ledger, and `CORRECTIONS.md` lists each change with before and after
digests. Current digests are in `SHA256SUMS`.

| file | role |
|---|---|
| `reg3_exclusion.py`, `.run1.out`, `.run2.out` | blocks A–E, 53 exact checks (SymPy 1.13.3, Python 3.13.16, `-I -B`); unchanged in this pass |
| `indep_check.py`, `.run1.out`, `.run2.out` | independent re-check using Fractions, 7 checks; unchanged |
| `kh_pc24.py`, `.run1.out`, `.run2.out` | K_H\* against hH2/PC24, 10 checks (new) |
| `monomial_branch.py`, `.run1.out`, `.run2.out` | exhaustive branch scan over all 8! permutations, with the control running through the same computation (revised) |
