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

## 1. Outcome of S0 (written 2026-10-11T04:18:50Z)

**The design run.** `dev-bridge/r4-avail` @ `152094b5` (L plus the module, verbatim from `937af1fb`, and one import
line); run 38110368244, created 2026-10-11T04:03:31Z, event `workflow_dispatch`; Mathlib bridge job 114384480945.
Build success (04:05:00–04:07:00Z; "Built OIBridge.BridgeAvail (3.7s)", "Build completed successfully (3644 jobs)").
The module's diagnostics are linter warnings only: four `unnecessarySeqFocus` (the `<;> ring` after the conjugation
`simp only`, lines 118, 208, 212, 216), four unused/unreachable-tactic notes (the `simp` fallbacks of `zPh_00`,
`zPh_11`, `uJ_00`, `uJ_01` never ran: `rfl` closed them) and four `haveI`→`have` style notes. All 61 `#print axioms`
lines of the module (lines 731–791) read `[propext, Classical.choice, Quot.sound]`; no `sorryAx`. Release gate:
`lean-axioms` PASS (5921 named results = L's 5860 + the module's 61, no sorry); the only red step is
`lean-manuscript` (1 problem: the new module has no census family, by construction). All other jobs of the run green.

| id | prediction | outcome |
|---|---|---|
| S0-1 | ray lemma for every architecture | holds, and is a kernel theorem at L: `exists_scaled_mem_of_instAvail_unitary` (MicroscopicReversibility.lean:251), found in the pre-dispatch review and used as it stands — CERTIFIED, not [D] |
| S0-2 | stated access refutes both, pair and token, every `n ≥ 1` | confirmed [D] (`statedAccess_refutes`) |
| S0-3 | quarter access refutes both; obstruction the fourth-root lattice | confirmed [D] (`mixEmpty_quartLattice`, `quarterAccess_refutes`) |
| S0-4 | monomial interface: `zPh` available at every level, `uJ` at none | confirmed [D] (`monomialInterface_split`) |
| S0-5 | full class supplies both | confirmed [D] (`fullClass_supplies`) |
| S0-6 | NOT pair-available in the stated access; quarter phase on the lattice | confirmed [D] (`statedAccess_pairAvail_nflip`, `quarter_on_lattice`) |
| S0-7 | (P) | confirmed [D] (`pairOp_prod`) |
| S0-8 | the exact facts | confirmed [X] (preflight P1–P3, 8/8) and, for `w⁴`, [D] (`w345_pow_four`, `w345_pow_four_ne_one`) |
| S0-9 | the CI outcome | confirmed exactly (Build green, 61/61 standard, `lean-axioms` PASS, gate red only on `lean-manuscript`) |
| S0-10 | NEW iff S0-2 and S0-3 | NEW (§6) |

## 2. The decision: form (ii) of the coordinator's second addendum

**Statement.** No derivation of the availability of `actT R_z(θ₀)` or of `actT J` on the pair — in the kernel's
vocabulary, `PairAvailAt 𝓘 arch U n` for `U = zPh` or `U = uJ`, by any `InstAvail` protocol at any level `n ≥ 1`, with
the class's blocks and relabellings of members (HO-17 item 8) — exists from the stated access, even together with
every inventory item the models below satisfy. The same holds on the token alone (`TokenAvailAt`).

**The obstruction, in inventory terms.** The H→M arrow the stage-6 graph has, the observer theory of a substratum
(I1.59: `obsTheory 𝒮 = permTheory 𝒮.Conf`, SubstratumInterfaceAudit.lean:769), lands in the stated access: its
implementation class is `permClass`, the contractively scaled partial permutations of I1.60
(`IsScaledPartialPerm`, :231). Through the ray step (S0-1, [K]) an available unitary conjugation puts a nonzero
multiple of its operator into the class at that carrier, so every class invariant is an availability invariant:
- `R_z(θ₀)` is excluded by I1.60's invariant (all nonzero entries of a member are equal): `diag(1, w)` has unequal
  nonzero entries for every nonzero scalar multiple. This is the kernel's `permTheory_diagonal_only_scalar`
  (SubstratumInterfaceAudit.lean:674) in another form; with the quarter phase adjoined (the kernel's own
  "stated access with the quarter phase", I4.175 at `D = ∅`) the invariant becomes the fourth-root lattice
  (`QuartLattice`: submonomial, nonzero entries with equal fourth powers, closed under all eight constructors of
  `MixR`, blocks and relabellings included), and `w⁴ = (−527 − 336i)/625 ≠ 1` excludes `diag(1, w)` [D];
