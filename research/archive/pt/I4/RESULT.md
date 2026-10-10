# RESULT — thread I4 (inventory: generalization and completion), stage 6, Q-EX-FULL, step 1

Governing text `PROTOCOL-STAGE6.md` (`b277b7c1…`). Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`,
read-only). Started 16:52:52Z (`.start_marker`), records closed 17:25Z. The inventory records; it does not decide:
no derivation is attempted, no verdict on (b) is given, and no status is upgraded.

## §0 Answer

**Counts** (`counts.out`, VERDICT COUNTS VALID; 248 records `I4.1`–`I4.248` in `INVENTORY.md`).

| by kind | n | by status | n | by level | n |
|---|---|---|---|---|---|
| theorem | 140 | proved [K] | 141 | M (matrix level, `FiniteOperationalTheory`) | 165 |
| hypothesis-structure | 73 | assumed | 82 | H (substratum-class objects, passive hidden dynamics) | 44 |
| definition-as-hypothesis | 28 | definition (no status) | 18 | G (carrier-general, typed, quasilocal) | 38 |
| obligation (ROADMAP) | 7 | open | 4 | O (single token; one record) | 1 |
| | | refuted | 2 | P (pair cone) | 0 |
| | | conditional-on | 1 | X (manuscript layer) | 0 |

The 141 proved items are the 140 theorems and the ROADMAP's settled INDEPENDENT findings (I4.239). Censuses
(`CENSUS.md`): (a) kernel 76 entries — 70 mapped, 6 out of scope (theorem-internal auxiliaries 5, a definition with
no hypothesis role 1), 0 unmapped (`census_map.out`, VERDICT ALL ENTRIES ACCOUNTED); (b) manuscript, cross-reference
only, 46 rows (GR.md 206–272, Main.md 538–570 and 628), all *out of scope: I2*, 32 of them carrying the I4 kernel
records they cite; (c) roadmap 15 rows — 10 mapped, 5 out of scope (I1 1, I2 2, I3 2), 0 unmapped. The 35 modules
contain no `axiom`, no `opaque` and no `class`.

**Every item with bearing other than "none at L": one.**
- I4.236, the Kₙ census's scope finding (level O): the K∞ geometric premises (`SingletonFaces`, `RelStrictConvex`)
  fail for complex quantum systems of level ≥ 3 (exact check on the qutrit, kn-elementary-carrier-census.md:47–50;
  ledger statement KN-CENSUS-RESULT.md:10–11), so they are premises about an elementary system. Bearing: constrains
  the single-token structure the pair inherits. The census's stated range (level ≥ 3) contains the two-token pair
  read as one four-level system; this is recorded as the census's scope, not as a verdict on candidate ζ.

**Every bridge found and every bridge absent.**
- **Found, to the pair level P (`W 3`, `K`): none at L.** Mechanically, over the whole kernel at L (214 modules plus
  the root aggregator, `bridge_scan.out`): the only module that imports both the pair-level definitions
  (CompositeDimension.lean:97 `W`, :198 `actT`, :201 `actC`, :775 `cnot`; K2Guard.lean:95 `CandidateCone`) and any of
  the matrix carrier (OperationalAssembly.lean:594 `FiniteOperationalTheory`), the substratum objects (RouteB.lean:279
  `substratumTheory`, StructuralClosure.lean:180 `substratumClass`) or the general carriers (TypedCompletion.lean:165,
  QuasilocalCharacterization.lean:168) is the root `OIBridge.lean`, and the root states nothing about the pair
  carrier (0 pair-token lines; a qualified-name grep also finds none, NOTES N8). Lean admits no other place for a
  theorem that mentions both.
- **Absent, M–P / H–P / G–P**: as above, for all 248 records (bridge field codes NB-M 175, NB-H 34, NB-HP 8, NB-G 24;
  the 7 ROADMAP/audit records state the same in words).
- **Absent, M–O / H–O / G–O** (single-token level, KInfFoundations.lean:264 `ElementaryDrivability`, :425 `cyc3`):
  no module but the root reaches both (`bridge_scan3.out`); no I4 module reaches the single-token definitions.
- **Absent, passive hidden dynamics (H) to P or O**: PassiveQuotient.lean (I4's scope) lies in the import closure of
  the pair carrier, by the chain CompositeDimension → TransitiveBody → CompletionAction → StageCompletion →
  OrbitNormalization → OrbitGeneration → KInfFoundations → CoherentExtension → ControlledQuotient → PassiveQuotient,
  but none of the 85 names declared in PassiveQuotient, ControlledQuotient and ObservabilityQuotient is used in any
  pair-level module (12, `bridge_scan2.out`) or any module of that chain (23, `bridge_scan4.out`), and none of those
  namespaces is opened or qualified there (NOTES N3, N5). The link is an import, not a theorem.
- **Absent, the dictionary between `W 3` and complex matrices**: no `.lean` file at L (221 files, both Lean projects)
  defines `pauliW`, `pauli1`, `Q3` or `twin`, or uses `pauliW`/`Q3` (`dictionary_scan.out`); the 12 pair-level
  modules contain no ℂ at all (NOTES N8). The dictionary exists only in the design module
  inputs/fourcopy/FourCopyPackage.lean:172–183 (ff9c3a35, not certified, the file carries `sorry`).
- **Nearest objects, named in the records**: `withSpectator` / `HasParallelReferenceExtension` /
  `InertSpectatorCompositionality` / `ObservationalIndependence` (I4.1, I4.3, I4.14, I4.82, I4.96) are stated for
  complex linear maps on `Matrix (A × Fin n)` with an appended finite spectator; `actC`/`actT` act by a real-linear
  map on one token of the real table `W d`; `ContextStable` (I4.29) is `𝓘 S K → 𝓘 (R × S) (1_R ⊗ K)` on
  implementations; `LayerFlowExecutable` (I4.56) is the conjugation by `gateFlow (levelPerm σ n) t` on `S × Fin n`,
  whose pair-level counterpart in stage 5 is the native drive on one token of `W 3`; `ObserverRecursion` /
  `EmbeddedObservation` (I4.87, I4.110) concern shifted matrix-level theories and theory families, not the pair cone;
  `psd_iff_trace_nonneg` (I4.210) is on `Matrix n n ℂ`. The field-neutral form of the missing spectator clause is
  the K2 obligation "local actions compatible with the composite cone" (ROADMAP.md:1001–1005, OPEN; I3's scope).
- **Level links found that do not reach P** (for the dependency graph): `substratumTheory` is a
  `FiniteOperationalTheory` (H realized at M, RouteB.lean:279); `coherentLiftTheory_eq_substratumTheory`
  (LiftSource.lean:180); typed theories have matrix-level shadows (`shadow`, TypedCompletion.lean:231; G → M);
  `gateFlow_stage` (LiftAudit.lean:95) reads a gate flow on one region as the stage image of the quasilocal gate
  unitary (M ↔ G); `driveQ_one_eq_heisQ` (SecondOrderDrive.lean:829) and `quasilocal_completion`
  (QuasilocalAlgebra.lean:1353) carry the substratum's reversible dynamics (H) into the quasilocal algebra (G).

**The do-not-assume items (44).** I4.3 `HasParallelReferenceExtension`; I4.4 `HasQutritReferenceExtension`; I4.14
`InertSpectatorCompositionality`; I4.29 `ContextStable`; I4.31 `ImplementationLocality`; I4.42 `OIPlusLocal`; I4.45
`StructurallyClosed`; I4.56 `LayerFlowExecutable`; I4.65 `PhysicalCompletionConditions`; I4.66
`CompositeOperationalValidity`; I4.67 `HasCompositeUnitaryControl`; I4.68 `IteratedAncillaClosure`; I4.69
`SystemToLevelOne`; I4.70 `ExactAllFiniteEndomorphicQuantumOps`; I4.73 `WellFormed`; I4.74 `SubstantiveCompletion`;
I4.80 `CompletedOI`; I4.82 `ObservationalIndependence` (qubit); I4.85 `ReversibleRichness` (qubit); I4.87
`ObserverRecursion`; I4.88 `OIPlus` (qubit); I4.96 `ObservationalIndependence` (carrier-general); I4.99
`ReversibleRichness` (carrier-general); I4.102 `OIPlus` (carrier-general); I4.110 `EmbeddedObservation`; I4.115
`OIPlusEmbedded`; I4.118 `PhaseFreeRichness`; I4.120 `OIPlusMin`; I4.123 `CyclicRichness`; I4.124 `OIPlusPos`; I4.127
`InverseAccessibility`; I4.128 `LieRankRichness`; I4.133 `ReversibleImplementationLocality`; I4.137 `OIPlusMicro`;
I4.143 `DrivesElementary`; I4.144 `QuantumArchitecture`; I4.179 `PairFlowSourced`; I4.187 `ShadowQuantum`; I4.210
`psd_iff_trace_nonneg`; I4.215 `psd_trace_mul_nonneg`; I4.216 `accessible_cone_full`; I4.241 `DerivedOI`; I4.244
`ElementaryTransitionRichness`; I4.245 `OIPlusElem`. Each is a hypothesis at its recorded status, never a premise of a
derivation; where a kernel theorem discharges one for a particular object (for example `StructurallyClosed` for
`substratumClass`, `HasParallelReferenceExtension` for the full theory) the record names that object and the general
status stays *assumed*. Their independence results at the matrix level are proved [K] with the scope the kernel
states: `control_not_implies_parallelReferenceExtension` (I4.10), `hcompRealized_not_implies_parallelReferenceExtension`
(I4.21), `redundancy_fails` (I4.33), `implementationLocality_independent` (I4.41), `oiPlus_independence` (I4.95,
I4.105), `embeddedObservation_independent` (I4.114) — all on `FiniteOperationalTheory (Fin 2)`.

**Assumption-watch markers (record only; for the coordinator and the graph thread).**
1. `Q3` and the Pauli dictionary are not kernel objects at L (above). The stage protocols' `Q3 = {w : pauliW w ⪰ 0}`
   and the [K] tag on `Q3 = dualW Q3` (PROTOCOL-STAGE3.md:66, citing JordanClassification.lean:84 and
   OperationalRigidity.lean:917, statements on `Matrix n n ℂ`) pass through a dictionary that is certified nowhere
   at L.
2. GR.md:212 numbers the five conditions (i) valid probabilities, (ii) trivial-ancilla consistency, (iii) inert
   spectators, (iv) full reversible control, (v) iterated composition; the kernel's `PhysicalCompletionConditions`
   (PhysicalCharacterization.lean:295) has the conjunct order validity, inert, control, closure, level-one. The
   records use the manuscript numerals and name the conjunct position.
3. The landed Kₙ audit's "`CompositeDimension` is imported by no module" holds at its base 95cb01ff, not at L
   (K2Guard and ten others descend from it at L); its operative content — no shared import between the field-neutral
   and complex operational sides — holds at L except for the root aggregator.
4. Locations against the launch text: `control_of_lieRank` and `inverseAccessibility_of_lieRank` are
   MicroscopicReversibility.lean:114 and :132 (PositiveReachability.lean carries
   `universalReachability_of_lieRank_positive`, :996); `parallel_of_observationalIndependence` exists twice
   (CompletedOI.lean:147, CarrierGeneralOIPlus.lean:87); `OIHierarchy` is a namespace (CompletedOI.lean:77;
   `OIHierarchyGeneral`, CarrierGeneralOIPlus.lean:50), not a module; PROTOCOL-STAGE5.md's
   `StructuralClosure.lean:365` is the second line of `quantumArchitecture_iff_drives_of_closed` (:364).

## §1 The inventory by section (`INVENTORY.md`, by reference)

| section | ids | content |
|---|---|---|
| A | I4.1–I4.63 | spectator / extension objects: ReferenceExtension (I4.1–I4.11, I4.23), SpectatorBridge (I4.12–I4.22), ImplementationLocality (I4.24–I4.43), StructuralClosure (I4.44–I4.53), LiftAudit (I4.54–I4.63) |
| B | I4.64–I4.142 | the carrier `FiniteOperationalTheory` (I4.64); conditions (i)–(v), their bundle and the QM endpoint (I4.65–I4.70); GeneralCarrier (I4.71–I4.78); CompletedOI (I4.79–I4.95); CarrierGeneralOIPlus (I4.96–I4.105); EmbeddedObservation (I4.106–I4.117); MinimalRepertoire (I4.118–I4.123); PositivePackage (I4.124–I4.126); MicroscopicReversibility (I4.127–I4.139); PositiveReachability (I4.140–I4.142) |
| C | I4.143–I4.185 | substratum-source chain: SubstratumSource, SubstratumInterface, PhaseSource, ReadWriteControl, DerivedQ3, ExecSource, LiftSource, FlowEndpoint, C5Discovery, StateMixingCoupling, PairFlowEquivalence, CoherentContinuumSource |
| D | I4.186–I4.232 | TypedCompletion, TypedPositive, QuasilocalAlgebra, QuasilocalCharacterization, SecondOrderDrive, JordanClassification, OperationalRigidity, PassiveObservation, PassiveIndependence, PassiveQuotient |
| E | I4.233–I4.239 | Kₙ (ROADMAP.md:1058–1069), the landed Kₙ census (disposition, §3, §4), K3 (ROADMAP.md:978–983), H-∞ (ROADMAP.md:936–951), the settled INDEPENDENT table (ROADMAP.md:1392–1416) |
| F | I4.240–I4.248 | hypotheses of recorded I4 theorems defined outside I4's module list: `substratumTheory`, `DerivedOI`, `ConfigurationLevel`, `HControl`, `ElementaryTransitionRichness`, `OIPlusElem`, `HComp`, `OnesFixing`, `SourcedOI` |

Every kernel statement in `INVENTORY.md` is quoted verbatim from L by `render_inventory.py` (docstring and
signature; whole declaration for definitions), with its file:line checked to hold the record's name (248/248).
Theorems not recorded individually (the 35 modules carry 1164; names and lines in `census_kernel.out`, statements in
`decl_dump.out`) are lemma-folded into their module's recorded theorems.

## §2 Ledger of sources read

Governing and context texts (read in full): `pt/PROTOCOL-STAGE6.md` (`b277b7c1…`), `pt/PROTOCOL-STAGE5.md`
(`9e01f098…`), `pt/PROTOCOL-STAGE5-AMENDMENT-1.md` (`1f639115…`), `pt/PROTOCOL-STAGE4.md` (`d3da2811…`),
`pt/PROTOCOL-STAGE3.md` (`1a649168…`), `pt/PROTOCOL.md` (`239dc123…`), `pt/INTEGRATION-NOTE-STAGE4.md`,
`pt/INTEGRATION-NOTE-STAGE3.md`, `pt/base/AGENTS.md` (`959c4333…`, byte-identical to the working copy's).

Kernel at L (`pt/base/verification/lean-mathlib/`; the checkout verified clean at start and end):
- read in full: `OIBridge/ReferenceExtension.lean`;
- module headers and every recorded declaration (docstring and signature, via `decl_dump.out` and the renderer):
  GeneralCarrier, CompletedOI, CarrierGeneralOIPlus, ImplementationLocality, MinimalRepertoire, PositivePackage,
  MicroscopicReversibility, PositiveReachability, StructuralClosure, SubstratumSource, SubstratumInterface,
  PhaseSource, ReadWriteControl, DerivedQ3, LiftAudit, ExecSource, LiftSource, FlowEndpoint, C5Discovery,
  StateMixingCoupling, PairFlowEquivalence, CoherentContinuumSource, EmbeddedObservation, SpectatorBridge,
  TypedCompletion, TypedPositive, QuasilocalAlgebra, QuasilocalCharacterization, SecondOrderDrive,
  JordanClassification, OperationalRigidity, PassiveObservation, PassiveIndependence, PassiveQuotient;
- definitions outside I4's list that are hypotheses of recorded theorems, at their lines only:
  OperationalAssembly.lean:585–672 (`FiniteOperationalTheory`, `HasCompositeUnitaryControl`),
  PhysicalCharacterization.lean:285–302, OperationalValidity.lean:80–95, LevelOneSeam.lean:110–122 and :180–192,
  AncillaClosure.lean:238–256, RouteB.lean:123–145 and :274–283, ManuscriptAxioms.lean:123–129,
  MonoidalCompletion.lean:311 and :345–352, LieRankSource.lean:436 and :527, InstrumentRealization.lean:180,
  SubstratumInterfaceAudit.lean:236, :606, :619, OIRealization.lean:234 and :252, KInfFoundations.lean:264 and
  :425 (sites only), CompositeDimension.lean:97, :161, :186, :198–229, :775 and K2Guard.lean:95–104 (sites only);
- mechanically, every `.lean` file of `OIBridge/` and the root `OIBridge.lean` (import graph, token scans) and of
  `pt/base/verification/lean/` (dictionary scan).

Roadmap and audits at L: `verification/ROADMAP.md` lines 66–75, 936–1110, 1146–1160, 1385–1440 (and the concept greps
recorded in `CENSUS.md` (c)); `verification/audits/foundations/kn-elementary-carrier-census.md` (58 lines, full).

Manuscripts at L (cross-reference only): `papers/GR.md` 206–272; `papers/Main.md` 538–570 and 624–632.

Stage inputs: `pt/inputs/ledgers/KN-CENSUS-RESULT.md` (108 lines, full; base 95cb01ff); design modules
`pt/inputs/fourcopy/*.lean` (12 files, imports and the dictionary definitions of FourCopyPackage.lean only).

Not read (protocol exclusions): `pt/I1/`, `pt/I2/`, `pt/I3/`, `pt/D5/`, `pt/C5/`, `pt/audit/stage3-inputs/OWNER-*`,
`pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`, `pt/audit/stage6-inputs/`, `pt/audit/reviews/`,
`pt/audit/aborted-launches/`. Listing of `pt/audit/` names and mtimes only, for the sweep.

## §3 What is not claimed

- No status upgrade. Every hypothesis-structure keeps status *assumed* unless a kernel theorem discharges it, and a
  discharge for a particular object (a class, a theory) is recorded as such, not as a general discharge.
- No derivation and no verdict on (b), (b_min), `K = Q3`, IE1, IE2 or frame covariance, and no verdict on any
  manuscript sentence; the manuscript rows are cross-references for thread I2.
- "None at L" for a bridge is a statement about the kernel at L only, established at the import level (no module
  but the root imports both levels, and the root states nothing about the pair carrier). It says nothing about
  design modules, about statements outside the kernel, or about whether such a bridge is provable.
- The level assignments follow the stated rule (INVENTORY.md header); a different level convention for the
  carrier-general `FiniteOperationalTheory` statements (M versus G) would move counts between M and G only.
- Theorems not recorded individually are lemma-folded by module; they were not inventoried one by one. Their names,
  lines and verbatim statements are in `census_kernel.out` and `decl_dump.out`.
- The applicability note at I4.236 restates the census's own range ("level ≥ 3"); no computation on a four-level
  system was run here.
- The kernel facts are cited as proved because they are in the certified build at L; no Lean was built or run here.

## §4 Evidence log

Every script is run from `pt/I4/` as `python3 -I -B <script>`, stdout to `<name>.out`, stderr plus an appended
`exit N` line to `<name>.err`; the decision rule is in each script's header, written before its first run; every
final run was replayed (`<name>.replay.*`) and stdout and stderr are byte-identical (10/10). Failed and superseded
runs are kept.

| script | purpose | runs | final verdict | replay |
|---|---|---|---|---|
| `census_kernel.py` | coverage control (a): Prop-valued declarations of the 35 modules; theorem list | 1 | CENSUS VALID (C1–C5 PASS) | identical |
| `decl_dump.py` | verbatim docstrings and signatures of every declaration | 2 (run 1 FAILED control D4a: Prop `def` body omitted; kept as `decl_dump.run1.{py,out,err}`; rule D2 widened before run 2) | DUMP VALID | identical |
| `bridge_scan.py` | import-level bridge census P versus M, H, G | 1 | no declaration mentions both a pair token and an M/H/G token (controls PASS) | identical |
| `bridge_scan2.py` | passive hidden-dynamics names (85) in the pair-level modules | 1 | no use (controls PASS) | identical |
| `bridge_scan3.py` | single-token level O versus M, H, G | 1 | SCAN VALID: only the root reaches both | identical |
| `bridge_scan4.py` | passive hidden-dynamics names in the single-token chain (23 modules) | 1 | no use (controls PASS) | identical |
| `dictionary_scan.py` | `pauliW` / `Q3` / `twin` definitions at L and in the design modules | 1 | NO DICTIONARY DEFINITION AT L (controls PASS) | identical |
| `census_map.py` | maps the 76 census entries to records or admissible out-of-scope reasons | 1 (replayed twice, after each records edit) | ALL ENTRIES ACCOUNTED | identical |
| `render_inventory.py` | renders INVENTORY.md from `records.txt` with verbatim quotes | dev1 (78 records), run1, run2, final (248 records): all INVENTORY RENDERED; superseded outputs kept | INVENTORY RENDERED (248 source checks, countercontrol PASS) | identical |
| `counts.py` | §0 counts, bearing exceptions, do-not-assume list | run1, run2, final (kept) | COUNTS VALID | identical |

`INVENTORY.md` is the byte copy of the final `render_inventory.out` (same sha256 below). Supplementary greps (not
scripts) are recorded in NOTES N5 and N8 with their results.

sha256 of every file in `pt/I4/` except RESULT.md (73 files):

| file | sha256 |
|---|---|
| `.start_marker` | `2d3f485b1147c69d816c2a960a26ec70140355acce659579f6a20db4f48bf175` |
| `CENSUS.md` | `77d00b0714971cb0de15777b95b9cc7dec7f9a286c12a1e119a26ca95218e569` |
| `INVENTORY-HEADER.md` | `02c431ff5dd5ee68892128aa3162c48de78814edb3690ae2c98900e22cf0eb07` |
| `INVENTORY.md` | `43bbada1db14f052e3ec3eb3d7fc99d1bb042d41a143c912aa6ca3e4cad75461` |
| `NOTES.md` | `3ae60fae1965e31b2d8cdfca875268ffa4c8b50e93d190cd22cbde7bf7334ba6` |
| `bridge_scan.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan.out` | `3568eb9a9759772ef6e0a7507a0f7101d506281d0fa9ba70ff13afdad2a23f42` |
| `bridge_scan.py` | `c134269b5f4decc1a529ff73fc7e67ba94321214e5603293c02b330c9c45f9cf` |
| `bridge_scan.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan.replay.out` | `3568eb9a9759772ef6e0a7507a0f7101d506281d0fa9ba70ff13afdad2a23f42` |
| `bridge_scan2.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan2.out` | `6473153d429527b46f60079f2e219d21e8fc75e9c926d6acf5714a096086f95f` |
| `bridge_scan2.py` | `43e9659f6481e58385100b73d215168721da063aec53942a32fedaaa67fa2cbd` |
| `bridge_scan2.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan2.replay.out` | `6473153d429527b46f60079f2e219d21e8fc75e9c926d6acf5714a096086f95f` |
| `bridge_scan3.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan3.out` | `627cc798272d877d7a28f06628b04ecd59fed4a2652f38f0ed45cb0df58d4c35` |
| `bridge_scan3.py` | `25e847e2c852ca5d54f90f98184e88796433081aeddac592142e2ea197c62b46` |
| `bridge_scan3.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan3.replay.out` | `627cc798272d877d7a28f06628b04ecd59fed4a2652f38f0ed45cb0df58d4c35` |
| `bridge_scan4.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan4.out` | `c9399425430bb0b4b77941481d0cac2e331801306601cbcd711ead5edeadb0e8` |
| `bridge_scan4.py` | `e29d3898bef50a783788e156fb8b541c7a69b5b64684fcf5260f541c217b9b41` |
| `bridge_scan4.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `bridge_scan4.replay.out` | `c9399425430bb0b4b77941481d0cac2e331801306601cbcd711ead5edeadb0e8` |
| `census_kernel.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `census_kernel.out` | `25c527846a97fe940c2a9f9d90d22bd9a837734b2804ecbe1c431e5c7db21d40` |
| `census_kernel.py` | `7f3a451b2e2bca9aee148670f07254c0e70e574939fee315393ff699990424ea` |
| `census_kernel.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `census_kernel.replay.out` | `25c527846a97fe940c2a9f9d90d22bd9a837734b2804ecbe1c431e5c7db21d40` |
| `census_map.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `census_map.out` | `8c912e01a25aacfea82d6ad9e8f8f437dff6a64e58f15e87b58cc7ab92fd73b4` |
| `census_map.py` | `f11daa85fde756dde584a48d7050378136d25d717be07d9d34658c8f033b53e1` |
| `census_map.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `census_map.replay.out` | `8c912e01a25aacfea82d6ad9e8f8f437dff6a64e58f15e87b58cc7ab92fd73b4` |
| `counts.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `counts.out` | `37e42fc0bc0f5a27ce5719e64b69ec51e3308e1b50b8aac2276ab9025d1667b2` |
| `counts.py` | `52d61511cef40589c420825f90f270582c92d1ab3932c49a1675ee81031ea325` |
| `counts.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `counts.replay.out` | `37e42fc0bc0f5a27ce5719e64b69ec51e3308e1b50b8aac2276ab9025d1667b2` |
| `counts.run1.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `counts.run1.out` | `92517543f0fca9fe6007deb73912f5203f150489dc39209754973b73ba1f5f57` |
| `counts.run2.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `counts.run2.out` | `37e42fc0bc0f5a27ce5719e64b69ec51e3308e1b50b8aac2276ab9025d1667b2` |
| `counts.run2.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `counts.run2.replay.out` | `37e42fc0bc0f5a27ce5719e64b69ec51e3308e1b50b8aac2276ab9025d1667b2` |
| `decl_dump.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `decl_dump.out` | `2b90d7dbeb9c4a0d3f87a43f847ab0f998186e754073a6935d0a850b2a07bb46` |
| `decl_dump.py` | `b769ef3fe42578659b0d4889c27bc16f2d51d2d0297e635d4625b74071aa73ad` |
| `decl_dump.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `decl_dump.replay.out` | `2b90d7dbeb9c4a0d3f87a43f847ab0f998186e754073a6935d0a850b2a07bb46` |
| `decl_dump.run1.err` | `0c6868c2c44f053619cef1cc383e1d530743b574ca192ace9168a9ccf46a86e3` |
| `decl_dump.run1.out` | `1fdded97d612669d8718b2a760da8318d13e0becfffe29139a321c2901a1ede9` |
| `decl_dump.run1.py` | `958a761ab505496cb19354a3b4923401b6f95018a638499fa0fde176a53a9357` |
| `dictionary_scan.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `dictionary_scan.out` | `00740ad2beae5b43a099c4e0db4eceb8b252c5f9df3dd3fd334397b8b28ed0b5` |
| `dictionary_scan.py` | `18ffbc6a8183e85970c980cfe45936c4a57ed46370a6466dd08bb1fe9a320247` |
| `dictionary_scan.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `dictionary_scan.replay.out` | `00740ad2beae5b43a099c4e0db4eceb8b252c5f9df3dd3fd334397b8b28ed0b5` |
| `records.txt` | `824f596773b8679421946e0f094f58cc11f8eec7cca1f15cad58b997b9c918e6` |
| `render_inventory.dev1.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `render_inventory.dev1.out` | `e1e0a84aeae0a463fae79f7d9aab0502014be288c0e9f7bea708346ceb1fb2a6` |
| `render_inventory.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `render_inventory.out` | `43bbada1db14f052e3ec3eb3d7fc99d1bb042d41a143c912aa6ca3e4cad75461` |
| `render_inventory.py` | `e3f92b0b9b1f1b4418cc310f68aabb3b20dc9f1f33ec884e2213b9fa0264acdc` |
| `render_inventory.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `render_inventory.replay.out` | `43bbada1db14f052e3ec3eb3d7fc99d1bb042d41a143c912aa6ca3e4cad75461` |
| `render_inventory.run1.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `render_inventory.run1.out` | `bd8e950bf3587bd1cbe0c6ecf1a4867f116d2b18cc24d4fe86b74a1378128994` |
| `render_inventory.run2.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `render_inventory.run2.out` | `629179f46ef0fa17189816e01b3998fc58217800b3b1e42ce1e7b2e3e2d8158a` |
| `render_inventory.run2.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `render_inventory.run2.replay.out` | `629179f46ef0fa17189816e01b3998fc58217800b3b1e42ce1e7b2e3e2d8158a` |

## §5 Integrity

- **Start (16:52:52Z, `.start_marker`).** `pt/I4/` absent at launch, created, `.start_marker` written first. (1) From
  `pt/`, `sha256sum -c --quiet` on `inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4` manifests: rc 0,
  no output; `audit/stage3-inputs/ns.manifest.sha256` from its own directory: `ns/NS-INPUT.md: OK`. (2) `pt/base`
  HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`, `status --porcelain` empty, no `__pycache__`/`.pyc`. (3) The ten
  protocol files at the expected prefixes (239dc123, b41aa0e7, 2a2f78f3, 38603692, 086a4cb8, 1a649168, d3da2811,
  9e01f098, 1f639115, b277b7c1), sidecars OK (six from `pt/`, four from SCRATCH). (4) Listing of the 64 top-level
  names of `pt/` with UTC mtimes.
- **End (17:24:48Z, NOTES N10).** The same four checks, all green; the 64 names; newer than the marker: `C5`, `D5`,
  `I1`, `I2`, `I3`, `I4`, `audit` only; no file under `pt/base` newer than the marker.
- **Sweep (17:24:57Z).** `find pt ( -path ./I1 -o -path ./I2 -o -path ./I3 -o -path ./I4 -o -path ./D5 -o -path ./C5
  -o -path ./audit -o -path './audit*-replay' ) -prune -o -newer I4/.start_marker -print`: nothing outside the
  excluded directories. A first sweep command of mine was malformed (operator precedence printed every non-excluded
  path) and was replaced by the expression above, with a control; recorded in NOTES N10. No anomaly; nothing
  quarantined; no `evidence/` directory was needed.
- **Writes.** Only inside `pt/I4/`; every authored file written in parts of at most 250 lines per write call;
  `INVENTORY.md` is a byte copy of a script output. One temporary file (`.permod.tmp`) and one temporary hash list
  (`.hashes.tmp`) were created inside `pt/I4/` and removed. A temporary list of hash rows (`hashcheck_i4.txt`)
  was written to the scratchpad root, outside `pt/I4/`, and deleted at once (17:27Z): a procedural slip, recorded in
  NOTES N11 addendum 2; nothing under `pt/` was touched and no result depends on it. No git write, branch, PR, CI, network access,
  publication, or sub-agent. Read exclusions honoured (§2).
