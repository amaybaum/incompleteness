# EQ4-SOURCE — what the architecture supplies for KT(4): result (research only)

Base: certified main `bcbc516f`, read-only snapshot `scratchpad/eq/base/`. Inputs: the EQ4-F preflight package at
`f0d37906` (`scratchpad/eq5/inputs/`). Protocol: `scratchpad/eq5/PROTOCOL.md`, section EQ4-SOURCE (not edited).
Nothing here is adopted, frozen or governed; no git write, no CI, no ROADMAP or manuscript edit. There is no Lean
toolchain: every Lean text cited from the package is UNBUILT. Running record: `NOTES.md` (N0–N6).

Evidence tags (protocol): **[K]** landed kernel identifier at the base (`file:line`, paths under
`verification/lean-mathlib/OIBridge/`; CI CompositeInterface, CD CompositeDimension, K2G K2Guard, RSB RelcSelectBlock,
RSP RelcSelectParity, KF KInfFoundations, TB TransitiveBody, SC StageCompletion, ES EffectSpace, OR
OperationalRigidity, MC MonoidalCompletion, RT RegionTower); **[X]** exact computation in this directory, replayed byte
for byte (`s0`, `s1`, `s2`, with check ids); **[W]** written argument; **[E]** exact exploration (a lead); **[M]**
Mathlib v4.33.0 declaration (checkout `db584cd6`, tag `v4.33.0`); cited evidence of other threads is marked with its
thread (e.g. [X EQ3 p6]) and its hash was re-checked against its own record (§10).

## 0. Answer

**No.** The existing observational and composition architecture supplies neither `TokenCoherent` nor the KT(4)
inequalities (`FourCopyCoherent`). Both have countermodels relative to every premise the architecture states. The
countermodels are verified by exact computation, with a written assembly for the PSD steps.

- **Nothing at three or more tokens.** The base has no carrier, composite or stage tower for three or more copies:
  - COMP-1 is two-factor, and no COMP-1 value takes a composite as a factor;
  - no field-neutral module has a carrier with three or more copy indices;
  - no stage product or joint tower exists;
  - the region tower's site structure is complex-matrix typed and has no import path to or from the ball side.

  Evidence: [X s0] (12/12); ROADMAP K2 :1001–1006 and Kₙ :1058–1069, both OPEN.
- **Every field of `KT4` other than `tok` is constructible from landed COMP-1 definitions, for every quadruple of
  nonempty pair bodies.** These fields therefore carry no four-token content.
  - `H.PA` and `H.PB` are each `ProductData.minPre` of the coordinate model [K CI:528, CI:686].
  - `one_body` holds in the anchor-sum construction (§3.1) [X s1 A1–A3 + W].
- **Removing `tok` makes the headline false.** Two models, M_ρ (§3.2) and M_tw (§3.3), satisfy every hypothesis of
  `kt4_forward` other than `H.tok`. Both also satisfy local tomography of both groupings.
  - Pair cones: (Q3, Q3, Q3, twin).
  - Gates: (cnot, cnot, cnot, cnotTw), each N-CLASS.
  - In both, `TokenCoherent` fails, family (i) fails at −1/8, and the conclusion of `kt4_forward` fails: the twist
    bits are forced to (0, 0, 0, 1), which is odd [X s1 R1–R6, T1–T5, P1–P7 + W].
- **`tok` carries all of the four-copy content.** For admissible pair cones, `FourCopyCoherent ⟺ ∃ V, KT4`. Each
  direction has its own witness: Lemma B1 for (⇐) and an explicit σ-construction for (⇒) [W + X s1 S1–S4, T1].
- **The precise missing link** is a four-token composite with token identity: the product of four token states is one
  state of the four-token body, whichever grouping composes it (**TokProdState**).
  - It is state-level coherence (associativity and symmetry) of parallel preparation, for composites of composites.
  - Relative to the other fields of KT4, CandidateCone and local tomography of one grouping, TokProdState ⟺
    `TokenCoherent`. Each direction has its own written witness (§3.7).
  - No source exists at the base, field-neutral or otherwise:
    - COMP-1 has no associator, symmetry or composite-as-factor;
    - site identity exists only in the complex region tower (circular);
    - there is no product or joint protocol tower.
- **Partially supplied: the pair-level premises.**
  - `hadm` is transported from COMP-1's body bounds. The two-copy composite itself is K2, OPEN.
  - `hcls` (N-CLASS) has a written-plus-exact route (EQ2-B) from the K1 two-copy gate premises. It is unbuilt.
  - `hgate`, `hinv` and `hcl` are not implied by any stated premise. For `hgate` and `hinv`, landed objects (the
    bodies of `ball3MaxComposite` and `ball3MinComposite` with `cnot`) are exact countermodels. For `hcl`, the closure
    foil is.

The owner's distinction, in one line: what `kt4_forward` USES from the four-token layer is exactly `tok` together with
fields the architecture can build vacuously. What the architecture SUPPLIES is the vacuous part.

## 1. Q1 — no carrier or composite with three or more copies

