# HO-39 (v1) — bridge → origin, equivalence, countermodels: the sufficient bridge in the owner's form, with the transfer clause as an explicit third assumption; classification (C), provisional

**From** `research/bridge` (round 5, node B20; proposal HP-bridge-17). **To** `research/origin` (O14 and its round-6
follow-ups), `research/equivalence` (E19, E22) and `research/countermodels` (K(Z_F)). Written by the coordinator from the
source thread's committed record and the round-5 audits; version 1, 2026-10-11.

## Statements and labels

1. **The data and their pair availability** (B20-1; availability). OpDrive(θ₀) := `TokenAvailAt 𝓘 arch zPh n` for every
   `n` (`zPh = diag(1, w)`, `w = 3/5 + 4i/5`, the operator of `R_z(θ₀)`); the J-datum := `TokenAvailAt 𝓘 arch uJ n` for
   every `n` (`uJ = (1 − i(X + Y + Z))/2`). OI (I4.29, I4.30, I4.32) + {OpDrive(θ₀), the J-datum} ⇒ `PairAvailAt` of
   both at every level; each datum is exactly that pair availability. Label: CONDITIONAL (on the two data, introduced,
   not OI premises) — [D] (run 38124442150, `lean/BridgeOpDrive.lean`, 21/21 standard).
2. **The derived half** (B20-2; availability in, invariance out). OI (I4.32, I4.134) + {OpDrive(θ₀), the J-datum} +
   **(T)_𝓘** ⇒ (T) for `{R_z(θ₀), J}`: a pair cone `K ⊆ W 3` satisfying the class's transfer clause is invariant under
   `actT R_z(θ₀)` and `actT J` (`bridge_derived_half`). (T)_𝓘 — every admissible one-token unitary `U` of `𝓘` maps `K`
   into itself through `transferMap U = coordOf ∘ Ad(1 ⊗ U) ∘ dict` (`TransferClause`, BridgeDictionary [D];
   `transferClause_iff`, BridgeConverge [D]) — is the **third introduced item**, not an OI premise, and is a hypothesis
   of the built statement. Closure rules used: spectator, transport, discard, ray, block; no bind step, no limiting
   step. Label: CONDITIONAL (on the two data and (T)_𝓘) — [D].
3. **(T) cannot be omitted from this construction** — verified independently by the coordinator. The full class
   satisfies every other hypothesis of the derived half (I4.29 `fullClass_contextStable`, ImplementationLocality.lean:376
   [K]; I4.30 `fullClass_labelInvariant` :378 [K]; I4.32 `fullClass_arch` :518 [K]; I4.134
   `fullClass_unitaryRaySaturated`, MicroscopicReversibility.lean:323 [K]; both data, `fullClass_opDrive_jDatum` [D]),
   and K(Z_F) is moved by `actT R_z(θ₀)` and by `actT J` (exact certificates in `indep_checkB5.py` Z8). K(Z_F) contains
   every product, is self-dual and satisfies the 118 pair-level rows of the stage-6 inventory [A]. Note: (T) for the
   stated access holds at K(Z_F); (T) excludes something only together with a datum that makes a non-Clifford token
   unitary admissible.
4. **Exact availability, not density.** The chain needs the exact operators `zPh` and `uJ`. A dense subgroup gives
   membership of its own elements only; passing to invariance under `actT R_z(θ₀)` needs a closed cone (H3, introduced)
   and continuity [W], and gives invariance only. Neither built nor claimed.
5. **Exclusion, refutation, non-equivalence** (B20-3). The bridge's premises are jointly unsatisfiable at K(Z_F) (the
   exclusion lemma, certified pairings `−4/5`, `−1`); FM refutes both data; FM's `Q3` has both invariances with neither
   datum, so the bridge is not an equivalence. Label: CONJECTURE ([D] + [X]).
6. **Disguise test** (B20-4). OpDrive(θ₀) restates I2.33's phase intervention at θ₀ in availability form and I3.169's
   operational reading at θ₀; it is not (b) in disguise; it is H-T's token clause at level M.

## Is (T) derivable from the existing OI assumptions? (the coordinator's audit, AUDIT-BRIDGE-R5.md §9)

