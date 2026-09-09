# All-time quantum-representation boundary for `C_OI` — result

Determination for `verification/OI-QUANTUM-REPRESENTATION-AUDIT.md`, frozen at commit
`38a8f09d9d314fdd3d7747d0d0351f07c693c582`, authoritative blob
`8177527b11a0970c7fc71f1bff382112aaf93aa6`, merged at
`073ef65ae286e67e84ce4dfc0f634252cf29939f`; read under
`OI-QUANTUM-REPRESENTATION-AUDIT-AMENDMENT-1.md`, blob
`e809e04aee45181d162bd4a2cc2782751b65f509`, merged at
`64565efc4441e266f552db2b85438d6a994d0285`, which retires the adversarial/bias machinery and
nothing else. Executed on branch `oi-quantum-representation-execution` from that merged `main`.

## Headline outcome — RC1, proper overlap

Both inclusions are decided over the frozen finite-visible universe, and both are **refuted**:

- `Q* ⊄ C_OI`, witnessed at `V = Fin 2` (`qStar_not_subset_finiteRootedRealizable`);
- `C_OI ⊄ Q*`, witnessed at the empty carrier (`qStar_inclusion_iff_nonempty`).

Two failed inclusions do not by themselves separate proper overlap from disjointness, which is what
RC1 additionally requires. The intersection is settled and is large: on every **nonempty** finite
carrier the whole of `C_OI(V)` lies inside `Q*(V)` (`qStar_of_finiteRootedRealizable`). So the
relation is **proper overlap**, not disjointness, and the Arc C exit condition is met.

### The carrierwise refinement, which is sharper than the headline

The global relation is proper overlap, but the two failures do **not** occur at the same carrier,
and no single carrier exhibits both. Carrierwise the picture is exact, and the inclusion reverses
direction:

| carrier | relation |
|---|---|
| `V` empty | `Q*(V) = ∅ ⊊ C_OI(V)` |
| `V = Fin 2` | `C_OI(V) ⊊ Q*(V)` |
| `V` nonempty finite, general | `C_OI(V) ⊆ Q*(V)`; strictness **not** proved |

Reading the headline as "at some carrier both inclusions fail" would be wrong. What is true is that
each inclusion fails *somewhere*, and they fail at different places.

## T1 — the translation

`OIBridge/QuantumRepresentation.lean`, sixteen named results.

`QfbData` is the merged `QfbReal` datum with the horizon index dropped. That is not a weakening:
`QfbReal V K` takes `K` as a parameter and **no field of it mentions `K`**, so the horizon lives in
the trajectory length and never in the datum. All four data fields, `IsLaw`, and the one-step Born
weight are carried verbatim.

What is added is the rooted object, because `QfbReal` carries one global `init` and no root-indexed
field of any kind. The frozen map conditions the single process on the visible event
`read (B_0) = a`, with positive mass on every root fibre so that the conditioning is defined:

> `∃ Bas` finite, `∃ U` unitary, `∃ init` a probability weight, `∃ read`, such that `∀ a`,
> `∑_{read b = a} init b > 0`, and `∀ a t j`, `Γ t a j = P[read (B_t) = j | read (B_0) = a]`.

The existential block stands outside `∀ a t j`, and the three rejected preparation maps are excluded
structurally rather than by comment: one datum for every root, no prior field, and every
conditioning sum over the read fibre rather than a basis point.

**Finite-horizon compatibility** is the strong form. `condReal` reuses `Q.Bas`, `Q.U` and `Q.read`
definitionally — `condReal_Bas`, `condReal_U`, `condReal_read` are `rfl`, which a per-horizon witness
built from unrelated data could not satisfy — and only the initial law is re-conditioned.
`rootTraj` is defined from the **unconditioned** chain weight, deliberately not as the law of the
re-conditioned datum, so `condReal_law` is not true by construction. The weaker `∀K ∃Q_K` appears
only as the derived corollary `qfbRealizable_rootTraj`.

**The seam** between the class and that theorem is closed by `rootTraj_marginal`: the
final-coordinate visible marginal of the root-conditioned trajectory law is the class entry, proved
**without assuming the visible process is Markov**. Without it, `QStar` (stated through `bornPow`)
and the horizon theorem (stated through the chain weight) would be two parallel definitions.

## T2 — refuted

`OIBridge/QuantumRepresentationT2.lean`, seventeen named results.

