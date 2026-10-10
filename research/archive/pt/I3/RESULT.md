# I3 RESULT — operational foundations and composite reconstruction (Q-EX-FULL, stage 6, step 1)

Thread I3, research only, read-only on the corpus. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`).
Governing text `pt/PROTOCOL-STAGE6.md` (`b277b7c1…`) with the earlier protocols it names. Deliverables in `pt/I3/`:
`INVENTORY.md` (records `I3.1`–`I3.187`), `CENSUS.md`, `NOTES.md`, this file. The inventory records; it decides nothing
about (b_min).

## §0 — Summary

**Scope covered.** The K programme at L: the 22 kernel modules governed by the K-programme rounds (K∞: KINF-1/2, OG-1,
TRB-1, IIP-1, CMP-1, OPACT-1, ORD-1, KTRANS-DENSE-1; K1: DIM-1, NB-1, EFF-1, K1-BRIDGE-1, K1-SHARP-TESTS-1, PARITY-NOT-1,
ODD-CHAR-1, RELC-SELECT-1; K2: K2-GUARD-1, COMP-1), the landed KT4 premise audit (KT4-PREM-1), the eleven four-copy design
modules [D] of `pt/inputs/fourcopy/`, the ROADMAP K row (`ROADMAP.md:68`, `:971–1102`) with the seams audit
(`verification/audits/foundations/kinf-seams-audit.md`), the PT stage records as far as they fix the pair premises
(H1–H3, the (b) forms, IE2, frame covariance, INV2, SDC, N0–N2, S2 Pair, H, T), and the one manuscript paragraph in scope
(`papers/Main.md:352`). Depth-first order as instructed: the pair carrier and `NativeGate` (§A–§D), then
`ElementaryDrivability` and the K∞ data (§E), the composite interface and NB-1 (§F–§G), the KT4 premises (§H), the PT
premises (§I), the obligations (§J), the manuscript (§K), additions (§L).

**Counts** (187 records; `rcount.out`, run 3, replayed identically).
- By kind: hypothesis-structure 63; theorem 64; definition-as-hypothesis 32 (one of them combined with a theorem,
  I3.142); lemma-folded 5; obligation 22; manuscript-principle 1.
- By status: proved [K] 92; assumed 40; open 22; conditional 3 (I3.164 K1; I3.184 Main.md:352; I3.187 KT4-PREM-1's
  written classification step); refuted 1 (I3.180, the KINF-1 vocabulary); not at L, design module [D] 14 (I3.129,
  I3.130, I3.133–I3.144); PT-record 15 (I3.147–I3.161). No status was upgraded; [D] and PT-record are marked as outside
  the L vocabulary.
- By level: O 92; P 94; X 1; H 0; M 0; G 0 (the K programme has no item at the substratum, matrix or general-carrier
  level; those levels are threads I1, I2, I4).
- Censuses (`CENSUS.md`): (a) kernel 47 Prop-valued items + 14 [D] items + 14 data structures, all mapped; 15 modules met
  in K-round records but not governed by them, out of scope (I2: 11, I4: 4); (b) manuscripts 161 vocabulary hits: 1
  mapped (M017 → I3.184), 152 out of scope (thread I2), 8 not census items (references, literature comparisons); (c)
  roadmap 30 K-section units: 24 mapped, 1 out of scope (K3 → I4), 5 navigation links; 2 lines outside the section: 1
  mapped (I3.162), 1 out of scope (I2). **Unmapped census entries: none.**

**Every item with `bearing` other than `none at L`** (142; generated from the tally, `r0lists.out`):

- **direct constraint on `K` or on (b_min)** (80): I3.1 `W d`; I3.2 `prodState`; I3.3 `maxCone`; I3.4 `jointStates`; I3.5 `IsProduct`; I3.6 `actT`; I3.7 `actC`; I3.9 `NativeGate`; I3.10 `Entangling`; I3.11 `cnot`, `sgn`, `pc`, `pt`, `z3`, `nflip`, `xplus`, `phiW` (the `; I3.12 `isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC`; I3.13 `nativeGate_cnot`; I3.14 `entangling_cnot`; I3.15 parity: `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGate; I3.16 `blockData_of_nativeGate` (with `BlockData`); I3.17 `not_entangling_one`; I3.20 DIM-1 controls: `nativeGate_cnot1`, `not_entangling_cnot1`, `no_; I3.22 `not_even_of_gateRel` (with `finrank_plus_eq_finrank_minus_rel`); I3.23 `GateRel`; I3.25 `not_gateRel_refl3`, `not_gateRel_negId3`; I3.26 `not_posFwd_gJ3`, `not_posFwd_gJ5`; I3.27 `exists_frame_gateRel_iff_odd`; I3.28 `not_posFwd_gRev`; I3.29 `CtrlGate`; I3.30 `not_even_of_relC`; I3.32 `ctrlGate_of_nativeGate`; I3.33 `gSq_sep`, `gSqInv_sep`; I3.34 `relT_not_dimension_selecting`; I3.35 `NativeGateOf`; I3.36 `EntanglingOf`; I3.41 `two_le_not_implied`; I3.42 `prodState_mem_maxCone`; I3.43 `CandidateCone`; I3.44 `no_candidateCone_cnot_reflY`; I3.46 `two_le_of_entangling`; I3.49 `maxConeOf`; I3.113 `ProductData`; I3.114 `PreComposite`; I3.115 `LocallyTomographic`; I3.116 `Composite`; I3.118 `JointReversible`; I3.120 `condA_prodState` (L9, no signalling on products); I3.121 `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPre; I3.122 `comp1_core` (COMP-1 verdict); I3.129 `hcls` — N-CLASS gates (`NClass`); I3.130 `hadm` — pair admissibility (`PairAdm`, with `IsConvexCone`); I3.131 `hcl` — closedness of each pair cone; I3.132 `hgate` — gate preservation (H2 of stage 3 is this clause for `c; I3.133 `H` — the four-copy core (`KT4Core`, with `KT4`, `KT4LT`); I3.134 token clauses `tokA`, `tokB` (`TokenCoherent`); I3.135 FCC — the cone-level four-copy interface (`FourCopyCoherent`, `F; I3.136 `PairLinked` (Lemma R's interface form); I3.137 IE1 (`IE1`, with `IsRot3`, `IsOrth3`); I3.138 `EvenCycle` (with `EvenCycle4`); I3.139 `kt4_forward_ie1` (Theorem A′, the audited theorem); I3.140 `fourCopyCoherent_of_kt4Core` (Lemma B1); I3.141 `KT4Cone`; I3.142 `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the d; I3.143 `ipW`, `dualW` (the Euclidean pairing and dual cone of tables); I3.144 `Q3`, `twin`, `pauliW`, `twistQ3`; I3.145 P-STAGE2 (named premise of KT4-PREM-1); I3.146 P-ACT2 (named premise of KT4-PREM-1); I3.147 H1 — products in `K`; I3.148 H2 — `cnot`-invariance (level (i)); `G16`-invariance (level (ii); I3.149 H3 — trace self-duality `K = dualW K`; I3.150 (b_S4) — the full rotation group of one token acts on the pair p; I3.151 (b_n) — one rotation subgroup of one token about an off-frame ax; I3.152 (b_R1) — one order-3 rotation of one token about (5,1,1); I3.153 (b_DJ) — the native drive with the native `J` acting on one toke; I3.154 IE2 — idle extension of the pair interaction groups; I3.155 frame covariance (FC) of the native gate; I3.156 INV2 — the native gate is an operational involution on the pair ; I3.157 SDC = P3 ∧ OVL4 ∧ CSD2 — self-duality under composition; I3.158 N0 ∧ N1 ∧ N2 — regrouping invariance of a four-token composite (; I3.159 S2 Pair — a compact, gate-reversible COMP-1 pre-composite (stage; I3.160 H — pair-level homogeneity of `K`; I3.161 T — pair-level reversible richness (transitivity on extreme rays; I3.165 K2 — the composite; I3.185 carrier-map identities for every one-copy linear map: `actT_prod; I3.187 the classification step of KT4-PREM-1: `hcls ∧ hadm ∧ hgate ∧ IE
- **constrains the single-token structure the pair inherits** (25): I3.8 `IsNot`; I3.18 `dim_of_nativeGate` (the selector); I3.19 `three_of_nativeGate`; I3.21 `dim1_core` (DIM-1 verdict); I3.24 `piRotation_three` (with `tangentPlus_three`, `det_three`); I3.31 `dim_of_ctrlGate`, `three_of_ctrlGate`; I3.37 `dim_of_nativeGateOf`; I3.38 `three_of_nativeGateOf`; I3.39 `HasTwoSharpTests`; I3.40 `hasTwoSharpTests_iff`; I3.45 `three_of_nativeGate_of_two_le`; I3.47 `three_of_nativeGateOf_of_two_le`; I3.69 `CopyNatural` (K∞-Copy); I3.76 `BoundaryTransitive` (K∞-Trans; "K∞-R" in OG-1's record); I3.87 `TransBody` (TRANS); I3.88 `eq_qBall_of_boundaryTransitive`; I3.89 `exists_affine_image_eq_eball`; I3.124 the effect cone of the ball: `lor_ehom`, `isEffectOn_affOf`, `lo; I3.125 `NativeGateBall.parity`; I3.126 `p_le_one`, `dim_of_bounds`; I3.128 `nb1_kernel_core` (NB-1 verdict); I3.164 K1 — the dimension; I3.166 K∞ — the field-neutral premises; I3.173 K∞-Copy; I3.186 `eball_three`
- **constrains the single-token structure, not read by any pair statement at L** (20): I3.50 `MixingClosed`; I3.52 `fullEffects_subset_avail`; I3.53 `not_fullEffects_of_orbit`; I3.57 `FiniteStage`; I3.78 `preservesBody_drive`; I3.79 `seedOrbit_ball3_eq` (the reduced orbit-generation theorem); I3.80 `boundaryTransitive_fullAut3`; I3.82 `orbit_generation_core` (OG-1 verdict); I3.83 `boundaryTransitive_ball3Drive` (with `driveWords3`); I3.92 `DirectedStages` (with `StageMap`); I3.94 `SCInf` (SC∞, K∞-Stage); I3.95 `BinaryVisible` (ELEM-bin); I3.97 `sharpSeed_completion`; I3.98 `exists_chart_of_finiteRank`; I3.101 `AffineRespect`; I3.111 `finiteOrderOn_of_stagePreserving`; I3.127 `lorentz_of_effects`; I3.167 K∞-Stage; I3.168 K∞-Act; I3.169 K∞-Drive
- **constrains the composite only through a named bridge** (I3.51 `maxConeOf_avail_eq`, I3.56 its dense form, or the absent P-STAGE2/P-ACT2 for I3.96, I3.99, I3.104, I3.105) (17): I3.48 `EffectsOn`; I3.51 `maxConeOf_avail_eq` (with `sharpFamily_subset_avail`, `maxConeO; I3.54 `DenseBoundaryOrbit`; I3.55 `denseBoundaryOrbit_of_boundaryTransitive`; I3.56 `maxConeOf_avail_eq_of_dense` (with the dense ball and selector ; I3.58 `IsEffectOn`; I3.60 `IsBoundaryState`; I3.73 `SharpSeed` (K∞-Seed, P1); I3.74 `PreservesBody`; I3.75 `SeedOrbitAvailable` (K∞-V4, V4′); I3.96 `FiniteRank` (K∞-Stage); I3.99 `OpDatum` (K∞-Act); I3.104 `body_isClosed`; I3.105 `preservesBody_inducedEquiv`; I3.170 K∞-Trans; I3.171 K∞-Seed; I3.172 K∞-V4
- for completeness, **none at L** (45): I3.59, I3.61, I3.62, I3.63, I3.64, I3.65, I3.66, I3.67, I3.68, I3.70, I3.71, I3.72, I3.77, I3.81, I3.84, I3.85, I3.86, I3.90, I3.91, I3.93, I3.100, I3.102, I3.103, I3.106, I3.107, I3.108, I3.109, I3.110, I3.112, I3.117, I3.119, I3.123, I3.162, I3.163, I3.174, I3.175, I3.176, I3.177, I3.178, I3.179, I3.180, I3.181, I3.182, I3.183, I3.184

(Titles in these lists are cut at 64 characters by the generator; the full titles are in `INVENTORY.md`.)

**Bridges found at L** (kernel theorems that carry an item across levels into, or out of, the pair carrier `W d`):
- **B1** `maxConeOf_avail_eq` (EffectSpace.lean:572; I3.51), O → P: body preservation, K∞-Seed, K∞-Trans, K∞-V4 and effect
  soundness on one ball make the product-test cone of the available family equal to `maxCone (eball d)`. It transfers
  effect availability, not operations. Consumers: `nativeGate_of_avail`, `entangling_of_avail`, `dim_of_nativeGateOf`,
  `three_of_nativeGateOf` (K1Bridge.lean:128, :138; I3.37–I3.38), `three_of_nativeGateOf_of_two_le` (K2Guard.lean:253;
  I3.47).
- **B2** `maxConeOf_avail_eq_of_dense` (DenseOrbit.lean:243; I3.56), O → P: the same with a dense boundary orbit.
- **B3** `prodState_mem_maxCone` (K2Guard.lean:165; I3.42), O → P: products of states of one copy lie in `maxCone`.
- **B4** `actT_prodState`, `actT_tens`, `actC_tens`, `toOp_actC` (K2Guard.lean:173; CompositeDimension.lean:1923, :1930,
  :451; I3.185), O → P on products only: every one-copy linear map, idle-extended by `actT`/`actC`, sends products to
  products. No kernel statement at L concerns non-product vectors under `actC g`/`actT g` for `g` not an involution.
- **B5** `lor_toOp_of_maxCone` (CompositeDimension.lean:1049; I3.124), O ↔ P: a `maxCone` vector read as an operator maps
  the single-ball (Lorentz) effect cone into itself.
- **B6** `piRotation_three` (ParityNot.lean:161; I3.24), P → O: `IsNot` with the two gate relations forces the NOT at
  `d = 3` to be a π-rotation (`det N = 1`); `not_gateRel_refl3`/`not_gateRel_negId3` (I3.25) exclude the determinant −1
  NOTs.
- **B7** `eball_three` (TransitiveBody.lean:670; I3.186), O-level identification: the K∞ ball `ball3` and DIM-1's
  `eball 3` are the same set (not a transfer to `W 3`).
- Not a bridge theorem but the only place a one-copy map meets the gate: the hypothesis fields `relT`/`relC` of
  `NativeGate`, `GateRel`, `CtrlGate`, `NativeGateOf` (I3.9, I3.23, I3.29, I3.35) — relations between `actT N`, `actC N`
  and the gate, with `N` the NOT; no invariance of a pair cone under `actC N`/`actT N` is stated.

**Bridges absent at L** (named; what exists instead):
- **A1** `ElementaryDrivability` (flow, NOT `D.N = D.flow D.t₀`, `J`; I3.66) → any pair statement: none. `actC`/`actT`
  are never applied to a flow member, `J` or `cyc3`; no theorem relates `D.N` (an affine equivalence) to an `IsNot` NOT
  or to `nflip`; `ElementaryDrivability` is read only in `OrbitGeneration`/`OrbitNormalization`. The only pair-level
  lift of the drive words anywhere is the design predicate `IE1Drive` (FourCopyPackage.lean:279, [D]) with
  `ie1Drive_of_ie1` a `sorry` (I3.142).
- **A2** one-body symmetry (`fullAut3`, `driveWords3`, `BoundaryTransitive`; I3.76, I3.80, I3.83) → invariance of a pair
  cone: none at L; it would be (b_S4)/(b_DJ). Present only as the [D] predicates `IE1` and `IE1Drive`.
- **A3** K∞-Stage (`SCInf`, `FiniteRank`, `body_isClosed`; I3.94, I3.96, I3.104) → closedness of a pair cone (`hcl`):
  none; the named missing premise is P-STAGE2 (I3.145). No declaration builds a directed system from two systems.
- **A4** K∞-Act (`OpDatum`, `preservesBody_inducedEquiv`; I3.99, I3.105) → gate preservation on a pair cone (`hgate`):
  none; the named missing premise is P-ACT2 (I3.146), whose idle-extension reading for rotations is IE1.
- **A5** `CopyNatural` (I3.69) → the common NOT of `NativeGate`: none; the common `N` is built into `NativeGate`.
- **A6** single-ball self-duality (the Lorentz effect cone, `lorentz_of_effects`; I3.124, I3.127) → pair self-duality
  H3 (I3.149): none; `dualW`/`ipW` exist only in a design module (I3.143).
- **A7** COMP-1 `Composite` (I3.116) → the carrier `W d`: none (adapter open, DIM-1 "What stays open").
- **A8** matrix level M (`Q3`/PSD self-duality, `psd_iff_trace_nonneg`, `DrivesElementary`, the OI⁺ modules) → `W d`:
  none; no module outside the 22 K modules imports any of them (`kimports.out`); `pauliW` and `Q3` on `W 3` exist only
  in the [D] preflight (I3.144).
- **A9** substratum level H (Axioms 1–2, C1–C4, the realization theorems) → `W d`: none; same import fact.
- **A10** four-token data → pair cones: only the [D] theorems `kt4_forward_ie1` and Lemma B1 (I3.139–I3.140).
- **A11** TRB-1's ball (`exists_affine_image_eq_eball`; I3.89) → DIM-1's hypothesis `eball d`: no composing kernel
  theorem (DIM-1 takes `eball d` as given).
- **A12** field-neutral drivability → sharp effects: open (ROADMAP.md:1053–1055; I3.178).
- **A13** the stage-level product of two `DirectedStages` and its identification with `W 3`: none (COMP-1 header;
  KT4-PREM-1 open question 3).

**Do-not-assume items** (stage-6 flag list; recorded, never used).
- Items that are themselves on the list: I3.137 IE1; I3.142 `IE1Drive` (IE1 in drive form); I3.144 `Q3`/`twin`/`pauliW`;
  I3.150 (b_S4); I3.151 (b_n); I3.152 (b_R1); I3.153 (b_DJ); I3.154 IE2; I3.155 frame covariance.
- Items at their own status whose flag names a do-not-assume clause or extension: I3.6 `actT` and I3.7 `actC`
  (invariance of `K` under a rotation); I3.66 `ElementaryDrivability` (its pair-level extension); I3.80 `fullAut3` and
  I3.83 `driveWords3` (their pair action); I3.118 `JointReversible` (an idle-extended instance); I3.139 `kt4_forward_ie1`
  (its conclusion is IE1); I3.146 P-ACT2 (the idle-extension reading); I3.165 K2 ("local actions compatible with" the
  composite cone); I3.184 (the five completion conditions of Main.md:352); I3.187 (uses IE1).
- On the stage-6 list but outside I3's scope: the OI⁺ completion conditions (i)–(v), observational independence,
  reversible richness, observer recursion, implementation locality's spectator clause, structural closure of an
  extension, `LayerFlowExecutable` (kernel side thread I4, manuscript side thread I2).

**Exposed facts** (record-only; gem-finding mode; none is a verdict on (b_min)):
1. The K-programme modules form a leaf cluster: no kernel module outside the 22 imports any of them, directly or
   transitively (`kimports.out`). At L no theorem at level H, M or G can read `W d`, `NativeGate`, `maxCone` or
   `ElementaryDrivability`.
2. On `W d`, every statement that constrains pair vectors under a one-copy map concerns an involution (a NOT or
   `reflY`); arbitrary one-copy maps occur only in identities that reach product vectors (B4); the one invariance
   statement for a non-gate local map is a no-go (`no_candidateCone_cnot_reflY`, I3.44).
3. The landed control drive `ball3Drive` (flow about the third axis; NOT `rot3 π`, which fixes `z3`; `J = cyc3`) and
   DIM-1's NOT `nflip` (the half-turn about the first axis, inverting `z3`) are distinct and unrelated in the kernel
   (reading of the definitions, not a kernel theorem). The "native drive through the NOT, on the NOT axis" of stages 4–5
   is a PT construction.
4. `dualW`, `ipW`, `Q3`, `twin` and `pauliW` have no kernel definition at L; H3 and the comparison object `Q3` on `W 3`
   are defined in the design modules (FourCopyDefs.lean:30–34, FourCopyPackage.lean:174–190) and in the PT stage
   protocols and scripts, not in the kernel; the kernel's PSD self-duality is matrix-level (thread I4).
5. None of the five premises of the audited four-copy theorem has an independent source at L (KT4-PREM-1); P-STAGE2 and
   P-ACT2 are the named missing pair-level bridges for closedness and gate preservation.
6. No paper or book chapter at L states a K-programme premise; Main.md:352 places the reconstruction axioms
   (purification, continuous transitivity, tomographic locality) as hypotheses of continuum endpoints.

## §1 — The inventory by section (records in `INVENTORY.md`)

| section | ids | content |
|---|---|---|
| §A the pair carrier and the native gate (DIM-1) | I3.1–I3.21 | `W d` (LT encoded), `prodState`, `maxCone`, `jointStates`, `IsProduct`, `actT`, `actC`, `IsNot`, `NativeGate`, `Entangling`, the `d = 3` witness (`cnot`, `nflip`, `z3`, `phiW`), parity, block data, the selectors, controls, `dim1_core` |
| §B the gate hypotheses taken apart | I3.22–I3.34 | `GateRel`, parity from the relations, the π-rotation NOT, `CtrlGate`, parity from `relC`, positivity separations, `relT` not dimension-selecting |
| §C K1 relative to available tests; sharp tests; K2 guard | I3.35–I3.47 | `NativeGateOf`, `EntanglingOf`, relative selectors, `HasTwoSharpTests`, `prodState_mem_maxCone`, `CandidateCone`, `no_candidateCone_cnot_reflY`, the `2 ≤ d` selectors |
| §D the effect set and the product-test cone | I3.48–I3.56 | `EffectsOn`, `maxConeOf`, `MixingClosed`, `maxConeOf_avail_eq` (B1), full effects, dense boundary orbits (B2) |
| §E K∞ single-system premises | I3.57–I3.112 | `FiniteStage`, effect vocabulary, SEC, SF, `ElementaryDrivability`, `ball3Drive`, `CopyNatural`, `KInf1`, OG-1 hypotheses and theorems, TRB-1 ball, IIP-1, CMP-1 stages, OPACT-1 operation data, ORD-1 order |
| §F the composite interface (COMP-1) | I3.113–I3.122 | `ProductData`, `PreComposite`, `LocallyTomographic`, `Composite`, `JointReversible`, `SharpReadout`, no-signalling on products, LT independence |
| §G NB-1 and the effect cone of the ball | I3.123–I3.128 | `Lor`, the Lorentz effect cone (B5), `parity`, `p_le_one`, `lorentz_of_effects` |
| §H the KT4 premise audit and the design modules [D] | I3.129–I3.146 | `hcls`, `hadm`, `hcl`, `hgate`, `H`/`KT4Core`, token clauses, FCC, IE1, `EvenCycle`, `kt4_forward_ie1`, Lemma B1, `KT4Cone`, `IE1Drive`, `ipW`/`dualW`, `Q3`/`twin`, P-STAGE2, P-ACT2 |
| §I the pair premises in the PT stage records | I3.147–I3.161 | H1, H2, H3, (b_S4), (b_n), (b_R1), (b_DJ), IE2, frame covariance, INV2, SDC, N0–N2, S2 Pair, H, T |
| §J the ROADMAP K row | I3.162–I3.183 | P1 K, framing, K1, K2, K∞ and its eight seams, the label note, the geometric scope notes, Kₙ, KINF-1, the research direction, the finite route, orthogonality to P0 |
| §K manuscript | I3.184 | Main.md:352, the reconstruction axioms |
| §L additions | I3.185–I3.187 | carrier-map identities (B4), `eball_three` (B7), KT4-PREM-1's written classification step |

## §2 — Ledger of sources read

- Protocols and PT records, in full: `pt/PROTOCOL-STAGE6.md`, `PROTOCOL-STAGE5.md` with its amendment 1,
  `PROTOCOL-STAGE4.md`, `PROTOCOL-STAGE3.md`, `PROTOCOL.md`, `INTEGRATION-NOTE-STAGE4.md`, `INTEGRATION-NOTE-STAGE3.md`,
  `INTEGRATION-ADDENDUM-STAGE2.md`, `INTEGRATION-REVIEW.md`; `pt/base/AGENTS.md` (byte-identical to the working-tree copy).
  Searched (grep, targeted lines): `pt/U/RESULT.md`, `pt/X/RESULT.md`, `pt/Y/RESULT.md`, `pt/audit/U/AUDIT-U.md`,
  `pt/audit/X/AUDIT-X.md`, `pt/audit/Y/AUDIT-Y.md`, `pt/audit/Z/AUDIT-Z.md`, `pt/S3/RESULT.md` (H3 and (b) status lines).
- Kernel at L: the 22 K modules — module headers in full; every Prop-valued declaration and data structure (`kcensus.out`,
  `kcensus2.out`); 161 headers and docstrings (`kdecls.out`); `CompositeDimension.lean:1–250, 676–866, 1148–1225,
  1376–1442, 2700–3007`; `KInfFoundations.lean:1–80, 114–162, 255–305, 349–358, 440–494, 985–1212`;
  `OrbitGeneration.lean:1–86, 146–172, 344–368, 518–540, 616–626`; `OrbitNormalization.lean:563–573, 663–668`;
  `TransitiveBody.lean:221–236, 669–675`; `StageCompletion.lean:52–80, 136–150, 218–226, 240–252, 296–301`;
  `CompletionAction.lean:44–60, 140–152, 198–203, 320–328`; `CompositionOrder.lean:45–66, 230–238`;
  `CompositeInterface.lean:137–142, 205–250, 328–333, 389–398, 440–447, 803–813, 905–945`; `EffectSpace.lean:405–414,
  564–595`; `K1Bridge.lean:46–67`; `SharpTests.lean:39–46`; `K2Guard.lean:93–98, 168–195`; `DenseOrbit.lean:50–56`;
  `ParityNot.lean:40–46`; `RelcSelectBlock.lean:43–52`; `NativeGateBall.lean:100–107, 170–197, 245–250`; the whole
  kernel tree by grep for `actC`/`actT`, `ElementaryDrivability`/`ball3Drive`/`cyc3`/`CopyNatural`, `dualW`/`ipW`/
  `Q3`/`twin`, import lines (`kimports.out`); headers of `CoherentExtension`, `FactorExchange`, `RegionLimit`;
  `SubstratumSource.lean:77` and `StructuralClosure.lean:364` (names only, for the A8 distinction).
- Round records at L (`verification/programmes/oi-qm/reconstruction/`): DIM-1 and KT4-PREM-1 result notes in full; the
  outcome and open sections of the result notes of KINF-1, KINF-2, OG-1, TRB-1, CMP-1, IIP-1, OPACT-1, ORD-1, COMP-1,
  EFF-1, K1-BRIDGE-1, K1-SHARP-TESTS-1, K2-GUARD-1, KTRANS-DENSE-1, NB-1, ODD-CHAR-1, PARITY-NOT-1, RELC-SELECT-1; the
  `v3-governed-paths` blocks of every round's preregistration; BG-1's preregistration head.
- `verification/ROADMAP.md:60–72, 940–1112`; `verification/README.md:280–310` and grep; `verification/audits/foundations/
  kinf-seams-audit.md` in full; the directory listing of `audits/foundations/`.
- Manuscripts: grep of the 12 papers and 30 book files (`mcensus.out`); `papers/Main.md:352, :540`;
  `papers/Structure.md:592, :605`; `book/ch19-open-problems.md:224` (= FULL.md:5388).
- Design modules [D]: `FourCopyCore.lean` (header, :28–37, :61–187), `FourCopyDefs.lean:28–62, 95–99`,
  `FourCopyHeadline.lean` (header, :112–162), `FourCopyBridge.lean:267–280`, `FourCopyPackage.lean` (header, :82–88,
  :174–330); `sorry` counts of all eleven.
- Research ledgers (leads, not at L): `pt/inputs/ledgers/DRIVE-RESULT.md:1–150`, `OPACT-RESULT.md:1–45`,
  `OISTAGE-RESULT.md:1–95`, `KN-CENSUS-RESULT.md:1–50`, `K-INF-DESIGN.md` (section list, §0–§2), `EQ2-SYNTHESIS.md`
  (grep, :75–:85), `HINF-REVIEW.md` (grep); `pt/inputs2/oi-substratum/RANK-RESULT.md`, `QUOTIENT-RESULT.md`,
  `RECORD-RESULT.md` (verdict sections). They refine but do not change any status at L; they are cited only as research
  records.
- Not read (as instructed): `pt/I1/`, `pt/I2/`, `pt/I4/`, `pt/D5/`, `pt/C5/` (names only, at the sweeps),
  `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`,
  `pt/audit/stage6-inputs/`, `pt/audit/reviews/`, `pt/audit/aborted-launches/`.

## §3 — What is not claimed

- No derivation and no verdict on (b_min) or on Q-EX-FULL: the records state what exists at L, at its recorded status.
  The "exposed facts" of §0 are statements about what the kernel contains, not about what follows from it.
- No status upgrade: every status is the one fixed by the record cited (kernel docstrings, round notes, `ROADMAP.md`,
  the seams audit, the PT stage records). "[D]" and "PT-record" are not L statuses and are marked so.
- No completeness claim beyond the censuses as defined: census (a) covers Prop-valued declarations and data structures of
  the 22 K modules and the eleven design modules; theorems are recorded where they carry a hypothesis structure of the
  pair setting, a bridge, a verdict or a status-fixing control (64 theorem and 5 lemma-folded records); the other 1000+
  K-module theorems enter only as lemmas of their round's verdict theorem. Census (b) is a vocabulary filter over the
  papers and the book; a K-programme statement worded outside the vocabulary would be missed.
- The quote control (`qcheck.out`, 308/308 fragments found) shows each quoted fragment occurs verbatim in the corpus; it
  does not check that each fragment comes from the cited line. Elisions are marked "…" and field breaks " · ".
- The observation that `ball3Drive`'s NOT fixes `z3` while `nflip` inverts it is a reading of the definitions
  (`rotFun`, `nflip`), not a kernel theorem.
- No statement about the scopes of threads I1, I2, I4 beyond naming them as the owners of out-of-scope items.

## §4 — Evidence log

Scripts (decision rule in each header before its first run; `python3 -I -B` from `pt/I3/`; stdout `.out`, stderr plus
`exit N` in `.err`; replays byte-identical in stdout and stderr, checked with `cmp`):

| script | purpose | runs | replay |
|---|---|---|---|
| `kcensus.py` | census (a): declaration counts, Prop-valued items | 1 (exit 0) | identical |
| `kcensus2.py` | census (a) supplement: data structures, untyped defs | 1 (exit 0) | identical |
| `kimports.py` | import graph of the kernel around the K modules | 1 (exit 0) | identical |
| `kdecls.py` | exact headers and docstrings of 162 named declarations | 1 (exit 0; 1 NOT FOUND, a list error: `body_isClosed` is in CompletionAction.lean:202) | identical |
| `mcensus.py` | censuses (b) and (c) | 1 (exit 0) | identical |
| `rcount.py` | record tally (§0 counts) | 3 (runs 1–2 kept as `.run1.*`, `.run2.*`; data edits between runs, script unchanged) | identical (twice) |
| `r0lists.py` | §0 bearing lists | 2 (run 1 exit 1, harness error, kept as `.run1.*`; one pre-run edit of the row filter) | identical (twice) |
| `qcheck.py` | quote control | 2 (run 1: 5 of 308 fragments not found, transcription fixed in `INVENTORY.md`; kept as `.run1.*`) | identical |

sha256 of every file in `pt/I3/` except this one (computed after the last write to each):

| file | sha256 |
|---|---|
| `.start_marker` | `221a52298ebcfbb7ba48ecc387a30146a0ff8f7a9a80fc924a0289e8bc1d0786` |
| `CENSUS.md` | `8b9f4670c109fc0ed303f2ae78288fc4c88e0cc72864fd7e7f45f4283ebdb1f7` |
| `END-CHECKS.txt` | `95a9ac83a227685c6bae098b50ac5bd6b712aa38302258da6855b3776901b3b6` |
| `INVENTORY.md` | `51eff9afef1f7ed25d82dc140a83dd97a9b24765d39b84cfdb636fa38ca96d7d` |
| `NOTES.md` | `6454e8dd42df15545e1d1f3d3052ad121f2d5343991b84b74899efd6f278a026` |
| `kcensus.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kcensus.out` | `3248f02567c3709c57bf27fbd517aa36f720f035e5ae60855f51f7d2052be06e` |
| `kcensus.py` | `b668b5f3465df75ae7556d33825208189725c329501ee5662a10ad2e0161638b` |
| `kcensus.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kcensus.replay.out` | `3248f02567c3709c57bf27fbd517aa36f720f035e5ae60855f51f7d2052be06e` |
| `kcensus2.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kcensus2.out` | `0c53fee220a5307e4b3c526f580f5544401529aeabd22120f938e8ffb5db4f5a` |
| `kcensus2.py` | `e0baf5fb75402cf7371de81256beec12f2530f47dc048b69c004eb8cc69639f0` |
| `kcensus2.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kcensus2.replay.out` | `0c53fee220a5307e4b3c526f580f5544401529aeabd22120f938e8ffb5db4f5a` |
| `kdecls.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kdecls.out` | `66271dbf0c75c6e5cbd15cf53db86fe72515f45ef980fdab0fe4e879365d1c61` |
| `kdecls.py` | `ff727ebed5191897d71fe63fb157dce31c3b215f682e3d8136b3ecc216913c7e` |
| `kdecls.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kdecls.replay.out` | `66271dbf0c75c6e5cbd15cf53db86fe72515f45ef980fdab0fe4e879365d1c61` |
| `kimports.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kimports.out` | `3284de2ca10be625b2a301fba9534ff9e996d3b72949d5b5831252620dfa9aaa` |
| `kimports.py` | `c89d4dde2c96d4a00ad2ab83d699289ee7987e33d43a6f876751ea666b2c0989` |
| `kimports.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `kimports.replay.out` | `3284de2ca10be625b2a301fba9534ff9e996d3b72949d5b5831252620dfa9aaa` |
| `mcensus.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `mcensus.out` | `3ae929788b2f7cae505aa6b139a795de24a8652a10228227dfd3d5b941cc4130` |
| `mcensus.py` | `0b62d224e25269d5455d75d069edae8b7de389161c7ac65a8b36a145e53cfb63` |
| `mcensus.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `mcensus.replay.out` | `3ae929788b2f7cae505aa6b139a795de24a8652a10228227dfd3d5b941cc4130` |
| `qcheck.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `qcheck.out` | `aae20862e94cb9bcbad11a184a844aaddb5c8a104221d6588729ad995a055266` |
| `qcheck.py` | `444cd35f274345175a8b5011ea29a87a62cad0e47c6884d4a7d43cdff28c2b1d` |
| `qcheck.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `qcheck.replay.out` | `aae20862e94cb9bcbad11a184a844aaddb5c8a104221d6588729ad995a055266` |
| `qcheck.run1.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `qcheck.run1.out` | `e9317fc21077c09eb54befcc85b9d382cd5032935f4fb5f6c80de2e22a3c75e5` |
| `r0lists.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `r0lists.out` | `be608dae38e080731a95f6bee1b61950603a082ea528cefcc8ed1a0eed55b084` |
| `r0lists.py` | `809c2afa86e2c93bbf35140632e3c5aaa0446b14807b8affb1280714400835f8` |
| `r0lists.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `r0lists.replay.out` | `be608dae38e080731a95f6bee1b61950603a082ea528cefcc8ed1a0eed55b084` |
| `r0lists.run1.err` | `daff1131a50990bc3b66a09fafa2232f9122bf88587f6671a46b5a19d8d9b5ee` |
| `r0lists.run1.out` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `rcount.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `rcount.out` | `a0964ad79de1e292135fe22b3f778dc031255719ec4cf7792775a73df139de6d` |
| `rcount.py` | `9e30d2a79ec274c87035d30430a2d811d0e9be19eda19091ba1334b7571a9ff9` |
| `rcount.replay.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `rcount.replay.out` | `a0964ad79de1e292135fe22b3f778dc031255719ec4cf7792775a73df139de6d` |
| `rcount.run1.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `rcount.run1.out` | `6b571472d7b775715fc0ca1112b0536a03293858d06e265306220cdc00872e99` |
| `rcount.run2.err` | `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320` |
| `rcount.run2.out` | `a60afb4100aff67bba2445dcaa8ba098b7ad214eb277e7380628ad92dc0e5423` |

## §5 — Integrity

- **Start** (`.start_marker`, written first into the newly created `pt/I3/`, which did not exist; UTC
  2026-10-10T16:52:12Z): the six manifests `inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4` verify (`sha256sum
  -c --quiet`, rc 0 each); `audit/stage3-inputs/ns.manifest.sha256` verifies from its own directory (`ns/NS-INPUT.md: OK`);
  `pt/base` HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`, `status --porcelain` empty, no `__pycache__`/`.pyc`; the ten
  protocol files match their prefixes (239dc123, b41aa0e7, 2a2f78f3, 38603692, 086a4cb8, 1a649168, d3da2811, 9e01f098,
  1f639115, b277b7c1) and every sidecar verifies (STAGE4, STAGE5, STAGE5-AMENDMENT-1, STAGE6 from the scratchpad root,
  the others from `pt/`); the `pt/` top-level listing with mtimes is recorded.
- **End** (`END-CHECKS.txt`, UTC 2026-10-10T17:24:59Z, repeated at 17:26:57Z before hashing): the same checks, all green;
  no bytecode under `pt/base` or `pt/I3`. **Sweep:** the only path under `pt/` newer than `.start_marker` outside
  `pt/I1/`, `pt/I2/`, `pt/I3/`, `pt/I4/`, `pt/D5/`, `pt/C5/`, `pt/audit/`, `pt/audit*-replay/` is `.` (the `pt/` directory
  entry itself, whose mtime changed when the sibling I4 created its directory at 17:24:24Z); the top-level names added
  since the start are `./I4` only. **No anomaly; nothing quarantined** (no `evidence/` directory was needed).
- **Writes.** Every file I wrote is in `pt/I3/` (listed in §4), with one exception, recorded: a temporary hash list
  redirected to `scratchpad/I3-hashes.tmp` (one level above `pt/`, sha256 `67da50b4…`, my own output, 53 hash lines of
  `pt/I3` files), deleted at once; no effect on any content under `pt/` (NOTES 17:27Z). Edits to my own files were made
  by appending (each write ≤ 250 lines) or by exact string replacements printed with their match counts (NOTES).
- **Reads and holds.** Read-only on `pt/base/` and on every PT record; git used only for `rev-parse` and `status
  --porcelain` with `GIT_OPTIONAL_LOCKS=0`. No sibling directory was read (names only at the sweeps). No branch, commit,
  PR, CI, network or URL fetch, publication or sub-agent.
