# NOTES-B14 — (A) at level H in the kernel's own vocabulary

Node B14 of `research/bridge` (round 4). Base L = `9f9f8257`. Evidence levels: [K] kernel at L (file:line checked at
L); [D] design module built in CI; [X] exact computation (`experiments/b14_preflight.py`); [W] written here; [A]
audited record. Received handoffs used at their labels (LOG, round 4): HO-17 items 1, 3, 5 as constraints and item 8
as binding on every availability argument; HO-9 v2 item 3; HO-18 item 1 (the dictionary's injectivity, [D]) for
RESPECT only.

## 0. Question

The round-4 directive: state "availability in the pair context of one stage-crossing token operation" as a
predicate over the kernel's `genTheory` / `InstAvail` (OperationalAssembly.lean:594 `FiniteOperationalTheory`;
ImplementationLocality.lean:268 `InstAvail`, :852 `genTheory`), with availability at a level taken as HO-17 item 8
requires: the class is closed under ancilla blocks and relabellings of its members at every level
(`MixR.block`, `MixR.relabel`; for an architecture, `Architecture.block`), and every `InstAvail` protocol counts
(`op`, `readout`, `coarse`, `bind`, `discard`). Then decide whether any protocol of the stated access makes
`actT R_z(θ₀)` (`cos θ₀ = 3/5`) or `actT J` available on the pair, with RESPECT and product behaviour: whether H-T
(B10-3, HO-20 item 3) or (A)_J is supplied or refuted inside the kernel's operational structure. Run the disguise
test on the premise stated.

## S0. Design, productivity test and predictions (written 2026-10-11T03:09:18Z, before any run or dispatch)

**Design decisions.**
- **The kernel's operators for the two token operations.** Through the dictionary, `actT R_z(θ₀)` is the
  conjugation by `1 ⊗ diag(1, w)`, `w = 3/5 + (4/5)i` (B11 `dict_actT_rotZ`, [D]), and `actT J` (`J = cycEquiv`,
  KInfFoundations.lean:416) is the conjugation by `1 ⊗ U_J`, `U_J = (1 − i(X + Y + Z))/2` (HO-18, the coordinator's
  X2; re-derived in the preflight). The predicate is stated for an arbitrary token operator `U`.
- **The predicate.** On the pair carrier `Fin 2 × Fin 2` (token A, token B) at level `n`:
  `PairAvailAt 𝓘 arch U n := (genTheory 𝓘 arch (Fin 2 × Fin 2)).availExt n Unit (fun _ => conjChannel (pairOp U n))`,
  with `pairOp U n = (1 ⊗ U) ⊗ 1ₙ` (token A and the ancilla as spectators). By `genTheory_availExt_iff`
  (ImplementationLocality.lean:909, `Iff.rfl`) this is `InstAvail` at the carrier `(Fin 2 × Fin 2) × Fin n`: every
  protocol, with the class's blocks and relabellings of members at every level. The token-only form
  `TokenAvailAt` (token B alone at level `n`, `tokOp U n = U ⊗ 1ₙ`) is stated beside it, so that a refutation can be
  located at the pair context or at the token.
- **The decision route (no enumeration of protocols).** For an architecture, every branch of every instrument-realized
  family is a sum of conjugations by class members (`realized_of_instAvail`, ImplementationLocality.lean:530), and
  every Kraus operator of a unitary conjugation lies on its ray (`kraus_of_conj_unitary`,
  MicroscopicReversibility.lean:189). So if a unitary `V`'s conjugation is available at a carrier, some nonzero
  multiple `a • V` is a class member there (the ray lemma, to be proved in the module). A class invariant that no
  nonzero multiple of `V` satisfies then refutes availability at that carrier, for every protocol and every level.
- **"The stated access".** The kernel uses the phrase for `permClass` (the contractively scaled partial
  permutations; OperationalSourcing.lean "the stated access is still exactly `permClass`", SubstratumInterfaceAudit.lean
  :236) and for `permClass` together with the quarter phase on any configuration (StateMixingCoupling.lean:13, the
  class `MixR ∅`). Both are decided. For comparison: the monomial interface `substratumClass`
  (StructuralClosure.lean:180; the substratum theory of RouteB.lean:279, whose phase intervention PhaseSource.lean
  isolates as a stipulation), and the full class.
