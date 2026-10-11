# Audit — `research/bridge`, round 5 (head `5ba9218e`)

Coordinator's audit of the bridge thread's round-5 report (nodes B18–B21, standing verdict V-5), from the round-4
head `a34d20b5`, against the certified base L = `9f9f8257`. Round 5 was narrowed by the owner at 10:38Z; the bridge had
already closed (10:32Z), so its scope is unchanged. Method as in rounds 1–4, plus the owner's round-5 checks and the
owner's direction of 10:38Z on the transfer clause (§9). Evidence levels: [K] kernel at L; [D] design module built in
CI on a disposable branch (not certified); [X] exact computation; [W] written; [A] audited record.

## 1. Receipts

HO-18 v2 and HO-27 … HO-32, copied into `inbox/` at `1eafec43`: 7/7 byte-identical to the overview's files at
`4c4a02b1`.

## 2. Provenance

- Six commits `a34d20b5..5ba9218e`, all by `Claude (research bridge)`; every changed path is under `research/bridge/`.
- Dev branches: `dev-bridge/r5-bridge` @ `36083b22` and `dev-bridge/r5-bridge2` @ `16e75fbe`, each one commit on L;
  changes only under `verification/lean-mathlib/` (the root import file and the design modules). The committed copies
  `lean/BridgeToken.lean` and `lean/BridgeOpDrive.lean` are byte-identical to the modules at `16e75fbe` (the green
  build). The carried modules are byte-identical to their sources: five to the round-4 `dev-bridge/r4-final` @
  `bf8ba746`, `EqvK2Converse` to `research/equivalence` @ `ab6788b9` (also the module of the green equivalence build
  `20c207f1`).
- The interruption of 08:34Z (`INTERRUPTION-2026-10-11.md`): all 17 uncommitted files of the record are byte-identical
  at `2c67f168`.
- Logged deviations, checked: the HO-36 hash mistyped in LOG and corrected forward; three timestamps corrected forward
  in LOG; `b21_ceq2` Q1's rule text changed after run 1 to the pre-registered form. For the last, the thread's
  transcript fixes the order: the S0 addendum stating Q1 for `CNOT U(u, v) h` was appended at 10:18:06Z, the script
  written at 10:19:42Z, run 1 at 10:19:44Z (kept as `b21_ceq2.run1.*`), the rule edit at 10:20:26Z, run 2 at 10:20:32Z.
  The correction restores the pre-registered check; it does not tune it.
- Observation: the same arithmetic slip — the pairing of two `c = 2` rank-one defects written `4(s − 1)` where it is
  `4s` — occurred independently in C22's preflight (countermodels) and B21's S0 (bridge, prediction S0-4); it does not
  come from any handoff (no handoff contains it), and both threads kept it as a failed prediction.

## 3. Replays

The six round-5 scripts replay byte-identically (stdout): `b18_preflight`, `b18_reclass`, `b19_preflight`,
`b20_bridge`, `b21_ceq2`, `b21_torus` (`REPLAY-r5.txt`). `b18_reclass` reads the archive's stage-6 tables and the
kernel by relative path; it was replayed with `research/archive/pt/` and `verification/lean-mathlib/OIBridge/`
exported from `5ba9218e` beside the experiments.

## 4. Independent check

`bridge/indep_checkB5.py`, decision rule fixed in its header before run 1; reads nothing the thread wrote; exact
(sympy). Run 2: **INDEP-B5-FIXED**, Z1–Z12 PASS, CC1–CC7 all False; replay identical. Run 1 is kept: Z8 failed on a
harness defect — the defect vector `ψ_s` was taken from the archive's formula, whose tensor-factor order differs from
this script's dictionary (`RUN-HISTORY.txt`); a design exploration before run 1 (`explore_J_family.py`, kept) had
already shown the two-term Bell family empty for `U_J`. What the check establishes, rebuilt from the definitions at L:

