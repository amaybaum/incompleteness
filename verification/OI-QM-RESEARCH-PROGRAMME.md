# OI → QM research programme map

Status base: `main` at `a3695ce27b25a468a9593e796fade1a1e938895c` (post-PR #550, Arc C closed).

The formalization-first manuscript synchronization gate and the theorem-to-prose spine are carried by `verification/OI-QM-RESEARCH-PROGRAMME-AMENDMENT-1.md`, referenced from §7 rule 11 and §9.

This file is the canonical **strategic map** for the larger OI → QM research programme. It is not a theorem, an audit, a preregistration, or a replacement for the detailed verification ledger. Its purpose is to state, in one place:

- the ultimate research objective;
- what has already been established;
- what is still open;
- the order in which the remaining questions should be attacked;
- what different success and failure outcomes would mean for the final scientific claim.

Detailed theorem status remains controlled by the Lean sources, audit files, verification ledger, and manuscript scope guards. Where this map and a theorem/audit disagree, the theorem/audit controls.

---

## 1. Ultimate objective

The strongest possible endpoint is a theorem of the form

`OI + C  <->  operational quantum mechanics`,

where `C` is an explicit set of physical conditions that are either derived from the OI substratum or clearly identified as additional principles.

If that cannot be proved, the programme should instead terminate in a classification theorem of the form

`OI  ->  precisely characterized family of possible operational theories`,

with quantum mechanics identified as one subclass and every additional principle needed to select it stated explicitly.

The programme therefore has two acceptable scientific endpoints:

1. **Equivalence:** OI, with a justified and explicit condition set, is operationally equivalent to QM.
2. **Classification:** OI does not uniquely force QM, but the exact OI-compatible theory space and the extra principles selecting QM are known.

A negative result at an intermediate bridge is not a failure of the programme if it sharpens this classification.

---

## 2. Three notions that must not be conflated

The programme distinguishes three increasingly strong claims.

### A. Quantum representation

The observer-accessible stochastic data can be represented in Hilbert-space / Born-rule form.

This is a mathematical representation statement. By itself it does **not** imply that the underlying physics supplies arbitrary coherent phases, Hamiltonians, unitary controls, instruments, or composite-system operations.

### B. Quantum operational repertoire

The physically available preparations, reversible controls, measurements, instruments, composites, and transformations are exactly those of quantum mechanics, at the stated finite or quasilocal level.

This is stronger than merely admitting a Hilbert-space representation.

### C. Full physical equivalence to QM

The OI physical theory, including composition, locality, dynamics, measurement, state preparation, correlations, and the relevant infinite-system/continuum qualifications, is equivalent to the target version of quantum mechanics.

The research programme is complete only when the scope of the final claim is explicit about which of A, B, or C has actually been established.

---

## 3. What is already established

### 3.1 Finite operational completion is classified

The Mathlib verification programme gives a finite operational-QM completion classification. Bare finite OI does not uniquely select quantum mechanics. Exact finite operational QM is obtained when the required well-formedness and substantive operational principles are added; the substantive principles have been separated by explicit countermodels.

The strongest carrier-general forms reduce the operational package to implementation locality, a sufficient reversible/control richness condition, and embedded observation. The development further reduces the control side to an elementary continuously driven transition plus exchanges, with no quarter-phase primitive required.

**Interpretation:** the abstract operational conditions selecting finite QM are understood. The open question is whether the concrete OI physics itself supplies those conditions.

### 3.2 Concrete substratum sourcing reaches a sharp control boundary

The substratum-source audits show that the current concrete OI substratum supplies the structural closure properties needed by the finite operational theory, but its directly sourced observable operators are monomial/permutation-like. Bijective dynamics and the existing read-write couplings do not by themselves source a continuously tunable off-diagonal generator.

Thus the current substratum plus continuous off-diagonal controllability yields finite operational QM, but that controllability resource is not presently derived from the current OI axioms.

**Interpretation:** this is a sourcing boundary, not a representation theorem and not a proof that OI forbids the missing control resource.

Historical statements that the “OI → QM derivation programme is closed” refer to this completed Level-I substratum/control sourcing branch. They do **not** mean that the larger equivalence/classification programme described in this file is finished.

### 3.3 Typed and quasilocal extensions are substantially understood

The typed-completion audit shows that, within the natural carrier-general operational interface, the endomorphic restriction is a typing artifact: the finite typed theory is determined by its quantum endomorphic shadow.

The quasilocal-completion work constructs and characterizes the fixed-lattice infinite-region C*-system generated by the finite stages, with states and OI-induced discrete dynamics. It also records the remaining qualifications: no preferred Hilbert representation is selected, continuous time is not uniquely determined by the discrete dynamics, and general infinite-support operational availability is not forced by the frozen structure.

**Interpretation:** the finite-to-quasilocal mathematical completion is much clearer than the physical sourcing of the full operational repertoire.

### 3.4 A rooted stochastic observer family is sourced at the realization level

The observer-realization layer supplies a legitimate rooted stochastic family

`Gamma_t(a,j) = P(X_t = j | X_0 = a)`

once the finite reversible realization and fixed hidden prior are specified.

A unique global invariant ensemble is not required for this rooted conditional family. The fixed hidden prior remains part of the realization datum, and different allowed priors can change the visible rooted family.

### 3.5 The Barandes route is a separate stochastic → quantum correspondence route

Representability alone sources no OI control. That is now a theorem rather than a discipline: Arc D's S1 padding theorem (§3.12) shows that padding by an arbitrary finite ancilla unitary preserves the represented rooted family exactly, so the operator properties it proves free — non-monomiality, and relative-phase content that moves the all-ones vector off its ray — are exhibited in some representation of every representable family. Representational presence of such a property therefore cannot ground a sourcing claim.

The full Barandes correspondence is a different object from bare representability. It carries its own stochastic hypotheses and develops measurement, interference, decoherence and entanglement downstream of the correspondence, so it may establish quantum-theory equivalence that representability alone cannot. **Those hypotheses must be matched to OI theorem by theorem**, and until they are, nothing about what the correspondence supplies is settled either way.

The Barandes audit supports the use of rooted/conditional stochastic data for the mathematical stochastic-to-quantum representation route. It does not supply physical coherent controls, and it does not identify OI P-indivisibility with every notion of stochastic indivisibility used in the external literature. That identification is settled at definition level by `BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, and it is settled in the negative: see §3.13.

The programme therefore keeps two routes separate:

`rooted stochastic family -> quantum mathematical representation`

and

`OI physical realization -> physically available quantum operations`,

and runs the correspondence route and the internal reconstruction route as two independent tracks (§4), with neither usable as evidence for the other.

### 3.6 Causal hidden readback does not force accessible-window P-indivisibility

PR #542 establishes a realization-level `CausalReadback` notion with physical write/store/read meaning, but shows that the local consequences are weaker than initially hoped.

In particular, on an arbitrary same accessible window:

- `CausalReadback -> C4e` is false;
- `CausalReadback -> C4r` is false;
- `CausalReadback -> PIndivisibleWithin K` is false.

The exact countermodel `I -> B_(3/4) -> B_(5/8)` is parent-positive and P-divisible through the audited two-step window.

The history-sensitive `C4w` implication survives only with the correct visible-preparation support condition on the two witness roots.

This exposes two independent preparation dependencies:

1. the hidden prior can change the rooted stochastic family itself;
2. the visible initial law can change whether process-level history dependence is actually witnessed.

**Interpretation:** real hidden causal memory is not enough to guarantee short-time quantum-style information backflow.

### 3.7 Part of what is established is carried by no manuscript

The registry classifies sixteen kernel families as carried by no publication-facing statement. Among them is the operational pair-flow equivalence, whose own registry entry records the closure with one sourced pair flow as exactly quantum mechanics — a statement stronger than anything the corpus presently asserts.

This is a scope gap in the direction opposite to overclaiming. The reporting rules in §7 all guard against asserting more than has been proved; a result proved in the kernel and narrated nowhere is the same defect reflected, and it is not visible from the manuscripts alone.

**Interpretation:** the publication-facing corpus is not an inventory of what the programme has established. Closing this debt is a matter of stating results at the scope they were proved, which is separate from, and must not be used to soften, the corrections owed where publication wording is too strong.

### 3.8 The return-horizon obstruction is proved, and the horizon is tight

PR #543 settles the recurrence-scale question at both ends.

The obstruction holds:

`identity return + strictly earlier rooted-row overlap -> C4r -> P-indivisibility`

at that horizon, kernel-checked in `OIBridge/RecurrenceHorizon.lean` and composed with the merged revival no-go. Its load-bearing ingredient is only the storage-overlap consequence — a visible value carrying positive probability under both rooted preparations. The write clause and both read legs of the causal-readback parent play no part, so the obstruction applies to realizations that store without any causal write at all, under hypotheses strictly weaker than the parent.

The horizon is also tight. One exact finite reversible parent-positive realization has rooted family

`I -> B_(7/10) -> B_(3/5) -> I`

with controlling horizon `N_CR = 3`: it is P-divisible on every shorter horizon and first fails when the identity return is included.

**Interpretation:** no universal theorem from the frozen parent can replace the controlling return horizon by an unspecified strictly earlier one. The witness has `N_CR = 3`, so #543 alone does not show that the horizon is large.

### 3.9 The scaling law of the return horizon is known

PR #546 settles what #543 left open about scale, as outcome **O-4 mixed** under its frozen taxonomy.

Tight horizons are unbounded: for every `N >= 4` there is a parent-positive finite reversible realization tight at `N_CR = N`, so no absolute constant bounds the horizon of tight realizations. The family-level tightness is kernel-checked in `OIBridge/ScalingFamily.lean`, quantified over the horizon rather than verified at particular horizons; the realization half is a uniform prose argument with exact instance controls.

Independently, every parent-positive finite reversible realization satisfies

`N_CR <= 2 ord(phi)`,   hence   `N_CR <= 2 (|V||H|)!`,

by normalizing a parent witness modulo the microscopic period. This bound is carrier-dependent, and so does not refute the unbounded construction: the construction's carriers, and hence its microscopic period, grow with the horizon.

The sharp joint statement is about the **worst case**: the dependence of the controlling horizon on the microscopic period is `Theta(ord(phi))` — universally `O(ord(phi))`, and attained up to a constant by a family with `N_CR = ord(phi)/2`. It is not a pointwise comparison: nothing bounds `N_CR` from below, and a realization may have a large microscopic period and a small controlling horizon.

**Interpretation:** the scaling law is now known, and it is a mathematical law about microscopic periods. It carries no accessibility conclusion in either direction. A bound stated in microscopic periods is not a bound in physical time without an independently sourced relation between one microscopic step, or `ord(phi)`, and experimentally accessible time — and no such relation is supplied here. What #546 establishes is that no fixed accessibility guarantee follows from recurrence alone; it says nothing about which recurrence periods nature realizes.

### 3.10 The OI-realizable rooted stochastic class is characterized intrinsically

Arc B is closed. For finite visible carriers,

`C_OI(V) = PPer(V)`,

where `PPer` asks for identity at the root time, row stochasticity at every time, and periodicity of the family. The characterization is intrinsic: it refers to no hidden permutation construction, and it is kernel-closed.

**Interpretation:** the visible stochastic boundary of finite reversible OI is now known in both directions, at the inherited realization interface and at finite visible carriers. The finite-visible restriction is part of the theorem and is not to be dropped in restatement.

### 3.11 The all-time quantum-representation boundary is settled in both directions

Arc C is closed, with headline outcome **RC1 — proper overlap** between `C_OI` and the all-time fixed-basis Born representation class `Q*`. Carrierwise:

- at the empty carrier, `Q*(V) = ∅ ⊊ C_OI(V)`;
- at every nonempty finite carrier, `C_OI(V) ⊆ Q*(V)`;
- at `V = Fin 2`, the inclusion is strict: `C_OI(V) ⊊ Q*(V)`;
- strictness at every nonempty finite carrier is **not** claimed.

The two failures of global inclusion occur at different carriers, which is why neither one-sided reading is available.

**Interpretation:** this is a representation result and nothing more. It does not source coherent control, phases, Hamiltonians, preparations, measurements, instruments, ancillas, composites, or any other physical operational repertoire. §3.5's separation of the two routes stands, and the #540 boundary remains binding: mathematical representability is not physical availability.

### 3.12 The representation quarantine is a theorem, and the boundary is reconciled

Arc D round 1 is closed, with headline outcome **RD1 — quarantine proved and the boundary reconciled**.

The quarantine is S1, the padding theorem, quantified over an **arbitrary** finite ancilla: for every finite ancilla, every unitary on it and every probability weight, the padded datum represents exactly the family the original datum represents, at every root, outcome and time. So non-monomiality is free, relative-phase content is free, and at every nonempty finite carrier every unitary occurs — up to the relabelling implementation classes are already invariant under — as the unitary of a representation of an OI-realizable family.

The consequence is the point: **"represented" is a disqualified ground for any sourcing claim, at any rank.** The properties proved free — non-monomiality, and relative-phase content moving the all-ones vector off its ray — are exhibited in some representation of every representable family, and by consequence 3 so is every unitary on every nonempty finite carrier. A representation-level operator property that every representable family already exhibits distinguishes nothing, and neither does a resource predicate witnessed by an admissible finite-unitary conjugation once the criterion is augmented by representation content. What §3.5 previously held as a discipline is now a theorem of the corpus, at that scope.

Three further results accompany it. The Arc C inclusion witness is control-inert — its unitary is a permutation matrix and therefore lies inside the stated access. The representation-augmented access is trivial: it contains every unitary at every finite carrier, so it returns *Sourced* for every resource expressible in an admissible finite-unitary conjugation — exactly what `InstAvail`'s `op` constructor admits — and therefore has no discriminating power, which is what makes the disposition criterion non-vacuous. And the inherited relative-phase *Additional* verdict of PR #521 and PR #515 is stable against the whole Arc C layer, because availability is a function of the admissible class alone.

**Interpretation:** this closes the round, not Arc D. No resource receives a new disposition, no *Reducible* verdict is recorded, and the deferred resources — coherent off-diagonal control, continuous unitary or Hamiltonian evolution, preparations, measurements, instruments, ancillas, composition, and everything in Arc E — remain undecided by name. The decisive Arc D question of whether a deeper OI condition sources the continuously tunable off-diagonal generator is untouched, and #540 remains binding.

### 3.13 Barandes's indivisibility is a class name, not our failure predicate

Track B act 1 is closed. `BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md` records the verdict pair **(BD3, BR3)**, determined from primary-source text at pinpoint locations in arXiv:2302.10778v3, arXiv:2507.21192v1 and arXiv:2309.03085v2 alone.

**BD3 — definitional mismatch.** Barandes's *indivisible stochastic process* is the six-component tuple `(C, T, T₀, Γ, p, A)` of arXiv:2309.03085v2 §3.1 eq (24). Membership is a conjunction of normalization and trivialization conditions on the data; it is not a failure predicate. The same paper places any Markov chain inside the class by name (§3.3 eq (54)) and works a fully divisible permutation example that "trivially satisfies" the theorem (§4.3). Our `PIndivisibleWithin` is the negation of an existence claim. The two are predicates of different kinds, and no stated transposition identifies them.

**BR3 — required only downstream.** The theorem quantifies over the whole class (§4.1 eq (69)), and **failure of divisibility is not among the hypotheses its proof uses**. That is a negative claim about divisibility specifically and is not a claim that the proof consumes only two inputs: it opens from non-negativity (45) at eq (72), which the text calls an identity rather than a postulate, but it also invokes trivialization (46) at eq (75) and draws on the tuple's `p` and `A` in the later construction. Failure of divisibility does load-bearing work in exactly one place in the accepted corpus: arXiv:2302.10778v3 §3.5 eq (43), where interference is derived as the discrepancy between the actual dynamics and its would-be division.

**Recorded separately, and not folded into BD.** After transposing his column-stochastic left action to our row-stochastic right action, the factorization equation of arXiv:2302.10778v3 eq (6) is the body of `PDivisible` **exactly**, with exactly two differences against that equation: horizon, and the endpoint of the intermediate range. Direction is not one of them — eq (6) restricts to `t > t′ > t₀`, the same forward orientation as our `s < t`; arXiv:2507.21192v1 p. 10 separately broadens the target-time convention at framework level, which widens where his `Γ` is defined rather than differing from the equation. An exact equation match standing beside a definitional mismatch is what Amendment 3 to the preregistration exists to keep legible.

**Interpretation.** The programme's use of the correspondence is unaffected on the representation side: `Main.md` §3.1 already states that class membership is tuple instantiation and not a divisibility property, and this round confirms that reading against the source. What changes is the target of any future equivalence attempt: `PIndivisible_OI ↔ Indivisible_Barandes` is not the right statement to aim at, because the right-hand side is a class name. The live question is what `PIndivisibleWithin` adds *on top of* class membership, and eq (43) says what it adds in his framework. One manuscript surface is destabilized and is recorded as backlog without edit.

### 3.14 The transposition between orientations is a theorem, not a prose step

Track B act 2 is closed at **RT1 — kernel-closed**. `verification/BARANDES-TRANSPOSE-BRIDGE-RESULT.md` records it; `OIBridge/TransposeBridge.lean` carries it in seven named results, each printing only `propext`, `Classical.choice`, `Quot.sound`.

The round was a **check on act 1**, not bookkeeping. Act 1 answered its Q4 with a prose transposition, which sits at level 3 of act 1's own frozen evidence hierarchy — the hierarchy that rates a Lean equivalence above it at level 2 and named this step as where the upgrade belonged. Had any direction been refused, the outcome would have been `RT3` and act 1's Q4 would have taken an appended correction. It was not: the kernel **confirms** the transposition, and act 1's Q4 stands at level 2 on its this-side half. The other-side half — what the accepted text's equation says — is untouched and stays at level 1, since nothing here bears on the reading of a source.

**What is proved.** A matrix is row-stochastic exactly when its transpose is column-stochastic, in both directions; the single-pair factorization `A = B * Λ` with `Λ` row-stochastic is equivalent to `Aᵀ = Λᵀ * Bᵀ` with `Λᵀ` column-stochastic; and, lifting that from one instance to the predicate, `PDivisible K Γ ↔ PDivisibleCol K (fun t => (Γ t)ᵀ)` with the corresponding equivalence for `PIndivisibleWithin`. The orientation hazard the act 1 freeze named — row-stochastic-on-the-right versus column-stochastic-on-the-left — is discharged rather than assumed.

**What is not.** `PDivisible` bounds its time pairs by a horizon `K` and the external equation does not. That difference stands, and is reported as a difference of quantifier domain rather than a defect. What act 2 *does* settle is the other difference act 1 recorded: `PDivisible`'s extra `s = 0` case costs nothing, and `rootedMap_zero` discharges the trivialization hypothesis that lemma needs for every family this programme produces.

**Interpretation.** `PDivisibleCol` is this programme's own `PDivisible` written in the opposite orientation. Nothing here identifies `PIndivisibleWithin` with any external predicate, `BD3` and `BR3` are neither reopened nor re-derived, and a transposition identity sources nothing.

---

## 4. Current frontier

Arc A is closed in its mathematical part (§3.8, §3.9). The recurrence-scale obstruction is proved, its horizon is tight, and its scaling law is known:

`N_CR` unbounded in general,   and   `N_CR <= 2 ord(phi)` universally,

so worst-case `Theta(ord(phi))`. What that does **not** settle is reachability: the law is stated in microscopic periods, and no independently sourced map from microscopic steps to experimentally accessible time exists. Arc A's recurrence-scaling question is closed; physical accessibility is not solved, and it is a sourcing question for Arcs D and E rather than a further stochastic-boundary question.

Arcs B and C are also closed (§3.10, §3.11). The class `C_OI` is characterized intrinsically as `PPer` at finite visible carriers, and its relation to the all-time fixed-basis Born class `Q*` is RC1 proper overlap.

Arc D round 1 is closed at outcome RD1 (§3.12). It proved the quarantine: representational presence is a disqualified ground for any sourcing claim, as a theorem rather than a discipline.

**The programme is therefore two-track from here** (Amendment 2). The two tracks share their origin and their endpoint and are otherwise independent:

```
                    ┌──> Track B: Barandes correspondence route ──┐
OI ──> sourced ─────┤                                             ├──> operational QM
       stochastic   └──> Track I: Arc B/C/D/E internal            ┘
       law               reconstruction route
```

**Neither track may be used as evidence for the other.** Agreement strengthens the result; disagreement identifies the missing hypothesis, and identifying it is itself a result.

**Track B** runs `OI → observer/hidden realization → rooted transition family → the applicable causal/readback condition → P-indivisibility where applicable → the exact relation to Barandes's indivisibility definition → verification of every hypothesis of his correspondence → determination of exactly what quantum structure his theorem supplies`. It is added because it may reach the intended `OI → QM` claim sooner, and because the cost of not checking is asymmetric.

**Track I** continues as before. Its value is independent: it is what tells the programme which assumptions are actually doing the work, and Arc D round 1 is the standing demonstration, since a theorem about the programme's own criterion is not something an external correspondence theorem could supply.

Track B act 1, the **narrow definition-level audit** preregistered as `BARANDES-INDIVISIBILITY-BRIDGE-AUDIT.md`, is executed and closed at **(BD3, BR3)** (§3.13). The programme declined to attempt `PIndivisible_OI ↔ Indivisible_Barandes` before establishing what the right-hand side means in the accepted text, and the audit's answer is that the right-hand side is a class name rather than a failure predicate, so that equivalence is not the statement to aim at.

Track B act 2, the **Lean transpose bridge** and step 5 of Amendment 2's sequence, is executed and closed at **RT1 — kernel-closed** (§3.14). It confirms act 1's Q4 transposition rather than contradicting it, so no correction is appended to act 1, and Q4's this-side half rises from prose to kernel evidence under act 1's own hierarchy.

**Further Arc D rounds remain paused** pending the decision below. Everything merged by PR #554 stands; the pause is on new rounds, not a retraction.

Two Track B continuations are now available and neither is executed: a `BarandesTuple` instantiation lemma making "our processes instantiate the tuple" checkable rather than argued, for which act 2's `rootedMap_zero` supplies the trivialization condition; and the question `BD3` leaves open — what `PIndivisibleWithin` adds *on top of* class membership, which act 1 located in the external framework's interference term. Whether one of those, or Arc D round 2, or Arc E is on the critical path is the decision the programme now faces.

Arc E — composites, locality, entanglement and Bell structure — remains the required continuation of Track I wherever the final claim uses subsystem composition, local operations, incompatible measurements, or quantum correlation structure.

No recurrence-scale result should be described as accessible quantum-like nonclassicality without an independent accessibility bound, and no representation result should be described as physical availability.

---

## 5. Next major research arcs

The remaining programme should proceed in the following order unless a later audit supplies a reason to reorder it.

### Arc A — finish the stochastic/nonclassicality boundary — **closed (mathematical part)**

1. Complete the recurrence-scale theorem at the exact controlling visible-return horizon. **Done — PR #543 (§3.8).**
2. Determine horizon tightness. **Done — PR #543, T3-A with the `N_CR = 3` witness (§3.8).**
3. Record the hypotheses actually used, and do not assert that they are the weakest available unless that has itself been proved; in particular distinguish storage overlap from the full write/store/read parent when the stronger clauses are not load-bearing.
4. Correct publication wording where preparation or horizon scope is demonstrably too strong.
5. **#63 — recurrence-horizon scaling / accessibility. Done — PR #546 (§3.9).** Tight horizons are unbounded, and every parent-positive finite reversible realization satisfies `N_CR <= 2 ord(phi)`; jointly, worst-case `Theta(ord(phi))`. Outcome O-4 mixed: an unbounded tight construction together with a non-refuting carrier-dependent bound. No accessibility bound was obtained, and none follows: the result is stated in microscopic periods, not in physical time.

**Exit condition — met, in its mathematical part.** We now know what nonclassical stochastic behavior finite reversible OI forces, at what horizon, under which preparation assumptions, and how that horizon scales: worst-case `Theta(ord(phi))`, unbounded in general.

The reachability half is **not** met, and is not closed by the scaling law. #546 shows that no fixed accessibility guarantee follows from recurrence alone; it does not establish what recurrence periods physical realizations have. Closing that would need an independently sourced map from microscopic steps, or `ord(phi)`, to experimentally accessible time — which is a sourcing question for Arc D and Arc E, not a further stochastic-boundary question. Arc A's recurrence-scaling question is closed; physical accessibility is not solved.

### Arc B — characterize the full class of OI-realizable rooted stochastic families — **closed**

**Done — PR #547 (§3.10).** `C_OI(V) = PPer(V)` for finite visible carriers, kernel-closed. The ideal endpoint below was reached: the characterization refers to no hidden permutation construction.

**Exit condition — met**, at finite visible carriers. The restriction to finite visible `V` is part of the theorem.

Move beyond examples and individual memory criteria. Seek an intrinsic characterization of the complete family of rooted stochastic processes realizable by finite reversible OI with the allowed observation and preparation structure.

Ideal endpoint:

`finite OI realizations  <->  C_OI`,

where `C_OI` is described without reference to a hidden permutation construction.

Questions include:

- which row-stochastic families admit one finite reversible dilation with one fixed hidden prior?
- what consistency, recurrence, memory, preparation, and support constraints characterize them?
- which visible stochastic families are impossible under OI?

**Why this matters:** if full QM equivalence fails, `C_OI` is the natural precise answer to “what other theories does OI allow?”

### Arc C — close the quantum-representation boundary in both directions — **closed**

**Done — PR #550 (§3.11).** Headline RC1, proper overlap, with the carrierwise refinement recorded in §3.11.

Formalize the exact interface between the sourced rooted family and the stochastic-to-Hilbert/Born representation theorem.

Keep the result explicitly representation-level.

Then audit the converse direction:

- which finite quantum stochastic/measurement structures correspond to OI-realizable rooted families?
- is every relevant finite quantum representation realizable by an OI hidden reversible realization, or only a subclass?

**Exit condition — met.** The precise mathematical relation between `C_OI` and the quantum representation class is known in both directions.

### Arc D — attack physical sourcing of the quantum operational repertoire — **round 1 closed (RD1); further rounds paused pending the Barandes bridge audit**

This is likely the decisive equivalence stage.

Determine whether the physical OI architecture itself can source, rather than merely represent or assume:

- continuous coherent state mixing;
- relative phases;
- unitary control;
- Hamiltonian or continuous-time evolution where claimed;
- measurements and update rules;
- Kraus instruments;
- preparation operations;
- ancilla use and discard;
- the required closure rules across carriers.

Existing conditional results should be used as assembly theorems: once a resource is physically sourced, determine exactly what operational repertoire follows from it.

The crucial question is whether the currently missing continuous off-diagonal control resource can be derived from a deeper OI condition, or whether it is genuinely an independent empirical principle.

#### Physical lift seam: from sourced single-system control to sourced instruments and composites

Sourcing a coherent operator or control law on one visible carrier is not by itself enough to claim that OI physically supplies the full instrument or composite repertoire. After any single-system control resource is sourced, audit whether that **same physical source** survives and is compatible with:

- adjoining and discarding ancillas;
- locality / inert-spectator requirements;
- subsystem restriction and regrouping;
- composition of sourced operations;
- measurement/instrument dilation;
- the composite interfaces used by the finite operational-QM assembly theorems.

Abstract completion theorems may be used to assemble the consequences of a physically sourced resource, but they must not substitute for proving that the source itself lifts through these interfaces. In particular, do not infer “OI sources composite operational QM” merely from “OI sources one-carrier coherent control” plus an abstract availability theorem whose hypotheses have not themselves been physically sourced.

**Exit condition:** every operational-QM resource is either derived from OI, proved reducible to a smaller physical condition, or explicitly classified as additional, and any single-system source used in that derivation has been shown to lift through the instrument/composite interfaces actually required.

### Arc E — composites, locality, entanglement, and Bell structure

Single-system operational equivalence is not the end of the programme.

Audit how OI sources the composite-system structure required for genuine quantum correlations:

- tensor/composite structure;
- local operations;
- incompatible measurements;
- entanglement;
- allowed correlation sets;
- causal/locality constraints;
- Bell/CHSH behavior.

The existing Bell correction is controlling: a deterministic completion with pointwise graph-cone locality, local setting interventions, readout before the cones meet, and one setting-independent pre-setting ensemble is a local hidden-variable model and obeys CHSH <= 2.

Therefore quantum Bell correlations cannot be claimed from that local hidden completion without an additional structural ingredient or a change in one of those assumptions.

**Exit condition:** the relation between OI composite physics and the quantum correlation set is explicitly characterized, including any additional principle required to reach it.

### Arc F — final equivalence-or-classification theorem

Assemble the previous arcs into the strongest justified final statement.

**Which endpoint is live must be decidable in advance, not chosen at assembly time.** §1 records that a negative result at an intermediate bridge is not a programme failure if it sharpens the classification. That is correct, but on its own it lets every outcome be read as progress, which leaves the programme unfalsifiable at the strategic level. The endpoints are therefore governed by an explicit retirement condition, fixed here rather than after the fact:

> **F1 is retired** when any arc returns an *Independent* verdict in the sense of §6 on a resource that F1 requires — a countermodel showing the resource does not follow from the OI axioms then in force. The standing candidate is Arc D's continuous off-diagonal control: a countermodel there retires F1, and the programme commits to F2 or F3 with that resource named as an additional principle.
>
> An *Open* verdict retires nothing. A construction or formalization that fails without an impossibility theorem leaves F1 live, and recording it otherwise would be the error §6 already forbids.

Retiring F1 is a result, not a defeat: it converts the programme's endpoint from an equivalence claim to a classification with an explicitly identified selection principle, which §1 names as an acceptable terminus.

Possible endpoints are:

#### F1. Full conditional equivalence

`OI + explicitly justified physical conditions  <->  target QM`.

Every condition is named, its sourcing status is known, and the target version of QM is explicitly scoped: finite, typed, quasilocal, discrete-time/continuous-time, operational availability, and composite structure as applicable.

#### F2. Minimal extension theorem

OI does not alone force QM, but there is a small, independently meaningful set of additional physical principles that is necessary and sufficient for QM.

This remains a strong reconstruction result if the added principles are physically transparent and separately testable.

#### F3. Exact classification without uniqueness

OI admits a larger theory space. The programme characterizes that space, identifies the QM subclass, and proves which additional principles select it.

This is the correct endpoint if some quantum resources are independent of OI rather than derivable from it.

---

## 6. Decision tree for interpreting future results

For every future bridge, distinguish four outcomes.

### Derived

The desired quantum structure follows from previously accepted OI physics. This strengthens the equivalence direction.

### Conditional

The structure follows once a named additional physical condition is assumed. Record whether the condition has independent motivation and whether it is necessary, sufficient, or both.

### Independent

A countermodel shows that the structure does not follow from the current OI assumptions. This bounds the equivalence claim and identifies an additional selection principle.

### Open

The current construction or formalization fails, but there is no impossibility theorem. Do not report tooling or construction failure as mathematical independence.

These four statuses should remain separate in both audits and manuscript summaries.

---

## 7. Programme-level reporting rules

1. Do not report mathematical representability as physical availability.
2. Do not report recurrence-scale nonclassicality as accessible-time nonclassicality without an accessibility bound.
3. State preparation assumptions explicitly: hidden-prior choice and visible-root preparation are different dependencies.
4. Keep finite, typed, quasilocal, and continuous-time claims distinct.
5. Keep single-system and composite/Bell claims distinct.
6. When a resource is not derived, distinguish “not derived under current axioms” from “forbidden by OI.”
7. Prefer exact classification of the residual theory space over forcing a false equivalence claim.
8. Every final equivalence statement must identify which direction is proved and which hypotheses are load-bearing.
9. State the evidence type of every reported result: kernel-checked, exact-probe-checked, or prose. Rules 1–8 guard the scope of a claim; this one guards its standing. A prose proof is not a formalized success, and a formalization or tooling failure is not a mathematical negative — the second half of that is already §6's *Open*, and the first half is its counterpart. Where a round's positive and negative results carry different evidence types, say so in the same place they are reported, so the asymmetry is visible without reading the sources. A theorem proved from a cited external premise is a fourth type, and is neither a gap nor a fully kernel-checked result; §8 records the corpus's standing instance.
10. Do not treat the publication-facing corpus as the inventory of what is proved. Where the kernel carries a result at a scope no manuscript states, that is a recorded debt (§3.7), not an absence of the result — and closing it means stating the result at the scope proved, never at a stronger one.
11. **Formalization-first manuscript synchronization gate.** The central OI → QM claims and proof narrative are not to be strengthened, reorganized, or newly integrated into the publication-facing manuscripts while the load-bearing chain is still being formalized. Arc B and Arc C results remain verification-layer results until the Arc D and Arc E obligations the intended claim actually uses are kernel-closed or carry an explicit disposition under §6. Manuscript integration then proceeds in one synchronized pass, generated from the theorem-to-prose spine rather than from the current prose. Corrections to statements already known to be false, over-scoped, or misqualified are exempt and are never delayed; so are bibliographic, typographic and formatting fixes. The gate, its exception, the spine and the synchronization procedure are stated in full in `verification/OI-QM-RESEARCH-PROGRAMME-AMENDMENT-1.md`, which controls their detail.

---

## 8. Parallel research tracks outside this roadmap

This roadmap covers the **OI → QM equivalence/classification programme only**. Other major corpus programmes remain active or backlogged, but they are not prerequisites for the equivalence chain unless a later theorem explicitly connects them.

Parallel tracks include, in particular:

- gravity / G3 sourcing and the remaining locality/interacting-sector debts;
- curved-continuum or geometry reconstruction questions;
- IR Lorentz / universal-cone questions;
- full-response, memory-resummed, or related dynamical-response programmes;
- other model-specific physics programmes whose results may constrain OI but do not currently sit on the logical path from the OI observer structure to operational QM.

These tracks retain their own theorem, audit, and backlog status. Progress on them must not be counted as progress on the OI → QM equivalence chain unless an explicit bridge is proved; conversely, the equivalence programme should not silently absorb or supersede their unresolved questions.

### The standing formalization debt of the reconstruction track

One parallel-track debt is named here because it is the corpus's largest instance of what reporting rule 9 governs, and because it is invisible from the manuscript statement it qualifies.

The reconstruction programme's two-branch theorem is graded K2 rather than K3 on a single unformalized input: the integer Piccard/Bekir–Golomb classification, carried in the kernel as the `Prop` `BGIntegerClassification` in `OIBridge/TurnpikeScopeTransfer.lean` and consumed as a cited external premise. That module records it as the only unproved input of the reconstruction programme. Every other step is kernel-proved, including the integer-to-real passage and the assembly `twoBranch_of_BGClassification`, and three probes record formalizing the 2007 classification as the sole remaining K3 backlog item.

The status is therefore precise and should be reported as such: the theorem is proved *relative to* a stated external classification, not from the kernel alone. It is neither a gap in the mathematics nor a fully kernel-checked result, and it is exactly the case rule 9 exists to keep visible.

This debt sits on the reconstruction track, not on the OI → QM chain. Discharging it neither advances nor blocks the equivalence programme, and it must not be counted in either direction.

---

## 9. Relation to existing documentation

This file is intentionally high-level.

Use the following sources for detailed status:

- `verification/README.md` — technical verification status and theorem inventory;
- `verification/coverage/LEDGER.json` — statement-by-statement proof coverage;
- `verification/CENSUS-oi-compatible-theories.md` — finite OI-compatible completion classes;
- the individual `*-AUDIT.md`, `*-RESULT.md`, and amendment files — preregistered questions and exact outcomes;
- `verification/OI-QM-RESEARCH-PROGRAMME-AMENDMENT-1.md` — the formalization-first manuscript synchronization gate, its exception, the theorem-to-prose spine, and the synchronization procedure;
- `verification/OI-QM-RESEARCH-PROGRAMME-AMENDMENT-2.md` — the two-track programme, the pause on further Arc D rounds, and the rule that neither track is evidence for the other;
- `verification/lean-mathlib/OIBridge/` — kernel statements and their hypotheses;
- `papers/GR.md`, `papers/Main.md`, the Explainer, and book chapters — publication-facing statements under their scope guards.

`verification/ROADMAP.md` remains the historical roadmap for the original zero-import verification layer. It is not the strategic roadmap for the larger OI → QM equivalence/classification programme.

---

## 10. Current one-line programme state

At the post-#554 boundary, with Track B act 1 closed:

**Arcs B, C and Arc D round 1 are kernel-closed: finite reversible OI yields exactly `PPer` at the rooted stochastic level, its relation to the all-time fixed-basis Born representation class `Q*` is RC1 proper overlap, and representational presence is now a proved disqualified ground rather than a stated discipline — arbitrary finite-ancilla unitary padding preserves the represented family exactly, so the operator properties Arc D proves free are exhibited in some representation of every representable family, and every resource expressible in an admissible finite-unitary conjugation is vacuous under the representation-augmented criterion, so no sourcing claim may rest on either. The programme is two-track from here: the Barandes correspondence route and the internal Arc B/C/D/E reconstruction route, neither usable as evidence for the other. Track B act 1 is closed at (BD3, BR3): Barandes's *indivisible stochastic process* is a tuple class containing Markov chains, not our failure predicate, and failure of divisibility is no hypothesis of his theorem though it is what his interference derivation runs on; separately, his factorization equation is our `PDivisible` body exactly after transposition. Act 2, the Lean transpose bridge, is closed at RT1: the two orientations are the same predicate under transposition, proved rather than argued, confirming act 1's Q4 and leaving the horizon difference standing. Whether the next act is a tuple-instantiation lemma, the question BD3 leaves open, Arc D round 2 or Arc E is the decision now open. Publication-facing strengthening of the central OI → QM argument is deferred under §7 rule 11 until that formal chain is closed or precisely classified, after which the manuscripts are synchronized in one pass from an explicit theorem-to-prose spine.**
