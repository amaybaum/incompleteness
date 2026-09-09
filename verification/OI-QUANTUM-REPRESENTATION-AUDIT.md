# All-time quantum-representation boundary for `C_OI` — preregistration

Base: `main` at `6081a66a57426f4d9d1ac02e07f4412769f5d9c6` (post-PR #547).

This round opens Arc C of `OI-QM-RESEARCH-PROGRAMME.md`: determine the exact relation, in both
directions, between the finite-visible OI-realizable rooted class closed by PR #547 and the finite
quantum representation class. The objective is a **proved relation** — equality, one strict
inclusion, two-sided proper overlap, disjointness, or a characterized intersection — not a list of
examples on either side.

No construction, counterexample search, proof search, census, probe, or simulation has been executed
for this round before this preregistration. The drafting expectations recorded below are priors, not
evidence, and are disclosed for exactly that reason.

Authorship: this draft is written by the side that will take the adversarial target. The reviewer of
this draft is the freeze authority and does not inherit the drafting priors below.

## Why this round is not already closed by the merged equivalence

`OIBridge/Equivalence.lean` already proves, for each **fixed finite horizon** `K`, that three classes
of trajectory law `P(x_0, ..., x_K)` coincide:

- `(S)` the finite stochastic laws;
- `(D)` visible marginals of finite reversible deterministic systems under incomplete observation
  (`RevRealizable`);
- `(Q_fb)` laws of finite-dimensional unitary systems with fixed-basis Born readout
  (`QfbRealizable`).

`finite_horizon_equivalence` assembles the three implications. Read carelessly, that theorem appears
to answer Arc C already: if `D` and `Q_fb` coincide, the OI side and the quantum side are the same
class and there is nothing to determine.

That reading is invalid, and the reason it is invalid is the same quantifier gap that frozen control
13 of `OI-ROOTED-CLASSIFICATION-AUDIT.md` caught in the standing readback controls, now recorded in
`C4-CAUSAL-READBACK-AUDIT-AMENDMENT-1.md`:

`forall K exists R_K forall t <= K`  does not give  `exists R forall t`.

`finite_horizon_equivalence` is quantified inside `K`. It supplies, for each horizon, a
representation of that horizon's law, and the representing object may differ at every horizon. PR
#547 closed the **all-time** rooted class, where a single realization must agree at every time.

What the merged equivalence does not supply is any all-time inclusion, equality, or separation
between the two sides. It is not inert, and this round does not treat it as inert: correctly
quantified finite-horizon lemmas and consistency checks against it are legitimate, and T1 below
requires one. The prohibited move is the quantifier swap itself, not contact with the theorem.

This is the central hazard of the round and is frozen here before execution: **no all-time
inclusion, equality, or separation may be derived from a per-horizon equivalence, and every use of a
horizon-indexed result states its quantifier explicitly at the point of use.**

## Fixed inherited interfaces

Two interfaces are inherited exactly as merged. Neither may be altered, widened, or replaced by a
convenient variant.

### The OI side

`OIBridge.RootedClassification` and its chain, as merged by PR #547:

- `FiniteRootedRealizable Γ` — existence of a finite hidden carrier `H`, one reversible
  `step : V × H ≃ V × H`, and one prior `H → ℝ` common to every visible root, whose `rootedMap`
  equals `Γ t` at **every** `t`;
- `PPer Γ` — `Γ 0 = 1`, `IsRowStochastic (Γ t)` for every `t`, and `PeriodicFamily Γ`;
- `finiteRootedRealizable_iff_pper : FiniteRootedRealizable Γ ↔ PPer Γ`, for finite visible `V`.

The finite-visible restriction is inherited with the theorem. This round does **not** extend it, and
no Arc C result may be stated for infinite visible carriers.

### The representation side

`OIBridge.Equivalence.QfbReal`, as merged:

```lean
structure QfbReal (V : Type u) (K : ℕ) where
  Bas : Type u
  fB : Fintype Bas
  dB : DecidableEq Bas
  U : Matrix Bas Bas ℂ
  init : Bas → ℝ
  read : Bas → V
```

with `IsLaw` requiring `U` unitary and `init` a probability weight, `born b b' = ‖U b' b‖^2`, and the
trajectory weight `chain σ = init (σ 0) * ∏ born (σ k) (σ (k+1))`.

Three properties of that object are load-bearing for this round and are recorded now, before
execution, so that no target silently drifts to a different quantum class:

1. **One fixed unitary.** `U` does not depend on time. A time-dependent family `U_t` is a different
   class and is not the inherited one.
2. **Projective fixed-basis measurement at every step, with collapse.** `chain` is a product of
   one-step Born weights, so the basis-level law is the Markov chain of the Born matrix. It is not
   free unitary evolution, and the visible law is not `‖(U^t) b' b‖^2`.
3. **A readout that need not be injective.** `read : Bas → V` may be many-to-one, so the visible
   law is a **marginal** of a Markov chain and need not itself be Markov.

Property 3 is the one that keeps this round open rather than arithmetic. Properties 1 and 2 are the
ones most likely to be blurred by a hostile or careless reading, and either blurring would change the
class.

## The object being classified, and the translation obligation

The two inherited interfaces do not currently speak about the same object.

- The Arc B object is an **all-time rooted conditional family** `Γ : ℕ → Matrix V V ℝ`, with one
  prior on the hidden carrier shared by every root.
- The `Q_fb` object is a **bounded-horizon joint trajectory law** `P : Traj V K → ℝ`, with one
  initial law on the whole basis.

Before any comparison is meaningful, the round must construct the all-time rooted analogue of the
representation class. The merged `QfbReal` carries **one global** `init : Bas → ℝ` and no
root-indexed preparation field of any kind, so the rooted object is not inherited and must be
defined. That definition is frozen here, in full, because several inequivalent choices are available
and they can change the answers to T2 and T3.

### The frozen root-preparation map

Let `(Bas, U, init, read)` be a `QfbReal` datum with `U` unitary and `init` a probability weight, and
let `B_0, B_1, B_2, ...` be the fixed-basis Born process it induces: `B_0` distributed as `init`, and
`B_{k+1}` drawn from `born (B_k) ·` where `born b b' = ‖U b' b‖^2`.

`Γ ∈ Q*(V)` is defined to mean, with the quantifiers in exactly this order:

> `∃ Bas` finite with decidable equality, `∃ U` unitary, `∃ init` a probability weight on `Bas`,
> `∃ read : Bas → V`, such that
>
> - (positive root mass) `∀ a : V`, `∑_{b : read b = a} init b > 0`, and
> - `∀ a : V`, `∀ t : ℕ`, `∀ j : V`, `Γ t a j = P[ read (B_t) = j | read (B_0) = a ]`.

One basis, one unitary, one initial law and one readout serve **every** root and **every** time: the
existential block stands outside `∀ a, t, j` and may not be moved inside it.

Three alternative maps are available and are rejected here, by name, so that none can be adopted
after execution as though it had been the frozen one:

- **Root-indexed initial laws** `init_a` sharing `U` and `read`. That is a preparation family rather
  than one system, and `QfbReal` supplies no such field.
- **An OI-style common hidden prior** imported onto `Bas`. That transplants the OI side's own
  structure into the quantum side, and would make T3 partly true by construction.
- **Conditioning on a basis event finer than** `read (B_0) = a`. That gives the preparer access to
  the hidden basis label rather than to the visible root, and is not a visible root preparation.

The positive-root-mass clause is a genuine side condition, not a formality: conditioning is undefined
without it, and it restricts which `(Bas, init, read)` may witness membership. It is treated as part
of the class, and any result that turns on it is reported as turning on it.

The translation is a target of this round, not an assumption of it. Two failure modes are frozen as
disqualifying:

- **Defining `Q*` so that it is trivially `PPer`.** If the definition of `Q*` builds in periodicity,
  identity at the root time, or the OI prior structure beyond what the merged `QfbReal` supplies, the
  round has assumed its own answer. `Q*` must be recognizably the merged representation class
  re-expressed on the rooted all-time object, and the report must say which clauses were carried and
  which were dropped.
- **Defining `Q*` so that it is trivially empty or trivially everything.** Either outcome indicates
  a translation defect rather than a mathematical result, and must be reported as such.

Equality of families is exact, at every root, visible outcome, and time. Approximate agreement,
epsilon-shadowing, asymptotic agreement, and agreement on a prefix are not equality and may not be
reported as the relation.

## Independent targets, frozen before execution

The three targets are independent. No target may be reported as settled on the strength of another.

### T1 — the translation

Formalize `Q*(V)` exactly as frozen above, and state which clauses of the merged `QfbReal` are
carried, which are dropped, and why each choice is forced rather than convenient.

Then prove the finite-horizon compatibility theorem, stated so that it cannot be discharged by a
per-horizon family of unrelated representations. A truncation of `Γ` is a collection of rooted
marginals, not a joint trajectory law, so the object to be represented must be named rather than
assumed: for a `Q*` witness `(Bas, U, init, read)` and a root `a`, let `P^a_K` be the length-`K`
**root-conditioned trajectory law** — the joint law of `(read (B_0), ..., read (B_K))` conditioned on
`read (B_0) = a`, which the positive-root-mass clause makes well defined.

The theorem is: for every `K` and every root `a`, `P^a_K` is `QfbRealizable`, **and** the witnessing
representation is built from the same all-time `Bas`, `U` and `read`, with only the initial law
re-conditioned.

`∀K ∃Q_K` is explicitly not the statement. A proof supplying a different basis or unitary at each
horizon would satisfy that weaker form while establishing nothing about `Q*`, and would reintroduce
the quantifier swap this round exists to keep out.

T1 is a prerequisite for T2 and T3 and is not itself a relation result.

### T2 — the forward direction

Decide `Q*(V) ⊆ C_OI(V)`, equivalently by PR #547 whether every `Q*` family is in `PPer`.

Proved, refuted by an exhibited family with a proof that it is not periodic, or open. A failed search
for a non-periodic `Q*` family is not a proof of inclusion and may not be reported as one.

### T3 — the converse direction

Decide `C_OI(V) ⊆ Q*(V)`, equivalently whether every family in `PPer` admits a fixed-basis Born
representation at every time.

Proved, refuted by an exhibited `PPer` family with a proof that no representation exists, or open.
The refutation standard here is the higher one: an obstruction must be proved against **every** finite
basis, unitary and readout, not observed to hold at small dimensions. Bounded search at small
dimension is a control, never the refutation.

## Drafting expectation disclosure

The following are the author's priors before any execution. They are recorded so that the adversarial
work can be audited against them, and because the side holding them takes the adversarial target
rather than the direction they favour. **No prior below is evidence, and none may be cited in the
final report as support for any conclusion.**

1. **T2 is expected to fail on readout-injective systems and to be the harder question in general.**
   A stochastic matrix of finite multiplicative order is a permutation matrix. If the readout is
   injective the visible family is the Markov chain of the Born matrix `B`, and `Γ ∈ PPer` would force
   `B^M = I`, hence `B` a permutation matrix — collapsing the quantum side to the deterministic
   reversible one. The author therefore expects `Q* ⊄ C_OI`, witnessed by any Born matrix of infinite
   order. This is the prior most likely to be wrong in the direction of overconfidence, because it
   ignores property 3.
2. **Non-injective readout is where the round's real content sits.** A many-to-one `read` makes the
   visible family a marginal of a Markov chain, which need not be Markov and need not inherit the
   order argument. Whether periodicity can be manufactured by lumping states is, to the author,
   genuinely open.
3. **T3 is expected to fail for a support reason rather than a dynamical one.** Born matrices are
   unistochastic, hence doubly stochastic, while `PPer` requires only row stochasticity; a `PPer`
   family with a non-doubly-stochastic entry pattern is the obvious candidate obstruction. The author
   has not checked whether the readout marginal defeats this, and expects that it may.
4. **The overall relation is expected to be two-sided proper overlap**, with the intersection needing
   its own characterization. The author assigns low probability to equality in either direction.

Prior 1 and prior 3 both point at the same structural fact — that the merged representation class
carries constraints (`finite order`, `double stochasticity`) which `PPer` does not — and both are
weakened by the same escape (`read` non-injective). A reviewer should treat the correlation as a
single point of failure rather than as two independent expectations.

## Outcome taxonomy

Exactly one headline class is reported. The classes are disjoint by construction, and where more than
one description could be argued to fit, the precedence order is

`RC1 > RC2 > RC3 > RC4 > RC5`,

so a two-sided result is never reported behind a one-sided one, and a translation is never reported
as a relation.

The labels are `RC` rather than `C` deliberately: `C1`–`C4` name the manuscript's observation
conditions and `C_OI` names the class under study, so an outcome label of the form `C<n>` would
collide with both.

### RC1 — the relation is settled in both directions

Both inclusions are decided, each proved or refuted, and the resulting relation is stated exactly.
The possibilities are equality, strict inclusion in one direction, proper overlap, and
**disjointness**. This round does not presuppose which, and in particular does not presuppose that
the two classes meet at all. This closes the Arc C exit condition.

When both inclusions fail, RC1 additionally requires enough proved information about `C_OI ∩ Q*` to
distinguish proper overlap from disjointness. Two failed inclusions do not decide between those two
relations — a witness outside each class says nothing about whether anything lies in both — and
reporting them as though they did is the inflation this class exists to prevent.

### RC2 — one direction settled, the other open

Exactly one of T2, T3 is proved or refuted; the other remains open, with the gap stated explicitly.
Neither the settled direction nor the open one may be presented as the relation. This does not close
Arc C.

### RC3 — the intersection is characterized without either inclusion being settled

A proved characterization of `C_OI ∩ Q*` — including a proof that it is empty — that decides neither
inclusion. This is a positive mathematical outcome, it does not close Arc C, and it may not be
promoted to RC1.

RC2 and RC3 are disjoint as defined: RC2 requires exactly one inclusion settled, RC3 requires
neither. The precedence order above therefore never has to adjudicate between them, and neither
class carries a clause claiming priority over the other.

### RC4 — translation only

T1 lands and neither relation direction is settled. Reported as a definitional and formalization
result, never as a relation result, and never as evidence about either inclusion.

### RC5 — unresolved

No new general theorem in any of the three targets. Failed constructions, bounded searches, negative
results at small dimension, and formalization blockers may all be recorded here, and none of them is
promoted to a relation.

## Mandatory controls

1. **Horizon quarantine.** No all-time inclusion, equality, or separation may be derived from
   `finite_horizon_equivalence` or from any other per-horizon result. Correctly quantified
   finite-horizon lemmas and consistency checks are permitted, and T1 requires one. Every use of a
   horizon-indexed theorem states its quantifier explicitly at the point of use.
2. **Interface fidelity, OI side.** One finite hidden carrier, one reversible step, one prior common
   to every root. No root-dependent, time-dependent, or renormalized prior.
3. **Interface fidelity, quantum side.** One time-independent unitary, projective fixed-basis
   measurement at every step, one readout, and the frozen root-preparation map above. Any widening —
   time-dependent unitaries, POVMs, non-collapse evolution, ancilla refresh between steps, or any of
   the three rejected preparation maps — is a different class and requires a preregistered scope
   extension, not a refinement.
4. **Readout-injectivity split.** Every result states whether it holds for injective readout only or
   for general readout. A theorem proved under injective readout may not be reported as a theorem
   about `Q*`.
5. **Root-time identity and stochasticity.** Verified at every time for every candidate family on
   both sides, not at displayed endpoints.
6. **Double-stochasticity accounting.** Wherever unistochasticity or double stochasticity is used, it
   is stated as a property of the representation class and never silently attributed to `PPer`.
7. **Finite-basis accounting.** Every positive representation exhibits a finite basis with an
   explicit bound or finiteness argument; no disguised infinite-dimensional construction.
8. **Negative controls.** Any decision procedure or checker must reject families violating
   stochasticity, root identity, periodicity, and — on the representation side — unitarity.
9. **Bounded-search guard.** Exhaustion at small basis dimension is reported at its bounds and never
   extrapolated to a general obstruction. This is the standard that frozen control 12 of the Arc B
   round imposed and that the Arc B carrier lower bound was labelled under.
10. **Prior-disclosure control.** No conclusion may cite the drafting expectations above. If a result
    matches a prior, the report says so and says what independent evidence carries it.
11. **Arc-boundary guard.** Nothing here is promoted to physical sourcing, coherent control, phases,
    Hamiltonians, instruments, measurements as physical operations, composites, or Bell structure.
    Those are Arc D and Arc E. In particular #540 remains binding: mathematical unitary and Born
    representability does not source the physical coherent-control repertoire, and no result of this
    round may be read as doing so.
12. **Positive-root-mass accounting.** Every `Q*` witness supplies the positive-root-mass clause,
    and every result that depends on it says so. It is a support condition on the representation
    side and is reported the way frozen control 8 of the Arc B round required zero prior mass to be
    reported on the OI side.
13. **Corpus-consistency obligation.** If a theorem proved here contradicts or destabilizes a merged
    description, the result note records it and it becomes a backlog item. Immutable audits receive
    append-only amendments; mutable status surfaces are corrected in place. No manuscript, book,
    bibliography, or publication edit occurs in this round.

## Evidence hierarchy

1. **Kernel theorem preferred.** Both inherited interfaces are already in Lean, so relation results
   should be formalized there when feasible. No `sorry`, custom axioms, or `native_decide`; axiom
   dependencies remain within `[propext, Classical.choice, Quot.sound]`.
2. **Exact finite probes.** Legitimate for witnesses, candidate falsification and negative controls,
   never for a universal statement. A probe that verifies instances says so, at its bounds, in the
   same place the statement is made.
3. **Prose theorem.** Permitted where formalization is genuinely blocked, and the same place that
   states the theorem states that boundary.

Mathematical status and kernel status are separate facts and are reported separately.

## Non-doings

Before freeze and during this round, do not:

- widen either inherited interface, or substitute a more convenient quantum class;
- treat the per-horizon equivalence as an all-time equivalence;
- extend any result to infinite visible carriers;
- claim physical sourcing of any quantum resource, or read a representation result as one;
- apply or extend the Barandes correspondence beyond what `BARANDES-BOUNDARY-AUDIT-RESULT.md`
  already determined;
- classify Bell, composite, or nonlocal structure;
- introduce a fifth condition, or name or adopt one;
- edit manuscripts, books, bibliography, or publication claims;
- edit the programme roadmap before a result exists;
- report a failed search as a proof, in either direction.

Verification-facing documentation required to reconcile a theorem proved in this round is allowed at
final packaging, subject to frozen-file discipline.

## Execution discipline

- Freeze this preregistration by exact commit SHA **and blob SHA** before any construction, search,
  proof search, census, probe, or simulation. Blob identity is authoritative if a rebase becomes
  unavoidable.
- Once frozen, this file is immutable. Any execution-affecting correction is an append-only
  amendment, committed and frozen before the affected work.
- One PR for this research round.
- Record the post-freeze execution allocation before research begins. The author of this draft holds
  the adversarial targets; the freeze authority does not inherit the drafting priors.
- Final exact-head review is required after all result files, code, controls, registry updates and CI
  are complete.
- No merge occurs without an explicit owner direction after exact-head review.

## Allowed final report

The final report must state separately:

1. finite-visible scope, confirmed and stated as inherited rather than re-derived;
2. T1: the translation, with the clauses carried and dropped, and the horizon-truncation theorem;
3. T2: proved / refuted / open, with the readout-injectivity split explicit;
4. T3: proved / refuted / open, with the refutation standard met or the shortfall named;
5. the exact relation between `C_OI(V)` and `Q*(V)`, and whether the Arc C exit condition is met;
6. headline outcome RC1 / RC2 / RC3 / RC4 / RC5;
7. any characterization of the intersection, including a proof of disjointness if one is obtained,
   and whether its criterion is intrinsic or existential;
8. every place a horizon-indexed result was used, with its quantifier;
9. evidence type for every general claim, and the remaining formalization debt;
10. whether Arc C is mathematically closed and whether it is kernel-closed;
11. which drafting priors were confirmed, refuted, or untested, and what independent evidence carries
    each confirmed one;
12. whether Arc D can begin at a precise representation boundary, without executing Arc D here.

Status: **preregistered draft; no construction, counterexample search, proof search, census, probe,
or simulation has begun; nothing in this file is frozen until the reviewer approves an exact
commit and blob as the preregistration freeze.**
