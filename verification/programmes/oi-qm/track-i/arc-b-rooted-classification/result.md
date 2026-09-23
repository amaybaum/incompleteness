# Intrinsic OI-realizable rooted stochastic class — result

Determination for `verification/programmes/oi-qm/track-i/arc-b-rooted-classification/preregistration.md`, frozen at commit
`945aa89484badb0b4c064693fe5b2006d049b778`, authoritative blob
`1dd761349a9f319fc7e507814b7acdbb85c3eb78`. Executed on branch `oi-rooted-classification-audit`
from clean `main` at `39ce478ba21c1c4c37cd95733025818effc4dda7`.

## Headline outcome — B1, finite visible carrier

For every finite visible carrier `V`, the class realizable by the inherited reversible interface is
characterized by a predicate on the visible family alone:

`Gamma in C_OI(V)  <->  Gamma_0 = I  and  every Gamma_t is row-stochastic  and  Gamma has a positive finite period`.

In the kernel:

```lean
theorem finiteRootedRealizable_iff_pper (Γ : ℕ → Matrix V V ℝ) :
    FiniteRootedRealizable (V := V) Γ ↔ PPer Γ
```

`OIBridge.RootedClassificationAllTime`, axioms `[propext, Classical.choice, Quot.sound]`.

The intrinsic candidate `C*` is `PPer`, and `C_OI(V) <-> C*` is **proved**, in both directions, as a
single named theorem rather than as a pair of one-way lemmas with a prose bridge. Its right-hand
side quantifies over nothing but the entries of `Gamma` itself: no hidden carrier, no reversible
update, no prior appears in it. That is what the frozen intrinsicness rule asks for, and it is why
the round reports B1 rather than the structural class B5, which a carrier bound alone would earn.

Evidence type: **kernel theorem**, both directions. There is no formalization debt on the headline
result and no prose step carrying any part of it.

### Integrated into the ordinary kernel gate

The result is not certified by a bespoke command. The three modules of the chain are imported from
the bridge root `OIBridge.lean`, so a bare `lake build` reaches them; every one of the chain's 40
named results carries a `#print axioms` line; and the R7-RCL guard in
`verification/lean/edge_rigidity_probe.py` enforces the architecture rather than a count — root
reachability, absence of a module-specific CI target, and equality of the declared theorem-name set
with the print-target set, module by module (16 / 8 / 16).

### Necessity

`pper_of_finiteRootedRealizable`, assembled from `rootedMap_zero`, `rootedMap_isRowStochastic` and
`rootedMap_periodic`. The visible period is obtained from the finite order of the microscopic
permutation and is proved for the complete family, not read off a window; control 5 is discharged
by the theorem itself, since the visible period is never identified with the microscopic order —
only bounded by it.

### Sufficiency

`pper_has_responseRealization`, then `finiteRootedRealizable_iff_pper`. The frozen quantifier order
is preserved exactly: **for every** `Gamma` in `P_per` **there exists** one finite `H`, one
reversible `step : V × H ≃ V × H`, and one prior common to every root, agreeing with `Gamma` at
**every** time. Agreement is proved on the first period (`rootedMap_responseRealization_first_period`)
and then propagated by the microscopic period return (`rootedMap_responseRealization_add_period`,
`responseRealization_agrees_all`), which is what discharges frozen control 7: no window is
extrapolated.

The hidden carrier is a response table together with root-labelled zero-prior padding, so for period
`M` its cardinality is exactly

`|H| = |V|^(|V|(M-1)) * (1 + |V|(M-1))`,

finite and explicit; control 9 is discharged by construction rather than by an argument that some
finite carrier must exist.

### Adversarial stress

No counterexample. T3's search over hostile families, a bounded-padding attack, and a counting
attack all closed, and the counting attack closed for a proved reason — the carrier lower bound
below does not cross the construction's upper bound at any `M` — rather than by exhaustion. The
adversarial direction is **superseded by the general theorem**: once sufficiency is proved for all
of `P_per`, no counterexample can exist inside it.

## Scope

Six qualifications stand beside the result. None of them weakens it; each of them bounds it.

