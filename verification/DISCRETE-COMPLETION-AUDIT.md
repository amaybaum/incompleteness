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

## The outcome

Preregistration commit `d4deada`, scope amendment `0a6ccbb`, executed from `main` at `1cb923d`.
The kernel module is `OIBridge/DiscreteCompletion.lean`, fifty-one named results, each printing
only `propext`, `Classical.choice`, `Quot.sound`; the kernel is at 133 modules and 2,941 named
results. Nothing is named "C5" in the module or adopted in this note; no continuous pair flow
enters any constructive route; no irrationality condition is stated as a physical principle;
nothing is generalized beyond `Fin 2`; no existing definition changes; no manuscript is edited.
The verdict is **outcome 2, unitary density succeeds, instrument density stalls**: dense unitary
control is proved at every level, for every fixed angle with `α/π` irrational, and the instrument
half stops at named steps of the exact Stinespring and Kraus chain, each stated below with the
lemma it would need.

**The predicates and the bridge (T1, T2).** `FixedGateSourced α T`, `ChanWithin ε Φ Ψ`,
`DenseUnitaryControl T`, `KrausDense T`, `DenseFiniteQM T := KrausSoundExt T ∧ KrausDense T` and
`ClosureAvail` are defined in the frozen forms, with the amendment's separation of density from
soundness. Unitaries have operator norm one (`norm_eq_one_of_unitary`); unitaries within `ε` have
conjugation channels within `2 ε` (`conj_within`), the constant `2` as frozen; and a product of two
unitaries is within the sum of the errors (`norm_mul_sub_mul_le`), the only error-accumulation
rule the round needs.

**The block algebra and the C*-identity bound.** The ancilla projector `anc k₀` and its
complement address one site pair: `blockOnly k₀ M` is `M` on the pair with ancilla value `k₀` and
zero elsewhere, `blockOf k₀ M` the same with the identity elsewhere; both are tensor forms, so the
group law, the adjoint and unitarity are one-line tensor identities (`blockOf_mul`,
`blockOf_unitary`). The distance from an addressed rotation to the identity is bounded by the
angle through the C*-identity `‖A‖² = ‖Aᴴ A‖` and the Gram matrix `(rot δ − 1)ᴴ (rot δ − 1) =
(2 − 2 cos δ) · 1` (`rot_sub_one_gram`, `blockOnly_rot_sub_one_norm_le`, `blockOf_rot_dist_le`),
with no passage between entries and the operator norm anywhere.

**The Euler decomposition.** The addressed quarter phase `S2`, the exchange `X2` and the
perpendicular rotation `rx θ = S2 · rot θ · S2ᴴ` (`rx_eq_conj`) give the product formula
`rot_rx_rot`. A two-by-two unitary of determinant one has the special-unitary form (`su2_form`),
every unitary is a unit scalar times one (`exists_unit_scalar_su2`), and the special-unitary form is
`rot a · rx b · rot c` for real angles obtained from two planar arguments and one arcsine
(`euler_of_su2`, `euler_of_unitary`).

**T4, density from one irrational angle.** The integer combinations of `β` and `2π` are dense when
`β/π` is irrational (`dense_angles`), by the dense-or-cyclic dichotomy for subgroups of the line
(`AddSubgroup.dense_or_cyclic` with `AddSubgroup.mem_closure_pair`); the preregistration named the
circle-density form of the same theorem, and the executed route uses the dichotomy it rests on,
the Mathlib module of the circle form not being in the project's build cache. A block repertoire,
a set containing the identity, closed under products, containing the addressed rotation by `β`,
the addressed quarter phase and the addressed exchange (`BlockRepertoire`), approximates every
addressed rotation (`rot_approx`, through integer powers, the exchange for negative multiples and
`2π`-periodicity) and every addressed perpendicular rotation (`rx_approx`), hence every addressed
special unitary within any `ε` by three approximations (`dense_block_su2`). At level one the
available set of a theory with the closure and the fixed gate is such a repertoire
(`blockRepertoire_levelOne`), and every unitary at level one is approximated up to a unit scalar by
an available unitary (`levelOne_dense`). The theorem is uniform over all `α` with `α/π`
irrational, not one witness.

