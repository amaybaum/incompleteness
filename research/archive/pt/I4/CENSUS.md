# I4 censuses — coverage controls (a), (b), (c) of PROTOCOL-STAGE6.md, thread I4

Base L = `9f9f8257…` (`pt/base/`). Every count below is taken from a script output in this directory
(`census_kernel.out`, `census_map.out`) or from the line lists given here; the record ids refer to `INVENTORY.md`.

## Counts

| census | entries | mapped to a record | out of scope (with reason) | unmapped |
|---|---|---|---|---|
| (a) kernel: `axiom`, `opaque`, `class`, Prop-valued `structure`/`def`/`abbrev`/`inductive` in the 35 modules | 76 | 70 | 6 (theorem-internal auxiliary 5; a definition with no hypothesis role 1) | 0 |
| (b) manuscript, cross-reference only (GR.md 206–272, Main.md 538–570 and 628) | 46 | 0 as I4 records; 32 carry the kernel record ids they cite | 46 (out of scope: I2) | 0 |
| (c) roadmap rows and bullets naming I4 modules or obligations | 15 | 10 | 5 (I1: 1; I2: 2; I3: 2) | 0 |

Kernel census specifics (`census_kernel.out`, all controls PASS): 0 `axiom`, 0 `opaque`, 0 `class` in the 35
modules; 76 Prop-valued or predicate-valued declarations (68 `def`, 5 `structure`, 3 `inductive`; 73 of type `Prop`, 3
predicate families); 1164 theorems;
169 non-Prop `def`/`abbrev`, 6 non-Prop `structure`, 22 `instance`. The protocol's strict grep
`^(axiom|opaque|structure|class|def) ` matches 154 lines outside comments (all parsed) and 3 inside comments.
Beyond census (a), the inventory records 172 further items: theorems, data definitions the protocol names,
Type-valued structures carrying assumed Prop fields, hypotheses of recorded theorems defined outside I4's module
list (Section F), and the Kₙ / ROADMAP items (Section E).

## (a) Kernel census — mapping (from `census_map.out`)

Per-module counts (census entries / theorems), from `census_kernel.out`:

| module | census | theorems | module | census | theorems |
|---|---|---|---|---|---|
| GeneralCarrier | 2 | 13 | C5Discovery | 2 | 24 |
| CompletedOI | 7 | 32 | StateMixingCoupling | 1 | 50 |
| CarrierGeneralOIPlus | 3 | 11 | PairFlowEquivalence | 1 | 16 |
| ImplementationLocality | 8 | 81 | CoherentContinuumSource | 2 | 19 |
| MinimalRepertoire | 5 | 45 | EmbeddedObservation | 5 | 22 |
| PositivePackage | 1 | 6 | ReferenceExtension | 4 | 47 |
| MicroscopicReversibility | 6 | 21 | SpectatorBridge | 3 | 30 |
| PositiveReachability | 0 | 47 | TypedCompletion | 2 | 53 |
| StructuralClosure | 3 | 35 | TypedPositive | 0 | 2 |
| SubstratumSource | 2 | 9 | QuasilocalAlgebra | 2 | 141 |
| SubstratumInterface | 2 | 12 | QuasilocalCharacterization | 2 | 87 |
| PhaseSource | 0 | 10 | SecondOrderDrive | 0 | 59 |
| ReadWriteControl | 1 | 9 | JordanClassification | 0 | 44 |
| DerivedQ3 | 0 | 17 | OperationalRigidity | 1 | 43 |
| LiftAudit | 2 | 56 | PassiveObservation | 3 | 25 |
| ExecSource | 0 | 12 | PassiveIndependence | 4 | 22 |
| LiftSource | 0 | 18 | PassiveQuotient | 2 | 31 |
| FlowEndpoint | 0 | 15 |  |  |  |
| **TOTAL** | **76** | **1164** | | | |

Mapping, entry by entry (`census_map.out`; VERDICT ALL ENTRIES ACCOUNTED):