- **B18.** For every involution without fixed points tested (the exchange on `Fin 2 × Fin n`, `n = 1, 2, 3`; the
  exchange of the second token on `(Fin 2 × Fin 2) × Fin n`, `n = 1, 2`; 48 configuration/enumeration cases), the
  kernel's phase diagonal is the scalar `e^{−iπt}`, the isolation identity holds exactly, and `G·D·G·D` is a unimodular
  multiple of the transition flow; every sign diagonal is a product of squared quarter phases (Z1, Z2). Read at L:
  `PhasesAvailable` and `ExchangesAvailable` quantify over every state and pair at every level, `DerivedOI` carries them
  as its fourth and third conjuncts, `PhaseFreeRichness`'s exchange clause is implied, `conjChannel_smul` discards a
  unimodular scalar, `avail_conj_mul` has no `SubstratumAvail` hypothesis, and `diagonal_avail`, :783 and :812 do (Z3).
  Countercontrol: with a fixed point (`Fin 3`, swap(0, 1)) the kernel identity still holds but the phase diagonal is
  not constant and `G·D·G·D` is not proportional to the flow (Z4, CC1).
- **B19.** The discard over a uniformly attached two-level ancilla returns the conjugation; with the ancilla attached
  as `1₂` it returns twice it (Z5, CC2).
- **B20.** `w⁴ = (−527 − 336i)/625`, no power `≤ 1000` is 1, `U_J³ = −1` (Z6); through the dictionary
  `Ad(1 ⊗ diag(1, w)) = actT R_z(3/5, 4/5)` and `Ad(1 ⊗ U_J) = actT cyc` on all 16 basis tables (Z7); exact
  certificates that `K(Z_F)` is moved by both: for `R_z(θ₀)` a defect `e_s ∈ K` and the projector onto
  `(ψ_a + χψ_b)/√2` in `Q3 ∩ Z* ⊆ K*` pair to `−1/10 = −sin θ₀/8` (the stage-6 law); for `J`, the projector onto the
  defect's image ray (Bell overlaps all `1/4`) pairs to `−1/8` (Z8). The thread's values `−4/5` and `−1` are these with
  the unnormalized defect `I − 2P_s` (a factor 8). Countercontrols: the identity and `1 ⊗ X` move nothing in the same
  family (CC3, CC4). `R_z(θ₀)` has infinite order and does not commute with `cyc` (Z9, CC5).
- **B21.** `CNOT U(u, v) CNOT = U(u, −v)` in the `(u, v)` coordinates (not `U(v, u)`: CC6 — the S0 wording "swaps
  `u ↔ v`" holds only in B10's `(a, b)` coordinates, as the thread's results row records); `X_B` negates both; the
  orthogonal-pair identity symbolically and on the exact instance; the product-free seed and the countercontrol seed
  (Z10–Z12, CC7).

## 5. Citations

`cite_check_r5.py` over the thread's own added text (inbox copies of handoffs excluded; they were checked when
issued): 60 distinct kernel citations, 60/60 resolve at L. Four lines flagged by the window rule because they name
several identifiers were read by hand; each points at the intended definition (`phaseGate` :209,
`ExchangesAvailable` RouteB.lean:123, `PhasesAvailable` :128, `instAvail_transport` ImplementationLocality.lean:644).

## 6. CI