1. **Finite visible carriers only.** `RootedRealization` requires `[Fintype H]` but not
   `[Fintype V]`. Finiteness of `V` is an additional restriction, declared before freeze because it
   is load-bearing for periodicity. Arbitrary visible carriers are **not** classified by this round,
   and neither the periodicity necessity nor the iff may be promoted to the arbitrary-`V` kernel
   interface. Extending to infinite `V` is a separate scope requiring its own preregistration.

2. **Zero prior mass is used, and it is provably necessary.** The response-table realization gives
   the padding states prior zero. This is not tidied away, and it cannot be: the full-support
   separation below exhibits a family in `P_per`, realizable at the inherited interface, with no
   full-support realization at all. The theorem is therefore a theorem about the inherited class,
   which permits zero mass, and it is **not** a full-support theorem. Frozen control 8 is discharged
   by recording exactly this.

3. **T3 was not blind.** The adversarial half of the round began after exposure to the T2
   construction. Its hostile families were chosen against a construction already seen. That is a
   weaker adversarial posture than a blind attack and is reported as such wherever T3 is cited.

4. **A no-counterexample search is not evidence for sufficiency.** T3's exact probes are controls,
   not support. The sufficiency claim rests on the kernel theorem alone; had the theorem failed,
   nothing in the probe would have stood in for it.

5. **The two side results are supporting results.** The full-support separation and the carrier
   lower bound are proved and are worth keeping, but neither is part of B1 and neither is offered as
   partial evidence for it.

6. **The author/reviewer split was crossed once, at `07e33c8`.** The T2 and T3 halves were allocated
   to opposite sides. When the all-time agreement chain failed to close in the kernel, the T3 side
   diagnosed and repaired it, so commit `07e33c8` is T2 mathematics written by the adversarial
   author. The crossing is disclosed rather than smoothed over; the repair is a kernel proof and is
   checked by the same gate as everything else, which is the only reason it is acceptable at all.

## Supporting results

### Full-support separation

> If `|V| >= 2` and `Gamma_t(a,j) = Gamma_t(b,j) = 1` for distinct roots `a`, `b`, then `Gamma` has
> no inherited realization whose prior has full support.

Full support forces `visible(step^t(a,h)) = j` for every `h`, and likewise from `b`, so `step^t`
carries `2|H|` states into `|H|`; injectivity gives `|H| = 0`, against normalization. The witness is
in `P_per` and **is** realizable at the inherited interface, so this separates the inherited class
from its full-support variant rather than restricting the class. Zero-prior padding is unavoidable
on such a family, not an artifact of one construction.

Evidence: **prose theorem**. The counting argument above covers every finite `|H|`; it is not
kernelized, and no probe establishes it. Section C of
`verification/lean/rooted_classification_t3_probe.py` supplies the witness — that it lies in
`P_per`, that it drives two distinct roots deterministically onto one visible value, that it is
realizable at the inherited interface, and that the realization carries zero-prior states — together
with a bounded control at `|H| <= 3` on a sixths grid and a refinement control confirming that a
family without a deterministic collision is not excluded by the theorem. Those are a witness and
controls at their stated bounds. Neither the bounded control nor any other executed check
establishes the universal statement, and neither is offered as doing so. Not load-bearing for B1.

### Carrier lower bound

> `dim_Q span_Q { Gamma_t(a,j) } <= |H|` for every inherited realization, since each entry is a
> subset sum of the `|H|` numbers `prior h`.
>
> Hence no carrier bound is a function of `|V|` alone: at `|V| = 2` there are period-`M` families in
> `P_per` forcing `|H| >= M`, for every `M`.

This is an existential worst-case bound, not a pointwise claim and not a `Theta(M)` claim.

Evidence: **prose theorem**, for the lemma and for the corollary alike. Neither is kernelized. The
corollary's arbitrary-`M` statement rests additionally on the classical linear independence over the
rationals of square roots of distinct primes, which is cited rather than proved here.