| check (s0) | finding |
|---|---|
| Q1a | No import path, in either direction, between the field-neutral composite core and the complex region/operational core. The core includes CompositeInterface, CompositeDimension, K2Guard, K1Bridge, EffectSpace, RelcSelectBlock, NativeGateBall, TransitiveBody, KInfFoundations, StageCompletion and CompletionAction. The other side includes RegionTower, RegionLimit, QuasilocalAlgebra, TypedCompletion, OperationalAssembly and MonoidalCompletion. No module other than the aggregator reaches both sides. |
| Q1b | `PreComposite`, `ProductData`, `LocallyTomographic` and `SharpReadout` occur only in `CompositeInterface.lean`. |
| Q1c | No real-valued carrier with three or more chained `Fin` binders exists on the field-neutral side (18 modules). Control: the scanner finds `W4` in the preflight input. Countercontrols: it does not count `W d`, `Model.Carrier` or `pc`. |
| Q1d | There are 9 COMP-1 values (`minPre`, `maxPre`, `minComposite`, `maxComposite`, `bitComposite`, `ball3MinComposite`, `ball3MaxComposite`, `paddedPre`, `paddedBall3`). All have one-copy factor bodies. |
| Q1e | None of these names occurs: `FiniteStage.prod`, `DirectedStages.prod`, `stageProd`, `LocalExt`, `JointTower`, `TokenCoherent`, `FourCopyCoherent`, `NClass`, `ctrlGate_classification`, `PairAdm`. |
| Q2a | The only `DirectedStages` values are the controls `badD`, `bitTower` and `midD`. |
| Q2b | The region tower's `inclObs` and `restrict` act on `Matrix (Conf Λ Q) (Conf Λ Q) ℂ` [K RT:123, :128]. |

Records that say so:
- COMP-1: a structure "over `V`, not a construction" [K CI:5]; the stage product and the bridge from product towers
  are "not part of this module" [K CI:54–55]. The COMP-1 result:53 says it "constructs no composite larger than the
  minimal body from any source"; result:102–106 leaves open "the stage-level product of two towers and its completion".
- ROADMAP:
  - K1, CONDITIONAL (:984–1000): two copies on `W d`;
  - K2, OPEN (:1001–1006): local tomography, the composite cone, local actions and the composition theorem;
  - K∞, OPEN (:1007–1057);
  - Kₙ, OPEN (:1058–1069): "No current theorem supplies the lift"; "K2's candidate route composes elementary systems
    only".
- The landed audit `audits/foundations/kn-elementary-carrier-census.md` §1–§2.
- K2-LEDGER (v): COMP-1 is "iterable by type … but no theorem states a composite as a factor".
- Main.md:82, :212, :534, :628: a common composite/tensor-product category is an additional, unestablished
  "operational-lifting and composition" hypothesis.

## 2. The USES-versus-SUPPLIES ledger

USES gives the exact Lean hypothesis or field of `inputs/FourCopyPackage.lean` and the place where the headline's proof
consumes it. In `kt4_forward` (package :506–516), `H` is consumed only by Lemma B1 (`fourCopyCoherent_of_kt4`, :297);
`hcls`, `hcl`, `hgate` and `hinv` only by Theorem C (`kt4_general`, :479); `hadm` by both.
- Lemma B1's consumption is the written route re-derived in §3.5.
- Theorem C's consumption is EQ4-F's planned skeleton (FORMAL §6, steps S0–S18), refined where the completed preflight
  layer (`FourCopyParity.lean`) pins it. That layer was kernel-checked in the preflight run, which is design evidence,
  not landed and not [K].

