# I2 censuses — kernel (a), manuscript (b), roadmap (c), with the book mirrors (d) and the residual screen (e)

Thread I2, stage 6, step 1. Base L = `9f9f8257…`. All counts are taken from the final runs
`kernel_census.out` (run 3, replay byte-identical) and `manuscript_census.out` (run 6, replay byte-identical); the
mapping table is `census_map.tsv`. Records are in `INVENTORY.md` (ids I2.1–I2.113).

**Counts.** (a) kernel: 32 I2 modules, 72 entries, 72 mapped (57 to records, 4 not declarations, 7 out of scope:
I1, 4 out of scope: I4 — listed below); 38 further modules cited from I2's sections belong to I1 (2), I3 (1), I4 (35).
(b) manuscript: 593 keyword sentences on 332 lines in 26 sections, 332/332 lines mapped (to records or out of
scope: I1). (c) roadmap: 83 entries (4 queue rows, 79 bullets/bold-led paragraphs), 83/83 mapped; plus the
section prose of H-∞ (938–947), H-Bell (955–966) and P3 (1150–1153), mapped to I2.103, I2.102, I2.104.
Unmapped entries: none.

## (a) Kernel census

**Method.** `kernel_census.py` collects every backticked identifier of Lean-name shape in I2's sections (the same
26 manuscript ranges and 7 ROADMAP ranges as the manuscript census), resolves it to the declaring module(s) of
`OIBridge/`, adds every module named as `OIBridge/<M>.lean`, assigns ownership by the protocol's partition, and
lists, for the I2 modules, every `axiom`, `opaque`, `class`, and every Prop-valued `structure`/`def`/`abbrev`/
`inductive` (column-0 declarations, modifiers allowed). The protocol's literal pattern
`^(axiom|opaque|structure|class|def) ` matches all 72 entries (`lit=P`). Runs: run 1 failed (round labels and
single letters resolved to Lean names; kept), run 2 superseded by the section extension (kept), run 3 final.

**No `axiom`, no `opaque`** in the I2 modules; no column-0 `axiom` in any OIBridge module (`grep -c '^axiom '` = 0
over 214 files). The only premise-type item in the I2 modules is the `def … : Prop` `BGIntegerClassification`
(I2.28), an explicit premise of `twoBranch_of_BGClassification`.

**Bridge control (`checks.py`, check B).** None of the 32 I2 modules names or imports a pair-cone object
(`CompositeDimension`, `K2Guard`, `KInfFoundations`, `maxCone`, `cnot`, `prodState`, `dualW`, `NativeGate`,
`W 3`, `eball`); the countercontrol (`CompositeDimension.lean`, 247 hits) behaves.

