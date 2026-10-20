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
| OI-7 | the sourced theory is not QM; relative to `SourcedOI`, QM ⟺ one continuously driven pair per level | (a) | `permTheory_sourcedOI` SubstratumInterfaceAudit.lean:660; `permTheory_not_qm` :716; `permTheory_not_phaseFree` :711; `sourcedOI_qm_iff_phaseFree` :654 (both directions in one iff, relative to `SourcedOI`) |
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
| ball and effects | the cone of available token tests is `maxCone (eball d)`; all affine effects available | (b) on effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4 | `maxConeOf_avail_eq` EffectSpace.lean:572; `avail_eq_fullEffects` :727; `sharpFamily_subset_avail` :374 |
| K1 | d ∈ {1,3}; d = 3 with an entangling gate | (b) on `0 < d`, effect soundness, the four K∞ hypotheses, `IsNot`, `NativeGateOf`, `EntanglingOf` | `dim_of_nativeGateOf` K1Bridge.lean:128; `three_of_nativeGateOf` :138; CNOT instances `nativeGate_cnot` CompositeDimension.lean:1160, `entangling_cnot` :1380 (the gate is OI's, OI-3) |

### 2.2 K2 — the pair

| id | premise of `pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153) | class | status |
|---|---|---|---|
| H-CAR / LT | the pair is `W 3` through the Pauli dictionary; local tomography | (d), RES | `Composite.lt` introduced; LT independent of the other composite fields `not_locallyTomographic_paddedBall3` CompositeInterface.lean:912 |
| hH1 | products of all `eball 3` states are states | (d) | non-basis token states need a non-monomial resource (I:H20); the four basis products are OI-4 |
| hadd, hsmul | convex cone | (d), RES | classical mixing; load-bearing (I:H21) |
| hmax | K ⊆ maxCone (product-test validity, X-5) | (d) | `maxCone_bound_of_sharp_available` EqvK2MaxCone.lean (premises `hvalid`, `hsharp`); `hsharp` is (b) via `sharpFamily_subset_avail` |
| hH2 | CNOT preserves K (PC, part of X-4) | (d) | the operation is OI-3; its preservation of K is unsourced (XS C13; MI+ C0/C8) |
| hA-drive | the `rotLin` flow on the target token preserves K | (d), and the operation itself crosses the barrier | `Q3_aMiss` EqvK2Converse.lean:174 (QM satisfies it); #865 |
| hA-cyc | `cycEquiv` on the target token preserves K | (d) | kept separate from the drive (MEMO App. A.1) |
| conclusion | K = Q3 ⟺ hH2 ∧ hA, given hH1, hadd, hsmul, hmax | (a), with one witness per direction | `pairCone_eq_Q3_iff_drive_maxCone` :174 from `pairCone_eq_Q3_of_drive_maxCone` :153 and `driveInvariant_of_eq_Q3` :165 |
| **new route** | hH2 ∧ hA replaced by native three-token premises (§4) | (b) [W + EC] | this ledger §4; not formalized |

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

## 3. The minimal open obstruction

Two premises, each shown non-droppable relative to the rest by an exact or kernel countermodel. Both are unsourced.

**O-A. A continuous non-monomial operation on the elementary system (X-1 = I5, with its images K∞-Trans/H8 and the
test closure H11b).** It is consumed three times: for the token ball and its non-configuration effects (§2.1 "ball and
effects", needed by hH1 and by every test that has exclusion power, reg3 D4c), and for (T2) availability of all
instruments. Countermodels without it: the sourced theory itself (`permTheory_not_qm`, `obsTheory_nonnegBounded`) and
the monomial class (`substratum_residual`). New, [W] with an exhaustive [EC] instance (`monomial_branch.py`): adding
**every** product-state preparation to the native class does not remove it. In any finite native protocol every Kraus
branch is ⟨c′\|M\|α⟩ with M a scaled partial permutation and \|α⟩ the ancilla preparation, so each entry is a single term,
a branch has at most \|S\| nonzero entries, and an invertible branch is monomial. A unitary channel therefore has to be
monomial, and the Hadamard channel is unavailable. So coherent preparations do not source coherent control.

**O-B. State–operation compatibility and test validity (X-4, X-5) together with the identification G3.** The [AT]
pair theorem consumes them as hH2 ∧ hA, the compatibility of a non-native drive and a cyclic action. §4 shows that, on
the same domain, **native** three-token compatibility and validity, together with register consistency, already
determine the pair cone. The weakest known sufficient form of O-B is therefore the premise set Σ3 of §4.1. It needs
no non-native operation and no drive-compatibility clause. It does need the fixed identification and
non-configuration token tests, and the latter come from O-A. Countermodel without it: K(Z_F), which satisfies every
other premise at the pair (§4.2).

The identification layer (H-CAR, H27, Origin) is required for any statement at all and has no predicates; it is
recorded as RES rather than as an obstruction, since no countermodel separates it.

***

## 4. Decisive investigation: is there a non-quantum pair structure satisfying everything OI sources?

### 4.1 Premise sets checked

- **Σ0 (strictly sourced):** OI-1…OI-8. Physical pair states contain the four basis products; native operations are
  the 24 pair permutations, configuration readouts, attach and discard; the native laws are OI's.
- **Σ1 = Σ0 + the pair domain:** hH1, hadd, hsmul, hmax. These are not sourced, but MEMO fixes them as the screening
  domain.
- **Σ2 = Σ1 + pair-level native compatibility:** all 24 native permutations preserve K (PC24 ⊇ hH2), together with
  readout closure, discard and MI.
- **Σ3 = Σ2 + one more register token** (all unsourced):
  - H1₃: products of token states lie in K₃;
  - MAX₃: product tests are nonnegative on K₃;
  - NC₃: K₃ is invariant under the native CNOT₁₃ and CNOT₂₃ (or any native permutation of the 8 configurations);
  - RO₃: the selective readout branch on token 3 maps K₃ into K₃;
  - ATT: ρ ∈ K₂ ⇒ ρ⊗\|0⟩⟨0\| ∈ K₃;
  - DIS: Tr₃ K₃ ⊆ K₂.

Fixtures: K(Z_F) = (Q3 ∩ Z_F\*) + cone(Z_F), with z_{s,t} = (I + sX⊗Z + tY⊗Y − stZ⊗X)/4. Also Γ(Q3), K_Γ, K_B,
K_S, K_H\* and maxCone (XS, SC), and the classical cone.

### 4.2 Verdicts

| set | verdict | evidence |
|---|---|---|
| Σ0 | **countermodel found**: the classical register family (diagonal cones) satisfies every sourced premise and is not QM | (a): `permTheory_not_qm`, `obsTheory_nonnegBounded`. It fails only hH1, which is unsourced |
| Σ1, Σ2 | **countermodel found: K(Z_F)** | reg3 A1–A4, indep I1. The 24 native pair permutations permute Z_F exactly, so PC24 holds and hence MI. The defects are block-positive because their coefficient matrices are orthogonal [EC+W]. Configuration readouts and discards map maxCone into SEP [W, as MI+ C1]. Its native statistics are OI's, since diagonal entries of maxCone elements are nonnegative and native protocols from sourced preparations stay diagonal [W]. It is incomparable with Q3: z has eigenvalue −1/2, and P_m = I/2 − z is a pure state with Tr(z P_m) = −1/2 while z ∈ K(Z_F)\* (A4) |
| Σ3 | **excluded: every pair cone other than Q3** (closed K₂). Q3 satisfies Σ3 (D1) | two routes, below |

**Upper route: ATT + NC₃ + MAX₃ ⇒ K₂ ⊆ Q3.**
- B1 [EC, symbolic]: after attaching \|0⟩ and applying CNOT₁₃ and CNOT₂₃, the product test a⊗b⊗c reads
  ⟨u\|X\|u⟩ with u = D_c(a⊗b), where D_c = diag(c₀,c₁,c₁,c₀).
- B2 and [W]: these u are dense in ℂ⁴, since every u with nonzero entries is reached, by choosing
  c₁²/c₀² = u₀₁u₁₀/(u₀₀u₁₁). So X is PSD.
- B4b [EC, symbolic]: with the non-affine native permutation σ that maps the slice {x₃ = 0} onto the weight-≤1 set,
  every u with u₀₀ ≠ 0 is reached exactly, with no density step.
- Exact witnesses (normalized values in brackets):
  - z_{1,1} on \|+i⟩\|−i⟩\|+i⟩ gives −2 (−1/4) (B3a, indep I2a);
  - z_{1,1} on the real tests (2,1)(1,2)(3,1) gives −47/4 (−47/1000) (D4b, indep I2b);
  - all four defects give a minimum of −2 over 216 axis tests (B3b);
  - Γ(Φ⁺) gives −1 (B3c);
  - the non-affine route gives −2 = −½\|u\|² (B4d).

**Lower route: H1₃ + NC₃ + RO₃ + DIS ⇒ pure states in K₂.**
- C1 [EC, symbolic]: the readout-0 branch after CNOT₁₃ and CNOT₂₃, discarded, is \|u⟩⟨u\| with the same u = D_c(a⊗b).
  So Q3 ⊆ cl K₂, and with σ⁻¹ every pure state lies in K₂ exactly.
- Exact instances of states missing from a fixture:
  - P_singlet, missing from K_H\* (C2a);
  - Φ⁺, missing from K_S (C2b);
  - CZ\|++⟩ (C2c);
  - P_m, missing from K(Z_F) (C2d–e, indep I4).

**Which fixtures each route excludes.**
- The upper route excludes every non-PSD fixture: K(Z_F), Γ(Q3), K_Γ, maxCone.
- The lower route excludes every fixture that does not contain all pure states: K(Z_F), K_B, K_S, K_H\*, the
  classical cone.

### 4.3 Controls and mutations (all PASS, `reg3_exclusion.run*.out`, 53 checks; `indep_check.run*.out`, 7 checks)

- **Positive.** Ad_C is unitary, and a PSD sample stays PSD with test minimum 0 (D1a–d).
- **Classical.** The upper route leaves diagonal states diagonal and nonnegative (D2a). The lower route produces Φ⁺
  (D2b).
- **Locality.**
  - With the extra token as a spectator, or under the 24 pair permutations tensored with the identity on it, the
    minimum is 0 (D3a, D3c).
  - CNOT₁₃ alone yields product test vectors (D3b).
  - So the exclusion requires coupling both tokens into the extra token, or a non-affine σ.
- **Which tests carry the exclusion.**
  - Configuration-only tests give minimum 0 on every defect and on Γ(Φ⁺) (D4c, indep I3).
  - x-axis-only ancilla tests give 0 for the axis family (D4a).
  - Real non-axis tests suffice for the real fixture (D4b).
- **Identification.** The Γ(token 2)-transported action of the same bijection agrees with Ad_C on every diagonal
  matrix unit and differs on an off-diagonal one (D5a–b). The exclusion of Γ(Q3) therefore holds only relative to
  the fixed identification (G3).
- **Independent code path.** `indep_check.py` uses no SymPy and no shared helpers. It reproduces I1 (permutation
  closure), the values −2 and −47/4, the configuration-test control, and the generation of P_m.

### 4.4 Drop-one models for the Σ3 routes [W; ingredients EC E1–E2]

Each model satisfies the other premises of its route and has K₂ ≠ Q3.

- **Upper route.**
  - Drop ATT: (K₂, K₃) = (maxCone, QK₃).
  - Drop NC₃: (maxCone, maxCone₃). RO₃ holds, because a token-3 Lüders branch of a block-positive operator is
    block-positive.
  - Drop MAX₃: (maxCone, cone{g(M⊗τ)g† : M ∈ maxCone, τ a token state, g ∈ ⟨CNOT₁₃, CNOT₂₃⟩}).
    - DIS holds by E1: Tr₃[g(M⊗τ)g†] = ½(1+r)M + ½(1−r)Z_ℓMZ_ℓ, where Z_ℓ is a local unitary.
    - MAX₃ fails by B3.
- **Lower route.**
  - Drop RO₃: (SEP, cone{g(ρ₁⊗ρ₂⊗τ)g†}). Its discards are separable by E1, and E2 shows that the readout branch is
    the filter D_c.
  - Drop DIS: (SEP, QK₃).
  - Drop NC₃: (SEP, SEP₃).
  - Drop H1₃: (classical, classical).

Of these models, only the drop-NC₃ model of the upper route and the drop-RO₃ model of the lower route depend on
computed facts (B3, E1, E2). The other models are standard cones. None of the drop-one models is formalized.

### 4.5 Pressure test of the favourable branch (§A.31)

1. **PSD import.**
   - No competing cone is evaluated in the PSD order. The routes use the fixtures' own elements, product tests, native
     permutations and the matrix carrier.
   - The carrier, the 8×8 Hermitian identification of three-token tables (H-CAR₃, `dictK` [CD #829]), is retained and
     unsourced. It is the same kind of premise as `dict_cnot` at the pair.
2. **Where the force comes from.** The parity coupling of both tokens into a meter, read by non-configuration tests
   (D3, D4c).
   - Those tests come from O-A, so the drive is not eliminated from F2-reg. It is eliminated only from the
     cone-selection step as a compatibility clause (hA).
3. **Disguise.**
   - NC₃ and RO₃ are memberships of native coherent outputs, class (b) of MI+ §2. MAX₃ is validity S13 extended to
     three tokens. Each is a compatibility or validity premise, so each fails G2 as a standalone X.
   - What is new is their exclusion power. The routes do not show that they are sourced.
4. **Relation to records.**
   - MI+ named C10 (MI-3: discards of three-token native images of products) and C11 (OV-nat at the pair), and
     computed neither exclusion (MI+ RESULT, "conditional sufficiency: untested").
   - C10 alone cannot generate CZ\|++⟩: its pure outputs are permuted products [W]. The selective branch RO₃ is what
     the lower route adds.
   - SC N4/E9 concerns exchange symmetry within the partial-transpose family.
   - KT4 (#869/#870) concerns four-copy coherence across groupings.
   - None of these is identified with Σ3. They share ingredients, and no formal map between them is claimed.
5. **Classification: NEW (scoped).** At the pair level, the survival of K(Z_F), Γ(Q3), K_B, K_S and K_H\* depends on
   truncating native protocols at two tokens. With one ready meter and native CNOTs into it, plus validity and
   register consistency, every one of them is excluded and K₂ = Q3. Cross-propagation marker AW-F1: a pair-level
   screen that excludes a fixture through hA may obtain the same exclusion from native three-token clauses. Any
   future X screen should test its fixtures against Σ3 before attributing the exclusion to a non-native clause.

### 4.6 What this does not show

- It is not a no-go for extensions, and not a sourcing argument: Σ3 is unsourced.
- K_k = QK_k for k ≥ 3 is stated only in written form. The route uses 2^k − 1 tokens, and every function on F₂^k
  factors through its parities (Walsh). It is not computed here.
- No implication from Σ3 to hA is formalized. The implication holds through K₂ = Q3 and `Q3_aMiss` [AT] once K₂ is
  closed.
- The monomial-branch lemma is [W]. Its exhaustive instance reproduces the counting argument and is not independent
  evidence of it.
- No equivalence is stated. Σ3 ⇒ K₂ = Q3 is one direction. Q3 satisfies Σ3 (D1), which is a holds-in-QM check (N1),
  not a converse theorem.

***

## 5. Recommendation: the premise to attack first

**Attack O-B in its native three-token form, NC₃ ∧ MAX₃ under the fixed identification**, before searching further
for X candidates at the pair.

Three reasons:
- It involves only OI's own operations: native CNOTs into a meter, a native readout, attach and discard.
- §4 shows that it carries all the cone-level work hA was doing: K2, the cone part of Kₙ, G3 relative to the fixed
  identification, and the exclusion aspect of G5 for every listed fixture.
- O-A already has an [AT] *Independent* verdict for the present architecture (PG:521), so it can only come from an
  extension. Once the cone is QK, O-A's compatibility half is automatic when X's operations act as unitary conjugations, since those preserve QK. Only O-A's
  availability half remains (G4 and the monomial lemma).

**What an OI-native derivation would have to show.**

1. **Content.** For every physical pair state ω, the state of (pair, ready meter) after the native CNOT₁₃ and CNOT₂₃
   is a physical three-token state with nonnegative product-test probabilities, and its selective native-readout
   branches and discards are physical.
   - Native bijections must act on coherence-level descriptions by Ad_P.
   - The natural OI route is the reduced-description reading: coherent descriptions as reductions of a
     configuration-level visible–hidden object on which bijections act by permutation (Main.md:600–602, the open lift).
2. **Non-circularity.**
   - It must not define states as the reachable closure (MEMO R4) or postulate PSD.
   - It must not be a bare transfer clause (G2).
   - It must hold for every admissible hidden prior (H0), or say which one it singles out.
3. **Discriminating controls, fixed in advance.**
   - It must fail to hold, or fail to be derivable, under the Γ-transported identification (D5). It must supply the
     orientation datum, not assume it.
   - It must exclude K(Z_F) at three tokens (B3), while K(Z_F) still satisfies all pair-level clauses (A2). This
     checks that the three-token content is what is used.
   - It must leave the classical sector's rooted and monitored laws unchanged (M1; D2a).
   - It must reproduce D4c: no exclusion with configuration tests only.
   - Kill test for the lift: `fiber_freedom` (AW-X6).
4. **Independent prediction (G6).** At least one consequence beyond the cone it fixes, with a preregistered decision
   rule. QM statistics of the parity-meter protocol would be a retrodiction. **None was found here, so G6 is OPEN.**

***

## 6. What could not be verified

- [CD] objects (#829 k-token, #831, #822, KN-DESC, `dictK`) were cited from MEMO, thread I and XS, not rebuilt.
- Thread I's line references are at `5bfdaba6`/`804843f1`. Every kernel name used above was re-grepped at `ec49d0b4`,
  but thread I's prose rows were not re-audited.
- No Lean was written or compiled. Every [W] step in §3–§4 is unreviewed by a second party:
  - density (B2);
  - the monomial lemma;
  - the drop-one models;
  - the general k ≥ 3 extension;
  - K(Z_F)'s readout and discard closure.
- MEMO §2.2 Fact B's [WA] items and #864's [W, new] exclusions (SC §3.2) were taken as recorded.
- The physical meaning of a three-token ready meter in OI (H-CAR₃, the Ad_P action on 8×8 descriptions) is a premise
  here, not a finding.

***

## 7. Files (this directory)

| file | role | sha256 |
|---|---|---|
| `reg3_exclusion.py` | blocks A–E, 53 exact checks (SymPy 1.13.3, Python 3.13.16, `-I -B`) | `661de3c5b0712e4e0d65f10c7518c2c7d952aa45020438c43368c56803668699` |
| `reg3_exclusion.run1.out`, `.run2.out` | 53 PASS, 0 FAIL, rc 0, byte-identical | `75b55ed017e693226103114cef391a9b49497bac78d410f767fca1a6e00fa42e` |
| `indep_check.py` | independent Fraction-based re-check, 7 checks | `dc8afbd5ff309714ade972682620b0ec5039c3c0d545ad164ac40aee06673321` |
| `indep_check.run1.out`, `.run2.out` | 7 PASS, byte-identical | `63501280f2a0ba487edb3cb2e512a6b55547aa27135be432c5e7b74e8f962cd2` |
| `monomial_branch.py` | exhaustive support check over all 8! permutations, two splits, with a Hadamard control | `b12b5e453b72b6bf56889e16a1da0c5a335c18c9c8c85bd528cd3d71c674b338` |
| `monomial_branch.run1.out`, `.run2.out` | 5 PASS, byte-identical | `bd7ad5f4e4b6cc9ecbec3173fbb3e5b01af6d7bb561ba48bcad3053a92c2a598` |
| `SHA256SUMS` | the digests above | — |