- `J` is excluded by monomiality (I1.56 / I4.242 `ConfigurationLevel`: every admissible operator monomial): `U_J` has
  two nonzero entries in its first row [D].

**Independence: models of the stated access in which the operations are unavailable.**

| model | satisfies (inventory, status at L) | refutes |
|---|---|---|
| `permTheory (Fin 2 × Fin 2)`, the pair's observer theory (I1.59) | `SourcedOI` (I1.60 / I4.248) [K `permTheory_sourcedOI`, :660], hence `ReversibleImplementationLocality` (I4.133) with `ContextStable` (I4.29) and `LabelInvariant` (I4.30) [K :358, :362], and `EmbeddedObservation` (I4.110) [K]; on the token's carrier also the sealed core `RealizesSealedOICore` / `OICore` (I1.43 / I1.47) [K :740] | `PairAvailAt` and `TokenAvailAt` of `zPh` and `uJ`, every `n ≥ 1` [D `statedAccess_obstruction`] |
| `mixTheoryR ∅ (Fin 2)`, the stated access with the quarter phase | `DerivedOI` (I1.49 / I4.241), "every theory-level predicate the kernel derives from the substratum" [D `mixEmpty_derivedOI`: the kernel's `derivedOI_of_stated` (StateMixingCoupling.lean:463) with the two stabilities proved by the kernel's own proofs at `D = ∅`] | the same four, every `n ≥ 1` [D `quarterAccess_obstruction`] |

Several of the satisfied items are flagged "do not assume" in the inventory (I4.29, I4.110, I4.241): the models grant
them, and the operations still do not follow. So the token operations are independent of {I1.43, I1.47, I1.49,
I1.59, I1.60, I4.29, I4.30, I4.110, I4.133, I4.241, I4.248} at the kernel's carrier.

**Where the decision falls: at the token, not in the pair context.** In both models `ContextStable` holds, i.e. the
kernel's form of (A) is satisfied, and the refutation is already a refutation on the isolated token. In the kernel's
vocabulary the two predicates coincide for every context-stable, label-invariant architecture [W]:
- token ⇒ pair: `instAvail_spectator` (ImplementationLocality.lean:789) gives the conjugation by `1 ⊗ tokOp U n` on
  `Fin 2 × (Fin 2 × Fin n)` (`amplRefL_conjChannel`, :697), and `instAvail_transport` (:644) along the associator
  gives `pairOp U n`;
- pair ⇒ token (label invariance alone): relabel so that token A is the last factor, then `InstAvail.discard` with
  `m = 2`; by `discardWith_uniform_conjChannel` (AncillaClosure.lean:461) the blocks of `tokOp U n ⊗ 1₂` are
  `δ_fe · tokOp U n`, and the discarded family is the conjugation by `tokOp U n`.

The module proves both predicates in each of the four classes directly; the general equivalence is a written
argument from kernel lemmas, a formalization target for a later round.

**Controls.** Positive: the NOT is pair-available in the stated access at every level (the predicate is satisfiable
there); the full class supplies both operations; the monomial interface supplies `R_z(θ₀)`. Countercontrol: the
quarter phase's pair operator lies on the fourth-root lattice, so the lattice excludes `R_z(θ₀)` by its angle, not
every phase.

## 3. What does supply the operations, and as which hypotheses