| module:line | kind | name | maps to | role |
|---|---|---|---|---|
| CentralObservation:67 | def | BlockDiag | I2.23 | definition used in the statement |
| CentralObservation:71 | def | InBlock | I2.23 | definition used in the statement |
| CentralObservation:164 | def | IsBlockPassiveInstrument | I2.23 | hypothesis of the passive-observation theorems |
| CentralObservation:509 | def | SeparatesBlockStates | I2.23 | definition used in the statement |
| CoherentContinuumSource:135 | def | NonMonomialCountablyCovered | I2.103 | definition of the H-∞ audit's condition |
| CoherentContinuumSource:143 | def | UncountableNonMonomialRays | I2.103 | definition of the H-∞ audit's condition |
| CoherentContinuumSource:269 | class | (doc line "class has …") | — | not a declaration: doc-comment line beginning with "class" |
| CoherentLift:489 | def | ProjectorShellRepresentation | I2.26 | definition (existence side) |
| CoherentLift:1211 | def | TwoTimeCoherentLift | I2.26 | definition (existence side) |
| CoherentLift:1504 | def | ActionIntertwining | I2.26 | definition (existence side) |
| CoherentLift:1512 | def | ReadoutIntertwining | I2.26 | definition (existence side) |
| CoherentLiftGauge:101 | def | StrongAnchorStabilizer | I2.94 | definition of act 11's statements |
| CoherentLiftGauge:114 | def | WeakAnchorStabilizer | I2.94 | definition of act 11's statements |
| CoherentLiftGauge:124 | def | CoherentLift | I2.94 | hypothesis of act 11–13 theorems (26 signature uses) |
| CoherentLiftGauge:135 | def | GaugeRelated | I2.94 | definition of act 11's statements |
| CrossTimeInvariants:118 | def | ConstRightRelated | I2.96 | definition of act 13's statements |
| CrossTimeInvariants:123 | def | ConstLeftRelated | I2.96 | definition of act 13's statements |
| CubicIsotropy:61 | def | IsSign | I2.80 | definition used in the statement |
| CubicIsotropy:65 | def | OhInvariant | I2.80 | definition used in the statement |
| CubicIsotropy:218 | def | KernelOh | I2.80 | hypothesis of the isotropy theorem |
| DilationChoice:134 | def | AdmissibleDilationAt | I2.101 | definition of act 7's dilation-choice statements (module reached by the name collision `permMatrix_mem_unitaryGroup`) |
| DilationChoice:271 | def | MovesVisibleCandidate | I2.101 | as above |
| DilationChoice:284 | def | VisibleInvariance | I2.101 | as above |
| Equivalence:147 | def | Stochastic | I2.39 | class (S) in the theorem's statement |
| Equivalence:168 | def | RevReal.IsLaw | I2.39 | normalisation predicate of class (D) |
| Equivalence:182 | def | RevRealizable | I2.39 | class (D) in the theorem's statement |
| Equivalence:201 | def | QfbReal.IsLaw | I2.39 | unitarity and normalisation of class (Q_fb) |
| Equivalence:216 | def | QfbRealizable | I2.39 | class (Q_fb) in the theorem's statement |
| EquivalenceChain:197 | def | IsDiag | I2.60 | definition used by `isDiag_Phi` |
| GramTrajectorySelection:61 | class | (doc line "class is …") | — | not a declaration: doc-comment line |
| GramTrajectorySelection:121 | def | GramTrajEquiv | I2.100 | act 17's cross-time equivalence |
| GramTrajectorySelection:131 | def | SelectsAt | I2.100 | act 17's candidate-selection predicate |
| InternalObserver:63 | def | Records | I2.23 | definition used in the statement |
| InternalObserver:68 | def | IsInternalObserver | I2.23 | hypothesis of the internal-observer theorems |
| OperationalSourcing:819 | def | RepUnitary | I2.25 | definition with no hypothesis role in the cited theorems (0 signature uses) |
| OrientationClosure:151 | def | OrientedShellRepresentation | I2.38 | named orientation premise |
| OrientationClosure:165 | def | ReadoutSeparating | I2.26 | definition used in the orientation statements |
| OrientationSelection:206 | class | (doc line "class as …") | — | not a declaration: doc-comment line |
| PassiveIndependence:74 | def | PassivelyIncomplete | I2.23 | definition used in the statement |
| PassiveIndependence:98 | def | SuppAnc | I2.23 | definition used in the statement |
| PassiveIndependence:103 | def | KeepsLabels | I2.23 | hypothesis of the passive-independence theorems |
| PassiveIndependence:288 | def | PassivelyCompleteOnDiagonal | I2.23 | definition used in the statement |
| PassiveObservation:203 | def | IsPassiveInstrument | I2.23 | hypothesis of `no_complete_passive_observation` |
| PassiveObservation:208 | def | SeparatesStates | I2.23 | definition used in the statement |
| PassiveObservation:288 | def | IsDiagonal | I2.23 | definition used in the statement |
| RegionTower:93 | def | AgreeOff | I2.36 | definition of the Level III state-selection audit |
| RegionTower:249 | def | DependsOnlyOn | I2.36 | as above |
| RegionTower:319 | def | Consistent | I2.36 | consistency of region-state families (Level III) |
| SecondOrderCircuit:518 | structure | IsGateList | I2.37 | hypothesis of the depth-two circuit theorems |
| Separability:83 | def | PosSemidefOn | I2.21 | definition used in the statement |
| Separability:130 | def | Separable | I2.21 | definition used in the statement |
| Separability:254 | def | EntanglementBreaking | I2.21 | the property the threshold theorem characterizes |
| ShellAssignment:149 | def | ShellRepresentationConsistency | I2.38 | named existence premise |
| SubstratumInterfaceAudit:84 | def | A1 | out of scope: I1 | substratum axiom A1 as a kernel definition (0 signature uses in I2's theorems) |
| SubstratumInterfaceAudit:87 | def | A2 | out of scope: I1 | substratum axiom A2 |
| SubstratumInterfaceAudit:91 | def | A3 | out of scope: I1 | substratum axiom A3 |
| SubstratumInterfaceAudit:94 | def | A4Exact | out of scope: I1 | substratum axiom A4 (exact form) |
| SubstratumInterfaceAudit:98 | def | A4 | out of scope: I1 | substratum axiom A4 |
| SubstratumInterfaceAudit:102 | def | A5 | out of scope: I1 | substratum axiom A5 |
| SubstratumInterfaceAudit:131 | def | A3Family | out of scope: I1 | substratum axiom A3, family form |
| SubstratumInterfaceAudit:231 | def | IsScaledPartialPerm | out of scope: I4 | substratum-interface definition; module reached only through `permClass` (ROADMAP.md:63) |
| SubstratumInterfaceAudit:370 | class | (doc line "class is …") | — | not a declaration: doc-comment line |
| SubstratumInterfaceAudit:485 | def | BijectionLevel | out of scope: I4 | substratum-interface definition |
| SubstratumInterfaceAudit:505 | def | PreservesNonneg | out of scope: I4 | substratum-interface definition |
| SubstratumInterfaceAudit:619 | def | SourcedOI | out of scope: I4 | substratum-interface definition (sourced OI class) |
| ThermalOrientation:192 | def | StrictlyPassive | I2.27 | definition used in the orientation corollary |
| ThermalOrientation:195 | def | Passive | I2.27 | hypothesis of the orientation corollaries |
| ThermalOrientation:318 | def | OperationalTransitionIdentification | I2.38 | named orientation premise |
| TrackBQfbBridge:297 | def | IsFlatHadamard | I2.25 | hypothesis of the flat instance theorems |
| TurnpikeScopeTransfer:542 | def | BGIntegerClassification | I2.28 | explicit premise (assumed) |
| WeylLift:246 | def | Indep | I2.21 | hypothesis of the Lagrangian-tuple lemmas |
| WeylTwirl:244 | def | Isotropic | I2.21 | hypothesis of the threshold theorem |

**Out-of-scope modules (38), cited from I2's sections.** I1 (2): `C3Necessity` (C1–C4 module), `OIRealization`
(realization of the sealed core). I3 (1): `CompositeDimension` (reached through `corner_form`, a name it shares
with `JordanClassification`). I4 (35): by the protocol's module list — `CarrierGeneralOIPlus`, `CompletedOI`,
`DerivedQ3`, `EmbeddedObservation`, `ExecSource`, `GeneralCarrier`, `ImplementationLocality`,
`JordanClassification`, `LiftAudit`, `LiftSource`, `MicroscopicReversibility`, `MinimalRepertoire`,
`OperationalRigidity`, `PhaseSource`, `PositivePackage`, `PositiveReachability`, `QuasilocalAlgebra`,
`QuasilocalCharacterization`, `ReadWriteControl`, `SecondOrderDrive`, `StructuralClosure`, `SubstratumInterface`,
`SubstratumSource`, `TypedCompletion`, `TypedPositive`; by the protocol's scope sentence (kernel side of the
operational-completion characterization and OI⁺, cited only from GR 212–276 / Main 564–568) — `AncillaClosure`,
`DiagonalTheory`, `DimensionalCountermodel`, `IsometryExtension`, `KrausSoundness`, `LevelOneSeam`,
`LieRankSource`, `OperationalValidity`, `PhysicalCharacterization`, `RankGapTheory`.

