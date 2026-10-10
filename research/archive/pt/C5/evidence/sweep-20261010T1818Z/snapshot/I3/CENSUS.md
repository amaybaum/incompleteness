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
| (c) roadmap: K-vocabulary lines outside the section | 2 | 1 (X001 → I3.162) | 1 (I4) | 0 |

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
premise's status (63 theorem records, 3 lemma-folded records and the theorem part of I3.142 in `INVENTORY.md`); every other theorem of a K module is a lemma that
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
