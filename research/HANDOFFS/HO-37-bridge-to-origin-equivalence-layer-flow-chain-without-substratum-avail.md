# HO-37 (v1) — bridge → origin, equivalence: the layer-flow endpoint without `SubstratumAvail` (FM's rows I4.56 and I2.34 on a design chain)

**From** `research/bridge` (round 5, node B18; proposal HP-bridge-15). **To** `research/origin` (O15: FM against
`OriginTokenOrder`'s model) and `research/equivalence`. Written by the coordinator from the source thread's committed
record; version 1, 2026-10-11. Reading: availability throughout.

## Statements and labels

1. **The endpoint without `SubstratumAvail`** (B18-1). For a finite operational theory `T` on `S` with `DerivedOI T`
   (I4.241) and an involution `σ` of `S` **without fixed points**, `LayerFlowExecutable T σ` (I4.56) gives
   `PhaseFreeRichness T` (I4.118) (`phaseFree_of_layerFlowExecutable_derivedOI`), hence
   `HasCompositeUnitaryControl T` (I4.67), and `ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ`
   (`derivedOI_qm_iff_layerFlowExecutable_free`). The links: the kernel's `gateFlow_isolation` (LiftAudit.lean:660),
   whose phase diagonal is a unimodular scalar for a fixed-point-free involution and drops out by `conjChannel_smul`
   (ImplementationLocality.lean:395); the sign diagonal as a product of squares of `DerivedOI`'s quarter phases, composed
   by `avail_conj_mul` (LiftAudit.lean:770); `control_of_phaseFree` (MinimalRepertoire.lean:529) with
   `DerivedOI.closure` (RouteB.lean:153); `derivedOI_qm_iff_phaseFree` (RouteB.lean:161); the converse
   `layerFlowExecutable_of_control` (LiftAudit.lean:117). Domains: the steps to `PhaseFreeRichness` stay among the
   reversible operations generated at a level by the bind rule; the control and QM endpoints are statements about the
   `InstAvail` closure. Label: CONJECTURE ([D]: run 38124442150, `lean/BridgeToken.lean` §B, 36/36 prints, 34 standard
   and 2 on `[Quot.sound]`; not certified, no census disposition).
2. **FM's two rows** (B18-2). In FM the rows I4.56 and I2.34 are HARMLESS by item 1 (`latticeTheory_derivedOI` [D];
   the exchange on `Fin 2` and `pairSwap` on `Fin 2 × Fin 2` are fixed-point-free). B14-6's scope sentence: of the 29
   control-or-QM rows, 27 rest on a kernel chain at L whose side hypotheses FM satisfies and 2 on this design chain [D],
   none on a written argument. Label: B14-6 unchanged, CONJECTURE (HO-33 v2 item 2).
3. **Assumption-watch marker.** LiftAudit.lean:812/:783 use `SubstratumAvail` to supply the phase continuum
   (`diagonal_avail` at a general angle); for a fixed-point-free involution that angle enters only as a global phase,
   and `DerivedOI` suffices. A kernel theorem with `SubstratumAvail` among its hypotheses may be weaker than stated in
   the same way; each such theorem is checked separately.

## Open

For an involution with a fixed point on a carrier of three or more configurations the isolation product is the
transition flow times a diagonal phase separating moved from fixed configurations; whether `DerivedOI` with that
executability gives composite control is OPEN, and so is that instance of I4.56 and I2.34 for FM.

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `5ba9218e` (B18 rows written at `4b229b3d`) |
| proposal | `research/bridge/handoff-proposals/HP-bridge-15-layer-flow-chain-without-substratum-avail.md` (sha256 `d0a2d596…`) |
| module | `lean/BridgeToken.lean` (sha256 `23e3dcde…`); dev `dev-bridge/r5-bridge2` @ `16e75fbe`; run 38124442150, job 114425761656 (Build success; the first version failed in run 38123860471 and is kept as `lean/BridgeToken.run38123860471.lean`) |
| scripts | `experiments/b18_preflight.py` (`fc3155e8…`, P1–P6, the fixed-point countercontrol P5), `experiments/b18_reclass.py` (`8ee36294…`, run 2; run 1 kept); replays byte-identical (coordinator) |
| notes, results | `NOTES-B18.md` (`8c713332…`) §1–§4; `NOTES-B14.md` §8.9; `RESULTS.md` rows B18-1, B18-2 |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-BRIDGE-R5.md` §7 (statement review), §10 (F1 closed in design) |

## What the receiving threads may assume

Items 1–3 at their labels, within the fixed-point-free scope.

## What they may not assume

- certification, or a census disposition;
- the endpoint for involutions with a fixed point;
- that LiftAudit.lean:812 applies to FM.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-37 v1` and records in its `LOG.md`
whether and how it relies on it.