| census entry (file:line) | keyword | name | record |
|---|---|---|---|
| `GeneralCarrier.lean:125` | WellFormed | `Prop` | I4.73 |
| `GeneralCarrier.lean:130` | SubstantiveCompletion | `Prop` | I4.74 |
| `CompletedOI.lean:96` | OICore | `Prop` | I4.79 |
| `CompletedOI.lean:99` | CompletedOI | `Prop` | I4.80 |
| `CompletedOI.lean:129` | ObservationalIndependence | `Prop` | I4.82 |
| `CompletedOI.lean:171` | ReversibleRichness | `Prop` | I4.85 |
| `CompletedOI.lean:315` | IsShiftedTheory | `Prop` | I4.86 |
| `CompletedOI.lean:327` | ObserverRecursion | `Prop` | I4.87 |
| `CompletedOI.lean:418` | OIPlus | `Prop` | I4.88 |
| `CarrierGeneralOIPlus.lean:73` | ObservationalIndependence | `Prop` | I4.96 |
| `CarrierGeneralOIPlus.lean:110` | ReversibleRichness | `Prop` | I4.99 |
| `CarrierGeneralOIPlus.lean:185` | OIPlus | `Prop` | I4.102 |
| `ImplementationLocality.lean:250` | Realized | `Prop` | I4.25 |
| `ImplementationLocality.lean:268` | InstAvail | `predicate` | I4.26 |
| `ImplementationLocality.lean:352` | ImplementationGenerated | `Prop` | I4.28 |
| `ImplementationLocality.lean:359` | ContextStable | `Prop` | I4.29 |
| `ImplementationLocality.lean:364` | LabelInvariant | `Prop` | I4.30 |
| `ImplementationLocality.lean:370` | ImplementationLocality | `Prop` | I4.31 |
| `ImplementationLocality.lean:506` | Architecture | `Prop` | I4.32 |
| `ImplementationLocality.lean:1053` | OIPlusLocal | `Prop` | I4.42 |
| `MinimalRepertoire.lean:423` | PhaseFreeRichness | `Prop` | I4.118 |
| `MinimalRepertoire.lean:544` | OIPlusMin | `Prop` | I4.120 |
| `MinimalRepertoire.lean:634` | CyclicRichness | `Prop` | I4.123 |
| `PositivePackage.lean:35` | OIPlusPos | `Prop` | I4.124 |
| `MicroscopicReversibility.lean:88` | InverseAccessibility | `Prop` | I4.127 |
| `MicroscopicReversibility.lean:93` | LieRankRichness | `Prop` | I4.128 |
| `MicroscopicReversibility.lean:216` | DaggerStable | `Prop` | I4.132 |
| `MicroscopicReversibility.lean:223` | ReversibleImplementationLocality | `Prop` | I4.133 |
| `MicroscopicReversibility.lean:238` | UnitaryRaySaturated | `Prop` | I4.134 |
| `MicroscopicReversibility.lean:336` | OIPlusMicro | `Prop` | I4.137 |
| `StructuralClosure.lean:183` | StructurallyClosed | `Prop` | I4.45 |
| `StructuralClosure.lean:401` | ExtendsSubstratum | `Prop` | I4.50 |
| `SubstratumSource.lean:77` | DrivesElementary | `Prop` | I4.143 |
| `SubstratumSource.lean:86` | QuantumArchitecture | `Prop` | I4.144 |
| `SubstratumInterface.lean:75` | IsMonomial | `Prop` | I4.148 |
| `SubstratumInterface.lean:180` | MonomialSource | `Prop` | I4.149 |
| `ReadWriteControl.lean:158` | ReadWriteSourced | `Prop` | I4.156 |
| `LiftAudit.lean:112` | LayerFlowExecutable | `Prop` | I4.56 |
| `LiftAudit.lean:745` | SubstratumAvail | `Prop` | I4.60 |
| `C5Discovery.lean:71` | KillBattery | `Prop` | I4.172 |
| `C5Discovery.lean:221` | PolGen | `predicate` | I4.174 |
| `StateMixingCoupling.lean:56` | MixR | `predicate` | I4.175 |
| `PairFlowEquivalence.lean:48` | PairFlowSourced | `Prop` | I4.179 |
| `CoherentContinuumSource.lean:135` | NonMonomialCountablyCovered | `Prop` | I4.182 |
| `CoherentContinuumSource.lean:143` | UncountableNonMonomialRays | `Prop` | I4.183 |
| `EmbeddedObservation.lean:98` | RegroupingInvariant | `Prop` | I4.107 |
| `EmbeddedObservation.lean:106` | RelabellingInvariant | `Prop` | I4.108 |
| `EmbeddedObservation.lean:114` | IsAmbientMember | `Prop` | I4.109 |
| `EmbeddedObservation.lean:123` | EmbeddedObservation | `Prop` | I4.110 |
| `EmbeddedObservation.lean:366` | OIPlusEmbedded | `Prop` | I4.115 |
| `ReferenceExtension.lean:98` | IsReferencePositive | `Prop` | I4.2 |
| `ReferenceExtension.lean:106` | IsThreePositive | `Prop` | I4.23 |
| `ReferenceExtension.lean:447` | HasParallelReferenceExtension | `Prop` | I4.3 |
| `ReferenceExtension.lean:469` | HasQutritReferenceExtension | `Prop` | I4.4 |
| `SpectatorBridge.lean:180` | IsSpectatorExtension | `Prop` | I4.12 |
| `SpectatorBridge.lean:223` | InertSpectatorCompositionality | `Prop` | I4.14 |
| `SpectatorBridge.lean:396` | HCompRealized | `Prop` | I4.18 |
| `TypedCompletion.lean:291` | ShadowQuantum | `Prop` | I4.187 |
| `TypedCompletion.lean:448` | IsTypedKrausInstrument | `Prop` | I4.188 |
| `QuasilocalAlgebra.lean:738` | IsStateFamily | `Prop` | I4.196 |
| `QuasilocalCharacterization.lean:196` | IsState | `Prop` | I4.202 |
| `QuasilocalCharacterization.lean:475` | LocalityPreserving | `Prop` | I4.204 |
| `OperationalRigidity.lean:647` | OrderIsoHyp | `Prop` | I4.213 |
| `PassiveObservation.lean:203` | IsPassiveInstrument | `Prop` | I4.217 |
| `PassiveObservation.lean:208` | SeparatesStates | `Prop` | I4.218 |
| `PassiveIndependence.lean:74` | PassivelyIncomplete | `Prop` | I4.220 |
| `PassiveIndependence.lean:103` | KeepsLabels | `Prop` | I4.221 |
| `PassiveIndependence.lean:288` | PassivelyCompleteOnDiagonal | `Prop` | I4.222 |
| `PassiveQuotient.lean:234` | ObservationCongruence | `Prop` | I4.226 |
| `PassiveQuotient.lean:240` | PassivelyMinimal | `Prop` | I4.227 |

