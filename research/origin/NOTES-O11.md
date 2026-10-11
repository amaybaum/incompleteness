# NOTES-O11 — the stage-crossing datum from the stated access

Thread `research/origin`, round 4, node O11. Base L = `9f9f8257`; kernel paths under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels as in NOTES-O1 ([K] kernel at L, [D] design module on a
dev branch, [W] written argument, [X] exact computation, [A] audited record, [L] literature named, not checked here).
Script: `experiments/o11_token.py`. Design module: `OIBridge/OriginTokenOrder.lean` on `dev-origin/token-order`
(cut from L).

**The question (HO-22 v1 item 5, (S1); HO-20 v1 item 3).** Does `genTheory` over the stated access — every
`InstAvail` protocol (`op`, `readout`, `coarse`, `bind`, `discard`), every ancilla block and relabelling of the class
— contain an infinite-order datum on the completed body of one token, or does every such datum have finite order?
HO-9 item 3 (O6-T1) answered it for passive repeatable finite-rank protocol towers; O11 asks it of the kernel's full
availability.

**The predicate, in the kernel's vocabulary (fixed before any computation).** For an implementation class `𝓘` with
an architecture and a finite carrier `T` (the token is `T = Fin 2`; level `n` is `Fin 2 × Fin n`):
- the configuration states `cfg s` (the point masses the substratum prepares);
- `Reach 𝓘 T`: the normalized branches `F a (cfg s) / tr` of every family with `InstAvail 𝓘 T O F`, every outcome
  type `O`, every branch `a` of nonzero weight, every configuration `s` — the states reachable from a configuration
  by one protocol, conditioned on one outcome (`bind` makes later protocols and conditioning part of one family);
