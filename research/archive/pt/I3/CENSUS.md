# I3 — the three coverage censuses, with the mapping and the out-of-scope list

Base L = `9f9f8257…` (`pt/base/`). Scripts (decision rule in each header, fixed before the first run; run as
`python3 -I -B <script>` from `pt/I3/`; stdout `<name>.out`, stderr plus `exit N` in `<name>.err`; replays in
`<name>.replay.out/.err`): `kcensus.py` (census (a)), `kcensus2.py` (census (a), supplement: data structures and
untyped definitions), `kimports.py` (import graph used in the `bridge` fields), `kdecls.py` (exact quotes),
`mcensus.py` (censuses (b) and (c)). Record ids refer to `INVENTORY.md`.

## Counts

| census | items | mapped to an I3 record | out of scope (named thread) | not a census item (reason given) |
|---|---|---|---|---|
| (a) kernel, Prop-valued items of the 22 K modules | 47 | 47 | 0 | 0 |
| (a) design modules [D], Prop-valued items | 14 | 14 | 0 | 0 |
| (a) supplement: data structures (K 11, D 3) | 14 | 14 | 0 | 0 |
| (a) modules met in K-round records but not governed by a K round | 15 modules | — | 15 (I2: 11; I4: 4) | — |
| (b) manuscripts: vocabulary hits in 12 papers and 30 book files | 161 | 1 (M017 → I3.184) | 152 (I2) | 8 |
| (c) roadmap: units of the K section, ROADMAP.md:971–1103 | 30 | 24 | 1 (I4) | 5 (navigation links) |
| (c) roadmap: K-vocabulary lines outside the section | 2 | 1 (X001 → I3.162) | 1 (I2) | 0 |

Unmapped census entries: none. Every axiom/opaque/class count in the 22 K modules is zero (kcensus.out, "K-total").

## (a) The kernel census

**Scope, mechanically fixed.** The 22 modules governed (execution path `A`) by the K-programme rounds of
`verification/programmes/oi-qm/reconstruction/` at L, read from each round's `v3-governed-paths` block: KINF-1/KINF-2
`KInfFoundations`; OG-1 `OrbitGeneration`, `OrbitNormalization`; TRB-1 `TransitiveBody`; CMP-1 `StageCompletion`; IIP-1
`InvariantInnerProduct`; OPACT-1 `CompletionAction`; ORD-1 `CompositionOrder`; COMP-1 `CompositeInterface`; DIM-1
`CompositeDimension`; EFF-1 `EffectSpace`; K1-BRIDGE-1 `K1Bridge`; K1-SHARP-TESTS-1 `SharpTests`; K2-GUARD-1 `K2Guard`;
KTRANS-DENSE-1 `DenseOrbit`; NB-1 `NativeGateBall`; ODD-CHAR-1 `OddChar`; PARITY-NOT-1 `ParityNot`; RELC-SELECT-1
`RelcSelectParity`, `RelcSelectBlock`, `RelcSelectSqueeze`, `RelcSelectC5`. KT4-PREM-1 governs no Lean module (two
probe scripts). The design modules `pt/inputs/fourcopy/FourCopy*.lean` (11 files) are censused separately and tagged [D].

**Declaration counts (column-0 declarations; `kcensus.out`).** K modules together: 0 axiom, 0 opaque, 0 class, 18
structure, 273 def, 9 abbrev, 0 inductive, 0 instance, 1119 theorem, 1 lemma (15457 lines). One indented match
(`EffectSpace.lean:11`, "theorem per") is docstring prose, not a declaration. Supplement B (`kcensus2.out`): the only
definitions without an explicit result type are the type abbreviations `E4`, `Carrier`, `HVec`, `W`, `OpSpace` and the
[D] `W4`, none Prop-valued; cross-check: 51 Prop-valued def/abbrev headers = 40 K + 11 D.

**Theorem coverage.** The census (a) counts hypothesis-bearing declarations. Theorems are recorded as records where they
carry a hypothesis structure of the pair setting, a bridge, a round verdict, or a negative control that fixes a
premise's status (64 theorem records, 5 lemma-folded records and the theorem part of I3.142 in `INVENTORY.md`); every other theorem of a K module is a lemma that
reaches the records only as an edge of its round's verdict theorem (`dim1_core`, `kinf2_kernel_core`,
`orbit_generation_core`, `og1_infrastructure_core`, `trb1_core`, `iip1_core`, `cmp1_core`, `opact1_core`, `ord1_core`,
`comp1_core`, `eff1_core`, `k1b_core`, `nb1_kernel_core`, and the verdict lists of the READ rounds' notes).

