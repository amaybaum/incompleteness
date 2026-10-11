# NOTES-B18 — the correction item of HO-33 (finding F1): FM's rows I4.56 and I2.34 without `SubstratumAvail`

Node B18 of `research/bridge` (round 5). Base L = `9f9f8257`. Evidence levels as in NOTES-B14: [K] kernel at L
(file:line checked at L in this tree, identical to L); [D] design module built in CI; [X] exact computation
(`experiments/b18_preflight.py`, `experiments/b18_reclass.py`); [W] written here; [A] audited record. Reading: every
statement of this node is an availability statement (operational availability through the kernel's protocols); none is
about the invariance of a pair cone. Received handoffs used at their labels (LOG, round 5): HO-33's correction item;
the round-4 audit's finding F1 (read-only).

## 0. Question

In FM's full-model classification (`experiments/b14_fullmodel.py`, NOTES-B14 §8.2) the rows I4.56
(`LayerFlowExecutable`) and I2.34 (the layer-flow form) were classed HARMLESS by the chain "with `DerivedOI`:
QM ⟺ `LayerFlowExecutable` [K] LiftAudit.lean:812 → QM". The cited theorem `derivedOI_qm_iff_layerFlowExecutable`
(LiftAudit.lean:812) has the hypothesis `SubstratumAvail T` (:745: every family available in the substratum theory is
available in `T`), which FM fails: the substratum theory makes `zPh` available and the lattice theory does not
(`lattice_strict_in_substratum`, BridgeAvailFull [D]). Its proof, `phaseFree_of_layerFlowExecutable` (:783), consumes
the hypothesis through `diagonal_avail` (:754) for the sign diagonal and for the phase diagonal `phaseFun` at a general
angle, and for the exchanges. So the two rows were HARMLESS by a written argument, not by the cited kernel chain, as
the round-4 audit found (F1). The round-4 audit's rule (now the coordinator's F1 rule): a chain of kernel theorems
applied to a model names the side hypotheses of every link and shows the model satisfies them; a link whose hypothesis
the model fails makes the chain a written argument, [W].

This node: supply a chain without `SubstratumAvail` as a design module if it is small; otherwise record the written
chain at [W]. Re-class the two rows; amend the verdict's scope sentence in NOTES-B14 §8.3 and RESULTS (a new row; the
old rows untouched). No label change is expected.

## S0. Design, productivity test and predictions (written 2026-10-11T07:39:54Z, before any run or dispatch)

