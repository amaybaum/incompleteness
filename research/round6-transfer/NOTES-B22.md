# NOTES-B22 — the transfer clause's source, in both forms

Started 2026-10-11 15:35:49 UTC (S0-b items 1, 5). Base L = `9f9f8257`. Sources: the stage-6 inventory and Table A2
(`research/archive` @ `4dc0321c`), the kernel at L, the round-5 audits (`research/overview` @ `1325160c`), HO-33 v2,
HO-39, HO-43, HO-45 at their labels. Evidence levels as in the S0. No computation is run in B22: it is a sourcing
analysis. Its one Lean dependency, `BridgeChannelTransfer` (dev `fd364020`), is UNBUILT until run 38151796092 reports.

**The two forms.** (T)_𝓘: every one-token unitary `U` with `𝓘 (Fin 2) U` maps `K` into itself through
`transferMap U = coordOf ∘ Ad(1 ⊗ U) ∘ dict` (`TransferClause`, BridgeDictionary; `transferClause_iff`,
BridgeConverge [D]). (T^ch)_𝓘: every channel `Φ` with `InstAvail 𝓘 (Fin 2) Unit (fun _ => Φ)` maps `K` into itself
through `coordOf ∘ (1 ⊗ Φ) ∘ dict` (`ChannelTransferClause`), used with `K` closed. (T^ch) ⇒ (T): `InstAvail.op` makes
each admissible unitary's conjugation available (`unitaryTransfer_of_channelTransfer`).

**The question.** Does an existing inventory item, at its recorded status, connect the implementation-generated state
space to an arbitrary P-level pair cone `K` through the dictionary and yield (T) or (T^ch) — that is, does OI's
operational semantics ("available operations are admissible maps on the state space of every system they act on")
apply to the P-level pair cone without identifying it with `Q3`?

**Productivity test (§A.31), fixed at the start.** A gem iff B22 yields a fact strictly stronger than "no M→P theorem at
L" (AUDIT-BRIDGE-R5 §9) that constrains the transfer's possible sources or exposes a hidden assumption; otherwise
ELABORATING. **Expectation at the start** (written after the reconnaissance reads, so not blind): OPEN in both forms,
with the gap located at a named open obligation.

## 1. Where the operational semantics lives at L

- **I4.66 `CompositeOperationalValidity`** (OperationalValidity.lean:88; level M; status assumed, derived from
  implementation locality by I4.38 `validity_of_implementationLocality` [K], necessary for exact QM [K]; flag do not
  assume; bridge none at L): every available family at every level `n` maps positive semidefinite matrices of the
  carrier `A × Fin n` to positive semidefinite matrices and preserves the trace in aggregate. Its state spaces are the
  PSD cones of matrix carriers. "Every system they act on" ranges over matrix carriers; a pair cone `K ⊆ W 3` is not
  the state space of any carrier in that vocabulary.
- The only link from a matrix carrier to `W 3` is the dictionary (`dict`, `coordOf`), a design object [D]
  (BridgeDictionary, EqvK2Schema; R6 §6: "The M→P dictionary `pauliW` is [D] only"). Through it the kernel's pair state
  space, the PSD cone on `Fin 2 × Fin 2`, is `Q3`. So I4.66 reaches `K` only through an identification of the pair
  system's state space with `dict '' K`. `channelTransfer_of_identified_stateSpace` (restated at `fd364020`) makes
  that route exact: validity for pair-available channels on a set `C`, I4.29 and I4.30 for the spectator step
  (`instAvail_spectator`, ImplementationLocality.lean:789), and `hId : C = dict '' K` give (T^ch)_𝓘. At `C` = the PSD
  cone, I4.66 supplies the validity and `hId` is `K = Q3` — the target, excluded as a source (S0 line 29). For any
  other `C`, validity on `C` and `hId` are both introduced.
- **Exposed hidden assumption** (S0-b item 5): the module as committed at `5d4b9833` quantified validity over
  token-available channels while asserting it of their spectator extensions on the pair, which is validity on the pair
  only through `instAvail_spectator`, i.e. I4.29 `ContextStable` and I4.30 `LabelInvariant`. The restatement makes
  both explicit. Assumption-watch marker: any statement of validity or transfer "on the pair" quantified over
  token-available channels carries I4.29 and I4.30 (HO-45 item 6's "with a spectator, at every level" is such a
  statement; for `MixR {π/4}` the stabilities are the kernel's fixed-gate proofs cited by BridgeAvail §E,
  DiscreteCompletion.lean:1861, :1890 — not re-read here).

## 2. Candidate sources examined