### (a.1) Prop-valued items of the K modules (47) → record

| census id | declaration (file:line) | kind | record |
|---|---|---|---|
| C001 | `IsEffectOn` KInfFoundations.lean:116 | def | I3.58 |
| C002 | `IsProperOn` KInfFoundations.lean:125 | def | I3.59 |
| C003 | `IsBoundaryState` KInfFoundations.lean:130 | def | I3.60 |
| C004 | `SupportingEffectComplete` KInfFoundations.lean:135 | def | I3.61 |
| C005 | `SingletonFaces` KInfFoundations.lean:139 | def | I3.62 |
| C006 | `RelStrictConvex` KInfFoundations.lean:144 | def | I3.63 |
| C007 | `PerfectlyDistinguishable` KInfFoundations.lean:154 | def | I3.64 |
| C008 | `CentrallySymmetric` KInfFoundations.lean:160 | def | I3.65 |
| C009 | `CopyNatural` KInfFoundations.lean:284 | def | I3.69 |
| C010 | `ClassicallyExposed` KInfFoundations.lean:894 | def | I3.70 |
| C011 | `KInf1` KInfFoundations.lean:1013 | def | I3.71 |
| C012 | `SharpSeed` OrbitGeneration.lean:65 | def | I3.73 |
| C013 | `PreservesBody` OrbitGeneration.lean:69 | def | I3.74 |
| C014 | `SeedOrbitAvailable` OrbitGeneration.lean:74 | def | I3.75 |
| C015 | `BoundaryTransitive` OrbitGeneration.lean:79 | def | I3.76 |
| C016 | `CoversBoundaryFrom` OrbitGeneration.lean:83 | def | I3.77 |
| C017 | `IsBodyGroup` TransitiveBody.lean:223 | structure | I3.86 |
| C018 | `TransBody` TransitiveBody.lean:235 | def | I3.87 |
| C019 | `StageMap.Consistent` StageCompletion.lean:59 | def | I3.93 |
| C020 | `SCInf` StageCompletion.lean:78 | def | I3.94 |
| C021 | `FiniteRank` StageCompletion.lean:299 | def | I3.96 |
| C022 | `StateRespect` CompletionAction.lean:53 | def | I3.100 |
| C023 | `AffineRespect` CompletionAction.lean:58 | def | I3.101 |
| C024 | `Undoes` CompletionAction.lean:325 | def | I3.102 |
| C025 | `InfiniteOrderOn` CompositionOrder.lean:51 | def | I3.106 |
| C026 | `FiniteOrderOn` CompositionOrder.lean:55 | def | I3.107 |
| C027 | `OrdInf` CompositionOrder.lean:60 | def | I3.108 |
| C028 | `MulClosed` CompositionOrder.lean:63 | def | I3.109 |
| C029 | `StagePreserving` CompositionOrder.lean:234 | def | I3.110 |
| C030 | `BoundedAffine` CompositeInterface.lean:139 | def | I3.117 |
| C031 | `LocallyTomographic` CompositeInterface.lean:235 | def | I3.115 |
| C032 | `JointReversible` CompositeInterface.lean:445 | abbrev | I3.118 |
| C033 | `IsProduct` CompositeDimension.lean:194 | def | I3.5 |
| C034 | `IsNot` CompositeDimension.lean:210 | structure | I3.8 |
| C035 | `NativeGate` CompositeDimension.lean:218 | structure | I3.9 |
| C036 | `Entangling` CompositeDimension.lean:229 | def | I3.10 |
| C037 | `BlockData` CompositeDimension.lean:712 | structure | I3.16 (theorem-internal auxiliary, recorded with `blockData_of_nativeGate`) |
| C038 | `Lor` CompositeDimension.lean:869 | def | I3.123 |
| C039 | `EffectsOn` EffectSpace.lean:567 | def | I3.48 |
| C040 | `MixingClosed` EffectSpace.lean:591 | def | I3.50 |
| C041 | `NativeGateOf` K1Bridge.lean:49 | structure | I3.35 |
| C042 | `EntanglingOf` K1Bridge.lean:64 | def | I3.36 |
| C043 | `HasTwoSharpTests` SharpTests.lean:41 | def | I3.39 |
| C044 | `CandidateCone` K2Guard.lean:95 | def | I3.43 |
| C045 | `DenseBoundaryOrbit` DenseOrbit.lean:53 | def | I3.54 |
| C046 | `GateRel` ParityNot.lean:42 | structure | I3.23 |
| C047 | `CtrlGate` RelcSelectBlock.lean:45 | structure | I3.29 |