Out of scope (admissible reasons only):

| census entry (file:line) | keyword | name | reason |
|---|---|---|---|
| `MinimalRepertoire.lean:208` | IsRealAntisym | `Prop` | a theorem-internal auxiliary (closure class of the colour-phase Lie algebra `colourAlg`, MinimalRepertoire.lean:250, used for the bipartite obstruction) |
| `MinimalRepertoire.lean:311` | ColourCompatible | `Prop` | a theorem-internal auxiliary (hypothesis of not_hControl_of_colourCompatible, MinimalRepertoire.lean:353, an obstruction lemma) |
| `StructuralClosure.lean:98` | IsSubmonomial | `Prop` | a definition with no hypothesis role (the elementwise form of IsMonomial; monomial_iff_submonomial, StructuralClosure.lean:169) |
| `QuasilocalAlgebra.lean:104` | AgreeOffG | `Prop` | a theorem-internal auxiliary (agreement off a finite set, used by agreeOffG_map, QuasilocalAlgebra.lean:942) |
| `PassiveObservation.lean:288` | IsDiagonal | `Prop` | a theorem-internal auxiliary (diagonal matrices, used by the pinching lemmas, PassiveObservation.lean:299-:342) |
| `PassiveIndependence.lean:98` | SuppAnc | `Prop` | a theorem-internal auxiliary (ancilla support predicate used by KeepsLabels and the label theory, PassiveIndependence.lean:103-:150) |