| item | status at L | what it transfers | yields (T) / (T^ch)? |
|---|---|---|---|
| I3.165 K2, clause "local actions compatible with the composite cone" | open obligation (ROADMAP.md:1001); flag: the clause is (b), do not assume | the field-neutral form of (b): `K` invariant under the local actions | it is the transfer, in invariance form; usable only as an introduced assumption |
| I3.150 (b_S4), I3.151 (b_n), I3.152 (b_R1), I3.153 (b_DJ) | PT-record open; INDEPENDENT of H1–H3 at L; do not assume | invariance of `K` under one token's rotations (all, or named subgroups, or the drive with `J`) | (b_S4) gives (T)_𝓘 for every class (every unitary's transfer is the target action of its adjoint rotation: [D] for the generators used, `dict_actT_rotZ`, `dict_actT_nflip`, `dict_actT_cyc`; [W] in general) and (T^ch) for mixed-unitary channels by convexity [W]; it is the (b) target itself |
| I4.66, I4.38 (validity) | I4.66 assumed, do not assume; derived from implementation locality by I4.38 [K] | PSD → PSD on matrix carriers | only through `hId` (§1); at the PSD cone `hId` is `K = Q3` |
| K2-GUARD-1: I3.43 `CandidateCone`, I3.44 | I3.43 assumed (hypothesis of I3.44); I3.44 proved [K] | products in `K` and `K ⊆ maxCone (eball 3)`; I3.44 takes `actT reflY`-invariance as a hypothesis | no: an upper bound, no invariance |
| K1-BRIDGE-1: I3.35–I3.38 with EFF-1 (`maxConeOf_avail_eq`) | I3.37, I3.38 proved [K], premises unsourced | the availability of one copy's tests (effects) to the cone of available product tests, `= maxCone (eball d)` | no: tests, not operations; an upper bound |
| K1-SHARP-TESTS-1: I3.39–I3.41; I3.42 `prodState_mem_maxCone` | proved [K] (I3.40–I3.42) | single-token sharp-test multiplicity ↔ `2 ≤ d`; products nonnegative on product tests (O→P) | no |
| I4.60 `SubstratumAvail` (outside Table A2) | assumed, level H | availability (it implies OpDrive(θ₀), HO-33 v2) | no: availability only; reaches `K` only through a transfer clause |
| the 68 NOT REACHED rows; every item outside Table A2 | as recorded | bearing "none at L": no statement about a cone in `W 3` | only through a bridge L does not have |