### (a.2) Prop-valued items of the design modules [D] (14) → record

| census id | declaration (file:line, `pt/inputs/fourcopy/`) | kind | record |
|---|---|---|---|
| C048 | `PairLinked` FourCopyCore.lean:33 | structure | I3.136 |
| C049 | `TokenCoherent` FourCopyCore.lean:64 | def | I3.134 |
| C050 | `IsOrth3` FourCopyCore.lean:119 | def | I3.129 (component of `NClass`) |
| C051 | `IsRot3` FourCopyCore.lean:123 | def | I3.137 (component of `IE1`) |
| C052 | `NClass` FourCopyCore.lean:132 | def | I3.129 |
| C053 | `IE1` FourCopyCore.lean:156 | def | I3.137 |
| C054 | `FCC` FourCopyCore.lean:177 | abbrev | I3.135 |
| C055 | `EvenCycle` FourCopyCore.lean:180 | def | I3.138 |
| C056 | `IsConvexCone` FourCopyDefs.lean:39 | def | I3.130 (component of `PairAdm`) |
| C057 | `PairAdm` FourCopyDefs.lean:43 | def | I3.130 |
| C058 | `FourCopyCoherent` FourCopyDefs.lean:56 | structure | I3.135 |
| C059 | `EvenCycle4` FourCopyDefs.lean:97 | def | I3.138 |
| C060 | `KT4Cone` FourCopyPackage.lean:83 | structure | I3.141 |
| C061 | `IE1Drive` FourCopyPackage.lean:279 | def | I3.142 |

### (a.3) Supplement: data structures (non-Prop `structure`, used as hypothesis data) (14) → record

| census id | declaration (file:line) | record |
|---|---|---|
| S001 | `FiniteStage` KInfFoundations.lean:63 | I3.57 |
| S002 | `ElementaryDrivability` KInfFoundations.lean:264 | I3.66 |
| S003 | `StageMap` StageCompletion.lean:53 | I3.92 |
| S004 | `DirectedStages` StageCompletion.lean:63 | I3.92 |
| S005 | `BinaryVisible` StageCompletion.lean:244 | I3.95 |
| S006 | `OpDatum` CompletionAction.lean:46 | I3.99 |
| S007 | `CompletionChart` CompletionAction.lean:144 | I3.103 |
| S008 | `ProductData` CompositeInterface.lean:210 | I3.113 |
| S009 | `PreComposite` CompositeInterface.lean:223 | I3.114 |
| S010 | `Composite` CompositeInterface.lean:243 | I3.116 |
| S011 | `SharpReadout` CompositeInterface.lean:393 | I3.119 |
| S012 | `KT4` [D] FourCopyCore.lean:73 | I3.133 |
| S013 | `KT4LT` [D] FourCopyCore.lean:82 | I3.133 |
| S014 | `KT4Core` [D] FourCopyCore.lean:99 | I3.133 |

### (a.4) Modules met in the K-round records but not governed by a K round (out of scope, named)

| module | where met | reason (thread) |
|---|---|---|
| `CoherentExtension` | imported by `KInfFoundations` (PSD lemma of the matrix-level `qubit_certain_face`); named in KINF-1's preregistration | coherent CPTP extensions of a reversible classical action, the dilation route: thread I2 |
| `RegionLimit` | named in KINF-1's preregistration; ROADMAP.md:1102 link | OI_Q Level III quasilocal completion: thread I2 |
| `SubstratumSource` | named in KINF-1/KINF-2 preregistrations; ROADMAP.md:1100 link | thread I4 (listed there) |
| `EmbeddedObservation`, `LiftAudit` | named in NB-1's preregistration | thread I4 (listed there) |
| `FactorExchange` | named in NB-1's preregistration | matrix-level factor exchange (`HasQubitFactorExchange`): thread I4 (matrix-level layer) |
| `BohrFrequency`, `CongruentReconstruction`, `EdgeRigidity`, `FrequencyMatching`, `HomometricKill`, `HomometricSix`, `PiccardBridge`, `TurnpikeClassification`, `TurnpikeScopeTransfer` | round BG-1 (a control plane with no `v3-governed-paths` block, under `oi-qm/reconstruction/`) | the Hamiltonian reconstruction of GR §3.3 and the Bekir–Golomb K3 backlog item (ROADMAP P2): thread I2 (established theorems / GR) |

