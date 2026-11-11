# TUNE-1, Step 1: the assumptions behind the state-mixing obstructions

**WIP / UNVERIFIED writer draft, revision r3 after two independent reviews (REVISE on `204043ce`; REVISE, narrow, on `e9fbe998`); r3 itself is not reviewed; paper-only; pin = origin/main SHA `cac5d26441dd33e9348151487e4df7b547195481`.**

Research unit under Issue #1236 (owner decision: paper-only). This file adopts no premise,
changes no manuscript or Lean file, promotes no claim and authorizes nothing. It has not been
independently reviewed. Step 2 (evaluation of candidate mechanisms) is not authorized and is not
attempted here.

**Pin and drift.** Every source was read in a worktree at the pin. `origin/main` advanced to
`553e790ba52be296b2327030798dd636bd924807` during the session (three commits, PR #1233). Between
the two commits the only changed files are `papers/Main.{md,tex,pdf}`, `papers/SM.{md,tex,pdf}`
and one fingerprint in `verification/coverage/LEDGER.json`; in `papers/Main.md` the changed lines
are 364, 416, 654 and 726, with no line inserted or removed. Of these only Main:726 is cited
below, and the part cited (ledger item (ii)) is identical in both commits. No Lean file and no
research record cited here differs between them.

**Support-layer labels.**

- **[K]**: a theorem or definition in the Lean source under `verification/lean-mathlib/OIBridge/`
  at the pin. The statement was read; where section B says so, the proof text was read too.
  Nothing was built in this unit, so [K] records what the source states, not a build this unit
  observed. A token search of the directory finds no `sorry`, `axiom` declaration or `native_decide` in any file cited here.
- **[P]**: a statement in a manuscript on `main`, at paper level. **[P-imp]**: its support is an
  imported external result.
- **[R]**: a research record on `main` that states it has not been independently reviewed.
- **[D]**: a draft that is not on `main`. Context only; never used as support.
- **[W]**: the writer's own short derivation, unreviewed and not kernel-checked.

"OB/" abbreviates `verification/lean-mathlib/OIBridge/`. "Main:n" is line n of `papers/Main.md`
at the pin.

**Disclosure.** The only commands run were `git` (fetch, worktree add, ls-remote, show, diff,
log, rev-parse, reflog, config, status, add, commit, push), `grep`, `sed`, `awk`, `wc`, `ls`, `df`, `mkdir`, `sha256sum` and `rm` of two
scratch text files used for one word-diff of Main:726. No interpreter, probe, Lean build or other
computation was run. No GitHub comment was posted.

**Disclosure, r2.** The revision added `cut`, `cat` and `sed -f` (text splicing of this file) to
the commands above, and `git show` of the two off-`main` drafts into scratch files. No interpreter,
probe or Lean build was run. The reviewer confirmed by hash that every Main line cited here is
identical at `origin/main` `553e790b`; the pin stays `cac5d264`.

**Reading for r2.** Read in full at the pin: `OB/FrozenSourcing.lean`, `OB/FlowEndpoint.lean`,
`OB/F2CoherenceControls.lean`, `OB/RecursiveFiniteFactor.lean`, `OB/NativePadicReduction.lean`;
`recursive-substates/` (`README.md`, `ANALYSIS.md`, F2-1 preregistration, A★, A★-1, run-2 result
and repairs, FIXED-SCALE-1 report, NATIVE-PADIC-1 report);
`continuous-substates/{README,operational-control-countercontrol,equivalence-and-d3-scope,later-access-result}.md`;
Q-A `DESIGN.md`; MECH-2 `DESIGN.md`; M-INACC-1 `DESIGN.md`, `RESULT.md`, A1, A3; the feedback
`RESULT.md`; `papers/GR.md`:130–142; `oi-qm-ext-1/observer-interface-source.md` §§4–7.

**Reading and disclosure for r3.** Read in full at the pin, for this revision: apparatus-1
`DESIGN.md` (1141 lines), MECH-1 `DESIGN.md` (1179 lines), MECH-2 `DESIGN.md` (1019 lines, a
second time). Re-read for the quotations used below: Q-A `DESIGN.md` :160–180, :455–520,
:915–945; M-INACC-1 `RESULT.md` §§0, 6, 8, 9; Main:726 items (ii), (vii), (xiii). One Issue
comment was read through `gh api` (read-only) and is cited once, as provenance: the owner's Q-B
target decision, #1169 comment 6712409082, which Q-A `DESIGN.md`:6 links. Commands added: `gh api`
(that one read) and `wc -w`. No interpreter, probe or Lean build was run and nothing was posted.
A search of `verification/`, `papers/` and `book/` for "Q-B" finds it in apparatus-1, Q-A, MECH-1
and MECH-2 only. Where a statement rests on the second reviewer's reading and was not re-opened
here, the place says so (section C, first row; section D, row D10).

**Read in part.** `OB/StructuralClosure.lean` (:1–60, :100–245, :300–375),
`OB/SubstratumInterfaceAudit.lean` (:215–360, :480–870), `OB/PhaseSource.lean` (:1–80 and the
declaration list), `OB/PC1Controls.lean` (header, :120–140), `OB/InstrumentRealization.lean`
(definitions of `ones`, `OnesFixing`, `onesClass` and four statements); PC-1 (`README.md`, run-2
result, the disposition, the heads of the preregistration and PC★); M-INACC-1 A2 (:1–60 and its
headings); Q-A `PROOF-RECOVERY.md` (:1–40, :150–212); the wave-sign `ASSESSMENT.md` (:1–60);
`papers/SM.md` §2.7 (:86–96); the 21 `native-*.md` units and five other
notes of `continuous-substates/` (opening and result lines only); FIXED-SCALE-1 and NATIVE-PADIC-1
preregistrations (in part). Off `main`: INTERVENE-1 r2 in full; SUBSTATE-BRIDGE-1 r2 lines 1–256
of 356 (§4.3 onward, its §5 scoring and §6–7 not read).

**Not read.** `verification/audits/foundations/*.md`, `substratum/frozen-sourcing-audit.md` and the
other audit notes behind the Lean modules; `observer-access-20261106`, `physical-controller-20261107`,
`record-control-20261107`, `controller-preparation-1`, `correlation-recombination-20261107`,
`measurement-record-formation`, the remaining `oi-qm-ext-1` files, `la-equal-gap/`; proof bodies
of the sufficiency directions of A.4; the hits of the corpus search for "inaccessib" and
"coarse-grain" under `book/`, `black-hole-information/`, `hydrodynamics/` and `audits/`. A negative
statement below of the form "nothing on `main` decides X" is limited to what is listed as read;
§A.19 is discharged for the records named in B.12 and not beyond them.

***

## Plain-language summary

**Which assumptions exclude continuously tunable mixing?**

- *Finite state representation.* The observer's finitely many states (Lemma 1) exclude nothing
  alone. Two paper-level results need the whole substratum finite (a posit) and exclude exact
  tunability only.
- *Restricted dynamics.* The operative cause in every kernel obstruction. Read as a matrix over
  configuration labels, a quantum state gains no coherence, exactly or approximately, from
  relabelling or averaging over hidden parts in a classical law independent of the input
  (kernel or Main if the hidden part is finite, the approximate form on the two-state carrier;
  unreviewed otherwise).
- *Restricted observational access.* It causes no exclusion. Where posited, for the lattice's
  linear rule, it gave no tunable operation and nothing a classical model lacks (research
  records, unverified). Under one fixed one-to-one linear encoding containing every cell
  correlated with the system, a finite substratum gives finitely many encoded reversible
  operations, whatever the dynamics and reads.

**Exact versus approximate.** On the configuration-label reading both are excluded. For encoded
quantum states, exact tunability needs an infinite state space, whatever the access;
approximation by growing finite systems is constructed in Main, with the quantum rule as input.

**Open on `main`: two questions.**

- *Tunability (Q-B).* What could produce continuous rotations? Its first test (the
  large-alphabet or continuum limit of the linear rule) is not run; its record expects no qubit
  rotation.
- *Nonclassicality (M-INACC).* Does OI keep a quantity the dynamics uses inaccessible, for a
  target-independent reason? Its nearest instance (Lemma Q) needs two posited access
  restrictions and protects present values only; the one further test, on one rule, was
  negative.

Also open: input-correlated memory; an infinite substratum (OI posits finite, derives neither).

## 0. Summary

1. **Kernel obstructions: three invariants, all class 2** (B.1, B.5).
   - *Diagonal preservation.* An operator with at most one nonzero entry in each row and column
     conjugates diagonal matrices to diagonal matrices (monomial and configuration-level
     classes). `rot` violates it.
   - *Nonnegativity preservation.* Scaled partial permutations, and more generally entrywise
     nonnegative operators, preserve entrywise nonnegative matrices (the read/write-sourced
     theory, every bijection-level class, the class `nonnegClass`). `rot` and the quarter phase
     violate it.
   - *Ones-fixing.* Admissible isometries of a ones-fixing class fix the all-ones vector up to a
     scalar. `rot` and the quarter phase violate it.
   The invariants use no bound on the number of states. The kernel's closure of the monomial
   class in the form "permutation times diagonal" uses finite cardinality once
   (`submonomial_monomial`). The interface identification of the matrix basis with the
   configuration labels belongs to none of the owner's three classes.
2. **Counting obstructions: class 1, about the underlying system.** Paper level: a fixed
   realization with `N < ∞` ontic configurations cannot reproduce one qubit's full
   prepare-and-measure theory (Main:560, half imported) and supports finitely many instrument
   families (Main:488). Kernel level: a class of operators countable up to scalar executes no
   layer flow at level one, and on the two-state carrier generates no exact quantum theory.
3. **Restricted access (class 3) is modelled on `main` and is the operative cause of no
   obstruction** (B.12). The research records below are [R]: paper derivations, model-reviewed
   or author-reported at most.
   - *Kernel.* Restricted access appears as discard of a uniformly mixed, input-independent
     finite ancilla and as the class `nonnegClass` of entrywise nonnegative operators. Neither
     yields `rot` or the phases.
   - *Results for every dynamics* [R]. MECH-2 Lemma F and Theorem U2(ii) assume a fixed bijection
     of a finite configuration set, cells attached in fixed laws, H-LIFT (every cell correlated
     with the encoded carrier belongs to it) and a fixed injective linear frame. They place no
     condition on the reads. Their conclusion: every encoded unitary is a frame symmetry, so the
     encoded unitaries form a finite group. Only Theorem NC, on noncontextuality, adds spanning
     preparations and reads; at `q = 2` the native reads do not span and its verdict is undecided
     there.
   - *Results under posited access restrictions* [R]. For the lattice model's linear rule with
     the access posits P1 and P2 and the arming posit P3: at `q = 2` in the one-cell frame, no
     encoded quarter phase, no encoded `rot` and no encoded dense control (apparatus-1 Lemma 5,
     §4.7); at odd prime `q` in Gross's frame, every protocol of the linear class is a stabilizer
     instrument, every encoded unitary is Clifford, and a noncontextual model reproduces the
     reachable class (MECH-1 Theorem W, Proposition C). Each is a result for the construction
     tested.
   - *The named missing premise* [R]. M-INACC (MECH-2 §6.2) concerns nonclassicality. Its
     nearest instance is Q-A Lemma Q(iii), which holds "Under P1 and P2"; apparatus-1 §3.1
     classes both as "new physical posits about control, access and resources", and by
     M-INACC-1 §9 the lemma "covers present active functionals only". The one test on a
     state-dependent rule (M-INACC-1, the ring `G_σ`) is negative, for that rule.
   - *The posed question on tunability* [R]. Q-B (apparatus-1 §5.7), with a first test named in
     MECH-1 §6.5 and not run (section D, row D10).
4. **"Finite observational access implies finite underlying dynamics" is not derived anywhere
   read.** Total finiteness is a posit (Main:62, Main:726 item (ii); `papers/Substratum.md`:92;
   `papers/GR.md`:142).
5. **Exact and approximate** (section C). On the configuration-basis interface approximation is
   excluded as well: in the kernel for every nonnegativity-bounded theory on the two-state
   carrier, in the form "no dense unitary control" (`nonnegBounded_not_denseUnitaryControl`,
   `permTheory_dense_ceiling`); by a short argument [W] for the monomial class with phases. The
   counting obstructions exclude exactness only. A continuously tunable flow alone is not
   sufficient for quantum mechanics (`flow_endpoint_refuted`).
6. **Openings and recommendation** (sections D, F). A mechanism survey is not supported. Two
   questions are posed on `main` and unanswered: Q-B, on tunability, and M-INACC, on
   nonclassicality. The recommendation is to hold Step 2 on one owner decision (F.1).
7. **One citation on `main` rests on a vacuous hypothesis** (Main:590,
   `readWriteSourced_not_qm`; recorded in Issue #1188; section F, finding 1).

***

## A. The conditions

### A.0 The frame the conditions are stated in

All conditions are predicates on one structure [K]:

> `structure FiniteOperationalTheory (A : Type*) [Fintype A] [DecidableEq A] where`
> `  avail : ∀ (O : Type) [Fintype O] [DecidableEq O], (O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) → Prop`
> `  availExt : ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O],`
> `    (O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) → Prop`
> (OB/OperationalAssembly.lean:594–600; the remaining fields are the closure rules, :601–653)

Availability is a proposition about an exact linear map. The structure has no metric and no
limit. The target of every equivalence is [K]:

> `def ExactAllFiniteEndomorphicQuantumOps (T : FiniteOperationalTheory A) : Prop :=`
> `  ExactFiniteEndomorphicQuantumOps T ∧ ExactCompositeQuantumOps T`
> (OB/LevelOneSeam.lean:186–187)

where the available families on the system and at every positive ancilla level are exactly the
normalized finite Kraus instruments (OB/KrausSoundness.lean:134–136; OB/AncillaClosure.lean:364–367).

### A.1 The five named conditions

Bundle [K]:

> `def PhysicalCompletionConditions (T : FiniteOperationalTheory A) : Prop :=`
> `  CompositeOperationalValidity T ∧ InertSpectatorCompositionality T`
> `    ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T`
> (OB/PhysicalCharacterization.lean:295–297)

The numbering (i)–(v) is Main:564's; the Lean bundle orders them differently.

| # | Lean definition (file:line) | Lean text, abridged to the body | Plain statement |
|---|---|---|---|
| (i) | `CompositeOperationalValidity`, OB/OperationalValidity.lean:88–93 | `T.availExt n O F → (∀ a X, X.PosSemidef → ((F a) X).PosSemidef) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace` | At every ancilla level each branch of an available family is positive and the branches preserve the trace in aggregate. |
| (ii) | `SystemToLevelOne`, OB/LevelOneSeam.lean:117–119 | `T.avail O F → T.availExt 1 O (fun a => transport (levelOneIdx A).symm (F a))` | A family available on the system is available with a one-state ancilla adjoined. |
| (iii) | `InertSpectatorCompositionality`, OB/SpectatorBridge.lean:223–229 | `T.availExt n O F → ∃ G, T.availExt m O G ∧ ∀ a, IsSpectatorExtension e (F a) (G a)` for every finite `R` and every `e : R × (A × Fin n) ≃ A × Fin m` | An available family stays available, acting identically, when a finite spectator is adjoined. |
| (iv) | `HasCompositeUnitaryControl`, OB/OperationalAssembly.lean:665–667 | `∀ (n : ℕ) (U : Matrix (A × Fin n) (A × Fin n) ℂ), Uᴴ * U = 1 → T.availExt n Unit (fun _ => conjChannel U)` | Conjugation by every unitary of every ancilla level is exactly available. |
| (v) | `IteratedAncillaClosure`, OB/AncillaClosure.lean:247–253 | `T.availExt (n * (m + 1)) O (fun a => transport (shiftIdx A n (m + 1)) (F a)) → T.availExt n O (fun a => discardWith (m + 1) (uniformAttach (m + 1)) (F a))` | Attach a fresh uniformly mixed ancilla to a composite, act, discard: the result is available on the composite. |

Condition (iv) is the only one that asks for a continuum of operations. It asks for all of
them, exactly.

### A.2 The layered forms

**OI⁺ (carrier-general)** [K]:

> `def OIPlus : Prop :=`
> `  WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T ∧ ObserverRecursion T`
> (OB/CarrierGeneralOIPlus.lean:185–186)

The qubit form adds a first conjunct `OICore T` (OB/CompletedOI.lean:418–420), with
`OICore T := RealizesSealedOICore T` (OB/CompletedOI.lean:96).

| Principle | Lean definition | Lean text (binders abridged) | Plain statement |
|---|---|---|---|
| Well-formedness | `WellFormed`, OB/GeneralCarrier.lean:125–126 | `CompositeOperationalValidity T ∧ SystemToLevelOne T` | Conditions (i) and (ii). |
| Observational independence | `ObservationalIndependence`, OB/CarrierGeneralOIPlus.lean:73 | `HasParallelReferenceExtension T` (OB/ReferenceExtension.lean:447) | Parallel extension by an untouched reference. |
| Reversible richness | `ReversibleRichness`, OB/CarrierGeneralOIPlus.lean:110–116 | `(∀ n V, T.availExt n Unit (fun _ => conjChannel V) → T.availExt n Unit (fun _ => conjChannel Vᴴ)) ∧ ∀ n, ∃ G H U, Hᴴ = H ∧ (∀ g, (U g)ᴴ * U g = 1) ∧ HControl H U ∧ (∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow H t))) ∧ (∀ g, T.availExt n Unit (fun _ => conjChannel (U g)))` | Inverses of available conjugations are available; at every level a Hermitian drift `H` has its flow `e^{-itH}` available at every real `t`, with controls whose Lie algebra with `H` contains `su(D)`. |
| Observer recursion | `ObserverRecursion`, OB/CompletedOI.lean:327–328 | `∀ n : ℕ, ∃ T' : FiniteOperationalTheory (A × Fin n), IsShiftedTheory T n T'` | Each composite level is itself the system of a finite operational theory with the transported families. |

The clause `∀ t : ℝ, … flow H t` makes continuous tunability a part of reversible richness
itself. `flow H t` is `NormedSpace.exp ((-(t : ℂ) * Complex.I) • H)` (OB/ReachabilitySeam.lean:95–96).

**Primitive-source refinement** [K]:

> `def OIPlusMin : Prop :=`
> `  ImplementationLocality T ∧ PhaseFreeRichness T ∧ EmbeddedObservation T`
> (OB/MinimalRepertoire.lean:544–545)

| Principle | Lean definition | Lean text (binders abridged) | Plain statement |
|---|---|---|---|
| Implementation locality | `ImplementationLocality`, OB/ImplementationLocality.lean:370–371 | `∃ 𝓘 : ImplementationClass, ImplementationGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘` | Availability at positive levels is exactly instrument realization (`InstAvail`, :268–290) by a class of admissible operators that is stable under an uncoupled spectator and under relabelling. |
| Phase-free richness | `PhaseFreeRichness`, OB/MinimalRepertoire.lean:423–428 | `∀ n, 2 ≤ Fintype.card (A × Fin n) → (∃ a b, a ≠ b ∧ ∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow (transition a b) t))) ∧ (∀ a b, a ≠ b → T.availExt n Unit (fun _ => conjChannel (permMatrix (Equiv.swap a b))))` | At every level with two or more states, one pair is driven at every real time, and every exchange is available. |
| Embedded observation | `EmbeddedObservation`, OB/EmbeddedObservation.lean:123–124 | `∃ 𝒯 : TheoryFamily, RegroupingInvariant 𝒯 ∧ RelabellingInvariant 𝒯 ∧ IsAmbientMember T 𝒯` | `T` is the member at its carrier of a family of theories on all finite carriers, invariant under regrouping a composite as a system and under relabelling. |

`transition a b` is `Matrix.single a b 1 + Matrix.single b a 1` (OB/LieRankSource.lean:199). The
pair `a, b` ranges over the states of `A × Fin n`, so at a positive level it is a pair of joint
system–ancilla states.

**Substratum-source form** [K]:

> `structure StructurallyClosed (𝓘 : ImplementationClass) : Prop where`
> `  arch : Architecture 𝓘`
> `  context : ContextStable 𝓘`
> `  label : LabelInvariant 𝓘`
> `  dagger : DaggerStable 𝓘`
> (OB/StructuralClosure.lean:183–187)
>
> `def DrivesElementary (𝓘 : ImplementationClass) : Prop :=`
> `  (∀ (S : Type) [Fintype S] [DecidableEq S] (a b : S) (t : ℝ), 𝓘 S (flow (transition a b) t))`
> `  ∧ (∀ (S : Type) [Fintype S] [DecidableEq S] (a b : S), 𝓘 S (permMatrix (Equiv.swap a b)))`
> `  ∧ (∀ (S : Type) [Fintype S] [DecidableEq S] (a : S), 𝓘 S (phaseGate a))`
> (OB/SubstratumSource.lean:77–82)

`Architecture` is closure under identity, product, scalar of modulus at most one, ancilla
projector and ancilla block (OB/ImplementationLocality.lean:506–515). The class the form starts
from is a definition:

> `def substratumClass : ImplementationClass := fun _ _ _ K => IsMonomial K`
> (OB/StructuralClosure.lean:180)
>
> `def IsMonomial (K : Matrix S S ℂ) : Prop :=`
> `  ∃ (σ : Equiv.Perm S) (d : S → ℂ), K = permMatrix σ * Matrix.diagonal d`
> (OB/SubstratumInterface.lean:75–76)

**Closure form** [K]: the consequence closure

> `def DerivedOI (T : FiniteOperationalTheory A) : Prop :=`
> `  ReversibleImplementationLocality T ∧ EmbeddedObservation T`
> `    ∧ ExchangesAvailable T ∧ PhasesAvailable T ∧ ReadWriteAvailable T`
> (OB/RouteB.lean:146–148)

and one continuous resource

> `def LayerFlowExecutable (T : FiniteOperationalTheory S) (σ : Equiv.Perm S) : Prop :=`
> `  ∀ (n : ℕ) (t : ℝ), T.availExt n Unit (fun _ => conjChannel (gateFlow (levelPerm σ n) t))`
> (OB/LiftAudit.lean:112–113)

The doc comment of `DerivedOI` states: "The phases conjunct is stipulated, not derived from the
stated access" (OB/RouteB.lean:144–145).

### A.3 Status of each condition relative to OI on `main`

Two different kernel objects are both called OI in prose, and the status differs between them.

- **The sealed core**: `RealizesSealedOICore T` (OB/OIRealization.lean:234–242), the predicate
  that one fixed process on eight configurations (`Fintype.card Core = 8`,
  OB/OIRealization.lean:292) with C1–C4 is realized in `T` at ancilla level four. This is what
  "bare OI" and "OI alone" mean in `oi_alone_not_qm` and in the independence theorems.
- **The substratum architecture**: the monomial class `substratumClass`, and the class the
  stated read/write access sources, `permClass` (scaled partial permutations,
  OB/SubstratumInterfaceAudit.lean:231–236), with the observer theory
  `obsTheory 𝒮 := permTheory 𝒮.Conf` (:770–771).

The module header of OB/ManuscriptAxioms.lean states the limit of both: "A
`FiniteOperationalTheory (Fin 2)` has no distinguished underlying substratum … no
manuscript-level conjunct of A1–A6 is presently a faithful predicate of the bare theory", and
"The kernel has no map from a substratum to an implementation class".

| Condition | Relative to the sealed core | Relative to the substratum architecture |
|---|---|---|
| (i) validity | Not entailed: first witness of `main_result` (OB/GeneralCarrier.lean:192–195) [K] | Derived for every implementation-local theory: `validity_of_implementationLocality` (OB/ImplementationLocality.lean:971) [K]. Holds for the observer theory through `obs_reversibleImplementationLocality` (OB/SubstratumInterfaceAudit.lean:824) and `implementationLocality_of_reversible` (OB/MicroscopicReversibility.lean:227) [K; the composition is the writer's reading]. |
| (ii) trivial-ancilla consistency | Not entailed: fifth witness of `main_result` (:208–211) [K] | Derived from embedded observation: `systemToLevelOne_of_embeddedObservation` (OB/EmbeddedObservation.lean:223); `obs_embeddedObservation` (OB/SubstratumInterfaceAudit.lean:820) [K]. |
| (iii) inert spectators | Not entailed: second witness (:196–199); `independence_independent` (OB/CompletedOI.lean:475) [K] | Derived: `observationalIndependence_of_implementationLocality` (OB/ImplementationLocality.lean:957) with `observationalIndependence_iff_inert` (OB/CarrierGeneralOIPlus.lean:75) [K]. |
| (iv) full reversible control | Not entailed: `control_independent` (OB/DiagonalTheory.lean:398–404), `oi_alone_not_qm` [K] | **Proved not supplied**: `substratumGen_not_control` (OB/StructuralClosure.lean:348), `obs_not_control` (OB/SubstratumInterfaceAudit.lean:856), `configurationLevel_not_qm` (OB/ManuscriptAxioms.lean:175) [K]. See section B. |
| (v) iterated composition | Not entailed: fourth witness (:204–207); `recursion_independent` (OB/CompletedOI.lean:496) [K] | Derived from embedded observation: `closure_of_embeddedObservation` (OB/EmbeddedObservation.lean:211) [K]. |

For the layered forms:

| Principle | Status | Witness |
|---|---|---|
| Observational independence | supplied by the architecture (as (iii)) | as above |
| Observer recursion | supplied by the architecture | `observerRecursion_of_embeddedObservation` (OB/EmbeddedObservation.lean:217) [K] |
| Reversible richness, inverse clause | derived from the Lie-rank clause on a well-formed theory | `inverseAccessibility_of_lieRank` (OB/MicroscopicReversibility.lean:132) [K] |
| Reversible richness, Lie-rank clause (`∀ t : ℝ` flow) | assumed; proved not supplied | `richness_independent` (OB/CompletedOI.lean:487); for the architecture, through (iv) [K] |
| Implementation locality | supplied | `obs_reversibleImplementationLocality` [K] |
| Embedded observation | supplied | `obs_embeddedObservation` [K] |
| Phase-free richness, exchanges | supplied | `obs_exchangesAvailable` (OB/SubstratumInterfaceAudit.lean:816) [K] |
| Phase-free richness, one pair driven at every real time | **proved not supplied** | `obs_not_phaseFree` (OB/SubstratumInterfaceAudit.lean:859); `configurationLevel_not_phaseFree` (OB/ManuscriptAxioms.lean:169, two-state carrier, label-invariant class) [K] |
| Structural closure (four clauses) | theorems of the monomial class | `substratumClass_structurallyClosed` (OB/StructuralClosure.lean:316) [K] |
| Elementary drivability, exchanges | supplied | `exchange_monomial` (OB/SubstratumInterface.lean:98) [K] |
| Elementary drivability, quarter phases | in the monomial class by the interface's definition (`phase_monomial`, OB/SubstratumInterface.lean:102); **not sourced by the read/write access** (`obs_not_phasesAvailable`, OB/SubstratumInterfaceAudit.lean:846). Main:590 words this as "a stated intervention principle". | [K] |
| Elementary drivability, flows of every pair at every real time | **proved not supplied** | `substratumClass_not_drivesElementary` (OB/StructuralClosure.lean:370) [K] |

For the observer theory the kernel compresses this to one statement [K]:

> `theorem obs_qm_iff_phaseFree :`
> `    ExactAllFiniteEndomorphicQuantumOps (obsTheory 𝒮) ↔ PhaseFreeRichness (obsTheory 𝒮)`
> (OB/SubstratumInterfaceAudit.lean:866–868)

together with `obs_not_phaseFree` (:859) and `obs_exchangesAvailable` (:816). What is missing
there is the first clause of phase-free richness, and the phases if the route through
`DerivedOI` is taken.

How these are proved matters for what is missing. `obs_not_control`, `obs_not_phaseFree` and
`obs_not_qm` are `permTheory_not_control`, `permTheory_not_phaseFree` and `permTheory_not_qm`
(OB/SubstratumInterfaceAudit.lean:708, :712, :717). All three reduce to
`permTheory_not_phasesAvailable` (:670): control would supply the quarter phase, and the quarter
phase does not preserve nonnegative entries. These proofs do not mention diagonal preservation or
`rot`. `obs_not_layerFlowExecutable` uses diagonal preservation, by containment in the substratum
theory. On the sourced theory two resources are therefore missing for two different reasons, and
supplying one does not supply the other:

> `theorem flow_endpoint_refuted :`
> `    ∃ T : FiniteOperationalTheory (Fin 2),`
> `      SourcedOI T ∧ LayerFlowExecutable T (Equiv.swap 0 1) ∧ ¬ PhaseFreeRichness T`
> (OB/FlowEndpoint.lean:149–151; witness `onesTheory (Fin 2)`; `onesTheory_not_qm`, :208) [K]

`SourcedOI` is `DerivedOI` without the phases (OB/SubstratumInterfaceAudit.lean:619). The witness
executes the gate flow of every layer involution at every real time and every level
(`onesTheory_layerFlowExecutable`, :89) and is not quantum mechanics. Exact continuous tunability
of a state-mixing family is necessary for the target and not sufficient. Conversely `realClass`
has `rot` and lacks the phases (`realTheory_rot`, `realTheory_not_phases`,
OB/F2CoherenceControls.lean:306, :317) [K].

### A.4 Each equivalence, one direction at a time (§A.34)

| Equivalence | QM ⇒ conditions | conditions ⇒ QM | Note |
|---|---|---|---|
| five conditions | `physical_of_exactAll` (OB/PhysicalCharacterization.lean:301) | `exactAll_of_physical_general` (OB/GeneralCarrier.lean:93) | Combined as `exactAll_iff_physical_general` (:100), under `[Nonempty A]` (:74). Both directions witnessed. The proof bodies of the sufficiency chain were not read. |
| OI⁺ | `oiPlus_of_qm` (OB/CarrierGeneralOIPlus.lean:198) | `qm_of_oiPlus` (:191) | Both witnessed. |
| observational independence ⇔ (iii) | one `Iff` | one `Iff` | `observationalIndependence_iff_inert` (:75) is `(inertSpectator_iff_parallelReferenceExtension T).symm` (OB/SpectatorBridge.lean:233). Only the opening of that proof was read. |
| reversible richness ⇔ (iv) | (iv) ⇒ richness needs `WellFormed T` and `[Nonempty A]`: `reversibleRichness_of_control` (:148) | `control_of_reversibleRichness` (:127) | Main:586 states the side conditions. |
| observer recursion ⇔ (v) | (v) ⇒ recursion needs the identity and the relative readout at every level: `observerRecursion_of_closure` (OB/CompletedOI.lean:392) | `closure_of_observerRecursion` (:332) | Main:586 states the side conditions. |
| primitive-source form | `oiPlusMin_of_qm` (OB/MinimalRepertoire.lean:562) | `qm_of_oiPlusMin` (:552) | Both witnessed. |
| closure form | `layerFlowExecutable_of_control` (OB/LiftAudit.lean:117) | `qm_of_derivedOI_layerFlowExecutable` (OB/DerivedQ3.lean:214) | `derivedOI_qm_iff_layerFlowExecutable'` (:222–227), under the hypothesis `DerivedOI T`, which contains the stipulated phases. |
| substratum-source form | `qm_generated_by_substratum_extension` (OB/StructuralClosure.lean:423–429) | `substratum_plus_control_qm` (:414–417) | **Qualified.** There is no single biconditional. The two statements have different shapes: one concerns `genTheory 𝓘 hc.arch A` for a class with `StructurallyClosed 𝓘` and `DrivesElementary 𝓘`; the other produces, for a quantum `T`, a class generating `T`. The class produced is `fullClass`, every operator admissible (OB/ImplementationLocality.lean:374). In the forward statement the hypothesis `ExtendsSubstratum 𝓘` is bound to `_` and unused. See section F, finding 2. |

No displayed equivalence was found with a direction lacking a witness. The last row is the one
whose prose form says more than the pair of theorems (finding 2).

***

## B. The obstruction theorems

The owner's three classes, verbatim:

1. "Finite state representation: Does the impossibility follow because the observer has finitely many distinguishable states?"
2. "Restricted dynamics: Does it follow because OI permits only particular transformations, such as discrete permutations or read-write shuffles?"
3. "Restricted observational access: Could continuous mixing exist in the deterministic substratum but remain only partially accessible to embedded observers?"

For each obstruction the last lines answer: does it (a) assume the underlying system finite,
(b) assume only the observer's accessible states finite, or (c) say nothing that distinguishes
the two.

### B.0 Where finiteness comes from on `main`

- Lemma 1 is about the observer: "The observer has finitely many distinguishable internal
  states, so the visible configuration space $\mathcal{C}_V$ is finite" (Main:48) [P]. Its
  kernel form is conditional on a premise of finitely many boundary modes, each with finitely
  many settings (OB/Finiteness.lean, header and `finiteness` at :153) [K].
- Total finiteness is a posit: "only finite visible resolution is a theorem (Lemma 1) … total
  finiteness of that representative is a physical posit" (Main:62); "Finiteness of the hidden
  sector is posited in the forward construction … it is not derived from Lemma 1" (Main:702);
  ledger item (ii), "finiteness of the *total* state space $S$ — Lemma 1 delivers finiteness of
  the observer's distinguishable states, and the extension to all of $S$ is A1 of the companion
  substratum construction" (Main:726) [P].
- The Substratum paper scopes A1: the entropy bound "alone does not establish finiteness of
  every underlying sector … Infinite extensions require specified normalized measures or states
  and well-defined dynamics; the finite identity does not supply that construction"
  (`papers/Substratum.md`:92), and "alternative would be an effective-finiteness argument with
  continuum UV completion, which the framework does not develop" (:216) [P].

So the step from finite observational access to a finite underlying system is made by posit.
No statement read derives it. The exact invariance that supports the posit covers finite
decoupled enlargements only (Main:726 item (ii)).

### B.1 `substratumGen_not_control` and the configuration-level family [K]

> `theorem substratumGen_not_control :`
> `    ¬ HasCompositeUnitaryControl (genTheory substratumClass substratumClass_arch (Fin 2))`
> (OB/StructuralClosure.lean:348–349)

**Proof, as read** (:350–356). Control at level 1 makes `conjChannel rot` available. In a
generated theory availability is `InstAvail`; by `realized_of_instAvail`
(OB/ImplementationLocality.lean:530) the map is a finite sum of conjugations by admissible
operators, here monomials. A monomial conjugation preserves diagonal matrices
(`preservesDiag_conj_of_monomial`, OB/SubstratumInterface.lean:126), sums preserve the property
(`preservesDiag_sum`, OB/DiagonalTheory.lean:84), and `conjChannel rot` does not
(`rot_not_preservesDiag`, OB/DiagonalTheory.lean:381: the image of `|0⟩⟨0|` has off-diagonal
entry `−12/25`).

**Same invariant, other statements** [K]: `configurationLevel_not_qm`
(OB/ManuscriptAxioms.lean:175) for every class of monomials on the two-state carrier;
`substratumTheory_not_layerFlowExecutable` (OB/LiftAudit.lean:200) on every finite carrier with
a permutation that moves a configuration, witnessed by the gate flow at time one half
(`configurationLevel_not_avail_gateFlow_half`, OB/ExecSource.lean:97); `coherentLiftClass_eq_substratumClass`
(OB/LiftSource.lean:164) and `stochastic_not_layerFlowExecutable` (:262) for the coherent lifts
and for classical stochastic channels in monomial Kraus form.

**Hypotheses and definitional restrictions the proof uses.**

1. *Kinematics.* States and operations are complex matrices indexed by the carrier and its
   ancilla extensions (A.0).
2. *The interface.* A substratum bijection `σ` of a state set `S` is represented by
   `permMatrix σ` on matrices indexed by that same `S`, and a phase by a diagonal matrix:
   `def bijectiveOperator (σ : Equiv.Perm S) : Matrix S S ℂ := permMatrix σ`,
   `def phaseOperator (d : S → ℂ) : Matrix S S ℂ := Matrix.diagonal d`
   (OB/SubstratumInterface.lean:80, 83). These are definitions. No theorem derives them from a
   substratum; the configuration basis is the matrix basis by construction. This agrees with
   the map used in Main's `D ⇒ Q_fb` step, `U_φ|x,h⟩ = |φ(x,h)⟩` with a diagonal initial law
   (Main:554).
3. *The class.* "The substratum's interventions" means `IsMonomial`: a permutation times an
   arbitrary complex diagonal. It is the largest configuration-level class
   (`configurationLevel_iff_le_substratum`, OB/ManuscriptAxioms.lean:134).
4. *"Generated by".* `InstAvail` (OB/ImplementationLocality.lean:268–290): one admissible
   isometric step; readout by admissible projectors of a register; classical coarse-graining;
   sequential composition with outcome-dependent continuation; discard of a uniformly mixed
   ancilla of any positive size. Derivations are finite. No limit, closure or completion is
   taken. The only preparation assumed is the uniformly mixed ancilla
   (`prepAvail_uniform`, OB/OperationalAssembly.lean:630), so every discarded sector starts in a
   state that is diagonal and independent of the input.
5. *Carrier.* The statement is on `Fin 2`, tested at ancilla level 1. The proof uses the two
   states only to write down `rot`.
6. *Exactness.* What is refuted is the exact availability of one operator.

**Sorting.**

- *Class 1.* Not the operative cause. Two separate facts:
  - *The invariant is cardinality-free.* An operator with at most one nonzero entry in each row
    and column conjugates diagonals to diagonals; nothing is counted.
  - *The kernel proof has one cardinality step.* `substratumGen_not_control` calls
    `realized_of_instAvail substratumClass_arch`, and four of the five closure clauses of
    `substratumClass_arch` (OB/StructuralClosure.lean:231–238) go through `submonomial_monomial`
    (:130–167), which extends a partial injection to a permutation by matching complements of
    equal `Fintype.card` (:148–149). The step sits in the form of the class ("permutation times
    diagonal"), not in the invariant. The nonnegativity route does not have it: `permClass` is
    defined by `IsSubmonomial` and `permClass_arch` (OB/SubstratumInterfaceAudit.lean:350–355)
    does not call `submonomial_monomial`.
  - *Whose finiteness.* `[Fintype A]` and `Fin n` make the carrier and every ancilla finite by
    type. In a generated theory on `Fin 2` that is the observer carrier with a hidden ancilla of
    arbitrary finite size; in `obsTheory` the carrier is the whole configuration space (B.5).
    The kernel cannot express "finite observer, infinite substratum".
- *Class 2.* The operative cause, in the precise form of items 2–3.
- *Class 3.* Present in a restricted form: `InstAvail.discard` marginalizes over a hidden
  ancilla that is uniformly mixed, finite and independent of the input. It yields no mixing.
  Not modelled: a hidden sector correlated with the input, a carrier that is a quotient and not
  a tensor factor, limits.
- *Outside the three classes.* Item 2, the identification of the matrix basis with the
  configuration labels.

**Finiteness: (c)**, with a hidden ancilla of arbitrary finite size. The inference "finite access
implies finite underlying dynamics" is not used.

[W] On an infinite index set the two forms of the class separate: a block of a
permutation matrix can be a non-surjective partial injection (a shift), which is not a
permutation times a diagonal. The cardinality-free statement is for weighted partial injections,
not for "a permutation of any index set". On an infinite carrier injective and bijective dynamics
differ; Main:62 uses "on a finite set, injectivity implies surjectivity". Not a theorem on `main`.

### B.2 `readWriteSourced_not_qm` [K, with a vacuous hypothesis]

> `def ReadWriteSourced (T : FiniteOperationalTheory A) : Prop :=`
> `  ∀ (n : ℕ) (V : Matrix (A × Fin n) (A × Fin n) ℂ),`
> `    T.availExt n Unit (fun _ => conjChannel V) → ∃ σ : Equiv.Perm (A × Fin n), V = permMatrix σ`
> (OB/ReadWriteControl.lean:158–160)
>
> `theorem readWriteSourced_not_qm (T : FiniteOperationalTheory (Fin 2))`
> `    (h : ReadWriteSourced T) : ¬ ExactAllFiniteEndomorphicQuantumOps T`
> (:174–176)

**Proof, as read.** `ReadWriteSourced` gives `MonomialSource` (:162–166); control would make
`rot` monomial; `rot` has two nonzero entries in its first row (`rot_not_monomial`,
OB/SubstratumInterface.lean:155).

**The hypothesis is unsatisfiable** [W]. (1) `conjChannel (lam • V) = conjChannel V` for
`‖lam‖ = 1` (`conjChannel_smul`, OB/ReachabilitySeam.lean:272) [K]. So if
`fun _ => conjChannel V` is available then so is `fun _ => conjChannel (−V)`, being the same
function, and the hypothesis would make both `V` and `−V` permutation matrices, which is
impossible on a nonempty carrier since `permMatrix` has entries in `{0, 1}`
(OB/CoherentLift.lean:92–93). (2) Every finite operational theory has a one-outcome conjugation
available at level 1: `readout_avail 1` with `availExt_coarse` to `Unit` gives the family
`fun _ => readout 1 0`, and `readout 1 0 = localLuders 0` (`readout_is_localLuders`,
OB/OperationalAssembly.lean:658) is the identity on `A × Fin 1`, which is `conjChannel 1`. Hence
no theory on a nonempty carrier satisfies `ReadWriteSourced`. This derivation was not
kernel-checked. The vacuity is already recorded on `main` in unreviewed research records:
"the vacuity of `ReadWriteSourced`, which requires an available `V` to equal `permMatrix σ`
exactly although `id = conjChannel(i·1)`"
(`verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`:864–866)
and "The vacuous `ReadWriteSourced` family (#1188) is not cited"
(`…/minacc-1-20261108/DESIGN.md`:585–586) [R].

**Non-vacuous statements with the intended content** [K]: `monomialSource_not_qm`
(OB/SubstratumInterface.lean:192); `permTheory_not_qm` and `obs_not_qm`
(OB/SubstratumInterfaceAudit.lean:717, 862), where `permClass` admits a common scalar;
`bijectionLevel_not_layerFlowExecutable` (OB/ExecSource.lean:89). They use the nonnegativity invariant for `permTheory` and `obsTheory` and monomiality or diagonal preservation for the others (B.5, A.3).

**What "read-write" means as defined.**

> `structure ReadWriteFamily (a b : S) where`
> `  couple : ℝ → Equiv.Perm S`
> `  reference : couple 0 = 1`
> `  local_support : ∀ (l : ℝ) (x : S), x ≠ a → x ≠ b → couple l x = x`
> (OB/ReadWriteControl.lean:86–89)

A real-parameter family of bijections of one finite set that moves at most the pair `{a, b}`.
No continuity is assumed. There is no visible/hidden partition, no memory and no readback in
the structure. The "hidden-memory and readback" countercontrol is `memorySwap`, the family
`if l = 0 then 1 else Equiv.swap a b` (:188–196).

**A finiteness statement in this neighbourhood** [K]:
`readWriteOperator_range_finite` (OB/CoherentContinuumSource.lean:292): the operators of a
read-write family form a finite set, because `Equiv.Perm S` is finite. This one is class 1,
and the finite set is the set the bijections act on, which in the observer theory is the
configuration space with an ancilla. [W] On an infinite state set a real-parameter family of
bijections need not have finite range.

**Sorting.** Class 2 as a hypothesis on the theory (and vacuous as stated). Class 1 only in
`readWriteOperator_range_finite`, where it is the underlying set that is finite: **(a)** for
that statement, **(c)** for the rest. Class 3: not used.

### B.3 `oi_alone_not_qm` [K]

> `theorem oi_alone_not_qm :`
> `    ∃ T : FiniteOperationalTheory (Fin 2),`
> `      RealizesSealedOICore T ∧ ¬ ExactAllFiniteEndomorphicQuantumOps T`
> (OB/GeneralCarrier.lean:160–163; witness `diagTheory`)

**Proof, as read.** `diagTheory` (OB/DiagonalTheory.lean:246–248) declares available exactly
the Kraus families (CP instruments at ancilla levels) all of whose branches preserve diagonal
matrices. It realizes the sealed core (`diag_realizesSealedOICore`, :358) and lacks control
because `rot` does not preserve the diagonal (`diag_not_control`, :390).

**What the proof uses.** (1) "OI" is the sealed-core predicate: one fixed eight-configuration
process realized at level four. (2) The witness is a theory chosen for the purpose; its
restriction to diagonal-preserving maps is a property of the countermodel. (3) The carrier is
the qubit.

**Logical type.** A non-entailment by countermodel: the predicate does not imply control. It
does not show that a physical OI substratum cannot supply control, and it does not quantify
over substrata. The section note that precedes `qm_implies_oiCore` makes the same point from the other
side: the core "is an existential realizability condition" (OB/CompletedOI.lean:533–534).

**Sorting.** Class 1: the core is a finite total system by definition, but that is not what
blocks control. Class 2: present as the countermodel's definition, not derived from OI.
Class 3: not used. **Finiteness: (a)** for the core (a finite total system, visible and hidden
both finite), immaterial to the conclusion.

### B.4 `oiPlus_independence` [K]

> `theorem oiPlus_independence :`
> `    (∃ T, OICore T ∧ WellFormed T ∧ ReversibleRichness T ∧ ObserverRecursion T ∧ ¬ ObservationalIndependence T)`
> `    ∧ (∃ T, OICore T ∧ WellFormed T ∧ ObservationalIndependence T ∧ ObserverRecursion T ∧ ¬ ReversibleRichness T)`
> `    ∧ (∃ T, OICore T ∧ WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T ∧ ¬ ObserverRecursion T)`
> (OB/CompletedOI.lean:506–513, `T : FiniteOperationalTheory (Fin 2)`, abridged)

Witnesses (:475–503): the round-34 `countermodel` (2-positive, not completely positive);
`diagTheory`; the rank-gap theory `gapTheory`. Only the second concerns mixing, and its
analysis is B.3's.

**Bearing on "recursive structure".** `richness_independent` (:487–493) exhibits a theory with
the core, well-formedness, observational independence and observer recursion, and without
reversible richness. So the kernel's recursion and independence principles coexist with the
absence of mixing. The same holds for the observer theory, which has embedded observation
(`obs_embeddedObservation`) and no phase-free richness (`obs_not_phaseFree`). Recursion
transports control between levels (`descend`, OB/MinimalRepertoire.lean:512, from level
`n·(m+1)` to level `n`) and does not create it at any level. This is a statement about the
formalized notions (`ObserverRecursion`, `EmbeddedObservation`, `IteratedAncillaClosure`), not
about every recursive structure a substratum might have.

**Sorting and finiteness.** As B.3.

### B.5 The observer theory of a substratum [K]

> `variable (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]`
> `noncomputable abbrev obsTheory : FiniteOperationalTheory 𝒮.Conf := permTheory 𝒮.Conf`
> (OB/SubstratumInterfaceAudit.lean:766, 770–771)
>
> `theorem obs_not_layerFlowExecutable {g : Equiv.Perm 𝒮.Conf} {x : 𝒮.Conf} (hx : g x ≠ x) :`
> `    ¬ LayerFlowExecutable (obsTheory 𝒮) g`
> (OB/ExecSource.lean:129–130)

**Proof, as read** (:131–134): the observer theory's availability is contained in the
substratum theory's (`obs_availExt_le_substratum`, OB/SubstratumInterfaceAudit.lean:837), which
executes no layer flow by B.1.

**What the definitions fix.**

1. The carrier of the observer theory is `𝒮.Conf = 𝒮.ι → 𝒮.V × 𝒮.V`, the substratum's whole
   configuration space (:78). There is no visible/hidden partition in `obsTheory`. The observer
   is granted every exchange of two configurations at every level.
2. Finiteness of sites and alphabet is an instance hypothesis, "under the finiteness A1
   supplies" (:768–769).
3. The rule does not enter: `obsTheory_rule_independent` (:780–782), "Configuration-level
   sourcing consumes nothing of A3–A6." Whatever recursive or local structure the dynamics has,
   this obstruction does not see it.
4. The write access generates `permClass`, "the least architecture containing the exchanges"
   (module header; `permClass_le_of_exchanges`, :464). That choice of class is a convention of
   the sourcing, not a theorem about which operations are physical.

**Sorting.** Class 2: operative, through two invariants. Nonnegativity carries `obs_not_control`,
`obs_not_qm`, `obs_not_phaseFree` and all of `FrozenSourcing` (by way of the phases, A.3);
diagonal preservation carries `obs_not_layerFlowExecutable`. Class 1: at the type level only, and
there it is **(a)**, the underlying configuration space, that is taken finite. Class 3: the
carrier is everything, so no visible/hidden split is inside `obsTheory`; the only marginalization
is the discard of an ancilla outside the substratum (B.1). The module headers state what is not
claimed: "anything about a richer observer architecture than the stated one" (OB/ExecSource.lean,
OB/LiftSource.lean) and "the site-space wave-operator formulation" (Main:590: "unresolved rather
than excluded").

### B.6 The counting obstruction [K]

> `theorem countable_not_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘)`
> `    {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x)`
> `    (D : Set (Matrix (S × Fin 1) (S × Fin 1) ℂ)) (hD : D.Countable)`
> `    (hmem : ∀ K, 𝓘 (S × Fin 1) K → ∃ (c : ℂ) (M : Matrix (S × Fin 1) (S × Fin 1) ℂ), M ∈ D ∧ K = c • M) :`
> `    ¬ LayerFlowExecutable (genTheory 𝓘 arch S) σ`
> (OB/PolarizationClosure.lean:87–92; abridged: the type ascription of `K` is dropped)

with `uncountableNonMonomialRays_of_qm` (OB/CoherentContinuumSource.lean:195),
`mixTheoryR_not_qm` for a mixing datum restricted to countably many angles
(OB/StateMixingCoupling.lean:679) and `fixedGateTheory_not_qm` (OB/DiscreteCompletion.lean:1948).

**Proof route** (the opening of the proof and the header were read): the flow takes pairwise
non-proportional values at distinct times in `[0, 2)`, so executing it would place uncountably
many rays in a countable set.

**Sorting.** A cardinality restriction on the set of admissible operators at level one: class 2
in the owner's wording ("only particular transformations"), by counting. It follows from a
finite state set only for bijection-level classes. It is not what blocks the monomial class,
which is not countably covered because of its diagonal weights
(`substratumClass_not_countablyCovered`, OB/CoherentContinuumSource.lean:235); the header calls
the two failures "orthogonal". **Finiteness: (c).** It excludes exactness only (section C).

### B.7 "No fixed finite realization of one qubit exactly" [P, P-imp]

> "*Proposition (finite-substratum operational obstruction — classical-dimension form).* Fix
> one realization: a substratum of $N < \infty$ ontic configurations with its observation map.
> Its full prepare-and-measure behavior factors as $B = \Xi M$ … for every $N$ there is a finite
> qubit experiment no $N$-state model reproduces exactly (Heinosaari–Kerppo–Leppäjärvi–Plávala
> [55] …) … the elementary factorization half proved here, the unboundedness imported. The
> obstruction is independent of C1–C4 and of horizon growth." (Main:560)

**Witness.** No Lean statement was found (a search of `OIBridge/` for nonnegative rank returns
nothing relevant). Paper level, with the unbounded-nonnegative-rank half imported from [55].
The factorization half and the SIC-embedding remark are checked exactly by
`papers/oi_lattice_code/foundations/nogo_probes.py` according to Main:562; the probe was not
run or read here. No row for this Proposition was found in `verification/coverage/LEDGER.json`
by a search for its label.

**Hypotheses.** (1) One fixed realization. (2) `N < ∞` ontic configurations. (3) The interface
"preparation → finite ontic system → measurement": preparations are arbitrary distributions
over the `N` states, effects arbitrary response functions. (4) Exact reproduction of the whole
continuum of qubit preparations and effects. No restriction on dynamics enters.

**Sorting.** Class 1, purely. Class 2: not used ("independent of C1–C4"). Class 3: not a
hypothesis, and no restriction of access removes the obstruction: "every behavior matrix the
realization generates has nonnegative factorization through $N$ states", so the behaviours of
any sub-collection of preparations and effects factor as well [W, one line from the quoted
sentence]. This is the paper-level statement that restricted access on a finite substratum does
not give exact reproduction of one qubit's full theory.
**Finiteness: (a).** It is the number of ontic configurations of the whole realization that is
finite. Lemma 1 does not supply this; the total-finiteness posit does. The inference "finite
access implies finite underlying" is therefore consumed here as a posit.

### B.8 "No uniform finite realization" [P]

> "A fixed finite $S$ with a fixed prior and a fixed bijection supports only finitely many
> distinct action-labelled conditional families, whereas the instrument space of any
> non-trivial system is a continuum." (Main:488)

A counting argument at paper level. Hypotheses: fixed finite `S`, fixed prior, fixed
bijection. **Sorting:** class 1. **Finiteness: (a).** Exactness only.

### B.9 The trace-out lemma [P]

> "**Lemma (diagonal preservation).** *The channels
> $\Phi_t(\rho) = \mathrm{Tr}_H[\,U^t(\rho \otimes \mu_H)\,U^{-t}]$ with $U$ a permutation
> unitary map computational-diagonal states to computational-diagonal states.*" (Main:328; proof
> at Main:330)

This is the one statement read on `main` that has the visible/hidden split inside it. It is the
paper-level form of B.1 with restricted access. Hypotheses: the configuration-basis embedding of
Main:268; a permutation unitary; a hidden state `μ_H` that is fixed and in product with the
input; `C_H` finite "under the total-finiteness posit" (Main:268). The two-line proof does not
use finiteness [W]. Main:336 states the scope: "the framework's channels are in that class".
**Sorting:** class 2 with a product prior; class 3 is present in the setting and does not
produce mixing under these hypotheses. **Finiteness:** the setting is **(a)**; the proof is
indifferent.

### B.10 Off-`main` context [D]

`origin/research/intervene-1-20261111` (head `ea12fde1`, PR #1230),
`verification/programmes/oi-qm/reconstruction/drafts/intervene-1-20261111/INTERVENE-UNIT1.md`,
draft r2 "pending re-review", states: under P-CONF (a finite configuration set, a bijection,
states are probability laws), H4 (the observer and its records are configuration coordinates)
and H-IND (the law of everything outside the identified carrier, given the carrier's
configuration, is fixed by the procedure), every procedure induces a nonnegative kernel on the
carrier's laws (its T0), and every linear lift preserves diagonal states (its T2). It leaves
undecided the routes with memory outside the identified carrier and with nonlinear register
encodings. It is unreviewed on `main` and is used below only to name routes.

### B.11 Summary

| Obstruction | Layer | Class 1 | Class 2 | Class 3 | Finiteness | "Finite access ⇒ finite underlying" used? |
|---|---|---|---|---|---|---|
| B.1 `substratumGen_not_control`, configuration-level family | K | type-level for carrier and ancilla; one cardinality step in the class closure, none in the invariant | **operative** (diagonal preservation) | restricted form: discard of a uniformly mixed, input-independent finite ancilla; no mixing | (c); hidden ancilla of arbitrary finite size | no |
| B.2 `readWriteSourced_not_qm` | K, vacuous hypothesis | only in `readWriteOperator_range_finite` | as hypothesis | not used | (c); (a) for the range statement | no |
| B.3 `oi_alone_not_qm` | K | definition of the core | countermodel's definition | not used | (a), immaterial | no |
| B.4 `oiPlus_independence` | K | as B.3 | as B.3 | not used | (a), immaterial | no |
| B.5 `obs_not_layerFlowExecutable`; `obs_not_control`, `obs_not_qm`, `obs_not_phaseFree` | K | type-level (A1 instance) | **operative**: diagonal preservation for the first, nonnegativity (through the phases) for the other three | carrier is the whole configuration space; ancilla discard only | (a) at type level | assumed as A1, not needed by the invariants [W] |
| B.6 counting (`countable_not_layerFlowExecutable`) | K | no | **operative**, by cardinality of the operator class | not used | (c) | no |
| B.7 Main:560 Proposition | P, P-imp | **operative** | not used | not a hypothesis; holds under every restriction of access [W] | (a) | **yes, as the posit** |
| B.8 Main:488 Proposition | P | **operative** | fixed prior and bijection | not used | (a) | **yes, as the posit** |
| B.9 Main:328 Lemma | P | setting only | **operative**, with product prior | present, yields no mixing | (a) in the setting | assumed, not needed by the argument [W] |
| `nonnegBounded_not_denseUnitaryControl`, `permTheory_dense_ceiling` (FrozenSourcing:173, :187) | K | type-level | **operative** (nonnegativity); dense unitary control excluded | not used | (c) | no |
| `nonnegClass_nonnegBounded` with `falsifierUnavailable_of_nonnegBounded` (F2CoherenceControls:173, :98) | K | type-level | **operative**, for the one class `nonnegClass` (entrywise nonnegative matrices times a contractive scalar); stochastic (coarse-grained, Koopman-compressed) operators enter as Kraus operators of realized branches | present as the form of the operators | (c) | no |
| `flow_endpoint_refuted` (countermodel) | K | type-level | a tunable flow without phases is not QM | not used | (c) | no |
| `operational-control-countercontrol.md` | R | no | **operative**: time shifts of one bijection are abelian | hidden carrier of any cardinality | none assumed | no |
| Q-A Lemma G2 | R | no | **operative**: center-free, bipartite, non-adaptive | traced-out sector included, any size | none assumed | no |
| apparatus-1 Lemma 5, C-ROT, dense control (§4.7) | R | the four-point cell of the one-cell frame R1 | **operative**, as bijections acting on laws: the encoded channel of any bijective process with fixed-law ancillas is a stochastic matrix on the four points | access posits P1, P2 in force. Lemma 5's proof uses neither (fixed-law ancillas only; "The proof uses no property of the ancilla laws"). C-ROT is derived from the isotropy they give (Lemma 4), and the `rot` image of `Z_+` is in any case not a law on the four points (§5.1) | (a) for the cell | no |
| MECH-1 Theorem W, Proposition C | R | **operative for "no infinite-order unitary"**: at a fixed odd prime `q` the Clifford group modulo phases is finite | **operative**, as bijections acting on laws: reachable laws have nonnegative Wigner functions, so every encoded unitary is Clifford; this part holds for every fixed bijection (MECH-2 node 8). The linear symmetric form with the `−x(t−1)` memory term is what makes every encoded branch completely positive (Theorem W, Proposition AS) | access posits P1, P2 in force and load-bearing for complete positivity; arming P3 supplied | (a) for the alphabet | as the posit |
| MECH-2 Lemma F, Theorem U2(ii), §6.4 | R | **operative**: finite configuration set and finite frame (posit) | **operative**, as bijections acting on laws; no restriction on which bijection | no condition on the reads; H-LIFT, fixed-law attachments and a fixed injective linear frame are the hypotheses | (a) | as the posit |
| MECH-2 Theorem NC | R | finite configuration set (posit) | as the row above | adds spanning preparations and reads; at `q = 2` the native `Z`/`X` reads do not span and the verdict is undecided there | (a) | as the posit |

### B.12 Records on `main` that model restricted access, recursive structure or an infinite hidden carrier

Status words are each record's own. "Model-reviewed" and "author-reported" reviews are not
verification (§A.46 item 7); none of the [R] rows is an established claim.

| Record | Statement and hypotheses | Layer; status on `main` | Bearing on class 3 |
|---|---|---|---|
| `InstAvail.discard` (OB/ImplementationLocality.lean:284–288); `nonnegClass` (F2CoherenceControls:120–180) | Marginalizing a uniformly mixed finite ancilla after any admissible instrument stays in the class; the theory generated by the one class `nonnegClass` (entrywise nonnegative matrices times a contractive scalar) is nonnegativity-bounded on every carrier, so lacks `rot` and the phases. A subclass needs a monotonicity step that is not a kernel theorem | K | Coarse-graining a classical hidden dynamics yields neither `rot` nor the phases on the configuration basis. The invariant is nonnegativity, not diagonal preservation: nonnegative coherences can appear. An isometric member of the class is a scaled permutation [W: orthogonal columns with nonnegative entries have disjoint supports], so stochastic operators enter as Kraus operators of realized branches |
| `RecursiveFiniteFactor` (:52, :83) | Finite-horizon and exact-period depth bounds, assuming stagewise factorization | K, conditional by statement | An aggregation step only; ANALYSIS.md:57–60 says the module "must not be described as a kernel proof of the topological lemma" |
| `NativePadicReduction` (:56, :66) | Every additive alphabet reduction commutes with the neighbour-sum two-slice step (coefficient 1) | K; the module scopes it "for passive congruence readout only" | Deeper digits never reach a fixed low-digit readout under the linear rule |
| SUBSTATE-2 `ANALYSIS.md`:14–54, models A, B1, B2, C | Topological finite-stage lemma (paper proof); A: no backflow; B1: one bit of classical memory at a chosen depth; B2: iid, no common return; C: profinite gauge links, no instrument | R; paper proofs and exact finite controls; "Quantum … claims **OPEN**" | General statement (paper lemma): continuous finite readouts of a tower see a finite stage at each horizon. The four models examined give classical memory or Markov laws; a continuous homomorphism from a profinite group to `U(1)` or `SU(2)` has finite image (:169–175) |
| FIXED-SCALE-1 `REPORT.md` | One fixed reversible rule reads unbounded depth: P-divisible two-time law, one bit of three-time memory, no common return | R; author-reported acceptance; "classical" | Finite visible alphabet with unbounded underlying depth is consistent and classical |
| NATIVE-PADIC-1 `REPORT.md` | No deep-to-low passive backflow for the integer-coefficient cubic stencil; a non-native kick breaks it | R (K for coefficient 1); narrow; "not an impossibility result for recursive … sub-states in general" | Passive congruence access to a tower adds nothing; an escape needs level-mixing or a non-congruence readout |
| F2-1 A★ §A★2, G★ (`amendments/A-star.md`:27–60, :138–188); run-2 result | Under the baseline rule (the preregistration's designated baseline, "The rule's form is the hypothesis"; A★2 "decides neither `R` nor `P`"), for a classical `(K, T, μ)` and a coupling that records set membership, the induced register operator is the compressed Koopman operator: positive, unital, nonnegative in the computed basis. Thirteen access rules screened on structure; none admissible. G★ names the gap: computed readout, leaving both invariants, a structure beyond the baseline with OI justification, no answer built in | R, frozen; token `INCONCLUSIVE (gap)`; "This is not a no-go"; review author-reported; G★ item 2 refuted in part (`README.md`:241–266) | Restricted access to substates, modelled as an induced operator, is nonnegative. The missing object is a coupling-level access principle |
| `operational-control-countercontrol.md` | On any carrier, controls restricted to time shifts of one bijection commute and cannot surject onto `PU(2)`; "a group-structure obstruction, not a finite-dimension obstruction" | R; paper argument; passive autonomous case only; it "does **not** assert an impossibility once the dynamics gains preparation- or setting-conditioned interventions" | An infinite hidden carrier with autonomous dynamics supplies no full control: the available group is abelian. An abelian one-parameter family is not excluded by it |
| `continuous-substates/README.md`, solenoid, infinite XOR, `equivalence-and-d3-scope.md`:19–30 | Real-type and `p`-adic per-site continua under the lattice wave map; exactly Markov solenoid law; "Moving to an infinite carrier removes the applicability of that theorem, **not** the underlying scientific challenge" | R; paper proofs "not independently reviewed on `main`" | Cardinality of the hidden space decides neither recurrence nor operations |
| `later-access-result.md`; 21 `native-*.md` units | Setting-conditioned access on the native rule: token `LA-EQUAL`, flag `EMPTY`, under five hypotheses; unit results such as "An independently programmable measurement interface is not established" | R; conditional; acceptance labels author-reported; opening and result lines read only | No programmable interface found for the candidates tried; none is a no-go |
| `observer-interface-source.md` §4 | "#1007: hidden continuum with finite observer access": "Infinite cardinality alone changes no specified operational availability map" | R; source assessment; "not an established premise on main" | States the owner's class 3 and finds no operation-changing process in the screened sources |
| apparatus-1 Lemma 2 (:153), §3.1 (:277–309), Lemma 5 (:731), C-ROT and dense control (:772–784), §5.3 (:955–1023), §5.7 (:1072–1085) | Lemma 2: every deterministic bijective apparatus lies in `permClass` on its physical carrier. Candidate SA-1: `q = 2`, the linear second-order step, with (a′) per-tick arming P3, (b) terminal registration P1, (c) half-known ready cells P2 and isolation E-iso; "Clauses (a′), (b) and (c) are new physical posits about control, access and resources". Under SA-1 and the one-cell frame R1: `Z`/`X` reads with the sequential Lüders law at stabilizer scope; no process induces the encoded quarter phase, "for any ancillas, adaptive record-conditioned corrections or input states" (Lemma 5); encoded `rot` is unavailable (C-ROT); "encoded dense unitary control fails". "The restriction to R1 is essential". §5.3: no finite carrier induces `rot` with exact statistics (the encoded action is one stochastic matrix applied `j` times; its unit-modulus eigenvalues are roots of unity); a continuum carrier (Kochen–Specker, imported, "Not read") induces every rotation for one system, with the re-preparation measure "the load-bearing choice". §5.7 poses Q-A and Q-B as open | R; merged after review rounds (status as reported in Q-A §6.1) | Restricted access as posited here gives phase-sensitive reads and no tunable operation in the frame tested. The negative is for `q = 2`, the linear step, R1 and posits P1–P3. Escape of the phase test needs another carrier: the finite rung P-8 needs "a permanently inaccessible functional" (a posit there) |
| Q-A Lemma G2 (:342), node 4 (:388–423), Lemma Q (:460) | G2: no encoded quarter phase from non-adaptive native processes, "with a hidden sector of any size, finite or not"; adaptive case open. Lemma Q, at `q = 2` for a symmetric center-free linear step: (i) the step conserves `Q = Σ u_i v_i`; (iii) "Under P1 and P2, every functional on active cells that the observer can determine has `Q* = 0`". P1 and P2 "keep apparatus-1's classification as supplied", and "native" there means "within N, using no posit beyond these" (:173–175). The P1-removed case "is an existing construction" that determines the protected functional (:512–516). §4.4: Lemma R's reflections and the Mermin–Peres parity constraint "should be among Q-B's controls" | R; paper proofs; model-reviewed ACCEPT (author-recorded) | Under the posited access restrictions P1 and P2, the conserved form of the linear rule at `q = 2` protects the present value of every `Q* = 1` functional of the active cells. Past values are not protected (M-INACC-1 §6.3). The conservation is derived from the rule; the inaccessibility is derived from posited access, not from OI's principles alone. With it the quarter phase needs a further premise (NNB), brings non-CP reflections (Lemma R) and fails two-system correlations (node 10) |
| feedback `RESULT.md` §§2–5 | Uniform linear encodings, common lift, available translations: no adaptive protocol gives `S` with a CP operation set; "an infinite hidden sector is allowed" | R; model-reviewed | Preparation-dependent lifts are outside its hypothesis H-C |
| MECH-1 Theorem W (:467–512), Proposition AS (:516), Proposition C (:751–766), §1.4 (:211–243), §6.5 (:1069–1076) | Class N: the linear symmetric center-free second-order rule with the `−x(t−1)` memory term, armed per tick and per edge (P3, E-iso), P2 ready cells, P1 terminal registration, discarding, translations, record feedback; N+NNB adds a same-sublattice coupling (a conditional premise). At odd prime `q`, in Gross's frame: every finite protocol of N or N+NNB, adaptive or not, whose ancilla laws have quantum images is a stabilizer instrument with every branch CP (Theorem W); "P1 is load-bearing" and "P2 is load-bearing" (without either, a branch has Choi eigenvalue `−1`; the record cites its self-checks c7, c7′ and apparatus-1 C9, C4). Among ontic bijections, CP ⇔ affine symplectic (Proposition AS). Proposition C, "For every protocol of N or N+NNB": reachable states have nonnegative Wigner functions; "Every available encoded unitary channel is Clifford", the group is finite, "so there is no encoded unitary of infinite order"; no quarter phase; the reachable class is "a local noncontextual hidden-variable model" (by Spekkens' equivalence, imported, read there in part). Setting selection is supplied by P3 and fails natively (Lemma A); missing premise M1. §1.4: the lead "Continuum or large-`q` limit with metaplectic quantization" is "Partly covered. Its exact finite form is the selected lead … The continuum form is left to Q-B (§6.5)" | R; paper proofs using Gross's theorems (read first-hand there in the parts it lists); reviewed scope as cited by MECH-2; the odd-`q` statements that use the memory sign need the `−x(t−1)` rule, which Main:726 item (xiii) posits (wave-sign `ASSESSMENT.md`, author checkpoint, review pending) | With the access posits the linear rule gives a quantum-compatible fragment; without them it gives non-quantum maps. They do not give tunability: at each fixed odd prime `q` the reversible encoded set is finite, and a classical model reproduces the fragment. Scope: linear rule, odd prime `q`, Gross's frame, posits P1–P3 |
| MECH-2 Lemma F (:325; hypotheses :309–323), Theorem U2 (:404), Theorem NC (:485), node 8 (:737–755), §6.2 (:810–871), §6.4 (:901–911) | *Lemma F.* Hypotheses: a fixed bijection of a finite configuration set, "any rule"; operations: attach cells "in fixed nonnegative laws", apply the rule, feedback, discard, condition on configuration records; H-LIFT; a linear identification by an orthogonal frame. No hypothesis on which reads exist. Conclusion: every encoded branch is a nonnegative matrix on frame coordinates. *Theorem U2(ii)*, product frame at `q = 2`: every encoded unitary branch of any fixed bijection is a frame permutation in `A_4 ≀ S_n`; its proof uses that "valid states span and the identification is injective", not spanning reads. So "no encoded `S`", no `T`, no entangling unitary, "no infinite-order unitary". Node 8, odd `q`: "every encoded unitary induced by any fixed bijection is Clifford". §6.4: under any finite orthogonal frame and H-LIFT the encoded unitaries of any dynamics "form a finite group"; an infinite carrier or hidden sector "is not assessed here; finite observer capacity does not imply a finite world". *Theorem NC* adds an injective identification with equivalences certified by spanning preparations and reads: then the configuration model is noncontextual for the whole encoded theory. "At `q = 2`, spanning certification needs a `Y` read, which is not exhibited natively. Over the native `Z`/`X` reads alone, Theorem NC does not apply"; "Such apparent contextuality is not a nonclassicality witness unless the missing reads are absent for a physical reason". M-INACC is named as the missing premise for nonclassicality; "Native class N has a native instance: Lemma Q", where "native" has Q-A's sense (within the class N, whose access posits P1 and P2 are supplied) | R; paper proofs; "Independent review of this file is a separate step" | Fewer reads do not reopen tunability: Lemma F and Theorem U2(ii) are universal over protocols, so they hold for every sub-collection [W]. What they assume about access is H-LIFT, with the fixed injective frame. Spanning reads are a hypothesis of the noncontextuality verdict only, and that hypothesis already fails natively at `q = 2`. "a contextual observer-level theory needs operational equivalences coarser than ontic equalities, and they must hold for a physical reason" |
| M-INACC-1 `RESULT.md` §0, §4, §6, §9 | For the symmetric state-dependent ring `G_σ` at `q = 2`, protocols using only the fixed rule, ready cells and terminal registration determine a protected functional in every record branch (the protocols `E_A`, `E_B`). Outcome (B, B); tiers Negative. Blocking premise P-GK reported, degenerate, not adopted. One control is red in the record's own table: "C-LIN is red for PROT-R", because the retrodictive property fails in the linear limits themselves ("archived cells can be sharp, so retrodictive `Q* = 1` protection does not hold even with Lemma Q"); "outcome (A), which requires PROT-R, is unreachable under the amended rule for any rule, QA's N included". "Neither class's outcome relies on PROT-R". The corrected property PROT-R′ holds in the linear limits and "is not adopted". "Lemma Q(iii) covers present active functionals only" | R; "WIP / UNVERIFIED"; model-reviewed | Lemma Q's protection does not survive this nonlinear rule. Negative for `G_σ` and these classes only. The negative is constructive and, on the record's terms, does not rest on the red control; the unit as amended could not have returned a positive |
| PC-1 `README.md` | Strict result `INCONCLUSIVE (void)`; finding carried under an owner exception: none of 25 candidates admissible; "not a no-go" | R; void; not independently validated on `main` | Not usable as a premise |
| `papers/GR.md`:136–142 | To `O(τ_S/τ_B)`, visible transition data do not depend on the cardinality of a slowly coupled deep sector, "finite, countably infinite, or uncountably infinite"; "The recurrence proof … requires $S$ finite, which Lemma 1 does not supply" | P; conditional on the frozen-deep-sector hypothesis | A mixing mechanism cannot sit in a slowly coupled deep sector; an infinite deep sector is admitted by GR's own corollary |

**What the records say about class 3.** None of the [R] items below is an established claim.

(i) *Modelled, and not a cause.* Restricted access is modelled, in the kernel and in the records,
wherever the state is a law on configurations and the hidden part is independent of the input;
there it only loses information. No obstruction read has restricted access as its operative
cause.

(ii) *Which results assume what about access.* Lemma F and Theorem U2(ii) of MECH-2, the results
that bear on tunability, assume fixed-law attachments, H-LIFT and a fixed injective linear frame,
and nothing about the reads. Under those hypotheses fewer reads do not reopen tunability, for any
fixed bijection. Theorem NC, the result on noncontextuality, adds spanning preparations and
reads, and that hypothesis already fails for the native reads at `q = 2`. Main:560 holds under
every restriction of access (B.7).

(iii) *Negatives obtained under restricted access.* Each is a result for the construction named
and for nothing wider.

- apparatus-1 [R]: `q = 2`; the linear second-order step; posits P1, P2, P3 and E-iso; the
  one-cell frame R1. No encoded quarter phase (Lemma 5, adaptive corrections and any ancillas
  included), no encoded `rot`, no encoded dense control. Lemma 5 does not depend on the access
  posits; the reads and their continuation do.
- Q-A Lemma G2 [R]: `q = 2`; bipartite linear class; native `X` read; non-adaptive processes; a
  hidden sector of any size. No encoded quarter phase. The adaptive case is open.
- MECH-1 Theorem W and Proposition C [R]: odd prime `q`; the linear symmetric rule with the
  `−x(t−1)` memory term; posits P1, P2, P3 and E-iso, with or without NNB; Gross's frame;
  adaptive protocols included. Every protocol is a stabilizer instrument; every available encoded
  unitary is Clifford, so none has infinite order; no quarter phase; no Wigner-negative state;
  the reachable class is a noncontextual hidden-variable model. Here P1 and P2 are what makes the
  encoded branches completely positive.
- M-INACC-1 [R]: `q = 2`; the state-dependent ring `G_σ`; P1, P2. The protection of Lemma Q is
  lost.

In the constructions on the linear rule the posited restrictions give stabilizer-type behaviour
that a classical model reproduces, with finitely many reversible encoded operations and no
tunable one. The cause of "finitely many" is not the access: under a fixed injective frame and
H-LIFT the encoded unitaries of every fixed bijection are frame symmetries (MECH-2 Theorem
U2(ii), node 8), and a finite alphabet makes that group finite. The second reviewer names the
affine rule as the class-2 cause; the source supports the wider form, bijections acting on laws,
since MECH-2 node 8 extends Proposition C(b) "from N to all dynamics". The affine form is what
makes the branches completely positive. So restricted access has been tried on the linear rule in the form in
which it was posited, and it did not supply tunability. Other rules, other frames, non-injective
identifications and infinite alphabets are outside these results.

(iv) *Where access could matter.* For nonclassicality, by changing what counts as an operational
state: equivalences coarser than ontic equalities, held for a physical reason. That premise is
named (M-INACC). Its nearest instance, Lemma Q(iii), is conditional on two posited access
restrictions ("Under P1 and P2"; apparatus-1 §3.1: "new physical posits") and protects present
values only ("covers present active functionals only", M-INACC-1 §9); it is not supplied by the
state-dependent rule tested. For tunability, M-INACC on a finite carrier would open the class of
the 8-point quarter-phase mechanism (MECH-2 §6.2, "What it buys"), where exact `rot` stays
excluded (apparatus-1 §5.3). The question on `main` about tunability is Q-B (section D, row D10).

(v) *Finiteness.* Nothing read assumes that finite access implies finite underlying dynamics; G2,
the countercontrol and GR's corollary are stated for hidden sectors of any size, and MECH-2 §6.4
leaves the infinite case unassessed.

***

## C. Exact versus approximate

Five separate claims: (1) exact continuous tunability; (2) ε-approximation for every ε by one
fixed finite system; (3) ε-approximation by a family of finite systems growing with 1/ε;
(4) ε-approximation from one fixed rule, as opposed to a construction made per experiment;
(5) either, on an infinite underlying state space.

**What the kernel has for approximation** [K]. Predicates on a theory over the two-state
carrier: `DenseUnitaryControl` (OB/DiscreteCompletion.lean:45–48: every unitary at every level
is within every `ε > 0`, in operator norm and up to a unit scalar, of an available one),
`KrausDense` (:52–56) and `DenseFiniteQM := KrausSoundExt T ∧ KrausDense T` (:59–60). Theorems:

> `theorem denseUnitaryControl_of_fixedGate (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi))`
> `    (hg : FixedGateSourced α T) : DenseUnitaryControl T`
> (OB/DiscreteCompletion.lean:1522–1523)
>
> `theorem fixedGateTheory_one_denseFiniteQM : DenseFiniteQM (fixedGateTheory 1)`
> (OB/DenseInstrumentBridge.lean:526)
>
> `theorem fixedGateTheory_not_qm (α : ℝ) : ¬ ExactAllFiniteEndomorphicQuantumOps (fixedGateTheory α)`
> (OB/DiscreteCompletion.lean:1948)

`fixedGateTheory α` is the stated access, the quarter phases and one real rotation of one site
by the fixed angle `α`, closed under the architecture operations (:1926–1927). At multiples of
`π/4` the generated level-one group is finite up to scalar (`gen2_multiple_finite_upToScalar`,
:1834). The census lists both modules as "kernel-only" with no manuscript text
(`verification/lean-manuscript-census.json`:676–694). The fixed gate is postulated; it is not
monomial for `α ∈ (0, π/2)` (`mixImage_not_monomial`, OB/StateMixingCoupling.lean:166).

**The kernel's exclusion of approximation** [K, proofs read].

> `theorem nonnegBounded_not_denseUnitaryControl {T : FiniteOperationalTheory (Fin 2)}`
> `    (h : NonnegBounded T) : ¬ DenseUnitaryControl T`
> (OB/FrozenSourcing.lean:173–174)

`NonnegBounded T` says that every available one-outcome operation at every ancilla level
preserves entrywise nonnegative matrices (:65–67). The proof takes the quarter phase at level
two, uses `preservesNonneg_of_approx` (:127: a unitary that is an operator-norm limit of
unitaries whose conjugations preserve nonnegativity has a conjugation that preserves it) and
contradicts `phaseGate_not_preservesNonneg`. The variant at :240 uses the real rotation at `π/4`
at level one, with no phase in the witness. `permTheory_dense_ceiling` (:187) is the instance for
the sourced theory; `nonnegBounded_of_bijectionLevel` (:74) covers every bijection-level class and
`nonnegClass_nonnegBounded` every nonnegative class; `sourcing_rule_independent` (:295) shows the
verdict is the same for every rule on the same sites and alphabet. The kernel also has the other
side: `fixedGateTheory_outside_ceiling` (:336), the dense theory is not nonnegativity-bounded.
Scope: the statement is on the two-state carrier and concerns approximation of a unitary by
available unitary conjugations. Approximation of a channel by available non-unitary operations is
excluded by the same closed invariant [W]; the kernel has no `¬ KrausDense` theorem.

**What Main has for approximation** [P]. The gluing theorem (Main:566) and the
uniform-continuum theorem (Main:598): for fixed `d`, outcome bound `m`, horizon `K` and `ε`
there is one finite reversible deterministic realization within `ε` in total variation of
every adaptive quantum protocol. Limits stated there: the bound holds for exact-arithmetic
registers, and "a bound on the realized outcome law of the clipped and normalized simulator at
finite $b$ is open" (Main:566 clause (1)); "Quantum mechanics enters as the instrument data and
as the state held in the hidden register … the construction uses no property of the substratum
beyond finiteness and reversibility" (Main:582); "the same reversible machinery can realize
non-quantum finite instrument families" (Main:584); "What remains is selection" (Main:602). The
coverage ledger records both theorems as paper level with "no Lean statement"
(`verification/coverage/LEDGER.json`:1200–1240).

| Obstruction | (1) exact | (2) every ε, one fixed finite system | (3) growing family | (4) one fixed rule | (5) infinite underlying space |
|---|---|---|---|---|---|
| Sourced observer theory; every nonnegativity-bounded theory (B.5) | excluded [K] (`permTheory_not_control`; `falsifierUnavailable_of_nonnegBounded` for `rot`) | excluded [K], two-state carrier, as no dense unitary control (FrozenSourcing:173, :187, :240) | the invariant holds at every ancilla level and on every carrier [K] (`permTheory_nonnegBounded`); non-approximability is [K] only as no dense unitary control on the two-state carrier, where the approximant is a unitary conjugation at the same level; an approximant built with a larger ancilla and a discard is the [W] step of the scope sentence above (the second reviewer's check of it: a nonnegativity-preserving map has `(0,1)` entry ≥ 0 on the matrix unit where the target has `−1/2`) | excluded [K]: `sourcing_rule_independent` | not expressible in the kernel (`Fintype`). [R]: no full control from autonomous dynamics on any carrier (the time-shift group is abelian); no quarter phase from non-adaptive native processes with any hidden sector (B.12) |
| Monomial class with complex phases (B.1) | excluded [K] | excluded [W]: diagonal preservation is closed; the target differs from every diagonal-preserving map by `12/25` in one entry, and from every monomial unitary by `3/5` in operator norm. No kernel theorem | excluded [W]: the invariant does not depend on ancilla size | excluded [W] | [W] for weighted partial injections (B.1); not on `main` |
| B.2 as stated | vacuous | vacuous | vacuous | vacuous | vacuous |
| B.3 / B.4 countermodels; `flow_endpoint_refuted` | non-entailment only | not addressed | not addressed | not addressed | not addressed |
| B.6 counting | excluded [K] | **not excluded**: with one postulated gate a dense countable class exists [K] | not excluded | not excluded: `fixedGateTheory 1` is dense for every ε [K], with a postulated gate and unbounded ancilla levels | not addressed |
| B.7 Main:560 | excluded for fixed `N` [P, P-imp] | excluded [W]: for fixed `N` and a fixed finite experiment the realizable behaviours form a compact set (the reviewer checked this argument) | **not excluded**; established with the stated limits [P] (Main:566, :598) | one map per `(𝓕, K, G)` (Main:582) [P]; one fixed finite rule for every ε is excluded by (2); one rule on an unbounded state space is not addressed on `main` | outside the hypothesis. [R] apparatus-1 §5.3: exact `rot` is impossible on a finite carrier and is induced by an imported continuum model for one system, with the measure a free choice |
| B.8 Main:488 | excluded for fixed finite `(S, prior, φ)` [P] | excluded for the whole instrument continuum [W] | not addressed | not addressed | outside the hypothesis |
| Encoded carrier, finite configuration set, fixed injective linear frame, H-LIFT (MECH-2, apparatus-1) [R] | excluded for every fixed bijection: encoded unitaries are frame symmetries, a finite group (MECH-2 §6.4) | excluded for the quarter phase under the one-cell frame: stochastic matrices are closed (apparatus-1:778–784); a finite group of encoded unitaries is not dense, for any fixed number of cells [W] | excluded under the product frame for every number of cells and ancillas (Theorem U2(ii)) | every rule | "not assessed" (MECH-2:910–911) |
| Linear class N with the posited access (P1, P2, P3, E-iso; with or without NNB), odd prime `q`, Gross's frame (MECH-1 Theorem W, Proposition C) [R] | excluded: every available encoded unitary is Clifford, a finite group, at each fixed `q` | excluded at a fixed `q`: the group is finite, and reachable states keep nonnegative Wigner functions (Proposition C(a), (b)) | cells and ancillas: excluded at fixed `q` (Proposition C covers every protocol). A family in growing `q`: not addressed; named and "left to Q-B (§6.5)" (:217) | the step is the lattice model's linear rule; which edge is armed at each tick is loaded from outside (P3); the access is posited | not derived. Named as Q-B's first test, "whether AS survives the real or large-`q` limit: exact continuous symplectic rotations of quadratures, with C-CP"; "A qubit `rot` would still need non-Gaussian, Wigner-negative resources" (:1073–1076) |

[W] remark on column (4), not a claim to adopt: any computation-universal reversible rule on an
unbounded state space can approximate to every ε with the quantum data in the initial condition,
which is the reading Main:582 gives of its own construction. The linear rule of ledger item (vii)
is not of that kind.

Two readings follow from the table and should be kept apart.

- If "quantum behaviour" means coherence on the configuration basis (the interface of B.1),
  approximation is as excluded as exactness, and finiteness is not the reason.
- If it means an encoded quantum carrier, as in the gluing theorem where the quantum state is
  "held in the hidden register", then approximation by growing finite families is established
  at paper level, exactness on a fixed finite system is excluded, and nothing read decides
  exactness or uniform approximation on an infinite underlying state space. For this reading
  `main` poses Q-B (D10): its approximate form is a family in growing alphabet size built from
  the lattice model's own linear rule, as distinct from Main:566 where the quantum rule is the
  input; its exact form is the continuum alphabet.

The kernel's approximate target needs less than the exact one: a single non-monomial gate at an
irrational angle with the phases and exchanges, not a continuum of operations. For the sourced
theory both the gate and the phases are excluded by the nonnegativity invariant, approximation
included; for the monomial class the gate is excluded by diagonal preservation.

***

## D. What is not excluded

Each row is logical room left by B and C, with its status against (a) kernel results on `main`,
(b) paper records on `main`, (c) the two off-`main` drafts. Column (c) is context only: INTERVENE-1
r2 (`origin/research/intervene-1-20261111`, `ea12fde1`) and SUBSTATE-BRIDGE-1 r2
(`origin/research/substate-bridge-1-20261111`, `86a413c8`) are unverified drafts, model-reviewed
at most, conditional on their hypotheses P-CONF (states are laws on configurations), H4 and H-IND
(the law of everything outside the carrier, given the carrier, does not depend on the input).
They establish nothing here. "Open" means logical room, not evidence.

| Opening | Outside which hypotheses | (a) kernel | (b) records on `main` | (c) off `main` [D] | Status |
|---|---|---|---|---|---|
| D1 infinite underlying space, finite access | Main:560, Main:488 (finite `N`); the kernel's `Fintype` | not expressible | autonomous dynamics: no full control on any carrier (the time-shift group is abelian); non-adaptive native processes: no quarter phase with any hidden sector; finite-stage reduction for continuous readouts of towers [R]. Exact `rot` needs an infinite carrier (apparatus-1 §5.3) [R] | E1 and saturation: an arbitrary measurable hidden carrier induces on a finite carrier only what a finite register induces | Closed conditionally on the configuration-law reading with input-independent hidden parts. Open only together with D2, D3 or D10. Revising it changes ledger item (ii) |
| D2 encodings that are non-linear, non-injective or chosen per measurement context | the fixed injective linear frame of MECH-2 Lemma F and Theorem U2 | not expressible | fixed injective linear frames with H-LIFT are closed for every dynamics as to encoded unitaries (Lemma F, Theorem U2(ii)), with no condition on the reads; noncontextuality needs spanning reads in addition (Theorem NC). Non-injective encodings host the finite quarter-phase mechanisms (U′, P-8; MECH-2 node 7). No finite carrier gives exact `rot` (apparatus-1 §5.3) [R] | E2: one shared linear encoding makes all native measurements jointly measurable; the continuum (Husimi) frame hosts every unitary as a point map and no sharp read | Open for non-linear and per-context encodings. As a class it contains "QM by fiat" (amplitudes as coordinates, the Born measure posited) |
| D3 memory outside the identified carrier | H-IND, H-LIFT, the uniform ancilla | not expressible (`prepAvail_uniform` only) | "Without H-LIFT … the encoded description must be enlarged until H-LIFT holds" (MECH-2:346–347); preparation-dependent lifts are outside the feedback result's H-C; Q-A's CP recovery "does not apply to an additional correlated or preparation-dependent hidden background by declaration" (PROOF-RECOVERY:24–25) | named route C-dyn, "not decided" | Open and unexamined for protocols whose hidden part depends on the input law; then no linear map on carrier states is defined |
| D4 limits and completions | finite derivations of `InstAvail` | nonnegativity passes to limits (`preservesNonneg_of_approx`) | towers: finite stage per horizon (ANALYSIS.md) [R]; quasilocal path "*additional structure*, chosen rather than derived" (Main:274) | E3 | Largely closed. Remaining: non-continuous readouts, infinite horizon |
| D5 sourcing that is not configuration-level | the choice of class | "say nothing about sourcings that do not" (OB/ManuscriptAxioms.lean, header); every lift formulation tested is configuration-level (`coherentLiftClass_eq_substratumClass`) | L3 lift: no map from amplitudes to the carrier is stated (F2-1 §3, G★) [R] | no admissibility criterion exists; the class is data | Open, and requires giving up "states are laws" or supplying an admissibility rule |
| D6 approximate target | — | excluded with exactness for the sourced theory | — | — | Not an opening |
| D7 restricted access as coarser operational equivalence (M-INACC) | H-LIFT and the injective identification (Lemma F, Theorem U2); spanning reads (Theorem NC) | discard and `nonnegClass` cover the configuration-law form: neither `rot` nor the phases | named missing premise. Nearest instance: Q-A Lemma Q(iii), "Under P1 and P2", which apparatus-1 §3.1 classes as "new physical posits about control, access and resources"; linear rule, `q = 2`; it "covers present active functionals only" (M-INACC-1 §9; past values are exposed by a one-tick protocol, §6.3). Negative for `G_σ` (M-INACC-1), in a unit that could not have returned a positive. With Lemma Q the quarter phase still needs NNB, yields non-CP reflections and fails two-system correlations [R] | every partition and every fixed conditional prior is covered by T0 | **Open.** The corpus's own form of the owner's class 3. It concerns nonclassicality, not tunability: on a finite carrier a positive answer opens the class of the 8-point quarter-phase mechanism, and exact `rot` stays excluded there. No source in OI's stated principles; the one instance rests on posited access |
| D8 adaptive native processes | non-adaptivity in Lemma G2 | not addressed | "Adaptive native processes are not covered" (Q-A §0, §4.3); the combined target with CP is excluded for uniform linear encodings (feedback result); record feedback is covered at odd prime `q` (MECH-1 Lemmas S, G; Proposition C) and in the one-cell frame at `q = 2` (apparatus-1 Lemma 5); adaptive gradedness at `q = 2` is open (MECH-1 node 5) [R] | — | Open in a bounded sense, at `q = 2` only |
| D9 time coarse-graining, stopping times | — | products of admissible operators | — | covered by T0 | Not an opening |
| D10 continuum or large-alphabet limit of the lattice model's linear rule under the posited access (Q-B) | the finite alphabet in MECH-1 Proposition C; the finite carrier in apparatus-1 §5.3 and MECH-2 §6.4 | not expressible | Q-B posed and open (apparatus-1 §5.7). Two first checks are named and neither is run: for the ball-containing carrier, "Whether a native reciprocal read on a continuum cell with a symplectic area form … produces the cosine-weighted re-preparation law without a supplied measure" (apparatus-1 §5.4); for the linear rule, "whether AS survives the real or large-`q` limit", "not derived here" (MECH-1 §6.5). The exact finite form at odd prime `q` was the lead MECH-1 selected and tested: a finite Clifford group, a stop. Controls named in Q-A §4.4. Infinite case "not assessed" (MECH-2 §6.4) [R] | per-site continua are the setting of SUBSTATE-BRIDGE-1 r2 (the second reviewer's reading of its later part: no new edge and no new single-procedure map under H-IND) | **Open, not started.** The question on `main` about continuous rotations. Its record expects a qubit `rot` to need more. Access and arming are posits. The approximate form stays on a finite substratum; the exact form revises ledger item (ii) |

The first draft's D2 ("encodings in which the quantum carrier is not the configuration basis")
was too broad and is replaced by the D2 row; its D7 ("not modelled by any obstruction theorem")
was wrong and is replaced by the D7 row.

***

## E. Inputs the characterization takes as given

These are not among the conditions. Deriving them is a separate obligation.

1. **Complex matrix kinematics.** States and operations are `ℂ`-linear maps on `Matrix A A ℂ`
   (A.0). Main:564: "a kinematics whose derivation from operational premises is open".
2. **Finite dimension.** `[Fintype A]`, and every ancilla is `Fin n`. The "exact finite
   endomorphic" qualifier is this input.
3. **Composite structure.** A composite is the product index `A × Fin n` with the Kronecker
   product; discard is the partial trace (`discardWith`, OB/OperationalAssembly.lean:515–518).
4. **The preparation.** A uniformly mixed ancilla is the only preparation assumed
   (`uniformAttach`, :492–496).
5. **The readout.** A basis readout of the ancilla exists and is spectator-independent
   (structure fields `readout`, `readout_avail`, `readout_local`, :640–644); its Lüders form is
   then derived (`readout_is_localLuders`, :658).
6. **Trace as probability.** Condition (i) is stated with the trace.
7. **Exact membership.** Availability is a proposition; no approximation is expressible in the
   characterization itself.
8. **For the substratum-source and closure forms only:** the interface map of B.1 item 2; the
   choice of class (`substratumClass`, or `permClass` as the least architecture with the
   exchanges); the isometry requirement `Kᴴ * K = 1` of `InstAvail.op`
   (OB/ImplementationLocality.lean:271–272).
9. **Upstream of all of it:** Lemma 1's physical premise in its kernel form (OB/Finiteness.lean),
   and the total-finiteness posit wherever a hidden sector is taken finite.

***

## F. Recommendation, the decisive question, and findings

### F.1 Recommendation on Step 2

The reconciliation with the records of B.12 and with the two off-`main` drafts is Step 1 work and
is done above, within the reading limits stated at the top.

**Recommendation: hold Step 2.** No mechanism survey. The one question on tunability that `main`
poses is Q-B. Hold on one owner decision: whether to activate Q-B's first test, paper-only, with
the controls below fixed in advance. M-INACC is not recommended now.

The grounds follow, in the order: why no survey; the two questions on `main`; why hold; the
controls.

**A survey of mechanisms is not supported.** By B.11 and section C the operative obstruction on
the configuration-basis interface is not finiteness and not restricted access, and it covers
approximation. By B.12 the restricted-access route has been worked on `main` through several
units, each ending in a stop or a gap with a named missing premise (G★; NNB and I; M1; M-INACC;
P-GK). Where access restrictions were posited for the linear rule, the result is a
stabilizer-type fragment that a classical model reproduces, with finitely many reversible
encoded operations (apparatus-1 at `q = 2`; MECH-1 at odd prime `q`). Lemma Q's protection holds
"Under P1 and P2", two posits, and "covers present active functionals only"; the one test of its
extension to a state-dependent rule was negative, for that rule.

**Two questions are posed on `main` and unanswered.** They concern two different missing things.
M-INACC concerns nonclassicality. Q-B concerns tunability, the subject of this unit. Neither is
derived or reviewed, and in both the access restrictions are posits.

| | Q-B | M-INACC |
|---|---|---|
| As `main` states it (M-INACC's list set inline) | "What additional OI principle could produce the continuous rotations (§5.3)? This means a ball-containing carrier whose reads re-prepare with the cosine-weighted law, without a supplied measure, and whose composite extension respects Main §3.3." (apparatus-1 §5.7) | "For each encoded system there is an ontic functional with three properties: the fixed rule uses it, so later statistics depend on it; no permitted preparation, read, reuse or recombination determines it or changes its conditional law; its inaccessibility follows from a structure stated without reference to the quantum target." (MECH-2 §6.2; "conditional extension premise, not adopted") |
| The missing thing | an encoded reversible operation of infinite order, exact or as a limit | operational equivalences coarser than ontic equalities, held for a physical reason |
| What blocks it in the records | a finite alphabet or carrier under a fixed injective frame: the encoded unitaries are a finite group (MECH-1 Proposition C(b); MECH-2 §6.4; apparatus-1 §5.3) | Theorem NC within its scope: injective identification, H-LIFT, spanning certification |
| First test, as named | "whether AS survives the real or large-`q` limit: exact continuous symplectic rotations of quadratures, with C-CP" (MECH-1 §6.5). For the ball-containing carrier: whether a native reciprocal read on a continuum cell gives the cosine-weighted law "without a supplied measure" (apparatus-1 §5.4) | "A symmetric `G(x)` under which Lemma Q(iii)'s conclusion survives nonlinear transport" (MECH-2 §6.2) |
| What the first test found | Not run: "This is not derived here"; Q-B is "not activated" (MECH-2 §6.4). What was run is the exact finite form at a fixed odd prime `q` (MECH-1): a finite Clifford group, no encoded unitary of infinite order, a stop | Run once, for the ring `G_σ` (M-INACC-1): negative for that rule and those protocol classes. Outcome (A) was unreachable in that unit as amended |
| What an answer would decide [W, read against the tables] | Yes: in the linear class the finite alphabet is the only reason no infinite-order operation exists, and approximation in growing alphabet size comes from the lattice model's own rule. No: a further obstruction is present in that class. Neither decides nonclassicality | Yes, for some rule: an observer-level theory outside Theorem NC's scope exists for a stated physical reason. No, for a rule: that rule only. Neither decides tunability |
| Ceiling stated by its own record | "A qubit `rot` would still need non-Gaussian, Wigner-negative resources" (MECH-1 §6.5); the continuum counterpart cited there is "the Liouville epistricted theory", read as an abstract only | "It opens the class in which AP1's rung P-8 and QA's U′ live" (finite, quarter phase); "Independent consequence (§A.29). None established"; flagged CC-RECON if adopted only to reach the target |
| Approximate case (finite substratum) | A family in growing alphabet size. Each member is finite, so exactness is excluded member by member. Comparing members needs a correspondence between alphabets; of such a correspondence SM §2.7 says it "is not constructed here" [W for the bearing]. Ledger item (ii) is untouched | On a finite carrier a positive answer gives finite-order operations only; exact `rot` stays excluded (apparatus-1 §5.3). Approximate tunability is not what the premise addresses |
| Exact case (infinite substratum) | A continuum alphabet. This revises ledger item (ii), a Layer-0 revision under §A.29 | "not assessed" (MECH-2 §6.4). Lemma Q(iii) "places no condition on the size of the hidden sector"; an infinite carrier revises ledger item (ii) |

So the two cases differ for both questions. For Q-B the approximate case is a finite-substratum
question and the exact case is not. For M-INACC the finite case cannot yield tunability at all.

**Separate openings, kept apart from both questions.**

- *Input-correlated memory* (D3). Unexamined: Q-A's CP recovery and the feedback result both
  exclude preparation-dependent hidden backgrounds by declaration, and MECH-2 handles them by
  enlarging the encoded carrier until H-LIFT holds. No record read poses it as a question.
- *The infinite substratum* (D1). On the configuration-law reading with input-independent hidden
  parts, cardinality alone changes no operation. It enters only as the exact case of Q-B, and
  then as a Layer-0 revision. Before any work it would have to state the results it preserves,
  which become its controls (the recurrence step needs finite `S`, GR:142; the finite-horizon
  equivalence; Lemma 3's counting measure, for which the records use a normalized product law on
  a cone as a named hypothesis, H-INF-μ), and at least one independent prediction. None is
  identified here.
- States that are not laws (D5) and non-linear, non-injective or per-context encodings (D2) stay
  as listed in section D.

**Why hold, and on what.** Step 2 was scoped as an evaluation of candidate mechanisms for tunable
mixing. The tables show one such question posed, Q-B; the other openings (D2, D3, D5) name no
mechanism. Three facts from the records bear on whether to start it, and each is for the owner
to weigh.

1. By its own record the first test's best outcome is continuous symplectic rotations of
   quadratures, with a counterpart in the Liouville epistricted theory, and not a qubit `rot`.
2. The access restrictions (P1, P2) and the arming of every coupling (P3) are posits, so a
   positive result would be conditional on them. MECH-1 finds that setting selection "fails
   natively" under one fixed affine rule (Lemma A).
3. The exact form is a Layer-0 revision for which no list of preserved results and no
   independent prediction exists.

Q-B also has a scope of its own. The record of the owner's decision on its target (Issue #1169,
comment 6712409082, amaybaum, 2026-11-07T20:08:39Z; provenance, not on `main`; linked from Q-A
`DESIGN.md`:6) reads: "This decision sets Q-B's scientific target. It does not authorize
execution", with the disposition "A Q-B unit gets its own scope from the owner". A Step 2 under
TUNE-1 would duplicate that unit. The decision to hold on is therefore whether to activate Q-B
with its first test. If the owner does not, TUNE-1 stops at Step 1 and the tables above are its
result.

M-INACC is not recommended as the next question: it is not a tunability question, no second
candidate rule is named in the records read, and the unit that tested the first one could not
have returned a positive, so its protection property would have to be repaired first (PROT-R′
"is not adopted").

**Controls to fix in advance, if Q-B's first test is activated.** Each comes from a recorded
failure or a recorded requirement.

1. *Classical-imitation control* (MECH-1 CC-IMIT′, rule D2). Report whether the mechanism's own
   noncontextual model reproduces every sequence. If it does, the verdict is stated as "not
   separated from classical imitation".
2. *External-control check* (MECH-1 SC-2, Lemma A). State which coefficients are loaded from
   outside. If the rotation angle is an armed coefficient, the tunability is supplied by P3 and
   is not derived [W for this application of the check].
3. *Selection controls* (Q-A §4.4; MECH-1 C-CP, C-COMP). Every encoded branch completely
   positive; Lemma R's reflections absent; the Mermin–Peres parity constraint for composites;
   the composition battery K1–K6, with errors followed under repetition, adaptive measurement
   and recombination.
4. *Limit and exposure controls.* At each fixed `q` the construction must reproduce Proposition C
   (a finite group), so that the limit is not built in. Removing P1 or P2 must break complete
   positivity, as in MECH-1's scope note.
5. *Preserved results, approximate form.* The correspondence between alphabets is stated before
   it is used (SM §2.7); the condition `3 ∤ q` for the normalized coefficient (SM §2.7) and the
   `−x(t−1)` memory term (Main:726 item (xiii)) are carried.
6. *Exact form only.* The §A.29 list above, before any work.

Should M-INACC be taken up instead, its controls are those its records name: no non-CP or
reflection-type encoded maps (Q-A Lemma R; MECH-2 P★); equivalences certified over a spanning
read set, or the missing reads shown absent for a physical reason (Theorem NC scope); the
protocol class fixed first, with the access posits removed as exposure controls and the linear
limit reproducing Lemma Q; verdicts per record branch.

### F.2 A prior question for the owner

Which interface counts as "quantum behaviour arising": coherence on the configuration basis
(excluded, approximation included, for a class-2 reason) or an encoded carrier (where exactness
needs an infinite substratum, and the open items are Q-B for tunability and M-INACC for
nonclassicality). The corpus does not settle this, and the answer changes which obstructions
bear. On the encoded reading a second point is for the owner: whether continuous rotations of
quadratures obtained without Wigner-negative resources count toward the target, since the record
of Q-B's first test expects a qubit `rot` to need more.

### F.3 Findings: prose on `main` versus the Lean statement

1. **Main:590 cites `readWriteSourced_not_qm`** for "finite reversible read-write dynamics,
   even with genuine hidden-memory and readback behavior, does not itself generate quantum
   state mixing". The theorem's hypothesis is unsatisfiable (B.2) [W; recorded as vacuous in
   [R] records on `main`]. The structure `ReadWriteFamily` has no hidden memory or readback in
   it; the countercontrol is a two-valued family. *Prose says more than the Lean statement
   supports.* Non-vacuous witnesses exist: `obs_not_qm`, `permTheory_not_qm`,
   `bijectionLevel_not_layerFlowExecutable`, `monomialSource_not_qm`. The same citation occurs
   in `papers/GR.md`:260 (seen in a search; the passage was not read), `verification/README.md`:298,
   `verification/programmes/substratum/source-audit.md`:100–121 and
   `verification/programmes/substratum/route-b-audit.md`:29.
   The vacuity and its citation sites, Main:590 and GR:260 among them, are recorded in Issue
   #1188 (open; the reviewer read it and reports the owner's decision there, "Do not use it as
   scientific evidence"). The reviewer names two further sites:
   `verification/audits/operational/completion-assumption-audit.md`:95 and the `RouteB.lean`
   docstring; `papers/Main.tex` and `papers/GR.tex` carry the citation as well. Not checked here.
2. **Main:590, "with that one operation added as an empirical controllability resource it is
   equivalent to the same operational quantum mechanics on every nonempty finite carrier"**,
   citing `substratum_plus_control_qm` and `qm_generated_by_substratum_extension`. The Lean
   hypothesis is `DrivesElementary`: the flows of every pair at every finite carrier at every
   real time, every exchange and every quarter phase. The hypothesis `ExtendsSubstratum` is
   unused in the forward statement, structural closure of the extended class is assumed and not
   derived, and the reverse statement is witnessed by the class of all operators. A
   one-datum statement exists, `mixTheory_qm` (OB/StateMixingCoupling.lean:511), on the
   two-state carrier only, with the quarter phases in the stated access. *Prose says more than
   either statement.*
3. **Main:590, "under finite bijective read-write dynamics, not the continuously tunable
   state-mixing operation".** The clause is a scope statement. The kernel invariants behind the
   cited results are cardinality-free, while the kernel proofs are typed over finite carriers and
   the monomial class closure uses cardinality once (B.1). *No discrepancy; the only
   finiteness-based statement in this neighbourhood is `readWriteOperator_range_finite`.*
4. **Main:584, full reversible control is what "the substratum's stated interventions do not
   supply".** The theorem is about the theory generated by `IsMonomial`, and the assignment of
   monomials to interventions is a definition (B.1 items 2–3). Main:590 later scopes this ("in
   every formulation stated that lands in the operational interface"). *Scope note:* the
   theorems bound configuration-level sourcings and say nothing about others, as the kernel
   header states.
5. **Two objects are called OI.** Main:584 says the five conditions are "none supplied by bare
   finite OI"; Main:590 says "the concrete OI substratum supplies the structural architecture".
   Both are supported, for different objects: the sealed-core predicate (independence by
   countermodel) and the generated theory of a class (four of the five conditions as theorems,
   A.3). The second is conditional on the class being taken as data. *Terminology, not a
   contradiction.*
6. **Reversible richness contains continuous tunability.** Main:586 names "reversible richness"
   without its definition; the Lean definition asserts the flow of a drift at every real time
   (A.2). A reader of the prose alone would not see that one of the three added principles of
   OI⁺ is the tunability premise. *Prose says less.*
7. **Lemma 1.** Main:62 says "only finite visible resolution is a theorem (Lemma 1)". The
   kernel module proves an implication from a premise of finitely many boundary modes and
   states that the lemma's "justification is physics" (OB/Finiteness.lean, header). Main:48 and
   Main:702 give two different justifications. *Prose says more than the Lean statement.*
8. **The kernel's density theorems are not in the manuscripts.** `DiscreteCompletion` and
   `DenseInstrumentBridge` are "kernel-only" in the census. Main's discussion of exact versus
   finite-accuracy realization (Main:564, :600) does not mention that one fixed theory with one
   postulated gate is dense in finite quantum mechanics and not exact. *Prose says less.*
9. **Main:560 has no kernel witness and no coverage row found.** Main:602 item (3) words it as
   "proved under the stated operational interface, the unbounded-dimension half imported",
   which is accurate. *Coverage note only.*
   The reviewer reports a ledger row at `"line": 488` whose label and evidence string do not
   match Main:488 at the pin, so this may be a stale row and not a missing one. Not checked here;
   outside this unit's scope. Likewise `equivalence-and-d3-scope.md`:19 cites "Main:554" for the
   Proposition that is at Main:560 at the pin.

### F.4 §A.31 classification of this unit's output

Productivity test for r2, fixed before the revision's reading: a finding counts if it changes a
cell of B.11, C or D, or a clause of the recommendation. The first draft fixed its test after
the fact.

- B.12 and the D7 and D10 rows (restricted access is modelled; of the results for every dynamics
  only Theorem NC needs spanning reads; negatives exist under posited access, each for its
  construction; two questions are posed on `main`): **ELABORATING**. The content is in
  apparatus-1, MECH-1 and MECH-2; the sorting against the owner's classes is the addition.
- The r3 changes (Lemma Q's conditions, the hypotheses of each MECH-2 result, Q-B) are
  **CONFIRMING**: findings of the second review, checked here against the three records read in
  full.
- Three invariants in place of one; the cardinality step in `submonomial_monomial`; the [K]
  status of the approximation cell: **CONFIRMING** (the reviewer's findings B2–B4, verified here
  against the proofs).
- `permClass_arch` has no cardinality step, so the nonnegativity route is cardinality-free up to
  the typing of matrices: **ELABORATING** [W].
- Finding 1: **CONFIRMING** (#1188). Finding 2: **BORDERLINE**; not checked against prior audits.
Assumption-watch marker for other units: a kernel non-availability theorem about a generated
theory is a statement about the chosen class and interface; before it is cited as a statement
about the substratum, the sourcing map has to be named.

No correctness band moves (§A.23): this unit relabels and sorts existing results.