Section D of the probe executes **instances at `M = 1..20`**, over a fixed list of thirty primes: for
each `M` it computes the family's exact rational span dimension, checks the row sums, checks the
range condition `4q <= D^2` as integer arithmetic, and checks that the forced carrier does not cross
the construction's upper bound; it then carries the denominator negative control at 2503. That
sweep verifies twenty instances and gives the denominator repair observable content. **It does not
prove the statement for every `M`**, and under frozen control 12 it is reported at its bounds and is
not extrapolated. A reader who wants the arbitrary-`M` claim has the prose argument for it and
nothing executable.

### Standing-control reconciliation

Frozen control 13 fired the moment periodicity necessity was certified, and is discharged in
`verification/audits/physical-realization/c4-causal-readback/amendments/amendment-1.md`, append-only, with the frozen C4 audit left
untouched. Three statements are kept apart there:

- the complete `pdFamily` is nonperiodic, hence outside the class (`pdFamily_not_periodicFamily`,
  `pdFamily_not_finiteRootedRealizable`);
- the complete `peFamily` is nonperiodic, hence outside it too (`peFamily_not_periodicFamily`,
  `peFamily_not_finiteRootedRealizable`);
- `build(K)` establishes `∀K ∃R_K ∀t ≤ K`, which does not give `∃R ∀t`. The quantifier swap is
  invalid in general and fails for these two families in particular.

For all-time `RootedRealization` semantics the frozen wording is superseded by that amendment: a
sentence true of horizon objects becomes false read as a claim about the complete families, and the
later theorem is what makes the difference decidable. No C4 result depends on the distinction; its
theorems are statements about the abstract families and are untouched.

## Frozen final-report items

The preregistration requires twelve things stated separately.

1. **Finite-visible scope.** `V` finite; arbitrary visible carriers not classified. See Scope 1.
2. **T1 necessity.** Proved, kernel, all three visible conditions.
3. **T2 sufficiency.** Proved, kernel, candidate class `P_per`, quantifier order
   `forall Gamma, exists realization` preserved.
4. **T3 adversarial stress.** No counterexample found, and superseded by the general theorem. The
   failed search is not offered as support for sufficiency.
5. **Final candidate and closure.** `C* = PPer`; `C_OI(V) <-> C*` proved.
6. **Full-universe structural results.** The explicit carrier cardinality above, and the carrier
   lower bound showing no bound in `|V|` alone. Membership requires no hidden search at all, so the
   decision criterion is intrinsic rather than hidden-existential.
7. **Headline outcome.** B1.
8. **Prior/support scope.** Zero-mass hidden states are used, and are necessary. See Scope 2.
9. **Standing-control reconciliation.** `pdFamily` and `peFamily` are horizon realizations, not
   complete-family ones; corrected in `verification/README.md` in place and recorded in the C4
   amendment.
10. **Evidence types and debt.** B1: kernel theorem, both directions, no debt. Both supporting
    results: prose theorems, neither kernelized, each stating that boundary where it is stated. The
    exact rational probe supplies a witness and bounded controls for the separation and instances at
    `M = 1..20` for the lower bound; it is not offered as proof of either universal statement.
    Kernelizing them is open formalization work, and no result of this round rests on it.
11. **Closure.** Finite-visible Arc B is mathematically closed **and** kernel-closed.
12. **Arc C.** Arc C can begin at a precise finite-visible `C_OI` interface: the class is now a
    named visible predicate with a two-way kernel bridge to the reversible realization. No Arc C
    work was executed here.

Frozen controls 1–6 and 10–12 are discharged inside the theorems and the T3 probe: one common prior
and one reversible step throughout, `Gamma_0 = I` and row stochasticity checked at every time rather
than at period endpoints, all roots realized by the same hidden model, negative visible controls
rejecting stochasticity, root-identity and periodicity violations, and no bounded exhaustion used as
a general decision procedure. Control 14 holds: nothing here is promoted to quantum representation,
operational QM, physical accessibility, or Bell structure.

## Corrections and verification-instrument findings

These are audit findings about the round's execution and its instruments. They are recorded here
because someone auditing the round later needs to know what went wrong, whether it threatened the
mathematical conclusion, and what durable mechanism prevents recurrence. They are **not**
qualifications on B1. The full chronology stays in the commits and the audit comments.

