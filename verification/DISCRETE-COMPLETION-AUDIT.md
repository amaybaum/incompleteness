# The discrete completion audit — does the closure with one fixed discrete mixing gate generate a theory dense in finite quantum mechanics?

Owner-called from `main` at `1cb923d`, the merge of the operational pair-flow equivalence audit.
Preregistered here and committed alone before any proof is attempted.

The pair-flow equivalence audit closed the operational question in exact form: on the two-valued
carrier, exact finite quantum mechanics is exactly the consequence closure together with one
sourced real pair flow, a continuous one-parameter family available as primitive executable
structure. This round asks whether that continuity was fundamental or an artifact of demanding
exact availability rather than closure. The resource is cut down to one fixed gate at one fixed
angle, with no continuous parameter anywhere, and the target is changed from exact availability to
density: every finite quantum operation approximable arbitrarily well, with exact quantum mechanics
recovered only by a topological completion.

## The question

> Can `DerivedOI` together with one fixed discrete mixing gate, available at every level at the
> same fixed angle, generate a theory dense in finite quantum mechanics, with continuity allowed
> only in the topological completion and never as primitive executable structure?

## The lead resource, frozen

`DerivedOI` already supplies the phases (`PhasesAvailable`, the quarter phase on every
configuration at every level) and the exchanges (`ExchangesAvailable`). No new phase assumption is
made. The only new datum is one fixed gate:

> **`FixedGateSourced α T`.** For every level `n`, the conjugation channel of `mixImage n α` is a
> one-outcome available operation of `T`, with the same fixed real `α` at every level:
>
> `∀ n, T.availExt n Unit (fun _ => conjChannel (mixImage n α))`.

`mixImage` is the construction audit's definition, unchanged: the real rotation `rot α` on the site
factor, the identity on the ancilla factor. There is no map `t ↦ α(t)`; `α` is chosen once. The
kernel already carries the fixed-gate class and theory at the class level, `MixR {α}` and
`mixTheoryR {α} (Fin 2)`, and already knows that this theory is not exact quantum mechanics
(`mixTheoryR_not_qm`, the datum at countably many angles). That negative is the reason for this
round's target: exactness fails for the discrete resource by cardinality, and the question is
whether density survives.

The two-valued carrier `Fin 2` is frozen throughout, as in the equivalence audit.

## The targets, frozen

