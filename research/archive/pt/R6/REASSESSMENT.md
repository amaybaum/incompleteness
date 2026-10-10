# R6 — reassessment of the stage-4/5 countermodels against every applicable item at L (Q-EX-FULL, step 3)

Thread R6, research only, read-only on the corpus. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`).
Governing texts: `pt/PROTOCOL-STAGE6.md` (`b277b7c1…`, step 3) and `pt/PROTOCOL-STAGE6-AMENDMENT-1.md` (`59019538…`,
A1.5), with the protocols they name; AUDIT-I §4–§5 binding. Inputs: the frozen inventories `pt/I1/`–`pt/I4/`, the
audited stage-3/4/5 records, the kernel and manuscripts at L. No status is upgraded, no verdict on (b) is given (that
is step 4), and no do-not-assume item is assumed true.

**Evidence levels.** [K] certified at L (file:line; CD = CompositeDimension.lean, KIF = KInfFoundations.lean, OG =
OrbitGeneration.lean, ON = OrbitNormalization.lean); [D] design module (`pt/inputs/fourcopy/`, not at L); [W] written
argument; [X] exact computation in `pt/R6/` (script and check id: `r2` = `r2_cones.py`, `r3` = `r3_seeds.py`, `r5` =
`r5_realization.py`, `r6` = `r6_single.py`); [A] audited stage record cited, not recomputed here; [L] unverified
literature (only inside cited [A] rows).

**Verdicts.** SATISFIES — the item applies to the alternative and the alternative meets it, tagged `[K-indep]` (a
proved statement or definition about objects every pair cone on `W 3` shares — the carrier, `cnot`, `nflip`,
`eball 3` — so it holds for the alternative because it holds at L), `[cone]` (the item's clause on `K` checked on the
alternative), `[K]` (a kernel theorem quantifying over `K` whose conclusion the alternative meets), `[inherit]` (a
single-token premise, met by the alternative's tokens exactly as by `Q3`'s), or `(vacuous)` (an implication whose
hypothesis the alternative fails). FAILS `[hyp]` — the alternative violates the item; every such item is a
do-not-assume item, a [D] design-module hypothesis or a PT-record candidate, so the failure is the failure of a
hypothesis, never of a theorem at L. NOT REACHED — the item is at level H, M, G or X, or needs a structure L does not
have (three or more tokens) or a bridge L does not have; no bridge at L carries it to a cone in `W 3`. UNDECIDED —
used once (node T on the existence-only alternatives), where neither SATISFIES nor FAILS is established.

**Method.** `r1_inventory.py` parses the four inventories and fixes the 199 applicable items: I3's 142 records with
bearing other than "none at L" (80 direct, 25 inherited single-token, 20 single-token not read by a pair statement,
17 through a named bridge — the class sets equal I3's own `r0lists.out`), I4.236 (I4's one non-none bearing), I1.17
(I1's formal value "only through <bridge>" with bridge none), the 44 do-not-assume records of I4 and the 11 of I2.
`r2_cones.py` checks the explicit cones exactly (57 checks), `r3_seeds.py` the existence seeds (30 checks),
`r5_realization.py` scans L for any statement attaching an embedded-observer realization to a pair-cone object,
`r6_single.py` checks the single-token premises (12 checks), and `r4_tables.py` assigns every item its class (data in
the script; class rules fixed in NOTES N3 before any run) and prints the tables below with seven controls (every item
classed; `Q3` fails nothing; every cited witness present; FCC failure present; bearing counts; seed lines; inputs
green). All six final scripts replay byte-identically. Kept failed runs: `r1` runs 1–2, `r2` runs 1–2, `r3` run 1
(each a harness error caught by its own controls; NOTES N4–N6).

## 1. The alternatives

| id | alternative | definition (exact) | level | record |
|---|---|---|---|---|
| A1 | `K(E0)` | `(Q3 ∩ E0*) + ℝ₊E0`, `E0 = E00 + E13 − E22` | (i) | stage 3 X `K1` / U `K★` (AUDIT-X) |
| A2 | `K(Z_F)` | `(Q3 ∩ Z_F*) + cone Z_F`, `z_s = (E00 + s1E13 + s2E22 − s1s2E31)/4` | (ii) | stage 3 X `K4` / U `K_F`; stage 4 Z z1 |
| A3a | Y4 seed | cap defect `(I − cφ0φ0†)/8`, `c = 4609/4608`, `φ0 = (1,2,3i,−1+i)` | (ii) | stage 4 Y4 (S3 = actC Rx with G16; the native drive) |
| A3b | Y5 seed | `c = 517/512`, `d_min = 5/256` | (ii) | stage 4 Y5 (S1, S2's reachable set, finite extensions) |
| A3c | Z seed | `(7/8)E00 − T_ψa/4`, `ψa = (15,−1,7,7)/18` | (ii) | stage 4 Z z3 (S3) |
| A4a | C5 census seeds | `αE00 − T_ψ/4`, `ψ = φ0/4`: `d_low = 1/2304` (`α = 499783/500000`), `5/256` (`α = 122509/125000`), `1/8704` (`c = 17409/17408`) | (ii) | stage 5 C5 census |
| A4b | κ Bell seed | `F = z_(−1,−1)` on the invariant circles `C1 ∪ C2` | (ii) | stage 5 C5 KAPPA; = stage 4 S2's Bell seeds |
| A4c | D5 monomial seed | `c = 513/512` at `(1,2,3,4)/√30` | (ii) | stage 5 D5 γ (substratum class) |
| A5 | torus and finite-group nodes | S2 (Bell seeds on `C1 ∪ C2`); `Stab_Cl(Z_F)` subgroups (explicit: A2); `G_S` (Bell seed, orbit 8); `G_H` (`α = 9/10`); `G_Cl` (`α = 99/100`); every finite group (dimension corollary) | (ii) | stage 4 Z z1–z4, Y5 |

A1 and A2 are explicit cones (EXOTIC-X). A3–A5, apart from the stabilizer subgroups served by A2, are existence
alternatives (EXOTIC-E): a closed, self-dual cone `K ⊇ cone(Ĝ·SEP ∪ Ĝ·e)` invariant under the node's compact group
`Ĝ ∋ cnot`, given by EBF [A, AUDIT-X] over the exactly checked seed `e`; their rows coincide item by item and are given
in one table (A3) with the alternative-specific rows in Table A3-seeds. `K({F, cnot F})` and `K(e_c)` are named in
`PROTOCOL-STAGE6.md` step 3 but not in A1.5; they are not reassessed here.

## 2. How to read the tables

Each table lists the 199 applicable items in id order with the verdict for that alternative and the evidence. The
`class` column names the rule applied (NOTES N3): `def`, `thm`, `gate` (K-independent statements and the certified
gate instance), `cone` (clauses on `K`), `kthm` (`no_candidateCone_cnot_reflY`), `dna` (do-not-assume items), `d4f` /
`d4v` / `d4s` (four-token [D] items: failed hypothesis, vacuous theorem, satisfied parity), `nr` (not reached:
three-or-more-token content or an absent bridge), `inh` / `b1` (single-token premises, directly or through the
bridges B1/B2, which fix only the upper bound `maxCone (eball 3)`), `cand` (the PT-record candidates H and T), `hmg`
(levels H, M, G, X). The `Q3` comparison column of `r4_tables.out` (not repeated below) has SATISFIES on every row
except the 68 NOT REACHED rows, and no FAILS.

Tally per alternative (`r4_tables.out`): A1 and A2 — 118 SATISFIES, 13 FAILS, 68 NOT REACHED; EXOTIC-E — 118
SATISFIES, 12 FAILS, 1 UNDECIDED (T), 68 NOT REACHED. EXCLUDED-BY-L: none.

## 3. The tables
### Table A1 — K(E0) = (Q3 ∩ E0*) + R+E0, level (i)

| item | statement (one line) | class | verdict | evidence |
|---|---|---|---|---|
| I3.1 | `W d` | def | SATISFIES [K-indep] | [K] CD:95-97; LT is encoded by the carrier (as for Q3) |
| I3.2 | `prodState` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.3 | `maxCone` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.4 | `jointStates` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.5 | `IsProduct` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.6 | `actT` — invariance of K under a rotation: rows I3.150-153 | def | SATISFIES [K-indep] | [K] CD:197-202; [X] r2 D0c |
| I3.7 | `actC` — invariance of K under a rotation: rows I3.150-153 | def | SATISFIES [K-indep] | [K] CD:197-202; [X] r2 D0c |
| I3.8 | `IsNot` | inh | SATISFIES [inherit] | [K] isNot_nflip CD:838; [X] r2 D1e, r6 T3 |
| I3.9 | `NativeGate` | gate | SATISFIES [K-indep] | [K] nativeGate_cnot CD:1159; [X] r2 D1b, D1d, D1g |
| I3.10 | `Entangling` | gate | SATISFIES [K-indep] | [K] entangling_cnot CD:1378; [X] r2 D1f |
| I3.11 | `cnot`, `sgn`, `pc`, `pt`, `z3`, `nflip`, `xplus`, `phiW` (the … | def | SATISFIES [K-indep] | [K] CD:741-798; [X] r2 D0a (cnot = Ad(CNOT), control first) |
| I3.12 | `isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC` | thm | SATISFIES [K-indep] | [K] CD:838-860; [X] r2 D1b, D1d, D1e |
| I3.13 | `nativeGate_cnot` | thm | SATISFIES [K-indep] | [K] CD:1159; [X] r2 D1g |
| I3.14 | `entangling_cnot` | thm | SATISFIES [K-indep] | [K] CD:1378; [X] r2 D1f |
| I3.15 | parity: `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGat… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.16 | `blockData_of_nativeGate` (with `BlockData`) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.17 | `not_entangling_one` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.18 | `dim_of_nativeGate` (the selector) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.19 | `three_of_nativeGate` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.20 | DIM-1 controls: `nativeGate_cnot1`, `not_entangling_cnot1`, `no… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.21 | `dim1_core` (DIM-1 verdict) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.22 | `not_even_of_gateRel` (with `finrank_plus_eq_finrank_minus_rel`) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.23 | `GateRel` | gate | SATISFIES [K-indep] | [K] gateRel_cnot (ParityNot); [X] r2 D1b |
| I3.24 | `piRotation_three` (with `tangentPlus_three`, `det_three`) | inh | SATISFIES [inherit] | [K] ParityNot:161; [X] r6 T3 (nflip = pi-rotation about e1) |
| I3.25 | `not_gateRel_refl3`, `not_gateRel_negId3` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.26 | `not_posFwd_gJ3`, `not_posFwd_gJ5` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.27 | `exists_frame_gateRel_iff_odd` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.28 | `not_posFwd_gRev` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.29 | `CtrlGate` | gate | SATISFIES [K-indep] | [K] ctrlGate_of_nativeGate RelcSelectBlock:53 |
| I3.30 | `not_even_of_relC` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.31 | `dim_of_ctrlGate`, `three_of_ctrlGate` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.32 | `ctrlGate_of_nativeGate` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.33 | `gSq_sep`, `gSqInv_sep` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.34 | `relT_not_dimension_selecting` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.35 | `NativeGateOf` | gate | SATISFIES [K-indep] | [W] from nativeGate_cnot: maxCone ⊆ maxConeOf avail for every effect-sound avail |
| I3.36 | `EntanglingOf` | gate | SATISFIES [K-indep] | [W] = Entangling once maxConeOf avail = maxCone (B1); [K] entangling_cnot |
| I3.37 | `dim_of_nativeGateOf` | inh | SATISFIES [inherit] | [K] K1Bridge:128, :138 (through B1) |
| I3.38 | `three_of_nativeGateOf` | inh | SATISFIES [inherit] | [K] K1Bridge:128, :138 (through B1) |
| I3.39 | `HasTwoSharpTests` | inh | SATISFIES [inherit] | [K] hasTwoSharpTests_iff SharpTests:155; [X] r6 T1 |
| I3.40 | `hasTwoSharpTests_iff` | inh | SATISFIES [inherit] | [K] hasTwoSharpTests_iff SharpTests:155; [X] r6 T1 |
| I3.41 | `two_le_not_implied` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.42 | `prodState_mem_maxCone` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.43 | `CandidateCone` | cone | SATISFIES [cone] | [X] r2 C1 (H1), C5 (maxCone bound) |
| I3.44 | `no_candidateCone_cnot_reflY` | kthm | SATISFIES [K] | [K] K2Guard:143; [X] r2 C7 (actT reflY moves the cone) |
| I3.45 | `three_of_nativeGate_of_two_le` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.46 | `two_le_of_entangling` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.47 | `three_of_nativeGateOf_of_two_le` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.48 | `EffectsOn` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.49 | `maxConeOf` | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.50 | `MixingClosed` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.51 | `maxConeOf_avail_eq` (with `sharpFamily_subset_avail`, `maxCone… | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.52 | `fullEffects_subset_avail` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.53 | `not_fullEffects_of_orbit` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.54 | `DenseBoundaryOrbit` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.55 | `denseBoundaryOrbit_of_boundaryTransitive` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.56 | `maxConeOf_avail_eq_of_dense` (with the dense ball and selector… | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.57 | `FiniteStage` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.58 | `IsEffectOn` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.60 | `IsBoundaryState` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.69 | `CopyNatural` (K∞-Copy) | inh | SATISFIES [inherit] | [X] r6 T5; K∞-Copy open for Q3 likewise (one N built into NativeGate) |
| I3.73 | `SharpSeed` (K∞-Seed, P1) | b1 | SATISFIES [inherit] | [K] B1; [X] r6 T2 (sharp seed on the ball); K ⊆ maxCone [X] r2 C5 |
| I3.74 | `PreservesBody` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.75 | `SeedOrbitAvailable` (K∞-V4, V4′) | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.76 | `BoundaryTransitive` (K∞-Trans; "K∞-R" in OG-1's record) | inh | SATISFIES [inherit] | [K] boundaryTransitive_fullAut3 OG:537, _ball3Drive ON:665; [X] r6 T6 |
| I3.78 | `preservesBody_drive` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.79 | `seedOrbit_ball3_eq` (the reduced orbit-generation theorem) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.80 | `boundaryTransitive_fullAut3` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.82 | `orbit_generation_core` (OG-1 verdict) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.83 | `boundaryTransitive_ball3Drive` (with `driveWords3`) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.87 | `TransBody` (TRANS) | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.88 | `eq_qBall_of_boundaryTransitive` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.89 | `exists_affine_image_eq_eball` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.92 | `DirectedStages` (with `StageMap`) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.94 | `SCInf` (SC∞, K∞-Stage) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.95 | `BinaryVisible` (ELEM-bin) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.96 | `FiniteRank` (K∞-Stage) | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.97 | `sharpSeed_completion` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.98 | `exists_chart_of_finiteRank` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.99 | `OpDatum` (K∞-Act) | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.101 | `AffineRespect` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.104 | `body_isClosed` | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.105 | `preservesBody_inducedEquiv` | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.111 | `finiteOrderOn_of_stagePreserving` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.113 | `ProductData` | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.114 | `PreComposite` | cone | SATISFIES [cone] | [W] over [X] r2 C1, C5, C6 (slice convex, compact, products inside, effects valid, unit pairing) |
| I3.115 | `LocallyTomographic` | def | SATISFIES [K-indep] | [K] CompositeInterface §E: LT is a theorem of the coordinate model W 3 |
| I3.116 | `Composite` | cone | SATISFIES [cone] | [W] over [X] r2 C1, C5, C6 (slice convex, compact, products inside, effects valid, unit pairing) |
| I3.118 | `JointReversible` | cone | SATISFIES [cone] | [X] r2 C2, C6, D1a (cnot preserves the body, involutive) |
| I3.120 | `condA_prodState` (L9, no signalling on products) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.121 | `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPr… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.122 | `comp1_core` (COMP-1 verdict) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.124 | the effect cone of the ball: `lor_ehom`, `isEffectOn_affOf`, `l… | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.125 | `NativeGateBall.parity` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.126 | `p_le_one`, `dim_of_bounds` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.127 | `lorentz_of_effects` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.128 | `nb1_kernel_core` (NB-1 verdict) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.129 | `hcls` — N-CLASS gates (`NClass`) | gate | SATISFIES [K-indep] | [D] NClass: cnot with identity locals (KT4-PREM-1 record, M_Q) |
| I3.130 | `hadm` — pair admissibility (`PairAdm`, with `IsConvexCone`) | cone | SATISFIES [cone] | [X] r2 C1, C5; convex cone by construction |
| I3.131 | `hcl` — closedness of each pair cone | cone | SATISFIES [cone] | [A] SD1/SD2 closedness (AUDIT-X); [W] a self-dual cone is closed |
| I3.132 | `hgate` — gate preservation (H2 of stage 3 is this clause for `… | cone | SATISFIES [cone] | [X] r2 C2 (level (i) for K(E0); level (ii) for K(Z_F)) |
| I3.133 | `H` — the four-copy core (`KT4Core`, with `KT4`, `KT4LT`) | d4f | FAILS [hyp] | [D] Lemma B1 (FourCopyBridge:267) + [X] r2 C9 (FCC fails, uniform) |
| I3.134 | token clauses `tokA`, `tokB` (`TokenCoherent`) — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.135 | FCC — the cone-level four-copy interface (`FourCopyCoherent`, `… | d4f | FAILS [hyp] | [X] r2 C9 (uniform: min -1 for K(E0), -1/2 for K(Z_F)) |
| I3.136 | `PairLinked` (Lemma R's interface form) — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.137 | IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | dna | FAILS [hyp] | [X] r2 C8 (rotation witnesses) |
| I3.138 | `EvenCycle` (with `EvenCycle4`) | d4s | SATISFIES | [W] cnot with identity locals: every twist bit false |
| I3.139 | `kt4_forward_ie1` (Theorem A′, the audited theorem) | d4v | SATISFIES (vacuous) | [D] (vacuous: hypothesis H fails, I3.133) |
| I3.140 | `fourCopyCoherent_of_kt4Core` (Lemma B1) | d4v | SATISFIES (vacuous) | [D] (vacuous: hypothesis H fails, I3.133) |
| I3.141 | `KT4Cone` — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.142 | `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the … | dna | FAILS [hyp] | [X] r2 C8 (rot3 pi: K(E0); cyc3: K(Z_F)) |
| I3.143 | `ipW`, `dualW` (the Euclidean pairing and dual cone of tables) | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.144 | `Q3`, `twin`, `pauliW`, `twistQ3` | dna | FAILS [hyp] | [X] r2 C4 (a pure state outside K); r2 CC twin (K ≠ twin) |
| I3.145 | P-STAGE2 (named premise of KT4-PREM-1) | nr | NOT REACHED | absent bridge A3 (P-STAGE2 not at L); its cone consequence hcl: I3.131 |
| I3.146 | P-ACT2 (named premise of KT4-PREM-1) | nr | NOT REACHED | absent bridge A4 (P-ACT2 not at L); cone consequence hgate: I3.132; idle-extension reading: I3.137 |
| I3.147 | H1 — products in `K` | cone | SATISFIES [cone] | [X] r2 C1 (symbolic SOS, whole ball) |
| I3.148 | H2 — `cnot`-invariance (level (i)); `G16`-invariance (level (ii… | cone | SATISFIES [cone] | [X] r2 C2 (level (i) for K(E0); level (ii) for K(Z_F)) |
| I3.149 | H3 — trace self-duality `K = dualW K` | cone | SATISFIES [cone] | [X] r2 C3 certificates + [A] SD1/SD2 (AUDIT-X) |
| I3.150 | (b_S4) — the full rotation group of one token acts on the pair … | dna | FAILS [hyp] | [X] r2 C8 actC rot3(pi) (K(E0)), actC cyc3 (K(Z_F)) |
| I3.151 | (b_n) — one rotation subgroup of one token about an off-frame a… | dna | FAILS [hyp] | [X] r2 C8 actC R_n(pi/2), n = (3,0,4)/5 |
| I3.152 | (b_R1) — one order-3 rotation of one token about (5,1,1) | dna | FAILS [hyp] | [X] r2 C8 actC R1 (-1; -2383/5316) |
| I3.153 | (b_DJ) — the native drive with the native `J` acting on one tok… | dna | FAILS [hyp] | [X] r2 C8 actC/actT nflip (flow members; K(E0)), actC cyc3 and actC Rx(pi/2) (K(Z_F)) |
| I3.154 | IE2 — idle extension of the pair interaction groups — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.155 | frame covariance (FC) of the native gate | dna | FAILS [hyp] | [W] FC ⟺ IE1 given hgate (stage 2 [A]); hgate holds (r2 C2), IE1 fails |
| I3.156 | INV2 — the native gate is an operational involution on the pair… | cone | SATISFIES [cone] | [X] r2 C2, C6, D1a (cnot preserves the body, involutive) |
| I3.157 | SDC = P3 ∧ OVL4 ∧ CSD2 — self-duality under composition — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.158 | N0 ∧ N1 ∧ N2 — regrouping invariance of a four-token composite … — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.159 | S2 Pair — a compact, gate-reversible COMP-1 pre-composite (stag… | cone | SATISFIES [cone] | [W] over [X] r2 C1, C5, C6 (slice convex, compact, products inside, effects valid, unit pairing) |
| I3.160 | H — pair-level homogeneity of `K` | cand | FAILS [hyp] | [A] stage 3 [W + L] (surgery cones not homogeneous); stage 4 Y6 |
| I3.161 | T — pair-level reversible richness (transitivity on extreme ray… | cand | FAILS [hyp] | [A] stage 4 Y6 (extreme-ray invariant c = 15 on defects, 9 on products) |
| I3.164 | K1 — the dimension | inh | SATISFIES [inherit] | [K] dim1_core instance; K1 CONDITIONAL for Q3 likewise |
| I3.165 | K2 — the composite — other K2 clauses: LT encoded, cone exists | dna | FAILS [hyp] | [X] r2 C8 (its clause "local actions compatible with the composite cone") |
| I3.166 | K∞ — the field-neutral premises | inh | SATISFIES [inherit] | K∞ OPEN for Q3 likewise (pair-blind) |
| I3.167 | K∞-Stage | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.168 | K∞-Act | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.169 | K∞-Drive | inh | SATISFIES [inherit] | [K] ball3Drive KIF:449; [X] r6 T4; operational availability open for Q3 likewise |
| I3.170 | K∞-Trans | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.171 | K∞-Seed | b1 | SATISFIES [inherit] | [K] B1; [X] r6 T2 (sharp seed on the ball); K ⊆ maxCone [X] r2 C5 |
| I3.172 | K∞-V4 | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.173 | K∞-Copy | inh | SATISFIES [inherit] | [X] r6 T5; K∞-Copy open for Q3 likewise (one N built into NativeGate) |
| I3.185 | carrier-map identities for every one-copy linear map: `actT_pro… | thm | SATISFIES [K-indep] | [K] CD:1923-1931, K2Guard:172 (products only) |
| I3.186 | `eball_three` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.187 | the classification step of KT4-PREM-1: `hcls ∧ hadm ∧ hgate ∧ I… | d4v | SATISFIES (vacuous) | [W] KT4-PREM-1 result.md:128 (vacuous: IE1 fails, I3.137) |
| I4.236 | Kₙ census §4 — scope of K∞'s geometric branch | inh | SATISFIES [inherit] | [A] kn census §4; [X] r2 C10: the pair reading of SF fails for Q3 and the cones alike |
| I1.17 | layered theorem statement (Main.md:82) | hmg | NOT REACHED | I1 bridge field: none at L (Main.md:82) |
| I4.3 | HasParallelReferenceExtension | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.4 | HasQutritReferenceExtension | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.14 | InertSpectatorCompositionality | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.29 | ContextStable | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.31 | ImplementationLocality | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.42 | OIPlusLocal | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.45 | StructurallyClosed | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.56 | LayerFlowExecutable | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.65 | PhysicalCompletionConditions | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.66 | CompositeOperationalValidity | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.67 | HasCompositeUnitaryControl | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.68 | IteratedAncillaClosure | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.69 | SystemToLevelOne | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.70 | ExactAllFiniteEndomorphicQuantumOps | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.73 | WellFormed | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.74 | SubstantiveCompletion | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.80 | CompletedOI | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.82 | ObservationalIndependence | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.85 | ReversibleRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.87 | ObserverRecursion | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.88 | OIPlus | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.96 | ObservationalIndependence | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.99 | ReversibleRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.102 | OIPlus | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.110 | EmbeddedObservation | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.115 | OIPlusEmbedded | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.118 | PhaseFreeRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.120 | OIPlusMin | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.123 | CyclicRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.124 | OIPlusPos | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.127 | InverseAccessibility | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.128 | LieRankRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.133 | ReversibleImplementationLocality | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.137 | OIPlusMicro | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.143 | DrivesElementary | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.144 | QuantumArchitecture | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.179 | PairFlowSourced | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.187 | ShadowQuantum | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.210 | psd_iff_trace_nonneg | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.215 | psd_trace_mul_nonneg | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.216 | accessible_cone_full | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.241 | DerivedOI | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.244 | ElementaryTransitionRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.245 | OIPlusElem | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.3 | The operational-extension boundary | hmg | NOT REACHED | level G (operational co…; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.29 | The operational-completion characterization (manuscript stateme… | hmg | NOT REACHED | level G (every nonempty…; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.30 | Bare finite OI does not imply QM; OI-compatible theory plus (i)… | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.31 | Quantum-complete OI (OI⁺): observational independence, reversib… | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.32 | Primitive-source form: implementation locality, phase-free rich… | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.33 | Substratum-source form | hmg | NOT REACHED | level G/H; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.34 | Layer-flow form | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.35 | Typed form | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.62 | Comparison of routes and dependency scope: in-house, imported, … | hmg | NOT REACHED | level M/G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.63 | Operational-reconstruction route: target conditions and the out… | hmg | NOT REACHED | level G/O; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.69 | The claim structure: the four layers, the four-part theorem sta… | hmg | NOT REACHED | level H/M/G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |

### Table A2 — K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F, level (ii) (also the explicit cone of every subgroup of Stab_Cl(Z_F))

| item | statement (one line) | class | verdict | evidence |
|---|---|---|---|---|
| I3.1 | `W d` | def | SATISFIES [K-indep] | [K] CD:95-97; LT is encoded by the carrier (as for Q3) |
| I3.2 | `prodState` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.3 | `maxCone` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.4 | `jointStates` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.5 | `IsProduct` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.6 | `actT` — invariance of K under a rotation: rows I3.150-153 | def | SATISFIES [K-indep] | [K] CD:197-202; [X] r2 D0c |
| I3.7 | `actC` — invariance of K under a rotation: rows I3.150-153 | def | SATISFIES [K-indep] | [K] CD:197-202; [X] r2 D0c |
| I3.8 | `IsNot` | inh | SATISFIES [inherit] | [K] isNot_nflip CD:838; [X] r2 D1e, r6 T3 |
| I3.9 | `NativeGate` | gate | SATISFIES [K-indep] | [K] nativeGate_cnot CD:1159; [X] r2 D1b, D1d, D1g |
| I3.10 | `Entangling` | gate | SATISFIES [K-indep] | [K] entangling_cnot CD:1378; [X] r2 D1f |
| I3.11 | `cnot`, `sgn`, `pc`, `pt`, `z3`, `nflip`, `xplus`, `phiW` (the … | def | SATISFIES [K-indep] | [K] CD:741-798; [X] r2 D0a (cnot = Ad(CNOT), control first) |
| I3.12 | `isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC` | thm | SATISFIES [K-indep] | [K] CD:838-860; [X] r2 D1b, D1d, D1e |
| I3.13 | `nativeGate_cnot` | thm | SATISFIES [K-indep] | [K] CD:1159; [X] r2 D1g |
| I3.14 | `entangling_cnot` | thm | SATISFIES [K-indep] | [K] CD:1378; [X] r2 D1f |
| I3.15 | parity: `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGat… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.16 | `blockData_of_nativeGate` (with `BlockData`) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.17 | `not_entangling_one` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.18 | `dim_of_nativeGate` (the selector) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.19 | `three_of_nativeGate` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.20 | DIM-1 controls: `nativeGate_cnot1`, `not_entangling_cnot1`, `no… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.21 | `dim1_core` (DIM-1 verdict) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.22 | `not_even_of_gateRel` (with `finrank_plus_eq_finrank_minus_rel`) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.23 | `GateRel` | gate | SATISFIES [K-indep] | [K] gateRel_cnot (ParityNot); [X] r2 D1b |
| I3.24 | `piRotation_three` (with `tangentPlus_three`, `det_three`) | inh | SATISFIES [inherit] | [K] ParityNot:161; [X] r6 T3 (nflip = pi-rotation about e1) |
| I3.25 | `not_gateRel_refl3`, `not_gateRel_negId3` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.26 | `not_posFwd_gJ3`, `not_posFwd_gJ5` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.27 | `exists_frame_gateRel_iff_odd` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.28 | `not_posFwd_gRev` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.29 | `CtrlGate` | gate | SATISFIES [K-indep] | [K] ctrlGate_of_nativeGate RelcSelectBlock:53 |
| I3.30 | `not_even_of_relC` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.31 | `dim_of_ctrlGate`, `three_of_ctrlGate` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.32 | `ctrlGate_of_nativeGate` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.33 | `gSq_sep`, `gSqInv_sep` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.34 | `relT_not_dimension_selecting` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.35 | `NativeGateOf` | gate | SATISFIES [K-indep] | [W] from nativeGate_cnot: maxCone ⊆ maxConeOf avail for every effect-sound avail |
| I3.36 | `EntanglingOf` | gate | SATISFIES [K-indep] | [W] = Entangling once maxConeOf avail = maxCone (B1); [K] entangling_cnot |
| I3.37 | `dim_of_nativeGateOf` | inh | SATISFIES [inherit] | [K] K1Bridge:128, :138 (through B1) |
| I3.38 | `three_of_nativeGateOf` | inh | SATISFIES [inherit] | [K] K1Bridge:128, :138 (through B1) |
| I3.39 | `HasTwoSharpTests` | inh | SATISFIES [inherit] | [K] hasTwoSharpTests_iff SharpTests:155; [X] r6 T1 |
| I3.40 | `hasTwoSharpTests_iff` | inh | SATISFIES [inherit] | [K] hasTwoSharpTests_iff SharpTests:155; [X] r6 T1 |
| I3.41 | `two_le_not_implied` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.42 | `prodState_mem_maxCone` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.43 | `CandidateCone` | cone | SATISFIES [cone] | [X] r2 C1 (H1), C5 (maxCone bound) |
| I3.44 | `no_candidateCone_cnot_reflY` | kthm | SATISFIES [K] | [K] K2Guard:143; [X] r2 C7 (actT reflY moves the cone) |
| I3.45 | `three_of_nativeGate_of_two_le` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.46 | `two_le_of_entangling` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.47 | `three_of_nativeGateOf_of_two_le` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.48 | `EffectsOn` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.49 | `maxConeOf` | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.50 | `MixingClosed` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.51 | `maxConeOf_avail_eq` (with `sharpFamily_subset_avail`, `maxCone… | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.52 | `fullEffects_subset_avail` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.53 | `not_fullEffects_of_orbit` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.54 | `DenseBoundaryOrbit` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.55 | `denseBoundaryOrbit_of_boundaryTransitive` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.56 | `maxConeOf_avail_eq_of_dense` (with the dense ball and selector… | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.57 | `FiniteStage` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.58 | `IsEffectOn` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.60 | `IsBoundaryState` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.69 | `CopyNatural` (K∞-Copy) | inh | SATISFIES [inherit] | [X] r6 T5; K∞-Copy open for Q3 likewise (one N built into NativeGate) |
| I3.73 | `SharpSeed` (K∞-Seed, P1) | b1 | SATISFIES [inherit] | [K] B1; [X] r6 T2 (sharp seed on the ball); K ⊆ maxCone [X] r2 C5 |
| I3.74 | `PreservesBody` | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.75 | `SeedOrbitAvailable` (K∞-V4, V4′) | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.76 | `BoundaryTransitive` (K∞-Trans; "K∞-R" in OG-1's record) | inh | SATISFIES [inherit] | [K] boundaryTransitive_fullAut3 OG:537, _ball3Drive ON:665; [X] r6 T6 |
| I3.78 | `preservesBody_drive` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.79 | `seedOrbit_ball3_eq` (the reduced orbit-generation theorem) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.80 | `boundaryTransitive_fullAut3` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.82 | `orbit_generation_core` (OG-1 verdict) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.83 | `boundaryTransitive_ball3Drive` (with `driveWords3`) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.87 | `TransBody` (TRANS) | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.88 | `eq_qBall_of_boundaryTransitive` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.89 | `exists_affine_image_eq_eball` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.92 | `DirectedStages` (with `StageMap`) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.94 | `SCInf` (SC∞, K∞-Stage) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.95 | `BinaryVisible` (ELEM-bin) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.96 | `FiniteRank` (K∞-Stage) | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.97 | `sharpSeed_completion` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.98 | `exists_chart_of_finiteRank` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.99 | `OpDatum` (K∞-Act) | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.101 | `AffineRespect` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.104 | `body_isClosed` | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.105 | `preservesBody_inducedEquiv` | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.111 | `finiteOrderOn_of_stagePreserving` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.113 | `ProductData` | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.114 | `PreComposite` | cone | SATISFIES [cone] | [W] over [X] r2 C1, C5, C6 (slice convex, compact, products inside, effects valid, unit pairing) |
| I3.115 | `LocallyTomographic` | def | SATISFIES [K-indep] | [K] CompositeInterface §E: LT is a theorem of the coordinate model W 3 |
| I3.116 | `Composite` | cone | SATISFIES [cone] | [W] over [X] r2 C1, C5, C6 (slice convex, compact, products inside, effects valid, unit pairing) |
| I3.118 | `JointReversible` | cone | SATISFIES [cone] | [X] r2 C2, C6, D1a (cnot preserves the body, involutive) |
| I3.120 | `condA_prodState` (L9, no signalling on products) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.121 | `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPr… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.122 | `comp1_core` (COMP-1 verdict) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.124 | the effect cone of the ball: `lor_ehom`, `isEffectOn_affOf`, `l… | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.125 | `NativeGateBall.parity` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.126 | `p_le_one`, `dim_of_bounds` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.127 | `lorentz_of_effects` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.128 | `nb1_kernel_core` (NB-1 verdict) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.129 | `hcls` — N-CLASS gates (`NClass`) | gate | SATISFIES [K-indep] | [D] NClass: cnot with identity locals (KT4-PREM-1 record, M_Q) |
| I3.130 | `hadm` — pair admissibility (`PairAdm`, with `IsConvexCone`) | cone | SATISFIES [cone] | [X] r2 C1, C5; convex cone by construction |
| I3.131 | `hcl` — closedness of each pair cone | cone | SATISFIES [cone] | [A] SD1/SD2 closedness (AUDIT-X); [W] a self-dual cone is closed |
| I3.132 | `hgate` — gate preservation (H2 of stage 3 is this clause for `… | cone | SATISFIES [cone] | [X] r2 C2 (level (i) for K(E0); level (ii) for K(Z_F)) |
| I3.133 | `H` — the four-copy core (`KT4Core`, with `KT4`, `KT4LT`) | d4f | FAILS [hyp] | [D] Lemma B1 (FourCopyBridge:267) + [X] r2 C9 (FCC fails, uniform) |
| I3.134 | token clauses `tokA`, `tokB` (`TokenCoherent`) — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.135 | FCC — the cone-level four-copy interface (`FourCopyCoherent`, `… | d4f | FAILS [hyp] | [X] r2 C9 (uniform: min -1 for K(E0), -1/2 for K(Z_F)) |
| I3.136 | `PairLinked` (Lemma R's interface form) — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.137 | IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | dna | FAILS [hyp] | [X] r2 C8 (rotation witnesses) |
| I3.138 | `EvenCycle` (with `EvenCycle4`) | d4s | SATISFIES | [W] cnot with identity locals: every twist bit false |
| I3.139 | `kt4_forward_ie1` (Theorem A′, the audited theorem) | d4v | SATISFIES (vacuous) | [D] (vacuous: hypothesis H fails, I3.133) |
| I3.140 | `fourCopyCoherent_of_kt4Core` (Lemma B1) | d4v | SATISFIES (vacuous) | [D] (vacuous: hypothesis H fails, I3.133) |
| I3.141 | `KT4Cone` — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.142 | `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the … | dna | FAILS [hyp] | [X] r2 C8 (rot3 pi: K(E0); cyc3: K(Z_F)) |
| I3.143 | `ipW`, `dualW` (the Euclidean pairing and dual cone of tables) | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.144 | `Q3`, `twin`, `pauliW`, `twistQ3` | dna | FAILS [hyp] | [X] r2 C4 (a pure state outside K); r2 CC twin (K ≠ twin) |
| I3.145 | P-STAGE2 (named premise of KT4-PREM-1) | nr | NOT REACHED | absent bridge A3 (P-STAGE2 not at L); its cone consequence hcl: I3.131 |
| I3.146 | P-ACT2 (named premise of KT4-PREM-1) | nr | NOT REACHED | absent bridge A4 (P-ACT2 not at L); cone consequence hgate: I3.132; idle-extension reading: I3.137 |
| I3.147 | H1 — products in `K` | cone | SATISFIES [cone] | [X] r2 C1 (symbolic SOS, whole ball) |
| I3.148 | H2 — `cnot`-invariance (level (i)); `G16`-invariance (level (ii… | cone | SATISFIES [cone] | [X] r2 C2 (level (i) for K(E0); level (ii) for K(Z_F)) |
| I3.149 | H3 — trace self-duality `K = dualW K` | cone | SATISFIES [cone] | [X] r2 C3 certificates + [A] SD1/SD2 (AUDIT-X) |
| I3.150 | (b_S4) — the full rotation group of one token acts on the pair … | dna | FAILS [hyp] | [X] r2 C8 actC rot3(pi) (K(E0)), actC cyc3 (K(Z_F)) |
| I3.151 | (b_n) — one rotation subgroup of one token about an off-frame a… | dna | FAILS [hyp] | [X] r2 C8 actC R_n(pi/2), n = (3,0,4)/5 |
| I3.152 | (b_R1) — one order-3 rotation of one token about (5,1,1) | dna | FAILS [hyp] | [X] r2 C8 actC R1 (-1; -2383/5316) |
| I3.153 | (b_DJ) — the native drive with the native `J` acting on one tok… | dna | FAILS [hyp] | [X] r2 C8 actC/actT nflip (flow members; K(E0)), actC cyc3 and actC Rx(pi/2) (K(Z_F)) |
| I3.154 | IE2 — idle extension of the pair interaction groups — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.155 | frame covariance (FC) of the native gate | dna | FAILS [hyp] | [W] FC ⟺ IE1 given hgate (stage 2 [A]); hgate holds (r2 C2), IE1 fails |
| I3.156 | INV2 — the native gate is an operational involution on the pair… | cone | SATISFIES [cone] | [X] r2 C2, C6, D1a (cnot preserves the body, involutive) |
| I3.157 | SDC = P3 ∧ OVL4 ∧ CSD2 — self-duality under composition — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.158 | N0 ∧ N1 ∧ N2 — regrouping invariance of a four-token composite … — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.159 | S2 Pair — a compact, gate-reversible COMP-1 pre-composite (stag… | cone | SATISFIES [cone] | [W] over [X] r2 C1, C5, C6 (slice convex, compact, products inside, effects valid, unit pairing) |
| I3.160 | H — pair-level homogeneity of `K` | cand | FAILS [hyp] | [A] stage 3 [W + L] (surgery cones not homogeneous); stage 4 Y6 |
| I3.161 | T — pair-level reversible richness (transitivity on extreme ray… | cand | FAILS [hyp] | [A] stage 4 Y6 (extreme-ray invariant c = 15 on defects, 9 on products) |
| I3.164 | K1 — the dimension | inh | SATISFIES [inherit] | [K] dim1_core instance; K1 CONDITIONAL for Q3 likewise |
| I3.165 | K2 — the composite — other K2 clauses: LT encoded, cone exists | dna | FAILS [hyp] | [X] r2 C8 (its clause "local actions compatible with the composite cone") |
| I3.166 | K∞ — the field-neutral premises | inh | SATISFIES [inherit] | K∞ OPEN for Q3 likewise (pair-blind) |
| I3.167 | K∞-Stage | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.168 | K∞-Act | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.169 | K∞-Drive | inh | SATISFIES [inherit] | [K] ball3Drive KIF:449; [X] r6 T4; operational availability open for Q3 likewise |
| I3.170 | K∞-Trans | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.171 | K∞-Seed | b1 | SATISFIES [inherit] | [K] B1; [X] r6 T2 (sharp seed on the ball); K ⊆ maxCone [X] r2 C5 |
| I3.172 | K∞-V4 | b1 | SATISFIES [inherit] | [K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5 |
| I3.173 | K∞-Copy | inh | SATISFIES [inherit] | [X] r6 T5; K∞-Copy open for Q3 likewise (one N built into NativeGate) |
| I3.185 | carrier-map identities for every one-copy linear map: `actT_pro… | thm | SATISFIES [K-indep] | [K] CD:1923-1931, K2Guard:172 (products only) |
| I3.186 | `eball_three` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.187 | the classification step of KT4-PREM-1: `hcls ∧ hadm ∧ hgate ∧ I… | d4v | SATISFIES (vacuous) | [W] KT4-PREM-1 result.md:128 (vacuous: IE1 fails, I3.137) |
| I4.236 | Kₙ census §4 — scope of K∞'s geometric branch | inh | SATISFIES [inherit] | [A] kn census §4; [X] r2 C10: the pair reading of SF fails for Q3 and the cones alike |
| I1.17 | layered theorem statement (Main.md:82) | hmg | NOT REACHED | I1 bridge field: none at L (Main.md:82) |
| I4.3 | HasParallelReferenceExtension | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.4 | HasQutritReferenceExtension | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.14 | InertSpectatorCompositionality | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.29 | ContextStable | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.31 | ImplementationLocality | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.42 | OIPlusLocal | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.45 | StructurallyClosed | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.56 | LayerFlowExecutable | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.65 | PhysicalCompletionConditions | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.66 | CompositeOperationalValidity | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.67 | HasCompositeUnitaryControl | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.68 | IteratedAncillaClosure | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.69 | SystemToLevelOne | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.70 | ExactAllFiniteEndomorphicQuantumOps | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.73 | WellFormed | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.74 | SubstantiveCompletion | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.80 | CompletedOI | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.82 | ObservationalIndependence | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.85 | ReversibleRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.87 | ObserverRecursion | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.88 | OIPlus | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.96 | ObservationalIndependence | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.99 | ReversibleRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.102 | OIPlus | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.110 | EmbeddedObservation | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.115 | OIPlusEmbedded | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.118 | PhaseFreeRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.120 | OIPlusMin | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.123 | CyclicRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.124 | OIPlusPos | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.127 | InverseAccessibility | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.128 | LieRankRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.133 | ReversibleImplementationLocality | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.137 | OIPlusMicro | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.143 | DrivesElementary | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.144 | QuantumArchitecture | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.179 | PairFlowSourced | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.187 | ShadowQuantum | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.210 | psd_iff_trace_nonneg | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.215 | psd_trace_mul_nonneg | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.216 | accessible_cone_full | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.241 | DerivedOI | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.244 | ElementaryTransitionRichness | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I4.245 | OIPlusElem | hmg | NOT REACHED | level M; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.3 | The operational-extension boundary | hmg | NOT REACHED | level G (operational co…; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.29 | The operational-completion characterization (manuscript stateme… | hmg | NOT REACHED | level G (every nonempty…; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.30 | Bare finite OI does not imply QM; OI-compatible theory plus (i)… | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.31 | Quantum-complete OI (OI⁺): observational independence, reversib… | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.32 | Primitive-source form: implementation locality, phase-free rich… | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.33 | Substratum-source form | hmg | NOT REACHED | level G/H; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.34 | Layer-flow form | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.35 | Typed form | hmg | NOT REACHED | level G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.62 | Comparison of routes and dependency scope: in-house, imported, … | hmg | NOT REACHED | level M/G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.63 | Operational-reconstruction route: target conditions and the out… | hmg | NOT REACHED | level G/O; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |
| I2.69 | The claim structure: the four layers, the four-part theorem sta… | hmg | NOT REACHED | level H/M/G; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a)) |

### Table A3 — every EXOTIC-E alternative (stage-4 Y4, Y5, Z seeds; stage-5 C5 census, κ and D5 seeds; S2 and the finite groups)

| item | statement (one line) | class | verdict | evidence |
|---|---|---|---|---|
| I3.1 | `W d` | def | SATISFIES [K-indep] | [K] CD:95-97; LT is encoded by the carrier (as for Q3) |
| I3.2 | `prodState` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.3 | `maxCone` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.4 | `jointStates` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.5 | `IsProduct` | def | SATISFIES [K-indep] | [K] CD:160-195 (definitions) |
| I3.6 | `actT` — invariance of K under a rotation: rows I3.150-153 | def | SATISFIES [K-indep] | [K] CD:197-202; [X] r2 D0c |
| I3.7 | `actC` — invariance of K under a rotation: rows I3.150-153 | def | SATISFIES [K-indep] | [K] CD:197-202; [X] r2 D0c |
| I3.8 | `IsNot` | inh | SATISFIES [inherit] | [K] isNot_nflip CD:838; [X] r2 D1e, r6 T3 |
| I3.9 | `NativeGate` | gate | SATISFIES [K-indep] | [K] nativeGate_cnot CD:1159; [X] r2 D1b, D1d, D1g |
| I3.10 | `Entangling` | gate | SATISFIES [K-indep] | [K] entangling_cnot CD:1378; [X] r2 D1f |
| I3.11 | `cnot`, `sgn`, `pc`, `pt`, `z3`, `nflip`, `xplus`, `phiW` (the … | def | SATISFIES [K-indep] | [K] CD:741-798; [X] r2 D0a (cnot = Ad(CNOT), control first) |
| I3.12 | `isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC` | thm | SATISFIES [K-indep] | [K] CD:838-860; [X] r2 D1b, D1d, D1e |
| I3.13 | `nativeGate_cnot` | thm | SATISFIES [K-indep] | [K] CD:1159; [X] r2 D1g |
| I3.14 | `entangling_cnot` | thm | SATISFIES [K-indep] | [K] CD:1378; [X] r2 D1f |
| I3.15 | parity: `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGat… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.16 | `blockData_of_nativeGate` (with `BlockData`) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.17 | `not_entangling_one` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.18 | `dim_of_nativeGate` (the selector) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.19 | `three_of_nativeGate` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.20 | DIM-1 controls: `nativeGate_cnot1`, `not_entangling_cnot1`, `no… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.21 | `dim1_core` (DIM-1 verdict) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.22 | `not_even_of_gateRel` (with `finrank_plus_eq_finrank_minus_rel`) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.23 | `GateRel` | gate | SATISFIES [K-indep] | [K] gateRel_cnot (ParityNot); [X] r2 D1b |
| I3.24 | `piRotation_three` (with `tangentPlus_three`, `det_three`) | inh | SATISFIES [inherit] | [K] ParityNot:161; [X] r6 T3 (nflip = pi-rotation about e1) |
| I3.25 | `not_gateRel_refl3`, `not_gateRel_negId3` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.26 | `not_posFwd_gJ3`, `not_posFwd_gJ5` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.27 | `exists_frame_gateRel_iff_odd` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.28 | `not_posFwd_gRev` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.29 | `CtrlGate` | gate | SATISFIES [K-indep] | [K] ctrlGate_of_nativeGate RelcSelectBlock:53 |
| I3.30 | `not_even_of_relC` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.31 | `dim_of_ctrlGate`, `three_of_ctrlGate` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.32 | `ctrlGate_of_nativeGate` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.33 | `gSq_sep`, `gSqInv_sep` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.34 | `relT_not_dimension_selecting` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.35 | `NativeGateOf` | gate | SATISFIES [K-indep] | [W] from nativeGate_cnot: maxCone ⊆ maxConeOf avail for every effect-sound avail |
| I3.36 | `EntanglingOf` | gate | SATISFIES [K-indep] | [W] = Entangling once maxConeOf avail = maxCone (B1); [K] entangling_cnot |
| I3.37 | `dim_of_nativeGateOf` | inh | SATISFIES [inherit] | [K] K1Bridge:128, :138 (through B1) |
| I3.38 | `three_of_nativeGateOf` | inh | SATISFIES [inherit] | [K] K1Bridge:128, :138 (through B1) |
| I3.39 | `HasTwoSharpTests` | inh | SATISFIES [inherit] | [K] hasTwoSharpTests_iff SharpTests:155; [X] r6 T1 |
| I3.40 | `hasTwoSharpTests_iff` | inh | SATISFIES [inherit] | [K] hasTwoSharpTests_iff SharpTests:155; [X] r6 T1 |
| I3.41 | `two_le_not_implied` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.42 | `prodState_mem_maxCone` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.43 | `CandidateCone` | cone | SATISFIES [cone] | [W] H1 from cone(G.SEP) ⊆ K; K = K* ⊆ SEP* = maxCone |
| I3.44 | `no_candidateCone_cnot_reflY` | kthm | SATISFIES [K] | [K] K2Guard:143 (no node group contains actT reflY [W]) |
| I3.45 | `three_of_nativeGate_of_two_le` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.46 | `two_le_of_entangling` | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.47 | `three_of_nativeGateOf_of_two_le` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.48 | `EffectsOn` | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.49 | `maxConeOf` | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.50 | `MixingClosed` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.51 | `maxConeOf_avail_eq` (with `sharpFamily_subset_avail`, `maxCone… | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.52 | `fullEffects_subset_avail` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.53 | `not_fullEffects_of_orbit` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.54 | `DenseBoundaryOrbit` | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.55 | `denseBoundaryOrbit_of_boundaryTransitive` | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.56 | `maxConeOf_avail_eq_of_dense` (with the dense ball and selector… | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.57 | `FiniteStage` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.58 | `IsEffectOn` | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.60 | `IsBoundaryState` | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.69 | `CopyNatural` (K∞-Copy) | inh | SATISFIES [inherit] | [X] r6 T5; K∞-Copy open for Q3 likewise (one N built into NativeGate) |
| I3.73 | `SharpSeed` (K∞-Seed, P1) | b1 | SATISFIES [inherit] | [K] B1; [X] r6 T2; K ⊆ maxCone [W] |
| I3.74 | `PreservesBody` | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.75 | `SeedOrbitAvailable` (K∞-V4, V4′) | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.76 | `BoundaryTransitive` (K∞-Trans; "K∞-R" in OG-1's record) | inh | SATISFIES [inherit] | [K] boundaryTransitive_fullAut3 OG:537, _ball3Drive ON:665; [X] r6 T6 |
| I3.78 | `preservesBody_drive` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.79 | `seedOrbit_ball3_eq` (the reduced orbit-generation theorem) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.80 | `boundaryTransitive_fullAut3` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.82 | `orbit_generation_core` (OG-1 verdict) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.83 | `boundaryTransitive_ball3Drive` (with `driveWords3`) | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.87 | `TransBody` (TRANS) | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.88 | `eq_qBall_of_boundaryTransitive` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.89 | `exists_affine_image_eq_eball` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.92 | `DirectedStages` (with `StageMap`) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.94 | `SCInf` (SC∞, K∞-Stage) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.95 | `BinaryVisible` (ELEM-bin) | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.96 | `FiniteRank` (K∞-Stage) | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.97 | `sharpSeed_completion` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.98 | `exists_chart_of_finiteRank` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.99 | `OpDatum` (K∞-Act) | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.101 | `AffineRespect` | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.104 | `body_isClosed` | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.105 | `preservesBody_inducedEquiv` | nr | NOT REACHED | routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3 |
| I3.111 | `finiteOrderOn_of_stagePreserving` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.113 | `ProductData` | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.114 | `PreComposite` | cone | SATISFIES [cone] | [W] as for the explicit cones |
| I3.115 | `LocallyTomographic` | def | SATISFIES [K-indep] | [K] CompositeInterface §E: LT is a theorem of the coordinate model W 3 |
| I3.116 | `Composite` | cone | SATISFIES [cone] | [W] as for the explicit cones |
| I3.118 | `JointReversible` | cone | SATISFIES [cone] | [W] cnot ∈ G-hat |
| I3.120 | `condA_prodState` (L9, no signalling on products) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.121 | `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPr… | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.122 | `comp1_core` (COMP-1 verdict) | thm | SATISFIES [K-indep] | [K] (statement does not quantify over K) |
| I3.124 | the effect cone of the ball: `lor_ehom`, `isEffectOn_affOf`, `l… | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.125 | `NativeGateBall.parity` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.126 | `p_le_one`, `dim_of_bounds` | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.127 | `lorentz_of_effects` | inh | SATISFIES [inherit] | [K] single-body theorems (pair-blind) |
| I3.128 | `nb1_kernel_core` (NB-1 verdict) | inh | SATISFIES [inherit] | [K] (d = 3 for eball 3 with nflip, cnot) |
| I3.129 | `hcls` — N-CLASS gates (`NClass`) | gate | SATISFIES [K-indep] | [D] NClass: cnot with identity locals (KT4-PREM-1 record, M_Q) |
| I3.130 | `hadm` — pair admissibility (`PairAdm`, with `IsConvexCone`) | cone | SATISFIES [cone] | [W] as I3.43; EBF output is a convex cone |
| I3.131 | `hcl` — closedness of each pair cone | cone | SATISFIES [cone] | [W] a self-dual cone is closed |
| I3.132 | `hgate` — gate preservation (H2 of stage 3 is this clause for `… | cone | SATISFIES [cone] | [W] cnot ∈ G-hat, G16 ⊆ G-hat (level (ii)) |
| I3.133 | `H` — the four-copy core (`KT4Core`, with `KT4`, `KT4LT`) | d4f | FAILS [hyp] | [D] kt4_forward_ie1 + [W] stage 4: H ⇒ IE1 ⇒ Q3 |
| I3.134 | token clauses `tokA`, `tokB` (`TokenCoherent`) — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.135 | FCC — the cone-level four-copy interface (`FourCopyCoherent`, `… | d4f | FAILS [hyp] | [D] Lemma B1 + kt4_forward_ie1 + [W] stage 4 |
| I3.136 | `PairLinked` (Lemma R's interface form) — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.137 | IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | dna | FAILS [hyp] | [W] IE1 ⊇ (b_S4) ⇒ K = Q3 (stage 4 Y2 [A]); K ≠ Q3 [X] r3 |
| I3.138 | `EvenCycle` (with `EvenCycle4`) | d4s | SATISFIES | [W] cnot with identity locals: every twist bit false |
| I3.139 | `kt4_forward_ie1` (Theorem A′, the audited theorem) | d4v | SATISFIES (vacuous) | [D] (vacuous: hypothesis H fails, I3.133) |
| I3.140 | `fourCopyCoherent_of_kt4Core` (Lemma B1) | d4v | SATISFIES (vacuous) | [D] (vacuous: hypothesis H fails, I3.133) |
| I3.141 | `KT4Cone` — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.142 | `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the … | dna | FAILS [hyp] | [W] {ball3Drive flow, J} forces Q3 (C5 census [A]); K ≠ Q3 [X] r3 |
| I3.143 | `ipW`, `dualW` (the Euclidean pairing and dual cone of tables) | def | SATISFIES [K-indep] | [K] definitions (I3.143 [D]) |
| I3.144 | `Q3`, `twin`, `pauliW`, `twistQ3` | dna | FAILS [hyp] | [X] r3 S (the seed excludes its own pure state) |
| I3.145 | P-STAGE2 (named premise of KT4-PREM-1) | nr | NOT REACHED | absent bridge A3 (P-STAGE2 not at L); its cone consequence hcl: I3.131 |
| I3.146 | P-ACT2 (named premise of KT4-PREM-1) | nr | NOT REACHED | absent bridge A4 (P-ACT2 not at L); cone consequence hgate: I3.132; idle-extension reading: I3.137 |
| I3.147 | H1 — products in `K` | cone | SATISFIES [cone] | [W] cone(G-hat.SEP) ⊆ K |
| I3.148 | H2 — `cnot`-invariance (level (i)); `G16`-invariance (level (ii… | cone | SATISFIES [cone] | [W] cnot ∈ G-hat, G16 ⊆ G-hat (level (ii)) |
| I3.149 | H3 — trace self-duality `K = dualW K` | cone | SATISFIES [cone] | [A] EBF (AUDIT-X) over the r3 seed |
| I3.150 | (b_S4) — the full rotation group of one token acts on the pair … | dna | FAILS [hyp] | [W] stage 4 Y2 [A] + K ≠ Q3 [X] r3 |
| I3.151 | (b_n) — one rotation subgroup of one token about an off-frame a… | dna | FAILS [hyp] | [W] stage 4 Y3/Z z5 [A] + K ≠ Q3 [X] r3 |
| I3.152 | (b_R1) — one order-3 rotation of one token about (5,1,1) | dna | FAILS [hyp] | [W] stage 4 Y7 [A] + K ≠ Q3 [X] r3 |
| I3.153 | (b_DJ) — the native drive with the native `J` acting on one tok… | dna | FAILS [hyp] | [W] C5 census / D5 B1 [A] + K ≠ Q3 [X] r3 |
| I3.154 | IE2 — idle extension of the pair interaction groups — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.155 | frame covariance (FC) of the native gate | dna | FAILS [hyp] | [W] as for the explicit cones |
| I3.156 | INV2 — the native gate is an operational involution on the pair… | cone | SATISFIES [cone] | [W] cnot ∈ G-hat |
| I3.157 | SDC = P3 ∧ OVL4 ∧ CSD2 — self-duality under composition — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.158 | N0 ∧ N1 ∧ N2 — regrouping invariance of a four-token composite … — not a function of the pair cone | nr | NOT REACHED | no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2) |
| I3.159 | S2 Pair — a compact, gate-reversible COMP-1 pre-composite (stag… | cone | SATISFIES [cone] | [W] as for the explicit cones |
| I3.160 | H — pair-level homogeneity of `K` | cand | FAILS [hyp] | [W + L] stage 4 Y6: H ⇒ K = Q3; K ≠ Q3 [X] r3 |
| I3.161 | T — pair-level reversible richness (transitivity on extreme ray… | cand | UNDECIDED | UNDECIDED (stage 4 T: EXCLUDES-ALL open) |
| I3.164 | K1 — the dimension | inh | SATISFIES [inherit] | [K] dim1_core instance; K1 CONDITIONAL for Q3 likewise |
| I3.165 | K2 — the composite — other K2 clauses: LT encoded, cone exists | dna | FAILS [hyp] | [W] as I3.150 |
| I3.166 | K∞ — the field-neutral premises | inh | SATISFIES [inherit] | K∞ OPEN for Q3 likewise (pair-blind) |
| I3.167 | K∞-Stage | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.168 | K∞-Act | inh | SATISFIES [inherit] | pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L) |
| I3.169 | K∞-Drive | inh | SATISFIES [inherit] | [K] ball3Drive KIF:449; [X] r6 T4; operational availability open for Q3 likewise |
| I3.170 | K∞-Trans | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.171 | K∞-Seed | b1 | SATISFIES [inherit] | [K] B1; [X] r6 T2; K ⊆ maxCone [W] |
| I3.172 | K∞-V4 | b1 | SATISFIES [inherit] | [K] B1/B2; K ⊆ maxCone [W] |
| I3.173 | K∞-Copy | inh | SATISFIES [inherit] | [X] r6 T5; K∞-Copy open for Q3 likewise (one N built into NativeGate) |
| I3.185 | carrier-map identities for every one-copy linear map: `actT_pro… | thm | SATISFIES [K-indep] | [K] CD:1923-1931, K2Guard:172 (products only) |
| I3.186 | `eball_three` | inh | SATISFIES [inherit] | [K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3) |
| I3.187 | the classification step of KT4-PREM-1: `hcls ∧ hadm ∧ hgate ∧ I… | d4v | SATISFIES (vacuous) | [W] KT4-PREM-1 result.md:128 (vacuous: IE1 fails, I3.137) |
| I4.236 | Kₙ census §4 — scope of K∞'s geometric branch | inh | SATISFIES [inherit] | [A] kn census §4 (token = qubit ball) |
| I1.17 | layered theorem statement (Main.md:82) | hmg | NOT REACHED | I1 bridge field: none at L |
| I4.3 | HasParallelReferenceExtension | hmg | NOT REACHED |  |
| I4.4 | HasQutritReferenceExtension | hmg | NOT REACHED |  |
| I4.14 | InertSpectatorCompositionality | hmg | NOT REACHED |  |
| I4.29 | ContextStable | hmg | NOT REACHED |  |
| I4.31 | ImplementationLocality | hmg | NOT REACHED |  |
| I4.42 | OIPlusLocal | hmg | NOT REACHED |  |
| I4.45 | StructurallyClosed | hmg | NOT REACHED |  |
| I4.56 | LayerFlowExecutable | hmg | NOT REACHED |  |
| I4.65 | PhysicalCompletionConditions | hmg | NOT REACHED |  |
| I4.66 | CompositeOperationalValidity | hmg | NOT REACHED |  |
| I4.67 | HasCompositeUnitaryControl | hmg | NOT REACHED |  |
| I4.68 | IteratedAncillaClosure | hmg | NOT REACHED |  |
| I4.69 | SystemToLevelOne | hmg | NOT REACHED |  |
| I4.70 | ExactAllFiniteEndomorphicQuantumOps | hmg | NOT REACHED |  |
| I4.73 | WellFormed | hmg | NOT REACHED |  |
| I4.74 | SubstantiveCompletion | hmg | NOT REACHED |  |
| I4.80 | CompletedOI | hmg | NOT REACHED |  |
| I4.82 | ObservationalIndependence | hmg | NOT REACHED |  |
| I4.85 | ReversibleRichness | hmg | NOT REACHED |  |
| I4.87 | ObserverRecursion | hmg | NOT REACHED |  |
| I4.88 | OIPlus | hmg | NOT REACHED |  |
| I4.96 | ObservationalIndependence | hmg | NOT REACHED |  |
| I4.99 | ReversibleRichness | hmg | NOT REACHED |  |
| I4.102 | OIPlus | hmg | NOT REACHED |  |
| I4.110 | EmbeddedObservation | hmg | NOT REACHED |  |
| I4.115 | OIPlusEmbedded | hmg | NOT REACHED |  |
| I4.118 | PhaseFreeRichness | hmg | NOT REACHED |  |
| I4.120 | OIPlusMin | hmg | NOT REACHED |  |
| I4.123 | CyclicRichness | hmg | NOT REACHED |  |
| I4.124 | OIPlusPos | hmg | NOT REACHED |  |
| I4.127 | InverseAccessibility | hmg | NOT REACHED |  |
| I4.128 | LieRankRichness | hmg | NOT REACHED |  |
| I4.133 | ReversibleImplementationLocality | hmg | NOT REACHED |  |
| I4.137 | OIPlusMicro | hmg | NOT REACHED |  |
| I4.143 | DrivesElementary | hmg | NOT REACHED |  |
| I4.144 | QuantumArchitecture | hmg | NOT REACHED |  |
| I4.179 | PairFlowSourced | hmg | NOT REACHED |  |
| I4.187 | ShadowQuantum | hmg | NOT REACHED |  |
| I4.210 | psd_iff_trace_nonneg | hmg | NOT REACHED |  |
| I4.215 | psd_trace_mul_nonneg | hmg | NOT REACHED |  |
| I4.216 | accessible_cone_full | hmg | NOT REACHED |  |
| I4.241 | DerivedOI | hmg | NOT REACHED |  |
| I4.244 | ElementaryTransitionRichness | hmg | NOT REACHED |  |
| I4.245 | OIPlusElem | hmg | NOT REACHED |  |
| I2.3 | The operational-extension boundary | hmg | NOT REACHED |  |
| I2.29 | The operational-completion characterization (manuscript stateme… | hmg | NOT REACHED |  |
| I2.30 | Bare finite OI does not imply QM; OI-compatible theory plus (i)… | hmg | NOT REACHED |  |
| I2.31 | Quantum-complete OI (OI⁺): observational independence, reversib… | hmg | NOT REACHED |  |
| I2.32 | Primitive-source form: implementation locality, phase-free rich… | hmg | NOT REACHED |  |
| I2.33 | Substratum-source form | hmg | NOT REACHED |  |
| I2.34 | Layer-flow form | hmg | NOT REACHED |  |
| I2.35 | Typed form | hmg | NOT REACHED |  |
| I2.62 | Comparison of routes and dependency scope: in-house, imported, … | hmg | NOT REACHED |  |
| I2.63 | Operational-reconstruction route: target conditions and the out… | hmg | NOT REACHED |  |
| I2.69 | The claim structure: the four layers, the four-part theorem sta… | hmg | NOT REACHED |  |

### Table A3-seeds — the alternative-specific rows of Table A3

| alternative | node group (level (ii)) | seed (exact) | r3 check | recomputed here | cited [A] |
|---|---|---|---|---|---|
| A3a Y4 | S3: actC Rx with G16; the native drive on one or both tokens | c = 4609/4608 at φ0 = (1,2,3i,−1+i) | S A3a; R-a | X⊗X forms 1/9, 121/42 | reduction to {φ0, CNOTφ0} (Y4) |
| A3b Y5 | S1 ⟨G16, SWAP⟩; S2 reachable set G16·SEP; the listed finite extensions | c = 517/512, d_min = 5/256 | S A3b; R-b | G16, ⟨G16,SWAP⟩ orbit minima 5/256 | Clifford census 23040 (Y5 F1–F5) |
| A3c Z | S3: actC Rx with G16 | α = 7/8 at ψ_a = (15,−1,7,7)/18 | S A3c; R-e | V-coefficients, f ≤ 7/8 | reachable-set formula (Z z3) |
| A4a C5 1/2304 | {flow}@C (drive about x on the control) with G16 | α = 499783/500000 at φ0 | S A4a 1/2304; R-a | as A3a | reduction (C5 census) |
| A4a C5 5/256 | {J}, {NOT, J} on either token; {flow}@T; native finite groups | α = 122509/125000 at φ0 | S A4a 5/256; R-b | orbits 768 / 384, min 5/256 | — |
| A4a C5 1/8704 | ball3Drive flow on the target (Z⊗Z torus) with G16 | c = 17409/17408 at φ0 | S A4a 1/8704; R-c | Z⊗Z bound 1/8704 (sharp) | reduction (C5 S4) |
| A4b κ / A5 S2 | κ: Ad U(w) with G16; S2: actC Rz ∘ actT Rx with G16 (and ⟨T³, G16⟩) | Bell seed F = z_(−1,−1) on C1 ∪ C2 | S A4b; R-g | circles invariant, maximally entangled | EBF (AUDIT-X) |
| A4c D5 | the substratum monomial class (with cnot, SWAP, T) | c = 513/512 at (1,2,3,4)/√30 | S A4c; R-d | min arrangement |det| 1/15 | σ_max arrangement bound (D5 C) |
| A5 G_S | ⟨G16, Ad(S⊗I)⟩ (32) | Bell seed e_F, orbit of 8 | R-h | orbit 8, overlaps {0, 1/2} | EBF |
| A5 G_H | ⟨G16, Ad(I⊗H)⟩ (128) | α = 9/10 at ψ_a | S A5 G_H; R-f | m = 4160/6561 (32 rays) | — |
| A5 G_Cl | Clifford ∪ Clifford∘T (23040) | α = 99/100 at ψ_a | S A5 G_Cl | window given m | m = 6272/6561 (Z z4) |
| A5 any finite group | every finite group ⊇ G16 | Y5 seed (or the group's own) | — | — | dimension corollary [W] (Y1.5, Z claim D) |


## 4. The three statements, per alternative

### A1 — K(E0), level (i)
- **(i) Exclusion by an item at L: none.** Every item at status *proved [K]* or a definition at L is SATISFIED —
  K-independently, or checked on the cone (the one kernel theorem that quantifies over pair cones with a one-copy
  map, `no_candidateCone_cnot_reflY` K2Guard.lean:143, holds: `actT reflY` moves K(E0), pairing −1, r2 C7). Every
  clause on `K` that L or the PT records carry is met: exactly for H1 (symbolic SOS over the whole ball), H2 (level
  (i)), the H3 certificates, `CandidateCone`, `hadm`, `hgate`, the `maxCone` bound and the slice conditions (r2
  C1–C6); `hcl` by the audited SD1/SD2 closedness [A].
  The 13 FAILS rows (§7) are do-not-assume items, [D] four-token hypotheses and PT-record candidates. K(E0) fails the
  (b) family already at the NOT: `actC nflip` and `actT nflip` move it out (pairing −1), as do `rot3 π`, `cyc3`, the
  quarter-turns about x and about (3,0,4)/5, and R1 (r2 C8); FCC fails uniformly at −1 (r2 C9). It is level (i) only
  (`⟨E0, Ad(Z⊗I)E0⟩ = −1`, r2 C2) and is not SWAP-invariant (−5/13).
- **(ii) Realization at L: nothing attached.** No statement at L gives K(E0), or any cone in `W 3`, an
  embedded-observer realization, and none proves an obstruction (§6; r5). Open; missing bridge H→P (and the M→P
  dictionary).
- **(iii) Single-token premises:** all inherited by construction (the tokens are `eball 3 = ball3` with `nflip`, `z3`,
  `cnot`, as for Q3); the checkable ones verified exactly (§5).

### A2 — K(Z_F), level (ii) (the explicit cone also of every subgroup of `Stab_Cl(Z_F)`, order 1536)
- **(i) none.** The same 13 FAILS rows. K(Z_F) is invariant under G16, SWAP, both NOTs and `rot3 π` (r2 C2, C8), so it
  meets the NOT-only and native-finite readings, and leaves itself under `cyc3` on either token (−1/2), under the
  quarter-turn of the drive about x (−1/2), under the quarter-turn about (3,0,4)/5 (−1/2) and under R1
  (−2383/5316, the value AUDIT-Y R7 found with its own witness) (r2 C8); FCC fails uniformly at −1/2 (r2 C9);
  `actT reflY` moves it (−1/8, r2 C7).
- **(ii) nothing attached at L.** The stage-5 records show K(Z_F) carries a pair-level drivability pattern (C5 ζ-1, D5
  F1–F3): a single-system structure of the cone, not an embedded-observer realization; L attaches none (r5).
- **(iii)** as A1.

### A3–A5 — the EXOTIC-E alternatives (Table A3, rows coincide; alternative-specific rows in Table A3-seeds)
- **(i) none.** H1, H2 (level (ii)) and the node invariance hold by construction [W]; H3 by EBF [A]; `K ⊆ maxCone`
  because `K = K* ⊆ SEP* = maxCone` [W]; `no_candidateCone_cnot_reflY` applies to each (a cnot-invariant candidate
  cone) and no node group contains `actT reflY` [W]. Each seed is checked exactly (r3: one negative eigenvalue; it
  excludes its own pure state, so `K ≠ Q3`; inside its window for the recomputed or recorded overlap bound; ≥ 0 on its
  group's listed reachable states). The 12 FAILS rows are hypothesis failures, each from the audited theorem "(b_min)
  with H1–H3 forces Q3" [A: stage 4 Y2, Y3/Z z5, Y7; stage 5 C5 census, D5 B1] with `K ≠ Q3` [X r3] for the (b) forms,
  IE1, IE1Drive, FC and K2's clause; Q3-reachability because `K ⊇ Q3` would force `K = Q3` by self-duality; FCC and
  `H` through the [D] theorems (Lemma B1, `kt4_forward_ie1`) with stage 4; homogeneity by stage 4 Y6 [W + L]. Node T
  is UNDECIDED (stage 4: EXCLUDES-KNOWN only).
- Per alternative: A3a and A4a-1/2304 — S3 (`actC Rx` with G16) and the native drive on one or both tokens; A4a-5/256 —
  K is invariant under J and the NOT (on either token) by construction and still fails (b_DJ); A4a-1/8704 —
  `ball3Drive`'s own flow (axis z) on the target; A4b — κ and S2 share the Bell seed on `C1 ∪ C2`; A4c — K is invariant
  under the whole monomial group (the transcription of the substratum class's structural closure) and is not Q3;
  A5 — `G_S` (Bell seed, orbit 8), `G_H` (`m = 4160/6561` recomputed), `G_Cl` (`m = 6272/6561` cited), every finite group
  (dimension corollary [W, A]).
- **(ii) nothing attached at L**; for an existence-only alternative even the cone is not exhibited.
- **(iii)** as A1.

## 5. Statement (iii): the single-token premises, common to every alternative

| premise | the alternatives' tokens (= Q3's) | evidence |
|---|---|---|
| K∞-Stage (`SCInf`, `BinaryVisible`, `FiniteRank`) | pair-blind; at L no `DirectedStages` instance for the ball (controls only): open for Q3 likewise | I3.94–I3.96, I3.167; ROADMAP.md:1010–1013 |
| K∞-Act (`OpDatum`, `AffineRespect`, inverse datum) | pair-blind; open likewise | I3.99, I3.101, I3.168 |
| K∞-Drive (`ElementaryDrivability`) | instance `ball3Drive` [K KIF:449]; `J_off_axis` re-checked for `ball3Drive` (flow about z) and for the stage-4/5 drive about x [X r6 T4, countercontrol T4c]; operational availability open likewise | I3.66, I3.169 |
| K∞-Trans (`BoundaryTransitive`) | [K] `boundaryTransitive_fullAut3` OG:537, `boundaryTransitive_ball3Drive` ON:665; instance [X r6 T6] | I3.76, I3.170 |
| K∞-Seed (`SharpSeed`) | `(1 + x3)/2` [X r6 T2] | I3.73, I3.171 |
| K∞-V4 (`SeedOrbitAvailable`) | [K] `not_fullEffects_of_orbit` EffectSpace:762 carries an instance (`fullAut d`, `sharpUnitFamily`) | I3.75, I3.172 |
| K∞-Copy (`CopyNatural`) | one NOT on both copies (built into `NativeGate`); the exchange identity [X r6 T5]; open as an OI source likewise | I3.69, I3.173 |
| K∞-Geom (`SingletonFaces`, `RelStrictConvex`) | hold on the token ball (the qubit: ROADMAP.md:1045–1047 [A]; the singleton-face identity [X r6 T7]); the pair reading fails for Q3, K(E0), K(Z_F) alike [X r2 C10] (I4.236's scope) | I3.62–I3.63, I3.174, I4.236 |
| DIM-1 `NativeGate`: frame, `posFwd`, `posInv`, `relT`, `relC` | [K] `nativeGate_cnot` CD:1159; [X] r2 D1b (`relT`, `relC` on all 16 basis tables), D1d (frame), D1g (positivity identity, through the [D] dictionary); countercontrol D1c (`reflY` fails both relations) | I3.9, I3.12–I3.13 |
| `IsNot`, `Entangling` | [K] `isNot_nflip` CD:838, `entangling_cnot` CD:1378; [X] r2 D1e, D1f; r6 T3 (π-rotation about e1, det 1) | I3.8, I3.10, I3.24 |
| `HasTwoSharpTests` | [K] `hasTwoSharpTests_iff` SharpTests:155 (2 ≤ 3); [X] r6 T1, countercontrol T1c | I3.39–I3.40 |

These are inherited from Q3's single-token structure by construction: every alternative is a cone in `W 3` built on
two copies of the same ball with the same NOT and gate. One identification gap is shared by Q3 and every alternative:
`ball3Drive`'s NOT `rot3 π` fixes `z3` and is not `nflip` [X r6 T3] (I3 exposed fact 3; C5, D5).

## 6. Statement (ii) in detail: what L provides

- **Scan [X r5]** over 214 kernel modules, the root and 64 text files: (a) the only module whose imports reach both a
  pair module and an H-level realization module is the root aggregator `OIBridge.lean`, which states nothing; (b) the
  one module carrying both vocabularies is CompositeInterface.lean, whose line 53 says the coordinate model "realizes a
  tensor product" (algebraic sense); (c) no manuscript, roadmap or round-note line carries both.
- **At level H, not about `W 3`:** Main.md:544–558, finite operational realization and gluing (ε-form) for a fixed
  quantum experiment (proved [M], no kernel anchor, I2.12); its composition clause, Main.md:552, applies "the local
  instruments' CP maps as `I_a ⊗ I_b` on the joint branch register". Main.md:562: "an **operational realization
  theorem**, not a uniqueness theorem: the same reversible machinery can realize non-quantum finite instrument
  families". Main.md:352: "Bare finite OI therefore does not select quantum mechanics". The kernel's H→M realizations
  (I1.41–I1.60) realize the sealed core in `FiniteOperationalTheory (Fin 2)`, whose composites are tensor products with
  the PSD cone by construction.
- **Missing bridge:** an H→P or M→P theorem; none at L (AUDIT-I §2, §5.3; I3 A8–A9; I4's bridge scan). The M→P
  dictionary `pauliW` is [D] only. The field-neutral composite obligation K2 is OPEN (ROADMAP.md:1001–1006).
- **Exposed assumption (assumption-watch marker).** The one H-level composition clause at L takes `I_a ⊗ I_b` as input,
  i.e. the composite action of local instruments, which is what every alternative lacks ((b) fails; K(E0) is not
  preserved even by the NOT). So L's realization statements cannot be read as realizing an exotic pair with local
  interventions, and Main.md:562's non-quantum families are not stated for cones in `W 3`. A cone-level countermodel
  therefore comes with no embedded-observer realization at L, and with no obstruction to one: open.

## 7. Pressure test of every FAILS row

| item | status at L | level | bridge | do-not-assume | exclusion |
|---|---|---|---|---|---|
| I3.137 IE1 | not at L, [D] | P | n/a | yes | no |
| I3.142 IE1Drive | not at L, [D] (`ie1Drive_of_ie1` is `sorry`) | P | n/a | yes | no |
| I3.144 Q3 / pure-state reachability | not at L, [D] | P | n/a | yes | no |
| I3.150–I3.153 (b_S4), (b_n), (b_R1), (b_DJ) | PT-record open; INDEPENDENT of H1–H3 at L | P | n/a | yes | no |
| I3.155 frame covariance | PT-record flagged (FC ⟺ IE1 given hgate) | P | n/a | yes | no |
| I3.165 K2, clause "local actions compatible with the composite cone" | open obligation (ROADMAP.md:1001) | P | n/a | the clause, yes | no |
| I3.133 `H` (KT4Core), uniform | not at L, [D]; as a premise assumed | P (four tokens) | no ≥3-token structure at L | no | no |
| I3.135 FCC, uniform | not at L, [D]; INDEPENDENT of L (PT stage 1–2) | P (four tokens) | as above | no | no |
| I3.160 homogeneity H | PT-record candidate ("absent at L for the pair") | P | none at L | no | no |
| I3.161 T (explicit cones; UNDECIDED for EXOTIC-E) | PT-record candidate (EXCLUDES-KNOWN) | P | none (single-system analogue K∞-Trans) | its OI⁺ counterpart (reversible richness) is | no |

No FAILS row is a theorem or a definition at L. The favourable branch (an exclusion would favour the QM target) was
pressure-tested at the one kernel theorem that ties a pair cone to a one-copy map (I3.44, met) and at the bridges
B1/B2 (they reach only the upper bound `maxCone`, which every alternative respects).

## 8. Closing table — excluded by L

| alternative | excluded by L | FAILS (hypotheses only, §7) | embedded-observer realization at L |
|---|---|---|---|
| A1 K(E0) | **none** | 13 | none attached, no obstruction: open |
| A2 K(Z_F) (and the `Stab_Cl(Z_F)` subgroups) | **none** | 13 | none attached: open |
| A3a Y4 (S3, drive) | **none** | 12 (+ T undecided) | none: open |
| A3b Y5 (S1, S2 set, finite extensions) | **none** | 12 (+ T undecided) | none: open |
| A3c Z (S3, ψ_a) | **none** | 12 (+ T undecided) | none: open |
| A4a C5 census (1/2304, 5/256, 1/8704) | **none** | 12 (+ T undecided) | none: open |
| A4b κ Bell seed (= S2 Bell seeds) | **none** | 12 (+ T undecided) | none: open |
| A4c D5 monomial seed | **none** | 12 (+ T undecided) | none: open |
| A5 G_S, G_H, G_Cl, every finite group | **none** | 12 (+ T undecided) | none: open |

## 9. What is not claimed

- No verdict on (b) and no outcome label (DERIVATION / INDEPENDENCE / CONDITIONAL): those are step 4's. No status of
  any item changes; a FAILS of a do-not-assume item is the failure of a hypothesis.
- EXOTIC-E alternatives are existence results (EBF, non-constructive); cited [A], not recomputed here: the Clifford
  census, the torus reductions to {φ0, CNOT φ0}, Z's reachable-set formula, EBF itself, SD1/SD2.
- Every check that uses `Q3` or PSD passes through the dictionary `pauliW`, a design-module object (I4 marker 1); the
  checks are exact relative to it. Instance checks (r3 S4, the rational points) are instance-scoped.
- "SATISFIES [inherit]" for an open single-token item means pair-blind and open for Q3 alike, not that the item holds.
- `K({F, cnot F})` and `K(e_c)` are not reassessed (not assigned by A1.5).
