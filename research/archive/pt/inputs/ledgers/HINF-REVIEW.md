# Review of the infinite-dimensional (H-∞) assessment, against the base

Research review only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/`. Nothing is adopted, and no
round, ROADMAP or manuscript change follows from this note. Paths are relative to
`verification/lean-mathlib/OIBridge/` unless stated otherwise.

## Verdict

The assessment is accurate about what exists and about the independence of infinite-support availability. It is
wrong on three points:
- It conflates the H-∞ roadmap row with the instrument-availability question.
- Its proposed first target was already pre-registered, analysed and set aside by the project's own audit.
- It does not say that the whole Level III construction starts from complex matrix stages. It therefore inherits the
  conditionality of the K row: the native-premises programme that the EQ2 threads are working on.

## Confirmed

| claim in the assessment | what the base says | where |
|---|---|---|
| An infinite-region quantum observable algebra is constructed from compatible finite regions | The local algebra is the set of equivalence classes of finite-region observables. Its norm completion is a C*-algebra, equal to the closure of the union of the stages. Site type ι is arbitrary; regions are finite subsets | QuasilocalAlgebra.lean header (1)–(3); `instCStarAlgebraQuasilocal`; `closure_iUnion_stage` :712 |
| States are included | Every consistent family of density matrices extends uniquely to a state of the completion | `quasiState`, `quasiState_unique` :879 |
| Dynamics induced by the discrete system are included | The reversible finite-range substratum update extends to an isometric *-automorphism | `heisQ` :1264 |
| "Conditional on the finite-region structure" | Yes, and more precisely: it is a uniqueness theorem among systems with the substratum's matrix-algebra stages, up to canonical *-isomorphism and intertwining the dynamics. It is not a classification of all quasilocal C*-systems | QuasilocalCharacterization.lean header (3)–(4); `canon_unique` :359; `systemEquiv_dyn` :497 |
| Not every operation of infinite-dimensional QM is shown available | Correct | InstrumentCompletion.lean "What is not claimed" |
| Finite-region availability does not give infinite-support availability (independence) | `q3_countermodel` :335, valid for an infinite site type and a nontrivial site space. Its availability predicate `AvailFS` is exactly the finite-region Kraus instruments (`availFS_of_kraus` :237, `kraus_of_availFS` :242). It is closed under identity, composition, relabelling, coarse-graining and the OI dynamics, and leaves states and dynamics untouched (`states_untouched` :361, `dynamics_untouched` :370). It withholds the all-sites phase map (`phaseAll_not_availFS` :279). Scope: within the fixed-algebra interface; Level II's dimension-changing operations are neither modelled nor withheld | InstrumentAvailability.lean |
| Existence is not availability | This is the audit's own framing | instrument-completion audit, second entry |
| A Hilbert-space bridge is not in Lean | Correct. No representation is constructed or selected; a sector choice is a state-level input | quasilocal-completion audit, outcome B |
| Continuous time needs extra structure | Stronger than "open": the base proves that discrete dynamics does not determine a continuous interpolation, at operator level and at the visible level | RegionLimit `continuous_extension_not_unique` :296; ContinuousExtension `extension_not_unique_visible` :234 |
| Lattice spacing is fundamental; continuum predictions only to controlled accuracy | This is the corpus's own position: "the continuum is a calculational approximation with a quantified error"; `L²(ℝ³)` is not claimed as a physical object | RegionLimit header; quasilocal audit, freeze scope guard 2 |
| QFT is a separate programme | Correct | ROADMAP "Gauge/QFT extension" (long-range, conditional); P3 GR → Level-III states (OPEN) |

## Corrections

1. **H-∞ is not the availability question.** The H-∞ row (ROADMAP:70, :936–951) asks for "a scope-correct OI→QM
   statement beyond finite carriers": the whole finite characterization (composites, dynamics and selection) carried
   to infinite-dimensional or QFT systems. The row says in terms that "infinite-support instruments are a separate,
   deliberately unprioritized question … and do not close this obligation". The section "Deliberately not
   prioritized" lists them, together with representation selection and the continuous-time generator.
2. **The proposed first target is the audit's Q2, already analysed.** "Compatible, suitably bounded finite-region
   instruments extend uniquely to the completion" is pre-registered question Q2 of
   `verification/audits/operational/instrument-completion-audit.md`.
   - **Partial result.** Decided affirmatively for the star-endomorphisms of compatible weight families (`wtQ_mul`,
     `norm_wtQ`).
   - **The missing lemma is named.** A uniform norm bound for positive subunital branch maps (‖Φ‖ = ‖Φ(1)‖ on a
     C*-algebra), or a direct Kraus-form bound. Neither is in the kernel. Uniqueness is the easy half, by density;
     existence needs the bound.
   - **Classification.** After the corpus census (third entry: "no live claim requires an infinite-support
     intervention"), Q2 and Q4 are classified as "open, and outside the core programme … an optional mathematical
     extension".
   - **Consequence.** Prioritizing it would reverse a recorded adjudication. It should return only if a live claim
     starts to depend on it.
   - **Unformalized adjacent question.** "Valid quantum instruments on the completion" would also need the abstract CP
     class there, which is not formalized; its relation to the Kraus class is Q4, which is open.
3. **Level III's foundation is not field-neutral.** Level III concerns OI_Q: the quantum-completed substratum, i.e. OI
   plus continuous off-diagonal controllability. Its local stages are complex matrix algebras by construction (freeze
   scope guard 1). So every infinite-system statement sits downstream of the K row (field-neutral premises → finite
   complex kinematics). The EQ2 tracks are the upstream work. The H-∞ items do not unblock them, and a derivation of
   infinite-system QM (as opposed to a characterization) needs K first.
4. **The Level III statement is a uniqueness theorem, not a biconditional.** The §A.34 lesson records this: "nothing
   here derives the OI_Q conditions from the existence of such a system". The missing direction is the converse, from
   a quasilocal system to the OI_Q conditions. It is a natural H-∞ item that needs no infinite-support operation.

## A candidate the assessment points toward (for later; not proposed as a round)

The assessment's second target, "a two-way characterization of the infinite-region theory with a precisely defined
class of available operations", is the closest match to the actual H-∞ obligation. A scope-correct first version
needs no new availability principle:
- **The class of operations.** Finite-support availability, which Q1 identifies exactly with the per-region Level II
  Kraus instruments (`finiteSupport_iff_kraus`, InstrumentCompletion :195).
- **Forward.** OI⁺ at every finite region gives the quasilocal theory with finite-support availability (Levels I/II
  per region, plus Level III, plus Q1).
- **Converse.** A quasilocal system with these stages and finite-support availability satisfies OI⁺ at every region.
  This is the missing direction named in point 4, and the place to check it is §A.34.

Whether the per-region assembly is cheap has not been checked. A design-only pass would decide that.

## Bearing on the current plan

None of the above changes the EQ2 tracks or their order. For the derivation goal, the K row (finite, native) is
upstream of every infinite-system statement. The H-∞ candidate above can be designed at any time, because it does not
depend on the EQ2 results; but its value as a derivation depends on them.
