# The scalar-closure audit — contractive scalars in the implementation architecture

`OIBridge/LieRankSource.lean` (`Architecture`, `Realized`, `realized_smul_nonneg`,
`realized_discard`, `genTheory`), `OIBridge/SubstratumSource.lean` (`fullClass_arch`),
`OIBridge/StructuralClosure.lean` (`substratumClass_arch`),
`OIBridge/SubstratumInterfaceAudit.lean` (`permClass`, `permClass_arch`,
`permClass_le_of_exchanges`), `OIBridge/ScalarClosure.lean` (the regression theorem);
`FLOW-EXTENSION-AUDIT.md` (the deferral that records the owner decision); guards `R7-SUB` and
`R7-SCAL` in `verification/lean/edge_rigidity_probe.py`.

**Status: pass complete. `Architecture.smul` is stated for scalars of modulus at most one; the
generated theory of every class is unchanged by definition; the sourced class migrates with every
theorem reproved under its name; the scalar-hull regression theorem holds and the unrestricted
and the migrated sourced classes generate the same availability; nothing weakens.** The
preregistration sections were written before any edit (commit `8a4bfaa`); this status line and
the outcome section are the only later edits. Nothing here is a manuscript claim.

## The question, and the decision it implements

`Architecture` (round fifty-nine) is the class of admissible implementation operators "closed
under the operations every finite operational theory performs on implementations". Its scalar
field is stated for every complex scalar:

> `smul : ∀ S [Fintype S] [DecidableEq S] (a : ℂ) (K : Matrix S S ℂ), 𝓘 S K → 𝓘 S (a • K)`.

Its only operational use is attenuation: the discard of a uniformly attached ancilla is realized
by multiplying each Kraus operator by `√(1/m)` (`realized_smul_nonneg`, consumed by
`realized_discard`, consumed by `genTheory.prepAvail_discard`). No theory-level construction
amplifies. The flow-extension diagnostic (`FLOW-EXTENSION-AUDIT.md`) found what the surplus
buys: an ancilla block of a word containing a readout projector can be a post-selected
contraction `c · U` with `0 < |c| < 1` and `U` unitary, and unrestricted scalar closure then admits
`(1/c) · (c · U) = U`, turning a probabilistic branch into a deterministic operation. In a
trace-preserving instrument every Kraus operator is contractive, `Kᵢ† Kᵢ ≤ 1`, so a scalar of
modulus above one is never needed to represent a branch; it matters only when the class is
allowed to promote a rescaled branch into a new one-outcome operation.

The owner decision, recorded in the flow-extension deferral and implemented here:

> Unrestricted scalar closure is rejected as an operational reading, because it turns a
> post-selected branch into a freely normalized deterministic operation; `Architecture.smul` is
> restricted to contractive scalars, `‖a‖ ≤ 1`, subject to the compatibility audit below.

This restriction is correct on its own terms and is not sufficient for the flow endpoint: the
same deferral records that `Realized` admits replication of a contractive branch, which is the
object of a separate round on realization provenance. This round does not touch `Realized`,
`ImplementationGenerated`, or any availability predicate, and decides nothing about the flow
endpoint.

## The change, fixed in advance

- `Architecture.smul` becomes
  `∀ S [Fintype S] [DecidableEq S] (a : ℂ) (K : Matrix S S ℂ), ‖a‖ ≤ 1 → 𝓘 S K → 𝓘 S (a • K)`.
- `realized_smul_nonneg` takes the contractive closure as its hypothesis and the bound `c ≤ 1`
  on the real scalar, scaling each Kraus operator by `√c` with `√c ≤ 1`.
- `realized_discard` passes `(m : ℝ)⁻¹ ≤ 1`, which holds for every natural `m` (with `0⁻¹ = 0`).
- Nothing else in `genTheory` changes: its availability fields are `IsGenInstrument`, which
  mentions no scalar closure, so the generated theory of every class is unchanged by definition.

## The census of consumers, taken before the change