**Identifiers not resolved to a Lean declaration:** `fiber_freedom` (a probe name, Main.md:598 — I2.45 is
probe-certified, no kernel anchor), and the backticked module names `RegionLimit`, `CoherentContinuumSource`
(resolved as modules).

## (b) Manuscript census

**Sections (26; identical in both scripts).** Main 14–22 (abstract), 82 (§1.3 theorem statement), 95–99 (§1.5),
101–196 (§2), 200–656 (§3.1–§3.5), 660–678 (§4.1–§4.2), 696–720 (§4.5), 722–740 (§4.6), 744–756 (§5); GR 164–296
(§3.3), 326–330 (§6.1 tensor product, H-local-lift), 709–866 (Appendix A); SM 10–16, 40–95 (§2), 96–165 (§3.1),
216–279 (§4.1), 535–566 (§4.8), 1354–1369 (§8.2), 1576–1635 (Appendix A); Substratum 12–40, 42–65 (§2), 70–173
(§3.1–§3.3), 186–195 (§3.5), 236–242 (§5, ER=EPR), 414–416 (§6.3), 430 (§6.4 Bell/Tsirelson test). Main §1.1–§1.4
(axioms, Definition, Lemmas 1–3, C1–C4) are I1's and were not censused by I2, except the theorem-statement
paragraph (82).