| # | premise (Lean) | USES — consumed where, what exactly | SUPPLIES — class | anchor | route / countermodel / open (evidence) |
|---|---|---|---|---|---|
| 1 | `hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)` | Theorem C only: Bell state and effect of each pair (`NClass.bell_state`, `NClass.bell_effect`), orthogonality for the dual action (`NClass.ipW_map`), orientation (`chart_rule`); S2, S3, S12, S17. Not B1. | **[U] route** | two-copy sources `IsNot` [K CD:210], `CtrlGate` [K RSB:45] (from `NativeGate` by RSB:53); K1 premises recorded unsourced, ROADMAP:995–996 | Per pair: IsNot ∧ CtrlGate (∧ NormPres, derivable [W]) ⇒ N-CLASS by EQ2-B N-CLASS.1–.5 on landed lemmas RSB:60, 87, 99, 129, 162, RSP:329, CD:1805, 1870, 2051 (present [X s2 N]); certificate [X EQ2-B b1, b7]; audit 56/56. No classification theorem at the base [X s0 Q1e, s2 N]. Unbuilt. |
| 2 | `hadm : ∀ p, PairAdm (K p)` = `CandidateCone ∧ IsConvexCone` | B1: `CandidateCone.2` (⊆ maxCone: X₀₀ ≥ 0, X₀₀ = 0 ⇒ X = 0, the slice bound \|X̂_μν\| ≤ 1) and positive scaling. Theorem C: `CandidateCone.1` (link states S2; Lemma P's states), `CandidateCone.2` (gate-supplied effects, `gate_sharp_mem_dualW`), the convex cone for the bipolar S5. B1 does not use `CandidateCone.1` or cone addition. | **[T]** | COMP-1 `convex` [K CI:226], `prod_mem` [K CI:227], `subset_maxBody` [K CI:467]; `CandidateCone` [K K2G:95–96]; `eball_three` [K TB:671] | Two-copy source: the body bounds of a COMP-1 pre-composite of two balls, read in `W 3`. Model coordinates equal DIM-1's [X s2 D1–D3]; T1 coordinate map [W K2-LEDGER §3.1]. The two-copy composite itself is K2, OPEN (ROADMAP:1001–1006). |
| 3 | `hcl : ∀ p, IsClosed (K p)` | Theorem C only (S14: from closures to the cones). Not B1, not Lemma P, not Theorem D. | **[U] countermodel** | none at the base: COMP-1's body is only `convex` [K CI:226]; KTRANS-DENSE-1 result:59 | Closure foil K_cl = int Q3 ∪ conv(SEP ∪ cnot SEP) satisfies every stated two-copy premise and hadm, hgate, hinv, hcls; it is not closed. ψ = (\|00⟩+\|01⟩+\|10⟩−\|11⟩)/2 lies in cl K_cl \ K_cl [X s2 C1–C3 + W; X EQ3 p2 F4]. |
| 4 | `hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p` | Theorem C only: link states as gate images of products (S2); gate-supplied effects (S3, `gate_sharp_mem_dualW`). Not B1. | **[U] countermodel** | base gate premises are product-level only: `NativeGate.posFwd/posInv` [K CD:222–223] | Landed: body of `ball3MaxComposite` [K CI:811] (maxCone(eball 3) in W 3) with `cnot` [K CD:1160]. All stated two-copy premises and hadm, hcl, hcls hold; idW ∈ maxCone but cnot idW = chainW ∉ maxCone [X s2 G1; K K2G:110, :134]. Likewise `ball3MinComposite` [K CI:807]: cnot(prodState xplus z3) = phiW ∉ minBody [X s2 G2]. |
| 5 | `hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p` | Theorem C only: the dual action of the inverse gate in general charts (S3, `dualW_of_inv`); equal to hgate in aligned charts. | **[U] countermodel** | `CtrlGate.posInv` is product-level [K RSB:50] | The same models: `cnot.symm = cnot` [K CD:790]. Remark R-inv [W, EQ4-F] reduces hinv to hgate ∧ hcls on closures. |
| 6 | `H.PA : PreComposite (pairBody K01) (pairBody K23) V` | B1: `prodState`, `prod_mem` (famI), `prodEff` bilinear, `prodEff_apply` (famI), `prodEff_effect` (famII). Not `convex`, not `prodEff_unit`. | **[K]** | `(Model.modelData 16 16).minPre (pairBody K01) (pairBody K23)` [K CI:528, CI:686], exact type `PreComposite _ _ (Model.Carrier 16 16)`; also `maxPre` [K CI:557] | Supplied for every pair cones, with no hypothesis. |
| 7 | `H.PB : PreComposite (pairBody K02) (pairBody K13) V` | B1: `prod_mem` and `prodEff_apply` (famII), `prodEff_effect` (famI), bilinearity. | **[K]** | as row 6, same carrier | Supplied for every pair cones. |
| 8 | `H.one_body : PA.Ω = PB.Ω` | B1: famI needs PA.Ω ⊆ PB.Ω (PB's effects on PA's products); famII needs PB.Ω ⊆ PA.Ω (`tok` at PB's products). | **[U] route** | built from [K] CI:633 (`pState`), CI:646 (`pEff`), CI:652 (`pEff_pState`), CI:686 | **Anchor sum** (§3.1): for every quadruple of nonempty pair bodies (nonempty by CandidateCone.1), PA, PB and one body exist on `Carrier × Carrier` [X s1 A1–A3 + W]. Supplied vacuously, with `tok` false there. |
| 9 | `H.tok : TokenCoherent PA PB` | B1 step 7, both families: the PB coordinate products equal the PA coordinate products on PA.Ω. | **[U] countermodel** | none (no structure with three or more tokens [X s0]) | **M_ρ** and **M_tw**: every other hypothesis of `kt4_forward` holds, and `lt` too; tok fails; the conclusion fails [X s1 R1–R6, T1–T5, P1–P7 + W]. Also the anchor sum (every quadruple). Not necessary: M_id, M_T [X s1 I1–I2 + W]. |
| 10 | `FourCopyCoherent K01 K23 K02 K13` (not a hypothesis of `kt4_forward`: produced by B1 from `H`, consumed by Theorem C as `h : FCC K`) | Theorem C: inclusions (I), (II) and every step after S0. | **[U] countermodel** | none | Relative to the stated premises with KT4 minus tok: M_ρ and M_tw violate famI at −1/8 [X s1 R4]. Relative to the pair premises alone: (Q3, Q3, Q3, twin) at −1/8; C_H at −1/200 [X EQ3 p6 H1–H3]. With tok, B1 supplies it (§3.5); FCC ⟺ ∃ KT4 (§3.6). |
| 11 | setting: the `W 3` table carrier (two-copy local tomography) | the type of every pair cone; B1's table calculus | **[T]** | DIM-1 `W` [K CD:95–97] ("Local tomography is the premise this carrier encodes"); ROADMAP K2 :1001–1006 lists it OPEN | Transported per pair from DIM-1's carrier premise. `W d` is the coordinate image of any COMP-1 `Composite` [W K2-LEDGER T1]. |
| 12 | setting: `pairBody` normalization (`ω 0 0 = 1`, flattened by `finProdFinEquiv`) | factor bodies of PA and PB; B1 steps 1, 3 | **[K]** | `jointStates` [K CD:190–191], `prodEff_unit` [K CI:230]; [M] Logic/Equiv/Fin/Basic.lean:334 | Statement diff: `pairBody K` uses K in place of maxCone, and flattens. That the four-token factor *is* the standalone pair body (H0 at four tokens) is part of H's typing (rows 6–9). |
| 13 | setting: per-token charts (one chart per token, shared by every pair containing it) | the conclusion (`twistQ3 (τ p)`, `EvenCycle`) and hcls's chart data | **[U] countermodel** | single-system charts: TRB-1 [K TB:602], conditional on K∞ premises (unsourced); no base object relates a token's factor in two different pairs | M_tw is exactly token 3's chart reflected between pairs 23 and 13 as seen through the body: undetectable without tok [X s1 T3–T5]. It has no content separate from row 9. |

Not consumed: `Composite.lt` (only `kt4_forward_lt`, which forgets it). Per grouping it is constructible by
`Model.minComposite` [K CI:750] given compact pair bodies [W]. In M_ρ and M_tw it holds for both groupings and does not
yield tok.

**Counts by class (13 rows).**

| class | count | rows |
|---|---|---|
| [K] | 3 | 6, 7, 12 |
| [A] | 0 | — |
| [T] | 2 | 2, 11 |
| [U] | 8 | route: 1, 8; countermodel: 3, 4, 5, 9, 10, 13; open: none |

No row is [A]. The two-copy sources of rows 1, 2 and 11 are ROADMAP-recorded premises with status unsourced (K1
CONDITIONAL) or OPEN (K2). None is an adopted posit: the Main.md posit ledger (:706) lists no composition posit.

## 3. Routes and countermodels

Conventions are as in the package. The COMP-1 coordinate model is `Model.Carrier 16 16` (17 × 17 arrays). ι embeds a
four-copy table Z (tokens 0, 1, 2, 3) into the carrier, with the hom row and column copying the (0,0) block. The other
maps:
- R is the regrouping, (RZ)_abcd = Z_acbd;
- σ = ιRπ + (id − ιπ) is a linear involution of the carrier with σι = ιR [X s1 T1];
- ρ = flatW ∘ actT reflY;
- ρ3 is the sign s_d on the token-3 index.

### 3.1 The anchor sum: KT4 minus tok for every quadruple (route for row 8)

Construction:
- V = C × C, with C = Model.Carrier 16 16.
- PA.prodState x y = (pState x y, a0) and PA.prodEff e f = pEff e f ∘ fst.
- PB.prodState L L′ = (b0, pState L L′) and PB.prodEff E F = pEff E F ∘ snd.
- Anchors a0 = pState L0 L0′ and b0 = pState x0 y0, with x0, y0, L0, L0′ points of the four pair bodies.
- Ω = the convex hull of both product sets.

Checks:
- `prodEff_apply` holds for both structures [X s1 A1].
- PA's product effects on PB's products take the values e(x0)·f(y0) ∈ [0, 1], and symmetrically [X s1 A2].
- Hence `prodEff_effect`, `prodEff_unit` (both anchors normalized) and `convex` hold [W].
- `one_body` holds by definition.
- tok fails [X s1 A3, difference −1].
- Control: with zero anchors the unit pairing fails [X s1 A-control].

So the minimal-form `KT4` minus `tok` holds for every quadruple of nonempty pair bodies, including C_H. C_H satisfies
every pair premise of `kt4_forward` and violates FCC at −1/200 [X EQ3 p6 H1–H3 + W]. Since C_H ∉ {Q3, twin}, the
classification part of the conclusion fails as well.

### 3.2 M_ρ: the headline without `tok` is false (countermodel, row 9)

The model:
- Pair cones K = (Q3, Q3, Q3, twin).
- Gates N = (cnot, cnot, cnot, cnotTw).
- Locals (A, B, A′, B′) = (id, id, id, id) on 01, 23 and 02, and (id, reflY, id, reflY) on 13.
- PA = `modelData.minPre (pairBody Q3) (pairBody Q3)`.
- PB.prodState L L′ = pState L (ρ L′) and PB.prodEff E F = pEff E (F ∘ ρ).
- PB.Ω := PA.Ω.

Every hypothesis of `kt4_forward` other than `H.tok` holds:
- **`H.PB` is a PreComposite.**
  - `prodEff_apply` [X s1 R1].
  - ρ maps `pairBody twin` onto `pairBody Q3` [X s1 R2], so PB's products lie in PA.Ω.
  - PB's product effects at pState x y equal E(x)·F(ρy) ∈ [0, 1] [W].
- **lt holds for both groupings.** PA has `minComposite`'s lt [K CI:753 + W: `pairBody Q3` is compact]. PB's family of
  product effects equals PA's, through the bijection F ↦ F ∘ ρ [W].
- **hcls.** The `NClass` identity for cnotTw holds [X s1 R6]. id and reflY are orthogonal.
- **hadm, hcl.** Pauli dictionary [X s1 P1, P4, P6] + [W]: products are PSD; PSD effects pair nonnegatively; Q3 and
  twin are closed convex cones.
- **hgate.** cnot = Ad(CNOT) [X s1 P2]. cnotTw preserves twin [W from P2, P3].
- **hinv.** cnot and cnotTw are involutions [X s1 R5].

The conclusion fails:
- Q3 ≠ twin, because phiW ∈ Q3 \ twin and idW ∈ twin \ Q3 [X s1 P6]. This forces τ = (0, 0, 0, 1), which is odd
  [X s1 R6].
- Family (i) of Lemma P is negative at the gate-supplied witnesses [X s1 R4, value −1/8]. The witnesses are memberships
  through R5 + [W]: X = Y = phiW, E = phiW/4, F = dg(1,−1,1,−1)/4.

Countercontrol: the token-coherent structure M_σ with the same cones gives the same −1/8 for PB's effect at PA's
product, so it has no common body [X s1 R-countercontrol]. tok fails in M_ρ [X s1 R3, difference −2].

### 3.3 M_tw: a genuine regrouping with one token chart reflected (countermodel, rows 9 and 13)

The model:
- PA = modelData.
- PB.prodState L L′ = σ(pState L (ρL′)) and PB.prodEff E F = pEff E (F∘ρ) ∘ σ.
- One body ι(B4), with B4 the normalized PSD₁₆ in table coordinates.

Exact checks:
- Cross values: PB.prodEff E F (PA.prodState X Y) = fourVal X Y Ẽ (ρF̃), and symmetrically [X s1 T2].
- tok difference: (s_d − 1)·Z_abcd, nonzero exactly at d = 2 [X s1 T3].
- **TokProdState fails exactly by ρ3** [X s1 T4].
- **Single-token marginal coherence (STMC) fails at token 3's y-marginal** [X s1 T5].
- Countercontrols: in M_σ all three differences vanish [X s1 T3–T5].

The PreComposite fields reduce to the PSD dictionary:
- op4(prodA X Y) = pauliW X ⊗ pauliW Y and op4(prodB L L′) = P(pauliW L ⊗ pauliW L′)Pᵀ [X s1 P5a];
- op4(ρ3 Z) = PT₃ op4(Z) and op4(RZ) = P op4(Z) Pᵀ [X s1 P5b];
- Σ_I Z_I Z′_I = 16 tr(op4 Z · op4 Z′) [X s1 P5c].

The rest is written [W]:
- Kronecker products of PSD matrices are PSD [M Analysis/Matrix/Order.lean:213];
- conjugation preserves PSD [M LinearAlgebra/Matrix/PosDef.lean:313];
- tr(PSD·PSD) ≥ 0 [K OR:917];
- the complement identity gives the upper bound [X s1 S4].

The pair premises and the conclusion's failure are as in §3.2.

### 3.4 `tok` is not necessary (P/A/C)

- **M_id.** Uniform Q3, PA = PB = `modelData.minPre`, so KT4 minus tok holds trivially. tok fails [X s1 I1, −1]. The
  conclusion holds: all cones are Q3, τ = 0, and IE₁ holds for Q3 (local rotations act as local unitary conjugations
  [W]).
  - FCC holds for uniform Q3: fourVal X Y E F = Σ_I (prodA X Y)_I (prodB E F)_I [X s1 I1] = 16 tr(op4·op4) ≥ 0 [W, P5].
- **M_T** (EQ4-F f1 W4 completed into a model). Uniform Q3, with pair 02 read token-exchanged through σ. tabT is SWAP
  conjugation [X s1 P7]. tok fails [X s1 I2, −1]. Cross values are fourVal X Y (tabT Ẽ) F̃ [X s1 I2], and the conclusion
  holds.

These are models of P_rest ∧ C ∧ ¬tok, so `tok` is not necessary relative to the other premises. M_ρ, M_tw and the
anchor sum are models of P_rest ∧ ¬C, which shows insufficiency without it. Neither kind of model shows necessity.

### 3.5 Route: Lemma B1 (`H : KT4` with admissible cones ⇒ `FourCopyCoherent`) [W]; exact endpoints [X s1 S2, S3, L]

famI, for X ∈ K01, Y ∈ K23, E ∈ dualW K02 and F ∈ dualW K13:
1. ⟨X, E·Y·Fᵀ⟩ = fourVal X Y E F [X s1 S3].
2. `CandidateCone.2` gives X₀₀ ≥ 0, and X₀₀ = 0 ⇒ X = 0 [W; X s1 L: the four sharp-product values sum to X₀₀].
   Scaling gives X̂ = X/X₀₀ ∈ K01 with X̂₀₀ = 1. fourVal is multilinear.
3. ω := PA.prodState (flatW X̂) (flatW Ŷ) ∈ PA.Ω (`prod_mem`). Then ω ∈ PB.Ω by `one_body`.
4. e_E := Σ E_μν tabCoord μν is ≥ 0 on `pairBody K02`, and ≤ Σ|E_μν| there by the slice bound [X s1 L: the
   sign-weighted sharp sum is X_ij]. So c_E·e_E is an `IsEffectOn` effect. The same holds for F.
5. PB.prodEff (c_E e_E)(c_F e_F) ω ≥ 0 (`prodEff_effect`). By bilinearity it equals
   c_E c_F Σ E_ac F_bd PB.prodEff (tabCoord a c)(tabCoord b d) ω.
6. Apply `tok` (ω ∈ PA.Ω), then `prodEff_apply` of PA. The value is c_E c_F fourVal X̂ Ŷ E F.

famII is symmetric. It uses ω := PB.prodState …, `one_body` for ω ∈ PA.Ω, `tok`, `prodEff_apply` of PB and
`prodEff_effect` of PA.

The route uses:
- from PairAdm: CandidateCone.2 and scaling only;
- from H: the fields listed in rows 6–9.

It does not use `convex`, `prodEff_unit`, the bi-affinity laws, `lt`, closedness, any gate, CandidateCone.1 or cone
addition. The vanishing lemma of EQ4-F's route is not needed, because only linear table functionals are used.
Countercontrol: in M_ρ the same expression is ⟨E, X⟩⟨ρF, Y⟩ ≠ fourVal [X s1 S2].

### 3.6 Route: `FourCopyCoherent ⟺ ∃ V, KT4`, for admissible cones (§A.34: one witness per direction) [W]

- **(⇐)** is Lemma B1 (§3.5).
- **(⇒)** Take V = Model.Carrier 16 16, PA = modelData, PB = σ∘modelData (prodEff ∘ σ). Take the body
  ι(B), where B is the set of normalized Z with effA e f Z ≥ 0 (e ∈ dualW K01, f ∈ dualW K23) and effB E F Z ≥ 0
  (E ∈ dualW K02, F ∈ dualW K13).
  - `prod_mem` for PA uses famI; for PB it uses famII [X s1 S2, T1].
  - `prodEff_effect`: an `IsEffectOn` effect e of `pairBody K` has table ẽ ∈ dualW K and U − ẽ ∈ dualW K, by
    CandidateCone.2 and scaling [W]. The upper bound comes from the complement identity [X s1 S4].
  - `tok` holds by construction [X s1 S1].
  - `lt` of PA holds on ι(B) ⊆ ι(W4) [W]: agreement on effect pairs extends to all affine pairs
    (`prodEff_eq_of_eff_eq` [K CI:342], with bounded pair bodies), hence to the basis pairs, which read every entry of
    ι(Z). So also FCC ⟺ ∃ V, KT4LT.

### 3.7 Route: `TokenCoherent ⟺ TokProdState` (§A.34) [W]

Setting:
- **TokProdState:** ∀ x0..x3 ∈ eball 3, PA.prodState (flatW(prodState x0 x1)) (flatW(prodState x2 x3)) =
  PB.prodState (flatW(prodState x0 x2)) (flatW(prodState x1 x3)).
- **Relative to:** PA and PB pre-composites of the pair bodies (bounded), CandidateCone.1 for the four cones, and local
  tomography of PA.

Directions:
- **(⇐)**
  - T_A := (PA.prodEff (basisEff μ)(basisEff ν))_μν is affine. Equal T_A-images give equal values of every product
    effect, through the coordinate expansion (`affine_expand` [K CI:130], `prodEff_expand` [K CI:290], bilinearity).
    LT(PA) then makes T_A injective on PA.Ω.
  - The vanishing argument (±(u − coord₀₀) are effects on the pair body, then rescaling [K CI:148]) puts T_A(PA.Ω) in
    the subspace ι(W4).
  - The four-token product tables lie in T_A(PA.Ω) and affinely span ι(W4)'s normalized slice.
  - PB.prodEff(coord ac)(coord bd) composed with T_A⁻¹ is affine on the convex set T_A(PA.Ω). It agrees with the
    (ab, cd) table entry on the products, by TokProdState and both `prodEff_apply` laws. Hence it agrees on all of
    T_A(PA.Ω).
  - This direction does not use `one_body`.
- **(⇒)**
  - p_B := PB.prodState(…) ∈ PB.Ω = PA.Ω (`one_body`).
  - `tok` at p_B and `prodEff_apply` give T_A(p_B) = T_A(p_A) on the coordinate block. The vanishing argument extends
    this to the hom row and column.
  - LT(PA) gives p_B = p_A.

Exact controls:
- In M_tw both sides fail together [X s1 T3, T4]; in M_σ both hold [X s1 S1, T4 countercontrol].
- LT(PA) is load-bearing for (⇐). In the padding-type model (V = C × ℝ, a body point (w0, 1) that PB reads as w1 ≠ w0),
  TokProdState holds at height 0, tok fails at (w0, 1), and LT(PA) fails [W].

### 3.8 Pair level (rows 1–5)

- **hgate, hinv** [X s2 G1, G2].
  - Maximal body: idW passes the Lorentz pairings (1; 1/2; (1 + b·c)/4); the reduction of every effect to these is
    `lor_decomp` [K ES:449]. cnot idW = chainW takes the value −1/2 on the K2G:134 sharp pair.
  - Minimal body: F(ω) = ω₀₀ − ω₁₁ + ω₂₂ − ω₃₃ equals ½|x − Dy|² + ½(1 − |x|²) + ½(1 − |y|²) on products, and
    F(phiW) = −2.
  - Controls (spot values of the landed `cnot_prodState_mem_maxCone`) are nonnegative.
- **hcl** [X s2 C1–C3].
  - T_ψ is real, and pauliW(T_ψ) = |ψ⟩⟨ψ| has rank one.
  - det C(ψ) = −1/2 and C₀₀C₁₀ − C₀₁C₁₁ = 1/2, while that expression vanishes identically on CNOT(a ⊗ b).
  - So ψ is neither a product nor a CNOT image of a product. ψ is extreme in normalized Q3, so it is not in
    conv(SEP ∪ cnot SEP), and it is not interior; it is in cl(int Q3) ⊆ cl K_cl [W].
  - The foil satisfies the stated premises [W]: int Q3 ∪ C is convex for convex C ⊆ cl Q3; cnot fixes both parts; it
    contains SEP and lies in Q3 ⊆ maxCone.
- **hadm** [X s2 D1–D3]: Model.hom = Fin.cons 1 x = Matrix.vecCons 1 x = DIM-1 hom, and coeff = ehom. So the COMP-1
  model's maxBody at (ball3, ball3) = jointStates (eball 3), and COMP-1's bounds give CandidateCone ∧ IsConvexCone.
- **hcls**: EQ2-B's route, landed ingredients present [X s2 N]; see row 1.

## 4. Q2 — candidate sources of `TokenCoherent`, and whether any is present

| candidate source | present at the base? | evidence |
|---|---|---|
| Coherence of composition (associativity, symmetry) | No. COMP-1 has two factors over an arbitrary carrier; there is no associator, symmetry or composite-as-factor value. ORD-1's "composition order" is the order of iterated operations, not composite associativity. | [X s0 Q1b, Q1d]; [K CI:5, CI:54–55]; ORD-1 result |
| Token or site identity (substratum, regions) | Only in the complex region tower: sites are a `Finset ι`, observables are `Matrix (Conf Λ Q) (Conf Λ Q) ℂ`, and there is no path to the ball side. `CopyNatural` [K KF:284] identifies copies' NOTs only. MonoidalCompletion's H_comp / H-tensor sits on `Matrix A A ℂ` [K MC:193] and is an operation-level spectator principle. A route through any of these imports the complex matrix cone; through H_comp it is also (o)-type. | [X s0 Q1a, Q2b]; Kₙ census §1 |
| The observational protocol tower | No product or joint tower; only three control towers. A joint four-token tower with token-indexed product labels would give tok, local tomography, one body and closedness (`body` = closed convex hull, [K SC:141–142]) by construction. | [X s0 Q1e, Q2a]; SA-LEDGER §1, §5; K2-LEDGER D6 |

**Models of KT4 without `tok` (the protocol's sub-question).** EQ4-F's f1 W4 is a check on one functional, not a
model. Completed (M_T), it is a model of KT4LT minus tok and of every stated pair premise, with the conclusion true.
M_ρ and M_tw are models of every stated premise with the conclusion false. The anchor sum is a model of the
minimal-form KT4 minus tok for every quadruple. The architecture states no premise that relates the two groupings
beyond `one_body`, so all of these are models of its stated premises.

## 5. Q3 — the inequalities, the full-effect reading and the one-body clause

- **Given whatever the architecture supplies** (KT4 minus tok), the two families do **not** follow: the counterexamples
  are M_ρ, M_tw and the anchor sum.
- **Given KT4 including tok**, they follow by Lemma B1's route (§3.5). Its exact uses are listed there.
- **The full-effect reading.**
  - B1 reads `prodEff_effect` only at the rescaled dual-cone table functionals of the pair bodies, up to scale all
    effects of the pair body (entangled pair effects included).
  - This quantifier is COMP-1's own field [K CI:228–229 over `IsEffectOn`, KF:116]. Any `H : KT4` carries it, so it is
    supplied as the meaning of the (unsourced) four-token composite.
  - It is not an availability claim. EFF-1's Q-SET (CONDITIONAL-FULL-EFFECTS: one ball, needing the unit and
    `MixingClosed`) neither enters the route nor bears on pair-body effects.
  - The restricted reading is insufficient: restricting effects to Q3 lets K_F pass [X EQ3 p2 F3].
  - This agrees with EQ3-AUDIT §2.2.
- **The one-body clause** is supplied only vacuously (anchor sum). Combined with `tok` it carries the whole of FCC
  (§3.6).

## 6. Q4 — the pair-level premises against the landed rounds

| landed round | what it provides for rows 1–5 | supplies a row? |
|---|---|---|
| DIM-1 | `W d`, `NativeGate` (product-level positivity), `cnot`, `isNot_nflip`, `entangling_cnot`, `maxCone`, `jointStates` | No. These are the two-copy premise vocabulary and the instances used in the countermodels. |
| RELC-SELECT-1, PARITY-NOT-1 | `CtrlGate`, `dim_of_ctrlGate`, the block lemmas, `finrank_plus_eq_finrank_minus_relC`; N is a π-rotation at d = 3 | They provide ingredients of row 1's route, not N-CLASS itself. |
| K2-GUARD-1 | `CandidateCone` (definition), `no_candidateCone_cnot_reflY`, "Nothing here sources a cone" (K2G:27) | The definition of row 2's family only. |
| COMP-1 | the PreComposite bounds; `JointReversible` is only a definition (CI:445); min and max bodies | Row 2 by transport. Rows 4–5 are not implied: its own `ball3Min/MaxComposite` with `cnot` are countermodels. |
| K1-SHARP-TESTS-1, ODD-CHAR-1, NB-1, K1-BRIDGE-1, EFF-1, TRB-1 | d, sharp tests, the ball and its effect cone | No pair-cone statement. |
| KTRANS-DENSE-1 | a dense orbit suffices for the ball and the test cone; "does not concern whether the composite cone is closed" (result:59) | No. |

Summary:
- landed: none of rows 1–5;
- transported: row 2;
- unsourced: route for row 1, countermodels for rows 3–5.

This corrects EQ4-F's FORMAL §2. It labelled H-gate, H-inv and H-NCLASS "transported". In fact gate preservation and its
inverse are implied by no stated premise (landed countermodels), and N-CLASS is a derivation (route), not a premise.

## 7. Q5 — circularity

| route | steps | uses IE₁ / IE₂ / quantum cone / (o)? |
|---|---|---|
| anchor sum (§3.1) | (s) | no |
| Lemma B1 (§3.5) | (s) | no |
| FCC ⟺ ∃ KT4 (§3.6) | (s) | no |
| tok ⟺ TokProdState (§3.7) | (s) | no |
| N-CLASS (row 1, EQ2-B) | (2)/(s) on the standalone pair's gate premises | no |
| Theorem C (EQ4-F §6, cited) | (s) and (2) only, as audited | no |

The countermodels use Q3, PSD₁₆ and C_H as models only; that is not a use as a premise. Any route through the region
tower or MonoidalCompletion would import the complex matrix cone. Through H_comp it would also be (o)-type. None is
used.

## 8. Candidate premise formulations (proposals only; not adopted)

| candidate | statement (Lean-style sketch, UNBUILT) | relation to the package | disguised circularity? |
|---|---|---|---|
| **CP1 TokProdState** (product-preparation coherence) | `∀ x0 x1 x2 x3 ∈ eball 3, PA.prodState (flatW (prodState x0 x1)) (flatW (prodState x2 x3)) = PB.prodState (flatW (prodState x0 x2)) (flatW (prodState x1 x3))` | ⟺ `tok`, relative to KT4 minus tok + CandidateCone.1 + `lt` of PA (§3.7); not implied by `lt` (M_tw) | No. It is (s); it names no operation and presupposes no cone. Relative to the pair premises it is equivalent, through FCC (§3.6) and EQ3-AUDIT §4 [X+W], to IE₁ ∧ even 4-cycle parity. That is a derivation through (s) and (2) steps; IE₁ is not restated. |
| **CP2 four-token product data** | a multi-affine `prodState4 x0 x1 x2 x3` and multilinear `prodEff4 e0 e1 e2 e3` with the evaluation law, through which both groupings' product data factor | implies CP1 directly; it is the multi-factor form of COMP-1's `ProductData` (a Kₙ-type structural premise at the level of products) | No. It is (s). |
| **CP3 four-token joint stage tower** with token-indexed product labels | a `DirectedStages` whose labels are 4-tuples of single-token labels, read as the four-token body | gives `tok`, `lt`, one body and closedness [K SC:141–142] by construction; does not give KT's positivity (prodEff over entangled pair effects) | No. It is (s). It relocates the content into "which tests the joint stage contains" (K2-LEDGER D6). |
| **CP4 single-token marginal coherence (STMC)** | each token's marginal is the same through either grouping | implied by tok [W]; excludes M_tw and every local twist (Ψ = ⊗ g_t forces g_t = id) [W]; the simplest STMC-respecting nonlocal twist fails family (i) at −1/4 [E e1]; sufficiency for tok or for FCC is **open** | No. It is (s). |
| **CP5 (pair level)** | the native gate is a reversible operation of the standalone pair (COMP-1 `JointReversible` of the pair body); the pair body is a completed (hence closed) body | would supply rows 4, 5 and 3 | No. These are (2)-type and (s). They are EQ2/EQ3's transported premises, which the base does not state. |

## 9. What is not claimed (P/A/C rule)

- **No necessity.** No premise is claimed necessary. M_id and M_T show `tok` is not necessary relative to the rest.
  Every countermodel is a model of P′ ∧ ¬C, which shows insufficiency only.
- **Scope of the anchor sum.** It is for the minimal form `KT4` (no `lt`). For `KT4LT` minus tok, failure is shown for
  (Q3, Q3, Q3, twin) and for uniform quadruples. Whether `KT4LT` minus tok constrains the other quadruples is open.
- **Status of the routes.** The equivalences §3.6–§3.7 and the PSD steps are written arguments with exact ingredients.
  Nothing is kernel-checked.
- **Scope of the instance.** No claim is made about pairs 03 and 12, other groupings, KT(n) for other n, or KT∞.
- **Cited evidence.** EQ2-B's N-CLASS route, EQ3's C_H and the closure foil are cited, not re-derived. Their hashes
  were re-checked (§10).
- **Bands.** Consistency-axis work only; bands unchanged.

## 10. Evidence log (sha256, first 16 hex digits)

Scripts are run as `python3 -I -B` from this directory. Each `.err` holds only the appended `exit=N`. Replays are
byte-identical.

| script | sha | output | sha | checks | verdict | runs |
|---|---|---|---|---|---|---|
| `s0_census.py` | `a1c366ce4e47a0da` | `.out` | `f5b4c1a08cd0e228` | 12/12 | `S0-CENSUS-NO-MULTICOPY-STRUCTURE` | run 1 kept (`.run1.py` `2351ac7ebb63fc95`, `.out` `df64399e03a3f532`: 12/12, listing defect); run 2; replay identical |
| `s1_kt4_models.py` | `3c7b3c993b7d5527` | `.out` | `c0d3c490f42a46bb` | 35/35 | `S1-KT4-WITHOUT-TOK-MODELS-EXACT` | run 1; replay identical |
| `s2_pair_premises.py` | `fcf2c56b103ed2cc` | `.out` | `1815cb58c292e8e0` | 11/11 | `S2-PAIR-PREMISE-CORES-EXACT` | run 1 kept (`.run1.py` `758614309f7a4870`, `.out` `1a1aff85d991550a`, `.err` `cbbdff32232b45cf`: harness error, no verdict); run 2; replay identical |
| `e1_stmc_twist.py` (lead) | `8f7ed449ccbbd674` | `.out` | `73bd137b9965f487` | 3 controls | `LEAD STMC-TWIST-EXCLUDED` | run 1; replay identical |

Arguments:
- `s0`: `<base>/verification/lean-mathlib/OIBridge <eq5>/inputs`.
- `s1`: `<base>/…/OIBridge`.
- `s2`: `<base>/…/OIBridge /home/user/leanprover-community/mathlib4`.

Cited evidence; each hash was re-computed and matches its own record:

| evidence | file | sha (.py / .out) | record |
|---|---|---|---|
| C_H at −1/200 | EQ3 `p6_cheap_foils` | `0a162d371f34d6f3` / `d6263e18beb054f6` | EQ3 RESULT :354 |
| closure foil F4 | EQ3 `p2_audit_twists_foils` | `b8cff894baa4902b` / `401efe5ca778a00a` | EQ3 RESULT :350 |
| N-CLASS certificate | EQ2-B `b1_native_class` | `03c2417273d6097e` / `a9ccaf0ad1130dd0` | EQ2-B RESULT :233 |
| N-CLASS certificate | EQ2-B `b7_certificates` | `50916f3ca8cbf326` / `e3a07ef55ec56439` | EQ2-B RESULT :239 |

## 11. Integrity

- At start:
  - the base manifest (1317 entries) and the inputs manifest (6 entries) checked silent, exit 0;
  - HEAD `f0d37906` on `claude/network-tool-access-8jtdhm`, working tree clean;
  - `.start_marker` written.
- At end:
  - both manifests silent, exit 0; no `__pycache__` under the base;
  - HEAD unchanged at `f0d37906`, working tree clean, reflog top unchanged;
  - files newer than the start marker outside this directory lie only in `eq5/SIX/` and `eq5/F/`, the
    concurrent thread's and the coordinator's directories; none was written or read by this thread (NOTES N6).
- Writes: only `scratchpad/eq5/SOURCE/`.