Two dispatches, verified at job and step level from the saved job logs (`CI-RUNS-R5.md`): `38123860471` @ `36083b22`
Build failure in `BridgeToken` (14 `sorryAx` prints, all from `diagonal_signFun_eq`'s errors); `38124442150` @
`16e75fbe` Build success, `BridgeToken` 36 (34 standard, two `_symm_apply` relabelling lemmas on `[Quot.sound]`),
`BridgeOpDrive` 21/21, carried modules standard, `lean-axioms` 6096 with no sorry, gate red only at `lean-manuscript`
(8 problems: the 8 design modules). None cancelled. Provenance as in round 4: tail-capped saved logs, not complete logs.

## 7. Lean statement review

- `phaseFree_of_layerFlowExecutable_free`: hypotheses — every sign diagonal and every exchange available at every
  level, `σ` involutive and fixed-point-free, `LayerFlowExecutable T σ`; conclusion `PhaseFreeRichness T`. The proof
  rewrites by the kernel's `gateFlow_isolation`, removes the scalar phase by `conjChannel_smul`, and composes by
  `avail_conj_mul`. No `SubstratumAvail`, no `diagonal_avail` (every occurrence of either name in the module is in a
  comment). `phaseFree_of_layerFlowExecutable_derivedOI` takes `DerivedOI T` and uses exactly its exchanges
  (`hd.2.2.1`) and quarter phases (`hd.2.2.2.1`). `derivedOI_qm_iff_layerFlowExecutable_free`: under `DerivedOI`, QM ↔
  executability of one fixed-point-free layer involution. Statements match B18-1. **F1 (round 4) is corrected in
  design**: the two rows now rest on a built chain whose side hypotheses FM satisfies; label CONJECTURE [D].
- `pairAvail_iff_tokenAvail` (B19-1): (C) and (L); `tokenAvail_of_pairAvail` takes (L) only. Matches.
- `BridgeOpDrive`: `OpDrive` and `JDatum` are explicit hypotheses of every theorem that uses them; no bind, limit,
  `diagonal_avail`, `SubstratumAvail` or `DrivesElementary` occurs outside comments. **`bridge_derived_half` takes
  `Architecture` (I4.32), `UnitaryRaySaturated` (I4.134), `OpDrive`, `JDatum` and `TransferClause 𝓘 K`**; context
  stability and label invariance enter only the pair-availability theorems, and the derived half reaches the class
  through token membership at level 1 (the ray step), not through pair availability — the thread's S0-7 confirmation
  records this correction.

## 8. Hypothesis classification (against the stage-6 inventory) and reading

B18: I4.241 (`DerivedOI`, assumed in general at L; FM [D]) and I4.56 (the row itself); nothing introduced; reading
availability. B19: I4.29, I4.30, I4.32; nothing introduced; availability. B20: inventory items I4.29, I4.30, I4.32,
I4.134; introduced: OpDrive(θ₀) (I2.33's phase intervention at the one angle θ₀, in availability form), the J-datum
(a non-monomial datum at `π/4`), and **(T)_𝓘**; reading availability in, invariance out. B21: CONDITIONAL on Lemma
C18-1 [W] (HO-31 item 3(a)); existence of an exotic `G`-invariant cone stays at claim (D) [A]; reading invariance.

## 9. The transfer clause (T)_𝓘 — the owner's direction of 10:38Z

**What (T)_𝓘 says.** For a class `𝓘` and a pair cone `K ⊆ W 3`: every admissible one-token unitary `U` of `𝓘` maps
`K` into itself through its transferred table, `transferMap U = coordOf ∘ Ad(1 ⊗ U) ∘ dict` (`TransferClause`,
BridgeDictionary [D]; `transferClause_iff`, BridgeConverge [D]). It is the link between the M-level description (which
operations a class makes available on matrix carriers) and the P-level object (a cone on the tables `W 3`).

**Is it an explicit third assumption?** Yes, in the thread's record and in the built statement: B20-2 is CONDITIONAL
on OpDrive(θ₀), the J-datum **and** (T)_𝓘, all three marked introduced; `bridge_derived_half` takes
`TransferClause 𝓘 K` as a hypothesis (§7). It is not folded into the OI premises anywhere in the round-5 text.

**The counterexample, verified independently.** The full class `fullClass` satisfies every hypothesis of the derived
half other than (T): I4.29 `fullClass_contextStable` (ImplementationLocality.lean:376 [K]), I4.30
`fullClass_labelInvariant` (:378 [K]), I4.32 `fullClass_arch` (:518 [K]), I4.134 `fullClass_unitaryRaySaturated`
(MicroscopicReversibility.lean:323 [K]), and both data (`fullClass_opDrive_jDatum` [D], printed standard in
`38124442150`). `K(Z_F)` is moved by `actT R_z(θ₀)` and by `actT J` (§4, Z8, exact; the thread's P3, replayed). So the
derived half fails at (full class, `K(Z_F)`) without (T): **(T) cannot be omitted from this construction**. The
counterexample is not merely formal: `K(Z_F)` contains every product (a product's overlap with a maximally entangled
`ψ_s` is at most `1/2`, so products lie in `Q3 ∩ Z*`) and is self-dual [A] (stage 3–4 audited record), and it
satisfies the 118 pair-level rows of the stage-6 inventory [A]. Note also that (T) alone excludes nothing:
(T) for the stated access holds at `K(Z_F)` (its transferred maps are the identity and `actT nflip`, which permutes
`Z_F`; round-4 X5); (T) bites only together with a datum that makes a non-Clifford token unitary admissible.

**Is (T) derivable from the existing OI assumptions?** What is established, and what is not:

- No theorem at L derives (T) for any class or carries M-level availability to a P-level cone ("no M→P theorem at L":
  B15-2, confirmed in the round-4 audit; the thread's round-5 inventory scan agrees) [A].
- (T) is not implied by the pair-level premises together with the derived half's other hypotheses: the full class with
  `K(Z_F)` satisfies the 118 pair-level rows, I4.29–I4.32, I4.134 and both data, and violates (T) [K] + [D] + [X] + [A].
- (T) for a class containing the drive implies (b) for the drive's flow, so a derivation of (T) from the complete
  stage-6 premise set would derive (b); the full-model independence of (b) is OPEN (V-4/V-5 (i): the 68 rows that do not
  reach the pair cone are undecided at `K(Z_F)`). **So whether the complete existing OI framework implies (T) is OPEN,
  not settled either way.**
- In the kernel's M-level vocabulary every theory has the Kronecker composite, whose pair cone is `Q3`, and `Q3`
  satisfies (T) for every class (`transferClause_Q3` [D], built in round 4). An identification of the P-level pair cone
  with the M-level composite cone would therefore supply (T) — but that identification is `K = Q3`, the cone
  conclusion itself (the thread's pressure test, NOTES-B20 §6). The non-circular question is whether OI's operational
  semantics — available operations are admissible maps on the state space of every system they act on — applies to the
  P-level pair cone without identifying it with `Q3`; if it does, (T) is a consistency requirement that OI supplies,
  not a new principle. That question is not decided by anything at L and is carried to round 6.

**The owner's four claims, kept apart.**

| claim | status after this audit |
|---|---|
| a bridge from the existing OI assumptions alone | not established (B20 uses two introduced data and (T)) |
| a bridge using additional assumptions (OpDrive(θ₀), the J-datum, (T)_𝓘) | CONDITIONAL [D] (B20-1, B20-2; built `38124442150`) |
| (T) is necessary for this particular construction | yes: not implied by the construction's other hypotheses, even with a cone satisfying the 118 pair-level rows (counterexample above, verified) [K] + [D] + [X] + [A] |
| (T) is necessary for any derivation of quantum equivalence | **not shown**. QM satisfies (T) for its own class, so any premise set that derives QM implies (T); whether the complete OI framework implies it, as a consistency requirement of its operational semantics, is OPEN |

**Outcome classification.** B20 stays at **(C) — provisional**: the drive is supplied by an assumption that is the phase
intervention at θ₀ (the disguise test, B20-4), and its carrying to the pair cone uses (T); the classification is held
open until origin's O14 (a different route to the drive or to the transfer) and the cross-thread checks are complete.
B14-6 as amended (B18-2) is **(D)** for the availability of the drive, within the stage-6 inventory and saying nothing
about every conceivable extension of OI.

## 10. Findings

- **F1 (round 4) — closed in design.** The two rows rest on the B18 chain [D]; LiftAudit.lean:812/:783 are not cited
  for FM; the fixed-point instances of I4.56 and I2.34 on carriers of three or more configurations stay OPEN for FM, as
  the thread records.
- **F-B5-1 — scope of "cannot be dropped" (B20-2, B20 §6).** Correct as a statement about this construction. The
  phrase "the inventory records no M→P theorem at L" is the absence of a derivation, not an independence result; the
  full-model status of (T) is OPEN with (b)'s. Recorded here; the thread's text already labels (T) introduced and
  keeps V-5 (i) OPEN, so no row needs a label change.
- No label changes. B18-1, B19-1 CONJECTURE [D]; B20-1, B20-2 CONDITIONAL [D]; B20-3 CONJECTURE ([D] + [X]); B21-1
  CONJECTURE ([X] + [W]); B21-2 CONDITIONAL on C18-1.

## 11. Carried to round 6 (bridge)

- (T): decide whether OI's operational semantics supplies the transfer to the P-level pair cone without identifying it
  with `Q3`; the full-model independence of (b) and of (T) (the 68 rows).
- The fixed-point instances of I4.56 and I2.34 for FM.
- B21: the `c = 2` and balanced surgery routes for the tower's closure (OPEN); claim (D).
- Handoff proposals HP-bridge-15 … 18 await issue at the round's close.