**T6, the all-level lift.** Isolation as the amendment records: the sign flips over any finite set
of configurations are available (`flipSet_avail`); conjugating the parallel gate by the flips on
the configurations with site value one and ancilla value other than `k₀`, and multiplying by the
parallel gate again, cancels every unselected block and leaves the rotation by `2α` on block `k₀`
(`echo_identity`), so the isolated gate is available at every level (`isolated_mem_availSet`) and
the available set at every level is a block repertoire at the doubled angle on every block
(`blockRepertoire_level`, with `2α/π` irrational when `α/π` is). Relocation: a permutation carries
any pair to any pair (`exists_perm_pair_map`), every permutation is available from the exchanges, and
the relocated addressed gate is approximated on every pair (`relocated_dense`). The Givens step is
carried out in full and not left named: the two-level matrix on a pair is written in the Sylvester
form `1 + ι (M − 1) ιᵀ` with `ι` the inclusion of the pair (`incl`, `twoLevel`), which makes the
group law, the adjoint and unitarity algebraic (`twoLevel_mul`, `twoLevel_unitary`) and the
determinant the determinant of the block by `det (1 + A B) = det (1 + B A)` (`det_twoLevel`);
the relocated gate is the two-level matrix on the carried pair (`relocated_eq_twoLevel`). Every
special unitary supported on a finite set of indices is a product of two-level special unitaries
(`su_mem_closure_of_suppOn`, `su_mem_closure_twoLevel`): the column of one index is cleared by
Givens blocks (`givens`, unitary and of determinant one, `givens_kill`), the unit phase that
remains is pushed onto another index by a diagonal special-unitary block (`phaseBlock`), the row is
then trivial by unitarity (`row_zero_of_col_zero`), and the rest is supported on fewer indices;
when one index remains the determinant fixes its phase. Products of approximable unitaries are
approximable with the errors added (`closure_approx`, by closure induction, so no factor count is
needed), every special unitary at every positive level is approximated (`su_dense`), every unitary
is a unit scalar times a special unitary on any finite carrier (`exists_unit_scalar_su'`), and
**D1 holds** (`denseUnitaryControl_of_fixedGate`): under `DerivedOI` and one fixed gate at any
angle with `α/π` irrational, dense unitary control at every level, level zero included.

**T3, the finite countercontrols.** The level-one group generated by the fixed gate, the quarter
phase and the exchange (`Gen2 β`) is finite up to scalar at `π/4`
(`gen2_pi_div_four_finite_upToScalar`): every element normalizes the sixteen-element Pauli set
(`Pauli`, `pauli_mul`, `Gen2.pauli_conj`, from the six conjugation identities
`rot_pi_div_four_X`, `rot_pi_div_four_Z`, `S2_X2`, `S2_Z2`, `X2_X2`, `X2_Z2`), two elements with the
same action on `X` and `Z` are proportional because the commutant of `X` and `Z` is the scalars
(`scalar_of_comm_XZ`, `proportional_of_same_conj`), and the action takes finitely many values.
Uniformly in `k ∈ ℤ`, the group at `k π/4` sits inside the group at `π/4` (`Gen2.subset_pi_div_four`)
and is finite up to scalar (`gen2_multiple_finite_upToScalar`). Ambition level 1 is reached in its
strongest uniform form.

**T5, the classification.** Ambition levels 1 and 2 are reached, each uniformly: finite up to
scalar at every multiple of `π/4`, dense at every `α` with `α/π` irrational. The predicted
classification is not kernel-proved in either remaining direction. That finiteness forces
`α ∈ (π/4)ℤ` needs the classification of finite subgroups of `SO(3)`; that density holds at
rational `α/π` outside `(1/4)ℤ`, the `π/8` case included, needs the classification of closed
subgroups of `SO(3)`. Neither is in Mathlib, neither was added as a hypothesis, and both are
recorded as the exact missing ingredients. The `π/8` case stays a prediction.