**D1, dense unitary control.** `DenseUnitaryControl T`: at every level `n`, for every unitary `U`
on `Fin 2 × Fin n` and every `ε > 0`, there is a unitary `V` whose conjugation channel is available
in `T` with `‖U − c • V‖ < ε` for some unit scalar `c`. The norm on representatives is the operator
norm on matrices (`Matrix.Norms.L2Operator`, the kernel's scoped instance). Approximation is up to
a unit scalar because a conjugation channel does not see one; density is stated for the projective
image, which is what availability records.

**The bridge, frozen as a lemma.** The channel metric is the operator norm of the difference of
the two linear maps, each acting on matrices normed by the operator norm:
`d(Φ, Ψ) := sup { ‖Φ X − Ψ X‖ : ‖X‖ ≤ 1 }`. For unitary `U, V`:
`‖U − V‖ ≤ ε → d(conjChannel U, conjChannel V) ≤ 2 ε`, since
`U X Uᴴ − V X Vᴴ = (U − V) X Uᴴ + V X (U − V)ᴴ`. The constant is `2`. In finite dimension every
norm on the space of linear maps is equivalent, so the density statements below do not depend on
this choice; the quantitative constants do, and they are stated for this metric only. The diamond
norm is not used and nothing is claimed in it.

**D2, dense finite quantum mechanics.** `DenseFiniteQM T`: at every positive level `k + 1`, for
every finite endomorphic Kraus instrument `F` with `m` outcomes
(`IsFiniteEndomorphicKrausInstrument F`) and every `ε > 0`, there is an available family `G` with
`d(F a, G a) < ε` for every outcome `a`; together with soundness, every available family is a Kraus
instrument (`KrausSoundExt T`). Dense means contained in quantum mechanics and dense in it; the two
halves are stated separately and both are required.

**D3, the completion statement.** The closure of a theory's availability is defined outcome-wise
at every level: `F` is in the closure iff for every `ε > 0` some available `G` is within `ε` of `F`
in the metric of D2. The statement to be made precise is: if `DenseFiniteQM T` and `KrausSoundExt T`,
then the closure of `T`'s availability at every positive level is exactly the finite endomorphic
Kraus instruments, which is the exact predicate `ExactCompositeQuantumOps` applied to the closed
availability. Whether the closed availability again satisfies the theory axioms
(`availExt_coarse`, `availExt_bind`) is a separate obligation of D3: proved, or the failing axiom
named. Dense availability is never identified with literal exact availability; the fixed-gate
theory itself remains not exact (`mixTheoryR_not_qm`).

## The level-one prediction, frozen, with what must be kernel-proved distinguished

At level one the carrier is `Fin 2 × Fin 1`, the quarter phase is `diag(1, i)`, the exchange is the
site swap, and the fixed gate is `rot α`. Because `rot α = cos α · 1 − i sin α · σ_y = exp(−i α σ_y)`,
its Bloch rotation angle is `2α`. The quarter phase is a Bloch quarter turn about the perpendicular
axis; the exchange is a Bloch half turn. Let `G_α` be the projective group generated by the three.

> **Prediction.** `G_α` is finite if and only if `α ∈ (π/4)ℤ`, and `G_α` is dense in the projective
> unitary group otherwise.

- `α = π/4`: Bloch quarter turn about the second axis; Clifford; finite.
- `α = π/8`: Bloch eighth turn; T-type up to Clifford conjugation; predicted dense although `α/π`
  is rational. This is the conceptually important case: it shows that irrationality of the
  primitive angle is not the requirement.
- `α/π` irrational: predicted dense, and the preferred first formal density witness.

The reasoning behind the prediction, recorded and not claimed as proved: on the finite side, a
finite subgroup of `SO(3)` containing a quarter turn about one axis and a rotation about a
perpendicular axis lies in the octahedral group or in a cyclic or dihedral group with the first axis
principal, which forces the second rotation's Bloch angle into `(π/2)ℤ`, so `α ∈ (π/4)ℤ`;
conversely those angles are Clifford. On the dense side, an infinite closed subgroup of `SO(3)`
is `SO(3)` or lies in a conjugate of `O(2)`, and the perpendicular-axis geometry excludes the latter
outside the already-finite cases.

**Three ambition levels, frozen exactly.**

1. **Finite countercontrols, in the kernel.** Prove `G_α` finite for `α = k π/4`, at minimum for
   `α ∈ {0, π/4, π/2, 3π/4, π}` and preferably uniformly in `k`. The intended route is a finite
   invariant set: each generator permutes the six octahedral rays, and a projective unitary fixing
   all six is trivial, so the group embeds in the permutations of six points. Admissible outcome:
   the theorems, or the strongest uniform version obtainable with the shortfall stated.
2. **One positive density theorem, in the kernel.** With `α/π` irrational, the integer multiples
   of the Bloch angle are dense on the circle (Mathlib's `AddCircle.denseRange_zsmul_coe_iff`, the
   multiples of `a` dense on the circle of length `p` iff `a/p` is irrational), so the powers of
   `rot α` approximate every real rotation; conjugation by the quarter phase gives the same density
   about the perpendicular axis; an explicit two-axis Euler decomposition of `SU(2)` then gives every
   projective unitary as a product of three such rotations, and unitarity bounds the error of a
   product by the sum of the errors. The route is uniform in `α` over all irrational `α/π` if the
   decomposition is, and the theorem is stated at that generality if it closes there. Admissible
   outcome: the theorem for at least one witness, with the generality reached stated.
3. **The full classification.** `G_α` finite iff `α ∈ (π/4)ℤ`, dense otherwise. The finite-only-if
   direction and the dense direction at rational `α/π ∉ (1/4)ℤ` need the classification of finite,
   respectively closed, subgroups of `SO(3)`. If Mathlib lacks it, the exact missing theorem is
   named and the classification is recorded as the predicted target with a partial result. It is
   not added as a hypothesis to manufacture a proof. The `π/8` case is recorded as a prediction
   unless it is actually proved.

## The all-level lift, frozen as a route

> level-one dense pair control → relocation by `ExchangesAvailable` → dense two-level rotations on
> every pair of configurations → dense `U(2n)` at every level.

At level `n` the carrier is `Fin 2 × Fin n` and the fixed gate acts on the pair `(0, k), (1, k)`
for every ancilla value `k` at once. Every permutation of the `2n` configurations is available
(`avail_perm_of_ne` from the exchanges), and conjugating by a permutation moves a two-level
operation from one pair to any other pair. Level-one density on the pair, together with the phases,
gives density of two-level unitaries on any pair up to a unit scalar. Every unitary on a finite set
is a product of two-level unitaries, the Givens form. The proof is the approximate analogue of the
kernel's repertoire control theorem (`control_at_level`, `control_of_phaseFree`), with explicit
error accumulation: a product of `N` unitaries each approximated within `ε` is approximated within
`N ε`, by unitarity. Nothing here is an informal density argument; every step carries its bound.
If the explicit two-level decomposition is heavier than the positive-reachability route the exact
theorem uses, the choice is recorded and the bound is still explicit.

## The instrument fork, frozen

This is where the genuinely open mathematics sits and where outcome 2 lives. The exact chain in the
kernel is

> unitary control (`HasCompositeUnitaryControl`) → the Stinespring circuit
> (`stinespringCircuit_branch`, `FiniteIsometryExtensionSF`) → the Kraus assembly
> (`compositeCompleteness`, `HasFullCompositeInstruments`) → exact finite instruments
> (`exactComposite_of_soundExt_full`, `exactAll_of_conditions`).

The audit determines, step by step, whether each is quantitatively stable under approximation of the
unitary. The expected picture: the isometry extension of a Kraus family to a unitary on the
composite is a fixed algebraic construction; the instrument branch is obtained from that unitary by a
fixed preparation, a fixed readout and a fixed discard, each a bounded linear operation, so the
branch map is Lipschitz in the unitary and an approximating available unitary gives an
approximating available instrument. The closure properties used by the exact chain,
`IteratedAncillaClosure` and `availExt_bind`, are exact properties of `T` applied to the exactly
available approximant, not approximations. The candidate obstruction is a non-uniform constant in
the branch map, or a step of the exact chain that quantifies over all unitaries at a composite level
that the approximant does not reach. If a step fails, the exact unstable or unproved step is named
with the quantitative lemma it would need, and dense unitary control is not promoted to dense
quantum mechanics.

## Admissible outcomes, frozen

1. **Full success.** Discrete fixed-gate access gives dense unitary control and dense finite
   quantum mechanics; exact quantum mechanics is obtained only by the completion of D3. The physical
   source question then targets the discrete repertoire, not a primitive continuous pair flow.
2. **Unitary density succeeds, instrument density stalls.** The exact unstable or unproved
   Stinespring or Kraus step is named with the quantitative lemma required; density is claimed for
   unitary control only.
3. **Level-one or all-level density fails.** The counterexample or the exact mathematical
   obstruction is given; the continuous pair flow remains the exact completion frontier.

No outcome names or adopts C5, none says OI itself supplies the fixed gate, none claims exact
quantum mechanics from density without the completion, and none claims the full classification
kernel-proved unless it is.

## Tests, frozen

**T1. The predicates and the metric.** `FixedGateSourced`, `DenseUnitaryControl`, `DenseFiniteQM`,
the channel metric of D1, and the closure of D3, in the forms above; `mixImage` and every existing
definition unchanged. Admissible outcome: the definitions.

**T2. The bridge.** The lemma `‖U − V‖ ≤ ε → d(conjChannel U, conjChannel V) ≤ 2 ε` for unitary
`U, V`, and the unit-scalar invariance of the channel. Admissible outcome: the lemmas.

**T3. The finite countercontrols.** Ambition level 1. Admissible outcome: as stated there.

**T4. The density witness.** Ambition level 2. Admissible outcome: as stated there.

**T5. The classification.** Ambition level 3. Admissible outcome: as stated there; a partial
result with the missing theorem named is admissible; a hypothesis added to reach it is not.

**T6. The all-level lift.** `DenseUnitaryControl` for the fixed-gate theory from level-one
density, along the frozen route with explicit bounds. Admissible outcome: the theorem; or the
exact step at which the bound cannot be closed.

**T7. The instrument audit.** Each step of the exact chain classified stable or not, with the
lemma proved or the missing lemma named; `DenseFiniteQM` if every step is stable; `KrausSoundExt`
for the fixed-gate theory cited or proved. Admissible outcome: outcome 1 or outcome 2, with the
step named.

**T8. The completion.** D3 stated and proved for the density reached, with the theory-axiom
obligation proved or the failing axiom named. Admissible outcome: the statement, with its
status.

**T9. The surfaces and the checks.** Module `OIBridge/DiscreteCompletion.lean`, nothing named C5,
no continuous pair flow used in any constructive route, no irrationality condition stated as a
physical principle, no existing definition restated; guard `R7-DCA` pinning the predicates, the
bridge, the theorems, this note's order, prediction, outcomes, tests and non-doings, rejecting any
C5 naming, any claim that OI supplies the gate, any identification of density with exact
availability, any claim of the full classification beyond what is proved, any continuous pair flow
in the constructive route, and any manuscript edit; README paragraph and counts; the census
carries the family as kernel-only; the pair-flow equivalence note may receive one append-only
cross-reference section after its frozen text. Full build; every result printing only `propext`,
`Classical.choice`, `Quot.sound`; the release gate; the probe; the Bohr probe; the census; the voice
check. No manuscript is edited. Admissible outcome: all green.

**T10. The verdict.** Exactly one of the three outcomes, with the level-one status, the all-level
status and the instrument status each stated separately.

## What this round does not do

- Name or adopt C5, or call the fixed gate or any discrete repertoire C5.
- Claim that OI itself supplies the fixed mixing gate; the gate is a stated datum.
- Claim exact quantum mechanics from density without the completion operation of D3, or identify
  dense availability with literal exact availability.
- Claim the full non-exceptional-angle classification kernel-proved unless it is; claim the `π/8`
  case proved unless it is.
- Use a continuous pair flow, `PairFlow`, `PairFlowSourced`, or any `t ↦ α(t)` in any
  constructive route.
- Introduce an irrationality condition as a physical principle; the irrational witness is a
  mathematical convenience of the formal route, and the `π/8` prediction is what shows it is not
  the requirement.
- Retract or weaken the exact benchmark `qm_iff_derivedOI_pairFlowSourced` or the cardinality
  necessity of the coherent-continuum audit; density and exactness are different targets.
- Generalize beyond `Fin 2`.
- Change `mixImage`, `MixR`, `mixTheoryR`, `DerivedOI`, or any existing definition.
- Edit a manuscript.

The point of the round is to decide whether the continuous completion resource of the preceding
rounds was fundamental physics or an artifact of asking for exact availability instead of closure.

Status: preregistered; no proof attempted.

## Scope amendment, recorded after the preregistration

Recorded at review of the preregistration, before any proof; the preregistration above is
untouched, and the question, the targets, the prediction and the admissible outcomes are
unchanged.

**(1) Isolation before relocation in the all-level route.** At level `n > 1` the fixed gate
`mixImage n α` acts on every ancilla-indexed site pair `(0, k), (1, k)` in parallel, its matrix
block-diagonal in the ancilla index. Conjugation by a permutation moves that whole matching; it
does not by itself produce a single two-level gate. The all-level route therefore has a discrete
isolation step before the relocation step. The first formal positive route may use a phase-echo
identity: the sign flips that `DerivedOI` supplies (`flip_avail`, the quarter phase squared)
conjugate the parallel gate so that every unselected block sees the rotation by `−α` while the
selected block keeps the rotation by `α`, and the product with the original parallel gate cancels
the unselected blocks and leaves a single rotation at the doubled angle `2α` on the selected pair.
This suffices for the irrational-angle witness, since `2α/π` is irrational when `α/π` is. No claim
is made that this doubled-angle route propagates the `α = π/8` level-one prediction to all levels:
doubling `π/8` gives `π/4`, a Clifford angle, and the rational prediction at higher levels needs
either a better discrete addressing identity or a separate argument, neither promised here.

**(2) Resource density and quantum soundness are separate theorems.** `DerivedOI T ∧
FixedGateSourced α T` targets dense unitary control:

> `DerivedOI T ∧ FixedGateSourced α T → DenseUnitaryControl T`, for the successful angles.

A theory satisfying those two predicates may also carry an unrelated surplus operation that is not
Kraus, so full dense finite quantum mechanics additionally requires soundness:

> `DerivedOI T ∧ FixedGateSourced α T ∧ KrausSoundExt T → DenseFiniteQM T`, if the instrument
> audit succeeds.

To remove the redundancy in D2 and D3, `KrausDense T` is the density-only predicate, every finite
endomorphic Kraus instrument at every positive level approximable by available families in the
metric of D2, and `DenseFiniteQM T := KrausSoundExt T ∧ KrausDense T`; wherever the preregistration
writes "`DenseFiniteQM T` and `KrausSoundExt T`" it is read as `DenseFiniteQM T` alone. The
canonical fixed-gate theory `mixTheoryR {α} (Fin 2)` is the primary full-density target: its
soundness is proved separately, or cited if the kernel already carries it for generated theories,
and full `DenseFiniteQM` is concluded for it; the generated theory is never conflated with every
theory containing the same resources.

**(3) Two closure obligations in D3.** The closure of availability must satisfy the relevant theory
axioms, `availExt_coarse` and `availExt_bind`, as the preregistration records; and, separately,
the set of finite normalized Kraus instruments must be closed in the chosen channel metric:

> `G_j → F` in the metric of D2, with every `G_j` a finite endomorphic Kraus instrument, implies
> that `F` is one.

Soundness of every approximant does not by itself give this. The kernel carries the direction
from Kraus to completely positive, and its own comments record that the converse needs a
positive-semidefinite factorization; `ExactCompositeQuantumOps` is equality with the finite
Kraus-instrument predicate, so the inclusion of the closure in the Kraus instruments is a genuine
obligation of D3. It is proved, in finite dimension through the Choi matrix, closedness of the
positive-semidefinite and trace constraints, and a finite-dimensional Kraus representation, or it is
named as the exact D3 obstruction. `KrausSoundExt` of the approximating theory alone is not treated
as sufficient.

The level-one prediction, the irrational witness as the first kernel target, the `π/8` case as a
recorded and uncertified prediction, and the instrument audit as the home of outcome 2 are all
unchanged. `DerivedOI` supplies `IteratedAncillaClosure` (`DerivedOI.closure`), so that part of the
instrument route is not an additional hypothesis.
