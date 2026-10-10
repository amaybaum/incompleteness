# I4 inventory — generalization and completion (stage 6, Q-EX-FULL, step 1)

Thread I4 of `PROTOCOL-STAGE6.md` (`b277b7c1…`). Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` at
`pt/base/` (read-only). Scope: the matrix-level and general-carrier layer — the Kₙ census, `GeneralCarrier`,
`CompletedOI` / `CarrierGeneralOIPlus` (OI⁺; namespaces `OIHierarchy`, `OIHierarchyGeneral`),
`ImplementationLocality` (namespace `InterventionLocality`), `MinimalRepertoire`, `PositivePackage`,
`MicroscopicReversibility`, `PositiveReachability`, `StructuralClosure`, `SubstratumSource`, `SubstratumInterface`,
`PhaseSource`, `ReadWriteControl`, `DerivedQ3`, `LiftAudit`, `ExecSource`, `LiftSource`, `FlowEndpoint`, `C5Discovery`,
`StateMixingCoupling`, `PairFlowEquivalence`, `CoherentContinuumSource`, `EmbeddedObservation` (namespace
`PrimitiveSource`), `ReferenceExtension`, `SpectatorBridge`, `TypedCompletion`, `TypedPositive`, `QuasilocalAlgebra`,
`QuasilocalCharacterization`, `SecondOrderDrive`, `JordanClassification`, `OperationalRigidity`, `PassiveObservation`
with `PassiveIndependence` and `PassiveQuotient`. The manuscript side is cross-referenced only (`CENSUS.md` §b).

## How this file is made

`INVENTORY.md` is the byte copy of `render_inventory.out`: `render_inventory.py` reads `records.txt` (the manual
fields, written in parts) and quotes every kernel statement verbatim from `pt/base` — the docstring that ends just
above the declaration, and the declaration itself (for a theorem, the signature to its `:=`; for a definition or
structure, the whole declaration) — and every Markdown statement verbatim by line range. Each record's source line
is checked to hold the record's name; the render's control line and verdict close the file. Provenance paths are
relative to `pt/base/` (kernel files under `verification/lean-mathlib/OIBridge/`).

## Field conventions

- **id** `I4.<n>`: issued once, never renumbered. Cross-references inside records use declaration names and
  `file:line` (stable at L), not ids.
- **kind**: as `PROTOCOL-STAGE6.md` lists. A data definition the protocol names (an operation constructor such as
  `withSpectator`, a carrier type, a class such as `substratumClass`) is recorded as *definition-as-hypothesis*
  with status "-": a definition has no truth value; the hypotheses stated with it carry theirs. Type-valued
  structures whose fields are propositions assumed of every instance (`FiniteOperationalTheory`,
  `TypedOperationalTheory`, `QuasilocalSystem`, `ReversibleDynamics`, …) are recorded as *hypothesis-structure*.
- **status**: theorems of the certified build are *proved [K]*. A Prop-valued definition used as a hypothesis is
  *assumed* unless a kernel theorem discharges it; where a theorem discharges it for a particular object (for
  example `substratumClass_structurallyClosed` for the substratum class) the record names that theorem and the
  object, and the general status stays *assumed*. ROADMAP items carry the ROADMAP's own label. No status is
  upgraded by this thread.
- **level**: M — stated over `FiniteOperationalTheory` at one (fixed or generic) finite carrier; G — the
  carrier-general closures (`general_characterization`, `main_result`, the `carrier_general_*` theorems), the typed
  carrier (`TypedOperationalTheory`) and the quasilocal algebra; H — substratum-class objects (`substratumClass`,
  `substratumTheory`, `IsMonomial`, configuration-level classes, read-write families, the passive hidden
  dynamics of `PassiveQuotient`, the substratum's reversible dynamics); O — the single-token level (one record,
  the Kₙ census's scope finding about K∞). Kernel level-H objects are themselves matrix-level theories or
  classes: `substratumTheory A` is a `FiniteOperationalTheory A`.
- **depends_on**: every hypothesis of the declaration (binders and, for definitions, the conjuncts), by name.
- **bridge**: for every record not at level P. The codes expand, verbatim, to the result of the import-level scans
  (`bridge_scan.out`, `bridge_scan2.out`, `bridge_scan3.out`, `bridge_scan4.out`); where the protocol asks for
  them, the nearest pair-level objects are named after the expansion.
- **bearing**: "none at L" wherever no bridge theorem exists at L; the single exception is recorded at I4.236.
- **flag**: "do not assume" for the OI⁺ completion conditions and packages ((i)–(v) and their bundles,
  observational independence / parallel reference extension, reversible richness and its clauses and forms,
  observer recursion / embedded observation, implementation locality and its spectator clause, structural
  closure of an extension, `LayerFlowExecutable`, `HasCompositeUnitaryControl`), for the quantum endpoints used as
  hypotheses (`ExactAllFiniteEndomorphicQuantumOps`, `ShadowQuantum`), and for the PSD-cone facts that serve
  `Q3` as a comparison object.

## Sections

- **A** (I4.1–I4.63): the spectator / extension objects — `ReferenceExtension`, `SpectatorBridge`,
  `ImplementationLocality`, `StructuralClosure`, `LiftAudit`.
- **B** (I4.64–I4.142): the characterizations — the carrier `FiniteOperationalTheory`, conditions (i)–(v) and the
  QM endpoint, `GeneralCarrier`, `CompletedOI`, `CarrierGeneralOIPlus`, `EmbeddedObservation`, `MinimalRepertoire`,
  `PositivePackage`, `MicroscopicReversibility`, `PositiveReachability`, with their independence theorems.
- **C** (I4.143–I4.185): the substratum-source chain — `SubstratumSource` through `CoherentContinuumSource`.
- **D** (I4.186–I4.232): typed and quasilocal completions, `SecondOrderDrive`, `JordanClassification`,
  `OperationalRigidity`, the passive modules.
- **E** (I4.233–I4.239): the Kₙ census and the ROADMAP obligations in scope.
- **F** (I4.240–I4.248): hypotheses of recorded I4 theorems that are defined in modules outside I4's list.

The 35 modules carry 1164 theorems (listed by name and line in `census_kernel.out`). Those not recorded
individually here are lemma-folded: each is an auxiliary of the recorded theorems of its module, and its
statement is available verbatim in `decl_dump.out`. The census of hypothesis-type declarations (coverage control
(a)) is complete: `census_map.out` maps all 76 entries.

***
