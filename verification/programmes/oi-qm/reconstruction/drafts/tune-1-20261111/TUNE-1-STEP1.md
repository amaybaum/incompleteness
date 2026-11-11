# TUNE-1, Step 1: the assumptions behind the state-mixing obstructions

**WIP / UNVERIFIED writer draft, revision r4 after three independent reviews (REVISE on `204043ce`; REVISE, narrow, on `e9fbe998`; REVISE, narrow, on `d573eec4`); r4 itself is not reviewed; paper-only; pin = origin/main SHA `cac5d26441dd33e9348151487e4df7b547195481`.**

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

**Reading and disclosure for r4.** An inventory of the records on `main` was built before this
revision was written; it is Appendix G, and it replaces the reading lists of the earlier
revisions as the statement of what was read. Method: every Markdown file under `verification/`
(778 files) was scored by two keyword families (Appendix G.1); the Lean tree and `papers/*.md` were
searched for `DenseBoundaryOrbit`, `KTRANS-DENSE`, dense orbits, boundary transitivity and infinite
order; each matching record or record group was classified on the basis Appendix G.1 and G.4 state,
and the records classified relevant were read as Appendix G.2 states. Commands added: `find`,
`sort`, `uniq`, `head`, `tail`, `cp`, `mv`, and `gh api` for three read-only reads (the bodies of
Issues #1236 and #1217; comment 6712409082 on #1169). No
probe, checker or Lean build was run (`python3` was invoked once by mistake with an empty script
and executed no code); no checker of any record cited below was
replayed, so a record's computed values are quoted as the record states them. Nothing was posted.
The D10 row does not depend on a reviewer's reading of
SUBSTATE-BRIDGE-1 r2, which was read to its end for this revision.

**Limit of the negative statements.** A statement below of the form "nothing on `main` decides X"
is limited to the records Appendix G marks as read in full, and to the named parts of those it
marks as read in part. Appendix G.3 names every relevant record not read in full, with the part
read and the reason.

***

## Plain-language summary

**The question.** In OI the world only reshuffles its configurations. Quantum mechanics needs
operations that blend two states by any chosen amount ("adjustable mixing"). What assumptions
rule that out?

**1. Finitely many observer states.** Alone this rules out nothing: such an observer can sit in an
infinite world. If the whole world is finite (assumed in OI, not derived), exact adjustable mixing
is impossible; approximation by ever larger finite systems is not.

**2. Only reshuffles allowed.** If the quantum state is written directly over the world's
configurations, reshuffling never produces mixing, exactly or approximately. Every valid
machine-checked obstruction says this. If the state instead summarises what an observer can
prepare and measure, a reshuffle can act as a quantum operation.

**3. Limited access.** It causes no obstruction; where quantum behaviour appears, limited access
produces it. Unverified research records on `main`:

- A known model with a continuous hidden sphere and coarse preparation and readout reproduces one
  quantum bit exactly, every rotation included, with its ingredients put in by hand.
- If lattice sites held real numbers and a coupling could be set externally to any value, OI's
  own update would blend two modes by any angle. Neither addition has a source, and with
  unrestricted readout the result is not quantum.
- On finite systems it gives a fixed finite set of operations.

**Exact versus approximate.** Exact needs an infinite underlying world. Growing finite systems
approximating it have been built twice, with key ingredients supplied.

**Cautions.** Adjustable mixing is necessary, not sufficient. One cited theorem
(`readWriteSourced_not_qm`, Issue #1188) has a premise nothing can satisfy; it is not counted.

**Open on `main`.** What fixes an observer's preparations and readouts; where real-valued sites
and adjustable couplings could come from; whether a finite world keeps anything permanently unreachable.

**Recommendation.** Hold Step 2. First decide what counts as "quantum behaviour arising" (F.2);
then whether to activate one question, its pass/fail rules fixed first.

## 0. Summary

1. **Kernel obstructions: three invariants, all class 2, all tied to one interface** (B.1, B.5).
   - *Diagonal preservation.* An operator with at most one nonzero entry in each row and column
     conjugates diagonal matrices to diagonal matrices (monomial and configuration-level
     classes). `rot` violates it.
   - *Nonnegativity preservation.* Scaled partial permutations, and more generally entrywise
     nonnegative operators, preserve entrywise nonnegative matrices (the observer theory
     generated by the exchanges, `permTheory`; every bijection-level class; the class
     `nonnegClass`). `rot` and the quarter phase violate it.
   - *Ones-fixing.* Admissible isometries of a ones-fixing class fix the all-ones vector up to a
     scalar. `rot` and the quarter phase violate it.
   The invariants use no bound on the number of states. The interface they are stated in
   identifies the matrix basis with the configuration labels; that identification belongs to
   none of the owner's three classes. A record on `main` exhibits its role: under another
   observer-level map a permutation of eight hidden points acts as a Hadamard gate, "including
   the output off-diagonal entry -1/2 that the previous pointwise map excluded"
   (`operational-quotient-v3/REPORT.md`) [R].
2. **Counting obstructions: class 1, about the underlying system, and exactness only.**
   - Paper level: a fixed realization with `N < ∞` ontic configurations cannot reproduce one
     qubit's full prepare-and-measure theory (Main:560, half imported) and supports finitely
     many instrument families (Main:488).
   - Kernel level, operational interface: a class of operators countable up to scalar executes no
     layer flow at level one, and on the two-state carrier generates no exact quantum theory.
   - Kernel level, convex-body interface of the reconstruction rounds: a countable family is not
     boundary transitive on the 3-ball; a body whose points have finite orbits admits no drive;
     an operation that carries each finite stage to itself has finite order on the completed body
     (section C).
3. **Restricted access (class 3) is the operative cause of no obstruction, and is the ingredient
   of every positive exhibit on `main`** (B.12). All [R]; none is an established claim.
   - *A continuum carrier with restricted preparations and reads reproduces one qubit exactly*
     (`history-architecture-v5`: the Kochen–Specker sphere model, credited prior work). Rotations
     are point maps of the hidden sphere. The preparation cone, the sign read, the fresh
     re-preparation and the private workspace are supplied: "None is sourced here by the native
     lattice or derived from OI's conditions." Exposing the workspace, the seeds or a
     state-dependent completion time breaks the correspondence.
   - *The lattice model's own second-order update gives every mixing angle on one pair, under two
     unsourced additions* (`two-mode-drive.md`, B1): real-valued sites (E-real) and an exactly
     loadable real coefficient (E-control). With point preparations and a sign read the
     statistics have "no realization by density states and preparation-independent effects on any
     one fixed finite-dimensional quantum carrier" (`whole-model-bridge.md`). Here the
     obstruction is too much access, and the record names the missing statement: an
     "observer/access quotient lemma".
   - *On a finite carrier an access quotient gives a finite set of operations*: the 24 Clifford
     actions on the eight-point model, with an error floor of 1/15 for one non-Clifford rotation
     in that representation (`operational-quotient-v3`); a finite group of encoded unitaries
     under any fixed orthogonal frame containing every correlated cell, for every dynamics
     (MECH-2 Lemma F, Theorem U2(ii)); stabilizer operations under the posited access
     restrictions on the linear rule (apparatus-1, MECH-1).
   - *The named missing premise for nonclassicality on a finite carrier* is M-INACC (MECH-2
     §6.2). Its nearest instance, Q-A Lemma Q(iii), holds "Under P1 and P2", two posits, and
     "covers present active functionals only"; the one test on a state-dependent rule is
     negative, for that rule.
4. **"Finite observational access implies finite underlying dynamics" is not derived anywhere
   read.** Total finiteness is a posit (Main:62, Main:726 item (ii); `papers/Substratum.md`:92;
   `papers/GR.md`:142). Both exact positive exhibits of item 3 use an infinite underlying space
   with finitely many observer outcomes.
5. **Exact and approximate are separate at every layer** (section C).
   - On the configuration-basis interface both are excluded: in the kernel for every
     nonnegativity-bounded theory on the two-state carrier, in the form "no dense unitary
     control"; by a short argument [W] for the monomial class with phases.
   - The counting obstructions exclude exactness only. The kernel has both sides: one postulated
     gate at an irrational angle gives a countable dense theory that is not exact; a countable
     family with a dense boundary orbit is not boundary transitive, and eleven named consequences
     of boundary transitivity need only the dense orbit.
   - For observer-level statistics: exact reproduction needs an infinite underlying space;
     approximation by growing finite systems is constructed in Main with the quantum rule as
     input (Main:566, :598) and, for one qubit at a fixed menu and horizon, from the sphere
     model's geometry (`finite-a2-v5`) [R]. One fixed finite controller of a stated class fails
     with depth on one protocol (`a2_depth_v7`, `a2_memory_v8`) [R].
   - A continuously tunable flow alone is not sufficient for quantum mechanics
     (`flow_endpoint_refuted`).
6. **Openings and recommendation** (sections D, F). A mechanism survey is not supported. `main`
   states one gap at several levels: the programme map's question for its active endpoint, the
   access quotient lemma, Q-B, the unresolved observer-level wave lift, and M-INACC for
   nonclassicality. The recommendation is to hold Step 2 on two owner decisions, in order: the
   target reading (F.2), then which single question, if any, to activate (F.1).
7. **One citation on `main` rests on a vacuous hypothesis** (Main:590,
   `readWriteSourced_not_qm`; recorded in Issue #1188; section F, finding 1). It is not counted in
   item 1.

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
    `FiniteOperationalTheory` cannot express "finite observer, infinite substratum"; the convex-body
    interface of the reconstruction rounds has a completion over directed finite stages (section C).
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

**Non-vacuous statements with the intended content** [K]: `monomialSource_not_qm`, on `Fin 2`
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

**Sorting.** No obstruction: the hypothesis cannot hold, so the theorem places no theory on either
side of any class. It is kept apart from the valid obstructions in B.11 and section C and is not
counted in section 0. The neighbouring `readWriteOperator_range_finite` is a class-1 statement in
which the underlying set is finite: **(a)** for that statement.

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
| B.2 `readWriteSourced_not_qm` | K, vacuous hypothesis | no obstruction: the hypothesis cannot hold. The neighbouring `readWriteOperator_range_finite` is a class-1 statement about the underlying set | no obstruction: the hypothesis cannot hold | no obstruction: the hypothesis cannot hold | (c); (a) for the range statement | no |
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
| MECH-2 Lemma F, Theorem U2(ii), §6.4 | R | **operative**: finite configuration set and finite frame (posit) | **operative**, as bijections acting on laws; no restriction on which bijection | no condition on the reads; H-LIFT, fixed-law attachments and a fixed orthogonal (hence one-to-one) linear frame are the hypotheses | (a) | as the posit |
| MECH-2 Theorem NC | R | finite configuration set (posit) | as the row above | adds spanning preparations and reads; at `q = 2` the native `Z`/`X` reads do not span and the verdict is undecided there | (a) | as the posit |
| `whole-model-bridge.md`, Proposition "BR-0(d) fails for every finite d" | R | not used: the carrier is `R^2 × R^2` (added input E-real) | not used: the drive supplies every angle (added input E-control) | **operative, in the reverse direction**: unrestricted point preparations, their composition with the drive, and a sign read give `d + 1` pairwise perfectly distinguishable preparations for every `d` | underlying space infinite by the added input | no |
| `operational-quotient-v3`, cube preservation; `product-section-v4` | R | **operative**: the eight-point hidden carrier | one stochastic kernel independent of the preparation label must intertwine a Bloch rotation with the fixed first-moment decoder on every admitted prior | in force as an access quotient (admitted preparation region, private workspace and seeds, fresh reset); under it the rotations are the 24 Clifford actions | (a) | no |
| `a2_depth_v7`, `a2_memory_v8` (one protocol) | R, exact computation and a paper proof | **operative**: finite whole persistent state, `B` fair fresh bits per slot | time-independent update | the sphere model's access contract in force | finite controller; "Nothing here concerns … OI" | no |
| OG-1 `isEmpty_drivability_of_finite_orbits`; EFF-1 `not_boundaryTransitive_of_countable`; ORD-1 `finiteOrderOn_of_stagePreserving`, `not_ordInf_of_finite_of_mulClosed` | K, native rounds with receipts as their result notes report | **operative**, as finite orbits, a countable family, a finite composition-closed family | **operative** for the stage statement: an operation that maps each finite stage's preparations to that stage | not modelled: the body is the operational state space | (c): the body is a completion over directed finite stages, of finite rank by hypothesis | no |

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
| apparatus-1 Lemma 2 (:153), §3.1 (:277–309), Lemma 5 (:731), C-ROT and dense control (:772–784), §5.3 (:955–1023), §5.7 (:1072–1085) | Lemma 2: every deterministic bijective apparatus lies in `permClass` on its physical carrier. Candidate SA-1: `q = 2`, the linear second-order step, with (a′) per-tick arming P3, (b) terminal registration P1, (c) half-known ready cells P2 and isolation E-iso; "Clauses (a′), (b) and (c) are new physical posits about control, access and resources". Under SA-1 and the one-cell frame R1: `Z`/`X` reads with the sequential Lüders law at stabilizer scope; no process induces the encoded quarter phase, "for any ancillas, adaptive record-conditioned corrections or input states" (Lemma 5); encoded `rot` is unavailable (C-ROT); "encoded dense unitary control fails". "The restriction to R1 is essential". §5.3: no finite carrier induces `rot` with exact statistics (the encoded action is one stochastic matrix applied `j` times; its unit-modulus eigenvalues are roots of unity); a continuum carrier (Kochen–Specker, imported, "Not read" there; the model is audited on `main` in `history-architecture-v5`, row below) induces every rotation for one system, with the re-preparation measure "the load-bearing choice". §5.7 poses Q-A and Q-B as open | R; merged after review rounds (status as reported in Q-A §6.1) | Restricted access as posited here gives phase-sensitive reads and no tunable operation in the frame tested. The negative is for `q = 2`, the linear step, R1 and posits P1–P3. Escape of the phase test needs another carrier: the finite rung P-8 needs "a permanently inaccessible functional" (a posit there) |
| Q-A Lemma G2 (:342), node 4 (:388–423), Lemma Q (:460) | G2: no encoded quarter phase from non-adaptive native processes, "with a hidden sector of any size, finite or not"; adaptive case open. Lemma Q, at `q = 2` for a symmetric center-free linear step: (i) the step conserves `Q = Σ u_i v_i`; (iii) "Under P1 and P2, every functional on active cells that the observer can determine has `Q* = 0`". P1 and P2 "keep apparatus-1's classification as supplied", and "native" there means "within N, using no posit beyond these" (:173–175). The P1-removed case "is an existing construction" that determines the protected functional (:512–516). §4.4: Lemma R's reflections and the Mermin–Peres parity constraint "should be among Q-B's controls" | R; paper proofs; model-reviewed ACCEPT (author-recorded) | Under the posited access restrictions P1 and P2, the conserved form of the linear rule at `q = 2` protects the present value of every `Q* = 1` functional of the active cells. Past values are not protected (M-INACC-1 §6.3). The conservation is derived from the rule; the inaccessibility is derived from posited access, not from OI's principles alone. With it the quarter phase needs a further premise (NNB), brings non-CP reflections (Lemma R) and fails two-system correlations (node 10) |
| feedback `RESULT.md` §§2–5 | Uniform linear encodings, common lift, available translations: no adaptive protocol gives `S` with a CP operation set; "an infinite hidden sector is allowed" | R; model-reviewed | Preparation-dependent lifts are outside its hypothesis H-C |
| MECH-1 Theorem W (:467–512), Proposition AS (:516), Proposition C (:751–766), §1.4 (:211–243), §6.5 (:1069–1076) | Class N: the linear symmetric center-free second-order rule with the `−x(t−1)` memory term, armed per tick and per edge (P3, E-iso), P2 ready cells, P1 terminal registration, discarding, translations, record feedback; N+NNB adds a same-sublattice coupling (a conditional premise). At odd prime `q`, in Gross's frame: every finite protocol of N or N+NNB, adaptive or not, whose ancilla laws have quantum images is a stabilizer instrument with every branch CP (Theorem W); "P1 is load-bearing" and "P2 is load-bearing" (without either, a branch has Choi eigenvalue `−1`; the record cites its self-checks c7, c7′ and apparatus-1 C9, C4). Among ontic bijections, CP ⇔ affine symplectic (Proposition AS). Proposition C, "For every protocol of N or N+NNB": reachable states have nonnegative Wigner functions; "Every available encoded unitary channel is Clifford", the group is finite, "so there is no encoded unitary of infinite order"; no quarter phase; the reachable class is "a local noncontextual hidden-variable model" (by Spekkens' equivalence, imported, read there in part). Setting selection is supplied by P3 and fails natively (Lemma A); missing premise M1. §1.4: the lead "Continuum or large-`q` limit with metaplectic quantization" is "Partly covered. Its exact finite form is the selected lead … The continuum form is left to Q-B (§6.5)" | R; paper proofs using Gross's theorems (read first-hand there in the parts it lists); reviewed scope as cited by MECH-2; the odd-`q` statements that use the memory sign need the `−x(t−1)` rule, which Main:726 item (xiii) posits (wave-sign `ASSESSMENT.md`, author checkpoint, review pending) | With the access posits the linear rule gives a quantum-compatible fragment; without them it gives non-quantum maps. They do not give tunability: at each fixed odd prime `q` the reversible encoded set is finite, and a classical model reproduces the fragment. Scope: linear rule, odd prime `q`, Gross's frame, posits P1–P3 |
| MECH-2 Lemma F (:325; hypotheses :309–323), Theorem U2 (:404), Theorem NC (:485), node 8 (:737–755), §6.2 (:810–871), §6.4 (:901–911) | *Lemma F.* Hypotheses: a fixed bijection of a finite configuration set, "any rule"; operations: attach cells "in fixed nonnegative laws", apply the rule, feedback, discard, condition on configuration records; H-LIFT; a linear identification by an orthogonal frame. No hypothesis on which reads exist. Conclusion: every encoded branch is a nonnegative matrix on frame coordinates. *Theorem U2(ii)*, product frame at `q = 2`: every encoded branch of any fixed bijection that acts as `p · Ad U` "with `p > 0` independent of the input" is a frame permutation in `A_4 ≀ S_n`; its proof uses that "valid states span and the identification is injective", not spanning reads. So "no encoded `S`", no `T`, no entangling unitary, "no infinite-order unitary". Node 8, odd `q`: "every encoded unitary induced by any fixed bijection is Clifford". §6.4: under any finite orthogonal frame and H-LIFT the encoded unitaries of any dynamics "form a finite group"; an infinite carrier or hidden sector "is not assessed here; finite observer capacity does not imply a finite world". *Theorem NC* adds an injective identification with equivalences certified by spanning preparations and reads: then the configuration model is noncontextual for the whole encoded theory. "At `q = 2`, spanning certification needs a `Y` read, which is not exhibited natively. Over the native `Z`/`X` reads alone, Theorem NC does not apply"; "Such apparent contextuality is not a nonclassicality witness unless the missing reads are absent for a physical reason". M-INACC is named as the missing premise for nonclassicality; "Native class N has a native instance: Lemma Q", where "native" has Q-A's sense (within the class N, whose access posits P1 and P2 are supplied) | R; paper proofs; "Independent review of this file is a separate step" | Fewer reads do not reopen tunability: Lemma F and Theorem U2(ii) are universal over protocols, so they hold for every sub-collection [W]. What they assume about access is H-LIFT, with the fixed orthogonal frame. Spanning reads are a hypothesis of the noncontextuality verdict only, and that hypothesis already fails natively at `q = 2`. "a contextual observer-level theory needs operational equivalences coarser than ontic equalities, and they must hold for a physical reason" |
| M-INACC-1 `RESULT.md` §0, §4, §6, §9 | For the symmetric state-dependent ring `G_σ` at `q = 2`, protocols using only the fixed rule, ready cells and terminal registration determine a protected functional in every record branch (the protocols `E_A`, `E_B`). Outcome (B, B); tiers Negative. Blocking premise P-GK reported, degenerate, not adopted. One control is red in the record's own table: "C-LIN is red for PROT-R", because the retrodictive property fails in the linear limits themselves ("archived cells can be sharp, so retrodictive `Q* = 1` protection does not hold even with Lemma Q"); "outcome (A), which requires PROT-R, is unreachable under the amended rule for any rule, QA's N included". "Neither class's outcome relies on PROT-R". The corrected property PROT-R′ holds in the linear limits and "is not adopted". "Lemma Q(iii) covers present active functionals only" | R; "WIP / UNVERIFIED"; model-reviewed | Lemma Q's protection does not survive this nonlinear rule. Negative for `G_σ` and these classes only. The negative is constructive and, on the record's terms, does not rest on the red control; the unit as amended could not have returned a positive |
| PC-1 `README.md` | Strict result `INCONCLUSIVE (void)`; finding carried under an owner exception: none of 25 candidates admissible; "not a no-go" | R; void; not independently validated on `main` | Not usable as a premise |
| `papers/GR.md`:136–142 | To `O(τ_S/τ_B)`, visible transition data do not depend on the cardinality of a slowly coupled deep sector, "finite, countably infinite, or uncountably infinite"; "The recurrence proof … requires $S$ finite, which Lemma 1 does not supply" | P; conditional on the frozen-deep-sector hypothesis | A mixing mechanism cannot sit in a slowly coupled deep sector; an infinite deep sector is admitted by GR's own corollary |
| `oi-qm-ext-1/endpoints.md` (Gate A) | Defines the comparison target `J_exact(A)`: every density preparation, every finite-outcome instrument, every finite adaptive protocol, every positive ancilla level, with one native model and one label interpretation for all of them. §3 keeps two targets apart: "exact correspondence for the full `J_exact(A)` family" and a "Separate approximation target: for declared dimension, finite menu, finite horizon and ε > 0, one realization covers the entire declared experiment family to a stated error. An approximation theorem does not establish the primary target"; "Failure of the primary target does not authorize retrospectively replacing it with the approximation target" | R; "Definitions, source inventory and proposed bridge obligations; no new equivalence theorem or physical mechanism is established"; scoped review recorded on PR #1173 (`README.md`) | The exact and the approximate claim are separate targets in the records' own contract |
| `oi-qm-ext-1/two-mode-drive.md` (B1) | *Question*: "Can one specified second-order, two-mode coupling supply a continuously driven mixing transition without postulating a quantum gate?" *Inputs*, each with the record's own status: E-pair, one isolated pair ("no physical isolation mechanism is derived here"); E-real, the pair and its one-step memory have real coordinates `(x,y)` in `R^2 × R^2` ("Added real-mode extension; not inferred from finite `Z_q` configurations or an unspecified coarse-graining"); E-control, a loaded signed coefficient `k` in `[-1,1]` with exact values ("Added intervention resource; native availability and exact continuum precision are unsourced"); E-clock, E-prepare, E-read. *Update*: `T_k(x,y) = (kXx − y, x)`, the second-order template of SM §4.1 on the pair, reversible "both over `Z_q` (for coefficients in that ring) and over the reals". *Result 1*: on the fixed coordinates `z = x + iy`, where multiplication by `i` is the zero-coupling step `J = T_0`, a fixed word of 24 updates acts as `U = exp(iθX)` for every real `θ`, with a common duration; "It does not identify a native configuration or ensemble with a quantum state"; a single step with `k ≠ 0` is not complex linear. "Exact real parameter loading is precisely the unsourced E-control resource; this construction does not obtain it from a finite controller alphabet." *Result 2*: a sensor copying `1[x_1 > 0]` records 1 after `U = I` and 0 after `U = −I` from the same point preparation; `z` and `−z` have the same rank-one density, so "No such instrument can match the native bits above while preserving this carrier/operation/record dictionary" | R; paper algebra; "a conditional amplitude-control component together with a concrete readout/dictionary obstruction and named physical sourcing gaps. It is not a native physical OI-to-QM reconstruction"; scoped review recorded on PR #1173 | Classes 1 and 2 are removed by hand (real sites, a loadable coefficient) and continuous mixing of two modes follows from the lattice update's own form. Class 3 then decides the outcome: with a sign read the density dictionary fails. "Any repair must physically establish an appropriate phase-congruent preparation/readout quotient, as well as the desired probability law. Simply declaring the native readout to be Born sampling, or choosing a hidden distribution to encode the desired quantum table, would add the answer as an assumption." The mixing is of real mode coordinates on one pair; "The all-level phase-free criterion is not discharged by this single pair" |
| `oi-qm-ext-1/whole-model-bridge.md` | Candidate E-AR: B1's carrier and drive, point preparation `z = e_1` followed by a drive as preparation and a second drive as test, the sign sensor, B3's detector. *Proposition*: the sign statistics `1[cos(θ+φ) > 0]` have no representation `Tr(σ_θ F_φ)` with density operators and preparation-independent effects on `C^d`, for any one fixed `d`; "The state encoding may be nonlinear and need not be the original rank-one dictionary". Proof: `d + 1` angles are pairwise perfectly distinguished by sign tests (Lemma 1), and pairwise perfectly distinguishable density operators have orthogonal supports (Lemma 2). Controls: any finite list of `N` angles is represented on `C^N` ("a table representation"); the sphere model of `history-architecture-v5` "does not admit the exact point-preparation orbit of Lemma 1. The present obstruction does not refute that conditional positive control"; "Changed preparation or access: finite resolution, noise, restricted preparations, loss of sign access, or a different carrier/reference model changes a premise of this assessment. Such a physical restriction must be sourced independently". §7: "The next missing physical statement is an **observer/access quotient lemma**: derive, from independent physical premises, which preparations and coupled readouts are available, and why their complete operational state can pass the required finite-dimensional state/effect test. A quotient must remain valid under every allowed control and read … It cannot simply identify states that an available sensor distinguishes." | R; "a hand proof about one added-access extension. It is not a no-go for bare OI, other preparation/access principles, or finite-menu representations with growing dimension"; scoped review recorded on PR #1173 | The owner's third possibility in the setting where continuous mixing exists in the substratum. With full access to it the observer's theory is not quantum; the statement that would make it quantum is a restriction of preparations and reads, derived and not chosen. "Exact real loading is an explicit added condition. It is not a derivation from a single fixed finite configuration space or a finite controller alphabet"; "A finite-menu/precision approximation remains a separately named target" |
| `oi-qm-ext-1/measurement-source.md` (B2), `measurement-exchange.md` (B3) | On B1's carrier, with a posited quadratic normalized sensor `t(z)`, seeds `q` with an atomless law `μ` and ready records. B2: the one-read law is `F(cos²θ)`; it matches the quantum value for every `θ` exactly when `μ` is uniform in the detector coordinate, "necessity and sufficiency for this response function and test family only"; with the signal unchanged and fresh seeds, no fixed `C^2` instrument matches the two-read law. B3: adding a record-controlled exchange with ready reference carriers gives the basis Lüders instrument's one- and two-read statistics for the uniform seed law; "The source verdict is **UNSOURCED at the inherited and first new physical gates**". Both retain B1's sign control: "This detector calculation supplies no physical reason to discard it" | R; conditional; scoped reviews recorded on PR #1173 | A quantum-like read on the real carrier is obtained with the response function, the seed measure and the exchange supplied. The quadratic response and the uniform law "are explicit inputs, not a derivation of Born selection" |
| `states-dynamics-audit-20261024/REPORT.md`, `CURRENT-HANDOFF.md` | Four endpoints kept apart: a bounded calibrated menu; "A2 approximation"; almost-sure termination; "A1 exact availability: each target instrument itself belongs to the available theory. A convergent sequence does not establish this membership without an additional rule; a closure rule changes the target theory". Assumption table: the entry "Countability excludes arbitrary-precision approximation" has status "False", with "The existing fixed-gate theory is a direct countercontrol"; the entry "Arbitrary real priors, arbitrary real observer dials, infinite descriptions, or closure points are automatically countable" has status "Not asserted". "the outstanding step remains sourcing an operation/state correspondence that actually changes a load-bearing A1 premise, or establishing a stated A2 endpoint under permitted resources" | R; "Consistency axis only"; internally reviewed | Exact and approximate are distinguished in the records in the owner's sense, with the kernel's countability premise stated as a hypothesis on the realization map |
| `…/operational-quotient-v3/REPORT.md`, `product-section-v4/REPORT.md` | Hidden carrier `{−1,+1}^3`; observer-level state by the fixed first-moment decoder `D(p)`; admitted preparation region; Pauli sign reads with fresh reset; private workspace and seeds. Under this contract operational equivalence is equality of first moments, the Hadamard gate is a hidden permutation, and every finite adaptive Pauli record and outgoing state agrees with the quantum reference. "the earlier invariant is not a map-independent no-go for all operational quotients. Its stated fixed-identification theorem remains intact." A stochastic kernel implementing a Bloch rotation on every admitted prior must preserve the sign cube, so "the proper rotations give only the 24 single-qubit Clifford actions"; for one rational non-Clifford rotation the record error on two admitted preparations is at least 1/15 (2/15 for the product preparations of `product-section-v4`). "It is not an A2 error floor for OI generally." Access countercontrols: retaining the carrier, reading old workspace or exposing the seed breaks the correspondence. The model is credited prior work (the eight-state stabilizer model) | R; exact bounded checks and written proofs; separate-author reviews retained; "No native implementation, new physical premise, changed G3 identification, observer restriction or full-equivalence verdict is adopted" | A finite carrier with an access quotient leaves the configuration-basis obstruction and reaches a finite set of operations only. "escaping the old invariant requires an explicit operational correspondence, and that correspondence has its own preparation, access and operation-availability constraints" |
| `…/history-architecture-v5/{PLAN,REPORT}.md`, `review/REPORT.md` | The Kochen–Specker sphere model (credited; read there through Ruebeck–Lillystone–Emerson, arXiv:1812.08218v3 §4.1.1). Hidden point `λ ∈ S^2`; pure preparations with density `(n·λ)_+/π`; the preparation cone is their finite positive mixtures, "a specified cone, not the set of all positive sphere measures"; decoder by mass and `(3/2)` first moment; a unitary is the rotation `λ → Rλ`; a read is `sign(a·λ)` followed by fresh re-preparation at `±a`; old carrier, seeds and workspace are private with no return coupling; fixed completion ticks. Proved there: the decoder is positive on the cone and covers every qubit state; every rotation intertwines; every finite adaptive rank-one projective protocol has the quantum record and outgoing-state law; a global reversible dilation exists. Countercontrols with exact gaps: no reset or reading old workspace (TV 1/5), exposed seeds (decoder outside the positive cone), state-dependent timing (TV 1). Supplied: "a continuum hidden sphere and exact cosine-hemisphere preparation laws; arbitrary exact real setting directions and unitary rotation primitives; initially independent continuum uniforms …; fixed timing, a one-bit public pointer and private workspace/seed isolation. None is sourced here by the native lattice or derived from OI's conditions." Not covered: general instruments, composites, Bell structure | R; written proofs and bounded exact controls; separate-author review "Accept within the stated scope", "separate-agent internal review, not external validation" | The owner's third possibility, exhibited for one qubit: every rotation is a deterministic point map of a continuum, the observer prepares only laws in a cone and reads one sign, and the observer-level theory is exact. "The density/response choice reproduces quantum probabilities; it does not derive their physical selection." "Enlarging a classical hidden space alone was insufficient under the old pointwise/G3 map: this candidate also changes the operational correspondence, preparation cone and supplied availability" |
| `…/finite-a2-v5/REPORT.md`; `a2_efficiency_v6` (through `CURRENT-HANDOFF.md`) | A finite discretization of the sphere model: `N = 6M²` grid labels, `W`-bit weights, `B` fair bits per reserved block, a rotation word of length at most `h`. For a fixed finite rational menu and at most `h` adaptive operations, the complete record and decoded outgoing state are within `min(1, (52h+300)/M + (8h+48)/2^W + (h+6)(N−1)/2^B)` of the quantum protocol in trace distance; for every `ε` parameters exist (`h = 3`, `ε = 1/10`: `N = 1,122,854,400` labels, 156 fair bits). "It uses one common geometric response function, not the unknown preparation label or a table of quantum protocol answers." Executed instance: `M = 16`, 1,536 labels, horizon three, error below 0.074764 | R; written proofs, exact checks at small sizes; internal reviews retained; "It is not a native OI implementation, selection of the sphere prior, physical clock or access derivation, composite-system model, or full A1/A2 reconstruction" | Approximation by a family of finite systems growing with `1/ε` and with the horizon, for one qubit, with the sphere model's geometry, reset and access supplied |
| `…/a2_depth_v7/REPORT.md`, `a2_memory_v8/REPORT.md` | On the protocol "prepare X+, then read a, X, a, X, …", whose quantum agreement probability is 4/5: for the executed controller extended by one fresh block per slot, and for every controller in the memoryless reset class at every fixed `B`, the complete-record total variation from quantum theory tends to 1 with depth (certified above 1/2 for `h ≥ 67,382,091`). *Theorem* (`a2_memory_v8`): the same for every controller whose whole persistent state is finite, with `B` fair fresh bits per slot and a time-independent update; "the obstruction is arithmetic: dyadic fresh randomness against a run law with ratio 4/5". Escapes recorded: a reset with linearly growing private memory "granted the target cuts"; a five-valued fair source. Open there: bounded private memory with unbounded public state, time-dependent updates, growing blocks | R; exact computation with independent audit code and a paper proof; internal reviews retained; "Nothing here concerns A1 (exact QM reconstruction), native availability, physical premises, access rules or OI" | One fixed finite system of this class does not approximate at every depth. A result on one protocol and one class of controllers |
| `…/stopping-source-v2/REPORT.md` | A countably infinite fair reservoir with almost-sure stopping samples a stated irrational probability exactly: "finite fair randomness at a fixed deadline and fair randomness with almost-sure unbounded access have different exact expressive power". "Under the fixed G3 identification and the pointwise mixed-hidden-state model, enlarging the reservoir does not change the kind of induced operation … A negative off-diagonal entry cannot be obtained by changing the scalar sampling weights"; "this is not a kernel theorem for an infinite native substratum" | R; a written argument; reviewed internally | An infinite hidden resource changes exact probabilities and, on the configuration-basis reading, no operation |
| `verification/audits/foundations/coherent-continuum-source-audit.md` (outcome and scope sections); `lift-source-audit.md` (outcome) | A census of nine routes (S1–S9) to an uncountable family of non-proportional non-monomial admissible operators, the resource an executable layer flow needs. Verdict: "**outcome 2, no current source; the empirical extension remains**". S3: "uncountable parameter domain does not give uncountable operational image". S5: the canonical gate path "has the algebraic continuum and is not an available family". S7, the observer-level wave lift: "a real/complex wave operator on site/amplitude space, with the map to the operational carrier explicitly unproved"; "underdetermined until a carrier map and admissibility statement are supplied"; "no map is invented". S8, the continuously tunable coupling: "**not part of the current axioms**; a future physical extension, not a current source". "The condition is necessary only" | K for the module `CoherentContinuumSource` (seventeen named results, as the note reports); the census is a reading of the corpus | The corpus's own list of where a continuum could come from. Every route that lands in the operational interface fails; the one that does not land (S7) is unresolved, and B1 is a worked instance of it for one pair |
| `verification/audits/foundations/real-pair-flow-audit.md` (outcome and scope sections) | `PairFlow`: a one-parameter family on one pair with identity at zero, the group law, continuity, orthogonality and nontriviality. Every such flow is the rotation family and supplies the mixing datum at every angle. Verdict: "**outcome 2, reduction succeeds, sourcing fails**": "no stated structure of the corpus establishes those hypotheses on the operational carrier" | K for the module `RealPairFlow` (twenty named results, as the note reports) | Continuous tunability on the operational carrier reduces to five hypotheses on one pair; none is sourced. B1's family acts on the real phase space of a pair, not on the operational carrier |
| `verification/programmes/oi-qm/PROGRAMME.md` §§1, 3.1–3.3, 5 (Arcs D, F), 10 | "The active endpoint is F2. For the presently stated architecture the equivalence endpoint F1 is retired". §3.2: "this is a sourcing no-go for the presently stated architecture. It is not a representation theorem, and it does not show that an extended architecture cannot source the resource." Arc D: "The crucial question for F2 is which physical principle, added to OI and separately motivated, sources it together with valid measurements and compatible state transformations, and what that principle predicts beyond the resource it is introduced to supply." The lift seam: "do not infer “OI sources composite operational QM” merely from “OI sources one-carrier coherent control”" | The programme's strategic map: "not a theorem, an audit, a preregistration"; "Where this map and a theorem/audit disagree, the theorem/audit controls" | The programme's own statement of the open question on tunability. It asks for a principle "added to OI"; the owner's question for TUNE-1 is about existing principles |
| Reconstruction rounds OG-1, EFF-1, ORD-1, KTRANS-DENSE-1 (`result.md` of each; Lean statements in section C) | A second kernel interface: a convex body of operational states, a family `G` of affine automorphisms, and a completion body over directed finite stages. Tunability enters as the hypotheses K∞-R (`BoundaryTransitive`) and a drive. OG-1 "What stays open": "a source … for the drive and its boundary transitivity on the completion body (K∞-R)". ORD-1: "Nothing here supplies an operation datum, finite rank, a completion chart or stage preservation from an OI construction". KTRANS-DENSE-1: "This round does not show that OI, StageCompletion or the observer architecture yields a dense boundary orbit or boundary transitivity" | K; native rounds, receipts and exact-head runs as each result note reports (not checked here); census: no manuscript text found by search | The exact and the approximate form of the tunability premise are separated in the kernel a second time, and the kernel has a limit object over finite stages |

**What the records say about class 3.** None of the [R] items below is an established claim.
The owner's wording has two parts: continuous mixing exists in the deterministic substratum, and
the embedded observer reaches it only in part. The records bear on each part separately.

(i) *Not a cause of any obstruction.* Wherever the state is a law on configurations, the
operation is read as a matrix over configuration labels and the hidden part is independent of the
input, restricted access only loses information (kernel: discard, `nonnegClass`; Main:328). No
obstruction read has restricted access as its operative cause. In the one obstruction where access
is operative, the bridge's Proposition, the cause is unrestricted access.

(ii) *The cause of every exact or approximate positive.* In each positive exhibit the hidden
dynamics is a bijection of configurations and the quantum behaviour is a property of the
observer-level description: which preparations are admitted, which reads exist, what is private.

- Continuum carrier, exact, one qubit: the sphere model (`history-architecture-v5`). Every
  rotation is a point map; the access contract is supplied; each countercontrol that widens the
  access breaks the correspondence.
- Finite carrier, a finite set of operations: the eight-point model
  (`operational-quotient-v3`), and the stabilizer fragments of apparatus-1 and MECH-1 under the
  posits P1 and P2, which are load-bearing for complete positivity there.
- Finite carriers of growing size, approximate, one qubit: `finite-a2-v5`, with the sphere
  model's contract kept.

In none of them is the access restriction derived from OI's stated principles. The sphere model's
ingredients are "supplied"; P1 and P2 are "new physical posits about control, access and
resources" (apparatus-1 §3.1); the eight-point contract is "not asserted to be the native
preparable set".

(iii) *Continuous mixing in the substratum.* One record constructs it from the lattice model's
update: B1, on one pair, under E-pair, E-real and E-control. Its object is a rotation of real mode
coordinates, written `exp(iθX)` on `z = x + iy`; it is a continuous family of bijections of an
infinite configuration space. Neither E-real nor E-control has a source: SM:222 states "The finite
bijection is fundamental; a real/complex wave operator is an observer-level lift whose derivation
must be stated separately" [P], ledger item (ii) posits a
finite total state space, and the coefficient is loaded from outside "with exact values". With the
access B1 and the bridge grant (point preparations, a sign read), the observer-level theory is not
a finite-dimensional quantum theory. The bridge states what is missing as a derivation: the
"observer/access quotient lemma". That lemma is the owner's third possibility stated as an
obligation: given continuous mixing in the substratum, derive which preparations and reads an
embedded observer has, such that its complete operational state passes a fixed finite-dimensional
state and effect test. The sphere model shows such a contract exists for one qubit; it is not
derived, and its carrier and rotation set differ from B1's (`S^2` with every rotation, against
`R^4` with one rotation axis). No record read connects the two.

(iv) *Which results assume what about access, on a finite carrier.* Lemma F and Theorem U2(ii) of
MECH-2 assume fixed-law attachments, H-LIFT and a fixed orthogonal (hence one-to-one) linear
frame, and nothing about the reads; U2(ii) concerns a branch acting as `p · Ad U` "with `p > 0`
independent of the input". Under those hypotheses fewer reads do not reopen tunability, for any
fixed bijection. Theorem NC, on noncontextuality, adds spanning preparations and reads, and that
hypothesis fails for the native reads at `q = 2`. Main:560 holds under every restriction of access
(B.7).

(v) *"No encoded reversible operation of infinite order" on a finite carrier has three causes
together.* (1) The dynamics is a bijection acting on probability laws (class 2). (2) The encoding
is one fixed orthogonal frame that contains every correlated cell (H-LIFT): a hypothesis about the
description, which belongs to none of the three classes and is the one an access restriction would
have to change. (3) The alphabet is finite (class 1, a posit). Affinity of the rule is not among
them: MECH-1's proof of Proposition C(b) uses nonnegativity of native laws and Gross's theorem (the
third review's reading of the proof text),
and MECH-2 node 8 states the extension to every fixed bijection, in two lines under the heading
"Odd `q` (conditional remarks)" of a file whose "Independent review … is a separate step".
Affinity is the cause of the stabilizer and complete-positivity statements (Theorem W,
Proposition AS) and of Lemma G2's grading.

(vi) *Negatives obtained under restricted access.* Each is a result for the construction named.

- apparatus-1 [R]: `q = 2`; the linear second-order step; posits P1, P2, P3 and E-iso; the
  one-cell frame R1. No encoded quarter phase (Lemma 5, adaptive corrections and any ancillas
  included), no encoded `rot`, no encoded dense control. Lemma 5 does not depend on the access
  posits; the reads and their continuation do.
- Q-A Lemma G2 [R]: `q = 2`; bipartite linear class; native `X` read; non-adaptive processes; a
  hidden sector of any size. No encoded quarter phase. The adaptive case is open.
- MECH-1 Theorem W and Proposition C [R]: odd prime `q`; the linear symmetric rule with the
  `−x(t−1)` memory term; posits P1, P2, P3 and E-iso, with or without NNB; Gross's frame;
  adaptive protocols included. Every protocol is a stabilizer instrument; every available encoded
  unitary is Clifford; no quarter phase; no Wigner-negative state; the reachable class is a
  noncontextual hidden-variable model.
- `operational-quotient-v3`, `product-section-v4` [R]: the eight-point carrier with the
  first-moment decoder. No non-Clifford rotation, with error at least 1/15 and 2/15 on the stated
  pairs.
- M-INACC-1 [R]: `q = 2`; the state-dependent ring `G_σ`; P1, P2. The protection of Lemma Q is
  lost.

(vii) *Where access could matter on a finite carrier.* For nonclassicality: equivalences coarser
than ontic equalities, held for a physical reason (M-INACC). Its nearest instance, Lemma Q(iii),
is conditional on two posited access restrictions and protects present values only; it is not
supplied by the state-dependent rule tested. On a fixed finite carrier a positive answer opens the
class of the 8-point quarter-phase mechanism (MECH-2 §6.2), where exact `rot` stays excluded
(apparatus-1 §5.3).

(viii) *Finiteness.* Nothing read assumes that finite access implies finite underlying dynamics.
G2, the countercontrol and GR's corollary are stated for hidden sectors of any size; MECH-2 §6.4
leaves the infinite case unassessed with the sentence "finite observer capacity does not imply a
finite world"; the two exact positives of (ii) and (iii) have finitely many observer outcomes over
an infinite underlying space.

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

**The same separation in the kernel's second interface** [K; native rounds OG-1, EFF-1, ORD-1 and
KTRANS-DENSE-1, with receipts and exact-head runs as their result notes report; not checked here].
The reconstruction rounds work with a convex body `Ω` of operational states in a real normed
space, a set `G` of affine automorphisms, and a completion body over a directed system of finite
stages (`StageCompletion`: preparation vectors in `ℓ^∞` over the stage effects, the body their
closed convex hull). In this interface the tunability premise is a hypothesis named K∞-R:

> `def BoundaryTransitive (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=`
> `  ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y`
> (OB/OrbitGeneration.lean:79–80)
>
> `def DenseBoundaryOrbit {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (Ω : Set V)`
> `    (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=`
> `  ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) '' G)`
> (OB/DenseOrbit.lean:53–55)

- *Exact form excluded for a countable family.*
  `theorem not_boundaryTransitive_of_countable {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} (hG : G.Countable) : ¬ BoundaryTransitive (eball 3) G`
  (OB/EffectSpace.lean:858–859). Scope: the 3-ball.
- *Approximate form not excluded, and strictly weaker.* `denseBoundaryOrbit_of_boundaryTransitive`
  (OB/DenseOrbit.lean:57); the countable family `ratRefl d` of reflections in rational hyperplanes
  has a dense boundary orbit on `eball d` (`denseBoundaryOrbit_ratRefl`, :359) and is not boundary
  transitive on `eball 3` (`not_boundaryTransitive_ratRefl`, :398). The result note: "`ratRefl` is
  a mathematical control, not an adopted family of operations."
- *What the approximate form buys.* "on the eleven consumers of the pairing table, a dense boundary
  orbit suffices wherever boundary transitivity was assumed, and it is a strictly weaker
  hypothesis" (KTRANS-DENSE-1 `result.md`): the ball theorems, the cone equality
  (`maxConeOf_avail_eq_of_dense`, :243) and the relative selectors. "The statements that need a
  specific effect to exist exactly keep exact boundary transitivity", and three statements are not
  covered (the Lorentz-cone bridge and boundary purity).
- *Finite orbits admit no drive.* `isEmpty_drivability_of_finite_orbits`
  (OB/OrbitNormalization.lean:124–127): a body every point of which has a finite orbit under the
  body's affine automorphisms admits no `ElementaryDrivability`; docstring: "a continuous flow
  cannot move a point inside a finite set".
- *Finite stages and order.* With
  `def InfiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop := ∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x`,
  `def FiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop := ∃ N : ℕ, 1 ≤ N ∧ ∀ x ∈ Ω, (⇑g)^[N] x = x`
  and
  `def StagePreserving (T : OpDatum D) : Prop := ∀ (i : D.ι) (x : (D.stage i).P), ∃ y : (D.stage i).P, T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩`
  (OB/CompositionOrder.lean:51–52, :55–56, :234–235):

  > `theorem finiteOrderOn_of_stagePreserving {S T : OpDatum D} (hS : AffineRespect S)`
  > `    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)`
  > `    (hsp : StagePreserving T) :`
  > `    FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)`
  > (OB/CompositionOrder.lean:348–351; contrapositive `not_stagePreserving_of_infiniteOrderOn`, :378–381)

  Hypotheses: a completion chart `C` (so the body has finite rank), two operation data that
  respect affine relations and undo one another, and stage preservation of `T`. Conclusion: the
  induced automorphism has finite order on the chart body. So an operation of infinite order on
  the completed body carries some stage's preparation out of that stage. Controls in the module:
  `not_ordInf_of_finite_of_mulClosed` (:109–110: a finite composition-closed set has no member of
  infinite order) and `infiniteOrderOn_rot3_one` (:418: the rotation of the ball by one radian has
  infinite order).

Scope of all five: each hypothesis is "stated as propositions and proved for no physical family"
(OG-1). KTRANS-DENSE-1: "This round does not show that OI, StageCompletion or the observer
architecture yields a dense boundary orbit or boundary transitivity; adopts no premise; introduces
no principle of closure of the operations". ORD-1: "Whether a composition-closed
boundary-transitive family in dimension ≥ 2 has a member of infinite order remains open"; "Nothing
here supplies an operation datum, finite rank, a completion chart or stage preservation from an OI
construction." No relation between this interface and `FiniteOperationalTheory` is used here; the
result notes read state none that bears on tunability. A search of `papers/*.md` for dense orbits, boundary
transitivity and infinite order returns nothing.

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

**What the research records have for approximation** [R; B.12]. Three statements, each for one
qubit under the sphere model's supplied geometry, reset and access contract, and none for OI's
rule.

- *A growing family approximates.* `finite-a2-v5`: for a fixed finite menu, horizon `h` and `ε`
  there is a finite carrier and a finite fair-bit bank within `ε`, in classical-quantum trace
  distance on complete records and outgoing states, of every adaptive protocol in the menu. The
  carrier grows with `1/ε` and with `h`.
- *One fixed finite controller of a stated class does not, in depth.* `a2_depth_v7`,
  `a2_memory_v8`: finite whole state, `B` fair bits per slot, a time-independent update; on one
  protocol the record law's distance from the quantum law tends to 1. A controller that keeps the
  distance bounded below 1 at every depth "needs the number of persistent states reachable within
  h slots … to grow without bound in h".
- *One fixed finite representation has an error floor.* `operational-quotient-v3`: at least 1/15
  for one rotation on the eight-point model; "It is not an A2 error floor for OI generally."

The records' own contract keeps the two targets apart (Gate A §3, B.12).

| Obstruction | (1) exact | (2) every ε, one fixed finite system | (3) growing family | (4) one fixed rule | (5) infinite underlying space |
|---|---|---|---|---|---|
| Sourced observer theory; every nonnegativity-bounded theory (B.5) | excluded [K] (`permTheory_not_control`; `falsifierUnavailable_of_nonnegBounded` for `rot`) | excluded [K], two-state carrier, as no dense unitary control (FrozenSourcing:173, :187, :240) | the invariant holds at every ancilla level and on every carrier [K] (`permTheory_nonnegBounded`); non-approximability is [K] only as no dense unitary control on the two-state carrier, where the approximant is a unitary conjugation at the same level; an approximant built with a larger ancilla and a discard is the [W] step of the scope sentence above (the second reviewer's check of it: a nonnegativity-preserving map has `(0,1)` entry ≥ 0 on the matrix unit where the target has `−1/2`) | excluded [K]: `sourcing_rule_independent` | not expressible in the kernel (`Fintype`). [R]: no full control from autonomous dynamics on any carrier (the time-shift group is abelian); no quarter phase from non-adaptive native processes with any hidden sector (B.12) |
| Monomial class with complex phases (B.1) | excluded [K] | excluded [W]: diagonal preservation is closed; the target differs from every diagonal-preserving map by `12/25` in one entry, and from every monomial unitary by `3/5` in operator norm. No kernel theorem | excluded [W]: the invariant does not depend on ancilla size | excluded [W] | [W] for weighted partial injections (B.1); not on `main` |
| B.2 as stated | no obstruction: vacuous hypothesis | no obstruction | no obstruction | no obstruction | no obstruction |
| B.3 / B.4 countermodels; `flow_endpoint_refuted` | non-entailment only | not addressed | not addressed | not addressed | not addressed |
| B.6 counting | excluded [K] | **not excluded**: with one postulated gate a dense countable class exists [K] | not excluded | not excluded: `fixedGateTheory 1` is dense for every ε [K], with a postulated gate and unbounded ancilla levels | not addressed |
| B.7 Main:560 | excluded for fixed `N` [P, P-imp] | excluded [W]: for fixed `N` and a fixed finite experiment the realizable behaviours form a compact set (the reviewer checked this argument) | **not excluded**; established with the stated limits [P] (Main:566, :598) | one map per `(𝓕, K, G)` (Main:582) [P]; one fixed finite rule for every ε is excluded by (2); one rule on an unbounded state space is not addressed on `main` | outside the hypothesis. [R] apparatus-1 §5.3: exact `rot` is impossible on a finite carrier and is induced by an imported continuum model for one system, with the measure a free choice |
| B.8 Main:488 | excluded for fixed finite `(S, prior, φ)` [P] | excluded for the whole instrument continuum [W] | not addressed | not addressed | outside the hypothesis |
| Encoded carrier, finite configuration set, fixed orthogonal (hence one-to-one) linear frame, H-LIFT (MECH-2, apparatus-1) [R] | excluded for every fixed bijection: encoded unitaries are frame symmetries, a finite group (MECH-2 §6.4) | excluded for the quarter phase under the one-cell frame: stochastic matrices are closed (apparatus-1:778–784); a finite group of encoded unitaries is not dense, for any fixed number of cells [W] | excluded under the product frame for every number of cells and ancillas (Theorem U2(ii)) | every rule | "not assessed" (MECH-2:910–911) |
| Linear class N with the posited access (P1, P2, P3, E-iso; with or without NNB), odd prime `q`, Gross's frame (MECH-1 Theorem W, Proposition C) [R] | excluded: every available encoded unitary is Clifford, a finite group, at each fixed `q` | excluded at a fixed `q`: the group is finite, and reachable states keep nonnegative Wigner functions (Proposition C(a), (b)) | cells and ancillas: excluded at fixed `q` (Proposition C covers every protocol). A family in growing `q`: not addressed; named and "left to Q-B (§6.5)" (:217) | the step is the lattice model's linear rule; which edge is armed at each tick is loaded from outside (P3); the access is posited | not derived. Named as Q-B's first test, "whether AS survives the real or large-`q` limit: exact continuous symplectic rotations of quadratures, with C-CP"; "A qubit `rot` would still need non-Gaussian, Wigner-negative resources" (:1073–1076) |
| Convex-body interface of the reconstruction rounds (OG-1, EFF-1, ORD-1, KTRANS-DENSE-1) [K] | boundary transitivity excluded for a countable family on the 3-ball; a drive excluded when every orbit is finite; infinite order excluded for a stage-preserving reversible datum | not addressed as such. A dense boundary orbit is not excluded for a countable family (`ratRefl`, a mathematical control) and suffices for eleven named consumers | not addressed: the completion body is the limit object; no theorem relates an approximating sequence of stages to the drive | not addressed: no hypothesis is derived from any rule | the body lies in `ℓ^∞` over the stage effects; the statements hold there under finite rank |
| Real two-mode carrier, amplitude coordinates `z = x + iy`, loaded coefficient (B1; bridge) [R] | constructed under E-pair, E-real, E-control: `exp(iθX)` for every real `θ` on one pair. With point preparations and a sign read, no fixed finite-dimensional quantum carrier represents the statistics | not addressed | not addressed: "Finite-alphabet versions or approximation limits do not automatically supply J_exact(A)" (B1 §8); "A finite-menu/precision approximation remains a separately named target" (bridge §7). The primitive is reversible over `Z_q`; what the word gives there is not derived in the record | the update is the lattice model's second-order form on an isolated pair; the angle is a loaded coefficient, so by the record's own ledger the tunability is supplied by E-control, not derived | this row is the infinite case: the underlying space is `R^4` per pair, an added input that ledger item (ii) excludes |
| Sphere model and its discretizations (`history-architecture-v5`, `finite-a2-v5`, `a2_depth_v7`, `a2_memory_v8`) [R] | exact for one qubit on the continuum sphere: every state, every rotation, every finite adaptive rank-one projective protocol, under the supplied contract | excluded in depth for a stated class on one protocol (finite whole state, dyadic fresh bits, time-independent update): the record law's distance tends to 1 | constructed for a fixed menu and horizon: `N = 6M²` labels and `(h+1)B` fair bits, with an explicit bound | no fixed OI rule: rotations, reset and reads are supplied primitives of an abstract model | exact case as column (1); the continuum, its measure and the access contract are supplied |
| Eight-point model with the first-moment decoder (`operational-quotient-v3`, `product-section-v4`) [R] | excluded beyond the 24 Clifford actions, for the stated decoder and preparation domains | excluded: error at least 1/15 (2/15 for product preparations) on stated pairs, for this representation | not addressed: "Changing which hidden preparations represent a quantum state, their conditional apparatus correlations, the decoder or the available interface changes premises of the calculation" | every stochastic kernel independent of the preparation label | outside the hypothesis |

[W] remark on column (4), not a claim to adopt: any computation-universal reversible rule on an
unbounded state space can approximate to every ε with the quantum data in the initial condition,
which is the reading Main:582 gives of its own construction. The linear rule of ledger item (vii)
is not of that kind.

Three readings follow from the table and are kept apart in sections D and F.

- *Configuration-basis reading.* "Quantum behaviour" means coherence in a matrix indexed by the
  substratum's configurations (the interface of B.1). Approximation is as excluded as exactness,
  and finiteness is not the reason. `operational-quotient-v3` records that this is a statement
  about the identification: "not a map-independent no-go for all operational quotients".
- *Observer-statistics reading, exact.* "Quantum behaviour" means that what an embedded observer
  can prepare and read has the statistics of a quantum system, the quantum state being a class of
  preparations the observer cannot tell apart. Exact reproduction of a qubit's full theory needs
  an infinite underlying space (Main:560 [P, P-imp]; apparatus-1 §5.3 [R]; the kernel statements
  above in their own interface). On an infinite space it is exhibited for one qubit by a supplied
  model (the sphere model) and constructed in its dynamical half from the lattice update under
  E-real and E-control (B1), where the unrestricted read fails. An exact claim about OI on this
  reading revises ledger item (ii).
- *Observer-statistics reading, approximate.* Approximation to every `ε` by finite systems that
  grow with `1/ε` and with the protocol's depth. Constructed twice at paper or record level: in
  Main with "the instrument data and … the state held in the hidden register" as input (Main:566,
  :582), and for one qubit from the sphere model's geometry (`finite-a2-v5`). Neither starts from
  OI's rule; whether a family in growing alphabet size built from the lattice update approximates
  anything is undecided on `main` (MECH-1 §1.4 leaves "The continuum form" to Q-B; the
  correspondence between alphabets "is not constructed here", SM §2.7). This reading leaves ledger
  item (ii) untouched.

The kernel's approximate target needs less than the exact one in both interfaces: a single
non-monomial gate at an irrational angle with the phases and exchanges, or a dense boundary
orbit, and not a continuum of operations. For the sourced theory both the gate and the phases are
excluded by the nonnegativity invariant, approximation included; for the monomial class the gate
is excluded by diagonal preservation.

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
| D1 infinite underlying space, finite access | Main:560, Main:488 (finite `N`); the `Fintype` typing of `FiniteOperationalTheory` | not expressible in `FiniteOperationalTheory`; in the convex-body interface the completion body is a limit object over finite stages, with no theorem sourcing a drive on it | configuration-basis reading: autonomous dynamics gives no full control on any carrier (the time-shift group is abelian); non-adaptive native processes give no quarter phase with any hidden sector; an infinite fair reservoir changes exact probabilities and no operation (`stopping-source-v2`, "not a kernel theorem for an infinite native substratum"); finite-stage reduction for continuous readouts of towers [R]. Observer-statistics reading: exact `rot` needs an infinite carrier (apparatus-1 §5.3); the sphere model reproduces one qubit exactly on a continuum with a supplied access contract (`history-architecture-v5`) [R] | E1 and saturation: an arbitrary measurable hidden carrier induces on a finite carrier only what a finite register induces, under H-IND | Configuration-basis reading: closed conditionally, at layer [K]/[P] for finite hidden parts, [R] for the three special infinite cases named, [W] and [D] for the general infinite case. Observer-statistics reading: open, and exhibited by a supplied model; open on OI's side only together with D2, D5 or D11. Revising it changes ledger item (ii) |
| D2 encodings that are non-linear, non-injective or chosen per measurement context | the fixed orthogonal (hence one-to-one) linear frame of MECH-2 Lemma F and Theorem U2 | not expressible | fixed orthogonal frames with H-LIFT are closed for every dynamics as to encoded unitaries (Lemma F, Theorem U2(ii)), with no condition on the reads. Worked non-injective instances: the eight-point first-moment decoder (finite; the 24 Clifford actions; error floor) and the sphere decoder on a restricted cone (continuum; every rotation) [R]. Coordinates read as amplitudes (B1): every angle, and the density dictionary fails with a sign read [R]. No finite carrier gives exact `rot` (apparatus-1 §5.3) [R] | E2: one shared linear encoding makes all native measurements jointly measurable; the continuum (Husimi) frame hosts every unitary as a point map and no sharp read | Open for non-linear and per-context encodings. As a class it contains "QM by fiat" (amplitudes as coordinates, the Born measure posited); the records' controls against that are the sign-record test and the supplied-measure test (B1 §6, B2 §4) |
| D3 memory outside the identified carrier | H-IND, H-LIFT, the uniform ancilla | not expressible (`prepAvail_uniform` only) | "Without H-LIFT … the encoded description must be enlarged until H-LIFT holds" (MECH-2:346–347); preparation-dependent lifts are outside the feedback result's H-C; Q-A's CP recovery "does not apply to an additional correlated or preparation-dependent hidden background by declaration" (PROOF-RECOVERY:24–25) | named route C-dyn, "not decided" | Open and unexamined for protocols whose hidden part depends on the input law; then no linear map on carrier states is defined |
| D4 limits and completions | finite derivations of `InstAvail` | nonnegativity passes to limits (`preservesNonneg_of_approx`) | towers: finite stage per horizon (ANALYSIS.md) [R]; quasilocal path "*additional structure*, chosen rather than derived" (Main:274) | E3 | Largely closed. Remaining: non-continuous readouts, infinite horizon |
| D5 sourcing that is not configuration-level | the choice of class | "say nothing about sourcings that do not" (OB/ManuscriptAxioms.lean, header); every lift formulation tested is configuration-level (`coherentLiftClass_eq_substratumClass`) | the observer-level wave lift is route S7 of the coherent-continuum source audit: "underdetermined until a carrier map and admissibility statement are supplied"; Main:590, "unresolved rather than excluded". B1 supplies a carrier map for one isolated pair (`z = x + iy`, `J = T_0`) under E-real and E-control and no admissibility statement; its read test fails the density dictionary. L3 lift: no map from amplitudes to the carrier is stated (F2-1 §3, G★) [R] | no admissibility criterion exists; the class is data | Open, and requires giving up "states are laws on a finite configuration set" or supplying an admissibility rule |
| D6 approximate target | — | excluded with exactness for the sourced theory | — | — | Not an opening |
| D7 restricted access on a finite carrier, as coarser operational equivalence (M-INACC) | H-LIFT and the one-to-one identification (Lemma F, Theorem U2); spanning reads (Theorem NC) | discard and `nonnegClass` cover the configuration-basis form: neither `rot` nor the phases | named missing premise. Nearest instance: Q-A Lemma Q(iii), "Under P1 and P2", which apparatus-1 §3.1 classes as "new physical posits about control, access and resources"; linear rule, `q = 2`; it "covers present active functionals only" (M-INACC-1 §9; past values are exposed by a one-tick protocol, §6.3). Negative for `G_σ` (M-INACC-1), in a unit that could not have returned a positive. With Lemma Q the quarter phase still needs NNB, yields non-CP reflections and fails two-system correlations. A supplied finite access quotient exists and gives the Clifford actions only (`operational-quotient-v3`) [R] | every partition and every fixed conditional prior is covered by T0 | **Open.** The finite-carrier form of the owner's class 3; the continuum form is D11. It concerns nonclassicality, not tunability: on a fixed finite carrier a positive answer opens the class of the 8-point quarter-phase mechanism, and exact `rot` stays excluded there. No source in OI's stated principles; the one instance rests on posited access |
| D8 adaptive native processes | non-adaptivity in Lemma G2 | not addressed | "Adaptive native processes are not covered" (Q-A §0, §4.3); the combined target with CP is excluded for uniform linear encodings (feedback result); record feedback is covered at odd prime `q` (MECH-1 Lemmas S, G; Proposition C) and in the one-cell frame at `q = 2` (apparatus-1 Lemma 5); adaptive gradedness at `q = 2` is open (MECH-1 node 5) [R] | — | Open in a bounded sense, at `q = 2` only |
| D9 time coarse-graining, stopping times | — | products of admissible operators | — | covered by T0 | Not an opening |
| D10 Q-B: a principle producing continuous rotations | the finite alphabet in MECH-1 Proposition C; the finite carrier in apparatus-1 §5.3 and MECH-2 §6.4 | not expressible in `FiniteOperationalTheory`; in the convex-body interface the corresponding hypotheses (drive, K∞-R) are unsourced | posed and open (apparatus-1 §5.7), with two named first checks. (1) "exact continuous symplectic rotations of quadratures, with C-CP" (MECH-1 §6.5). Its dynamical half is worked for one pair in B1, conditionally on E-pair, E-real and E-control; its law-level half, complete positivity in one fixed frame under the access posits on a real or large alphabet, is "not derived here". (2) "Whether a native reciprocal read on a continuum cell with a symplectic area form … produces the cosine-weighted re-preparation law without a supplied measure" (apparatus-1 §5.4). The ball-containing carrier with that law exists as a supplied model (`history-architecture-v5`); what is underived is the law "without a supplied measure", a native read and reset, and the composite extension. The exact finite form at odd prime `q` was tested: a finite Clifford group, a stop (MECH-1). Controls named in Q-A §4.4 [R] | per-site continua are the setting of SUBSTATE-BRIDGE-1 r2: "an infinite hidden carrier adds no single-procedure map" under H-IND; route R1, a non-linear encoding on a connected continuum, "fails hard-to-vary as stated" | **Open; neither first check is run as stated.** Q-B asks for an "additional OI principle", so an answer is a new premise unless the principle is derived. Its record expects a qubit `rot` to need more than quadrature rotations. The exact form revises ledger item (ii) |
| D11 an access quotient on a carrier with continuous mixing | the finite configuration set (Lemma F); the unrestricted preparations and sign access of the bridge's Proposition | not expressible | "The next missing physical statement is an **observer/access quotient lemma**" (`whole-model-bridge.md` §7). Negative control: point preparations with a sign read, no fixed finite-dimensional quantum carrier. Positive control: the sphere model's cone, sign read, re-preparation and privacy, all supplied. "Such a physical restriction must be sourced independently; this paper neither assumes it nor selects a replacement candidate" [R] | — | **Open; posed on `main`; not started.** The continuum form of the owner's class 3. Every exact form sits on a real-valued carrier (E-real, unsourced; ledger item (ii)). A finite or approximate form is not posed in any record read |
| D12 approximation by finite systems of growing size, from ingredients other than the quantum rule | "one fixed finite system" in column (2) of section C | dense unitary control from one postulated gate [K]; dense boundary orbit as a hypothesis [K] | for one qubit, a fixed menu and horizon: constructed from the sphere model's geometry (`finite-a2-v5`), with reset, access and clock supplied; a fixed finite controller of a stated class fails in depth on one protocol, and the least growth that suffices is open (`a2_memory_v8`). From OI's rule: a family in growing alphabet size is named and not built (MECH-1 §1.4, §6.5; SM §2.7) [R] | — | Open on OI's side. It leaves ledger item (ii) untouched. The records' contract forbids replacing a failed exact target by it after the fact (Gate A §3) |


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
is done above, within the reading limits of Appendix G.

**Recommendation.** Hold Step 2. No mechanism survey. Two owner decisions, in order: (1) which
reading of "quantum behaviour arising" is the target, and whether the exact or the approximate
form is meant (F.2); (2) whether to activate one question that `main` already poses, as a
paper-only unit whose decision rule and controls are fixed before any work. Under the owner's
standing instruction not to adopt an infinite substratum, the question nearest the owner's third
possibility, the access quotient, can be taken up only as a conditional derivation that carries
real-valued sites and an externally loaded coefficient as named unsourced hypotheses into every
conclusion; if that form is not wanted, TUNE-1 stops at Step 1 and the tables above are its
result.

The grounds follow, in the order: why no survey; the open questions as `main` states them; the
candidates compared; why hold; the controls.

**A survey of mechanisms is not supported.** Issue #1236 names the Step 2 candidates as
"recursive substates, vector- or complex-valued states, and the two-slice complex structure
(#1217)". Each has a record on `main`.

- *Recursive substates.* SUBSTATE-2 and its units (B.12): finite stage at each horizon for
  continuous readouts; classical memory in the models examined; `NATIVE-PADIC-1`'s no-backflow
  for the linear rule. In the kernel's second interface, an operation that preserves each finite
  stage has finite order on the completed body (ORD-1).
- *Vector- or complex-valued states.* B1 and the bridge: real mode pairs read as complex
  amplitudes give every mixing angle under two unsourced additions, and fail the read test.
- *The two-slice complex structure.* B1's `J = T_0` is the complex structure of one isolated pair
  at zero coupling, built from the two time slices; the single coupled step does not commute with
  it, and the 24-step word is built to return to it. Issue #1217 (not on `main`; provenance) poses
  the six-link case, with the open question whether "the second-order phase space of the
  real-lift update suppl[ies] a canonical J".

By B.11 and section C the operative obstruction on the configuration-basis interface is not
finiteness and not restricted access, and it covers approximation. By B.12 every positive exhibit
obtains its quantum behaviour from a supplied access contract. A survey would re-list these
records.

**The open questions, as `main` states them.** They state one gap at different levels.

| Where | Statement |
|---|---|
| Programme map (`PROGRAMME.md`, Arc D) | "The crucial question for F2 is which physical principle, added to OI and separately motivated, sources it together with valid measurements and compatible state transformations, and what that principle predicts beyond the resource it is introduced to supply." |
| `whole-model-bridge.md` §7 | "The next missing physical statement is an **observer/access quotient lemma**: derive, from independent physical premises, which preparations and coupled readouts are available, and why their complete operational state can pass the required finite-dimensional state/effect test." |
| `two-mode-drive.md` §8 | "The next scientific decision should address the physical status of these explicit inputs and the readout quotient, rather than reprove the already available control/characterization theorems." |
| apparatus-1 §5.7, Q-B | "What additional OI principle could produce the continuous rotations (§5.3)? This means a ball-containing carrier whose reads re-prepare with the cosine-weighted law, without a supplied measure, and whose composite extension respects Main §3.3." |
| Coherent-continuum source audit, route S7; Main:590 | the observer-level wave lift is "underdetermined until a carrier map and admissibility statement are supplied"; "unresolved rather than excluded" |
| Coherent-continuum source audit, route S8 | the continuously tunable coupling is "**not part of the current axioms**; a future physical extension, not a current source" |
| OG-1, ORD-1, KTRANS-DENSE-1 | "a source … for the drive and its boundary transitivity on the completion body (K∞-R)"; "a source of reversible operation data, of finite rank or of stage preservation in an OI construction; the drive and its continuity" |
| `states-dynamics-audit-20261024/REPORT.md` | "the outstanding step remains sourcing an operation/state correspondence that actually changes a load-bearing A1 premise, or establishing a stated A2 endpoint under permitted resources" |
| MECH-2 §6.2, M-INACC (nonclassicality) | "For each encoded system there is an ontic functional with three properties: the fixed rule uses it, so later statistics depend on it; no permitted preparation, read, reuse or recombination determines it or changes its conditional law; its inaccessibility follows from a structure stated without reference to the quantum target." ("conditional extension premise, not adopted") |

Not posed as a question in any record read: input-correlated memory (D3).

**The candidates compared.** Three of the statements above are specific enough to be a unit.
Rows marked [W] are the writer's reading of the tables.

| | Access quotient (bridge §7; D11) | Q-B (apparatus-1 §5.7; D10) | M-INACC (MECH-2 §6.2; D7) |
|---|---|---|---|
| The missing thing | a derived restriction on preparations and reads under which a carrier with continuous mixing has a finite-dimensional quantum state space | a principle giving continuous rotations and the cosine re-preparation law | operational equivalences coarser than ontic equalities, held for a physical reason |
| Already worked on `main` [R] | the drive, for one pair (B1); the negative control with unrestricted access (bridge); a positive control with a supplied contract (sphere model); one conditional detector (B2, B3) | the dynamical half of MECH-1's first check, for one pair (B1); the ball-containing carrier as a supplied model; the exact finite form at odd prime `q` (a finite Clifford group) | Lemma Q(iii) under P1 and P2 for the linear rule at `q = 2`; one negative for the ring `G_σ`; a supplied finite quotient with Clifford actions only |
| Underived | any restriction that is not chosen to obtain the target; E-pair, E-real, E-control; the measure; composites | the cosine law "without a supplied measure"; a native read and reset; complete positivity in one frame on a real or large alphabet; the composite extension | a rule under which the protection survives; the access posits themselves |
| What a unit could decide [W] | for the stated carrier and drive: whether a stated family of restrictions, each written without reference to quantum probabilities, passes the fixed-dimension state and effect test and survives the access countercontrols; or that none of the stated family does | whether the linear class on a real or large alphabet keeps complete positivity in one frame under P1 and P2 | whether a stated rule keeps a quantity it uses out of the observer's reach under P1 and P2 |
| What it could not decide [W] | where real-valued sites or a loadable coefficient come from; the composite and lift-seam obligations of the programme map; all restrictions outside the stated family | the source of a real carrier or adjustable coupling; a qubit `rot` ("would still need non-Gaussian, Wigner-negative resources"); nonclassicality | tunability: on a fixed finite carrier exact `rot` stays excluded (apparatus-1 §5.3) |
| Kind of work | paper derivation | paper derivation; the owner's Q-B record says a computational part would run as a V3 round and that the target decision "does not authorize execution, adopt additional physical premises, or bypass V3" (Issue #1169, comment 6712409082, amaybaum, 2026-11-07T20:08:39Z; provenance, not on `main`) | paper derivation for a stated rule; the first check "can be decided for a fixed small ring and bounded protocol depth" (MECH-2 §6.3), which would be a computation |
| Exact form and ledger item (ii) | on a real-valued carrier. As a conditional derivation with E-real and E-control carried into the conclusion it adopts nothing; as a statement about OI it is a Layer-0 revision under §A.29, which the owner has said not to adopt | as the previous column | finite carrier; ledger item (ii) untouched |
| Approximate form (finite substratum) | not posed in any record read. B1 notes the primitive is reversible over `Z_q` and derives nothing there | a family in growing alphabet size, named and not built; needs the correspondence between alphabets that SM §2.7 says "is not constructed here" | not what the premise addresses |
| New-premise risk | the restriction is the answer if it is chosen and not derived: "It cannot simply identify states that an available sensor distinguishes" | the question asks for an "additional OI principle" | the premise is "not adopted", "easy to vary" and flagged CC-RECON if adopted only to reach the target |

Relation between the first two [W]. They concern one object from two sides. Q-B's first named
check asks for rotations and their law-level form; the access quotient asks which preparations
and reads make a carrier that already has rotations into a quantum system. After B1 the rotations
exist conditionally, so what remains of Q-B's first check on a real carrier is an access
statement. Q-B's second check, the cosine law "without a supplied measure", is an instance of the
access quotient for a ball-containing carrier. Route S7 is the same object stated as a missing
carrier map and admissibility statement. Whether these are one unit or several is for the owner;
this document does not design the unit.

**Why hold, and on what.**

1. *The target reading is undecided* (F.2). On the configuration-basis reading the answer to the
   owner's question is already on `main`: excluded, exactly and approximately, for a class-2
   reason. On the observer-statistics reading the exact and approximate forms lead to different
   units.
2. *Every exact form of the tunability questions sits on a real-valued carrier.* That is the
   infinite underlying space the owner has said not to adopt as a premise. A conditional paper
   derivation is compatible with that instruction only if E-real and E-control appear in every
   conclusion as unsourced hypotheses; the owner decides whether such a result is wanted.
3. *The approximate form on a finite substratum is the form compatible with ledger item (ii), and
   it is the least developed.* No record read builds a growing family from the lattice update, and
   its first obligation, a correspondence between alphabets, is unbuilt.
4. *The answer is at risk of being supplied.* In every positive exhibit the access contract, the
   measure or the coefficient is put in by hand. A unit without a decision rule and a
   supplied-measure control fixed in advance would add one more such exhibit.

M-INACC is not recommended as the next question: it is not a tunability question, no second
candidate rule is named in the records read, and the unit that tested the first one could not have
returned a positive (PROT-R′ "is not adopted").

**Controls.** The list below is a proposal drawn from the records' recorded failures. It is not a
fixed protocol: it has no decision rule, and the owner's Q-B record asks for "a specified
observational precision and finite experimental horizon" and for error control under repetition,
adaptive measurement and recombination. Before any unit starts, the following would have to be
fixed (§A.29).

1. *A decision rule stated before the work*: the outcome classes, the family of restrictions or
   constructions quantified over, and for an approximate claim the metric, the error and the
   horizon (Gate A §3; `states-dynamics-audit` REPORT, endpoint 2).
2. *Supplied-measure control* (B2 §4; Q-B's "without a supplied measure"). Report every measure,
   response function and seed law that enters, and whether the result survives a second law with
   the same symmetries (B2's density `6q(1−q)`). If it does not, the verdict is "supplied, not
   derived".
3. *Sign-record control* (B1 §6; bridge Lemma 1). State whether a read that separates `z` from
   `−z`, or any read giving more than `d` pairwise perfectly distinguishable preparations, is
   available, and by what stated reason it is absent if it is.
4. *Access countercontrols* (`history-architecture-v5`, `operational-quotient-v3`). Exposed seeds,
   retained workspace, a state-dependent completion time and an unreset carrier each break the
   supplied contracts; a derived restriction must exclude each for a stated reason.
5. *Finite-menu control* (bridge §5). Any finite list of preparations is representable on some
   `C^N`; a positive result must hold for one fixed dimension over the whole admitted family.
6. *External-control check* (MECH-1 SC-2, Lemma A; B1 E-control). State which coefficients are
   loaded from outside. If the angle is a loaded coefficient the tunability is supplied.
7. *Classical-imitation control* (MECH-1 CC-IMIT′). Report whether a noncontextual model
   reproduces every sequence.
8. *Selection controls* (Q-A §4.4; MECH-1 C-CP, C-COMP): every encoded branch completely
   positive; Lemma R's reflections absent; the Mermin–Peres parity constraint and the composition
   battery for composites; the programme map's lift seam.
9. *Limit control.* At each fixed finite alphabet the construction reproduces the finite result
   (a finite group), so that a limit is not built in; the correspondence between alphabets is
   stated before it is used (SM §2.7); the condition `3 ∤ q` and the `−x(t−1)` memory term
   (Main:726 item (xiii)) are carried.
10. *Exact form only.* The §A.29 list: the results the revision preserves (the recurrence step
    needs finite `S`, GR:142; the finite-horizon equivalence; Lemma 3's counting measure) and at
    least one independent prediction. None is identified here.
11. *Which first check is meant*, where a record names two (MECH-1 §6.5; apparatus-1 §5.4).

### F.2 The prior decision for the owner, in plain terms

**Question 1. What has to look quantum?**

- (A) *The world's configurations themselves.* The quantum state is a table of numbers over the
  world's configurations, and mixing must appear in that table. On `main` this is ruled out for a
  world that only reshuffles configurations, exactly and approximately, at any size. If (A) is
  the target, TUNE-1's answer is "no, because of the reshuffling restriction read through this
  identification", and no further step is needed.
- (B) *What an embedded observer can prepare and measure.* The quantum state is a summary of the
  observer's information about hidden configurations. Under (B) reshuffles can act as quantum
  operations, and the question becomes which preparations and readouts the observer has, and why.

**Question 2, if (B). Exact or approximate?**

- (B-exact) Every rotation, exactly. This needs an infinite underlying world. The owner has said
  not to adopt that as a premise; a result of this kind can only be stated as "if sites held real
  numbers and couplings were adjustable from outside, then …".
- (B-approx) As close as desired, with finite systems that grow as the precision grows. This
  keeps the world finite. Nothing on `main` builds it from OI's own update.

For Q-B the owner has recorded a target that orders the two (Issue #1169, comment 6712409082,
amaybaum, 2026-11-07T20:08:39Z; provenance, not on `main`): "exact quantum rotations as the
ultimate target for Q-B, while allowing observer-resolution approximations as an intermediate
research milestone"; "Full OI–QM equivalence | Not established by approximation alone"; "Error
control: Quantify how approximation errors behave under repeated operations, adaptive measurements
and recombination. Small single-step errors are not enough"; "OI's finite observer capacity does
not necessarily imply that the underlying world is finite." The decision asked here is whether
TUNE-1 takes the same ordering, and how it combines with not adopting an infinite substratum: on
the records read, the two are compatible only if an exact result is stated conditionally on
real-valued sites, with that hypothesis named in the conclusion.

**Question 3, if (B). What counts as enough?** One quantum bit, or composites as well; and whether
rotations of two wave amplitudes, which a classical model also has, count toward the target before
a readout rule is derived. The records expect a single-system result to leave composites open and
expect a qubit rotation to need more than amplitude rotations.

The corpus does not settle these, and the answers change which obstructions bear and which
question, if any, is worth activating.

### F.3 Findings: prose on `main` versus the Lean statement

1. **Main:590 cites `readWriteSourced_not_qm`** for "finite reversible read-write dynamics,
   even with genuine hidden-memory and readback behavior, does not itself generate quantum
   state mixing". The theorem's hypothesis is unsatisfiable (B.2) [W; recorded as vacuous in
   [R] records on `main`]. The structure `ReadWriteFamily` has no hidden memory or readback in
   it; the countercontrol is a two-valued family. *Prose says more than the Lean statement
   supports.* Non-vacuous witnesses exist: `obs_not_qm`, `permTheory_not_qm`,
   `bijectionLevel_not_layerFlowExecutable`, `monomialSource_not_qm` (on `Fin 2`). The same citation occurs
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

Productivity test, fixed before the r4 reading: a finding counts if it changes a cell of B.11, C
or D, or a clause of the recommendation.

- The r4 additions (B1, the bridge, the sphere model and its discretizations, the eight-point
  quotient, the second kernel interface, the programme map's question): **ELABORATING**. The
  content is in records on `main`; the sorting against the owner's three classes and the five
  columns of section C is the addition. They change four statements of the recommendation and add
  rows to B.11, B.12, C and D.
- Restricted access as the ingredient of every positive exhibit, and unrestricted access as the
  cause of the bridge's obstruction: **ELABORATING** [W]; each half is stated in its own record.
- B.12 and the D7 and D10 rows; the r3 changes: **ELABORATING** and **CONFIRMING** as recorded for
  r3, checked there against apparatus-1, MECH-1 and MECH-2.
- Three invariants in place of one; the cardinality step in `submonomial_monomial`; the [K]
  status of the approximation cell: **CONFIRMING** (first review).
- `permClass_arch` has no cardinality step, so the nonnegativity route is cardinality-free up to
  the typing of matrices: **ELABORATING** [W].
- Finding 1: **CONFIRMING** (#1188). Finding 2: **BORDERLINE**; not checked against prior audits.

Assumption-watch markers for other units:

- A kernel non-availability theorem about a generated theory is a statement about the chosen
  class and interface; before it is cited as a statement about the substratum, the sourcing map
  has to be named.
- A positive exhibit of quantum statistics from deterministic hidden dynamics is a statement about
  its access contract; before it is cited, each of the contract's clauses (admitted preparations,
  reads, privacy, timing, measure) is classed as derived or supplied.
- A list of records read is not an inventory. Three review rounds of this unit each found a
  relevant record on `main` outside the list; Appendix G is built by search first.

No correctness band moves (§A.23): this unit relabels and sorts existing results.

***

## Appendix G. Inventory of records consulted

### G.1 Method and counts

Scope searched at the pin: `verification/` (2,899 files, 778 of them Markdown; 1,436 files and 449
Markdown files under `verification/programmes/oi-qm/`), the Lean tree
`verification/lean-mathlib/OIBridge/` (240 modules) and `papers/*.md`.

Each Markdown file was scored by two keyword families, case-insensitively.

- *Family 1*: `tunab`, `continuously`, `rotation`, `exp(i`, `real-valued`, `real coefficient`,
  `real coordinate`, `two-mode`, `large alphabet`, `large-q`, `infinite order`, `Q-B`,
  `DenseBoundaryOrbit`, `KTRANS-DENSE`, `dense`, `Clifford`, `p-adic`, `continuum`, `irrational`.
- *Family 2*: `quotient`, `inaccessib`, `coarse`, `substate`, `tower`, `restricted`,
  `partially accessible`, `finite access`, `infinite (carrier|substrat|hidden|alphabet)`,
  `uncountabl`.

The words `phase`, `complex`, `access`, `limit` and `drive` from the brief match nearly every
record and were used only inside the phrases above. 343 files have at least one hit in family 1
or three in family 2. They are classified below. Rows are records or record groups, with the
number of Markdown files in each; code, JSON, logs and review scripts in a record's directory are
classed with the record and were not opened. The 435 Markdown files below the threshold were not
opened. For the groups classed "not relevant" the classification rests on the path, the title and
a second search for the narrower terms `tunab`, `continuously (tun|driv|mix)`, `exp(i`,
`real-valued`, `two-mode`, `infinite order`, `Q-B`, `dense (orbit|unitary|control)`, `Clifford`,
`p-adic`, `large alphabet`, `access quotient` and `operational quotient`, whose hits were read in
context; their headers and outcome sections were not all opened, and the row says where they
were.

Classes: **relevant** (bears on tunable mixing, on real- or complex-valued or infinite carriers,
on an access quotient, or on exact against approximate); **context** (bears on what an observer
can prepare or read on a finite carrier, or on the interface, without bearing on tunability);
**not relevant** (one-line reason).

Counts: 76 relevant records on `main` outside the Lean tree: 39 read in full, 35 read in part and
2 not read (the preregistrations of KTRANS-DENSE-1 and ORD-1, whose result notes were read) (G.3);
17 kernel modules, 5 read in full and 12 at the cited statements; 2 off-`main` drafts read in
full.

### G.2 Relevant records

"Full" means every line was read, in this revision or an earlier one as marked.

| Record (path under `verification/` unless stated) | The record's own outcome or status | Read |
|---|---|---|
| `programmes/oi-qm/reconstruction/oi-qm-ext-1/two-mode-drive.md` | "a conditional amplitude-control component together with a concrete readout/dictionary obstruction and named physical sourcing gaps" | full (r4) |
| `…/oi-qm-ext-1/whole-model-bridge.md` | "The first state/readout bridge fails for the candidate specified below"; next missing statement: the observer/access quotient lemma | full (r4) |
| `…/oi-qm-ext-1/measurement-source.md` (B2) | "a conditional one-shot implementation plus a candidate-scoped instrument obstruction and named physical-source gaps" | full (r4) |
| `…/oi-qm-ext-1/measurement-exchange.md` (B3) | "UNSOURCED at the inherited and first new physical gates" | full (r4) |
| `…/oi-qm-ext-1/endpoints.md` (Gate A) | definitions and obligations; "no new equivalence theorem or physical mechanism is established" | full (r4) |
| `…/oi-qm-ext-1/README.md` | guide to the collection; "the recorded no-candidate outcome, not an impossibility theorem for OI" | full (r4) |
| `…/oi-qm-ext-1/observer-interface-source.md` | "bounded no-candidate assessment" (README) | part: head, §§4–7 |
| `…/oi-qm-ext-1/pair-operation-source.md` | "no identified change of operational interface and no derived available quantum operation"; "a source stop" | part: §§1–3.2 |
| `…/states-dynamics-audit-20261024/REPORT.md` | "Consistency axis only"; the A1 cardinality obstruction is not removed; four endpoints | full (r4) |
| `…/states-dynamics-audit-20261024/CURRENT-HANDOFF.md` | "internally reviewed research. None of them establishes native availability, probability selection, premise or access adoption, or full OI-to-QM equivalence" | full (r4) |
| `…/history-architecture-v5/{PLAN,REPORT}.md`, `review/REPORT.md` (3) | "A continuous positive qubit interface that passes the non-Clifford test"; review "Accept within the stated scope" | full (r4) |
| `…/finite-a2-v5/REPORT.md` | "conditional A2 reproduction for the stated single-qubit projective/unitary finite-menu/horizon class" | full (r4); `PLAN.md` first 60 lines |
| `…/a2_depth_v7/REPORT.md` | `NO_DEPTH_UNIFORM_COMPLETE_RECORD_BOUND_FOR_THIS_EXTENSION` | full (r4) |
| `…/a2_memory_v8/REPORT.md` | `BOUNDED_STATE_CLASS_NO_ESCAPE` | full (r4) |
| `…/operational-quotient-v3/REPORT.md` | "passed a useful positive test and failed the next operation-coverage test under an explicit contract" | full (r4) |
| `…/operational-quotient-v3/product-section-v4/REPORT.md` | "Product preparations do not remove the fixed-map operation obstruction" | part: result and the first three sections |
| `…/stopping-source-v2/REPORT.md` | an infinite fair reservoir with almost-sure stopping; "does not yet supply A1" | part: through the joint-record section |
| `…/a2_efficiency_v6/REPORT.md` | executed finite-menu certificate, horizon three | part: head; its summary in the handoff |
| `…/a1_reset_v6/REPORT.md` | "Fixed continuous vectors do not supply a reusable projective reset" | part: head; its summary in the handoff |
| `…/native-code-bridge-v6/REPORT.md` | a calibration bridge and a limit of the twelve-code carrier | part: head; its summary in the handoff |
| `…/round-ktrans-dense-1/result.md` | `KTRANS-DENSE-1-READ`; three cells proved | full (r4); preregistration not read |
| `…/round-ord-1-composition-order/result.md` | `ORD-1-COMPOSITION-ORDER-PROVED` | full (r4); preregistration not read |
| `…/round-og-1-orbit-generation/result.md` | `OG-1-INFRASTRUCTURE-PROVED` | part: head, the B1/B5 items, "What stays open" |
| `…/round-eff-1-effect-space/result.md` | `EFF-1-READ` | part: outcome line; the Lean statement |
| `programmes/oi-qm/PROGRAMME.md` | the strategic map; F1 retired for the stated architecture, F2 active | part: §§1, 3.1–3.3, Arc D, Arc F, 8, 10 |
| `…/apparatus-1-20261107/DESIGN.md` | merged after review rounds (as Q-A §6.1 reports) | full (r3) |
| `…/mechanism-1-20261107/DESIGN.md` | paper proofs; reviewed scope as MECH-2 cites it | full (r3) |
| `…/mechanism-2-20261108/DESIGN.md` | "Independent review of this file is a separate step" | full (r2, r3) |
| `…/quarter-phase-native-20261107/DESIGN.md`, `PROOF-RECOVERY.md` (2) | model-reviewed ACCEPT (author-recorded); C-CP recovered "Under R1 … non-adaptive product-ready instrument inputs" | full (r2; the recovery note completed in r4) |
| `…/minacc-1-20261108/{DESIGN,RESULT}.md`, amendments A1, A3 (4) | "WIP / UNVERIFIED"; outcome (B, B) | full (r2) |
| `…/minacc-1-20261108/amendments/A2-a1-confirmation.md` | amendment of decision rules | part: to §A2.2 |
| `…/quarter-phase-feedback-20261107/RESULT.md` | model-reviewed | full (r2) |
| `programmes/substratum/recursive-substates/` (`README`, `ANALYSIS`, F2-1 preregistration, A★, A★-1, run-2 result, FIXED-SCALE-1 report, NATIVE-PADIC-1 report) (8) | "Quantum … claims **OPEN**"; F2-1 `INCONCLUSIVE (gap)` | full (r2) |
| `programmes/substratum/continuous-substates/{README,operational-control-countercontrol,equivalence-and-d3-scope,later-access-result}.md` (4) | paper proofs "not independently reviewed on `main`"; `LA-EQUAL`, `EMPTY` | full (r2) |
| `audits/foundations/coherent-continuum-source-audit.md` | "outcome 2, no current source; the empirical extension remains" | part: census, outcome, "does not claim" |
| `audits/foundations/real-pair-flow-audit.md` | "outcome 2, reduction succeeds, sourcing fails" | part: outcome, "does not claim", scope correction |
| `audits/foundations/lift-source-audit.md` | no formulation that lands derives either target; the wave-operator lift underdetermined | part: outcome table |
| `programmes/substratum/frozen-sourcing-audit.md` | "outcome 3, the no-go" | part: outcome head, "does not claim", cross-reference |
| `audits/operational/stochastic-observer-interface-audit.md` | "outcome A, the interface gap" | part: question, outcome head, "does not claim" |
| `audits/operational/discrete-completion-audit.md` | "outcome 2, unitary density succeeds, instrument density stalls" | part: outcome head, "does not claim" |
| Eighteen audit notes that accompany kernel modules cited in sections A–C: `audits/foundations/{state-mixing-coupling,pair-flow-equivalence,polarization-closure,c5-discovery,lift,exec-source,flow-endpoint,flow-extension,derived-q3}-audit.md`, `MINIMAL-REPERTOIRE-AUDIT.md`; `audits/operational/{dense-instrument-bridge,quasilocal-completion}-audit.md`, `census-oi-compatible-theories.md`; `audits/physical-realization/continuous-time-audit.md`; `programmes/substratum/{route-b,source,interface,primitive-source}-audit.md` | verdict lines as found by search: state-mixing "outcome 1"; pair-flow-equivalence "outcome 1, both"; polarization-closure "split"; c5-discovery "C, underdetermined"; exec-source "negative for the stated access"; flow-endpoint "pass complete"; flow-extension "preregistered, no proof attempted"; dense-instrument-bridge "outcome 1, full dense-instrument success"; route-b "B0 and B1 complete"; the others carry no one-line verdict | part: header and section headings; the kernel statements are read at the Lean source |
| Kernel modules, full (r2): `FrozenSourcing`, `FlowEndpoint`, `F2CoherenceControls`, `RecursiveFiniteFactor`, `NativePadicReduction` | — | full |
| Kernel modules, at the cited statements: `DenseOrbit` (header, §A, statement list), `CompositionOrder` (header, definitions, four theorems), `OrbitGeneration` (:70–90), `OrbitNormalization` (:121–132), `EffectSpace` (:850–866), `StageCompletion` (header, `DirectedStages`), `CompletionAction` (`OpDatum`, `CompletionChart`); from r2: `StructuralClosure`, `SubstratumInterfaceAudit`, `PhaseSource`, `PC1Controls`, `InstrumentRealization` | — | part |
| Off `main` [D]: INTERVENE-1 r2 (`ea12fde1`); SUBSTATE-BRIDGE-1 r2 (`86a413c8`) | drafts; "r2 has not been re-reviewed" | full (r2; the second completed in r4) |
| Provenance, not on `main`: Issue #1236 (body), Issue #1217 (head of body), Issue #1169 comment 6712409082 | planning records and one owner decision | read as stated |

### G.3 Relevant records not read in full, and why

The reading for r4 was done in one session with a bounded context. Priority went to the records
the third review named, to the records those cite as controls, and to the result notes of the
kernel rounds. What remains:

- *Audit notes accompanying kernel modules* (24: the six read at their outcome sections and the
  eighteen read at their headings). Their theorem statements are cited from the Lean source. Their
  preregistration, test and scope-amendment sections were not read; a scope statement made only
  there is not reflected above.
- *Control planes of rounds whose results were read*: the preregistrations of KTRANS-DENSE-1 and
  ORD-1; the bodies of the OG-1 and EFF-1 result notes.
- *Package reports summarised in a handoff that was read in full*: `a2_efficiency_v6`,
  `a1_reset_v6`, `native-code-bridge-v6`; and the later sections of `product-section-v4` and
  `stopping-source-v2`.
- *Others*: `observer-interface-source.md` §§1–3; `pair-operation-source.md` §§4–7;
  `PROGRAMME.md` outside the sections named; M-INACC-1 amendment A2 after §A2.2.

### G.4 Context and not-relevant groups

| Group (Markdown files; of which keyword-matching) | Class and reason | Opened |
|---|---|---|
| `…/oi-qm-ext-1/` remaining seven notes: `physical-interface`, `preparation-loading`, `prepared-pair-source`, `two-system-interface`, `composition-source-map`, `probability-source-assessment`, `parallel-synthesis-20261107` | context: sourcing of preparation, pair preparation, Bell composition and probability on finite reference dynamics; each a conditional component or a source stop (collection README) | head of each; README in full |
| `…/observer-access-20261106`, `record-control-20261107`, `physical-controller-20261107`, `controller-preparation-1-20261108`, `correlation-recombination-20261107` (6) | context: one receiving interaction, one record-to-control candidate, controller sourcing, hidden-parity recombination, on the finite reference rule; "a local transfer equation, not the proposed quantum preparation and measurement interface"; "stop; no controller passes the physical source gate"; "source gate NOT PASSED" | head and stated outcome of each |
| `…/mathcon1-polc-20261108/DESIGN.md` | context: "Preregistration only"; "no derivation". The polarization closure it concerns is countable up to scalar in the kernel (`polC_countable_upToScalar`, cited in the coherent-continuum audit) | head |
| `…/physical-coupling-pc1/` (9; 5) | context: strict result `INCONCLUSIVE (void)`; not usable as a premise | README, run-2 result, disposition, heads (r2) |
| `programmes/substratum/continuous-substates/` 21 `native-*` units and 11 other notes, `la-equal-gap/` | context: setting-conditioned access on the native finite rule; conditional; none a no-go | opening and result lines (r2) |
| `programmes/substratum/wave-sign-20261108/ASSESSMENT.md` | context: the memory sign of the second-order rule; author checkpoint | :1–60 (r2) |
| `…/native-y-continuation-20261024/` (85; 18) | context: a native Y readout and reset on a finite twelve-code carrier; its relation to tunability is stated in `states-dynamics-audit` REPORT ("does not remove the existing A1 cardinality obstruction") | not opened; read through that REPORT |
| `…/composition-access-20261024/`, `physical-state-operation-compatibility/`, `bridge-compatibility-audit/` | context: composition contract; pair-cone preservation; no tunability statement | head of each |
| Reconstruction rounds other than OG-1, EFF-1, ORD-1, KTRANS-DENSE-1 (28 rounds): TRB-1, CMP-1, OPACT-1, KINF-1/2, DIM-1, K1-*, K2-GUARD-1, KTRANS-SEP-1/2, KTOKEN/PAIR-MAXCONE, PARITY-NOT-1, ODD-CHAR-1, RELC-SELECT-1, IIP-1, COMP-1, NB-1, BG-1/2/3, OI-CHANNEL-1, OI-FINITE-PROTOCOL-1, PRESERVE-INDUCT-1, ARP1-MARC, KT4-PREM-1 | not relevant to the three classes: they prove consequences of the hypotheses (ball, cone, dimension selector, composite interface) or audit premises; none sources a drive. KTRANS-SEP concerns a body on which the kernel properties hold without transitivity | outcome line of each result note |
| `…/k1-rdy-*`, `bsel-2-*`, `born-sel-b-measure-20261104`, `oiqmsel-*`, `observer-interface-obsmu-20261104`, `measurement-record-formation`, `o-ret-routes-20261103`, `oi-pseudoentropy-20261025`, `bekir-golomb-orientation-design` | not relevant: Born measure selection, record retention, ready-state supply, gauge relatedness, pseudoentropy; narrower search: one unrelated hit ("real-valued conserved energy") | not opened beyond titles |
| `programmes/oi-qm/track-b/` (99; 35), `track-i/` (17; 5), `interface/`, `h-bell/`, `amendments/` | not relevant: the Barandes correspondence route (indivisibility, Gram and orbit laws, lifts), representation boundary, Bell obligation. Act 8, "the continuous-extension round" (outcome `CE1`), concerns continuity in time of a stochastic family, not a tunable operation. Summarised in `PROGRAMME.md` §10, read | not opened beyond titles and the act-8 outcome line |
| `programmes/hydrodynamics/` (14; 14), `black-hole-information/` (17; 9), `physical-realization/` (10; 5) | not relevant: "continuum" there is the fluid or spacetime continuum; C4 storage and readback | titles; narrower search hits read |
| `audits/manuscript/` (104; 55), `audits/infrastructure/`, `audits/provenance-errata/`, `audits/evidence-pruning/`, `audits/physical-realization/` other than the continuous-time audit | not relevant: manuscript hunk dispositions, tooling, provenance; hits are "Clifford" in the Dirac-algebra sense and quotations of manuscript lines | titles; narrower search hits read |
| `audits/foundations/` and `audits/operational/` notes not listed in G.2 (16) | not relevant to tunability beyond the kernel statements already cited: scope propagation, scalar closure, instrument realization and migration, typed completion, phase-source and its propagation | titles |
| `programmes/substratum/` other notes: `a5-linear-affine-20261104`, `a6-*`, `lemma-24-1*`, `manuscript-axiom-audit`, `substratum` planning | not relevant: linear against affine dynamics, background independence, semigroup transfer | titles |
| `verification/infrastructure/` (51), `README.md`, `ROADMAP.md`, `MIGRATION-*.md`, `lean/ROADMAP.md`, `lean/VERIFYING.md` | not relevant: verification tooling, the frozen queue, indices | `README.md`:298 only (finding 1) |