## (b) Manuscript census — cross-references only (all *out of scope: I2*, the kernel statement kept)

The launch assigns GR.md ~205–270 and Main.md ~540–570 to thread I2. Every paragraph or display in GR.md 206–272
and Main.md 538–570 that states an axiom, condition, principle or theorem is listed, with the I4 kernel records
it cites or restates; Main.md:628 is added because the stage-5 protocol cites it (candidate ε). No verdict is
given on any manuscript sentence.

| manuscript line | statement (short form) | kernel records kept (I4) |
|---|---|---|
| GR.md:206 | coherent-completion classification, scope conditions | — (I2's classification; no I4 kernel record) |
| GR.md:208 | boxed: OI + coherent completion + positive thermodynamic orientation ⟹ QM | — |
| GR.md:210 | two substantive questions remain | — |
| GR.md:212 | the operational-completion characterization; conditions (i)–(v) defined | I4.65, I4.66, I4.69, I4.14, I4.67, I4.68 |
| GR.md:214 | Theorem (operational-completion characterization) | I4.71, I4.72 |
| GR.md:216 | (i),(ii) well-formedness; (iii)–(v) substantive; five-way minimality; `oi_alone_not_qm` | I4.73, I4.74, I4.75, I4.76, I4.78 |
| GR.md:218 | boxed: bare finite OI ⇏ QM | I4.76 |
| GR.md:222 | boxed: OI-compatible theory + (i)–(v) ⟺ finite operational QM | I4.77, I4.78 |
| GR.md:224 | kernel citation; the OI clause does no work under full control | I4.77, I4.78, I4.79 |
| GR.md:226 | Quantum-complete OI (OI⁺) introduced | I4.79, I4.88, I4.102 |
| GR.md:228 | 1. Observational independence | I4.3, I4.82, I4.96, I4.98 |
| GR.md:230 | 2. Reversible richness | I4.85, I4.99 |
| GR.md:232 | 3. Observer recursion | I4.87 |
| GR.md:234 | "With these definitions, the kernel proves" | — |
| GR.md:236 | boxed: OI⁺ ⟺ exact finite endomorphic operational QM | I4.103, I4.104 |
| GR.md:238 | `carrier_general_oiPlus`; OI⁺ is completed OI | I4.80, I4.91, I4.104 |
| GR.md:240 | an axiomatic completion theorem, not a derivation from bare OI | I4.95, I4.105 |
| GR.md:242 | primitive-source form of OI⁺ | I4.42, I4.120, I4.124 |
| GR.md:244 | 1. Implementation locality | I4.26, I4.28, I4.29, I4.30, I4.31, I4.37 |
| GR.md:246 | 2. Phase-free richness | I4.118 |
| GR.md:248 | 3. Embedded observation | I4.110, I4.111, I4.112, I4.113 |
| GR.md:252 | boxed: implementation locality + phase-free richness + embedded observation ⟺ exact QM | I4.121, I4.122 |
| GR.md:254 | holds on every nonempty finite carrier; not a claim that bare OI entails the principles | I4.27, I4.122 |
| GR.md:256 | substratum-source form (an implementation architecture) | I4.45, I4.143, I4.144, I4.46 |
| GR.md:258 | boxed: current OI substratum + continuous off-diagonal controllability ⟺ exact QM | I4.51, I4.52, I4.53 |
| GR.md:260 | not a derivation; controllability not entailed by A1–A6 | I4.49, I4.143 |
| GR.md:262 | layer-flow form | I4.56, I4.61 |
| GR.md:264 | boxed: within the substratum's closure with phases, exact QM ⟺ one layer flow executable | I4.161, I4.62 |
| GR.md:266 | kernel citation `derivedOI_qm_iff_layerFlowExecutable'`; necessity via control | I4.161, I4.57 |
| GR.md:268 | boxed: stated substratum dynamics with observer access ⇏ one layer flow executable | I4.165, I4.59, I4.58 |
| GR.md:270 | the equivalence is exact; the sourcing of the hypothesis is not | I4.56 |
| GR.md:272 | typed form | I4.190, I4.186, I4.187 |
| Main.md:538 | Proposition (finite-substratum operational obstruction) | — |
| Main.md:540 | Remark (why the geometry alone cannot do it) | — |
| Main.md:542 | Remark (the operational-extension boundary) | — (I2's scope by name) |
| Main.md:544 | Theorem (finite operational realization and gluing, ε-form) | — |
| Main.md:546–554 | clauses (1)–(5) of that theorem | — |
| Main.md:556 | Rounding Lemma | — |
| Main.md:558 | Proof (construction and bound) | — |
| Main.md:560 | Corollary (single controlled dynamics) | — |
| Main.md:562 | Remark (what the gluing theorem does and does not deliver) | — |
| Main.md:564 | OI⁺ as a layered formulation | I4.88, I4.102 |
| Main.md:566 | display: OI⁺ ⟺ exact finite endomorphic operational QM | I4.90, I4.103, I4.104 |
| Main.md:568 | independence of the added principles; primitive-source, substratum-source, typed and quasilocal forms | I4.95, I4.104, I4.121, I4.122, I4.126, I4.131, I4.46, I4.52, I4.158, I4.190, I4.194, I4.199, I4.205, I4.207, I4.208, I4.209 |
| Main.md:570 | passive observation, kept apart | I4.219, I4.223, I4.224, I4.228 |
| Main.md:628 | (ii) visible-sector tensor product; dynamical causal separation (stage-5 candidate ε) | — (no I4 kernel record states it) |

Rows: 46 (GR.md 32, Main.md 14). Rows citing at least one I4 kernel record: 32.

## (c) Roadmap census — `verification/ROADMAP.md` rows and bullets naming I4 modules or obligations

| ROADMAP line(s) | item | disposition |
|---|---|---|
| 68 | P1 K row: K3 CONDITIONAL (citing `genTheory_qm_of_quantumArchitecture`, `typed_determined_iff`), Kₙ OPEN | mapped: I4.237 (K3), I4.233 (Kₙ); its K1, K2, K∞ parts out of scope: I3 |
| 70 | P1 H-∞ row (CoherentContinuumSource, quasilocal audits), OPEN | mapped: I4.238 |
| 75 | P3 GR states → Level-III quasilocal states, OPEN | out of scope: I2 (GR physical layer; Level III manuscript statements) |
| 773, 823 | `SubstratumInterfaceAudit.lean`'s `Substratum` structure (manuscript axioms) | out of scope: I1 |
| 936–951 | H-∞ section text and links | mapped: I4.238 |
| 973–977 | K section preamble: the finite characterization (`oiPlus_iff_qm`, `typed_determined_iff`) has quantum kinematics in its premises | mapped: I4.237, I4.103, I4.190 |
| 978–983 | K3 bullet, CONDITIONAL | mapped: I4.237 |
| 984–1006 | K1 and K2 bullets (K2: local tomography, the composite cone, local actions compatible with it; OPEN) | out of scope: I3 (named in I4's bridge notes as the field-neutral form of the missing spectator clause) |
| 1007–1057 | K∞ bullet and its eight obligations | out of scope: I3 |
| 1058–1069 | Kₙ bullet, OPEN | mapped: I4.233 (with the landed audit I4.234, I4.235, I4.236) |
| 1091 | finite route: "Kₙ (the operational architecture at every finite carrier)" | mapped: I4.233 |
| 1100–1101 | links to SubstratumSource.lean, TypedCompletion.lean | mapped: I4.237 |
| 1148–1156 | P3 section: GR states → Level-III quasilocal states | out of scope: I2 |
| 1392–1403 | Settled negatively — INDEPENDENT table (phases; dense control; executable intermediate layer flow; observer-level lift) | mapped: I4.239 |
| 1405–1420 | the table's commentary and audit links | mapped: I4.239 |

Rows: 15; mapped 10; out of scope 5 (I1: 773/823 counted as one row; I2: 75, 1148–1156; I3: 984–1006, 1007–1057;
the out-of-scope parts of row 68 are counted under its mapped row).
