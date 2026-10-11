# NOTES-B20 — the sufficient bridge in the owner's form, and its disguise test

Node B20 of `research/bridge` (round 5). Base L = `9f9f8257`. Evidence levels as in NOTES-B14. Readings are stated
statement by statement: the premises and the pair-availability conclusions are availability statements; the cone
conclusions are invariance statements. Inventory ids are the stage-6 inventories' (`research/archive/pt/I1–I4/
INVENTORY.md` at `4dc0321c`, hashes in the round-4 LOG). Received handoffs used at their labels (LOG, round 5): HO-29
items 1–3; HO-31 items 1–2; HO-32 items 1–5; HO-18 v2 item 1; HO-27 items 1–3 as context.

## 0. Question

The owner's central question: what is the weakest independently justified principle that excludes the established
non-quantum countermodels and supplies the missing composite operations, without assuming quantum mechanics itself.
The round-5 directive, in the kernel's vocabulary: define

- **OpDrive(θ₀)** := `TokenAvailAt 𝓘 arch zPh n` for every `n` — K∞-Drive's operational reading at `θ₀`
  (`cos θ₀ = 3/5`; B14-7): the conjugation by the token operator `diag(1, w)`, `w = 3/5 + (4/5)i`, of `R_z(θ₀)` is
  available on the token alone at every level;
- **the J-datum** := `TokenAvailAt 𝓘 arch uJ n` for every `n` — the conjugation by `U_J = (1 − i(X + Y + Z))/2`, the
  operator of `J = cycEquiv`, available on the token alone at every level;

and prove in design, for a context-stable, label-invariant architecture: OI (the inventory items actually used, by id)
+ {OpDrive(θ₀), the J-datum} ⇒ `PairAvailAt` of both at every level (B19) ⇒ the transfer clause in table form for the
clause's two operations (`transferClause_iff` of BridgeConverge; the tables `actT (rotZ (3/5) (4/5))` and
`actT cycEquiv` through `dict_actT_rotZ_345` and the cycEquiv intertwining) — the derived half of the bridge,
availability ⇒ invariance. Record that FM refutes OpDrive(θ₀) (`lattice_refutes`) and that K(Z_F) violates it
(B10-2: (A) fails at `−2/5`), so that the bridge excludes K(Z_F) by the owner's criterion. Disguise test: name
exactly which inventory item OpDrive restates, and decide whether it is (b) in disguise or an instance of OI⁺-1 at
level H (H-T's token clause). State the result as "OI + {OpDrive(θ₀), J-datum} ⇒ (T) for {R_z(θ₀), J}", every
hypothesis classified, labels as the evidence gives; no equivalence claimed (objective 3).

## S0. Design, productivity test and predictions (written 2026-10-11T07:39:54Z, before any run or dispatch)

**Design.**
- **Module** `lean/BridgeOpDrive.lean`, importing `BridgeToken` (B19), `BridgeConverge` (B15: one dictionary, the
  transfer clause in table form) and the equivalence thread's `EqvK2Converse` (HO-29 item 2: the cycEquiv intertwining
  `dict_actT_cyc` and `Q3_aMiss`), read at `research/equivalence` @ `ab6788b9` (LOG) and carried verbatim with
  attribution on the dev branch only.
- **The definitions.** `OpDrive 𝓘 arch := ∀ n, TokenAvailAt 𝓘 arch zPh n`; `JDatum 𝓘 arch := ∀ n, TokenAvailAt 𝓘 arch uJ n`.
- **Pair availability** (`pairAvail_of_opDrive`, `pairAvail_of_jDatum`; reading: availability): under (C) I4.29 and
  (L) I4.30, by B19's `pairAvail_of_tokenAvail`; and conversely (`opDrive_iff_pairAvail`), by B19's other direction.
- **Membership at the token carrier** (`exists_scaled_mem_of_tokenAvail`, `mem_of_tokenAvail`; reading:
  availability). From `TokenAvailAt 𝓘 arch U n` at a positive level: the kernel's ray step
  `exists_scaled_mem_of_instAvail_unitary` [K] (MicroscopicReversibility.lean:251; hypothesis: the architecture I4.32)
  puts a nonzero multiple of `tokOp U n = U ⊗ 1ₙ` into the class at `Fin 2 × Fin n`; the architecture's `block`
  clause (I4.32) extracts the `(0, 0)` ancilla block, `c • U`, into the class at `Fin 2`; unitary-ray saturation
  (I4.134, `UnitaryRaySaturated`, MicroscopicReversibility.lean:238) gives `𝓘 (Fin 2) U`.
- **The two table identities** (`transferMap_zPh`, `transferMap_uJ`; reading: a dictionary fact). `zPh = zPhase (3/5)
  (4/5)` and `uJ = cycMat` exactly; by the injectivity of the one dictionary (B15 [D]), `transferMap zPh ω =
  actT (rotZ (3/5) (4/5)) ω` (`dict_transferMap` and `dict_actT_rotZ_345`, BridgeDictionary [D]) and
  `transferMap uJ ω = actT cycEquiv ω` (`dict_actT_cyc`, EqvK2Converse [D]).
- **The derived half** (`transfer_of_opDrive`, `transfer_of_jDatum`, `bridge_derived_half`; reading: the conclusion is
  invariance). For a pair cone `K ⊆ W 3` satisfying the class's transfer clause `TransferClause 𝓘 K` (B9-1, B15-1):
  with `𝓘 (Fin 2) zPh` from the membership step, `transferClause_iff` gives `transferMap zPh ω ∈ K` for `ω ∈ K`,
  i.e. `actT (rotZ (3/5) (4/5)) ω ∈ K`; likewise `actT cycEquiv ω ∈ K`. At the kernel's own pair cone `Q3` the two
  invariances hold with no hypothesis at all (`Q3_two_invariant`: `Q3_phase_invariant` [D], `Q3_aMiss` [D]), as
  `transferClause_Q3` already says for every class — the control that the derived half is non-vacuous and that the
  transfer clause is where the pair cone enters.
- **Refutations and controls** (reading: availability). FM refutes both data (`latticeClass_not_opDrive`,
  `latticeClass_not_jDatum`, from `lattice_refutes` [D]); the monomial interface satisfies OpDrive(θ₀) and refutes the
  J-datum (`substratum_tokenAvail_zPh`, `monomialInterface_split` [D]); the full class satisfies both. The exclusion
  lemma (`not_opDrive_of_moved`): a pair cone satisfying the class's transfer clause and moved by
  `actT (rotZ (3/5) (4/5))` refutes OpDrive(θ₀) for that class — K(Z_F)'s instance is exact (P3).
- **The exact script** `experiments/b20_bridge.py` (sympy, exact): (P1) the operator identities and unitarity, `w⁴ ≠ 1`;
  (P2) the two transfer identities on the 16 basis tables of `W 3`, through the coordinate map; (P3) K(Z_F) is moved
  by both operations on the target: a certified member of K(Z_F) and a certified member of its dual pairing negatively
  with the image under `actT R_z(θ₀)`, and likewise under `actT J`, with a `Q3` control (the same witnesses pair
  nonnegatively with the images of Bell projectors); (P4) `R_z(θ₀)` has infinite order and the two transferred tables
  do not commute (the group they generate with the gate is infinite and non-abelian, as B12-3 and HO-31 item 1 need);
  (P5) a positive control for the membership step: the `(0, 0)` ancilla block of `c · (U ⊗ 1ₙ)` is `c · U`.
- **Disguise test**, run in §3 on the statement OpDrive(θ₀) exactly as defined.
- **No local Lean**; every kernel name read at L in this tree, every Mathlib name in the pinned sources.

**Productivity test (§A.31), fixed now.** B20 is a gem iff the bridge in the owner's form yields a fact strictly
stronger than the restatement of B14-3 and B14-7 ("OpDrive is the phase intervention at `θ₀`; `J` needs a non-monomial
datum") that constrains the sourcing of a bridge or exposes a hidden assumption — the candidate fixed now: that H-T's
second component, (A), is inside the kernel's vocabulary an inventory item at L (I4.29, context stability) rather than
an introduced hypothesis, so that the only introduced content of a sufficient bridge is token-level, and that the pair
cone on `W 3` is reached from availability only through the transfer clause (T), which stays introduced. If both hold,
POSITIVE (an inheritance validated: B14-4's "a sufficient bridge must add a token-level resource and carry it to the
pair cone" sharpened to "…and the carrying is (T), nothing else"); otherwise ELABORATING.

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | `zPh = zPhase (3/5) (4/5)` and `uJ = cycMat` exactly; both unitary; `w⁴ = (−527 − 336i)/625 ≠ 1` | P1; module (`zPh_eq_zPhase`, `uJ_eq_cycMat`) |
| S0-2 | On the 16 basis tables, `coordOf (Ad(1 ⊗ zPh)(dict E)) = actT (rotZ (3/5) (4/5)) E` and `coordOf (Ad(1 ⊗ uJ)(dict E)) = actT cycEquiv E` | P2; module (`transferMap_zPh`, `transferMap_uJ`) |
| S0-3 | K(Z_F) is moved by `actT R_z(θ₀)` and by `actT J`: certified witnesses with negative pairings (the values printed; for `R_z(θ₀)` with the Bell-projector witness family the flow law of B8 X3 gives `−s = −4/5` on the target at `(3/5, 4/5)`); the `Q3` control passes | P3 |
| S0-4 | `R_z(θ₀)` has infinite order (`2 cos θ₀ = 6/5` is not an algebraic integer); `actT (rotZ (3/5) (4/5))` and `actT cycEquiv` do not commute on `W 3` | P4 |
| S0-5 | The `(0, 0)` ancilla block of `c · (U ⊗ 1ₙ)` is `c · U` (the membership step's matrix identity) | P5; module (`ancBlock_smul_tokOp`) |
| S0-6 | The module builds: `pairAvail_of_opDrive`, `opDrive_iff_pairAvail`, `mem_of_tokenAvail`, `transfer_of_opDrive`, `transfer_of_jDatum`, `bridge_derived_half`, `Q3_two_invariant`, `latticeClass_not_opDrive`, `latticeClass_not_jDatum`, `substratumClass_opDrive_not_jDatum`, `fullClass_opDrive_jDatum`, `not_opDrive_of_moved`; every `#print axioms` line standard | dispatch, job log |
| S0-7 | Hypotheses of the derived half, classified: I4.29, I4.30, I4.32, I4.134 (inventory items, assumed in general at L, discharged for the kernel's classes and for FM's lattice class [K]/[D]); OpDrive(θ₀) and the J-datum (introduced, not OI premises: I2.33's phase intervention at `θ₀`, the datum at `π/4`); (T)_𝓘 (introduced, not an OI premise: nothing at L sources it, B15-2) | §2 |
| S0-8 | Disguise test: OpDrive(θ₀) restates I2.33's phase intervention at the angle `θ₀` (I4.44's class with its stipulated phase makes it true: `substratum_tokenAvail_zPh`) and I3.169's operational reading at `θ₀` (B14-7); it is not (b) in disguise (one token, no pair cone, no `W 3`); it is H-T's token clause, and H-T's (A) is I4.29 | §3 |
| S0-9 | FM refutes OpDrive(θ₀) and the J-datum; K(Z_F) fails the bridge's premises for every class whose transfer clause it satisfies (the exclusion lemma with P3's witness); the bridge is not an equivalence (FM's `Q3` has the invariance without the availability, B14-5) | §2, §4 |
| S0-10 | Gem: POSITIVE as fixed in the productivity test | §5 |

### S0 addendum (written 2026-10-11T07:55:45Z, after the owner's round-5 directions, before any dispatch)

The owner's requirement (2) and the safeguard (LOG, 2026-10-11T07:55:45Z), applied to the design above:
- **The two introduced data are explicit**: OpDrive(θ₀) and the J-datum are hypotheses of every theorem of the
  derived half, never discharged inside it. **Every other hypothesis is an inventory item cited by id**: I4.29
  (`ContextStable`), I4.30 (`LabelInvariant`), I4.32 (`Architecture`), I4.134 (`UnitaryRaySaturated`), each
  "assumed in general" at L and discharged for the kernel's classes [K] and FM's lattice class [D]; and (T)_𝓘, the
  class's transfer clause, introduced (B15-2). **No step uses any availability beyond the two data**: no
  `diagonal_avail`, no `SubstratumAvail`, no `DrivesElementary`, no phase at any angle, no exchange. **The
  kernel closure rules used, step by step** (HO-17 item 8): token ⇒ pair: the spectator rule (`instAvail_spectator`,
  one uncoupled token A) and the transport rule (`instAvail_transport`, the associator); pair ⇒ token: the transport
  rule (`toEnd`) and the discard rule (`InstAvail.discard`, `m = 2`); the membership step: the ray step
  (`exists_scaled_mem_of_instAvail_unitary`: the branch-realization of every protocol, `realized_of_instAvail`, and
  the Kraus ray lemma) with the architecture's `block` and the saturation clause; the transfer: the clause itself
  (`transferClause_iff`), one operation at a time. No bind step (`avail_conj_mul`) and no composition of
  operations occurs anywhere in B20's chain — each of the two operations is transferred as it stands.
- **Sufficient, not necessary.** OpDrive(θ₀) is recorded as a *sufficient* token datum for the derived half, never as
  necessary: that every available primitive of a class has finite order does not exclude dense control from
  compositions (Hadamard and the π/8 phase are of finite order and generate a dense subgroup of `PSU(2)` [L]).
  Alternative generating sets named, not characterized (the characterization under the kernel's composition rules is
  the origin thread's, pending as O14/O15): (i) a finite-order non-Clifford datum on the token together with the
  quarter phase and the exchange — origin's fixed gate `rot(π/8)` with the stated access, whose level-one group is
  dense up to phase (HO-27 item 4, CONDITIONAL [D] + [W + L]); (ii) the Hadamard and the π/8 phase [L]; (iii) the
  exchange's own layer flow at one non-Clifford time together with the quarter phase (`R_x(πt)` with `S`; the
  Euler-angle remark of the round-4 audit's F1 for `t` ranging over all times, and a finite-order instance at one
  `t` with `πt ∉ (π/4)ℤ`); none of these is examined here.
- **Exact availability versus density, kept apart.** *Version E (the chain as designed):* the transfer clause in
  table form transfers the admissible unitaries of the class one by one, so the derived half needs the **exact**
  availability of `R_z(θ₀)` and of `J` — OpDrive(θ₀) and the J-datum as stated; its conclusions are the pair
  availability of the two operations (exact, at every level) and, through (T)_𝓘, the two invariances. *Version D
  (density):* if a dense subgroup of token unitaries is available (each finite composition exactly, by the bind
  rule) and the pair cone `K` is **closed** (H3's self-duality `K = dualW K` makes `K` closed), then, since
  `U ↦ transferMap U ω` is continuous, (T)_𝓘 on the dense subgroup gives the invariance of `K` under the
  transferred table of every token unitary, `R_z(θ₀)` and `J` included — an invariance conclusion only. Version D
  delivers no availability of `R_z(θ₀)` or `J` themselves: in the kernel's vocabulary a limit of available
  operations is not available unless a closure premise says so, and the kernel refutes exactness for the fixed-gate
  theories that have dense control (`fixedGateTheory_not_qm`, DiscreteCompletion.lean:1948, HO-27's scope). So the
  density → "every unitary available" step is not an inventory item and is not introduced here; the density →
  "closed cone invariant" step needs the closedness of the cone (H3, I3.149, introduced, not an OI premise) and the
  continuity of the transferred table [W]. Version D is stated in §2 at [W] and is not built this round; the module
  builds Version E only. Prediction S0-7's classification stands with (T)_𝓘's status as written; added predictions:
  S0-11 — Version E's chain uses the spectator, transport, discard, ray and block rules and no bind step (verified by
  reading the module's proofs); S0-12 — the bridge is recorded "sufficient, not necessary" with the three named
  alternatives.

### Second S0 addendum (written 2026-10-11T08:07:01Z, after the owner's further distinctions, before any dispatch)

- **Domains** (the owner's distinction (1)). OpDrive(θ₀) and the J-datum are availabilities of one-outcome
  conjugations in the InstAvail closure of the token carrier. `pairAvail_of_opDrive`/`pairAvail_of_jDatum`: the
  reversible operations alone (spectator and transport, B19). `opDrive_iff_pairAvail`/`jDatum_iff_pairAvail`: the
  InstAvail closure with ancillas and discard (the converse half discards token A; `discardWith_uniform_conjChannel`
  returns a conjugation). `exists_scaled_mem_of_tokenAvail`/`mem_of_tokenAvail`: a statement about the InstAvail
  closure — the ray step holds for every protocol (every branch of every instrument-realized family is a sum of
  conjugations by members, `realized_of_instAvail`), and the block clause is the architecture's own closure under
  the discard's blocks. `transfer_of_opDrive`/`transfer_of_jDatum`/`bridge_derived_half`: cone invariance on `W 3`,
  one operation at a time, no composition. No theorem of B20 forms a product of operations: no group-generation step
  occurs, so no step relies on a transformation outside its domain.
- **Exact availability, not density** (the owner's distinction (2)). The derived half needs the **exact** availability
  of `R_z(θ₀)` and of `J` — object (i), OpDrive(θ₀) and the J-datum as stated — and invokes no density. Objects (ii)
  (a dense subgroup of `SU(2)` generated by finite-order data) and (iii) (exact invariance of the pair cone under
  the full closure) are not used: the passage (ii) ⇒ (iii) would need the pair cone closed (H3, I3.149, introduced)
  and the continuity of `U ↦ coordOf (Ad(1 ⊗ U) (dict ω))` [W, not stated as a theorem here], with the exact
  statement that a closed set invariant under a dense set of continuous maps is invariant under their closure; none
  of this is claimed or built, and the "Version D" of the first addendum is withdrawn as a derivation and kept only
  as the name of the different statement it would be. Prediction S0-11 is restated: the chain uses the spectator,
  transport, discard, ray and block rules, no bind step, and no limiting step.
- **Alternative generating sets**: the three candidates of the first addendum are listed as candidates only; their
  density at the level claimed is for the origin thread to establish (O14/O15, pending) and is not asserted here —
  the classical density of `⟨H, T⟩` [L] concerns abstract matrices and says nothing about the kernel's availability
  at a level without a density-to-exactness step. Prediction S0-12 is restated accordingly.
- **The owner's outcome classification**: B20 is expected at **(C)** — the drive supplied by an assumption
  equivalent to the phase intervention at `θ₀` (OpDrive(θ₀) is I2.33's intervention in availability form, B14-3;
  the disguise test S0-8), a sufficient bridge with no independent explanation of its origin — unless origin's O14
  moves it; B14-6 is **(D)** for the availability of the drive: the stage-6 premises below the 29 control-or-QM rows
  admit FM, a non-quantum model (`latticeTheory_not_qm`) in which the drive is unavailable — insufficiency definitive
  within the audited scope (the stage-6 inventory) and saying nothing about every conceivable extension of OI. Added
  prediction S0-13: the verdict row names (C) for B20 and (D) for the availability verdict of B14-6, each with that
  scope sentence.