The Hadamard datum with an **injective** readout is a valid `Q*` member whose induced rooted family
is exactly `pdFamily`, the merged N1 control. Nonperiodicity is the already-merged
`pdFamily_not_periodicFamily`, so the refutation rests on a merged theorem rather than an argument
invented for the occasion.

**Readout-injectivity split.** The witness is injective. One valid member outside `C_OI` refutes the
inclusion, so the non-injective classification — genuinely harder, and the reason the round stayed
open rather than being arithmetic — is untouched and not attempted.

**What is forced, and what is not.** A counterexample must use non-permutation Born dynamics, and
that much is forced: a permutation of a finite carrier has finite order, so by the Arc B
characterization a permutation datum is realizable and therefore periodic. Nothing beyond that is
forced. A two-state rotation is non-permutation over an interval of angles, rational choices such as
`3/5` and `4/5` included, and any of them would refute T2 equally well. Hadamard is chosen because
its Born matrix is exactly fully mixing, which makes the identification with `pdFamily` immediate;
the `1/√2` amplitudes are what fully mixing costs on two values, not a requirement of the target.

## T3 — proved, and carrierwise exact

`OIBridge/QuantumRepresentationT3.lean`, thirteen named results.

```lean
theorem qStar_inclusion_iff_nonempty :
    (∀ Γ : ℕ → Matrix V V ℝ, FiniteRootedRealizable (V := V) Γ → QStar Γ) ↔ Nonempty V
```

Both halves are kernel-proved, so the nonemptiness condition is a **theorem about the target**
rather than a hypothesis inserted to make the target come out true.

**The empty carrier is a genuine failure**, not an oversight. There `C_OI` is inhabited — take a
one-point hidden carrier and the identity update — while `Q*` is empty: `IsLaw` forces
`∑ b, init b = 1`, so the basis is nonempty, and no map runs from a nonempty basis into an empty
carrier. The obstruction is in the shape of the representation datum, not in the dynamics, so no
construction repairs it.

**The construction**, on a nonempty carrier, reads the Arc B realization as a quantum system. The
reversible `step : V × H ≃ V × H` is already an `Equiv.Perm (V × H)`, so unitarity is the merged
`permMatrix_mem_unitaryGroup` and no new unitarity argument is needed. The hidden prior, shared by
every root, is spread over the product with the visible coordinate uniform; that makes
`rootMass a = 1/|V|` on every root, and conditioning on the visible fibre removes the uniform factor
exactly, returning `rootedMap`.

**Refutation standard for the negative half.** The frozen standard for refuting `C_OI ⊆ Q*` demands
an obstruction proved against every finite basis, unitary and readout — not observed at small
dimension. It is met: `nonempty_of_qStar` derives a contradiction from the shape of any datum
whatever, with no bound on the basis.

## Frozen final-report items

1. **Finite-visible scope.** Inherited from Arc B with the theorem and not re-derived; arbitrary
   visible carriers are not classified.
2. **T1.** Clauses carried and dropped are stated above; the horizon-compatibility theorem is the
   strong form on `condReal`, with the per-horizon existential derived from it.
3. **T2.** Refuted, with the readout-injectivity split explicit.
4. **T3.** Proved for nonempty finite carriers and refuted for the empty one, as an iff; the
   refutation standard is met.
5. **The relation.** Proper overlap globally, with the carrierwise table above. The Arc C exit
   condition is met.
6. **Headline.** RC1.
7. **The intersection.** On every nonempty finite carrier it is all of `C_OI(V)`. Its criterion is
   **intrinsic**: by the Arc B characterization membership in `C_OI(V)` is `PPer`, a predicate on the
   visible family alone, so the intersection is described without any hidden-existential data.
8. **Horizon-indexed results.** `finite_horizon_equivalence` is cited nowhere in the proofs. The one
   place a horizon-indexed statement is used is T1's own compatibility theorem, and it is used in
   the strong direction — `∀ K`, the witnessing representation is `condReal`, built from the same
   all-time `Bas`, `U` and `read`. No all-time inclusion, equality or separation anywhere in this
   round is derived from a per-horizon result.
9. **Evidence and debt.** Every result above is a kernel theorem. Forty-six named results across the
   three modules, each printing `[propext, Classical.choice, Quot.sound]`, with the declared
   theorem-name set equal to the print-target set in every module. No prose theorem, no probe
   carries any claim, and there is no formalization debt.