- the completed token body `body 𝓘 T = closure (convexHull ℝ (Reach 𝓘 T))` in `Matrix T T ℂ` (a real vector
  space; closure and convex hull as the kernel's `StageCompletion.body` takes them);
- the data: the available unitary conjugations `X ↦ U X Uᴴ` with `InstAvail 𝓘 T Unit (fun _ => conjChannel U)`,
  as real affine automorphisms of `Matrix T T ℂ`;
- ORD∞ on the token body: `CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T)` — the kernel's own predicate
  (CompositionOrder.lean, §A): some available datum has `InfiniteOrderOn` the body.
The stated access is `RouteB.substratumTheory = genTheory substratumClass` (RouteB.lean:279; the monomial class,
which contains every diagonal unitary — the phase continuum) and its sourced subclass `permClass`
(SubstratumInterfaceAudit.lean:236; scaled partial permutations, no relative phases).

**Productivity test, fixed before starting (§A.31).** A finding counts only if it is strictly stronger than HO-9
item 3 ("passive finite-rank towers carry no infinite-order datum") and either (i) decides ORD∞ on the token body for
`genTheory` over the stated access with every `InstAvail` protocol, kernel-checked in design, or (ii) exposes what
(S1) restates — a hidden assumption in HO-22's split of the stage-crossing substratum's obligations into (S1)–(S4).
The obvious restatement "reachable states are diagonal, so data act as permutations" is a non-gem on its own.

**The suspected hidden assumption, recorded before any computation.** HO-22's (S1) asks for "an infinite-order
datum on the token" as if the datum were what the stated access lacks. On the kernel's matrix carrier the frame-axis
rotation `R_z(θ)` is conjugation by `diag(1, e^{iθ})`, a monomial unitary: it is in the substratum class for every
θ, `θ₀` with `cos θ₀ = 3/5` included, and it has infinite order on the full matrix algebra. If O11 finds every datum
of finite order on the token body, the obstruction is then not the datum's availability but the body: the datum
would be present and act trivially. Whether that is so, and what (S1) is then equivalent to, is what O11 decides.

## S0 — predictions, written before the first run of `o11_token.py` and before any dispatch (2026-10-11T03:18:03Z)

Design module `OriginTokenOrder.lean` (predicted to build with every declaration on
`[propext, Classical.choice, Quot.sound]`):
- **D1 (the stated access).** For every class whose members at `T` are submonomial and which has an architecture,
  every reachable state is configuration-diagonal (`reach_diag_of_submonomial`; instances `substratumClass`,
  `permClass`), the completed body is contained in the diagonal matrices, every available unitary maps each
  configuration state to a configuration state, and every available unitary datum has finite order on the body
  (`finiteOrderOn_of_reach_diag`, through the kernel's `exists_return` and `exists_common_period`
  [K CompositionOrder.lean:149, :171]). Hence `¬ OrdInf (body substratumClass T) (availData substratumClass T)` and the
  same for `permClass`, at every carrier, so at every level.
- **D2 (necessity).** For every architecture, ORD∞ on the token body forces a member of the class at `T` that is not
  submonomial (`exists_nonsubmonomial_of_ordInf`).
- **D3 (the frame-axis rotation).** The frame phase `diag(…, e^{i}, …)` is available in the substratum theory, acts as
  the identity on its token body, has infinite order on the ambient matrices (π irrational), and no finite set
  containing a coherent state is carried into itself by it (the finite-stage mechanism of
  `not_stagePreserving_of_infiniteOrderOn` [K CompositionOrder.lean:378], through `exists_return`).
- **D4 (the equivalence, one direction at a time, §A.34).** For every class: ORD∞ on the body ⇒ the body carries a
  coherent state (`coherent_of_ordInf`, no hypothesis on the class). For every class containing the frame phases at
  `T` (in particular every class extending the substratum class): a coherent state in the body ⇒ ORD∞
  (`ordInf_of_coherent`). The two give `ordInf_iff_coherent` under the phase hypothesis.
- **D5 (control).** On the full class the token body carries a coherent state (`rot(π/4)` applied to a configuration)
  and ORD∞ holds (`fullClass_ordInf`): the predicate is not vacuous.

Exact computation `o11_token.py` (every number exact; Q(ζ₁₆) with rational coefficients; levels one and two):
- **E1.** Substratum theory, levels one (2 states) and two (4 states): over the enumerated protocol families
  (monomial unitaries with phases from {±1, ±i, (3 ± 4i)/5}; register readouts with outcome-dependent monomial
  corrections, coarse-grained; uniform ancilla of size 2 attached, a monomial unitary on the doubled carrier, discard),
  every normalized branch applied to a configuration state is diagonal with nonnegative rational entries summing to
  one, and every point mass occurs. Predicted: diagonal in every case; all point masses reached.
- **E2.** Every enumerated available unitary datum acts on the configuration states as a permutation; at level one its
  period on the reached states divides 2, at level two it divides 12 (orders 1, 2, 3, 4 of S₄); after its period it fixes
  every reached state exactly.
- **E3.** The frame phase `diag(1, z)`, `z = (3 + 4i)/5` (the rotation `R_z(θ₀)`, `cos θ₀ = 3/5`), fixes every reached
  state of E1 exactly; on the coherent state |+⟩⟨+| its orbit has 200 distinct members, and `z` has minimal polynomial
  `5x² − 6x + 5`, not monic over ℤ (not a root of unity).
- **E4 (the extension).** Substratum class plus one balanced mixer (`rot(π/4)` at level one): the reached states
  include a coherent one (|+⟩⟨+|, off-diagonal 1/2) and the frame phase has infinite order there (orbit ≥ 200; the
  same certificate): ORD∞ holds exactly when coherence appears (D4, computed).
- **E5 (countermodel to "coherence ⇒ ORD∞" without the phase continuum).** `fixedGateTheory (π/4)` at level one: the
  level-one group has 192 elements and 24 channels, its reached states include the six octahedral pure states
  (coherent), and every one of the 24 channels has finite order (orders 1, 2, 3, 4). With O9-L1 [W] (these 24 are all
  the available unitary channels at level one), ORD∞ fails on a coherent body.
- **E6 (positive control at a rational angle).** `fixedGateTheory (π/8)` at level one: the word
  `rot(π/8) · S rot(π/8) S†` has trace `1 + √2/2` (minimal polynomial `2x² − 4x + 1`, not monic: infinite order), and
  its orbit of a coherent reached state has 200 distinct members: ORD∞ holds without the phase continuum.
- **E7 (stage crossing).** For the infinite-order data of E3 (ambient), E4 and E6, no orbit closes within 200 steps;
  for the finite-order data of E2 the finite set of configuration states is carried into itself.
- Countercontrols, each expected False: CC1 the diagonality test on E4's reached states; CC2 "a period ≤ 200 exists"
  for the frame phase on |+⟩⟨+|; CC3 the infinite-order certificate (minimal polynomial not monic) on the level-one
  word at π/4 (trace 1); CC4 "the frame phase fixes every reached state" on E4's reached states; CC5 "maps
  configurations to configurations" for the non-monomial `rot(π/4)`.
- **Addendum to S0, before run 1 (2026-10-11T03:34:48Z).** E8 (added to the script's rule before any run): every
  enumerated deterministic family of the stated access, restricted to the configuration states, is a column-stochastic
  matrix, and it has a nonnegative inverse exactly when it is a permutation matrix — the finite-carrier form of the
  written step for reversible data that are not unitary conjugations (§3). Predicted: so in every case. E5's rule
  counts the group-orbit states of the configurations: 6, of which 4 are coherent (±x, ±y). One library check was run
  before run 1, outside the script: sympy 1.14.0's `minimal_polynomial` on 2cos(π/8) written as a sum of exponentials
  (x⁴ − 4x² + 2) and on 1 + (ζ₁₆² − ζ₁₆⁶)/2 (2x² − 4x + 1), to confirm the function accepts such sums.

Run 1 of `o11_token.py` (2026-10-11T03:34:58Z): `VERDICT UNDECIDED (E8)`, every countercontrol False; the defect was the
script's own permutation test (columns only, so a reset counted as a permutation), kept as `o11_token.run1.*`. Run 2
(03:35:52Z), rows checked as well, decision rule unchanged: `VERDICT O11-FINITE-ON-STATED-ACCESS+ORDINF-IFF-COHERENT`,
every countercontrol False; replay byte-identical. Every S0 prediction met (E1: 3 and 10 reached states, all diagonal,
every point mass; E2: periods {1, 2} and {1, 2, 3, 4}; E5: 192, 24, orders {1, 2, 3, 4}, 6 states, 4 coherent; E6: trace
1 + √2/2, 2x² − 4x + 1; E8: 95/95, 399/399). Design module: workflow run 38108620996, Mathlib bridge job 114379324788,
Build success, 45/45 declarations on [propext, Classical.choice, Quot.sound] (§5).

## 0. Verdict — case (ii): on the stated access every such datum has finite order

1. **The predicate, in the kernel's vocabulary.** ORD∞ on the completed body of one token is
   `CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T)` — the kernel's predicate (I3.108) over the kernel's own
   availability (I4.26 `InstAvail`; genTheory, ImplementationLocality.lean:852, yielded by I4.32), with
   `body 𝓘 T = closure (convexHull ℝ (Reach 𝓘 T))` and `Reach 𝓘 T` the normalized branches of every `InstAvail` family
   (every protocol: step, readout, coarse-graining, feed-forward, discard; the class's ancilla blocks enter through the
   discard, `realized_of_instAvail`) applied to a configuration state [D, definitions].
2. **It is false on the stated access, at every carrier and so at every level** (`substratum_not_ordInf`,
   `permClass_not_ordInf`, `substratumTheory_datum_finiteOrderOn` [D]): every available unitary datum has finite order on
   the token body. More generally, for every architecture whose members at the token's carrier are submonomial —
   every configuration-level class (I4.242) — every reachable state is configuration-diagonal
   (`reach_diag_of_submonomial` [D]), every available unitary carries configuration states to configuration states
   (`eq_cfg_of_diag` [D]: a diagonal rank-one projector is a configuration state), and a common period of the finitely
   many configuration states (`exists_return`, `exists_common_period` [K CompositionOrder.lean:149, :171]) fixes the
   whole body (`finiteOrderOn_of_reach_diag` [D]). This extends HO-9 item 3 (passive repeatable finite-rank towers) to the
   kernel's full availability over the stated access, and to the observer theory of every kernel substratum
   (`obsTheory_obstruction` [D]).
3. **Necessity** (`exists_nonsubmonomial_of_ordInf` [D]). For every architecture, ORD∞ on the token body forces an
   operator of the class at the token's carrier that is not submonomial.
4. **The frame-axis rotation is present; the body is what is missing.** Conjugation by the frame phase
   `diag(…, e^{i}, …)` is available in the substratum theory (`framePhase_avail_substratum` [D]; a monomial, I4.148,
   I4.44), acts as the identity on its token body (`framePhase_trivial_on_substratum_body` [D]), has infinite order on the
   full matrix algebra and on every set containing a state with a nonzero entry between its configuration and another
   (`framePhase_infiniteOrderOn`, `framePhase_infiniteOrderOn_univ` [D]; π irrational), and crosses every finite stage
   that holds such a state (`framePhase_crosses_stages` [D], the finite-stage mechanism of CompositionOrder.lean:378). The
   same holds with `e^{iθ₀}`, `cos θ₀ = 3/5`, in place of `e^{i}` [X E3: `z = (3+4i)/5` has minimal polynomial
   5x² − 6x + 5; the module uses `e^{i}`]. So the matrix form of HO-20's frame-axis rotation is in the stated access
   already, at every level; what the stated access lacks is a coherent state for it to act on.
5. **The equivalence, one direction at a time (§A.34).** Direction one, for every class: ORD∞ on the token body ⇒ the body
   is coherent (`coherent_of_ordInf` [D]; witness: the contrapositive through `not_ordInf_of_reach_diag`). Direction two,
   for every class containing the frame phases at the carrier, in particular every class containing the substratum class
   there: a coherent body ⇒ ORD∞ (`ordInf_of_coherent`, `ordInf_iff_coherent_of_extends` [D]; witness: the frame phase).
   Without the phase continuum direction two fails: `fixedGateTheory (π/4)` has a coherent level-one body and only the 24
   Clifford channels at level one, each of finite order [X E5; completeness of the 24 by O9-L1, [W]], so its level-one
   datum set is finite and composition-closed and `not_ordInf_of_finite_of_mulClosed` [K CompositionOrder.lean:109]
   excludes ORD∞. At `π/8` (rational, no continuum) ORD∞ holds through the level-one word `W` [X E6].
6. **Reversible data that are not unitary conjugations** [W + X E8]. For a submonomial class the body is the simplex Δ of
   configuration-diagonal states (it contains every configuration state, `instAvail_id`, and lies in the diagonal
   matrices). An available deterministic family Φ with an available inverse Ψ on the body maps Δ onto Δ affinely, so it
   permutes the extreme points of Δ, which are the configuration states, and a common period fixes Δ. On every enumerated
   deterministic family of levels one and two the configuration restriction is column-stochastic and has a nonnegative
   inverse exactly when it is a permutation matrix (95/95, 399/399) [X E8]. Not kernel-checked.
7. **The completed chart body** [W]. The kernel's chart body (I3.103, `chartBody`) is built from a protocol tower of finite
   stages of preparations and effects. For the stated access every effect value depends only on the diagonal of the state
   (each branch commutes with the dephasing, O1-T3), and the configuration readouts (available, I4.64's `readout_avail`)
   separate diagonal states, so the completed chart body of the token is affinely the simplex Δ and each datum induces on
   it the permutation it induces on Δ. The tower is not formalized here; the statement of item 2 is the matrix-level one.

**Which way O11 comes out, in the owner's terms.** Case (ii): every such datum has finite order on the stated access.
The predicate is stated over the kernel's structures and refuted against named items (the table of §1): the substratum
theory satisfies every listed inventory item and carries no datum of infinite order on its token body. So the infinite-order
stage-crossing datum is not a consequence of those items; it is an additional principle, and by items 3 and 5 any principle
that supplies it supplies a coherent token body, through an operator that is not submonomial.

## 1. Hypotheses, by kind (the coordinator's rule)

| result | hypotheses | kind | form |
|---|---|---|---|
| the no-go on the stated access (`substratum_not_ordInf`, `substratumTheory_datum_finiteOrderOn`) | the substratum class (I4.44, definition), its generated theory (I4.240), its architecture (I4.32, discharged by `substratumClass_arch` [K StructuralClosure.lean:231]), configuration-level (I4.242, discharged by `substratumClass_configurationLevel` [K ManuscriptAxioms.lean:129]), `InstAvail` (I4.26), branch realization (I4.25, `realized_of_instAvail` [K ImplementationLocality.lean:530]), the order predicates (I3.106–I3.108) | (i) all | OI ⇒ no datum of infinite order on the token body of the stated access [D] |
| the same for the sourced class and the observer theory (`permClass_not_ordInf`, `obsTheory_obstruction`) | `permClass` (I1.60's folded `IsScaledPartialPerm`), `permClass_arch` [K SubstratumInterfaceAudit.lean:350], a kernel substratum with finite sites and alphabet (I1.57; A1 is I1.63), its observer theory (I1.59) | (i) all | OI ⇒ the same for the observer theory of every kernel substratum [D] |
| necessity (`exists_nonsubmonomial_of_ordInf`) | an architecture (I4.32, assumed in general); ORD∞ on its token body (I3.108, the conclusion of a sourcing, not an OI premise) | (i) and the target | a statement about any sourcing [D] |
| direction one (`coherent_of_ordInf`) | none beyond the definitions | (i) | [D] |
| direction two (`ordInf_of_coherent`, `ordInf_iff_coherent_of_extends`) | the class contains the frame phases at the carrier, as the substratum class does (I4.44, I4.148) | (i) for the stated access; an extension that adds coherence is introduced | [D] |
| the frame phase (`framePhase_avail_substratum`, `framePhase_trivial_on_substratum_body`) | I4.44, I4.148, I4.26 | (i) | OI ⇒ [D] |
| the control (`fullClass_ordInf`) | the full class (ImplementationLocality.lean:374) | not an OI item: the control's own object | [D] |

No hypothesis of kind (ii) — no exclusive readout, no re-preparation law, no H-T, (A), (b) or KB-D — enters any O11 result.

**What the obstruction satisfies while the datum is absent** (`substratum_obstruction`, `obsTheory_obstruction` [D];
each item discharged for the stated access by the kernel theorem named):

| inventory id | item | discharged for the stated access by |
|---|---|---|
| I4.64 | `FiniteOperationalTheory` (the matrix-level carrier) | `substratumTheory A` is one (I4.240, RouteB.lean:279) [K] |
| I4.26, I4.25 | `InstAvail`, `Realized` | generated availability; `realized_of_instAvail` [K ImplementationLocality.lean:530] |
| I4.28 | `ImplementationGenerated` | `genTheory_generated` [K ImplementationLocality.lean:926] |
| I4.32 | `Architecture` | `substratumClass_arch` [K StructuralClosure.lean:231] |
| I4.29, I4.30, I4.132, I4.45, I4.46 | `ContextStable`, `LabelInvariant`, `DaggerStable`, `StructurallyClosed` | `substratumClass_contextStable`, `_labelInvariant`, `_daggerStable`, `_structurallyClosed` [K StructuralClosure.lean:261, :275, :289, :316] |
| I4.242 | `ConfigurationLevel` | `substratumClass_configurationLevel` [K ManuscriptAxioms.lean:129] |
| I4.60 | `SubstratumAvail` | `substratumTheory_substratumAvail` [K LiftAudit.lean:750] |
| I1.49 = I4.241, I4.133, I4.110 | `DerivedOI` (with `ReversibleImplementationLocality`, `EmbeddedObservation`, the exchanges, the quarter phases, the read-write operators) | `substratumTheory_derivedOI` [K RouteB.lean:290] |
| I1.43, I1.50, I1.52 | the sealed OI core; `DerivedOICore` | `substratumTheory_realizesSealedOICore`, `substratumTheory_derivedOICore` [K RouteB.lean:375, :380] |
| I1.57, I1.63, I1.64 | the kernel substratum's A1, A2 | `obs_a1` [K SubstratumInterfaceAudit.lean:785], `a2_every_substratum` [K :106] |
| I1.59, I1.60 | the observer theory; `SourcedOI` | `obs_sourcedOI` [K SubstratumInterfaceAudit.lean:827] |
| I1.58, I1.65–I1.68 | A1–A5 for the wave rule; A3–A6 for any rule | the observer theory does not depend on the rule (`obsTheory_rule_independent` [K :779]), so the obstruction holds for every rule on finite sites and alphabet, the wave rule's included (A1–A5: `waveSubstratum_A1` … `_A5` [K :185–:211]) [W, composition] |

The obstruction fails exactly the flagged completion conditions that are not OI premises: I4.67
`HasCompositeUnitaryControl` (`substratumGen_not_control` [K StructuralClosure.lean:348]), I4.70
`ExactAllFiniteEndomorphicQuantumOps` (`substratumGen_not_qm` [K :359]), I4.143 `DrivesElementary`
(`substratumClass_not_drivesElementary` [K :370]), I4.56 `LayerFlowExecutable` (`substratumTheory_not_layerFlowExecutable`,
I4.59 [K LiftAudit.lean:200]), I4.118 `PhaseFreeRichness` (`substratumTheory_not_phaseFree` [K RouteB.lean:388]). In Table
A2 of the stage-6 reassessment the items I4.29, I4.45, I4.110, I4.133, I4.241 are NOT REACHED for the pair cone (level M); O11
places them at the token level, where they hold together with the absence of the datum.

## 2. Disguise test of the predicate

- *Letter.* ORD∞ on the token body names no non-monomial operator, no complex structure and no balanced state: it
  passes the owner's letter.
- *Kernel carrier.* It is equivalent, for every class containing the stated access, to a coherent token body (item 5),
  and it forces an operator that is not submonomial (item 3) — the non-generating half of O1-T1 negated, the output of a
  coherence-generating operation. As a sourcing target it restates the coherence the Discrete Origin is to source (SRC):
  it **fails** the disguise test as an independent target on the kernel's carrier. The infinite-order datum itself, the
  frame-axis rotation, is already available and is not what a source must supply.
- *Without the continuum* (MixR classes, no frame phases) coherence is not enough (π/4, item 5), and the fixed gate that
  supplies both at a non-Clifford angle is a postulated mixer (O2-G3, FAILED by disguise).

## 3. Relation to HO-22 (S1)–(S4) and HO-20 H-T (checked against, not premises)

- (S1) "an infinite-order datum on the token": on the kernel's matrix carrier with the stated access's phase continuum it
  is not a separate obligation; it holds exactly when the token body is coherent (item 5). The hidden assumption in the
  split is that the datum is what the stated access lacks; it lacks the coherent body.
- (S3) "R_z(θ₀) crossing every stage structure that carries J and cnot": on a coherent body the frame phase crosses every
  finite stage holding a coherent state (item 4); on the stated access's body it is stage-preserving and trivial.
- (S4) and H-T's (A) for the frame-axis rotation and the NOT: at the matrix level both are monomial, so their spectator
  forms are in the context-stable substratum class (I4.29 [K StructuralClosure.lean:261]) and available in the pair context
  at every level [K, composition]. HO-20 item 6 (L-REG) is the matching marker: read configuration-wise this availability is
  Bell-local. Matrix-level availability in context is therefore not where the stated access fails; it fails at the body.
  Nothing here is about the level-H conditions (W), (P) of HO-20, which are not read.

## 4. Classification (§A.31)

- **NEW, O11-N1 (hidden assumption exposed).** On the kernel's carrier, (S1) is not an independent obligation: given the
  stated access's phase continuum, ORD∞ on the token body holds exactly when the body is coherent, and the frame-axis
  rotation that would carry it is available on the stated access already, acting as the identity on its classical body.
  Assumption-watch marker: a missing infinite-order datum on a classical body is a missing coherent state, not a missing
  operation.
- **NEW, O11-N2.** HO-9 item 3 extended from passive towers to the kernel's full availability: for every configuration-level
  architecture, at every carrier, every available datum has finite order on the token body; ORD∞ forces a non-submonomial
  member of the class (design module, 45/45).
- **ELABORATING, O11-E1.** Without the phase continuum coherence does not give ORD∞ (π/4), while a non-Clifford rational
  angle does (π/8): the bridge between the two is O12's angle condition.
- **CONFIRMING, O11-C1.** O1-T3 (dephasing covariance of the monomial classes), recomputed as the diagonality of every
  reached state at levels one and two; O9-L1's 24 channels at π/4 (E5).

## 5. Design-module record

`OIBridge/OriginTokenOrder.lean` at dev commit `35d326a3` on `dev-origin/token-order` (cut from L; the diff from L is the
module and one aggregator import line): workflow run 38108620996, Mathlib bridge job 114379324788, step Build success
(`Built OIBridge.OriginTokenOrder`, four linter warnings), 45/45 `#print axioms` lines on [propext, Classical.choice,
Quot.sound], release gate red only on `lean-manuscript` (1 problem, by construction), `lean-axioms` PASS (5905 named results,
no sorry). Verbatim copy: `lean/OriginTokenOrder.lean` (blob `f1ad72e5`, sha256 `bdf62599…c6ea53c`, 700 lines). Design
evidence only; nothing certified.

## 6. Open

- The chart-body form (item 7) and the non-unitary reversible data (item 6) are written arguments, not kernel-checked.
- Whether some principle outside the inventory supplies a coherent token body without introducing a mixer is the open
  question of SRC itself; O11 shows the stage-crossing datum adds no obligation beyond it on the kernel's carrier.

## 7. The acceptance criteria of coordinator addendum 3 (appended 2026-10-11T04:40Z)

Addendum 3 makes two distinctions acceptance criteria for O11's verdict. This section states how O11's results stand
under them; §0–§6 are not edited and are read with this section. Where §0 ("Which way O11 comes out") says that the
stage-crossing datum "is an additional principle", read the narrower statement N11 below: O11 does not establish that
the datum is independent of OI.

**(1) Pair-level versus full-OI insufficiency.** An independence verdict needs a full model of the stated access — its
generated theory with every `InstAvail` protocol and ancilla block — that satisfies the applicable OI premises at every
level that applies to it, the 68 NOT REACHED rows of the stage-6 reassessment (Table A2, R6 REASSESSMENT at
research/archive 4dc0321c, sha256 1ff62ad6…a884ffe) included so far as they apply to the model's level, and in which
every datum on the token's completed chart body has finite order.

What O11 has. The model is the substratum theory `substratumTheory A` (RouteB.lean:279; `genTheory` of the substratum
class, every `InstAvail` constructor — step, readout, coarse-graining, feed-forward, discard — and every ancilla block,
the class being closed under `Architecture.block`); its theorems quantify over every carrier, so they hold at every
level A × Fin n. The finite-order statement is [D] on O11's own token body (the closed convex hull of the
`InstAvail`-reachable normalized states, §0.1) for available unitary conjugations; for other available reversible data
it is [W] (§0.6), and on the kernel's completed chart body it is [W] (§0.7). Against the 68 NOT REACHED rows:

| class | rows | how |
|---|---|---|
| (a) satisfied, 16 | I4.241 DerivedOI; I4.133, I4.110 (its first two conjuncts); I4.31 ImplementationLocality; I4.29 ContextStable; I4.45 StructurallyClosed; I4.68 IteratedAncillaClosure; I4.69 SystemToLevelOne; I4.87 ObserverRecursion; I4.66 CompositeOperationalValidity; I4.73 WellFormed; I4.96 and I4.3 ObservationalIndependence = HasParallelReferenceExtension; I4.82 (the same on the qubit carrier); I4.14 InertSpectatorCompositionality; I4.4 HasQutritReferenceExtension | [K] RouteB.lean:290, :141, :149, :153; StructuralClosure.lean:261, :316; EmbeddedObservation.lean:217, :223; ImplementationLocality.lean:957, :971; GeneralCarrier.lean:125; SpectatorBridge.lean:233; ReferenceExtension.lean:474 (composition of these per row [W]) |
| (b) kernel theorems, true in every model, 5 | I4.210, I4.215, I4.216 (positive-semidefinite facts, comparison objects); I3.104 `body_isClosed`, I3.105 `preservesBody_inducedEquiv` | [K] JordanClassification.lean:84; OperationalRigidity.lean:917, :956; CompletionAction.lean:202, :352 |
| (c) failed, 21 — each flagged in the inventory as an OI⁺ completion condition, an OI⁺ package equivalent to exact quantum mechanics, or a form of reversible richness ("do not assume"; none is an OI premise) | I4.67 HasCompositeUnitaryControl; I4.70 ExactAll…QuantumOps; I4.56 LayerFlowExecutable; I4.118 PhaseFreeRichness; I4.143 DrivesElementary; I4.144 QuantumArchitecture; I4.65, I4.74, I4.80 (they contain or are equivalent to conditions containing control); I4.85, I4.99 ReversibleRichness and I4.128 LieRankRichness (each gives control); I4.123 CyclicRichness (gives phase-free richness); I4.179 PairFlowSourced (with DerivedOI, equivalent to exact QM); I4.42, I4.88, I4.102, I4.115, I4.120, I4.124, I4.137 (packages equivalent to exact QM) | [K] StructuralClosure.lean:348, :359, :370, :376; LiftAudit.lean:200; RouteB.lean:388 (qubit carrier); the implications CarrierGeneralOIPlus.lean:127 (I4.99), CompletedOI.lean:200 (I4.85), MicroscopicReversibility.lean:114 (I4.128), MinimalRepertoire.lean:642 (I4.123); the equivalences PairFlowEquivalence.lean:199 (I4.179), CompletedOI.lean:110 (I4.80), ImplementationLocality.lean:1079, CompletedOI.lean:440, CarrierGeneralOIPlus.lean:213, EmbeddedObservation.lean:384, MinimalRepertoire.lean:569, PositivePackage.lean:55, MicroscopicReversibility.lean:357 (the packages) |
| (c′) not decided here, 4 — flagged as clauses or forms of reversible richness, or as the quantum endpoint (not OI premises) | I4.127 InverseAccessibility; I4.244 ElementaryTransitionRichness; I4.245 OIPlusElem; I4.187 ShadowQuantum (level G) | — |
| (d) level P, not at the model's level, 8 | I3.134, I3.136, I3.141, I3.154, I3.157, I3.158 (three or four tokens); I3.145 P-STAGE2, I3.146 P-ACT2 (named pair premises) | the model has no pair-cone structure; no M→P bridge at L |
| (e) manuscript scope statements and theorem statements, 12 (not premises) | I1.17; I2.3, I2.29, I2.30, I2.31, I2.32, I2.33, I2.34, I2.35, I2.62, I2.63, I2.69 | consistent with the model: an OI-compatible theory that is not quantum (I2.30's statement) |
| (f) level O, applicable, not shown for the model, 2 | I3.96 `FiniteRank` (K∞-Stage), I3.99 `OpDatum` (K∞-Act) | the kernel's completed chart body of the stated access's token tower is not constructed in O11 |

Counts: 16 + 5 + 21 + 4 + 8 + 12 + 2 = 68. The H-level items of the model's substratum stand as in §1: A1, A2 [K];
the wave rule's A1–A5 through the rule independence of the observer theory [K]; the other A3–A6 readings [W].

**Conclusion under (1).** O11 establishes the narrower statement

> **N11.** In the stated-access model — which satisfies every row of the inventory checked against it at level M, the
> NOT REACHED rows of class (a) included, and fails only rows flagged as OI⁺ completion conditions, packages or
> endpoints — every available unitary datum has finite order on the matrix-level token body, at every level.

Label: CONDITIONAL ([D] run 38108620996 with [K] per item). It does not establish independence of the stage-crossing
datum from OI. That question is a precisely scoped OPEN; the unproved lemma at the model's own levels is:

> **(L-O)** For the stated access, the kernel's completed chart body of one token — the StageCompletion and
> CompletionAction construction (I3.92–I3.105) applied to the token's protocol tower, whose stage n holds the
> `InstAvail`-reachable states and effects at level n — has finite rank (I3.96) and is affinely the simplex of
> configuration states, and every operation datum on it (I3.99) with `AffineRespect` and an inverse datum that is
> realized by available operations of the stated access is induced by an available operation, so that it permutes the
> vertices of the simplex and has finite order.

(L-O) is argued in §0.6–0.7 [W]; there is no kernel or design proof. The rows of class (c′) are not premises, so they do
not bear on the criterion, and the rows of class (d) are at a level the model does not have; neither is claimed either
way. No independence is claimed.

**(2) Cone invariance versus operational availability.** Every O11 row is an availability statement: the data are
operations obtainable through the kernel's protocols (unitary conjugation channels available by `InstAvail`; in O11-T7,
available deterministic families with available inverses), and the token body is built from `InstAvail`-reachable
states. No O11 row is a cone-invariance (admissibility) statement, and none lets preservation stand in for
availability: where preservation enters (§0.6, an available reversible family maps the simplex onto itself and so
permutes its vertices), it is a consequence of availability, not a substitute for it. O11 does not use the pair-level
(b), (T) or A_miss, which are cone-preserving admissibility statements.