| consumer | file | use of the scalar | under the contractive axiom |
|---|---|---|---|
| `realized_smul_nonneg` | `LieRankSource` | `√c` for real `c ≥ 0` | needs `c ≤ 1`; the one call site has `c = 1/m` |
| `realized_discard` | `LieRankSource` | passes `arch.smul` to the above with `c = 1/m` | unchanged after supplying `1/m ≤ 1` |
| `genTheory.prepAvail_discard` | `LieRankSource` | passes `arch.smul` to `realized_discard` | unchanged |
| `fullClass_arch` | `SubstratumSource` | trivial | unchanged |
| `diagClass_arch` | `LieRankSource` | any scalar keeps the off-diagonal zero | unchanged |
| `substratumClass_arch` | `StructuralClosure` | any scalar keeps a monomial monomial | unchanged |
| `permClass_arch` | `SubstratumInterfaceAudit` | any scalar keeps entries uniform | the class migrates, below |
| `permClass_le_of_exchanges` | `SubstratumInterfaceAudit` | the only consumer of an arbitrary scalar, granted by the axiom and not sourced | reproved with the bound |

No manuscript narrates the scalar closure: GR §3.3 and Main §3.4 state closure under
composition, coarse-graining and ancilla blocks, spectators, relabelling and the adjoint.

## The tests, each with its admissible outcomes

**T1. Operational preservation.** The structure `genTheory 𝓘 arch S` is built for every
architecture under the contractive axiom, with identity, composition, coarse-graining, readout,
preparation and discard as before. Admissible outcomes: the kernel compiles with
`realized_smul_nonneg` and `realized_discard` under their contractive hypotheses and every
`genTheory` field unchanged (`genTheory_availExt_eq`, the availability fields are
`IsGenInstrument` by definition), or a construction that needs a scalar of modulus above one,
recorded with the scalar it needs.

**T2. Class migration.** `permClass` is redefined as the contractively scaled partial
permutations: `IsScaledPartialPerm K := IsSubmonomial K ∧ ∃ c, ‖c‖ ≤ 1 ∧ ∀ i j, K i j ≠ 0 → K i j = c`.
Admissible outcomes: `permClass_arch`, `permClass_contextStable`, `permClass_labelInvariant`,
`permClass_daggerStable`, `permClass_permMatrix`, `permClass_readWrite`, `permClass_le_substratum`
and `permClass_le_of_exchanges` reproved for the migrated class, the last with the bound `‖c‖ ≤ 1`
supplied to `arch.smul`; every theorem of `SubstratumInterfaceAudit` reproved under the same
name; or a theorem that does not survive, recorded by name. The three other classes keep their
definitions and their architecture proofs.

**T3. Regression.** The scalar hull `scalarHull 𝓘 S K := ∃ (a : ℂ) (K'), 𝓘 S K' ∧ K = a • K'` of a
class closed under contractive scalars realizes exactly what the class realizes:
`realized_scalarHull_iff : Realized (scalarHull 𝓘) S Φ ↔ Realized 𝓘 S Φ`. Mechanism, fixed in
advance: a conjugation by `a • K` with `|a| > 1` is `⌊|a|²⌋` copies of the conjugation by `K`
plus one conjugation by `√(|a|² − ⌊|a|²⌋) • K`, all admissible. Hence, with
`scalarHull_arch` and `scalarHull_permClass_iff` (the hull of the migrated class is the class
of the first outcome head of `SUBSTRATUM-INTERFACE-AUDIT.md`, the uniformly scaled partial
permutations with any scalar), `permTheory_hull_availExt_iff`: the theory generated by the old
class and the theory generated by the migrated class have the same availability at every level.
The three other classes are closed under every scalar, so their theories are unchanged by
definition. Admissible outcomes: the theorems, or a realized operation of the hull not realized
by the class, recorded.

**T4. What weakens.** The expectation, fixed in advance: nothing. Admissible outcomes: the list
of results that needed a stronger hypothesis after the change is empty, or it is recorded by
name with the hypothesis added.