**Design decisions.**
- **Where the kernel's chain uses the phase continuum, and why FM does not need it.** The kernel's isolation identity
  `gateFlow_isolation` (LiftAudit.lean:660) [K] writes the transition flow between a moved configuration `a` and its
  image `τ a` as `diagonal (phaseFun τ t) · G · (D · G · D)`, with `G = gateFlow τ t` the executable layer flow,
  `D = diagonal (signFun τ e a)` a diagonal of entries `±1`, and `phaseFun τ t` the diagonal that is `e^{−iπt}` on the
  moved configurations and `1` on the fixed ones. For an involution without fixed points — the exchange of the two
  values of `Fin 2`, and its lift `levelPerm σ n` to every level, where the ancilla is a spectator; likewise the
  exchange of the second token on the pair carrier `Fin 2 × Fin 2` — `phaseFun τ t` is the constant `e^{−iπt}`, so its
  diagonal is a unimodular scalar multiple of `1`, and a unimodular scalar drops out of conjugation
  (`conjChannel_smul` [K], ImplementationLocality.lean:395: `conjChannel (a • V) = (a · a*) • conjChannel V`). What the
  chain then needs of the theory is the executable flow (the row's own content), the sign diagonal `D`, and the
  exchanges — nothing at a general angle.
- **FM supplies the rest.** `D` is submonomial with entries `±1`, whose fourth powers are `1`: it lies on the lattice
  (`latticeClass`), and it is unitary; the exchanges are available at every level in FM (`ExchangesAvailable`, the third
  conjunct of `DerivedOI`, `latticeTheory_derivedOI` [D]).
- **The design lemma** (`BridgeToken.lean`, §B): `phaseFree_of_layerFlowExecutable_free`, for any finite operational
  theory `T` on `S`: if the conjugations by the `±1` diagonals and by the exchanges are available at every level, and
  `σ` is an involution of `S` without fixed points, then `LayerFlowExecutable T σ` gives `PhaseFreeRichness T`
  (MinimalRepertoire.lean:423). Its proof is the kernel's proof of :783 with the phase step replaced by the scalar step.
  From there the kernel's own chain runs with hypotheses FM satisfies: `control_of_phaseFree` [K]
  (MinimalRepertoire.lean:529; side hypothesis `IteratedAncillaClosure`, FM's `latticeTheory_closure` [D]) gives
  composite unitary control, hence every token unitary at every level (`zPh` and `uJ` among them) and, on the pair
  carrier, both pair operators (`pairAvail_of_control` [D]); `derivedOI_qm_iff_phaseFree` [K] (RouteB.lean:161; side
  hypothesis `DerivedOI`, FM's `latticeTheory_derivedOI` [D]) gives exact QM. The converse direction of I2.34's
  biconditional is the kernel's `layerFlowExecutable_of_control` [K] (:117) through `physical_of_exactAll` [K]. So FM
  gets the exact analogue of LiftAudit.lean:812 without `SubstratumAvail`: `ExactAllFiniteEndomorphicQuantumOps
  (latticeTheory S) ↔ LayerFlowExecutable (latticeTheory S) σ` for every fixed-point-free involution `σ`, in
  particular for `S = Fin 2`, `σ` the exchange (the token carrier, I4.56 at FM's level M) and for `S = Fin 2 × Fin 2`,
  `σ` the exchange of the second token (the pair carrier).
- **Scope of the design lemma.** Fixed-point-free involutions only. For an involution with a fixed point the phase
  diagonal is not a scalar (`e^{−iπt}` on the moved, `1` on the fixed configurations), and the chain is not claimed:
  FM's two rows concern the exchange, which has no fixed point at any level, so the scope covers them. The
  countercontrol P5 shows the hypothesis is load-bearing for the method.
- **The re-classification** (`experiments/b18_reclass.py`): the row table of `b14_fullmodel.py` is loaded unchanged
  (the round-4 script and its output stay as the round-4 record); the two rows' chains are replaced by the design chain
  — "`LayerFlowExecutable (latticeTheory (Fin 2)) (swap 0 1)` ⇒ [D] `PhaseFreeRichness` ⇒ [K] control ⇒ both token
  operators; QM ⟺ executability [D]+[K]" — and the classifier and controls C1–C5 are re-run; the scope sentence is
  generated from the measured counts (how many of the 29 control-or-QM rows rest on a kernel chain at L with side
  hypotheses FM satisfies; how many on a design-module chain; how many on a written argument). Decision rule: the two
  rows are HARMLESS by the design chain iff the module builds green with standard axioms in this round's dispatch;
  until then, and if it does not build, they are HARMLESS [W] (the audit's disposition) and the sentence says so.
- **No local Lean** (as in rounds 2–4). Every kernel name is read at L in this tree; every Mathlib name is read in the
  pinned sources (`leanprover-community/mathlib4` at tag `v4.33.0` = `db584cd6`, the rev the lakefile pins).

**Productivity test (§A.31), fixed now.** B18 is a gem iff the repaired chain yields a fact strictly stronger than
"the two rows are HARMLESS after all" that constrains something or exposes a hidden assumption — for example that
LiftAudit.lean:812's hypothesis `SubstratumAvail` is stronger than its proof needs for fixed-point-free involutions
(the phase continuum enters only as a global phase, which conjugation discards), so that the kernel's Q4′ endpoint
holds relative to a weaker baseline. Otherwise CONFIRMING. Expected: POSITIVE (the HARMLESS classification validated in
design) with that ELABORATING sharpening of the kernel hypothesis.

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | For `S = Fin 2`, `σ` the exchange and `n = 1, 2, 3`, `τ = levelPerm σ n` moves every configuration and `phaseFun τ t` is the constant `e^{−iπt}`; the same for the exchange of the second token on `Fin 2 × Fin 2` | P1, P6 (exact, symbolic in `t`) |
| S0-2 | The isolation identity rebuilt from the kernel's definitions (`unit`, `permMat`, `signFun`, `phaseFun`, `flow`, `transition`) holds symbolically in `t` for `n = 1, 2, 3`, and so does its scalar-free form `G · D · G · D = e^{iπt} · flow (transition a (τ a)) (π t)` | P2, P3 |
| S0-3 | `D` has entries `±1`, fourth powers `1`, and is unitary (on the lattice) | P4 |
| S0-4 | Countercontrol: for `S = Fin 3` and the exchange of `0, 1` (fixing `2`), `phaseFun` is not a scalar and `G · D · G · D` is not a scalar multiple of the transition flow | P5 |
| S0-5 | `BridgeToken.lean` §B builds: `phaseFree_of_layerFlowExecutable_free`, FM's `latticeTheory_phaseFree_of_layerFlow`, `latticeTheory_control_of_layerFlow`, `latticeTheory_qm_iff_layerFlowExecutable`, and the token and pair instances, every `#print axioms` line on `[propext, Classical.choice, Quot.sound]` | dispatch, job log |
| S0-6 | The re-class leaves the tally unchanged (SAT 34, HARMLESS 29, NA 5, HARMFUL 0; C1–C5 green); of the 29 control-or-QM rows, 27 rest on a kernel chain at L whose side hypotheses FM satisfies and 2 (I4.56, I2.34) on the design chain [D] + [K] once S0-5 holds | `b18_reclass.py` |
| S0-7 | No label change: B14-6 stays CONJECTURE ([D] + [A] + [W]); the verdict's scope sentence gains the count of S0-6 | §3 |
| S0-8 | Gem: POSITIVE, with the ELABORATING sharpening named in the productivity test | §4 |

### S0 addendum (written 2026-10-11T07:55:45Z, after the owner's round-5 directions, before any dispatch)

The owner's requirement (1) (LOG, 2026-10-11T07:55:45Z): the re-classification must rest on a chain whose every link's side
hypotheses FM satisfies — the quarter phase from `DerivedOI`, `avail_conj_mul`, the exchange's layer flow — and
LiftAudit.lean:812 and :783 are never cited for FM. The design above already uses no `SubstratumAvail` and no
`diagonal_avail`; one change makes the chain's side hypotheses exactly the owner's list: the sign diagonal `D` is
obtained **from `DerivedOI`'s quarter phases**, not from a class fact about FM. A diagonal with entries `±1` is the
product, over the configurations carrying `−1`, of the squares of the kernel's quarter phases `phaseGate p`
(`diag(1, …, i, …, 1)`, LieRankSource.lean:209), each available at every level by `PhasesAvailable` (the fourth
conjunct of `DerivedOI`, RouteB.lean:128); the products are available by `avail_conj_mul` [K] (LiftAudit.lean:770,
the kernel's sequential composition of two one-outcome interventions through `availExt_bind` and
`availExt_coarse` — the bind rule of HO-17 item 8); the empty product is the identity, available as the fourth
power of one quarter phase. The exchanges come from `ExchangesAvailable` (the third conjunct). So the design lemma
reads: for any finite operational theory `T`, **`DerivedOI T`** (I4.241) **and `LayerFlowExecutable T σ`**
(I4.56) **for an involution `σ` without fixed points give `PhaseFreeRichness T`** (I4.118)
(`phaseFree_of_layerFlowExecutable_derivedOI`), hence composite unitary control (I4.67, through
`control_of_phaseFree` [K] with `IteratedAncillaClosure` I4.68 from `DerivedOI`'s embedded observation I4.110
[K]) and exact QM (I4.70, through `derivedOI_qm_iff_phaseFree` [K]); and conversely, from `DerivedOI T`:
`ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ` (`derivedOI_qm_iff_layerFlowExecutable_free`) —
the exact analogue of LiftAudit.lean:812 with `SubstratumAvail` replaced by the fixed-point-free hypothesis. FM's
instances (`latticeTheory_derivedOI` [D]) follow with no FM-specific fact beyond `DerivedOI`. The `hsign`/`hswap`
form of the lemma (the sign diagonals and exchanges available) is kept as the core statement, and the DerivedOI form
is derived from it. Kernel closure rules used in the chain, named: bind (`avail_conj_mul`), nothing else at the
level of availability — the spectator, transport and discard rules do not enter B18. Prediction S0-5 now names the
DerivedOI form as the module's statement; S0-6's "design chain [D] + [K]" reads "the DerivedOI chain: [D]
`phaseFree_of_layerFlowExecutable_derivedOI`, [K] `control_of_phaseFree`, `derivedOI_qm_iff_phaseFree`,
`layerFlowExecutable_of_control`, `physical_of_exactAll`, `avail_conj_mul`, `gateFlow_isolation`,
`conjChannel_smul`, `closure_of_embeddedObservation`, and FM's `latticeTheory_derivedOI` [D]". The predictions'
content is otherwise unchanged. Added prediction: S0-9 — the quarter-phase product reproduces every `±1` diagonal
exactly (`b18_preflight.py` is not re-run; the identity `phaseGate p · phaseGate p = diag(1, …, −1, …, 1)` is
checked in `b18_reclass.py`'s control C8 on `Fin 2 × Fin n`, `n = 1, 2, 3`).

### Second S0 addendum (written 2026-10-11T08:07:01Z, after the owner's further distinctions, before any dispatch)

**Domains** (the owner's distinction (1)). The chain `LayerFlowExecutable ⇒ PhaseFreeRichness`
(`phaseFree_of_layerFlowExecutable_free` and its `DerivedOI` form) lives in the reversible operations generated at
each level by the bind rule on conjugations: every operation it forms is a finite product of available unitaries —
the executable layer flow, the quarter phases and their squares, the sign diagonal as such a product
(`signDiag_avail_of_phases`), and the isolation product `G · (D · G · D)` (`avail_conj_mul`, LiftAudit.lean:770,
which composes two one-outcome conjugations through `availExt_bind` and `availExt_coarse` into the conjugation by
the product, `conjChannel_comp_conjChannel`); no ancilla is attached or discarded, and the scalar phase is discarded
by the identity `conjChannel (c • M) = conjChannel M` for `|c| = 1`, not by a protocol. The next link,
`PhaseFreeRichness ⇒ HasCompositeUnitaryControl` (the kernel's `control_of_phaseFree`, MinimalRepertoire.lean:529),
lives in the InstAvail closure with ancillas and discard: on carriers with three or more states it is the positive
reachability theorem at the level (reversible compositions), and on smaller carriers it descends from level `3n`
through `IteratedAncillaClosure` (I4.68, the kernel's `descend`: attach, act, discard, with `discard_tensorOf_one`
returning a conjugation) — for FM's token carrier `Fin 2` at level `n = 1` this descent is used. The endpoint
`derivedOI_qm_iff_phaseFree` [K] is a statement about the theory's full availability. So: the design lemma is a
reversible-group statement; the control and QM endpoints are InstAvail-closure statements, exactly as the kernel's own
LiftAudit.lean:812 is. Recorded in every RESULTS row of B18.

## 1. Outcome (written 2026-10-11T10:24:11Z)

**The runs.** `b18_preflight.py` run 1 (07:45:20Z) 6/6, VERDICT B18-PREFLIGHT-OK, replay byte-identical (07:57:57Z).
`lean/BridgeToken.lean` §B: dispatch 1 (run 38123860471, dev `36083b22`) failed in two local elaboration errors of §B
(`signDiag_empty`: `congr 1` already closed the goal; `diagonal_signFun_eq`: an `if_neg` term without a type ascription),
the failed text kept as `lean/BridgeToken.run38123860471.lean`; the repair changed no statement. Dispatch 2 (run
38124442150, dev `16e75fbe`, job 114425761656): "Built OIBridge.BridgeToken (3.2s)", 36/36 `#print axioms` lines standard
(34 on `[propext, Classical.choice, Quot.sound]`, two `rfl` lemmas on `[Quot.sound]`), no `sorryAx`, `lean-axioms` PASS
(6096); the gate red only on `lean-manuscript` (the eight design modules have no census disposition, identified locally;
LOG 10:11:59Z). `b18_reclass.py` run 1 (08:09:47Z, `DESIGN_BUILT = False`, kept as `.run1.*`) and run 2 (08:32:37Z,
`DESIGN_BUILT = True` after the green build), each replayed byte-identically. The rule of `b18_reclass.py` was written
after the reading 08:07:01Z, not at the 08:06:00Z its header states (LOG, timestamp corrections).

| id | outcome |
|---|---|
| S0-1 | confirmed [X]: P1 (levels 1–3: every configuration moved, `phaseFun` the single value `e^{−iπt}`), P6 (the pair carrier with the second token's exchange) |
| S0-2 | confirmed [X]: P2, P3, symbolic in `t`, levels 1–3 |
| S0-3 | confirmed [X]: P4 |
| S0-4 | confirmed [X]: P5 — with a fixed point (`Fin 3`, the exchange of `0, 1`) `phaseFun` takes two values; the kernel identity still holds with the phase; the scalar-free form fails (`(0, 1)` entry of the difference `1 + i` at `t = 1/2`) |
| S0-5 | confirmed at dispatch 2 [D] (above), in the `DerivedOI` form of the S0 addendum; failed at dispatch 1 for two elaboration errors, no statement changed |
| S0-6 | confirmed [X]: tally SAT 34 / HARMLESS 29 / NA 5 / HARMFUL 0, C1–C8 PASS; 27 rows on kernel chains at L, 2 (I4.56, I2.34) on the design chain [D], none on a written argument — within the scope stated below |
| S0-7 | confirmed: B14-6's label unchanged, CONJECTURE ([D] + [A] + [W]); its [W] now comes only from the written arguments among the 34 SAT rows (NOTES-B14 §8.1, S0-17), none from the 29 HARMLESS rows |
| S0-8 | confirmed: POSITIVE with the ELABORATING sharpening (§4) |
| S0-9 | confirmed [X]: C8 (every `±1` diagonal on `Fin 2 × Fin n`, `n = 1, 2, 3`, is the product of quarter-phase squares over its `−1` positions; `phaseGate⁴ = 1`) |

## 2. The chain, link by link (the F1 rule)

`derivedOI_qm_iff_layerFlowExecutable_free` [D]: for a finite operational theory `T` on `S` with `DerivedOI T`
(I4.241) and an involution `σ` of `S` without fixed points, `ExactAllFiniteEndomorphicQuantumOps T ↔
LayerFlowExecutable T σ`. Links, each with its side hypotheses and FM's discharge:

| link | statement | side hypotheses | FM |
|---|---|---|---|
| 1 | `signDiag_avail_of_phases` [D]: every `±1` diagonal available at every level | `PhasesAvailable T` (the fourth conjunct of I4.241, RouteB.lean:128) | `latticeTheory_derivedOI` [D] |
| 2 | `diagonal_phaseFun_free` [D]: the kernel's phase diagonal is a unimodular scalar | `σ` (hence `levelPerm σ n`) without fixed points | the exchange on `Fin 2`; `pairSwap` on `Fin 2 × Fin 2` [D] |
| 3 | `phaseFree_of_layerFlowExecutable_free` [D]: the kernel's `gateFlow_isolation` (LiftAudit.lean:660 [K]), the scalar removed by `conjChannel_smul` (ImplementationLocality.lean:395 [K]), three bind steps `avail_conj_mul` (LiftAudit.lean:770 [K]) ⇒ `PhaseFreeRichness T` (I4.118) | the sign diagonals (link 1); `ExchangesAvailable T` (the third conjunct of I4.241, RouteB.lean:123); `LayerFlowExecutable T σ` (I4.56, the row itself) | as links 1–2 |
| 4 | `control_of_phaseFree` [K] (MinimalRepertoire.lean:529) ⇒ `HasCompositeUnitaryControl T` (I4.67) | `IteratedAncillaClosure T` (I4.68), from I4.241's embedded observation I4.110 (`DerivedOI.closure`, RouteB.lean:153 [K], which is `closure_of_embeddedObservation`, EmbeddedObservation.lean:211 [K]) | `latticeTheory_derivedOI` [D] |
| 5 | `derivedOI_qm_iff_phaseFree` [K] (RouteB.lean:161) ⇒ QM (I4.70) | I4.241 | as above |
| 6 | the converse: `layerFlowExecutable_of_control` [K] (LiftAudit.lean:117) through `physical_of_exactAll` [K] (PhysicalCharacterization.lean:301) | none beyond QM | — |

No link uses `SubstratumAvail`, `diagonal_avail` or `DrivesElementary`, and LiftAudit.lean:812/:783 are cited only as
the chain replaced. FM's instances: `latticeTheory_token_qm_iff_layerFlow` and `latticeTheory_pair_qm_iff_layerFlow`
(the biconditional of I2.34 on the token and on the pair carrier), `layerFlow_supplies_token` (an executable exchange
flow would give both token operators at every level) and `layerFlow_supplies_pair` (both pair operators), with
`latticeTheory_token_not_layerFlow` and `latticeTheory_pair_not_layerFlow` (both sides false in FM) [D].

**Domains** (the owner's distinction (1)). Links 1–3 are statements about the reversible operations generated at each
level by the bind rule on conjugations: every operation formed is a finite product of available unitaries, no ancilla
is attached or discarded, and the scalar is removed by an identity of channels, not by a protocol. Links 4–6 are
statements about the InstAvail closure with ancillas and discard: `control_of_phaseFree` descends from level `3n`
through `IteratedAncillaClosure` (attach, act, discard, with `discard_tensorOf_one` returning a conjugation), which FM's
token carrier `Fin 2` uses. **Kernel closure rules used**: bind (`avail_conj_mul`) in links 1 and 3; the ancilla descent
inside the kernel's link 4; no spectator or transport step.

**Hypotheses, classified.** I4.241 (`DerivedOI`): inventory item, assumed at L, holds for the substratum theory [K] and
for FM [D]. I4.56 (`LayerFlowExecutable`): the row being classified. The fixed-point-free condition on `σ`: a condition
on the involution, not an availability. No introduced hypothesis.

**Scope.** The chain covers involutions without fixed points. On FM's token carrier `Fin 2` the only involution that
moves a configuration is the exchange, so there the two rows are covered completely. On a carrier with three or more
configurations, an involution with a fixed point (the controlled exchange on `Fin 2 × Fin 2`, for one) is covered by
neither LiftAudit.lean:812 (FM fails `SubstratumAvail`) nor the design chain: there the isolation product
`G · D · G · D` is the transition flow times a diagonal phase that separates the moved from the fixed configurations
(P5), and whether `DerivedOI` with that executability gives composite control is **OPEN**. The row classification of
B14-6 reads I4.56 and I2.34 at the exchange (round-4 reading, kept); the OPEN instance is recorded with the amended scope
sentence (NOTES-B14 §8.9).

**Reading.** Availability throughout; no statement of this node concerns a pair cone.

## 3. Comparison with the route sketched in the round-5 node list

The node list (research/overview @ `51cce8ac`, OVERVIEW.md, round 5) sketched: for `S = Fin 2` and the exchange, the
executable layer flow is an `R_x`-type flow at every level, and with the quarter phase and `avail_conj_mul` the
generated group is the token's unitary group, so `TokenAvailAt zPh`. That route also avoids `SubstratumAvail`, and it
needs no density: up to a global phase every token unitary is an exact product `R_x(α) R_y(β) R_x(γ)` (Euler angles),
`R_x` the flow at a time and `R_y` its conjugate by the quarter phase, each available by the bind rule [W, not built].
It is specific to the token carrier. The built chain goes through the kernel's own isolation
identity to `PhaseFreeRichness` and the kernel's `control_of_phaseFree`, so it gives composite unitary control on every
carrier with a fixed-point-free involution (the pair carrier included) and the QM endpoint — the analogue of
LiftAudit.lean:812 — at the price of the fixed-point-free scope above. Both routes are exact; neither invokes a closure
or limiting step.

## 4. Gem classification (§A.31)

**POSITIVE** — the HARMLESS classification of I4.56 and I2.34 in FM is validated by a chain whose every link's side
hypotheses FM satisfies, kernel-checked in design. **ELABORATING** sharpening, as predicted: the kernel's endpoint
LiftAudit.lean:812 holds with `SubstratumAvail` replaced by `DerivedOI` alone for involutions without fixed points
(`derivedOI_qm_iff_layerFlowExecutable_free` [D]); `SubstratumAvail` supplies the phase continuum, which for such an
involution enters the isolation identity only as a global phase. Assumption-watch marker, cross-propagated: a kernel
theorem with `SubstratumAvail` among its hypotheses may use it only through `diagonal_avail` at a general angle; where
that angle enters as a global phase, `DerivedOI` suffices (for :812 the involution must be fixed-point-free; the
fixed-point case is OPEN). Not NEW: the fact that FM fails `SubstratumAvail` was the round-4 audit's (F1).

## 5. Manuscript obligations

None applied (manuscript hold). Recorded for the coordinator: GR.md:262–268 states I2.34's biconditional with the
substratum's phase continuum among its premises; a version with `DerivedOI` for a fixed-point-free involution exists in
design only.