**Entry rule.** A census entry is a sentence matching the protocol's keyword list (Axiom, Condition, C1–C4,
(i)–(v), H-, K, A1–A6, Theorem, Lemma, Principle, Assumption, boxed statements; added: Proposition, Corollary,
hypothesis). Sentences are mapped by their line (paragraph) through `census_map.tsv`; `manuscript_census.out`
prints every line with its sentence count, keys and mapping.

| section | keyword sentences | section | keyword sentences |
|---|---|---|---|
| Main 14–22 | 4 | SM 10–16 | 6 |
| Main 82 | 4 | SM 40–95 | 11 |
| Main 95–99 | 2 | SM 96–165 | 40 |
| Main 101–196 | 38 | SM 216–279 | 25 |
| Main 200–656 | 216 | SM 535–566 | 27 |
| Main 660–678 | 4 | SM 1354–1369 | 13 |
| Main 696–720 | 14 | SM 1576–1635 | 11 |
| Main 722–740 | 23 | Substratum 12–40 | 13 |
| Main 744–756 | 3 | Substratum 42–65 | 8 |
| GR 164–296 | 35 | Substratum 70–173 | 50 |
| GR 326–330 | 5 | Substratum 186–195 | 13 |
| GR 709–866 | 27 | Substratum 236–242, 414–416, 430 | 0, 0, 1 |

Total: 593 keyword sentences on 332 lines; 332 lines mapped, 0 unmapped.

**Mapping summary (lines whose mapping names the record).** I2.1:1 I2.2:1 I2.3:1 I2.4:1 I2.5:5 I2.6:1 I2.7:1
I2.8:2 I2.11:3 I2.12:7 I2.15:1 I2.16:3 I2.17:1 I2.18:1 I2.19:2 I2.20:5 I2.21:12 I2.22:13 (12 of them through the
note "320 also I2.22" of the I2.21 range) I2.26:4 I2.27:7 I2.29:3 I2.30:3 I2.31:3 I2.32:2 I2.33:3 I2.34:2 I2.35:1
I2.36:1 I2.39:2 I2.40:2 I2.41:11 I2.42:6 I2.43:7 I2.44:3 I2.45:1 I2.47:2 I2.48:5 I2.49:1 I2.50:4 I2.51:2 I2.52:1
I2.53:3 I2.54:6 I2.55:3 I2.56:5 I2.57:8 I2.58:3 I2.59:3 I2.60:4 I2.61:1 I2.62:1 I2.63:1 I2.64:4 I2.65:5 I2.67:6
I2.68:2 I2.69:8 I2.70:4 I2.71:3 I2.72:8 I2.73:4 I2.75:2 I2.76:2 I2.77:5 I2.79:1 I2.80:17 I2.81:11 I2.82:9 I2.83:8
I2.84:7 I2.85:2 I2.87:9 I2.88:9 I2.89:22 I2.102:2 I2.105:6 I2.106:10 I2.107:1 I2.108:1 I2.109:16 I2.111:1
I2.112:1.
Records not named by any line mapping (located by reading: their source lines carry no keyword sentence, or are
mapped to a neighbouring record's range — e.g. GR 178 within I2.27's range for I2.28 — or they come from the
ROADMAP, the kernel or the book): I2.9, I2.10, I2.13, I2.14, I2.23, I2.24, I2.25, I2.28, I2.37,
I2.38, I2.46, I2.66, I2.74, I2.78, I2.86, I2.90–I2.101, I2.103, I2.104, I2.110.

**Out of scope (whole line): 38 lines, 71 sentences — all I1.** Main 109 (slow-bath regime of C1/C2), 153–157
(C2 storage mechanism), 172–176 (C1–C4 separation and roles), 216–218 (Lemma 1 finiteness commitment), 419–421
(C1 witness, one-way coupling), 423–456 (ETH motivation; C2 necessity theorems; role of C2), 478–482 (ETH and
C2 status), 484–492 (C3 necessity and capacity corollary), 602 (which condition is primitive), 706 (posit ledger),
717–720 (C1–C4 necessity rows of the status ledger); Substratum 54 (effective finiteness, A1), 92–104 (axioms
A1–A6). A further 34 lines map to I2 records with a named clause out of scope: I1 (C1–C4, A-axiom, Lemma 1
clauses inside an I2 statement); `census_map.tsv` names the clause on each.

## (c) Roadmap census

