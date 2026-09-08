# Intrinsic OI-realizable rooted stochastic class — preregistration

Base: `main` at `39ce478ba21c1c4c37cd95733025818effc4dda7` (post-PR #546).

This round opens Arc B of `OI-QM-RESEARCH-PROGRAMME.md`: characterize exactly which complete rooted
stochastic families are realizable by the finite reversible OI interface already formalized in the
repository. The objective is an **intrinsic visible-level characterization** of the class denoted
`C_OI`, not another list of examples and not a restatement of hidden realizability.

No sufficiency construction, counterexample search, proof search, brute-force census, probe, or
simulation has been executed for this round before this preregistration. The drafting expectation
below is a prior, not evidence.

## Fixed inherited interface

The target is the merged `CausalReadback.RootedRealization` / `rootedMap` layer, used exactly as it
stands after PR #546.

For a fixed finite visible carrier `V`, a realization consists of:

- a finite hidden carrier `H`;
- one deterministic reversible update `step : V × H ≃ V × H`;
- one fixed hidden prior `prior : H -> R`, **common to every visible root**;
- `prior h >= 0` and `sum_h prior h = 1`;
- the canonical visible projection after `t` iterations of `step`.

The rooted family is

`Gamma_t(a,j) = sum_h [ visible(step^t(a,h)) = j ] prior(h)`.

The inherited interface allows zero prior mass. **Full support is not part of the target.** No
root-dependent prior, time-dependent prior, changing observation map, stochastic microscopic update,
or nonreversible microscopic update may be introduced and still called the inherited class.

This round concerns **all** rooted realizations at this interface. The `CausalReadback` parent,
P-divisibility, tightness, and `N_CR` are not membership conditions for `C_OI`; those were Arc A
properties of particular realizations/families. Parent-negative and P-divisible rooted families are
inside the Arc B universe if they are realized by the inherited interface.

No assumption from Barandes, Hilbert-space representation, operational QM, coherent control,
composites, Bell structure, or physical accessibility is part of the class definition.

## The object being classified

For each finite visible carrier `V`, the primary object is the **complete infinite rooted family**

`Gamma : N -> Matrix V V R`,

not a finite observation window.

Define the semantic target class only for reference:

`Gamma in C_OI(V)`

iff there exist a finite `H` and an inherited `RootedRealization V H` whose `rootedMap` equals
`Gamma_t` for every `t`.

This existential hidden definition tells us what set we are trying to characterize. It does **not**
count as the requested characterization.

Equality is exact, for every root, visible output, and time. Approximate simulation, epsilon-shadow
realization, matching finitely many times, or matching only a process averaged over an initial
visible distribution is outside the primary target.

## What “intrinsic” means in this round

A full Arc B answer must put on the right-hand side of an iff a predicate of the visible family
`Gamma` itself.

The statement may use visible-level data such as:

- `V`, `Gamma`, natural times, and matrix entries;
- stochasticity, support, rank, convex/algebraic relations, equalities and inequalities among the
  visible matrices;
- visible temporal recurrence or a period of `Gamma`;
- a finite decision criterion computed from a proved finite visible description of `Gamma`.

The final RHS may **not** quantify over a hidden carrier, a reversible map on `V × H`, a hidden
prior, hidden trajectories, or an auxiliary object whose only content is “a reversible hidden
realization exists”. In particular,

`Gamma is intrinsically characterized iff Gamma admits a finite reversible OI dilation`

is tautological and is not a B1 result.

Hidden objects are of course allowed inside a proof of sufficiency or necessity. The restriction is
on what is presented as the final membership criterion.

A useful intermediate representation theorem that still contains hidden or dilation data is a
legitimate partial result, but it does not by itself close Arc B.

## Minimal visible candidate, frozen as a hypothesis rather than an answer

The inherited realization makes three visible properties immediate candidates for necessary
conditions. Define the audit-local class `P_per(V)` by:

1. **root identity:** `Gamma_0 = I`;
2. **stochasticity:** `Gamma_t` is row-stochastic for every `t`;
3. **finite temporal periodicity:** there exists an integer `M > 0` such that
   `Gamma_(t+M) = Gamma_t` for every `t`.

The period here is a visible period of the family; it is not assumed to equal `ord(step)` and need
not be minimal.

`P_per` is the **first candidate to test**, not a frozen conclusion. The round must not assume that
these obvious visible necessities are sufficient. In particular, the common-prior and common
reversible-dynamics constraints may impose additional cross-root or cross-time conditions that are
not visible from the three clauses separately. Discovering such a condition is an intended outcome,
not a failure of the round.

If `P_per` is too large, execution may refine the visible candidate by deriving additional
visible-level conditions and retesting necessity and sufficiency. Such refinement is within the
frozen full-class target and does not require an amendment provided the universe and inherited
interface are unchanged. Restricting the universe to a proper subclass because the full problem is
hard is different: that is a scoped partial outcome and may not be narrated as the full class.

## Independent targets, frozen before execution

The directions below are independent. Progress on one may not be used to reduce the effort on the
others, and failure of one is not evidence for another.

### T1 — necessity / visible envelope

Prove the strongest visible-level conditions that every inherited rooted realization must satisfy.

The first required theorem is

`C_OI(V) subseteq P_per(V)`.

If execution discovers an additional candidate condition `Q(Gamma)`, it may be added to the
proposed visible class only after proving

`Gamma in C_OI(V) -> Q(Gamma)`.

A condition fitted merely because it rejects attempted counterexamples is not a necessary condition.

T1 should state which consequences use only finiteness/reversibility, which use the common prior,
and which use the canonical visible projection.

### T2 — sufficiency / realization

Independently determine whether the visible candidate is sufficient.

The first falsifiable target is

`P_per(V) subseteq C_OI(V)`.

A positive result must be uniform over every finite `V` and every complete family in `P_per(V)`;
it must construct or otherwise prove existence of **one finite hidden carrier, one reversible
update, and one fixed prior common to all roots** that reproduces the entire family exactly.

If the candidate is refined by a proved visible necessity `Q`, the sufficiency target becomes the
correspondingly refined full visible class, not a hand-selected set of examples.

A finite carrier bound or explicit finite construction size should be reported whenever the proof
provides one. The construction may use zero-prior hidden states because the inherited interface
permits them, but that dependence must be stated rather than silently upgraded to a full-support
result.

### T3 — adversarial converse stress / nonrealizability

Independently try to falsify T2. Seek a complete visible family satisfying the current candidate
visible conditions but admitting **no** inherited realization.

The initial stress target is therefore a family

`Gamma in P_per(V)` but `Gamma notin C_OI(V)`.

Special attention should be paid to possible constraints created by:

- one prior shared across all roots;
- one reversible microscopic update shared across all roots and times;
- simultaneous consistency of different rooted rows;
- recurrence of the full microscopic dynamics versus recurrence visible only after marginalization.

A failed realization attempt is not a nonrealizability theorem. To refute T2, the round must exhibit
a family satisfying the candidate visible conditions **and prove that no inherited realization can
produce it**.

If such a counterexample exists, extract the visible obstruction it witnesses, return that
obstruction to T1 for a necessity proof, and then retest sufficiency. This adversarial loop is part
of the frozen target; it must not be stopped after the first plausible construction theorem or the
first small-carrier census.

## Preparation/prior scope, frozen before execution

The main class uses exactly the inherited common-prior interface.

The following variants are **not** interchangeable with the main target:

- full-support prior;
- uniform prior;
- rational prior;
- root-dependent hidden priors `mu(h|a)`;
- time-dependent priors;
- a chosen visible initial distribution mixed over roots.

If a theorem is proved only for one of these variants, report that scope explicitly. A theorem for
uniform or full-support priors is a proper-subclass result unless equivalence with the inherited
class is separately proved. A theorem using root-dependent priors belongs to a different model and
cannot establish sufficiency for `C_OI`.

Conversely, if the full inherited-class sufficiency proof relies essentially on adding zero-prior
hidden states, say so. That is allowed by the inherited definition but is scientifically relevant
when later arcs ask which preparations are physically sourced.

## Whole-family versus finite-window guard

Because the microscopic state space is finite and the update reversible, the inherited rooted
family is recurrent. Arc B therefore classifies the whole temporal object.

A theorem or probe matching

`Gamma_0, ..., Gamma_K`

for some finite `K` does not prove realization of the infinite family unless a separate theorem
shows that the finite data determine the continuation being claimed.

For a periodic candidate, checking one visible period may certify all times **only after** the
periodicity of both the target family and the constructed realization has been proved with the
correct alignment. A finite table of periods, carrier sizes, or visible dimensions is never an iff
classification of the unbounded class.

## Refutation and completeness standards

### T2 refutation

`P_per subseteq C_OI` is refuted only by a proved counterexample `Gamma in P_per` with
`Gamma notin C_OI`.

The following do not refute it:

- failure to find a realization;
- failure to formalize a construction;
- exhaustive search over bounded `|V|`, `|H|`, period, or a finite probability grid;
- numerical optimization that fails to reach zero error.

### T3 failure

Failure to find a counterexample does not prove T2. Sufficiency requires an actual theorem covering
all candidate families.

### Full classification

A finite census, however large, does not establish B1. A full iff requires both directions as
general theorems at the fixed inherited interface and an intrinsic visible RHS.

If a candidate class is changed during execution, the final report must preserve the history:
which candidate was tested, whether it was refuted or refined, and the theorem/counterexample that
forced the change. A final successful condition must not be presented as though it had been assumed
from the start.

## Drafting expectation disclosure

Before execution, the drafting expectation is that the minimal visible candidate `P_per` **may be
sufficient**, rather than requiring a further visible obstruction. This is only a prior. It is
motivated by the flexibility of the inherited interface, including arbitrary finite hidden
extension and the fact that zero prior mass is permitted; no uniform realization construction has
been built, inspected, probed, or proved for this round.

The prior is recorded because it creates an asymmetric risk: under-investment in T3 and premature
acceptance of a sufficiency construction. Therefore:

- it is not evidence for T2;
- T3 may not be weakened, deferred, or stopped because T2 looks promising;
- no failed T3 search may be cited as support for sufficiency;
- execution allocation must be recorded after freeze and before research begins, with the disclosed
  prior taken into account;
- if possible, the sufficiency and adversarial-nonrealizability directions should be executed by
  different people, as in the bias-control split used successfully in PR #546.

## Outcome taxonomy

The round must report exactly one headline class.

### B1 — full intrinsic characterization

For every finite visible carrier `V`, an intrinsic visible predicate `C*(Gamma)` is given and both
implications are proved:

`Gamma in C_OI(V)  <->  C*(Gamma)`.

The RHS passes the intrinsicness rule above. This is the full mathematical Arc B target.

### B2 — exact characterization of a proper named subclass

An iff is proved only after a genuine scope restriction, for example bounded visible cardinality,
bounded period, a named probability class, or a stronger prior condition, while the inherited full
class remains open.

This is a real result but does not close Arc B. The restriction must appear in the headline.

### B3 — two-sided partial boundary

General necessary visible conditions and a general sufficient visible class are both proved, or the
first candidate is rigorously refuted and a nontrivial refined boundary is established, but a gap
between necessity and sufficiency remains.

The gap must be stated explicitly; neither side may be promoted to an iff.

### B4 — one-sided general theorem

A nontrivial full-universe necessity theorem or sufficiency theorem is proved, but the opposite
direction remains open and no two-sided boundary strong enough for B3 is obtained.

### B5 — unresolved

No new general theorem closes either direction. Finite searches, examples, failed constructions, or
tooling/formalization blockers may be recorded, but they are not promoted to a mathematical
classification.

If a refined candidate eventually yields the full iff, the headline is B1 even if earlier candidates
were refuted; the final report retains those refutations as provenance.

## Mandatory controls

1. **Inherited-interface fidelity.** Every positive realization uses one finite `H`, one reversible
   `step`, and one normalized nonnegative prior shared by every visible root. No root-dependent
   preparation is allowed to slip into a construction.
2. **Root-time identity.** Verify `Gamma_0 = I` for inherited realizations and for every positive
   candidate family.
3. **Row stochasticity.** Verify it for every time, not only the displayed period endpoints.
4. **Whole-family periodicity.** Any positive inherited realization must have a proved finite visible
   period. The visible period is not silently identified with microscopic order.
5. **All roots simultaneously.** A construction that realizes each row using a different hidden
   model or a different prior does not realize the matrix family.
6. **Exact all-time equality.** Matching a finite window is insufficient without a theorem extending
   it to the complete family.
7. **Prior-support audit.** Record whether zero-prior hidden states are used. Do not call such a proof
   a full-support theorem unless full support is separately established.
8. **Finite-carrier accounting.** Every sufficiency proof must actually produce a finite hidden
   carrier, with a bound or finiteness argument explicit enough to rule out a disguised infinite
   construction.
9. **Negative visible controls.** The membership criterion/checker must reject at least families
   violating stochasticity, `Gamma_0 = I`, and temporal periodicity, so the implementation cannot
   pass vacuously.
10. **Refinement control.** If an extra visible condition is introduced after a counterexample, carry
    a control satisfying the previous candidate but violating the new condition, so the refinement
    has observable content.
11. **Finite-census guard.** Exhaustion at bounded carrier sizes or periods is reported only at those
    bounds and never extrapolated.
12. **Arc-boundary guard.** No result here is promoted to quantum representation, operational QM,
    physical accessibility, or Bell/composite structure. Those belong to later arcs.

## Evidence hierarchy

Every final claim carries its evidence type.

1. **Kernel theorem preferred.** The existing `RootedRealization` and `rootedMap` interfaces are
   already in Lean, so necessity and sufficiency should be formalized there when feasible. No
   `sorry`, custom axioms, or `native_decide`; foundational axiom dependencies remain limited to the
   repository standard.
2. **Exact finite probes.** Useful for constructions, candidate falsification, and negative controls,
   but never sufficient for a universal iff.
3. **Prose theorem.** Permitted when an interface/formalization gap genuinely blocks kernelization,
   but the same place that states the theorem must state that evidence boundary. Formalization
   failure is not mathematical failure.

A mathematical B1 result and its formalization status are separate facts. If the iff is established
mathematically but not kernelized, the report may say so, but the roadmap must not imply
kernel-closure that was not achieved.

## Non-doings

Before freeze and during this round unless required by the fixed targets, do not:

- apply the Barandes correspondence or characterize the quantum representation class;
- source coherent control, phases, Hamiltonians, instruments, measurements, or composites;
- classify Bell/nonlocal correlations;
- add a physical accessibility interpretation to recurrence or period;
- require the `CausalReadback` parent as a condition of `C_OI`;
- replace the inherited common prior by a root-dependent preparation family;
- change the canonical visible projection or microscopic reversibility assumption;
- edit manuscripts, books, bibliography, or publication claims;
- edit the programme roadmap before a result exists;
- treat the semantic hidden definition of `C_OI` as the requested intrinsic answer.

## Execution discipline

- Freeze this preregistration by exact commit SHA and blob SHA before any sufficiency construction,
  counterexample search, proof search, brute-force census, new probe, or simulation.
- Once frozen, this file is immutable. Any execution-affecting correction or scope change is an
  append-only preregistration amendment, committed and frozen before the affected work.
- Candidate refinement within the fixed full-class target is allowed as described above; narrowing
  the universe or changing the inherited interface is a scope change and must not be hidden as a
  refinement.
- One PR for this research round.
- Record the post-freeze execution allocation before research begins; the reviewer of this draft is
  the freeze authority.
- If rebasing becomes unavoidable, verify by blob hash; blob identity is authoritative.
- Final exact-head review is required after all result files, code, controls, registry/roadmap updates
  and CI are complete.
- No merge occurs without an explicit owner direction after exact-head review.

## Allowed final report

The final report must state separately:

1. T1 necessity: proved / partial / not settled, with every visible condition proved necessary;
2. T2 sufficiency: proved / refuted / partial / not settled, naming the exact candidate class;
3. T3 adversarial stress: counterexample proved / no counterexample found / superseded by a general
   theorem, never confusing failed search with proof;
4. the final intrinsic candidate `C*` and whether `C_OI <-> C*` is actually proved;
5. headline outcome B1 / B2 / B3 / B4 / B5;
6. prior/support scope, especially whether zero-mass hidden states are used;
7. evidence type for every general claim and the remaining formalization debt, if any;
8. whether Arc B is mathematically closed and whether it is kernel-closed;
9. whether Arc C can begin at a precise `C_OI` interface, without executing Arc C in this round.

Status: **preregistered draft; no sufficiency construction, counterexample search, proof search, brute-force census, probe, or simulation has begun.**