- **Invariants.** For `permClass`: all nonzero entries of a member are equal and at most one per row
  (`IsScaledPartialPerm`). For `MixR ∅`: submonomial, and any two nonzero entries have equal fourth powers (`QuartEq`;
  their ratio is a fourth root of unity), proved by induction over the eight constructors, the `mix` constructor
  being empty at `D = ∅`. For J, submonomiality alone suffices: `U_J` has two nonzero entries in a row.
- **RESPECT and product behaviour.** (P) is proved for `pairOp`: `conj((1⊗U)⊗1)(ρ⊗σ⊗τ) = ρ⊗(UσU*)⊗τ`. (W) holds
  for every operation on the kernel's pair carrier: its states are the matrices themselves, and the dictionary to
  `W 3` is injective (HO-18 item 1, [D]), so equal readouts are equal states [W].
- **Controls.** Positive: the NOT (a permutation matrix) is pair-available in the stated access at every level, so
  the predicate is satisfiable there; the full class supplies both operations. Countercontrols: the monomial
  interface supplies `R_z(θ₀)`'s pair operator, so the stated access's invariants are load-bearing; the quarter phase
  `diag(1, i)` satisfies `QuartEq`, so the `MixR ∅` invariant does not exclude every phase, only those whose ratio is
  not a fourth root of unity.
- **No local Lean** (as in rounds 2–3). Every kernel name used is read at L in this tree (identical to L:
  `git diff 9f9f8257 HEAD -- verification papers book` is empty); every Mathlib name used is one the kernel at L
  already uses, so it exists in the pinned Mathlib `v4.33.0`. The module imports the kernel only.

**Productivity test (§A.31), fixed now.** B14 is a gem iff it yields a fact strictly stronger than the obvious
restatement ("H-T needs (A) for `R_z(θ₀)`; (A)_J needs (A) for `J`") that constrains the sourcing of (A) or exposes a
hidden assumption: for example, a decision of H-T or (A)_J inside the kernel's operational structure located at a
definite clause (the pair context or the token), or an assumption of the bridge vocabulary that the kernel's
operational structure does not share. Otherwise ELABORATING.

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | The ray lemma holds for every architecture: an available unitary conjugation has a nonzero multiple of its operator in the class at that carrier | module, `ray_of_instAvail` |
| S0-2 | Stated access `permClass`: for every level `n ≥ 1`, neither `R_z(θ₀)`'s nor `J`'s operator is available, on the pair (`¬ PairAvailAt`) or on the token alone (`¬ TokenAvailAt`). The refutation sits at the token operator: the pair context adds nothing | module; preflight P5 |
| S0-3 | Stated access with the quarter phase (`MixR ∅`): the same four refutations. The obstruction for `R_z(θ₀)` is the fourth-root lattice: `w⁴ = (−527 − 336i)/625 ≠ 1` | module; preflight P1, P5 |
| S0-4 | Monomial interface: `R_z(θ₀)`'s pair operator is available at every level (supplied, by the phase stipulation); `J`'s is refuted at every level `n ≥ 1` | module; preflight P8 |
| S0-5 | Full class: both pair operators available at every level | module |
| S0-6 | Controls: the NOT is pair-available in `permTheory` at every level; `QuartEq` holds for the quarter phase's pair operator | module; preflight P5, P7 |
| S0-7 | (P): `conj((1⊗U)⊗1)(ρ⊗σ⊗τ) = ρ⊗(UσU*)⊗τ`, exact on instances and proved in the module | module; preflight P6 |
| S0-8 | Exact facts the module relies on: `U_J` is unitary with first-row entries `(1−i)/2`, `(−1−i)/2`; through the dictionary `Ad(1⊗U_J)` is `actT cycEquiv` and `Ad(1⊗diag(1,w))` is `actT R_z(θ₀)`; `U_J = ((1−i)/√2)·X·rot(π/4)·S³` exactly (so `J` lies in the datum class `MixR {π/4}`); the polynomial certificate for `w⁴` | preflight P1–P3 |
| S0-9 | The CI build succeeds: Build green, every `#print axioms` line of the module on `[propext, Classical.choice, Quot.sound]`, `lean-axioms` PASS, gate red only on `lean-manuscript` | dispatch, job log |
| S0-10 | Gem classification: NEW if S0-2 and S0-3 hold (inside the kernel the decision falls at the token, so (A) is not the separating clause of either operation under the stated access); otherwise ELABORATING | §3 |