- **The monomial interface** (`substratumClass`, I4.44; `substratumTheory`, I4.240) supplies `R_z(θ₀)` on the pair
  and on the token at every level, and satisfies `DerivedOICore` [K `substratumTheory_derivedOICore`, RouteB.lean:380]
  — but only through the phase intervention at the angle `θ₀`, which I2.33 records as an assumption ("The phase
  intervention enters as an assumption on the substratum class, not as a consequence of the finite states with the
  bijective read-write dynamics", GR.md:256; flag "do not assume"). In standing-rule form:
  OI + {phase intervention at θ₀ — introduced, not an OI premise (I2.33)} ⇒ `PairAvailAt substratumClass … zPh n`
  for every `n` [D]. It does not supply `J` (monomiality, I1.56) [D].
- **`J`** is supplied only with a non-monomial datum: `U_J = ((1 − i)/√2) · X · rot(π/4) · S³` exactly [X preflight
  P2], a unimodular multiple of a product of members of `MixR {π/4}` (I4.175 with the datum at `π/4`), whose
  stabilities the kernel proves (`mixR_singleton_contextStable`, DiscreteCompletion.lean:1890) [K]; so
  OI + {the datum at π/4 — introduced, not an OI premise} ⇒ `TokenAvailAt`/`PairAvailAt` of `uJ` [X + W, not
  built]. The datum at `π/4` does not supply `R_z(θ₀)`: `MixR {α}` is countable up to scalar
  (`mixR_countable_upToScalar`, StateMixingCoupling.lean) [K], which bounds what it supplies but does not by itself
  exclude `diag(1, w)`; the exclusion of `R_z(θ₀)` from `MixR {π/4}` is not decided here.
- **The full class** supplies both [D]; it is not a sourcing.

## 4. Disguise test on the predicate stated

`PairAvailAt` is availability on the kernel's pair carrier `Fin 2 × Fin 2`, whose composite is the Kronecker
composite by construction (the kernel's H→M realizations "realize the sealed core in `FiniteOperationalTheory (Fin 2)`,
whose composites are tensor products with the PSD cone by construction", stage-6 R6 §6 [A]). Read as a statement about
a pair cone on `W 3` it becomes the transfer clause (T) of B9 — for the monomial class, (b) for the phase circle
(B11-2, I3.165's clause) — so as a bridge to the pair cone it FAILS the disguise test (it is (b) under the
dictionary; B10-6's assumption-watch marker). As a statement about the kernel's carrier it is not a disguise: it
introduces nothing and is decided there (§2). The token premise that would make it true — the phase intervention at
`θ₀` (I2.33) or a non-monomial datum for `J` — is an availability premise of K∞-Act/K∞-Drive type (I3.168, I3.169),
introduced, and not a form of (b) (I3.150–I3.153, I3.165), because it concerns one token alone.

## 5. K(Z_F) and the owner's framing

With A the applicable non-hypothetical OI premises at L and b the composite action, K(Z_F) ⊨ A and K(Z_F) ⊭ b. The
candidate bridge's continuous half H-T (B10-3) has two components: availability of `R_z(θ₀)` on token B, and (A) for
it. They fail in different models:
- in B4's realization of K(Z_F) (an H-level hidden realization, not a kernel `genTheory`), the token operation is
  available on the isolated token and (A) fails (`−2/5`, B10-2; `−1/2` for `J`, B12-4);
- in the kernel's theories of the stated access (§2), the kernel's (A) holds (`ContextStable`) and the token
  operation is unavailable.

So neither component is supplied by the items at L, and each is needed: a sufficient bridge must add a token-level
resource (the phase intervention at `θ₀`, introduced; a non-monomial datum for `J`, introduced) and must carry it to
the pair cone, which at L no bridge does (the level-M items of the models, I4.29, I4.110, I4.133, I4.241, are NOT
REACHED in Table A2 for K(Z_F); this node adds no M→P bridge, so their status there is unchanged).

## 6. Gem classification (§A.31)

**NEW**, with ELABORATING parts. The productivity test (S0) is met: the decision of H-T's token clause and of (A)_J
inside the kernel's operational structure is located at a definite clause — the token, not the pair context. Inside
the kernel, (A) is implied by context stability and carries no separating content; the obstruction from the stated
access is token-level availability itself, fixed by a class invariant (I1.60's scaled-partial-permutation form, and
for the quarter access the fourth-root lattice, new here). ELABORATING parts: the ray step (kernel theorem); the
`R_z(θ₀)` refutation in `permTheory` (a form of `permTheory_diagonal_only_scalar`); the `J` refutation by
monomiality (the configuration-level mechanism of I1.56).

**Assumption-watch marker (cross-propagation).** Pair availability in the kernel's vocabulary is token availability
(for context-stable, label-invariant classes): any argument that derives a pair-cone property on `W 3` from the
kernel's pair availability uses the Kronecker composite, i.e. (T) = (b). Rows that read `ContextStable` as (A) at the
pair cone (B2-4, B10-6) carry this marker.

## 7. Manuscript obligations

None. Nothing here bears on a manuscript statement; the results are research statements about the kernel's own
models.