**Sections.** ROADMAP rows 63 (P0, Track B), 67 (H-Bell), 70 (H-∞), 75 (P3, Level III); the P0 section 77–664
(acts 9–17 and the act-7 records); H-∞ 936–952; H-Bell 953–970; P3 1148–1157. Entries: queue rows, bullets and
bold-led paragraphs (`manuscript_census.out`, part (c), prints each with its mapping).

| range | entries | record |
|---|---|---|
| 63 | 1 | I2.90 |
| 67 | 1 | I2.102 |
| 70 | 1 | I2.103 |
| 75 | 1 | I2.104 |
| 79–89 (P0a) | 2 | I2.91 |
| 91–121 (P0b) | 7 | I2.92 |
| 123–127 (D3) | 1 | I2.93 |
| 129–188 (act 11) | 12 | I2.94 (180–186 also I2.93) |
| 189–244 (act 12) | 10 | I2.95 |
| 245–304 (act 13) | 10 | I2.96 |
| 305–384 (act 14) | 8 | I2.97 |
| 385–471 (act 15) | 9 | I2.98 |
| 472–540 (act 16) | 8 | I2.99 |
| 541–629 (act 17) | 9 | I2.100 |
| 630–664 (act-7 records, chronology guard) | 2 | I2.101 |
| 953–970 (H-Bell section; bold line 961) | 1 | I2.102 |
| 936–952, 1148–1157 (prose only) | 0 | I2.103, I2.104 |