10. **Closure.** Arc C is mathematically closed **and** kernel-closed for the finite-visible universe.
12. **Arc D.** It can begin at a precise representation boundary. It is not begun here, and #540
    remains binding: representability in this sense sources no physical repertoire.

Item 11 was retired by Amendment 1.

## Controls

Frozen controls 1–9 and 11–13 hold; control 10 was retired by Amendment 1.

Horizon quarantine holds as item 8 records. Interface fidelity holds on both sides: one common prior
and one reversible step on the OI side, and one time-independent unitary with fixed-basis collapse
at every step and the frozen root-preparation map on the quantum side. Positive root mass is carried
as a support condition and is reported wherever a result turns on it — it is exactly what fails at
the empty carrier. Bounded search is used nowhere; both witnesses are exhibited and proved. Nothing
is promoted to physical sourcing, coherent control, instruments or composites.

`R7-QSTAR` enforces the frozen map as a shape contract rather than trusting review: quantifier order
checked positionally with no inner existential, shared all-time data backed by the three `rfl`
lemmas, visible-fibre conditioning, the strong horizon theorem with the per-horizon form derived
from it, root-build reachability across all three modules, seam closure, and axiom-report
completeness as a set equality. Each is mutation-tested against the weakening it exists to catch,
and every mutation is asserted to change the source.

## Corrections and verification-instrument findings

Recorded as audit findings, not as qualifications on the results above.

### (a) An overstatement about what the T2 witness requires

The T2 module first claimed that non-permutation Born dynamics on two values forces an amplitude of
modulus `1/√2`. That is false: a two-state rotation with `cos θ = 3/5` has Born matrix
`[[9/25, 16/25], [16/25, 9/25]]` — rational, non-permutation, and with eigenvalue `−7/25`, so its
powers never return to the identity and it refutes T2 with no irrational anywhere. What is forced is
only non-permutation dynamics. The claim was corrected in the module, the census entry and row, and
the README paragraph; the proof was untouched, since the witness was never in question.

### (b) Three defects in the guard, found by writing it

`R7-QSTAR`'s declaration extractor ran past the definition into the prose between declarations —
prose that spells out `∀K ∃Q_K`, the very shape the check forbids — so the quantifier check was
reading a comment. A second check matched a lemma name by substring, which `condReal_readout`
satisfies while deleting `condReal_read`; its own mutation 5 exposed it. A third, mutation 4, was a
no-op carrying an argument dropped when `condReal_law` lost its positivity hypothesis, and was caught
by the assertion that every mutation must change the source — the assertion inherited from the Arc B
vacuous mutation, which has now paid for itself twice.

### (c) A count pin corrected before it could go stale

The first packaging of T2 pinned 3,119 named results, having missed the two lemmas lifted into the
T1 module. `lean_axiom_check` reported 3,121; the pins were corrected rather than left to drift.

### (d) An orientation that type-checks either way

Mathlib writes `permMatrix σ i j = if σ i = j then 1 else 0`, while the Born weight reads
`‖U b' b‖^2` — the transposed index order. Building the T3 datum from `step.permMatrix` therefore
runs the Born chain along `step⁻¹` and proves a theorem about a different family, with no type error
to warn of it. The datum uses `step.symm.permMatrix`, and the module says why. This is a hazard of
the interface rather than a defect that shipped, and it is recorded so the next round does not have
to rediscover it.

## Preserved boundaries

This round does not:

- claim strictness of `C_OI(V) ⊆ Q*(V)` at any carrier other than `Fin 2`;
- classify the non-injective readout case;
- extend anything to infinite visible carriers;
- derive any all-time statement from the merged per-horizon equivalence;
- claim physical sourcing of coherent control, phases, Hamiltonians, instruments, measurements as
  physical operations, or composites — Arc D and Arc E, with #540 binding;
- apply or extend the Barandes correspondence beyond the merged determination;
- edit manuscripts, books, bibliography, or publication claims.

Status: **RC1 recorded. Both inclusions decided, the intersection settled, and the relation is proper
overlap over the finite-visible universe, with the carrierwise refinement exact: the empty carrier
has `Q*` empty and `C_OI` inhabited, every nonempty finite carrier has `C_OI ⊆ Q*`, and the
containment is strict at `Fin 2`. Arc C is closed mathematically and in the kernel; Arc D may begin
at this boundary.**
