# I1 CENSUS — the three coverage controls (foundations; L = `9f9f8257…`)

Every count below is printed by a script in `pt/I1/` run as `python3 -I -B` with its decision rule
in its header, replayed byte-identically (outputs and hashes: RESULT.md §4). Record ids refer to
INVENTORY.md. "OOS" = out of scope, with the admissible reason the protocol allows.

## (a) Kernel census — `kernel_census.py` → `kernel_census.out`

**Scope rule.** Whole-module census of the twelve modules whose subject is I1's (part A):
OIRealization, IndependenceCensus, ManuscriptAxioms, RouteB, SubstratumInterfaceAudit,
BackgroundIndependence, A6Instantiation, C3Necessity, CausalReadback, PhysicalC4Discharge,
PhysicalC4StorageReadback, InternalObserver; plus the single declaration `OICore` of
CompletedOI.lean (part A′; the rest of that module is named in I4's scope); plus a cross-tree token
census (part B) of every declaration anywhere in OIBridge whose *signature* mentions `OICore`,
`RealizesSealedOICore`, `CoreC1C4`, `SealedCoreIsFiniteOI`, `DerivedOICore`, `IsInternalObserver`,
`A1Realized`, `A2Realized` or `A1A2Realized`; plus the zero-import layer `verification/lean/*.lean`
(part C). Census entry = `axiom`/`opaque`/`class` (any type) or `structure`/`def` (and, as an
extension, `abbrev`/`inductive`) whose signature ends in `Prop`.

**Counts.** Part A: 41 census entries (0 `axiom`, 0 `opaque`, 0 `class`, 0 `structure … : Prop`,
41 `def … : Prop`; 0 extension entries); 376 theorems listed as material. Part A′: 1. Part B: 94
declarations in 18 modules. Part C: 10 heads (7 `class`, 3 `structure`, none `Prop`-valued, no
`axiom`). **No `axiom` and no `opaque` occurs in any I1 module.**

**Part A + A′ mapping (42 entries, all mapped).**

| entry (file:line) | record |
|---|---|
| OIRealization.lean:234 `RealizesSealedOICore` | I1.43 |
| OIRealization.lean:291 `SealedCoreIsFiniteOI` | I1.42 |
| IndependenceCensus.lean:187 `CoreC1C4` | I1.39 |
| IndependenceCensus.lean:549 `IsLocalOnB`, :554 `IsLocalOnVH` | I1.41 (folded definitions of the census theorem) |
| ManuscriptAxioms.lean:76 `A1Realized`, :83 `A2Realized`, :90 `A1A2Realized` | I1.55 |
| ManuscriptAxioms.lean:125 `ConfigurationLevel` | I1.56 |
| RouteB.lean:123 `ExchangesAvailable`, :128 `PhasesAvailable`, :133 `ReadWriteAvailable`, :141 `DerivedOI` | I1.49 |
| RouteB.lean:146 `DerivedOICore` | I1.50 |
| RouteB.lean:174 `FalsifierUnavailable`, :252 `RouteBTarget` | I1.51 |
| SubstratumInterfaceAudit.lean:84 `A1`, :87 `A2`, :91 `A3`, :94 `A4Exact`, :98 `A4`, :102 `A5`, :131 `A3Family` | I1.57 |
| SubstratumInterfaceAudit.lean:231 `IsScaledPartialPerm`, :485 `BijectionLevel`, :505 `PreservesNonneg`, :619 `SourcedOI` | I1.60 |
| BackgroundIndependence.lean:96 `PreservesPointwise`, :104 `A6Inv`, :111 `A6Glob`, :131 `A6Cov` | I1.61 |
| CausalReadback.lean:48 `IsRowStochastic`, :54 `PDivisible`, :58 `PIndivisibleWithin`, :62 `C4e`, :67 `C4r` | I1.70 |
| PhysicalC4Discharge.lean:68 `RoutedReadback` | I1.71 |
| PhysicalC4Discharge.lean:633 `LatticeCutReadback` | I1.73 |
| PhysicalC4StorageReadback.lean:69 `RoutedReadbackAtStorage` | I1.72 |
| InternalObserver.lean:63 `Records`, :68 `IsInternalObserver` | I1.75 |
| CompletedOI.lean:96 `OICore` | I1.47 |

Modules A6Instantiation and C3Necessity have 0 census entries; their theorems are recorded at
I1.62 and I1.32. Theorems of the twelve modules not named in a record are theorem-internal
auxiliaries or lemma-folded into the record whose theorem they serve (each record names its
folded lemmas); none is an `axiom`.

**Part B mapping (94 declarations: 82 mapped to I1 records, 12 OOS).**

| declarations (file:line) | record / OOS |
|---|---|
| CompletedOI.lean:96 | I1.47 |
| CompletedOI.lean:115, :549, :557 | I1.48 |
| CompletedOI.lean:475, :487, :496, :506 (`independence_independent`, `richness_independent`, `recursion_independent`, `oiPlus_independence`) | OOS: belongs to thread I4 (OI⁺ completion layer, named in I4's scope) |
| DiagonalTheory.lean:358, :398, :415 | I1.80 |
| EmbeddedObservation.lean:343, :351 | OOS: thread I4 (`EmbeddedObservation.lean`) |
| GeneralCarrier.lean:160, :168, :177, :188 | OOS: thread I4 (`GeneralCarrier.lean`; cited from I1.81) |
| ImplementationLocality.lean:207, :1035 | OOS: thread I4 (`ImplementationLocality.lean`) |
| IndependenceCensus.lean:187, :200 | I1.39 |
| IndependenceCensus.lean:811 | I1.41 |
| InternalObserver.lean:68, :116, :124, :137, :150, :162, :169, :206, :222, :315 | I1.75 |
| IsometryExtension.lean:257 | I1.81 |
| LevelOneRecursion.lean:46; LevelOneSeam.lean:320, :353; PhysicalCharacterization.lean:343, :364, :375 | I1.83 |
| ManuscriptAxioms.lean:76, :83, :90, :94, :98, :103, :107, :112 | I1.55 |
| OIRealization.lean:234 | I1.43 |
| OIRealization.lean:252, :260, :263, :266 | I1.44 |
| OIRealization.lean:291, :305 | I1.42 |
| OIRealization.lean:316, :324, :333, :343 | I1.45 |
| OIRealization.lean:360, :366 | I1.46 |
| PassiveIndependence.lean:237, :248, :255, :260, :269, :335 | I1.79 |
| RankGapTheory.lean:338, :688, :702 | I1.81 |
| RouteB.lean:146 | I1.50 |
| RouteB.lean:231 | I1.54 |
| RouteB.lean:257, :263 | I1.51 |
| RouteB.lean:318 (`target_of_substratum_core`) | I1.53 (lemma-folded) |
| RouteB.lean:375, :380 | I1.52 |
| RouteB.lean:395 | I1.53 |
| SubstantiveCensus.lean:394, :776, :828, :862, :891, :927, :935, :943, :950, :957, :964, :971, :978, :986, :1012 | I1.82 |
| SubstratumInterfaceAudit.lean:740, :753 | I1.60 |

**Part C (10 heads) — OOS.** `lean/OI_Gauge_Certificates.lean` (`Grp`, `AddCommGrp`, `Ch`, `El`),
`OI_Staggered_Relations.lean` (`Rng`, `Gens`), `OI_Structural_Chain.lean` (`CMon`),
`OI_Structural_Core.lean` (`Rng`, `CRng`), `OI_Time_Reversal.lean` (`AbGrp`): definitions with no
hypothesis role in I1's scope (algebraic carrier classes of the zero-import SM structural chain,
gauge certificates and time reversal); the layer's subject belongs to thread I2 (physical layer).

**Definitions met as dependencies, not censused here** (records belong elsewhere; INVENTORY §I):
`FiniteOperationalTheory`, `HasCompositeUnitaryControl`, `InertSpectatorCompositionality`,
`IteratedAncillaClosure`, `ExactFiniteEndomorphicQuantumOps`, `ExactAllFiniteEndomorphicQuantumOps`,
`PhaseFreeRichness`, `EmbeddedObservation`, `ReversibleImplementationLocality` — thread I4;
`HiddenMemory.Realization`, `capacity_floor_of_fun`, `tv`, `RootedRealization`, `rootedMap`,
`marg`, `horizon_verdict` — thread I2. `StochasticInterface.lean` (two theorems recorded at
I1.76) was not censused whole: its two cited theorems are recorded; its remaining declarations are
not in I1's records (stated as an incompleteness in RESULT.md §0).

## (b) Manuscript census — `census_ms.py` → `census_ms.out` (run 2; run 1 kept)

**Scope rule.** Main.md lines 24–659 (§1–§3); Methodology.md lines 239–286 (§6) with the declared
extension 160–163 (§4.6) and 216–238 (§5.4–§5.5); Substratum.md lines 88–130 (A1–A6, Stage 1
C1–C4) and 204–219 (A1–A6 remarks); Explainer.md, every sentence mentioning a condition or an
axiom; book/ch01-observation.md whole; every other book chapter, appendix and the glossary:
restatement sentences only (axiom/condition with its label); FULL.md: mirror check. A counted
sentence matches the census keywords (axiom, condition, C1–C4, (i)–(v), H-, K labels, A1–A6,
theorem, lemma, principle, assumption, hypothesis, definition, corollary, proposition, posit,
postulate, boxed). Mapping rules: line-anchored, then keyword, then section defaults (header of
`census_ms.py`); run 1 left 18 sentences unmapped, each read and given a manual mapping in run 2.

**Counts.** 946 sentences counted: Main 518, Methodology 71, Substratum 52, Explainer 74, ch01
168, other book files 63 (appendix-a 1, appendix-b 6, appendix-c 8, ch02 1, ch03 4, ch04 4, ch07 4,
ch09 3, ch10 1, ch11 3, ch12 3, ch13 4, ch14 1, ch15 4, ch16 2, ch17 1, ch18 8, glossary 5).
**Unmapped: 0.** Mirror check: all 231 counted book sentences have an identical sentence in FULL.md
(mirror=FULL 231, mirror=none 0); FULL-only restatement sentences: 0.

**Mapping counts (a sentence naming several items maps to each).**

| record | sentences | record | sentences | record | sentences |
|---|---|---|---|---|---|
| I1.1 | 35 | I1.13 | 1 | I1.25 | 5 |
| I1.2 | 33 | I1.14 | 6 | I1.26 | 17 |
| I1.3 | 45 | I1.15 | 14 | I1.27 | 5 |
| I1.4 | 9 | I1.16 | 2 | I1.28 | 10 |
| I1.5 | 6 | I1.17 | 5 | I1.29 | 5 |
| I1.6 | 5 | I1.18 | 6 | I1.30 | 7 |
| I1.7 | 7 | I1.19 | 8 | I1.31 | 11 |
| I1.8 | 2 | I1.20 | 120 | I1.32 | 7 |
| I1.9 | 5 | I1.21 | 134 | I1.33 | 4 |
| I1.10 | 11 | I1.22 | 36 | I1.34 | 3 |
| I1.11 | 4 | I1.23 | 113 | I1.35 | 7 |
| I1.12 | 7 | I1.24 | 87 | I1.36 | 1 |
| I1.63 | 8 | I1.64 | 5 | I1.65 | 4 |
| I1.66 | 3 | I1.67 | 3 | I1.68 | 8 |
| I1.69 | 8 | | | | |

The condition records I1.20–I1.24 collect both their defining sentences and every use-site in the
counted sections (a §2–§3 sentence that uses C2 maps to I1.21). I1.37 (Explainer's access-condition
reading) is anchored at Explainer.md:905, which the keyword rule sends to I1.20–I1.24.

**OOS (381 sentence-mappings).** belongs to thread I2: Main §2–§3 (P-indivisibility, dilation,
Bell, finite-horizon equivalence, characterization) 298; ch01 §1.5–§1.11 52; ch01 §1.1 5; Main
§1.1 problem statement (finite-horizon equivalence) 2; physical layer (named hypotheses H-*,
empirical inputs E1–E7, Theorem 23, Bell) 22; the structural observer-selection theorem (Main §4.6)
2.

## (c) Roadmap census — `census_rm.py` → `census_rm.out` (run 2; run 1 kept)

**Scope rule.** Every item of ROADMAP.md: table rows with a bold first cell, the finding rows of
"Settled negatively" (added in run 2), bulleted bold labels, `###` headings, `**Executed`
paragraphs, and the two unheaded accounting paragraphs (lines 38 and 1455). Mapping by obligation
(queue rows) or by enclosing section.

**Counts.** 96 items; **unmapped 0**; in scope 10:

| item | record |
|---|---|
| ROADMAP.md:38 (programme interpretation boundary) | I1.78 |
| ROADMAP.md:65 (queue row P1 A6, CONDITIONAL); :722 (section heading) | I1.61, I1.62, I1.68 |
| ROADMAP.md:66 (queue row P1 Physical C4 discharge, OPEN) | I1.74 |
| ROADMAP.md:838 (section heading), :845 (round C4-1), :870 (round C4-2) | I1.71, I1.72, I1.73, I1.74 |
| ROADMAP.md:69 (queue row P1 stochastic observer interface, OPEN); :918 (section heading) | I1.76 |
| ROADMAP.md:1455 (declared inputs and conditional hypotheses) | I1.77 |

**OOS (86).** thread I2: P0 and the Track B acts 36 (P0 row 1, P0 section 1, act sections 34
counted by heading/bullet), P0 geometry directions 5, Lemma 24.1 4, H-Bell 2, GR / Level III 4,
SM physical layer 1, other P2 physical layer 4, gauge/QFT 1, hydrodynamics 3, Bekir–Golomb 1,
not-prioritized items 5; threads I2/I4: H-∞ 2; threads I3/I4: K programme 7; thread I4: the four
"Settled negatively" sourcing findings (phases, dense control, layer flow, observer-level lift) 4;
a definition with no hypothesis role: the seven status-vocabulary rows 7. (Exact per-item lines in
`census_rm.out`.)