Total 83 entries (77–664: 78), 83 mapped, 0 unmapped. Further rows that mention H-Bell outside these sections:
ROADMAP.md:909 (physical C4 discharge: "successor on this track is H-Bell") and :1006 (K section: "discharge
H-Bell") — mentions, not obligations; they are I1's (C4) and I3's (K) rows. Not in I2's rows and not censused:
P1 Lemma 24.1 (row 64; named as a dependency of I2.89), P2 Bekir–Golomb (row 71; named at I2.28), P2 H-link (row
72; named at I2.77).

## (d) Book mirrors (the book restates; it adds no record here)

`manuscript_census.out`, part (d), lists every book line containing each phrase. Summary (FULL = the consolidated
`The-Incompleteness-of-Observation-FULL.md`, whose chapters mirror `ch*.md`):

| phrase | record | hits | files |
|---|---|---|---|
| `Q_{\mathrm{fb}}` | I2.39 | 57 | FULL 28; ch01 6; ch19 5; appendix-b 4; ch00 3; glossary 3; ch09 2; ch18 2; README, appendix-c, ch02, ch11 1 each |
| hidden predictive memory | I2.44 | 19 | FULL 9; ch02 3; ch00 2; ch01, ch18, glossary, preface, README 1 each |
| predictive quotient | I2.45 | 0 | — (the canonical predictive quotient is not restated in the book) |
| process dilation | I2.40 | 0 | — (not restated under that name) |
| Stinespring | I2.19, I2.59 | 54 | FULL 26; appendix-b 7; appendix-c 6; ch02 4; others ≤ 2 |
| P-indivisib | I2.48, I2.50 | 183 | FULL 91; ch01 23; appendix-b 10; ch15 9; ch17 7; ch18 7; others ≤ 6 |
| causal cone | I2.1, I2.2 | 22 | FULL 10; README, appendix-c, ch00, ch01, ch02 2 each; ch03, ch04 1 each |
| Bell ceiling | I2.5 | 4 | FULL 2; appendix-c 1; ch18 1 |
| ontic parameter dependence | I2.6 | 39 | FULL 19; ch03 6; ch04 3; others ≤ 2 |
| no-signal | I2.10 | 45 | FULL 22; ch01 5; appendix-c 4; ch03 4; others ≤ 2 |
| H-Bell | I2.102 | 39 | FULL 19; ch02 11; ch03 3; others 1 |
| local tomography | I2.2, I2.3, I2.63 | 0 | — (the book does not name the local-tomography boundary) |
| gluing | I2.12 | 4 | FULL 2; ch19 1; glossary 1 |
| Kochen | I2.14 | 39 | FULL 19; ch04 6; ch03 5 (KS inheritance: FULL:1042, ch03:168); others ≤ 2 |
| inert spectators | I2.29 | 4 | FULL 2; ch01 1; ch19 1 |
| OI⁺ | I2.31 | 4 | FULL 2; ch01 1; ch19 1 |
| operational-completion | I2.29 | 2 | FULL 1; ch19 1 |
| quasilocal | I2.36 | 4 | FULL 2; ch01 1; ch19 1 |
| tensor product | I2.19, I2.2 | 8 | FULL 4; appendix-b 2; ch06 1; ch08 1 |

Record-only observations (no action; read-only): the book carries no restatement of I2.45 or I2.40 by name and
never names local tomography, so the corpus's explicit statements that local tomography / composite completeness
is not established (I2.2, I2.3, I2.63) have no book mirror under that term.

## (e) Residual screen (lines outside the sections with a composition/locality/operation term)

`manuscript_census.out`, part (e). Screen terms: composite, tensor product, no-signal, locality, causal cone,
spectator, Bell, subsystem, local tomography, operational, trace-out, bipartite, Kochen. After the section
extension (run 5): Main 13 lines, GR 31, SM 52, Substratum 35. Classification by block:

- **Main (13).** 30 (§1.1; restates the coherent-instrument/composite boundary — mirror of I2.69); 44, 50, 74, 80
  (Definition, Lemma 2, C1 and C4 definitions — out of scope: I1); 686–692 (§4.4 relation to prior work — no
  constraint stated); 818–886 (reference list).
- **GR (31).** 20 (abstract — mirror of I2.16/I2.29); 60–76 (§2.3 horizon application: H-state, H-balance,
  H-slope, gravity-track hypotheses of ROADMAP P2 row 73, not I2's rows; :76 restates that the composite and
  coherent instrument lift is open — mirror of I2.69); 118 (§3.2 proof step: coupling chain V ↔ B ↔ D by spatial
  locality — the same premise as I2.109); 306 (§4 self-consistency of ε — physical layer); 340–362 (§6.2–§6.3
  cosmological-constant problem, trace-out ordering — physical layer); 376–452 (§7 dark energy and dark sector,
  trace-out ontology — physical layer); 530, 551 (§7.3–§7.4: temporal non-locality of the sourcing; the magnitude
  question reduced to emergent locality — physical layer, linked to SM §3.1 emergent-Lorentz problem, I2.106);
  585–601 (§8.4 assumptions — mirrors of I2.62 and I2.20); 649 (§8.5 component-blind trace-out, H-blind — SM
  physical-carrier bridge); 943 (reference list).
- **SM (52).** 32 (tier-2 conditional carrier chain, H-blind); 292 (§4.2: chaotic mixing underlying operational
  measurement independence — mirror of I2.5's hypothesis (iv)); 422–533 (§4.6–§4.7 gauge group and fermion
  embedding after the trace-out; Schur-complement trace-out; tensor products of carrier representations — physical
  layer, gauge structure); 627–641 (§5 strong CP: the bipartite C4 ring counterexample — physical layer); 791 (§6
  gauge coupling — physical layer); 891–1273 (§7 predictions, composite Higgs — "composite" in the particle sense);
  1410–1562 (§8.3–§8.8 trace-out map, baryon number, composite-Higgs protection — physical layer); 1736 (reference).
  Not censused sentence by sentence: SM §4.4 (multi-component dynamics and gauge structure) and §6 (gauge
  coupling prediction) — screened only; no sentence there was found stating a constraint on observers or composites
  in the operational sense. This is a stated limitation, not a result.
- **Substratum (35).** 68 (§3 overview of the composite theorem — mirror of I2.89); 198–234 (§3.6 remarks: the
  Bell-inclusive substratum not unique — mirror of I2.89/I2.102); 264–266 (§4 amplitude-scale gauge, "adjoined as
  an explicit operational principle", status open — the linearity premise A5: out of scope: I1); 300–350 (§5
  synthesis, three projections through the trace-out — physical layer); 370 (§5.5); 382–402 (§6.1–§6.2 structural
  realism: Bell-completion structure left open — mirror of I2.89/I2.102); 427–428 (§6.4 falsification: exotic
  matter — physical layer); 491–495 (§7 conclusion — mirrors).

In-scope items the screen found outside the first section list (run 3) were added as records I2.107–I2.111 and
their lines added to both scripts' sections (kernel census run 3; manuscript census runs 4–5): GR 326–330, GR
753–866, Substratum 236–242, 414–416, 430. I2.112 (H-blind, SM.md:12 and Proposition 4b at SM.md:328) was added
after run 5 by reading SM §4.4; the map of SM:12 names it (manuscript census run 6). I2.113 (H-observer-bundle,
H-Y-vertex, SM.md:791) was added by reading SM §6; its lines lie outside the census sections and no census
line names it.
