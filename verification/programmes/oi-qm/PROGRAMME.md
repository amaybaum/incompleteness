# OI → QM research programme map

Status base: `main` at `a3695ce27b25a468a9593e796fade1a1e938895c` (post-PR #550, Arc C closed).

The formalization-first manuscript synchronization gate and the theorem-to-prose spine are carried by `verification/programmes/oi-qm/amendments/amendment-1.md`, referenced from §7 rule 11 and §9.

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

Track B act 2 is closed at **RT1 — kernel-closed**. `verification/programmes/oi-qm/track-b/act-02-transpose-bridge/result.md` records it; `OIBridge/TransposeBridge.lean` carries it in eight named results, each printing only `propext`, `Classical.choice`, `Quot.sound`.

The round was a **check on act 1**, not bookkeeping. Act 1 answered its Q4 with a prose transposition, which sits at level 3 of act 1's own frozen evidence hierarchy — the hierarchy that rates a Lean equivalence above it at level 2 and named this step as where the upgrade belonged. Had any direction been refused, the outcome would have been `RT3` and act 1's Q4 would have taken an appended correction. It was not: the kernel **confirms** the transposition, and act 1's Q4 stands at level 2 on its this-side half. The other-side half — what the accepted text's equation says — is untouched and stays at level 1, since nothing here bears on the reading of a source.

**What is proved.** A matrix is row-stochastic exactly when its transpose is column-stochastic, in both directions; the single-pair factorization `A = B * Λ` with `Λ` row-stochastic is equivalent to `Aᵀ = Λᵀ * Bᵀ` with `Λᵀ` column-stochastic; and, lifting that from one instance to the predicate, `PDivisible K Γ ↔ PDivisibleCol K (fun t => (Γ t)ᵀ)` with the corresponding equivalence for `PIndivisibleWithin`. The orientation hazard the act 1 freeze named — row-stochastic-on-the-right versus column-stochastic-on-the-left — is discharged rather than assumed.

**What is not.** `PDivisible` bounds its time pairs by a horizon `K` and the external equation does not. That difference stands, and is reported as a difference of quantifier domain rather than a defect. What act 2 *does* settle is the other difference act 1 recorded: `PDivisible`'s extra `s = 0` case costs nothing.

**Two results beyond the frozen four, and why there are two.** T4 is proved on the exact frozen signature, which carries no `DecidableEq V` binder; the identity matrix notation gets its decidable equality from a scoped classical instance instead, because an added hypothesis would have been a target change. `rootedMap_zero` proves the trivialization fact `rootedMap R 0 = 1`. That alone does **not** discharge T4's hypothesis at a concrete family: T4's identity elaborates under the classical instance while `rootedMap` carries the ambient one, so the two identity matrices are propositionally but not syntactically equal and bare instantiation does not go through. `rootedMap_root_factor` proves the endpoint conclusion directly at the realization layer, so the concrete claim rests on a theorem rather than on an instance-compatibility argument. Both are declared as additions in the result note rather than folded into T4.

**Interpretation.** `PDivisibleCol` is this programme's own `PDivisible` written in the opposite orientation. Nothing here identifies `PIndivisibleWithin` with any external predicate, `BD3` and `BR3` are neither reopened nor re-derived, and a transposition identity sources nothing.

### 3.15 The representation does not determine the candidate intermediate

Track B act 3 is closed at **`CU1a` — the named rules are underdetermined**. `verification/programmes/oi-qm/track-b/act-03-candidate-selection/result.md` records it; `OIBridge/CandidateSelection.lean` carries it in seven named results, each printing only `propext`, `Classical.choice`, `Quot.sound`.

**Why this round and not an interference round.** Reaching "does OI force a nonzero interference discrepancy" needs the chain *OI stochastic family → representation → candidate intermediate → discrepancy*. Arc D round 1 settled that the **first** arrow does not determine operator content. A representation-invariance round on the interference discrepancy was drafted and **withdrawn before freeze**: padding is the only parameterized same-family freedom the corpus proves, it appears inert at the candidate level, and so that round's positive outcome could have failed for want of a construction rather than for want of truth. The scoping pass (`BARANDES-REPRESENTATION-FREEDOM-SCOPING.md`, PR #563) established that, non-adjudicatively, and this round asks the prior question instead — designed so every outcome is reachable and each decisive one earned by a named proof.

**What is proved.** Two natural extraction rules — weight the visible fibre by the normalized initial law, or weight it uniformly — are each admissible, admissible weights give row-stochastic candidates, and the two rules **differ on one lawful representation with the representation held fixed**. No appeal to representation freedom is made or needed, which is exactly what makes the target reachable. The general question closes with it: over *arbitrary* admissible weights the candidate is not unique either.

**Where the sign condition earns its place.** Writing `R_b(j)` for a basis point's visible row, the candidate entry is `∑_{b ∈ fibre k} μ k b · R_b(j)`. Support and normalization force the row **sums** on their own — which is what disguised the gap — while leaving each **entry** an affine rather than convex combination of the fibre's rows: weights `(2, −1)` give a normalized but negative row. Admissibility therefore carries nonnegativity, and none of its three clauses mentions `init`, `U` or fibre cardinality, so none privileges either rule.

**What is not proved, and is not thereby refuted.** Two frozen theorem statements are deliberately absent from the module: the universal-agreement side, which cannot hold since it is the exact negation of what closed; and the criterion-failure side, for which no counterexample exists to exhibit because admissibility of both named rules closed. That absence is the record of which outcomes were not reached. A failed search is never reported as its negation.

**What this licenses.** *The merged OI → `QfbData` bridge does not select the candidate at this interface*, so a candidate-selection principle is **required** before the interference question is well posed at family level — stated as a requirement, with no such principle proposed or adopted.

**What it does not.** No claim that the external framework requires an additional physical principle: act 1 established that the external diagnostic uses a *particular* candidate while `PDivisible` quantifies existentially, and that construction may supply the selection canonically from its own dilation — in which case the task is to show **our** representation instantiates **his**, which is a separate mapping obligation no theorem here addresses. No claim that no neutral admissibility criterion exists, since the round quantifies over no space of criteria. Nothing identifies `candidateOf` with any external object, and nothing here is a sourcing claim.

### 3.16 Source C's construction produces no intermediate candidate to select

Track B act 4 is closed at **`MP4` — unresolved at the frozen interface**. `verification/programmes/oi-qm/track-b/act-04-dilation-mapping/result.md` records it. It is an **audit determination, not a theorem**: act 1's evidence levels 1 and 3, never level 2, and no Lean was written.

**The question.** Act 3 left it open whether the missing candidate selection was already supplied by the external correspondence. Against **Source C's theorem construction** — the only one this round adjudicates — the answer is narrower than either yes or no: that construction produces no intermediate candidate at all, so there is nothing there to select.

**What the construction does.** Starting from the tuple with one conditioning time taken to be `0`, non-negativity lets each transition probability be written `Γ_ij(t ← 0) = |Θ_ij(t ← 0)|²` (eq (72)); a dictionary (81) expresses `Γ` as a trace; a Kraus decomposition (87)–(91) gives a CPTP map; and Stinespring dilation (§5.7) purifies it to a unitary `Ũ(t ← 0)` on `H̃` of dimension `Ñ ≤ N³`, with the dilated transition matrix unistochastic at (105).

**Why that leaves the frozen question unanswered.** Every object it builds is indexed `(t ← 0)`, and the dilated process's conditioning-time set is declared the singleton `{0}` (§5.8). So the construction's output contains **no propagator from an intermediate time**, and hence no visible intermediate candidate. The frozen M2a asks what *the construction* fixes; a construction that fixes no candidate answers neither *uniquely* nor *up to a named parameter*, which is why the outcome is `MP4` rather than `MP2`. The only route from its outputs to a candidate is the relative operator, which Source C does not form — and act 4 declines to form it on the source's behalf, since reading an answer off an unauthorized post-processing and attributing it to the construction is exactly the error the round's own rule forbids.

**A countercontrol, not a determination.** Along the relative-operator route the answer would turn on a choice. The source states the non-uniqueness itself: eq (72) is "an **identity**, not a postulate", and `Θ` is a "**non-unique** potential matrix" fixed per target time. Right-multiplying `Θ(t ← 0)` by a diagonal unitary preserves every constraint, and act 4 exhibits two admissible choices whose relative operators give the **identity** and the **swap** — different visible propagators from the same `Γ`. This is recorded as a countercontrol on *that one rule*, showing the open question is not easy. It does **not** say what Source C selects, and does not show that every extraction rule is choice-dependent.

**The freedoms, at the scope each has earned.** The per-target-time phase freedom in `Θ` beyond `|Θ|²` is exhibited as candidate-load-bearing for the relative-operator rule. The Stinespring completion — added columns that "can always be chosen", dimension only bounded — is **not** shown to move any visible candidate, so it is recorded as downstream representation non-uniqueness and is not named as a selection datum.

**Hypotheses.** All satisfied against our source-side datum — the merged `RootedRealization` read as a tuple through act 1's Q8 — under the permitted `T₀ = {0}` and `p` declarations. `p` is undetermined on our side but the transition-bearing layer never consumes it, which extends Q8's §5.1-scoped observation to the layer that would induce a candidate.

**What would settle it.** An append-only frozen amendment admitting and defining a candidate-extraction rule, which would let M2 be asked of a stated interface rather than of a construction that has none — or **Source A's earlier construction**, out of scope here and forming relative operators in its own development.

**What this does not say.** Not that the external framework requires an additional physical principle; act 3's frozen licence forbids it and this round does not earn it. Not that the selection is unavailable. Nothing about the backward obligation, which was not attempted. And `CU1a` is untouched: it is a theorem about **our** bridge, and no external audit revises it.

### 3.17 Source A forms an intermediate candidate, and it is not fixed by the visible data

Track B act 5 is closed at **`SA2` — selection conditional on a named extra datum**. `verification/programmes/oi-qm/track-b/act-05-source-a-candidate/result.md` records it, under the contract frozen by PR #568. It is an **audit determination, not a theorem**: act 1's evidence levels 1 and 3, never at level 2, and no Lean was written. **Source A alone is adjudicated**, on the PDF of arXiv:2302.10778v3 as the authoritative numbering surface.

**The question.** Does Source A's relative-time machinery define a visible intermediate candidate, is it part of the construction rather than post-processing, and is the candidate fixed by the stochastic datum or does it depend on further choices?

**The object, and the dichotomy underneath it.** Source A contains two relative-time objects. `Γ̃(t ← t′) ≡ Γ(t ← 0)Γ⁻¹(t′ ← 0)` at eq (37), p. 13, is computed from the visible data alone — where `Γ(t′ ← 0)` is invertible, a hypothesis (37) states explicitly — and Source A rules it out anyway: the inverse of a stochastic matrix is stochastic only for permutation matrices, so `Γ̃` is "not generically stochastic". `Γ_ik(t ← t′) ≡ |U_ik(t ← t′)|²` at eq (42), p. 14, built from the relative time-evolution operator `U(t ← t′) ≡ U(t ← 0)U†(t′ ← 0)` at (39), p. 13, **is** "manifestly unistochastic" — a genuine visible candidate. So the object computable from the visible data is not a candidate, and the object that is a candidate is not computable from the visible data.

**It is part of the construction.** Not merely located: eq (43), p. 14 uses it to produce what Source A calls "the general mathematical formula for quantum interference", and the same readout is carried into division events and the Markov approximation (§3.7, (46)), entanglement (§3.9, (65)–(66)) and the measurement process (§4.2, (73)–(77)). Act 5 invents nothing on Source A's behalf.

**Why the candidate is not fixed by the visible data, and the two layers that must not be run together.** Evaluating (39)/(42) consumes, over and above the **base stochastic datum** — the family `Γ(s ← 0)`, presupposed unistochastic at (39) — a **choice of unitary lift** `U(s ← 0)` constrained only by `Γ_ij = |U_ij|²` at (30), p. 11. Eq (30) determines `Γ` from `U` and not conversely, so the lift is an extra construction parameter, not a restatement of the base datum. The admissibility of two different lifts is **definitional**: p. 11 defines a unistochastic matrix as one whose entries are the modulus-squares of a unitary's, and (39) takes "unitary time-evolution operator `U(t ← 0)`" as given, so any unitary meeting (30) qualifies. Source A separately recognizes the freedom — `Θ(t ← 0)` is "guaranteed to exist, although it is **not unique**" (p. 7), footnote 6, p. 7 calls it "a previously unrecognized form of **gauge invariance**" under "arbitrary, time-dependent phase factors" that alters "the dynamics" while leaving "all empirical results unchanged", and p. 9 adds that these objects "are not uniquely defined by `C` or by `Γ(t ← 0)`" — but the round does **not** rest admissibility on that footnote, whose empirical-results sentence could otherwise be read as restricting which transformations count as gauge.

**Exhibited at the visible level, across the whole family.** Given a lift with `U(t′ ← 0) = U(t ← 0) = H` the real Hadamard, take any diagonal-unitary-valued `D(s)` with `D(0) = D(t′) = 𝟙` and `D(t) = diag(1, −1)`, smooth if wanted, and set `U′(s ← 0) = U(s ← 0)D(s)`. Then `|U′(s ← 0)|² = |U(s ← 0)|²` for **every** `s` — the two lifts agree with the base datum at every time, not merely at the two endpoints — while the relative readout at `(t, t′)` is the **identity** from `U` and the **swap** from `U′`. Displayed as candidates, after the readout, not as operators.

**The named datum** is therefore that choice of lift, whose relative part between the two times is what moves the candidate. It is a freedom **internal to Source A's construction**, not a datum missing from our side.

**The branch this settles, and the freedoms at the scope each has earned.** `SA2` is established on the **direct unistochastic branch** that eq (39) assumes. The lift freedom is examined and exhibited. The choice of number system for `Θ` and lifts outside the `E U D` orbit are recorded **not examined** rather than absent; neither bears on which of A5's three answers holds, since the exhibition rules out *unique* and fixing the lift rules out *unresolved*. The Stinespring dilation freedom is recorded as representation freedom and not named as a selection datum, exactly as act 4 recorded its counterpart — and is **scoped, not dismissed**: on a non-unistochastic visible process §3.4's dilation runs before (39) applies, and its choice may then be load-bearing, a case this round does not adjudicate. What stays open on the settled branch is whether the parameter list is complete.

**What this changes at programme level.** The missing selection is now **located** rather than supplied: an external construction does form the candidate, and does not fix it from the visible transition data.

**What it does not say.** Not that the external framework requires an additional physical principle — act 3's licence forbids it and this round does not earn it. Not that the selection is unavailable; an operational specification could fix the representatives, and act 5 did not look. Nothing comparing Source A with Source C on quality, equivalence, agreement or supersession — all four are outside the freeze, and whether the two agree is recorded open. `CU1a` is untouched, act 4's `MP4` is unrevised, and no extraction rule has been authorized: A6 **names** a parameterized family and selects no member of it.

**The sharpest open question it produces.** Eq (43)'s discrepancy moves with the gauge, its other two terms being invariant, while §3.6, p. 15 reads that discrepancy empirically. Act 5 records the tension and **does not adjudicate it** — settling it needs the operational content of "a heuristic-approximate divisible approximation" pinned down well enough to say whether it fixes the representatives.

### 3.18 OI instantiates the external tuple, and is not contained in the direct unistochastic branch

Track B act 6 is closed at the **pair `(TI1, UB2)`**. `verification/programmes/oi-qm/track-b/act-06-tuple-instantiation/result.md` records it, under the contract frozen by PR #570, and `verification/lean-mathlib/OIBridge/BarandesTuple.lean` carries the mathematics: twenty-four named results at act 1's **evidence level 2 — kernel-checked**, each printing only `[propext, Classical.choice, Quot.sound]`. It is the first Track B round since act 2 to write Lean.

**Two layers, and they are independent.** Layer 1 reads Source C v2 and mentions unistochasticity nowhere; layer 2 reads Source A and uses no component of the tuple. Neither label is evidence for the other, and the round reports a pair rather than one headline.

**`TI1` — the OI visible class instantiates Source C v2's tuple.** `BarandesTuple` types the tuple `(C, T, T₀, Γ, p, 𝒜)` of eq (24), p. 8 with all ten axioms of eqs (25)–(35) and (40)–(41) as fields, each cited and each proved as its **own named result** — the four carried by the declarations included, since a component supplied by `rfl` is still a component that has to be checked against what the source asks for. `barandesTupleOfPPer` then instantiates it from `PPer Γ` — Arc B's exact OI visible class, so the theorem holds for every member rather than for one realization — under the declarations `C = V`, `T = ℕ`, `T₀ = {0}`, `Γ_B(t ← 0) = (Γ t)ᵀ` in act 2's orientation, and `𝒜` the maximal algebra of maps `V × ℕ → ℝ`.

**`p` is constructed, and `p0` is parameterized.** Source C's eq (33), p. 10 *fixes* `p` at every later time from `p(0)` and `Γ`; only `p(0)` is free, by eq (32). So the whole time-dependent distribution is built from an arbitrary normalized `p0`, the marginalization axiom holds by construction, and all-time normalization is **derived** from the other two — as Source C itself derives eq (34) from (28) and (32). Act 1's **Q8** stands: our datum does not carry `p`, and the theorem takes `p0` as a hypothesis rather than supplying it.

**The `T₀ = {0}` vacuity, in two parts.** Source C's divisibility axiom, eq (35), p. 10, is *required* — the source writes that `Γ` "will be assumed to satisfy" it — but quantifies only over conditioning times, never over general target times, which is how it coexists with act 1's `BD3` and with the source's own p. 11 remark that the process "is therefore indivisible for generic target times". It is discharged here at the singleton by trivialization. **And discharging it bears on our all-time `PDivisible` in neither direction**, proved separately by exhibiting two `PPer` families that both satisfy the singleton condition, one `PDivisible` and one not. No reading of `TI1` licenses the inference that the OI family is divisible.

**`UB2` — the OI class is not contained in Source A's direct unistochastic branch.** `IsUnistochastic` is Source A eq (30), p. 11 defined from scratch — existence of a complex unitary whose entrywise modulus-squares are the matrix — and deliberately not routed through `QfbData`, `QStar`, `born` or `overlap`, since defining it that way would build Arc D's disqualified representation shortcut into the predicate. Source A's own p. 11 observation that every unistochastic matrix is doubly stochastic is proved rather than cited, and makes the branch decidable by a stochasticity check. The witness is a lawful `PPer` family on `Fin 2` with `Γ 0 = 1`, period `2`, and a collapsing row-stochastic slice, upgraded through the merged `pper_has_responseRealization` to a genuine `RootedRealization`. Its transpose is column-stochastic and fails **row** stochasticity, so the refutation runs through the row half of the structural lemma — the orientation that survives transposition into Source A's convention.

**What this changes at programme level, and at exactly `UB2`'s strength.** The instantiation obligation act 3 named as a separate task is discharged at layer 1's scope. And a **full-class** correspondence route — one covering all of `PPer` — cannot stay entirely on Source A's direct branch: it must handle the **dilated** branch for the exhibited off-direct members. `DirectBranch` is false, which is an existential fact — some lawful member is off the branch — not a classification of every member, so directly unistochastic OI members may still use the direct branch, and this round says nothing about how many there are.

**What it does not say.** Not that the external correspondence fails: Source A's §3.4, p. 10 dilates a non-unitary `Θ(t ← 0)` to a unitary one on a larger carrier, so a visible matrix that is not unistochastic may still embed there. Not that every OI family is off the direct branch — `UB2` refutes a universal statement by one lawful witness and classifies nothing. Direct unistochasticity and dilatability are **different propositions** and neither is inferred from the other in either direction. Whether the dilation choice moves the induced candidate is not adjudicated. `CU1a`, `MP4` and `SA2` are cited and left exactly as merged, no candidate-selection principle is adopted, nothing here claims OI forces quantum structure, and nothing here is a sourcing claim.

### 3.19 Source A's dilation does not accept the off-direct witness we have

Track B act 7's **layer 1** is closed at **`DC2a` — §3.4's input contract is not met by the off-direct witness**. `verification/programmes/oi-qm/track-b/act-07-dilation-choice/result.md` records it, under the contract frozen by PR #572. It is an **audit determination at act 1's evidence level 3**, on the PDF of arXiv:2302.10778v3 verified by its p. 1 stamp. **No Lean was written and layer 2 was not reached.**

**The question.** For an OI/`PPer` process off the direct branch, does Source A's dilation contain free choices that move the **visible** candidate?

**What is dilated (D1).** `Θ(t ← 0)`, the time-evolution operator, by enlarging the configuration space — §3.4, p. 10, "if `Θ(t ← 0)` is not **already** a unitary matrix, then one can **turn it into** a unitary matrix by enlarging or **dilating** the original `N`-element configuration space". Not the visible family, and `Θ` is already a non-unique choice upstream ((12) p. 6; "not unique", p. 7).

**Why the round stopped (D2).** The orientation half of the contract is met: Source A normalizes over the **first** index at (3) p. 4 and names the object a "(column) stochastic matrix", which act 6's `transpose_nonneg` and `transpose_isColStochastic` supply for `(Γ t)ᵀ` under act 2's `RT1`. So does every hypothesis §3.4 restates locally. What fails is **inherited, and exactly one hypothesis is load-bearing**: p. 4's **continuity condition**, that `Γ(t ← t₀)` "**will be assumed**" to approach `𝟙` as `t → t₀` — unhedged, and uninstantiated on `ℕ` with `t₀ = 0`, where that limit carries no content. Act 6's off-direct witness is literally `Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ`. p. 3's sentence that target times are "**usually** … isomorphic to the real line `ℝ`" carries the source's own hedge, so it is recorded as the **usual setting** the continuity condition is written for — the domain mismatch behind that failure — and **not** as an independent hard prerequisite.

**Two observations cut the other way and were recorded, not suppressed** — §3.4's Stinespring step is applied at a fixed `t` and does not itself invoke continuity, which is consumed downstream at (33) p. 12 where the source adds "differentiable function of the time `t`"; and the source exhibits discrete-time instances of its own (fn. 11 p. 12; (57)–(58) p. 19). **Neither licenses narrowing D2 to §3.4's own sentences**, which the freeze forbade in terms before the source was read. A contract narrowed after reading the source is not the contract that was frozen.

**One layer-1 finding survives the stop (D3), and it is a gap of derivation and selection rather than a missing assumption.** §3.4 asserts the dilation **per `t`** — Stinespring "implies the **existence**" of `Ũ(t ← 0)` at each `t` — and neither derives nor selects a coherent time-indexed family. A regularity assumption *does* arrive: (28) p. 11 drops the tildes "without any real loss of generality" and (33) p. 12 then assumes that post-(28) unitary family is "a **differentiable function** of the time `t`". So the finding is **not** that the source assumes nothing, nor that it imposes no analogue on the dilated object. It is that **Stinespring supplies only pointwise existence, and the source never shows an admissible dilation choice meeting (33)'s regularity exists, nor selects one**, while the relative operator (39) p. 13 consumes **two** times. A property of Source A's text rather than of our witness, so it stands open.

**What this changes at programme level.** The dilation obligation act 6 identified is **not yet testable on the witness we have**. The next obligation is specific, and its wording matters because `PPer` is `ℕ`-indexed by definition so there is no such thing as a "continuous `PPer` witness": **construct a Source-A-admissible continuous EXTENSION of a lawful off-direct OI/`PPer` witness — with its OI/`PPer` restriction identified and off-directness preserved — or prove no such extension exists under the OI constraints.** If the extension relation is not yet defined, defining it is the first sub-obligation, and it is a Track I question. A hazard is recorded from the source itself — footnote 11, p. 12 gives Source A's own discrete-to-continuous interpolation and it produces a **unistochastic** family, which is the wrong side of the branch for an off-direct witness, so the obvious continuization may destroy the property the witness exists to have. Recorded as a signpost, not as a proof of impossibility. Whether the OI visible class has a continuous-time formulation at all is a Track I question: Arc B's `C_OI(V) = PPer(V)` is defined over `ℕ` with a periodicity condition.

**What it does not say.** Not that the dilation is inapplicable to OI, not that the correspondence fails, and nothing whatever about whether the dilation moves the visible candidate — `DC1`, `DC3` and `DC4` are **not reached**, and none of them is *unresolved*. A **counterfactual** source reading is recorded and is explicitly **not outcome-bearing**: conditional on D2 being repaired, D4a reads positive and D4b negative, which would route to the readback-amendment path rather than to `DC2b`. `BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1` and `UB2` are cited and unrevised; nothing here is a sourcing claim; no manuscript is edited.

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

Track B act 3, **candidate selection and uniqueness**, is executed and closed at **`CU1a`** (§3.15). It changes what the next Track B round can be: an interference round is **not well posed on this route** until a candidate is selected, because the representation does not select one.

**Further Arc D rounds remain paused** pending the decision below. Everything merged by PR #554 stands; the pause is on new rounds, not a retraction.

Track B act 4, **the dilation mapping obligation**, is executed and closed at **`MP4`** (§3.16): Source C's construction produces no intermediate candidate at all, so the frozen question of what it selects has no answer at that interface. Act 5, **Source A's candidate selection**, is executed and closed at **`SA2`** (§3.17): Source A does form the candidate, as part of its own development and load-bearing for its interference formula, but computes it from the unitary rather than the transition matrix, so it is fixed only given a choice of unitary representatives — exhibited at the visible level as the identity against the swap on the same transition data.

**Together these two acts locate the missing selection rather than supplying it.** They do not exhaust the source-side questions: act 5 leaves open the tension between the gauge-dependence of the (43) discrepancy and §3.6's empirical reading of it, the completeness of its parameter list, and the non-unistochastic branch it does not adjudicate. What they do settle is bounded: **neither construction, under the aspects adjudicated so far, supplies a canonical candidate.** Any of the open items above could still reveal a canonicalization mechanism, so this is not a claim that none exists. Two live options remain and should not be conflated: adopt a selection principle on our side and say plainly that it is an addition to the merged bridge, or argue some member of the family Source A's construction names canonical on grounds act 5 did not examine. Neither has been adopted.

Track B act 6, **tuple instantiation and the Source-A branch test**, is executed and closed at the pair **`(TI1, UB2)`** (§3.18), and it is a kernel round rather than an audit: twenty-four named results at evidence level 2. It answers both of the questions that put it at the front of the queue. Our processes **do** instantiate the external tuple — Source C v2's actual ten-axiom process, typed rather than summarized, at `T₀ = {0}` with `p0` parameterized — so "OI instantiates the tuple" is now checkable rather than argued. And the containment question act 5 deferred to it is settled in the direction act 6 predicted: the OI class is **not contained in** the direct unistochastic branch, so a full-class correspondence route cannot stay entirely on it and must handle **act 5's dilated branch** for the exhibited off-direct members. `DirectBranch` is false, which is an existential fact — some lawful member is off the branch — not a classification of every member, so directly unistochastic OI members may still use the direct branch.

**That made the dilation the next load-bearing obligation on Track B's full-class route**, and act 7 went at it. Act 7's **layer 1** is closed at **`DC2a`** (§3.19): Source A's §3.4 does not accept the off-direct witness we have, because of one **inherited** hypothesis — p. 4's **continuity condition**, that `Γ(t ← t₀)` "will be assumed" to approach `𝟙` as `t → t₀`, which is uninstantiated on `ℕ` where that limit has no content, act 6's witness being `ℕ`-indexed. p. 3's "**usually** … isomorphic to the real line" carries the source's own hedge and is context for that failure, not a second one. Layer 2 was **not reached**, so nothing is known — in either direction — about whether the dilation moves the visible candidate.

**The obligation is therefore displaced rather than discharged**, and it is now sharper: **construct a Source-A-admissible continuous EXTENSION of a lawful off-direct OI/`PPer` witness — its `PPer` restriction identified, off-directness preserved — or prove none exists under the OI constraints.** `PPer` is `ℕ`-indexed, so the object sought is an extension rather than "a continuous `PPer` family", and if the extension relation is not yet defined then defining it is the first sub-obligation and a Track I question. Act 5's `F4` remains the freedom that may be doing work, and act 7's D3 recorded a finding that survives its own stop — Stinespring supplies only **pointwise existence**, and the source neither derives nor selects a dilation family meeting the differentiability (33) p. 12 assumes of the post-(28) unitary, while the relative operator needs two times. If such an extension is produced, act 7 reopens at D4a positive / D4b negative, on the readback-amendment path. What a dilation round would have to establish is act 5's `A4`/`A5` burden one branch over: whether the choice of dilation moves the **visible** candidate, exhibited at the visible level rather than at the operator level, per act 4's earned control.

Behind it stand the question `BD3` leaves open — what `PIndivisibleWithin` adds *on top of* class membership, which act 1 located in the external framework's interference term — along with Arc D round 2 and Arc E. Which of those follows the continuous-extension obligation is the decision the programme now faces.

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
11. **Formalization-first manuscript synchronization gate.** The central OI → QM claims and proof narrative are not to be strengthened, reorganized, or newly integrated into the publication-facing manuscripts while the load-bearing chain is still being formalized. Arc B and Arc C results remain verification-layer results until the Arc D and Arc E obligations the intended claim actually uses are kernel-closed or carry an explicit disposition under §6. Manuscript integration then proceeds in one synchronized pass, generated from the theorem-to-prose spine rather than from the current prose. Corrections to statements already known to be false, over-scoped, or misqualified are exempt and are never delayed; so are bibliographic, typographic and formatting fixes. The gate, its exception, the spine and the synchronization procedure are stated in full in `verification/programmes/oi-qm/amendments/amendment-1.md`, which controls their detail.

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
- `verification/audits/operational/census-oi-compatible-theories.md` — finite OI-compatible completion classes;
- the individual `*-AUDIT.md`, `*-RESULT.md`, and amendment files — preregistered questions and exact outcomes;
- `verification/programmes/oi-qm/amendments/amendment-1.md` — the formalization-first manuscript synchronization gate, its exception, the theorem-to-prose spine, and the synchronization procedure;
- `verification/programmes/oi-qm/amendments/amendment-2.md` — the two-track programme, the pause on further Arc D rounds, and the rule that neither track is evidence for the other;
- `verification/lean-mathlib/OIBridge/` — kernel statements and their hypotheses;
- `papers/GR.md`, `papers/Main.md`, the Explainer, and book chapters — publication-facing statements under their scope guards.

`verification/ROADMAP.md` remains the historical roadmap for the original zero-import verification layer. It is not the strategic roadmap for the larger OI → QM equivalence/classification programme.

---

## 10. Current one-line programme state

At the post-act-6 boundary, with Track B acts 1 through 6 closed:

**Arcs B, C and Arc D round 1 are kernel-closed: finite reversible OI yields exactly `PPer` at the rooted stochastic level, its relation to the all-time fixed-basis Born representation class `Q*` is RC1 proper overlap, and representational presence is now a proved disqualified ground rather than a stated discipline — arbitrary finite-ancilla unitary padding preserves the represented family exactly, so the operator properties Arc D proves free are exhibited in some representation of every representable family, and every resource expressible in an admissible finite-unitary conjugation is vacuous under the representation-augmented criterion, so no sourcing claim may rest on either. The programme is two-track from here: the Barandes correspondence route and the internal Arc B/C/D/E reconstruction route, neither usable as evidence for the other. Track B act 1 is closed at (BD3, BR3): Barandes's *indivisible stochastic process* is a tuple class containing Markov chains, not our failure predicate, and failure of divisibility is no hypothesis of his theorem though it is what his interference derivation runs on; separately, his factorization equation is our `PDivisible` body exactly after transposition. Act 2, the Lean transpose bridge, is closed at RT1: the two orientations are the same predicate under transposition, proved rather than argued, confirming act 1's Q4 and leaving the horizon difference standing. Act 3, candidate selection, is closed at CU1a: two independently admissible extraction rules give different visible candidate propagators on one lawful representation with the representation held FIXED, so the merged OI → QfbData bridge does not select the candidate at this interface and a candidate-selection principle is required before “OI forces this interference discrepancy” is a well-defined family-level question — which is a requirement on this side and not a claim that the external framework needs an added principle, since that construction may supply the selection canonically from its own dilation. An interference round is therefore not well posed on this route until a candidate is selected. Act 4, the dilation mapping obligation, is closed at MP4: Source C's theorem construction runs on our datum — every hypothesis satisfied under the permitted T0 and p declarations — but every object it builds is indexed from time 0 and its dilated process declares the conditioning-time set to be the singleton {0}, so it produces no intermediate propagator at all and there is nothing there to select; the frozen question of what the construction fixes therefore has no answer at that interface, which is MP4 and not MP2, since MP2 would presuppose a candidate the construction does not yield. The only route from its outputs to a candidate is the relative operator, which Source C never forms and which act 4 declines to form on the source's behalf; as a countercontrol on that one rule, two admissible choices of the non-unique potential matrix Theta give relative operators whose modulus-squares are the identity and the swap, so that route would not be choice-free. The Stinespring completion is recorded as downstream representation non-uniqueness and is NOT named as a selection datum, not having been shown to move any candidate. This is an audit determination and not a theorem, it says nothing about the external framework needing an added physical principle, and it leaves CU1a untouched. Settling the question needs either an append-only frozen amendment defining a candidate-extraction rule or Source A's earlier construction, which was out of scope by that round's freeze. Act 5 took Source A, adjudicating it alone, and is closed at SA2: Source A DOES form a visible intermediate candidate as part of its own development — the modulus-squares of the relative time-evolution operator, which it builds at eq (39) p.13 and reads out at eq (42) p.14, and which is load-bearing because its interference formula at (43) runs on it and three later subsections carry it. But evaluating it consumes, over and above the base stochastic datum, a choice of unitary lift constrained only by eq (30) p.11 — and (30) determines Gamma from U and not conversely, so the lift is an extra construction parameter rather than a restatement of the base data. Admissibility of two different lifts is definitional, from p.11's definition of unistochastic and (39) taking a unitary time-evolution operator as given, and does not rest on the footnote 6 gauge reading, which act 5 records as corroboration only. Act 5 exhibits two lifts agreeing with the base datum at EVERY time, not merely at the two endpoints in play, whose VISIBLE readouts at the pair of times are the identity and the swap. So the extra datum SA2 names is that choice of lift — a freedom internal to Source A's construction and explicitly NOT a datum missing from our side, containment against our RootedRealization being deliberately deferred to the tuple-instantiation step. SA2 is established on the direct unistochastic branch eq (39) assumes; the non-unistochastic case, where section 3.4's dilation runs first and its choice may become load-bearing, is scoped out and not adjudicated. Underneath sits the dichotomy the round reports: Source A's other relative object, at eq (37), IS computed from the visible data alone where Gamma(t'<-0) is invertible, as (37) itself requires, but is not generically stochastic, so the object computable from the visible data is not a candidate and the object that is a candidate is not computable from the visible data. The missing selection is therefore located rather than supplied. Act 5 adopts no principle — A6 names a parameterized family and selects no member — leaves CU1a and act 4's MP4 untouched, authorizes no extraction rule, and compares the two sources on no axis, whether they agree being recorded open. Its sharpest open question is that the (43) discrepancy moves with the gauge while Source A reads that discrepancy empirically, a tension act 5 records and does not adjudicate. Act 6 then took the tuple-instantiation lemma and is closed at the PAIR (TI1, UB2), the first Track B round since act 2 to write Lean: twenty-four named results at kernel evidence, in two layers that are independent by construction, layer 1 mentioning unistochasticity nowhere and layer 2 using no component of the tuple, so neither label is evidence for the other. TI1 proves that the OI visible class instantiates Source C v2's actual tuple — eq (24) p.8 with all ten axioms of (25)-(35) and (40)-(41) typed as fields rather than summarized, each cited and each proved as its own named result — at C = V, T the naturals, T0 = {0}, Gamma_B(t<-0) the transpose of Gamma t, and the observable algebra maximal on V times T. It is proved for PPer, the exact OI visible class, not for one realization. p is CONSTRUCTED and not declared, because eq (33) p.10 fixes p at every later time from p(0) and Gamma leaving only p(0) free by (32), so all-time normalization is derived from (28) and (32) exactly as the source derives (34); p0 is parameterized and never supplied, so act 1's Q8 stands unchanged. The divisibility axiom (35) p.10 is a REQUIRED axiom quantified over conditioning times only, which is how it coexists with BD3 and with the source's own remark that the process is indivisible for generic target times; it is discharged at the singleton by trivialization, and — proved separately, not asserted — discharging it bears on our all-time PDivisible in NEITHER direction, two PPer families being exhibited that both satisfy the singleton condition, one P-divisible and one not. So TI1 licenses no inference that the OI family is divisible. UB2 settles the containment question act 5 deferred: IsUnistochastic is Source A eq (30) p.11 defined FROM SCRATCH and deliberately not routed through QfbData, QStar, born or overlap, since defining it that way would build Arc D's disqualified representation shortcut into the predicate; Source A's own p.11 observation that every unistochastic matrix is doubly stochastic is proved rather than cited; and a lawful PPer family on Fin 2, upgraded to a genuine RootedRealization through the merged pper_has_responseRealization, is exhibited whose transposed slice is column-stochastic and fails ROW stochasticity, so DirectBranch is false. Direct unistochasticity and DILATABILITY are different propositions and neither is inferred from the other in either direction: section 3.4 p.10 dilates a non-unitary Theta to a unitary one on a larger carrier, so a visible matrix that is not unistochastic may still embed there, and NO result says the external correspondence fails. What UB2 does is put the FULL-CLASS route onto act 5's dilated branch, the branch act 5 scoped out: a correspondence covering all of PPer cannot stay entirely on the direct branch and must handle the dilated one for the exhibited off-direct members, while directly unistochastic OI members may still use the direct branch — UB2 refutes a universal statement by one lawful witness and classifies no member beyond it. That makes the dilation the next load-bearing obligation on Track B's full-class route and makes act 5's F4 the freedom that may now be doing work; what a dilation round must establish is act 5's A4/A5 burden one branch over, whether the dilation choice moves the VISIBLE candidate, exhibited at the visible level per act 4's earned control. Act 6 adopts no candidate-selection principle, leaves CU1a, MP4 and SA2 exactly as merged, edits no manuscript, and claims nothing about sourcing in either direction. Act 7 then took the dilation round and its LAYER 1 is closed at DC2a, with no Lean written and layer 2 NOT REACHED: Source A's section 3.4 dilates Theta rather than the visible family, by enlarging the configuration space, and the orientation half of its contract is met by our transposed object — Source A normalizes over the FIRST index at (3) p.4 and names the object a column stochastic matrix, which act 6 supplies — as is every hypothesis section 3.4 restates locally; what fails is INHERITED and exactly one hypothesis is load-bearing — p.4's continuity condition, which Gamma WILL BE ASSUMED to satisfy as t approaches t0, unhedged and uninstantiated on the naturals where that limit has no content, act 6's off-direct witness being literally an N-indexed discrete family on Fin 2; p.3's sentence that target times are USUALLY isomorphic to the real line carries the source's own hedge and is recorded as the usual setting behind that failure rather than as an independent hard prerequisite. Two observations cutting the other way were recorded rather than suppressed — the Stinespring step is applied at a fixed t and does not itself invoke continuity, which is consumed downstream at (33) p.12 where the source adds differentiability, and the source exhibits discrete-time instances of its own at footnote 11 p.12 and at (57)-(58) p.19 — and NEITHER licenses narrowing D2 to section 3.4's own sentences, which the freeze forbade in terms before the source was read. One layer-1 finding survives the stop, and it is a gap of DERIVATION AND SELECTION rather than a missing assumption: section 3.4 asserts the dilation PER t, Stinespring giving only pointwise existence at each t and neither deriving nor selecting a coherent time-indexed family, while a regularity assumption does arrive — (28) p.11 drops the tildes without real loss of generality and (33) p.12 then assumes that post-(28) unitary family differentiable in t — so the finding is NOT that the source assumes nothing or imposes no analogue on the dilated object, but that it never shows an admissible Stinespring choice meeting that regularity exists nor selects one, while the relative operator (39) p.13 consumes TWO times. DC2a is a finding about a CONTRACT and not about dilations: DC1, DC3 and DC4 are not reached and none is unresolved, and a counterfactual source reading — that conditional on repairing D2, D4a is positive and D4b negative, routing to the readback-amendment path rather than DC2b — is recorded explicitly as NOT outcome-bearing. The next obligation is to construct a Source-A-admissible continuous EXTENSION of a lawful off-direct OI/PPer witness, with its PPer restriction identified and off-directness preserved, or prove none exists under the OI constraints — phrased as an extension because PPer is N-indexed by definition, so a continuous PPer witness is not a thing, and if the extension relation is not yet defined then defining it is the first sub-obligation and a Track I question. A hazard is recorded from the source itself, that its own discrete-to-continuous interpolation at footnote 11 p.12 produces a UNISTOCHASTIC family and so lands on the wrong side of the branch. The continuous-extension obligation, the question BD3 leaves open, Arc D round 2 and Arc E are the decision now open. Publication-facing strengthening of the central OI → QM argument is deferred under §7 rule 11 until that formal chain is closed or precisely classified, after which the manuscripts are synchronized in one pass from an explicit theorem-to-prose spine.**