## (b) The manuscript census

**Rule** (`mcensus.py`): every line of `papers/*.md` (12) and `book/*.md` (30) matching the K-programme vocabulary
regex (K∞, Kₙ, K1, K2, pre-quantum, field-neutral, native gate, dimension selector, DIM-1, drivab…, local tomography,
tomographic locality, copy natural…, boundary/continuous transitiv…, sharp seed, four-copy, KT(4), Bloch ball, elementary
system, reconstruction theorem, operational axiom, Masanes, Chiribella, Hardy, self-dual, Barnum, Wilce). 161 hits
(`mcensus.out`, M001–M161). The census set is the hits that state an axiom, condition, hypothesis, principle or theorem;
hits that state none are listed with that reason.

**Finding.** No paper and no book chapter at L states a K-programme premise or result (no K∞, K1, K2, Kₙ, `NativeGate`,
drivability-as-K∞, DIM-1, four-copy or local-tomography-as-K2 statement); the K programme lives in the kernel, the
round records and `ROADMAP.md`. The one manuscript sentence in I3's scope is Main.md:352's statement on the axioms of the
operational reconstructions.

| hits | content | mapping |
|---|---|---|
| M017 (papers/Main.md:352) | "Operational-reconstruction route: target conditions and the outstanding bridge" — the purification, continuous-transitivity and tomographic-locality axioms "are hypotheses of their continuum endpoint … not what the finite characterization uses" | **I3.184**; the rest of the paragraph (the five completion conditions, the intervention dilation, P-indivisibility) is out of scope: thread I2 (manuscript) / I4 (kernel) |
| M022, M023, M024 (Main.md:874, :876, :878) | bibliography entries [51] Hardy, [52] Masanes–Müller, [53] Chiribella–D'Ariano–Perinotti | not a census item (references; cited by I3.184) |
| M016 (Main.md:212) | scope of the correspondence: kinematic locality "does **not**, by itself, prove local tomography …" | out of scope: thread I2 (composition/locality constraints in Main) |
| M018 (Main.md:540) | remark: SIC embedding of the Bloch ball; sharp effects not carried by a four-state model; the classical-dimension obstruction | out of scope: thread I2 (Main's finite-substratum obstruction); cross-note: cited by the research ledger K-INF-DESIGN as a finite-level obstruction on effects (K∞-Seed/K∞-Stage) |
| M019 (Main.md:542) | the operational-extension boundary ("local tomography/composite completeness and all-level operational purification are sufficient …") | out of scope: thread I2 (named in its scope) |
| M020 (Main.md:600) | remark on the purification axiom (CDP) | out of scope: thread I2 (canonical predictive quotient / dilation route) |
| M021 (Main.md:628) | (ii) tensor product structure: dynamical causal separation; "does not alone establish … local tomography" | out of scope: thread I2 (named in its scope) |
| M011 (GR.md:192) | classification by two-slot contexts; positivity through "the self-duality of the positive cone (kernel: `sameData_orderIso`, `psd_iff_trace_nonneg`)" | out of scope: thread I2 (GR) / I4 (matrix-level PSD self-duality, `JordanClassification`) |
| M012 (GR.md:246) | 2. *Phase-free richness* ("some pair of distinguishable states is continuously drivable …"; kernel `MinimalRepertoire.lean`) | out of scope: thread I2 (manuscript form) / I4 (kernel); an OI⁺ completion condition (do not assume) |
| M040 (SM.md:918) | an independent construction's numbers (word "self-…") | out of scope: thread I2 (SM physical layer); no K-programme content |
| M001–M010, M013–M015, M025–M039, M041–M051, M053–M060, M063–M110, M112–M160, M161 (144 lines: Complexity, Computation, Explainer, GR, Methodology, SM, Structure, Substratum, and the book's README, FULL, ch00, ch02–ch05, ch09, ch12, ch19, appendix-c, bibliography) | the substratum **reconstruction theorem** (Substratum Theorem 23: the local lattice/gauge residue fixed modulo `𝒢_sub`), its scope, its realism reading and its mirrors in the book (M119/M161 mention the operational reconstructions only as a comparison for "how to value" that result) | out of scope: thread I2 (established theorems and the physical layer; Substratum, SM, GR, and their book mirrors); none states a K-programme premise |
| M052 (Structure.md:592) | an operational formalization option for universality classes, citing GPTs | not a census item (comparative methodology; states no OI axiom, condition or theorem) |
| M061, M062 (Structure.md:1294, :1384) | Adlam on operational axiomatizations; bibliography | not a census item (literature discussion; reference) |
| M111, M153 (FULL.md:2719; ch09-universality.md:249) | Adler's trace dynamics, "pre-quantum matrix dynamics" | not a census item (literature comparison) |

Counts: 161 = 1 mapped (M017) + 152 out of scope, thread I2 (144 + M011, M012, M016, M018, M019, M020, M021, M040) + 8
not census items (M022–M024, M052, M061, M062, M111, M153).

## (c) The roadmap census

**Rule** (`mcensus.py`): the unit starts of the K section `ROADMAP.md:971–1103` (bounds check OK: line 971 is "### P1 —
K: pre-quantum kinematics", line 1104 "### P2 — Bekir–Golomb …"), and every line outside it matching the K vocabulary.

| unit | line | content | mapping |
|---|---|---|---|
| R001 | 971 | heading "P1 — K: pre-quantum kinematics" | I3.163 |
| R002 | 973 | framing ("five parts, each with its own status") | I3.163 |
| R003 | 978 | **K3 — the operations. CONDITIONAL** (`genTheory_qm_of_quantumArchitecture`, `control_of_lieRank`, `fullInstruments_of_control`, `typed_determined_iff`) | out of scope: thread I4 (matrix-level K3: `SubstratumSource`, `TypedCompletion`) |
| R004 | 984 | **K1 — the dimension. CONDITIONAL.** | I3.164 |
| R005 | 1001 | **K2 — the composite. OPEN.** | I3.165 |
| R006 | 1007 | **K∞ — the field-neutral premises. OPEN.** | I3.166 |
| R007 | 1010 | K∞-Stage | I3.167 |
| R008 | 1014 | K∞-Act | I3.168 |
| R009 | 1017 | K∞-Drive | I3.169 |
| R010 | 1018 | K∞-Trans | I3.170 |
| R011 | 1023 | K∞-Seed | I3.171 |
| R012 | 1025 | K∞-V4 | I3.172 |
| R013 | 1027 | K∞-Copy | I3.173 |
| R014 | 1031 | K∞-Geom | I3.174 |
| R015 | 1035 | the K∞-R label note | I3.175 |
| R016 | 1040 | the geometric obligation not committed to SF | I3.176 |
| R017 | 1045 | the geometric branch elementary-scoped | I3.177 |
| R018 | 1053 | matrix-level drivability; region limit; continuous NOT | I3.178 |
| R019 | 1058 | **Kₙ — elementary-to-arbitrary-carrier lift. OPEN.** | I3.179 (the census result `kn-elementary-carrier-census.md` itself: thread I4) |
| R020 | 1071 | **KINF-1** halted | I3.180 |
| R021 | 1075 | **A research direction, unproved.** | I3.181 |
| R022–R024 | 1081, 1083, 1093 | **The finite route** and its code block | I3.182 |
| R025 | 1095 | orthogonal to `P0` | I3.183 |
| R026–R030 | 1098–1102 | links: NB-1 result, KINF-1 result, `SubstratumSource.lean`, `TypedCompletion.lean`, `RegionLimit.lean` | not census items (navigation links; the two round notes were read, I3.128, I3.180; the modules are I4's and I2's) |
| X001 | 68 | the P1 table row "K — pre-quantum kinematics" | I3.162 |
| X002 | 1108 | P2 Bekir–Golomb: "the sole remaining K3 backlog item" | out of scope: thread I2 (Hamiltonian reconstruction modules, see (a.4)) |

Counts: K section 30 units = 24 mapped + 1 out of scope (I4) + 5 not census items; outside the section 2 lines = 1 mapped
+ 1 out of scope (I2). Also read at L and used for statuses, not separate census units: the seams audit
`verification/audits/foundations/kinf-seams-audit.md` (its §3 table gives "sourced: no" for each K∞ obligation) and
the K-programme round result notes (statuses of every theorem record).