**The canonical theory.** The stated access with the datum at one angle, `fixedGateTheory α :=
mixTheoryR {α} (Fin 2)`, satisfies the closure (`fixedGateTheory_derivedOI`, through the
dagger-stability and context-stability of the fixed-angle class, the adjoint of the gate being its
exchange conjugate: `mixR_singleton_daggerStable`, `mixR_singleton_contextStable`), sources the
gate (`fixedGateTheory_fixedGateSourced`), is Kraus-sound as every implementation-generated theory
is (`fixedGateTheory_krausSoundExt`), has dense unitary control at every angle with `α/π`
irrational (`fixedGateTheory_denseUnitaryControl`), and is not exact quantum mechanics
(`fixedGateTheory_not_qm`, the construction audit's countable-angle negative): density is not
exactness. The angle one radian is a concrete witness (`fixedGateTheory_one_denseUnitaryControl`,
from the irrationality of `π`).

**T7, the instrument audit: where the chain stops.** The exact chain
`HasCompositeUnitaryControl → shift → circuit_available_pureSeed → stinespringCircuit_branch →
fullInstruments_of_control → compositeCompleteness → exactComposite_of_soundExt_full` consumes
exact composite unitary control at two structural places, and `KrausDense` is not claimed.
(i) The shifted theory `shift T hctrl hin hclos n`, through which the composite levels are
reached, takes exact control as an argument: its composite identity is `availExt_id_of_control`,
and it also takes inert-spectator compositionality, which is not among the conjuncts of
`DerivedOI`. Under dense control the identity itself is available at every level from the
exchanges alone (`one_mem_availSet`), so that obligation is discharged; but the shifted theory is
stated with exact control and would need restating with identity availability in its place, and
inert-spectator compositionality would need proving for the theory. (ii) `circuit_available`
requires the Stinespring unitary `U` of the target instrument itself to be available. Under dense
control an available approximant `V` within `ε` of `U` exists, and the circuit built from `V` is
available by the same closure properties; the distance between the two circuits, in the channel
metric at the composite carrier, is controlled by a Lipschitz bound for the branch map
`U ↦ discardMap ∘ localLuders ∘ conjChannel U`, which is not proved. The quantitative lemma
required is therefore: the branch map is Lipschitz in the operator norm of `U` with a constant
depending only on the carrier, together with the shifted-theory construction under identity
availability and inert-spectator compositionality for the fixed-gate theory. Dense unitary control
is not promoted to dense quantum mechanics.

**T8, the completion.** `ClosureAvail` is defined as frozen. Its two obligations are named and not
proved: that the closed availability satisfies `availExt_coarse` and `availExt_bind`, and that the
finite normalized Kraus instruments are closed in the channel metric. No completion statement is
made beyond the definition.

| test | outcome | kernel |
|---|---|---|
| T1 | the predicates and the metric, in the frozen forms, density separated from soundness | `FixedGateSourced`, `ChanWithin`, `DenseUnitaryControl`, `KrausDense`, `DenseFiniteQM`, `ClosureAvail` |
| T2 | the bridge at constant two, unit norm of unitaries, the product error rule | `norm_eq_one_of_unitary`, `conj_within`, `norm_mul_sub_mul_le` |
| T3 | finite up to scalar at `π/4` and uniformly at every `k π/4` | `Gen2.pauli_conj`, `scalar_of_comm_XZ`, `proportional_of_same_conj`, `gen2_pi_div_four_finite_upToScalar`, `gen2_multiple_finite_upToScalar` |
| T4 | density at level one for every `α` with `α/π` irrational: dense angles, the block repertoire, the Euler decomposition | `dense_angles`, `BlockRepertoire.rot_approx`, `BlockRepertoire.rx_approx`, `BlockRepertoire.dense_block_su2`, `euler_of_su2`, `euler_of_unitary`, `blockRepertoire_levelOne`, `levelOne_dense` |
| T5 | levels 1 and 2 reached uniformly; the finite-only-if direction and the rational non-exceptional case not proved; the classifications of finite and of closed subgroups of `SO(3)` named as the missing ingredients; `π/8` a prediction | the theorems of T3 and T4 |
| T6 | isolation by the echo, relocation, two-level density on every pair, the Givens decomposition, dense unitary control at every level | `echo_identity`, `isolated_mem_availSet`, `blockRepertoire_level`, `relocated_dense`, `det_twoLevel`, `su_mem_closure_twoLevel`, `closure_approx`, `su_dense`, `denseUnitaryControl_of_fixedGate` |
| T7 | outcome 2: the chain consumes exact control in the shifted theory and in the circuit availability; the Lipschitz bound for the branch map, the shifted theory under identity availability and inert-spectator compositionality named; `KrausDense` not claimed; the canonical theory Kraus-sound | `fixedGateTheory_krausSoundExt`; the named lemmas |
| T8 | the closure defined; its two obligations named, not proved | `ClosureAvail` |
| T9 | the surfaces and the checks: `R7-DCA`; README and census, the family kernel-only; the pair-flow equivalence note's cross-reference section; full build, axiom check, gate, probe, Bohr probe, census, voice check; no manuscript edited | `verification/lean/edge_rigidity_probe.py` |
| T10 | the verdict: outcome 2, with the level-one, all-level and instrument statuses stated | this section |

**The verdict, with its content.** Outcome 2 is reached. Discrete fixed-gate access, one gate at
one angle with `α/π` irrational on top of the closure, gives dense unitary control at every level,
with the continuum entering only in the closure of what is executable: every unitary at every level
is a limit of available unitaries, and the fixed-gate theory itself is not exact quantum
mechanics. Dense finite quantum mechanics is not reached, because the exact instrument chain is
built on exact composite control at two places, and the quantitative replacement is named and not
proved. Outcome 1 is not reached; outcome 3 is not reached.

**What the outcome means.** On the unitary side the question of the round is answered: the
continuous pair flow of the preceding rounds is not needed for dense unitary control, one fixed
discrete gate suffices, and the continuity that exact quantum mechanics carries appears in the
completion of the generated repertoire and not as primitive executable structure. On the
instrument side the answer is deferred to a quantitative audit of the Stinespring and Kraus
assembly, whose missing lemma is stated. The exact benchmark of the equivalence audit stands
untouched: exact finite quantum mechanics on the two-valued carrier remains exactly the closure
with one sourced pair flow, and the fixed-gate theory, dense in the unitaries, is not it. The
`π/8` prediction, that irrationality of the primitive angle is not the requirement, is unchanged
and unproved; the irrational witness is the formal route's convenience and nothing more. The
manuscript status of the state-mixing resource is unchanged.

**What the outcome does not establish.** `KrausDense` or `DenseFiniteQM` for any theory. Any
completion statement beyond the definition of the closure. The full level-one classification, or
density at any rational `α/π`. That OI itself supplies the gate; the gate is a stated datum.
That exact quantum mechanics follows from density. Anything about a manuscript.

## What this note does not claim

That dense finite quantum mechanics, or the completion of D3, holds for the fixed-gate theory or
any theory; only dense unitary control is proved. That the level-one classification is
kernel-proved beyond the multiples of `π/4` and the irrational angles, or that the `π/8` case is
dense. That OI itself supplies the fixed gate. That density is exactness, or that exact quantum
mechanics follows from density without the completion operation, which is only defined here. That
anything is named C5. That any manuscript statement changes.

Status: pass complete. Outcome 2, unitary density succeeds, instrument density stalls: the
predicates and the bridge, the block algebra with its C*-identity bound, the Euler decomposition,
density at level one from one irrational angle, isolation by the sign echo, relocation, the Givens
decomposition and dense unitary control at every level, the finite countercontrols uniformly at
every multiple of `π/4`, the canonical fixed-gate theory with the closure, the sourced gate,
soundness, dense unitary control and no exactness, and the instrument chain's consumption of exact
control named with its missing lemma; fifty-one named results; no C5 named or adopted; no
manuscript edited.