**T5. Guards.** `R7-SUB` pins the migrated definition verbatim in place of the unrestricted one;
a new guard `R7-SCAL` pins the contractive `smul` field verbatim, the bound in
`realized_smul_nonneg`, the regression theorem and this note, and rejects the unrestricted form.

## What the round does not do

Touch `Realized`, `IsGenInstrument`, `ImplementationGenerated`, or any availability predicate.
Decide the flow endpoint or prove anything from `FLOW-EXTENSION-AUDIT.md`. Change `490e03c`.
Narrate anything in a manuscript. Propagate Route B. Refresh the transfer bundle.

## The outcome

Preregistration commit `8a4bfaa`. The change was made exactly as fixed in advance, the census
was complete, and every test reached its expected outcome.

| test | outcome | kernel |
|---|---|---|
| T1 | operational preservation: the kernel compiles with the contractive axiom; `realized_smul_nonneg` carries `hc1 : c ≤ 1` and scales by `√c ≤ 1`; `realized_discard` supplies `(m : ℝ)⁻¹ ≤ 1`; every field of `genTheory` is unchanged, its availability being the generated-instrument predicate by definition | `Architecture.smul`, `realized_smul_nonneg`, `realized_discard`, `genTheory_availExt_eq` |
| T2 | class migration: `permClass` is the contractively scaled partial permutations, `‖c‖ ≤ 1` in the factored form; every theorem of `SubstratumInterfaceAudit` reproved under its name, `permClass_le_of_exchanges` supplying the bound to the architecture's scalar closure; `fullClass`, `diagClass`, `substratumClass` unchanged | `IsScaledPartialPerm`, `scaledPartialPerm_iff`, `permClass_arch`, `permClass_le_of_exchanges` |
| T3 | regression: a class closed under contractive scalars realizes exactly what its scalar hull realizes, by `⌊|a|²⌋` copies and one contractive remainder; the hull of an architecture is an architecture; the hull of the migrated sourced class is the unrestricted class of the substratum-interface audit's outcome, and the two generate the same availability at every level | `scalarHull`, `realized_nsmul`, `realized_real_smul`, `realized_scalarHull_iff`, `scalarHull_arch`, `IsUniformSubmonomial`, `scalarHull_permClass_iff`, `permTheory_hull_availExt_iff` |
| T4 | what weakens: nothing; no result needed a stronger hypothesis, and the four architecture instances were reproved with the same proofs | the full build |
| T5 | guards: `R7-SUB` pins the migrated definition; `R7-SCAL` pins the contractive field, the bound, the regression theorem and this note, and rejects the unrestricted form | `verification/lean/edge_rigidity_probe.py` |

**Ten named results**, each printing only `propext`, `Classical.choice`, `Quot.sound`.

**What the outcome establishes.** The kernel's implementation architecture is closed under
attenuation and global phases and not under amplification, which is exactly what its one
operational use, the discard normalization, requires, and what a trace-preserving instrument
requires of each of its branches. No generated theory changed: the generated theories never
consumed the scalar field, and the one class whose definition carried an unrestricted scalar
generates, after migration, the same availability as before. Nothing weakens: no result needed a
stronger hypothesis.

**What the outcome does not establish.** Anything about the flow endpoint. The restriction is
correct on its own terms and is not sufficient there: `Realized` admits `N` replicated
contractive branches `(1/√N) • U` of a post-selected contraction `c • U`, whose sum is the
conjugation by `U`, with no common-instrument provenance; that is the object of the separate
round on realization provenance, and until it is settled the minimal flow extension is neither
a countermodel nor a positive instance.

## What this note does not claim

That the replication loophole is closed: it is not, and the round does not touch `Realized`.
That any manuscript narrates the scalar closure: none does, the manuscripts stating closure
under composition, coarse-graining and ancilla blocks. That the flow endpoint is settled in either
direction. That anything here reaches a manuscript.
