# The completion-assumption audit — the ledger reconciled with the kernel

`verification/EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md` (the charter),
`OIBridge/LevelOneRecursion.lean` (the one witness the charter asks for that the kernel did not
carry), `PRIMITIVE-SOURCE-AUDIT.md`, `SUBSTRATUM-SOURCE-AUDIT.md`, `TYPED-COMPLETION-AUDIT.md`;
guard `R7-CAA` in `verification/lean/edge_rigidity_probe.py`.

The charter asks that the five-assumption completion package be minimized, that every assumption
end as DERIVED or INDEPENDENT with a kernel witness, and that no semantic relabelling count as a
derivation. This note reconciles the charter's ledger with what the kernel proves. The finding is
that the programme the charter describes is the primitive-source audit of rounds fifty-six to
fifty-nine and the substratum-source audit of rounds sixty-one to sixty-four: every row is
settled, with one witness missing, and the charter's "current exact package" is the round-41
five-condition package rather than the most compressed package currently recorded.

## The ledger, with kernel witnesses

Each row records the derivation the charter names as the first route to test, the kernel result
that settles it, and the countercontrol that keeps the assumption from being redundant among its
peers. DERIVED means derived from a strictly more primitive principle that mentions neither the
assumption nor its operational vocabulary; INDEPENDENT means an explicit theory carries the other
assumptions and not this one.

| assumption | status | derived from | kernel witness | independence countercontrol |
|---|---|---|---|---|
| `SystemToLevelOne` | DERIVED from embedded observation; INDEPENDENT of observer recursion | relabelling along `A ≃ A × Fin 1` | `systemToLevelOne_of_embeddedObservation` | `levelOne_independent'` (loose theory, against the other four conditions and the core); `levelOne_independent_of_recursion` (the same theory has observer recursion) |
| `IteratedAncillaClosure` | DERIVED from observer recursion, and from embedded observation | the shifted theory's own discard rule | `closure_of_observerRecursion`, `closure_of_embeddedObservation`; conversely `observerRecursion_iff_closure` given identity and readout at every level | `closure_independent` (admissible theory: exact system QM, control, inert spectators, no closure) |
| `InertSpectatorCompositionality` | DERIVED from implementation locality | context-stable, label-invariant implementation class generating availability | `observationalIndependence_of_implementationLocality` | `redundancy_fails` (2-positive countermodel: core, validity, reversible richness, embedded observation, no inert spectators); `form_fixed_existence_fails` |
| `CompositeOperationalValidity` | DERIVED from implementation locality (positivity); normalization is the trace clause of implementation generation, stated rather than derived | realized operations are completely positive | `validity_of_implementationLocality` | `validity_independent` (everywhere-available theory) |
| `HasCompositeUnitaryControl` | DERIVED from elementary transition richness with dagger-stable implementation locality | driven transition, exchanges, quarter phase generate `su(D)` | `lieRank_of_elementary`, `inverseAccessibility_of_generated_daggerStable`, `control_of_lieRank_inverse`; necessity `elementary_of_control` | `lieRank_not_redundant` (diagonal architecture: reversible implementation locality and embedded observation, no Lie-rank richness); `control_independent` (diagonal theory) |

**The missing witness.** The charter's first row names observer recursion as a candidate source
of the seam alongside embedded observation. The kernel derived the seam from embedded observation
in round fifty-six and had no statement about observer recursion. `LevelOneRecursion.lean` closes
it: the loose theory has control, inert spectators and closure, which is all the shifted-theory
construction consumes, so it has observer recursion (`systemLoose_observerRecursion`), and it has
no seam. `levelOne_row` states both halves in one place: derived from embedded observation, not
from observer recursion. The gap is relabelling invariance, which observer recursion does not
carry.

## The most compressed package currently recorded

The charter's "current exact package" — well-formedness and the three substantive principles,
`exactAll_iff_substantive` — is the round-41 statement. The kernel carries three successive
compressions below it, each equivalent to exact finite endomorphic operational quantum mechanics
on every nonempty finite carrier:

| package | conjuncts | theorem |
|---|---|---|
| `OIPlusEmbedded` | validity, observational independence, reversible richness, embedded observation | `carrier_general_oiPlusEmbedded` |
| `OIPlusLocal` | implementation locality, reversible richness, embedded observation | `carrier_general_oiPlusLocal` |
| `OIPlusElem` | reversible implementation locality, elementary transition richness, embedded observation | `carrier_general_oiPlusElem` |

`OIPlusElem` is the charter's desired endpoint: every conjunct is stated at the level of
implementations or of the observer architecture, none is a Lie-algebraic, reachability or
availability condition, and both directions are kernel-witnessed. The substratum-source audit
then collapses the three conjuncts to one object, a quantum architecture — an implementation
class closed under the theory operations, context-, label- and dagger-stable, and driving the
elementary transitions — and shows the current OI substratum supplies the four stabilities and
not the drivability (`substratum_residual`): `current OI substratum + continuous off-diagonal
controllability ⟺ finite operational quantum mechanics` (`substratum_plus_control_qm`,
`qm_generated_by_substratum_extension`). Level II shows "endomorphic" is a typing artifact
(`typed_determined_iff`).

## What remains open

These are the residual items the earlier audits named and did not settle; nothing in this note
settles them.

1. **The inverse clause.** Whether inverse accessibility is forced by implementation locality,
   embedded observation and Lie-rank richness is open in both directions. The compact-semigroup
   argument — the available unitaries at a level form a subsemigroup of a compact group
   containing the flows in both time directions, and a subsemigroup with nonempty interior is a
   group — is the candidate derivation; no countermodel is built either.
2. **The minimal elementary repertoire.** Whether the quarter phase is dispensable on three or
   more states, and whether one driven pair and one exchange orbit suffice, is not settled.
3. **Context stability given generation.** Whether a theory generated by a class not closed under
   `1 ⊗ ·` can fail observational independence is not settled.
4. **The empirical addition.** Continuous off-diagonal controllability is not supplied by the
   current substratum (`readWriteSourced_not_qm`, `substratumClass_not_drivesElementary`); no
   control law is postulated to obtain it.

## What this note does not claim

That any row of the charter was settled by this note beyond the one witness; the rest are the
earlier rounds' theorems, cited. That `OIPlusElem` is minimal in any sense stronger than the
independence rows record: item 2 above is exactly the open minimality question. That the
substratum supplies elementary drivability. That any statement here bears on the OI-N thread,
the concrete-cut freeze, or CT3.