- No theorem at L derives (T) for any class or carries M-level availability to a P-level cone.
- (T) is not implied by the pair-level premises together with the derived half's other hypotheses (item 3).
- (T) for a class containing the drive implies (b) for the drive's flow, so a derivation of (T) from the complete
  stage-6 premise set would derive (b), whose full-model independence is OPEN. **Whether the complete existing OI
  framework implies (T) is OPEN**, not settled either way. Identifying the P-level pair cone with the M-level composite
  cone would supply (T), but that identification is `K = Q3`, the conclusion. The non-circular question — whether OI's
  operational semantics (available operations are admissible maps on the state space of every system they act on)
  applies to the P-level pair cone without identifying it with `Q3` — is carried to round 6.

## Cross-thread note from origin's O14 (AUDIT-ORIGIN-R5.md §8; HO-45)

At the balanced angle the drive is a limit of available channels and never available. That route cannot supply the
availability premise OpDrive(θ₀) of item 2. It gives invariance under the drive of every closed pair cone that is
invariant under every available **channel** of the class, which needs the transfer clause in channel form — (T^ch)_𝓘:
every available one-token channel `Φ` of `𝓘` maps `K` into itself through `coordOf ∘ (1 ⊗ Φ) ∘ dict` — and closedness of
`K`. The candidate alternative premise set {J-datum as the balanced mixer, (T^ch)_𝓘, `K` closed} trades the phase
intervention for a stronger transfer clause; it is [W] + [X] and not checked against `bridge_derived_half`.

## The owner's four claims, kept apart

| claim | status |
|---|---|
| a bridge from the existing OI assumptions alone | not established (items 1–2 use two introduced data and (T)_𝓘; at the audited scope FM excludes the drive) |
| a bridge using additional assumptions | items 1–2: CONDITIONAL [D] on {OpDrive(θ₀), the J-datum, (T)_𝓘}; candidate alternative {J-datum, (T^ch)_𝓘, `K` closed} [W] + [X] |
| (T) necessary for this construction | yes (item 3, verified counterexample) |
| (T) necessary for any derivation of quantum equivalence | not shown: QM satisfies (T) and (T^ch) for its own class, so every premise set deriving QM implies them; whether the complete OI framework implies (T) is OPEN |

**Classification.** B20 is **(C), provisional**; B14-6 as amended is (D) for the drive's availability at the scope of
Table A2's rows (HO-33 v2). Scope: insufficiency for the complete stage-6 inventory is definitive within that scope and
says nothing about every conceivable extension of OI. Nothing here treats the transfer clause as necessary for quantum
mechanics.

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `5ba9218e` (B20 written at `4b229b3d`) |
| proposal | `research/bridge/handoff-proposals/HP-bridge-17-sufficient-bridge-opdrive.md` (sha256 `1f0fa951…`) |
| module | `lean/BridgeOpDrive.lean` (sha256 `5d41b3f3…`; imports `BridgeToken`, `BridgeConverge` and the equivalence thread's `EqvK2Converse`, carried on the dev branch only); run 38124442150 |
| script | `experiments/b20_bridge.py` (`5b0e6e6d…`, P1–P5, run 2; run 1 kept), replay byte-identical |
| notes, results | `NOTES-B20.md` (`9694116b…`); `RESULTS.md` rows B20-1 … B20-4, V-5 |
| audits | `research/AUDITS/2026-10-11-round5/AUDIT-BRIDGE-R5.md` (§7 statement review, §9 the transfer clause, `bridge/indep_checkB5.py` run 2: Z1–Z12 PASS, CC1–CC7 False), `AUDIT-ORIGIN-R5.md` §8 |

## What the receiving threads may assume

Items 1–6 at their labels; the four-claims table as the standing record. **Origin:** a candidate principle that yields
`TokenAvailAt zPh n` and `TokenAvailAt uJ n` at every level, in a context-stable, label-invariant, unitary-ray-saturated
architecture, feeds item 2 directly; one that yields only a limit or a dense set needs item 4's premises, or the channel
form of the transfer, and gives invariance only. **Equivalence:** item 2's conclusion meets E19's A_miss through
`aMiss_of_transferClause` (HO-43).

## What they may not assume

- certification;
- (T) for `{R_z(θ₀), J}` from the data without (T)_𝓘;
- that OpDrive(θ₀) or the transfer clause is necessary for quantum mechanics, or that any alternative generating set is
  dense at a level;
- that any inventory item at L implies either datum (I4.60 implies the drive, outside Table A2: HO-33 v2);
- an equivalence between the data and the invariances.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-39 v1` and records in its `LOG.md`
whether and how it relies on it.
