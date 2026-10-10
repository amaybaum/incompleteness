# GRAPH — stage 6 (Q-EX-FULL), step 2: the dependency graph of the 633 inventory records

Thread G6. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only). Assignment:
`PROTOCOL-STAGE6-AMENDMENT-1.md` §A1.4 (`59019538…`), under `PROTOCOL-STAGE6.md` (`b277b7c1…`) and the binding
§4–§5 of `pt/audit/stage6-inputs/I-audit/AUDIT-I.md`. Machine-readable graph: `graph.tsv` (a byte copy of
`classify.out`; table `nodes`, one row per record: id, kind, status, level, class, sublabel, depends_on,
named_hypotheses, flag, derived, needs, external; table `edges`, one row per edge: src, dst, kind, xlevel,
supply, note). Per-item detail: `analyze.out` (sections S1–S5), the check: `check.out`. Decision vocabulary and
every rule: `NOTES.md` N1–N3, fixed before the step it governs; amendments are written into the script headers
and disclosed in NOTES.

## 0. Summary

- **Graph.** 633 nodes (I1.1–I1.85, I2.1–I2.113, I3.1–I3.187, I4.1–I4.248; ids kept). 1054 dependency
  edges: 801 recorded (`R`), 31 inherited from "as Ix.n" (`RA`), 70 to kernel or design names with no record
  (`RN`), 152 completed from the kernel signature at L (`KC`, on 122 nodes: I1 8, I2 14, I3 25, I4 75; each
  cites the declaration's file:line). 495 `yields` edges (`Y`) are listed and used only as a robustness control.
- **Item 1 (partition).** (a) 109: the two axioms; 103 premise-free statements (closed statements about defined
  objects, `a0`); one consequence of Axioms 1–2 alone, I1.3 (the non-derivability of Axiom 2, `a1`); three that
  add only an observation-base posit (I1.7, I1.8, I2.11, `a2`). (b) 15: C1–C4 themselves (I1.20–I1.24) and ten
  derived items, all manuscript H-level. (c) 172 need an operational hypothesis. (d) 36 need a physical
  hypothesis. (e) 301 have no derivation at L. No kernel declaration at level O, P, M or G is in (a1), (a2) or
  (b).
- **Item 2 (do-not-assume).** 75 rows carry the flag (I2 11, I3 20, I4 44). The general items stand at
  *assumed*, *open*, *PT-record*, *[D]* or *scope statement*; the flagged rows with a proved status are
  theorems about flagged objects (I2's manuscript statements, I3.80, I3.83, I4.210, I4.215, I4.216). No flagged
  item is a hypothesis of any derived node in the ancestor set of the pair objects; the flagged nodes inside
  that set are the seeds `actT`, `actC` and the (b) forms, and the single-token objects the (b) forms are
  stated with (I3.66 `ElementaryDrivability`, I3.80 `boundaryTransitive_fullAut3`).
  Discharges for particular objects exist at L only at the matrix level (e.g. `ContextStable` and
  `StructurallyClosed` for the substratum class by closed theorems; `HasParallelReferenceExtension` for the
  full theory; each listed in §3 with the premises of the discharging theorem).
- **Item 3 (meeting).** **NO-MEET.** The ancestor set of the pair objects (25 nodes) lies at levels P and O;
  the descendant set of Axioms 1–2 (31 nodes) lies at level H (manuscript records and two kernel H theorems).
  They share no node, with or without the `yields` edges, and with manuscript-asserted cross-level edges
  counted. The missing links are named by K∞ (I3.166–I3.173), K2 (I3.165), P-STAGE2 (I3.145), P-ACT2
  (I3.146), K1 (I3.164), and, for H3, no obligation at L.
- **Item 4 (check).** `check.py` (independent of the build scripts): C0 PASS, C1 PASS (every edge target
  exists), **C2 FAIL** (two 2-cycles in the recorded fields, I2.6 ⇄ I2.10 and I2.42 ⇄ I2.56, each between two
  assumed records), **C3 FAIL** (44 sampled theorems: 19 recorded fields agree with the signature, 21 are
  incomplete and completed by `KC`, 4 disagree: I2.25, I2.36, I2.96, I3.105); countercontrols behave; no
  VERDICT line. Both failures are statements about the step-1 records; no record is edited.
- **Item 5.** No status is changed (statuses are read verbatim from the records); proved lemmas are traversed
  to their own roots, never counted as premises; a cross-level edge is marked kernel-supplied or
  manuscript-asserted, and the meeting result holds under either reading.

## 1. Construction

**Nodes and fields.** `parse.py` reads I1–I3 `INVENTORY.md` and I4 `records.txt` (633 records; P1–P3 and
countercontrol PASS, `parse.out`). Kind, level, status and flag are the records' own strings.

**Edges** (`edges.py`, final run 4; E1–E3 PASS). An edge `u → v` reads "`u` uses `v`". Ids and id ranges of
`depends_on` are `R`; backticked or identifier-shaped names in `depends_on` are resolved to the record that
carries the name (`R`) or, failing that, to the declaration at L (`RN`, `K:<name>`) or in the design modules
(`D:<name>`); "as Ix.n" inherits Ix.n's `R` targets (`RA`). Kernel completion (`KC`): for a derived node with
kernel-proved status, every theorem named in its title or status (I4: the declaration at its `src` line) is
read at L; each declared argument whose type has a head naming a record or a Prop-valued / structure
declaration at L becomes an edge when the recorded field lacks it (A1.4: "a theorem's hypotheses are its
declared arguments at L"). Name resolution respects the import closure of the source file, bound variables
and the namespace the source qualifies, shares or opens (13 ambiguous names, all resolved to the declaration
the source text uses). Free text that is neither an id nor a name is kept per node as *named hypotheses*.

**Levels.** A node's span is the set of level letters in its `level` field. An edge is cross-level when the
spans are disjoint; its supply is K when its source has kernel status, MS otherwise. The supply rule reads
the status string: the nine I2 manuscript statements whose status cites kernel theorems ("proved [K] per the
manuscript's kernel citation", I2.29–I2.37) and I2.3 (a scope statement citing a [K] component) count as K;
the meeting result of §4 does not depend on this, since it holds over all edges.

**Derived and roots.** A node is derived at L when its status is proved (kernel, `[M]` or manuscript) or
conditional-on, and its kind is not a definition, hypothesis-structure, axiom or condition. Every other node is
non-derived; its root category is fixed by the table of NOTES N2 (`AX`, `C1`–`C4`, `FOUND`, `PHYS`, `NEUTRAL`,
`DEF`, `OPER`). A derived node's roots are the non-derived nodes reachable from it through `R`, `RA`, `RN`, `KC`
(traversing derived nodes, so proved lemmas enter through their own dependencies), with the named hypotheses
met on the way, each categorized by the keyword rules of N2 (kernel binder fragments as `DEF`).

**Runs and amendments** (all kept, NOTES N2–N4): `edges.py` runs 1–3 superseded (one-letter title fragments
and bound variables resolved as records; namespace order; a free-text filter that dropped short hypothesis
names such as "C2 (I1)"). `classify.py` runs 1–3 superseded: run 1 applied the manuscript-H rule to ten kernel
hypothesis-structures at level H and level-defaulted kernel binder fragments to PHYS (post hoc re-scoping,
disclosed; run 1 → final: a0 74 → 103, b 13 → 15, c 178 → 172, d 63 → 36); run 2 missed the plural
"(definitions)" of I3.11; run 3 left I3.184 in a0 because a file reference hid its condition text; run 4
read 'proved' inside the component lists of two scope statements (I2.3, I2.69) as their status.

## 2. Item 1 — the partition (`graph.tsv` columns `class`, `sublabel`, `needs`; `analyze.out` S1)

| class | meaning | n |
|---|---|---|
| (a) | consequences of Axioms 1–2 alone: generators `gen` 2; premise-free `a0` 103; Axioms only `a1` 1; with an observation-base posit `a2` 3 | 109 |
| (b) | consequences of Axioms 1–2 with C1–C4: generators 5, derived 10 | 15 |
| (c) | items needing an operational hypothesis | 172 |
| (d) | items needing a physical hypothesis | 36 |
| (e) | items with no derivation at L (definitions, hypothesis-structures, hypotheses, obligations, [D], PT-record, scope) | 301 |

**(a).** Generators: I1.1 (Axiom 1), I1.2 (Axiom 2; recorded as presupposing Axiom 1).
- `a1` (Axioms 1–2 and definitions only): **I1.3** — the two-axiom base and the non-derivability of Axiom 2
  (proved [manuscript, not K], a written countermodel). It is the only derived item whose roots are the axioms.
- `a2` (Axioms with a named observation-base posit): **I1.7** (dynamics from the composition law) and **I1.8**
  (Lemma 1, finiteness) — both through I1.6 (the Definition of an observation, *assumed*) and I1.4 (the
  perspectival reading, *assumed*); **I2.11** (the classical joint law of two observers) — through "Lemma 3
  counting measure" (I1.12's selection, *assumed*). Lemma 2 (I1.9, *assumed*, definitional) and Lemma 3 (I1.10,
  *empirically motivated / assumed*) carry no derivation at L and are in (e); everything that uses Lemma 3 is
  in (d) through I1.10 and I1.11 (total finiteness).
- `a0` (premise-free; no axiom, condition or hypothesis in the closure; closed statements about defined
  objects, or theorems whose only arguments are mathematical setting). These are consequences of Axioms 1–2 only
  in the vacuous sense; none uses an axiom. I1: 32, 40, 41, 58. I2: 8, 9, 21, 22, 24, 39, 40, 43, 44, 45, 47, 49,
  50, 55, 57, 58, 59, 64, 65, 83, 91, 105. I3: 14, 20, 26, 28, 33, 34, 41, 42, 53, 67, 68, 80, 83, 85, 91, 104,
  125, 126, 127, 128, 186. I4: 6, 7, 8, 9, 10, 11, 13, 21, 22, 27, 33, 34, 40, 41, 46, 48, 49, 59, 63, 72, 76,
  78, 114, 147, 152, 154, 159, 162, 163, 165, 166, 167, 169, 170, 171, 177, 178, 185, 190, 192, 208, 209, 210,
  211, 212, 214, 215, 216, 223, 224, 228, 229, 230, 231, 232, 239. They include the matrix-level independence
  and countermodel theorems (e.g. I4.9, I4.10, I4.41, I4.114, I4.76 `oi_alone_not_qm`), the C3 necessity
  theorem I1.32 (stated for every realization), the finite-horizon equivalence I2.39 (stated for every finite
  alphabet and horizon), the substratum-class discharges I4.46 `substratumClass_structurallyClosed` and the
  layer-flow no-go I4.59, the K∞ single-ball theorems I3.67, I3.80, I3.83, and the PSD facts I4.210, I4.215,
  I4.216 (flagged: comparison objects only). The column `external` names the kernel declarations without a
  record that such a statement mentions.

**(b).** Generators: I1.20 (C1), I1.21 and I1.22 (C2 in its structural and slow forms), I1.23 (C3), I1.24 (C4);
as recorded, C1, C2-structural, C3 and C4 depend on Lemma 2 or the Definition (`FOUND` I1.4, I1.6, I1.9), and
C4 on C1 and C2-persistence. Derived (all manuscript H, one kernel theorem):
- I1.17 (the layered theorem statement; layers 1–3) — C1, C2, C3, C4;
- I1.25 (only C4 is logically independent) — C1–C4; I1.29 (accessible backflow) — C1–C4; I1.33 (existential and
  universal readings) — C1–C4;
- I1.27 (readback with finite recurrence forces indivisibility; proved [K] with the routed form as hypothesis) —
  C4 through the kernel form `RoutedReadback` (I1.71), with the recurrence of the rooted map;
- I1.28 (a fast bath erases readback) — C2 (I1.22); I1.34 ((C1) does not fix the composite) — C1;
- I2.53 — C2 (the erosion-rate hypothesis); I2.54 — C4 ("a C4 gap at order k"); I2.61 — C2 (slow-bath and
  weak-coupling conditions, its status condition).
No kernel declaration outside level H lies in (b); no item of (b) is at level O, P, M or G.

**(c)** (172; each row's `needs` column names its operational roots). I1: 44, 45, 46, 48, 52, 53, 54, 79, 80,
81, 82, 83. I2: 12, 13, 15, 16, 17, 19, 20, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 74, 94–100, 112. I3: 12, 13,
15–19, 21, 22, 24, 25, 27, 30, 31, 32, 37, 38, 40, 44, 45, 46, 47, 51, 52, 55, 56, 72, 78, 79, 81, 82, 84, 88,
89, 90, 97, 98, 105, 111, 112, 120, 121, 122, 124, 164, 184, 185, 187. I4: 5, 15, 16, 17, 19, 20, 35–39, 43, 47,
51, 52, 53, 57, 58, 61, 62, 71, 75, 77, 81, 83, 84, 89–95, 97, 98, 100, 101, 103, 104, 105, 111, 112, 113, 116,
117, 119, 121, 122, 125, 126, 129, 130, 131, 135, 136, 138, 139, 141, 142, 145, 146, 150, 151, 153, 157, 158,
160, 161, 164, 168, 173, 176, 180, 181, 184, 189, 191, 193, 194, 199, 200, 205, 206, 207, 219, 237.
The operational hypotheses most often needed (number of (c) items whose closure contains the root):
- matrix carrier and completion layer: I4.64 `FiniteOperationalTheory` 83; I4.30 `LabelInvariant` 20; I4.29
  `ContextStable` 19; I4.32 `Architecture` 16; I4.132 `DaggerStable` 15; I4.107 `RegroupingInvariant`, I4.108
  `RelabellingInvariant`, I4.109 `IsAmbientMember`, I4.28 `ImplementationGenerated` 11 each; I4.67
  `HasCompositeUnitaryControl` 10; I4.110 `EmbeddedObservation` 9; I4.243 `HControl` 7; I4.70
  `ExactAllFiniteEndomorphicQuantumOps` 7; I4.133, I4.143, I4.45 `StructurallyClosed` 6 each; I4.156, I4.50,
  I4.66, I4.69, I4.73 5 each; I4.3 `HasParallelReferenceExtension`, I4.31 `ImplementationLocality`, I4.56
  `LayerFlowExecutable` 4 each;
- K programme: I3.1 `W d` 23; I3.8 `IsNot` 18; I3.74 `PreservesBody` 14; I3.76 `BoundaryTransitive` 13; I3.9
  `NativeGate` 13; I3.73 `SharpSeed` 11; I3.75 `SeedOrbitAvailable` 8; I3.48 `EffectsOn` 6; I3.10 `Entangling`
  5; I3.23 `GateRel`, I3.35 `NativeGateOf` 4 each; I3.66 `ElementaryDrivability`, I3.96 `FiniteRank`, I3.113
  `ProductData` 3 each;
- manuscript: I2.28 the Bekir–Golomb premise 3.
Two K-programme records in (c) are themselves obligations with a conditional status: I3.164 (K1, CONDITIONAL on
the K∞ hypotheses, `IsNot` and the relative native-gate hypotheses) and I3.184 (the operational-reconstruction
route, conditional on the five completion conditions).

**(d)** (36; `needs` names the physical roots). Manuscript H: I1.15, I1.30, I1.31 (the mixing hypothesis),
I1.69 (Substratum A1–A6), I1.84, I1.85 (kernel theorems on the observability quotient, through their recorded
links to Lemma 3 and total finiteness), I2.1, I2.2 (site factorization, the coupling graph), I2.5 (Bell ceiling:
determinism, setting interventions, readout timing, common ensemble), I2.41 (with C1–C4 and the imported
Barandes correspondence I2.42 ⇄ I2.56), I2.48, I2.51, I2.52, I2.66 (total finiteness, Liouville measure), I2.72
((EM), canonical typicality). H/X and X: I1.35 (Stage 1: E1–E3, M1-T, A1–A2), I1.62 (A6 readings),
I2.7, I2.71, I2.75, I2.77, I2.79, I2.80, I2.81, I2.82, I2.88, I2.89 (E1–E7, M1-T, M1-B, the Bell branch I2.6),
I2.106, I2.107, I2.108 (H-local-lift), I2.109 (H-scramble). M and G: I2.14 (the coherent operational lift and
I2.5's Bell hypotheses), I2.36, I2.37 (the matrix completion roots I4.29, I4.45, I4.50, I4.156, I4.198 … with
the lattice hypotheses of I2.36), I2.60 (total finiteness), I2.67 (as I2.41).

**(e)** (301; sublabel = category / kind). Categories: `OPER` 205 (hypothesis-structures 142, definitions used
as hypotheses 27, obligations 32, the [D] theorems I3.139 and I3.140, the hypothesis I2.56 and the principle
I2.10); `DEF` 45; `PHYS`
21 (I1.5, I1.10, I1.11, I1.36, I1.61, I1.63–I1.68, I1.74, I1.77, I2.6, I2.46, I2.73, I2.76, I2.86, I2.87,
I2.102, I2.113); `NEUTRAL` 20 (I1.16, I1.18, I1.19, I1.26, I1.37, I1.76, I1.78, I2.3, I2.4, I2.18, I2.62, I2.63,
I2.68, I2.69, I2.70, I2.78, I2.84, I2.85, I2.110, I2.111); `FOUND` 6 (I1.4, I1.6, I1.9, I1.12, I1.13, I1.14);
`C4` 4 (the kernel readback forms I1.70–I1.73). The extension of A1.4's (e) — "definitions and
hypothesis-structures" — to every non-generator item without a derivation at L (hypotheses, obligations,
PT-record and [D] items, scope statements) is this thread's convention (NOTES N1); the sublabel keeps them apart.

**Sensitivity.** Run 1 of `classify.py` (kept) placed 63 items in (d); the final run places 36 after re-scoping
two N2 rules to manuscript records (NOTES N3). The membership of (a1), (a2) and (b) is the same in every run
except I2.53 and I2.61, which enter (b) once the free-text filter keeps the pieces "τ_B ≪ τ_S" and "C2 (I1)".

## 3. Item 2 — the do-not-assume items: status at L and discharges for particular objects

Scope: every row flagged in the step-1 records (`flag` = DNA in `graph.tsv`: I4's 44, I3's 20 — its nine
listed items and eleven items whose flag names a flagged clause — and I2's 11). The status is the record's own
text at L (cut at 170 characters; full text in `analyze.out` S2 and the inventories). The last column lists the
kernel theorems the status cites with the clause before the citation ("discharged for the substratum class",
"holds for exact QM", "refuted for `countermodel`", "implied by", …), the record carrying the theorem with its
class, and that theorem's premises (graph dependencies, or for a theorem without a record its declared
arguments at L). A discharge for a particular object is a clause naming the object; the general item keeps its
status. Rows are formatted from `analyze.out` S2/S2d without change of content.

| id | item | class | status at L | cited kernel relations: [clause] theorem → record [class]; premises |
|---|---|---|---|---|
| I2.3 | The operational-extension boundary | e/NEUTRAL/manuscript-principle | scope statement (components: I2.39 proved [K]; I2.12 proved [M]; I2.17 proved [M] with imported half; I2.29 manuscript statement of an I4 kernel result) | — |
| I2.29 | The operational-completion characterization (manuscript statement; ker | c/ | proved [K] per the manuscript's kernel citation (`exactAll_iff_physical_general`, `general_characterization`, GeneralCarrier.lean) — kernel side out of scope: I4 | — |
| I2.30 | Bare finite OI does not imply QM; OI-compatible theory plus (i)–(v) if | c/ | proved [K] per manuscript citation (`main_result`, `oi_compatible_classification`, `oi_alone_not_qm` in GeneralCarrier.lean; `five_way_minimality` in RankGapTheory.lean) … | — |
| I2.31 | Quantum-complete OI (OI⁺): observational independence, reversible rich | e/OPER/definition-as-hypothesis | equivalence proved [K] per manuscript citation (`carrier_general_oiPlus`, `oiPlus_iff_completedOI`, `oiPlus_independence`) — kernel side out of scope: I4; the three pri… | — |
| I2.32 | Primitive-source form: implementation locality, phase-free richness, e | c/ | equivalence proved [K] per manuscript citation (`carrier_general_oiPlusMin`, `oiPlusMin_iff_qm`, `carrier_general_oiPlusPos`) — kernel side out of scope: I4; the princi… | — |
| I2.33 | Substratum-source form | c/ | proved [K] per manuscript citation (`substratum_plus_control_qm`, `substratum_extension_quantum_iff_drives`, `readWriteSourced_not_qm`) — kernel side out of scope: I4; … | — |
| I2.34 | Layer-flow form | c/ | proved [K] per manuscript citation (`derivedOI_qm_iff_layerFlowExecutable'`, `substratumTheory_not_layerFlowExecutable`, `obs_not_layerFlowExecutable`) — kernel side ou… | — |
| I2.35 | Typed form | c/ | proved [K] per manuscript citation (`typed_determined_iff`, `typed_determined_of_oiPlusMin`, `typed_interface_not_quantum`) — kernel side out of scope: I4 | — |
| I2.62 | Comparison of routes and dependency scope: in-house, imported, additio | e/NEUTRAL/manuscript-principle | scope statement (components I2.39, I2.44, I2.56, I2.29) | — |
| I2.63 | Operational-reconstruction route: target conditions and the outstandin | e/NEUTRAL/manuscript-principle | scope statement | — |
| I2.69 | The claim structure: the four layers, the four-part theorem statement, | e/NEUTRAL/manuscript-principle | scope statement (layers 1–3 proved; layer 4 / part (4) requires additional hypotheses) | — |
| I3.6 | `actT` | e/DEF/definition-as-hypothesis | proved [K] (definition) | — |
| I3.7 | `actC` | e/DEF/definition-as-hypothesis | proved [K] (definition) | — |
| I3.66 | `ElementaryDrivability` (K∞-Drive) | e/OPER/hypothesis-structure | assumed / open — ROADMAP.md:1017 "**K∞-Drive** — field-neutral drivability, `ElementaryDrivability`", K∞ OPEN, "All are unsourced" (ROADMAP.md:1009); KINF-2 "name… | — |
| I3.80 | `boundaryTransitive_fullAut3` | a/a0 | proved [K] | — |
| I3.83 | `boundaryTransitive_ball3Drive` (with `driveWords3`) | a/a0 | proved [K] | — |
| I3.118 | `JointReversible` | e/OPER/hypothesis-structure | assumed (a predicate; no OI source; KT4-PREM-1 / PT stage 1 B: `JointReversible`/`PreservesBody` of the pair slice restates `hgate`) | — |
| I3.137 | IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | e/OPER/definition-as-hypothesis | not at L — [D] FourCopyCore.lean:155–157; conclusion of I3.139 (CONDITIONAL on the five premises, [D]); PT stage 1–3: INDEPENDENT of L; fails on every exotic cone o… | — |
| I3.139 | `kt4_forward_ie1` (Theorem A′, the audited theorem) | e/OPER/theorem | not at L — [D] "kernel-checked in a design run, not certified" (KT4-PREM-1 result.md:188, :241) | — |
| I3.142 | `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the drive w | e/OPER/definition-as-hypothesis | not at L — [D]; `ie1Drive_of_ie1` is "Open." with proof `sorry` (FourCopyPackage.lean:291–293) | — |
| I3.144 | `Q3`, `twin`, `pauliW`, `twistQ3` | e/OPER/definition-as-hypothesis | not at L — [D] in the `sorry` preflight FourCopyPackage.lean:174–190; in the kernel at L `Q3` occurs only as a question label in DerivedQ3/FlowEndpoint (name collisio… | — |
| I3.146 | P-ACT2 (named premise of KT4-PREM-1) | e/OPER/hypothesis-structure | assumed (named premise of the landed KT4-PREM-1 record; a premise `D` does not state) (KT4-PREM-1 result.md:162) | — |
| I3.150 | (b_S4) — the full rotation group of one token acts on the pair preserv | e/OPER/hypothesis-structure | PT-record: open — "INDEPENDENT of H1–H3 plus the certified pair structure at L" (PROTOCOL-STAGE5.md:17–20; INTEGRATION-NOTE-STAGE4.md:20, :118–123); sufficient fo… | — |
| I3.151 | (b_n) — one rotation subgroup of one token about an off-frame axis | e/OPER/hypothesis-structure | PT-record: open; stage 4 record S3[n]: "UNIQUE iff n is off the native frame's coordinate axes (level (ii))" (INTEGRATION-NOTE-STAGE4.md:40) | — |
| I3.152 | (b_R1) — one order-3 rotation of one token about (5,1,1) | e/OPER/hypothesis-structure | PT-record: open; stage 4 record R1: "UNIQUE [W + X]; its only proper sub-extension (cnot alone) EXOTIC-X" (INTEGRATION-NOTE-STAGE4.md:42) | — |
| I3.153 | (b_DJ) — the native drive with the native `J` acting on one token | e/OPER/hypothesis-structure | PT-record: open; stage 4: "The drive the corpus attaches to the NOT (`nflip`, axis x; corner axis `z3`) lies exactly on the exceptional set: its idle extension does not f… | — |
| I3.154 | IE2 — idle extension of the pair interaction groups | e/OPER/hypothesis-structure | PT-record: open ("IE₂ open", INTEGRATION-REVIEW.md:187, :211); forbidden as a premise (PROTOCOL.md:82; PROTOCOL-STAGE3.md:133) | — |
| I3.155 | frame covariance (FC) of the native gate | e/OPER/hypothesis-structure | PT-record: flagged; "FC ⟺ IE1 given hgate, with exact words confirmed" (INTEGRATION-ADDENDUM-STAGE2.md:124); candidate μ "fails the disguise test by record" (PROTOCOL-… | — |
| I3.165 | K2 — the composite | e/OPER/obligation | open (ROADMAP.md:1001 "**K2 — the composite. OPEN.**") | — |
| I3.184 | the operational-reconstruction route: reconstruction axioms as hypothe | c/ | conditional — the manuscript states the route as "a classification conditional on the five completion conditions, not an independent derivation" (Main.md:352) | — |
| I3.187 | the classification step of KT4-PREM-1: `hcls ∧ hadm ∧ hgate ∧ IE1 ⇒ K_ | c/ | conditional-on IE1, `hcls`, `hadm`, `hgate`; "a written argument and it is not yet kernel-checked" (KT4-PREM-1 result.md:142); finite steps exact (probe checks C1–C6); … | — |
| I4.3 | HasParallelReferenceExtension | e/OPER/hypothesis-structure | assumed (never discharged for a general theory at L). Satisfiable: hcompRealized_consistent_with_parallelReferenceExtension (SpectatorBridge.lean:472) [K]; refuted for th… | [. Satisfiable:] hcompRealized_consistent_with_parallelReferenceExtension (SpectatorBridge.lean:472) -> I4.22 [a/a0] — premises (none); [refuted for the round-34 `countermodel`] countermodel_not_parallelReferenceExtension (:501) -> I4.9 [a/a0] — premises (none); [not supplied by composite unitary control] control_not_implies_parallelReferenceExtension (:507) -> I4.10 [a/a0] — premises K:countermodel;K:countermodel_control; [[K] nor by the other OI⁺ principles] oiPlus_independence (CompletedOI.lean:506) -> I4.95 [c/] — premises I4.64; [equivalent to] InertSpectatorCompositionality (SpectatorBridge.lean:233) -> I4.14 [e/OPER/hypothesis-structure] — premises I4.64;I4.12; [implied by] ImplementationLocality (ImplementationLocality.lean:957) -> I4.31 [e/OPER/hypothesis-structure] — premises I4.28;I4.29;I4.30 |
| I4.4 | HasQutritReferenceExtension | e/OPER/hypothesis-structure | assumed; implied by HasParallelReferenceExtension (qutrit_of_parallel, :474) [K]; refuted for `countermodel` (countermodel_not_qutritReferenceExtension, :492) [K] | [implied by HasParallelReferenceExtension] qutrit_of_parallel (:474) -> I4.5 [c/] — premises I4.3;I4.64; [refuted for `countermodel`] countermodel_not_qutritReferenceExtension (:492) -> I4.8 [a/a0] — premises K:countermodel;K:countermodel_reduction2_available |
| I4.14 | InertSpectatorCompositionality | e/OPER/hypothesis-structure | assumed (hypothesis of krausSoundExt_of_sound_control_inert (:249), exactAll_iff_substantive (GeneralCarrier.lean:144) and, through PhysicalCompletionConditions, of exact… | [hypothesis of] krausSoundExt_of_sound_control_inert (:249) -> I4.16 [c/] — premises K:FiniteIsometryExtensionSF;K:KrausSound;I4.67;I4.14;I4.64; [] exactAll_iff_substantive (GeneralCarrier.lean:144) -> I4.75 [c/] — premises I4.73;I4.64; [and, through PhysicalCompletionConditions, of] exactAll_iff_physical_general (GeneralCarrier.lean:100) -> I4.71 [c/] — premises I4.64; [equivalent to] HasParallelReferenceExtension (:233) -> I4.3 [e/OPER/hypothesis-structure] — premises I4.64;I4.1; [necessary for exact finite QM] physical_of_exactAll (PhysicalCharacterization.lean:301) -> no record — args PhysicalCharacterization.lean:301 FiniteOperationalTheory, ExactAllFiniteEndomorphicQuantumOps |
| I4.29 | ContextStable | e/OPER/hypothesis-structure | assumed in general; discharged for the substratum class (substratumClass_contextStable, StructuralClosure.lean:261) [K] and for StateMixingCoupling's class (mixC_contextS… | [discharged for the substratum class] substratumClass_contextStable (StructuralClosure.lean:261) -> no record — args StructuralClosure.lean:261 (none: closed statement); [[K] and for StateMixingCoupling's class] mixC_contextStable (StateMixingCoupling.lean:442) -> no record — args StateMixingCoupling.lean:442 (none: closed statement) |
| I4.31 | ImplementationLocality | e/OPER/hypothesis-structure | assumed; satisfied by exact finite QM (implementationLocality_of_qm, :1017) [K]; not supplied by the OI core, validity, reversible richness and embedded observation (impl… | [satisfied by exact finite QM] implementationLocality_of_qm (:1017) -> I4.39 [c/] — premises I4.70;I4.64; [not supplied by the OI core, validity, reversible richness and embedded observation] implementationLocality_independent (:1035) -> I4.41 [a/a0] — premises (none) |
| I4.42 | OIPlusLocal | e/OPER/hypothesis-structure | assumed; equivalent to exact finite operational QM on every nonempty finite carrier (carrier_general_oiPlusLocal, :1079) [K] | [equivalent to exact finite operational QM on every nonempty finite carrier] carrier_general_oiPlusLocal (:1079) -> I4.43 [c/] — premises I4.64 |
| I4.45 | StructurallyClosed | e/OPER/hypothesis-structure | assumed for an extension (hypothesis of quantumArchitecture_iff_drives_of_closed, substratum_extension_quantum_iff_drives, substratum_plus_control_qm); discharged for sub… | [discharged for substratumClass itself] substratumClass_structurallyClosed (:316) -> I4.46 [a/a0] — premises I4.44 |
| I4.56 | LayerFlowExecutable | e/OPER/hypothesis-structure | assumed; holds under composite unitary control (layerFlowExecutable_of_control, :117) [K]; fails in the substratum theory for every involution moving a configuration (sub… | [holds under composite unitary control] layerFlowExecutable_of_control (:117) -> I4.57 [c/] — premises I4.67;I4.64; [fails in the substratum theory for every involution moving a configuration] substratumTheory_not_layerFlowExecutable (:200) -> I4.59 [a/a0] — premises (none) |
| I4.65 | PhysicalCompletionConditions | e/OPER/hypothesis-structure | assumed; necessary for exact finite QM (physical_of_exactAll, PhysicalCharacterization.lean:301) [K]; jointly satisfiable (main_result clause (ii)) [K]; each of the five … | [necessary for exact finite QM] physical_of_exactAll (PhysicalCharacterization.lean:301) -> no record — args PhysicalCharacterization.lean:301 FiniteOperationalTheory, ExactAllFiniteEndomorphicQuantumOps |
| I4.66 | CompositeOperationalValidity | e/OPER/hypothesis-structure | assumed; derived from ImplementationLocality (validity_of_implementationLocality, ImplementationLocality.lean:971) [K]; necessary for exact QM [K] | [derived from ImplementationLocality] validity_of_implementationLocality (ImplementationLocality.lean:971) -> I4.38 [c/] — premises I4.31;I4.64 |
| I4.67 | HasCompositeUnitaryControl | e/OPER/hypothesis-structure | assumed; derived from ReversibleRichness (control_of_reversibleRichness, CarrierGeneralOIPlus.lean:127) [K], from LieRankRichness (control_of_lieRank, MicroscopicReversib… | [derived from ReversibleRichness] control_of_reversibleRichness (CarrierGeneralOIPlus.lean:127) -> I4.100 [c/] — premises I4.99;I4.64; [[K], from LieRankRichness] control_of_lieRank (MicroscopicReversibility.lean:114) -> I4.130 [c/] — premises I4.128;I4.64; [[K], from PhaseFreeRichness with IteratedAncillaClosure] control_of_phaseFree (MinimalRepertoire.lean:529) -> I4.119 [c/] — premises I4.68;I4.118;I4.64; [] readWriteSourced_not_control (ReadWriteControl.lean:169) -> I4.157 [c/] — premises I4.156;I4.64 |
| I4.68 | IteratedAncillaClosure | e/OPER/hypothesis-structure | assumed; derived from EmbeddedObservation (closure_of_embedded, EmbeddedObservation.lean:184) [K] | [derived from EmbeddedObservation] closure_of_embedded (EmbeddedObservation.lean:184) -> I4.111 [c/] — premises I4.107;I4.108;I4.109;I4.64;I4.106 |
| I4.69 | SystemToLevelOne | e/OPER/hypothesis-structure | assumed; derived from EmbeddedObservation (systemToLevelOne_of_embedded, EmbeddedObservation.lean:203) [K]; necessary for exact QM (levelOne_of_exactAll, PhysicalCharacte… | [derived from EmbeddedObservation] systemToLevelOne_of_embedded (EmbeddedObservation.lean:203) -> I4.112 [c/] — premises I4.107;I4.108;I4.109;I4.64;I4.106; [necessary for exact QM] levelOne_of_exactAll (PhysicalCharacterization.lean:285) -> no record — args PhysicalCharacterization.lean:285 FiniteOperationalTheory, ExactAllFiniteEndomorphicQuantumOps |
| I4.70 | ExactAllFiniteEndomorphicQuantumOps | e/OPER/hypothesis-structure | assumed where it is a hypothesis (the necessity directions: implementationLocality_of_qm, qm_generated_by_substratum_extension, oiPlus_of_qm, ...); never derived from the… | [never derived from the OI core alone] oi_alone_not_qm (GeneralCarrier.lean:160) -> I4.76 [a/a0] — premises (none) |
| I4.73 | WellFormed | e/OPER/hypothesis-structure | assumed (hypothesis of exactAll_iff_substantive, reversibleRichness_of_control, inverseAccessibility_of_lieRank; conjunct of OIPlus) | — |
| I4.74 | SubstantiveCompletion | e/OPER/hypothesis-structure | assumed | — |
| I4.80 | CompletedOI | e/OPER/hypothesis-structure | assumed; equivalent to PhysicalCompletionConditions (completedOI_iff_physical, :110) [K] | [equivalent to PhysicalCompletionConditions] completedOI_iff_physical (:110) -> I4.81 [c/] — premises I4.64 |
| I4.82 | ObservationalIndependence | e/OPER/hypothesis-structure | assumed; by definition HasParallelReferenceExtension T; equivalent to InertSpectatorCompositionality (observationalIndependence_iff_inert, :131) [K]; independent of OICor… | [equivalent to InertSpectatorCompositionality] observationalIndependence_iff_inert (:131) -> I4.83 [c/] — premises I4.64; [independent of OICore, WellFormed, ReversibleRichness, ObserverRecursion] independence_independent (:475) -> I4.92 [c/] — premises I4.64 |
| I4.85 | ReversibleRichness | e/OPER/hypothesis-structure | assumed; independent of the other OI⁺ principles (richness_independent, :487; oiPlus_independence, :506) [K] | [] oiPlus_independence (:506) -> I4.95 [c/] — premises I4.64 |
| I4.87 | ObserverRecursion | e/OPER/hypothesis-structure | assumed; derived from EmbeddedObservation (observerRecursion_of_embeddedObservation, EmbeddedObservation.lean:217) [K]; independent of the other OI⁺ principles (recursi… | [derived from EmbeddedObservation] observerRecursion_of_embeddedObservation (EmbeddedObservation.lean:217) -> I4.113 [c/] — premises I4.110;I4.64; [independent of the other OI⁺ principles] recursion_independent (:496) -> I4.94 [c/] — premises I4.64 |
| I4.88 | OIPlus | e/OPER/hypothesis-structure | assumed; equivalent to exact finite operational QM on the qubit (oiPlus_iff_qm, :440) [K] | [equivalent to exact finite operational QM on the qubit] oiPlus_iff_qm (:440) -> I4.90 [c/] — premises I4.64 |
| I4.96 | ObservationalIndependence | e/OPER/hypothesis-structure | assumed; by definition HasParallelReferenceExtension T; implied by ImplementationLocality (ImplementationLocality.lean:957) [K] | [implied by] ImplementationLocality (ImplementationLocality.lean:957) -> I4.31 [e/OPER/hypothesis-structure] — premises I4.28;I4.29;I4.30 |
| I4.99 | ReversibleRichness | e/OPER/hypothesis-structure | assumed; gives HasCompositeUnitaryControl (control_of_reversibleRichness, :127) [K]; follows from control on a well-formed theory (reversibleRichness_of_control, :148) [K… | [gives HasCompositeUnitaryControl] control_of_reversibleRichness (:127) -> I4.100 [c/] — premises I4.99;I4.64; [follows from control on a well-formed theory] reversibleRichness_of_control (:148) -> I4.101 [c/] — premises I4.73;I4.67;I4.64; [⟺ InverseAccessibility ∧ LieRankRichness] reversibleRichness_iff (MicroscopicReversibility.lean:100) -> no record — args MicroscopicReversibility.lean:101 (none: closed statement) |
| I4.102 | OIPlus | e/OPER/hypothesis-structure | assumed; equivalent to exact finite operational QM on every nonempty finite carrier (carrier_general_oiPlus, :213) [K] | [equivalent to exact finite operational QM on every nonempty finite carrier] carrier_general_oiPlus (:213) -> I4.104 [c/] — premises I4.64 |
| I4.110 | EmbeddedObservation | e/OPER/hypothesis-structure | assumed; implies ObserverRecursion (:217), IteratedAncillaClosure (:184) and SystemToLevelOne (:203) [K]; holds for exact QM (embeddedObservation_of_qm, :327) [K] and for… | [implies] ObserverRecursion (:217) -> I4.87 [e/OPER/hypothesis-structure] — premises I4.86; [] IteratedAncillaClosure (:184) -> I4.68 [e/OPER/hypothesis-structure] — premises I4.64; [and] SystemToLevelOne (:203) -> I4.69 [e/OPER/hypothesis-structure] — premises I4.64; [holds for exact QM] embeddedObservation_of_qm (:327) -> no record — args EmbeddedObservation.lean:327 Nonempty, FiniteOperationalTheory, ExactAllFiniteEndomorphicQuantumOps; [[K] and for every theory generated by a label-invariant architecture] genTheory_embeddedObservation (ImplementationLocality.lean:904) -> I4.36 [c/] — premises I4.30;I4.32; [independent of OICore, WellFormed, ObservationalIndependence, ReversibleRichness] embeddedObservation_independent (:343) -> I4.114 [a/a0] — premises (none) |
| I4.115 | OIPlusEmbedded | e/OPER/hypothesis-structure | assumed; ⟺ OIHierarchyGeneral.OIPlus (oiPlusEmbedded_iff_oiPlus, :388) [K]; ⟺ exact finite operational QM (:384) [K] | [⟺ OIHierarchyGeneral.OIPlus] oiPlusEmbedded_iff_oiPlus (:388) -> no record — args EmbeddedObservation.lean:388 (none: closed statement) |
| I4.118 | PhaseFreeRichness | e/OPER/hypothesis-structure | assumed; implied by LayerFlowExecutable under SubstratumAvail (phaseFree_of_layerFlowExecutable, LiftAudit.lean:783) [K] and by CyclicRichness (phaseFree_of_cyclic) [K]; … | [implied by LayerFlowExecutable under SubstratumAvail] phaseFree_of_layerFlowExecutable (LiftAudit.lean:783) -> I4.61 [c/] — premises I4.60;I4.56;I4.64; [gives control with IteratedAncillaClosure] control_of_phaseFree (:529) -> I4.119 [c/] — premises I4.68;I4.118;I4.64 |
| I4.120 | OIPlusMin | e/OPER/hypothesis-structure | assumed; ⟺ exact finite operational QM (oiPlusMin_iff_qm, :569) [K] | [⟺ exact finite operational QM] oiPlusMin_iff_qm (:569) -> I4.121 [c/] — premises I4.64 |
| I4.123 | CyclicRichness | e/OPER/hypothesis-structure | assumed; implies PhaseFreeRichness (phaseFree_of_cyclic) [K] | — |
| I4.124 | OIPlusPos | e/OPER/hypothesis-structure | assumed; ⟺ exact finite operational QM (oiPlusPos_iff_qm, :55) [K] | [⟺ exact finite operational QM] oiPlusPos_iff_qm (:55) -> I4.125 [c/] — premises I4.64 |
| I4.127 | InverseAccessibility | e/OPER/hypothesis-structure | assumed; derived from LieRankRichness on a well-formed theory (inverseAccessibility_of_lieRank, :132) [K] and from a dagger-stable, unitary-ray-saturated generating class… | [derived from LieRankRichness on a well-formed theory] inverseAccessibility_of_lieRank (:132) -> I4.131 [c/] — premises I4.73;I4.128;I4.64 |
| I4.128 | LieRankRichness | e/OPER/hypothesis-structure | assumed | — |
| I4.133 | ReversibleImplementationLocality | e/OPER/hypothesis-structure | assumed; holds for exact QM (reversibleImplementationLocality_of_qm, :329) [K] | [holds for exact QM] reversibleImplementationLocality_of_qm (:329) -> I4.136 [c/] — premises I4.70;I4.64 |
| I4.137 | OIPlusMicro | e/OPER/hypothesis-structure | assumed; ⟺ exact finite operational QM (oiPlusMicro_iff_qm, :357) [K] | [⟺ exact finite operational QM] oiPlusMicro_iff_qm (:357) -> I4.138 [c/] — premises I4.64 |
| I4.143 | DrivesElementary | e/OPER/hypothesis-structure | assumed for an extension; refuted for substratumClass (substratumClass_not_drivesElementary, StructuralClosure.lean:370) [K] and for the diagonal class (diagClass_not_dri… | [refuted for substratumClass] substratumClass_not_drivesElementary (StructuralClosure.lean:370) -> no record — args StructuralClosure.lean:370 (none: closed statement); [[K] and for the diagonal class] diagClass_not_drivesElementary (:174) -> I4.147 [a/a0] — premises (none); [holds for the full class] fullClass_quantumArchitecture (:151) -> no record — args SubstratumSource.lean:151 (none: closed statement) |
| I4.144 | QuantumArchitecture | e/OPER/hypothesis-structure | assumed; for a structurally closed class ⟺ DrivesElementary (StructuralClosure.lean:364) [K]; refuted for substratumClass (substratumClass_not_quantumArchitecture, Stru… | [for a structurally closed class ⟺] DrivesElementary (StructuralClosure.lean:364) -> I4.143 [e/OPER/hypothesis-structure] — premises I4.24; [refuted for substratumClass] substratumClass_not_quantumArchitecture (StructuralClosure.lean:376) -> no record — args StructuralClosure.lean:376 (none: closed statement) |
| I4.179 | PairFlowSourced | e/OPER/hypothesis-structure | assumed; ⟺ (with DerivedOI) exact QM on the qubit (qm_iff_derivedOI_pairFlowSourced, :199) [K] | [exact QM on the qubit] qm_iff_derivedOI_pairFlowSourced (:199) -> I4.180 [c/] — premises I4.64 |
| I4.187 | ShadowQuantum | e/OPER/hypothesis-structure | assumed; ⟺ the typed Kraus determination (typed_determined_iff, :850) [K]; refuted for typedDiag (typedDiag_shadow_not_qm, :940) [K] | [⟺ the typed Kraus determination] typed_determined_iff (:850) -> I4.190 [a/a0] — premises (none); [refuted for typedDiag] typedDiag_shadow_not_qm (:940) -> I4.192 [a/a0] — premises (none) |
| I4.210 | psd_iff_trace_nonneg | a/a0 | K | — |
| I4.215 | psd_trace_mul_nonneg | a/a0 | K | — |
| I4.216 | accessible_cone_full | a/a0 | K | — |
| I4.241 | DerivedOI | e/OPER/hypothesis-structure | assumed (hypothesis of derivedOI_qm_iff_layerFlowExecutable, qm_of_derivedOI_layerFlowExecutable, derivedOI_qm_iff_layerFlowExecutable', qm_iff_derivedOI_pairFlowSourced)… | [holds for the substratum theory] substratumTheory_derivedOI (RouteB.lean:290) -> no record — args RouteB.lean:290 (none: closed statement) |
| I4.244 | ElementaryTransitionRichness | e/OPER/hypothesis-structure | assumed (conjunct of OIPlusPos) | — |
| I4.245 | OIPlusElem | e/OPER/hypothesis-structure | assumed (hypothesis of typed_determined_of_oiPlusElem) | — |

**Discharges for particular objects at L** (all matrix- or substratum-class level; none at level O or P):
- `ContextStable` (I4.29): for the substratum class by `substratumClass_contextStable` (StructuralClosure.lean:261)
  and for StateMixingCoupling's class by `mixC_contextStable` (StateMixingCoupling.lean:442) — both closed
  statements (no declared argument); general status *assumed*.
- `StructurallyClosed` (I4.45): for `substratumClass` by `substratumClass_structurallyClosed` (I4.46, :316; premise
  the class's definition I4.44); *assumed* for an extension (hypothesis of I4.47, I4.51, I4.52, I2.33).
- `HasParallelReferenceExtension` (I4.3): satisfiable by the full theory (I4.22, premise-free); refuted for the
  round-34 countermodel (I4.9, premise-free); not supplied by composite unitary control (I4.10) nor by the other
  OI⁺ principles (I4.95); equivalent to `InertSpectatorCompositionality` (I4.14) and implied by
  `ImplementationLocality` (I4.31), both *assumed*.
- `LayerFlowExecutable` (I4.56): holds under composite unitary control (I4.57; premises I4.67, I4.64); fails in the
  substratum theory for every involution moving a configuration (I4.59, premise-free).
- `ImplementationLocality` (I4.31) and `ReversibleImplementationLocality` (I4.133): hold for exact finite QM (I4.39,
  I4.136; premises I4.70 `ExactAllFiniteEndomorphicQuantumOps` — itself flagged — and I4.64).
- `EmbeddedObservation` (I4.110): holds for exact QM (`embeddedObservation_of_qm`, arguments
  `FiniteOperationalTheory`, `ExactAllFiniteEndomorphicQuantumOps`) and for every theory generated by a
  label-invariant architecture (I4.36; premises I4.30, I4.32).
- `DerivedOI` (I4.241): holds for the substratum theory (`substratumTheory_derivedOI`, RouteB.lean:290, closed).
- `DrivesElementary` (I4.143) and `QuantumArchitecture` (I4.144): refuted for `substratumClass` (StructuralClosure
  .lean:370, :376) and for the diagonal class (I4.147); hold for the full class (SubstratumSource.lean:151) —
  closed statements.
- (b) in its four forms (I3.150–I3.153), IE1 (I3.137), IE2 (I3.154), frame covariance (I3.155): PT-record open or
  flagged, IE1 and `IE1Drive` design-only [D]; no kernel statement at L discharges any of them for any object.
- `Q3`, `twin`, `pauliW` (I3.144): design modules only [D]; the PSD-cone facts I4.210, I4.215, I4.216 are
  premise-free matrix theorems (class a0), comparison objects only.

## 4. Item 3 — the ancestor set of the pair objects, the descendant set of Axioms 1–2, and where they fail to meet

Seeds (NOTES N3): `W d` I3.1, `actT` I3.6, `actC` I3.7, `cnot` I3.11, `CandidateCone` I3.43, H1–H3 I3.147–I3.149,
(b_S4), (b_n), (b_R1), (b_DJ) I3.150–I3.153. Edges `R`, `RA`, `RN`, `KC`; `Y` added as a control.

**Ancestor set Anc(P)** (25 nodes, `analyze.out` S3anc), all at levels P and O: the seeds; the definitions
`prodState` I3.2, `maxCone` I3.3, `IsEffectOn` I3.58, `ipW`/`dualW` I3.143 ([D]); the kernel facts about the
native gate I3.12 (`isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC`) and I3.13 (`nativeGate_cnot`); and the
single-token objects the (b) forms are stated with: I3.66 `ElementaryDrivability`, I3.67 `ball3Drive`, I3.80
`boundaryTransitive_fullAut3`. Its roots (non-derived members) and the obligation that would source each:

| root | status at L | missing source (obligation) |
|---|---|---|
| I3.1 `W d` (local tomography encoded) | assumed | K2 (I3.165): two-copy local tomography, the pair as a composite in `W 3` |
| I3.43 `CandidateCone`; I3.147 H1 | assumed; PT-record | K2 (`hadm`: products in `K`, `K ⊆ maxCone`) |
| I3.148 H2 (`cnot` / `G16` invariance) | PT-record | P-ACT2 (I3.146): the gate as an operation of the pair system |
| I3.149 H3 (`K = dualW K`) | PT-record | none at L: no ROADMAP row; `dualW`, `ipW`, `Q3` design-only (AUDIT-I §5.4) |
| I3.150–I3.153 (b) forms | PT-record, open | K2 "local actions compatible with the composite cone" (ROADMAP.md:1001–1005), with K∞-Act I3.168 and K∞-Drive I3.169 for the availability of the flow and `J` |
| I3.66 `ElementaryDrivability` | assumed / open | K∞-Drive (I3.169) |
| I3.143 `ipW`, `dualW` | [D] | none at L (design module) |
| I3.2, I3.3, I3.6, I3.7, I3.11, I3.58 | definitions [K] | none needed as definitions; `actC`/`actT` applied to a flow or `J` is (b) itself |

**Descendant set Desc(AX)** (31 nodes, S3desc): Axioms 1–2; I1.3; the observation-base posits I1.4, I1.6, I1.9,
I1.12, I1.13; Lemma 3 I1.10; the C1–C4 records I1.20, I1.21, I1.23, I1.24 and the manuscript items built on them
(I1.17, I1.18, I1.19, I1.25, I1.26, I1.29, I1.33, I1.34, I1.37); I1.5; I1.7, I1.8, I1.15; I1.35, I1.64, I1.69; and
two kernel theorems at level H, I1.84 (the finite-horizon observability quotient) and I1.85 (bare OI does not
make the ontic carrier observable), reached through their recorded links to Lemmas 2–3. Every member's span is
H (three manuscript records also carry M or X in a mixed level string: I1.17, I1.34, I1.35). No member is a
kernel declaration at level O, P, M or G.

**Meeting: NO-MEET.** Anc(P) ∩ Desc(AX) = ∅ — over the dependency edges; with the `yields` edges added (Anc 32,
Desc 41, shared 0); and with manuscript-asserted cross-level edges counted (the shared set is empty over all
edges, so the result does not rest on the supply rule). Countercontrol: one synthetic edge I3.1 → I1.1 yields
MEET-K. Every P-level node (94) has a closure free of Axioms 1–2, C1–C4 and of every H, M, G or X node; 49 of
them reach O-level nodes (the K∞ single-token premises, through I3's bridges B1–B7).

**Where they fail to meet, link by link** (each missing edge named by the obligation that would supply it):
1. manuscript H → kernel H: the kernel carries images of the axioms and of C1–C4 on one eight-state carrier
   (`SealedCoreIsFiniteOI`, `CoreC1C4`, I1.39, I1.42; ManuscriptAxioms.lean "images, not the axioms", I1.55); no
   kernel theorem takes Axiom 1, Axiom 2 or a general C1–C4 as a hypothesis. Nearest open row: the stochastic
   observer interface (I1.76, ROADMAP.md:69, OPEN).
2. H or M → O: no kernel theorem at L ends at a K∞ premise (I3's A9; I4's `bridge_scan3`); the obligation is K∞
   (I3.166) with its seams K∞-Stage I3.167, K∞-Act I3.168, K∞-Drive I3.169, K∞-Trans I3.170, K∞-Seed I3.171,
   K∞-V4 I3.172, K∞-Copy I3.173 (OPEN).
3. H, M or G → P: none (AUDIT-I §5.3; I3's A8–A9; I4's `bridge_scan`): obligation K2 (I3.165, OPEN).
4. O → P beyond products and involutions (I3's B1–B7 transfer effect availability, products, carrier identities
   on products, the Lorentz effect cone, the π-rotation NOT, `eball_three`; I3's A1–A2): the composite action of
   a flow or `J` — (b) — obligation K2's "local actions compatible with the composite cone", with K∞-Act and
   K∞-Drive for single-token availability; closedness of a pair cone — P-STAGE2 (I3.145, A3); gate
   preservation — P-ACT2 (I3.146, A4); the dimension selector — K1 (I3.164, CONDITIONAL).
5. single-ball self-duality → pair self-duality H3: none at L, no obligation row (I3's A6; AUDIT-I §5.4).

## 5. Item 4 — the check script (`check.py`, `check.out`)

Independent of the build scripts: it imports none of them and re-reads the record ids, titles, statuses and
dependency texts from the inventories, the declarations from the kernel at L and the design modules, and the
nodes and edges from `graph.tsv`. Decision rule, sampling rule and the 44-node sample are in its header,
written before run 1; amendments before runs 2 and 3 are in the header (NOTES N4).

| check | result |
|---|---|
| C0 — 633 nodes, each with kind, status, level and class; every edge source a node | PASS |
| C1 — every edge target (1549 rows, `Y` included) exists: record id, declaration at L, or design declaration | PASS |
| C2 — no directed cycle among the dependency edges | **FAIL**: two strongly connected components, I2.6 ⇄ I2.10 and I2.42 ⇄ I2.56 |
| C3 — kernel-signature agreement on 44 theorems (I1 10, I2 10, I3 12, I4 12) | **FAIL**: 19 AGREE-RECORDED, 21 INCOMPLETE-RECORDED, 4 DISAGREE |
| CC1 / CC2 / CC3 — countercontrols (an absent target; a synthetic cycle; a removed signature head) | each behaves |

No VERDICT line is printed. Sampling rule: eligible = derived rows with kernel-proved status and kind
theorem (I1 20, I2 22, I3 61, I4 140), positions ⌊j·n/m⌋ (m = 10, 10, 12, 12); a node whose header names no
theorem declared at L is replaced by the next eligible node: I1.40 → I1.41, I2.94 → I2.23, I2.98 → I2.26.

**C2.** Both cycles join two non-derived records that cite each other: I2.6 (the adopted Bell branch, *assumed*)
lists I2.10 (operational no-signalling, "assumed for the adopted branch"), which lists I2.6; I2.42 (the
definition of unitarily evolving QM with the translation hypothesis (T), *assumed*) lists the Barandes
correspondence I2.56 (an imported external theorem, assumed under (T)), which lists I2.42. Neither cycle contains
a derived node, so no derivation is circular; the records state co-presupposition as mutual dependence. Neither
cycle meets Anc(P) or Desc(AX).

**C3.** INCOMPLETE-RECORDED (21): the recorded field omits a declared argument that `KC` supplies — mostly the
carrier (`FiniteOperationalTheory` I4.64 for I4.5, I4.19, I4.83, I4.101, I4.122, I4.160, I4.173, I1.44, I1.54; `W`
I3.1 for I3.12, I3.17, I3.22, I3.37), and named hypotheses: `RootedRealization` (I1.27), `ClassData` (I1.82),
`ExactAllFiniteEndomorphicQuantumOps` (I1.54), `Isotropic`/`Separable` (I2.21), `Passive` (I2.27), `Stochastic`/`IsDiag` (I2.39), `IsBoundaryState` I3.60 (I3.90), and for I2.23,
I2.33, I2.36 the hypotheses of the cited kernel theorems (I2.33: `ImplementationClass`, `ExtendsSubstratum`,
`StructurallyClosed`, `DrivesElementary`, `ReadWriteSourced`). DISAGREE (4) — a recorded dependency named nowhere
in the cited declarations (signature or proof) and with no recorded reason: I2.25 → I2.39, I2.36 → I2.33, I2.96 →
I2.95 (manuscript or ROADMAP-level dependencies of records whose status cites kernel theorems), I3.105 → I3.103
(a definition reached only through `OpDatum`). Other recorded dependencies that are not arguments of the
declaration but are manuscript records are listed as MS-links and not judged (e.g. I1.84 → I1.9, I1.10).

## 6. Item 5 — statuses, lemmas, levels

- **No status change.** Every status in `graph.tsv` is the record's own string (cut at 160 characters); the
  derived / non-derived split reads it and changes nothing.
- **Lemmas through their dependencies.** A derived node is never a root: the closure passes through every proved
  item to its own premises (e.g. I3.37 reaches the K∞ premises through I3.51 `maxConeOf_avail_eq`; I4.89
  reaches I4.64 through `oiPlus_iff_qm`), and `RA` edges inherit the premises named by "as Ix.n".
- **Levels kept apart.** Cross-level dependency edges (`analyze.out` S4): P → O 61 (43 from kernel records), O →
  P 10, H ↔ M 28, M ↔ G 34, and a few with mixed spans (counts by direction and supply in S4). No dependency
  edge joins H, M or G to P; the only edges joining H, M or G to a span containing O are two inside I2, both
  from manuscript records (I2.3 → I2.17, counted K by the supply rule because I2.3's status cites a [K]
  component; I2.63 → I2.64, MS), and neither lies on a path to or from a pair seed. An H–M or M–G edge whose
  source is a kernel record is a recorded or completed dependency of that declaration; §5 checks such fields
  against the signatures on the sample only. The supply rule counts ten I2 manuscript statements as kernel
  because their status cites kernel theorems (§1).

## 7. Findings (§A.31 output labels)

1. CONFIRMING, at the level of the whole record graph, of AUDIT-I §5.2–§5.3: no path joins the descendants of
   Axioms 1–2 to the premises of `W 3`, `K`, `cnot`, `actC`/`actT`, H1–H3 or (b), under any of the edge rules,
   and the missing links are exactly K∞, K2, P-STAGE2, P-ACT2, K1, and nothing for H3.
2. NEW: the descendant set of Axioms 1–2 is 31 records, all at level H; its only kernel members are two
   passive-observability theorems (I1.84, I1.85) reached through recorded application links to Lemmas 2–3. The
   axioms have no descendant among the C1–C4 kernel forms (I1.39, I1.70–I1.73) or the core-realization
   theorems (I1.41–I1.60): the kernel's core and C1–C4 predicates are definitions on one carrier, not consequences
   of the axioms in the graph.
3. NEW: the only consequence of Axioms 1–2 alone is a no-go (I1.3, the non-derivability of Axiom 2). Lemmas 1–3
   do not follow from Axiom 1 alone in the records: Lemma 1 (I1.8) uses the Definition of an observation (I1.6)
   and the perspectival reading (I1.4), both *assumed*; Lemma 2 (I1.9) is *assumed* (definitional); Lemma 3
   (I1.10) is *empirically motivated / assumed*. Assumption-watch marker: any manuscript claim that a result
   follows "from Axiom 1" passes through I1.4 and I1.6.
4. NEW (record-level, for the coordinator): two dependency cycles between assumed records (I2.6 ⇄ I2.10, I2.42 ⇄
   I2.56); four recorded dependencies of [K]-status records that their cited declarations do not contain (I2.25,
   I2.36, I2.96, I3.105); 21 of 44 sampled [K] theorems with a recorded field narrower than the kernel signature
   (completed here by 152 `KC` edges on 122 nodes).
5. ELABORATING: (b) is a seed with no premise at L other than the single-token objects it is stated with
   (I3.66, I3.67, I3.80); no do-not-assume item is a hypothesis of any derived node in Anc(P).
6. BORDERLINE (method): the classification of 21 non-derived H/X records as physical, of six as
   observation-base posits, and of free-text hypotheses by keywords is a convention fixed in NOTES N2; it moves
   items between (c) and (d) (run 1 → final: d 63 → 36) but never into or out of (a1), (a2) or (b) except I2.53 and
   I2.61, and it does not touch item 3.

## 8. What is not claimed

- No derivation, no verdict on (b), (b_min), `K = Q3` or the stage's question; the graph records dependencies at
  L as the inventories and the kernel state them.
- "Consequence" in the partition means: reachable by recorded or kernel-completed dependency edges; it is not
  a proof. (a0) items need no premise, which says nothing about their relevance to the axioms.
- NO-MEET is a statement about the record graph at L under the stated edge rules; it does not say that no bridge
  can be proved.
- `KC` completion covers derived kernel-proved nodes whose header names a theorem declared at L (122 of 252);
  section `variable` binders are included without section scoping; a hypothesis written in a conclusion
  (`A → B` after the colon) is not a declared argument and is not completed.
- The physical / operational / observation-base categories of NOTES N2 are a convention; every root is listed by
  id so that another convention can be applied to `graph.tsv` without rebuilding it.