Every landed result that carries an M- or O-level fact to pair cones transfers the availability of **tests** and yields
the upper bound `K ⊆ maxCone`; none transfers an **operation**, and none yields invariance (R6 §7: "the bridges B1/B2
reach only the upper bound `maxCone`, which every alternative respects").

## 3. The mandatory countercontrol: the full class with `K(Z_F)`, both forms

- The full class satisfies every hypothesis of `bridge_derived_half` except (T): I4.29 `fullClass_contextStable`,
  I4.30 `fullClass_labelInvariant` (ImplementationLocality.lean:376, :378 [K]), I4.32 `fullClass_arch` (:518 [K]),
  I4.134 `fullClass_unitaryRaySaturated` (MicroscopicReversibility.lean:323 [K]), both data (`fullClass_opDrive_jDatum`
  [D], run 38124442150) — HO-39 item 3, verified by the coordinator (AUDIT-BRIDGE-R5 §9).
- `K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F` contains every product, is self-dual [A] — hence closed (`isClosed_of_selfDual`
  [D]) — and satisfies the 118 SATISFIES rows of Table A2 [A]; it is moved by `actT R_z(θ₀)` (certified pairing
  `−1/10`) and by `actT J` (`−1/8`) [A + X: `indep_checkB5.py` Z8, run 2, replay identical].
- So (T)_fullClass fails at `K(Z_F)`, and (T^ch)_fullClass fails there as well, since (T^ch) ⇒ (T).
- The same pair satisfies every hypothesis of `bridge_channel_half` except (T^ch): `K(Z_F)` closed; the witness
  `AvailableChannelApproximation fullClass zPh` by the constant sequence `conjChannel zPh` (available by `InstAvail.op`:
  every operator is in the full class, `zPh_unitary` [D]; `channelTransfer_conjChannel` gives the limit); `J` available
  by `InstAvail.op` (`uJ_unitary` [D]). The conclusion fails at `K(Z_F)` [A + X].
- **Filter.** Every DERIVED chain for either form must use a hypothesis that (full class, `K(Z_F)`) fails. Within
  Table A2 these are exactly the 13 FAILS rows — I3.133, I3.135, I3.137, I3.142, I3.144, I3.150, I3.151, I3.152,
  I3.153, I3.155, I3.160, I3.161, I3.165 — none a theorem or a definition at L: each is a do-not-assume item, a [D]
  design hypothesis or a PT-record candidate (R6 §7) [A]. Items outside Table A2 make no statement about a cone in
  `W 3`. No chain found in §2 survives the filter except through I3.150–I3.153 or I3.165, i.e. through (b) assumed.

## 4. Verdicts — the owner's four claims, per form

**(T)_𝓘 (admissible unitaries).**

| claim | status |
|---|---|
| (i) from the existing OI assumptions at their recorded status | **OPEN** — no derivation: the inventory's only items whose content contains the transfer are I3.165's clause and the (b)-forms I3.150–I3.153, each open and do-not-assume; every other item either holds at `K(Z_F)` or makes no statement about a cone in `W 3`. Not an independence result: the full-model status of (b) and (T) is the bridge thread's B24 |
| (ii) with an additional assumption | CONDITIONAL on any one of: (T)_𝓘 itself, introduced (B20-2 [D]); (b_S4) I3.150, do not assume ([W]; [D] for the generators); the identification `K = Q3` (`transferClause_Q3` [D]) — the target, excluded as a source |
| (iii) necessary for this construction (`bridge_derived_half`) | yes: §3, [K] + [D] + [X] + [A] (HO-39 item 3) |
| (iv) necessary for any derivation of quantum equivalence | not shown: `Q3` satisfies (T) for every class, so every premise set that derives `K = Q3` entails (T) — a consequence of the target, not an independent necessary premise; not concluded from (iii) |

**(T^ch)_𝓘 (available channels; `K` closed).**

| claim | status |
|---|---|
| (i) from the existing OI assumptions at their recorded status | **OPEN** — as (T), and (T^ch) ⇒ (T) inherits the filter. OI's operational semantics (I4.66, with I4.38 [K]) is stated for the PSD state spaces of matrix carriers; it applies to a P-level pair cone only through `hId`, which at the kernel's own pair state space is `K = Q3`; no inventory item makes an arbitrary `K` the state space on which available operations act (I3.165's clause, open) |
| (ii) with an additional assumption | CONDITIONAL on: (T^ch)_𝓘 itself, introduced (`bridge_channel_half`, [D] pending run 38151796092); or a pair state space `C` with validity for pair-available channels and `hId : C = dict '' K`, with I4.29, I4.30 (`channelTransfer_of_identified_stateSpace`, [D] pending) — at `C` = PSD this is `K = Q3`, excluded; (b_S4) gives it for mixed-unitary channels only [W] |
| (iii) necessary for this construction (`bridge_channel_half`) | yes: §3 — (full class, `K(Z_F)`) meets closedness, the witness and `J`, and the conclusion fails [A + X; K for `InstAvail.op`; D pending]. Whether (T) can replace (T^ch) where the drive is only a channel limit (`MixR {π/4}`) is DEFERRED to round 7 (S0-b item 4, control (a)) |
| (iv) necessary for any derivation of quantum equivalence | not shown: `Q3` satisfies (T^ch) for every class (`channelTransfer_Q3`, [D] pending; CP maps preserve PSD, `cp_of_instAvail`, `cp_referencePositive` [K]) — a consequence of the target; not concluded from (iii) |

**What B22's channel-form verdict says for the placement** (the rest DEFERRED): HO-45's route needs (T^ch), whose
source is OPEN at the same place as (T) — I3.165's clause. HO-45's (B) placement stays provisional and B20's (C) stays
provisional; nothing here makes the channel route premise-free.

## 5. Passes (§A.31)

1. Skeptical, the favourable branch (an item that yields (T)): I4.66/I4.38 reach `K` only through `hId`; the test
   transfers (I3.35–I3.43, EFF-1) give an upper bound; I4.60 gives availability. No NEW.
2. Skeptical, the unfavourable branch (does §3 prove independence?): no — it forces any derivation through a FAILS row
   or an absent bridge; the full-model question is B24's. No NEW.
3. Cross-propagation: the spectator marker of §1 applies to every "on the pair" statement quantified over
   token-available channels. ELABORATING.

**Outcome.** OPEN in both forms, the gap located at I3.165's clause "local actions compatible with the composite cone"
(open, do not assume). Classification: ELABORATING (the location sharpens "no M→P theorem at L" but constrains nothing
new), with one exposed hidden assumption at statement level (I4.29, I4.30 in the identified-state-space lemma), recorded
as an assumption-watch marker. Not a gem.