### (a) Carrier-bound denominator defect — a mathematical correction to a supporting result

The first form of the carrier lower bound used a fixed denominator, `1/2 + sqrt(q_k)/100`. That
entry leaves `[0,1]` at `q = 2503`, and only 367 primes sit below that, so a fixed denominator
reaches `M <= 368` and no further; the corollary as stated did not hold for arbitrary `M`. The
repair makes the denominator family-dependent: `D = 4*max(q_k)` keeps every entry in `[0,1]` because
`4q <= D^2`, and dividing by a nonzero rational leaves `{1, sqrt q_1, ..., sqrt q_(M-1)}` linearly
independent over the rationals, so the span dimension is untouched.

Row-sum checking could not have caught this — `p + (1-p) = 1` holds coordinatewise whatever `p` is —
so the probe now range-checks the entries as integer arithmetic and carries a negative control at
2503. **B1, T1 and T2 were unaffected**: the defect was confined to the existential lower bound,
which is a supporting result and is not used anywhere in the classification.

### (b) Ten named results with no printed axioms — a verification-coverage defect

The chain declared 40 named results and printed the axioms of 30. The ten unprinted results were
inside modules whose other results were printed, so nothing about the modules looked wrong; the gap
surfaced only when the declaration counts were computed for the census pins. Three of the ten were
attribute-prefixed declarations (`@[simp] theorem ...`), which a naive scan for a line beginning
`theorem` also misses — the same blind spot in a second instrument.

Print blocks were regenerated from the declaration lists, giving 40/40. The durable mechanism is
R7-RCL, which compares the **set** of declared theorem names against the **set** of print targets,
per module, and fails on any difference in either direction. Coverage is now enforced rather than
maintained by hand.

### (c) A guard that tripped on its own disclaimer — a guard false positive

R7-RCL forbids the verification README from claiming the arbitrary-visible case is classified, by
scanning for a set of substrings. The README's required disclaimer, "nothing here classifies the
arbitrary-visible case", contains one of them, so the guard fired on the very sentence that makes the
scope honest — a check that penalizes the correct text is worse than no check, because the cheapest
way to satisfy it is to delete the disclaimer.

The repair requires the disclaimer to be present **and** excises exactly that occurrence from the
forbidden-substring scan, so the negated form is mandatory while every un-negated claim still fails
the guard.

### (d) A mutation that tested nothing — a guard false negative, and the most important of the four

R7-RCL is negative-tested by five mutations, each of which must break the guard. Mutation 4 deleted
a print line for `FiniteRootedRealizable`, which is a `def` and therefore has no print target: the
mutated text was identical to the original, the guard's verdict was unchanged, and the mutation
recorded a pass while exercising nothing.

This is the finding that matters most, because it is the failure mode that hides the others. A
false positive is loud and gets fixed within the hour; a vacuous negative test reports green forever
and makes an unguarded property look guarded. The repair deletes a real theorem print target and
additionally asserts that the mutated source differs from the original, so a mutation that fails to
mutate is itself a failure. Every mutation in the guard now carries that assertion.

## Preserved boundaries

This round does not:

- classify rooted families over infinite visible carriers;
- claim a full-support characterization;
- claim any bound on `|H|` as a function of `|V|` alone;
- retract, revise, or restate any theorem of the C4 causal-readback audit;
- require the `CausalReadback` parent, P-divisibility, tightness, or `N_CR` as membership
  conditions;
- alter the inherited interface, the canonical visible projection, or microscopic reversibility;
- apply the Barandes correspondence or characterize a quantum representation class;
- source phases, coherent control, Hamiltonians, instruments, measurements, or composites;
- edit manuscripts, books, bibliography, or publication claims.

Status: **B1 earned and kernel-closed for finite visible carriers. `C_OI(V)` is exactly the rooted
families that are the identity at the root time, row-stochastic at every time, and periodic, proved
in both directions as one named theorem and reached by the ordinary `lake build`. Arc C may begin at
that interface.**
