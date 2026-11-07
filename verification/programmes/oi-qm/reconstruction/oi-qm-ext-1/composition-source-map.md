# OI–QM EXT-1: composition and Bell source map

**Paper-only author assessment — submitted for independent review; not an established physical equivalence result.**

Accountable issue: [#868](https://github.com/amaybaum/incompleteness/issues/868). Feeds [#1060](https://github.com/amaybaum/incompleteness/issues/1060) and [#1169](https://github.com/amaybaum/incompleteness/issues/1169). Guiding draft: [#1173](https://github.com/amaybaum/incompleteness/pull/1173). Sole author: `/root/writer_composition`, on `research/oi-qm-composition-source-20261107`; this file is its only write target. Scope and authority are recorded in [#868 c.6704792136](https://github.com/amaybaum/incompleteness/issues/868#issuecomment-6704792136) and [#1169 c.6704790395](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6704790395).

Research base: `235305e24b22633848f1b399efb77fbba5f8b4df`; maintained-corpus read pin: `71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd`. AGENTS.md was read at the latter pin (blob `496eb7018c736a064dddcf00fd1a278790872f49`). Existing issue/branch writer scopes were checked by the coordinator and recorded before activation. The earlier #836 planning branch and #1060 frozen H-Bell namespace remain separate.

## 1. Selection and stopping contract, fixed before the derivation

This is an assumption/source assessment, not selection of another fitted Bell model. Literature and actual corpus proofs are read before proposing a mechanism. The test is whether a physically motivated source supports a *common* joint preparation and controlled operations, including all accessible records, on the same realization.

1. Start from the accepted conditional local component at the research base. Its bounded dependency cone and screened-local Bell ceiling are controls; better preparation or read access alone does not repeal them. Its review is scoped to that component.
2. Compare Bell local causality with setting independence, complete-history operational no-signalling, and the actual composite/local-operation hypotheses used in the Barandes–Hasan–Kagan proof. Hidden memory may be included in a response-complete variable. Determinism is admissible.
3. Separate a global stochastic-law representation, a quantum upper bound on an admitted operational class, physical availability of quantum preparations and controls, and exact whole-model equivalence. None is substituted for another.
4. Consider only an existing OI mechanism or an independently motivated extension proposal. No cross-wing gate, hidden measure, inaccessible register or reset is chosen merely to produce a desired table. New physical premises remain proposals, not adopted inputs.
5. Stop at the first missing physical source: name the carrier/dynamics/preparation/setting operation/measure/access/continuation clause that is missing. If no source-backed pair realization is identified, deliver a precise bridge obligation rather than an invented example.
6. Controls are the screened-local classical bound, classical complete-history no-signalling, and the PR distinction between no-signalling and quantum soundness. A pass at one time or one CHSH setting menu does not establish closure under repetitions, spectators, ancillas or combined experiments.
7. Deliver an assumption-by-assumption map and one next proof obligation with explicit inputs and a discriminating pass/fail/stop rule. Unknown physical data remain unknown; the parallel preparation and measure studies are not assumed to supply them.

Only paper analysis, hand derivations, draft checkpoints and independent review are authorized. No simulation, enumeration, implementation, new physical-premise adoption, freeze, special workflow dispatch, merge or manuscript claim promotion occurs in this thread. Prior studies retain their distinct review status. In particular, `two-system-interface.md` is author analysis awaiting its own independent review and is not supporting evidence for this assessment.

## 2. Result and source disposition

The read corpus supplies a conditional local apparatus component, representations of supplied finite stochastic laws, and conditional quantum/composite assembly. It does **not supply the physical pair required by this assessment**: one preparation, setting-independent uncontrolled source, selectable local operations and complete reusable records whose joint law has the required quantum composition.

This is a scoped source stop, not a no-go for all native OI.

- **Derived conditionally:** separated implementations of the accepted bounded-range component obey the screened-local CHSH ceiling for any common setting-independent source law. Hidden memory can be included in the pre-setting state.
- **Conditional sufficient route:** a common positive joint-state representation with local normalized quantum instruments gives complete-history no-signalling and the quantum CHSH upper bound. The short proofs below identify what must be sourced.
- **Unsourced here:** a physically prepared pair and a setting- and continuation-compatible map from its actual dynamics to those instruments. Preparation-indexed geometry is an existing motivated research direction, but no particular long-edge mechanism or selected pair measure is supplied.
- **Not concluded:** a Bell violation, the complete quantum correlation set, B3 on the native ring, a resolution of H-Bell's geometry debt, or OI–QM equivalence.

The next obligation is a **two-use prepared-pair interface bridge** (§7), reusing #868's joint-state/test obligation. It starts with a source-backed pair and tests the local-instrument correspondence on its whole physical boundary. A Bell table is an output, not its definition.

## 3. Source review before mechanism selection

### 3.1 Primary literature, actual versions

The arXiv version histories were checked on 2026-11-07: [Barandes, The Stochastic-Quantum Theorem, 2309.03085v2](https://arxiv.org/html/2309.03085v2), and [Barandes–Hasan–Kagan, The CHSH Game, Tsirelson's Bound, and Causal Locality, 2512.18105v1](https://arxiv.org/html/2512.18105v1). The latter lists a journal publication; no uninspected journal revision is used.

Barandes's finite-configuration theorem is a subsystem dilation (§4.1, §5.7–5.8), recovering specified conditional probabilities by marginalization. This is useful for representation; it does not identify OI's native preparation, controls or observer cut. Its §3.1 explicitly leaves higher-order conditional probabilities unspecified; §5.8 constructs a dilated conditioning-time set consisting only of the initial time. Matching those data therefore does not identify a prescribed intervened history law. Compatibility with actual interventions and physical wings remains an additional obligation here.

BHK uses Cartesian composite configurations, stochastic dynamics/division events and a marginal-independence causal criterion (Eqs.22–24). Its CHSH protocol includes a shared preparation, local settings, monitored observer memories and shielded resources. The operative proof uses a common prepared vector and product readout (Eq.28), then a tensor-factorized setting operation (Eq.30) to obtain the bound (Eqs.31–36). We use that sufficient representation, not an inference from endpoint marginals alone. The pinned proof supplies neither an OI source nor an all-reuse-history theorem. This assessment is not a review of every claim in either paper.

### 3.2 Maintained corpus and existing research

The following material sources and assumptions were read. Main sources are at the maintained-corpus pin in §1. No Lean build or replay of old computations is claimed.

| Source | Actual support used here |
| --- | --- |
| [Main §§3.3–3.4](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/papers/Main.md), blob a954cfb47c740766b8ca6ab9027a46bbf6fa2f94 | Cone/screened-local Bell proofs; finite-law representation; action-labelled classical dilation with supplied target probabilities and action-ledger operations. No physical compiler follows. |
| [SM §3.1](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/papers/SM.md), blob de1466b0c004339d60f1490e494e8f5037020948 | State-dependent-geometry motivation, explicit bounded-range ring rule and discussion of preparation-indexed longer edges. Broader isotropy/curvature claims are not premises. |
| [Accepted local component](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md), blob 3229ef3cd234e613a4b0cb63bab548e0fec666a9 | Conditional ring, common prior, controller-inclusive records and outgoing state; preparation/loading/read hardware and same-model B3 unsupplied. Acceptance is provenance, not physical adoption. |
| [B3 exchange candidate](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-exchange.md), blob aeaa8ca03f187bd0adda82532faf3154f4b4dd5f | Real mode carrier represented in C², posited quadratic sensor, independent seed slots and detector-controlled exchange. This is a different conditional realization, not native ring availability. |
| [Gate A](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md), blob d9d92e038a8022e854586101067ce4de9789fdf6 | Target: full stated finite preparation/instrument families, every finite adaptive depth, ancillas and complete records with one compatible model family. A target specification, not a source. |
| [PROGRAMME, Arc D physical lift seam and Arc F](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/programmes/oi-qm/PROGRAMME.md), blob 03ea3bdd774ae225bf6058231f90e566d7593fad | F2 separates physical extension, conditional sufficiency and necessity. The same source must survive ancillas, spectators, regrouping, instruments and composition. |
| [GeneralCarrier](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/GeneralCarrier.lean), blob 778fd9fc8ccc26084bced15f15c1148d648870e6 | exactAll_iff_physical_general: existing five-condition characterization for each nonempty finite carrier inside FiniteOperationalTheory. |
| [PhysicalCharacterization](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/PhysicalCharacterization.lean), blob 1a96e2454009638cee5bd3569b3bbcd5ec791d3a; [LevelOneSeam](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/LevelOneSeam.lean), blob 57805fe4ff5cd7b37ffa5ebe026f817a366605aa | Explicit validity, inert spectators, composite unitary control, iterated ancilla closure and system/level-one consistency; endpoint includes system and positive composites. |
| [OperationalAssembly](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/OperationalAssembly.lean), blob 592d8203c488914fe36c3e1b1371eb5efa9af3ca | Ambient complex-linear matrix maps and availability fields for preparation/readout/discard/feed-forward. readout_is_localLuders derives form from existence/locality fields; circuit_available consumes preparation and composite control. |
| [MinimalRepertoire](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/MinimalRepertoire.lean), blob 7df37d3f606350f547985c3d577faba106a76a56; [ImplementationLocality](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/ImplementationLocality.lean), blob d96b65bd262e658baf0be52cfaf4b6e33de0dd28 | qm_of_oiPlusMin consumes implementation locality, phase-free richness and embedded observation. InstAvail tracks complete instrument protocols, not arbitrary separately selected branches. |
| [EqvK2MaxCone](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/EqvK2MaxCone.lean), blob 5b4b98c8e81e21eb002de25383eada381b65e3dd | pairCone_eq_Q3_of_drive_maxCone consumes product inclusion, cone closure, product-test positivity/maxCone and preserving CNOT/drive generators. A linear dictionary or local test validity alone is insufficient. |
| [Preserved #868 plan](https://github.com/amaybaum/incompleteness/blob/0e0b3ddc64446f362199a3b00e5bdefae80e4674/verification/programmes/oi-qm/reconstruction/research-planning/joint-test-validity-source.md), blob 67d84959b1499ba80b22b8a99489a9b7276d9ad3 | Existing obligation and proposed controls, not a proof. This assessment reuses its accountable issue. |
| [Composition/access REPORT](https://github.com/amaybaum/incompleteness/blob/2af1d5d5b5fff4375e9fe9460f892c680ae99f0c/verification/programmes/oi-qm/reconstruction/composition-access-20261024/REPORT.md), blob 2f77fe2fbb15cdcf3f04656e1e215124137ac1a6 | Off-main conditional intertwining contract. Its elementary induction is checked again in §6; native source/gate computations are not inherited. The distinct composition_flag_v6/REPORT concerns a logical acceptance circuit. |

Live #868, #1060, #1169 and #914 records were read to locate scope, sources and pending decisions. They are planning records, not scientific premises. #1060 retains its separate metric/curvature and quantum-bound questions; no frozen record is modified.

### 3.3 Candidate-selection finding

The existing **state-dependent-geometry proposal** is motivated by allowing geometry/coupling to respond to physical state (SM §3.1). Main §3.3 identifies preparation-indexed adjacency as its proposed ontic-parameter-dependent Bell route while retaining setting independence as a posit. This makes that source question worth studying; it does not select a long edge, coefficient or probability law.

The explicit ring is useful because its update predates the Bell table. It is not the missing long-edge family. No concrete prepared pair with the required controls is identified in the sources checked above. This paper therefore selects no new Bell mechanism. A next proposal must source its graph/interaction and preparation and preserve the reference rule where its controls apply. An extension needs a consequence beyond the correlations it was introduced to explain. A fitted cross-wing gate and calibrated Bell weight fail that selection rule.

## 4. Assumption-by-assumption map

**Derived** means the stated mathematical consequence follows under explicit premises; **assumed** identifies an input; **unsourced** means the sources assessed here supply no physical realization of it. **Refuted** applies only to a displayed implication or a delimited class.

| Obligation | Exact content and support | Physical status / remaining clause |
| --- | --- | --- |
| A. Bell locality | For response-complete pre-setting \(\Omega\), \(p(a,b\mid x,y,\Omega)=p(a\mid x,\Omega)p(b\mid y,\Omega)\). Main's deterministic cone theorem supplies this in its separated screened class. | Conditional; the class cannot reach CHSH \(>2\). Stochastic marginal independence is different. |
| B. Setting independence | \(p(\Omega\mid x,y)=p(\Omega)\), or common-source interventions. Actual setting generators and their acquired information must be accounted. | Assumed in Main's selected Bell branch and the conditional local interface; physical loader unresolved. The full closed-universe state containing setting bits is not independent of those bits. |
| C. Joint preparation | Prepare pair, apparatus and residual state before separated settings, retaining all heralds, failures and resource costs. | Conditioned ring fields define a measure, not a demonstrated procedure. Bell pair and joint state/test dictionary unsourced here. |
| D. Local setting operations | Same dynamics/source across programs; real controllers and reads, with controller information included in accessible records. | Local ring interaction derived conditionally; no pair instrument family or physical loader supplied. |
| E. Stochastic causal cut | Remote-initial-configuration independence of transition marginals at the applicable conditioning events (§3.1). | A coarse process may satisfy it without factorization at a deterministic refinement. P-indivisibility is not an intervention/composition bridge. |
| F. Quantum local representation | One common positive joint state, fixed tensor split, and actual operations mapped to local normalized instruments. | Sufficient comparator structure. A global dilation or prepared graph alone does not supply it. |
| G. Complete-history no-signalling | Bob's complete accessible history law is independent of Alice's isolated policy, and conversely; include controller memories, failures, timing and later permitted local access. | Derived from §6's contract. First-read marginals or a private-register declaration do not establish its physical premises. |
| H. Quantum upper bound | Every admitted preparation/operation has the same positive-state/local-instrument representation. | Conditional bound available. Unrestricted finite-law representability also admits PR; a physically selected common operation class is unsourced. |
| I. Reuse | Output boundary is a valid next input; spent resources and correlated memory remain. Reset/freshness is justified whenever used. | Ring controller retains the signal; no automatic ready reset. Existing serial contracts are conditional. |
| J. Composites and spectators | Product tests valid on independently identified pair states; inert spectators, ancilla operations, regrouping and preserving generators. | K2 and the five-condition theorem identify premises; a local component or declaring a quantum cone does not source them. |
| K. Reachability and coverage | Bell \(>2\) distinguishes this route from classical screened models. Full #1169 needs all target operations and no extra accessible behavior. | No-signalling or a quantum upper bound alone proves neither reachability nor both directions of equivalence. |
| L. Geometry | Prepared graphs meet separately claimed metric/curvature requirements. | #1060's H-Bell debt remains independent. |

If marginal independence is imposed on **response-complete deterministic** data for each setting intervention, outcomes are point masses. Both wings are then parameter-independent and Bell factorization follows. If imposed only after hidden variables are marginalized, it need not constrain each hidden response. A viable deterministic Bell route must physically identify that difference, then prevent signalling in every accessible history. Calling hidden memory indivisible does not change this logic.

## 5. Three algebraic controls

### 5.1 The accepted local component retains its ceiling

The ring update is
\[
 F(u,v)=(f(u)\mathbin{\mathrm{XOR}}v,u),\qquad
 f_i(u)=u_{i-1}\mathbin{\mathrm{XOR}}(u_{i+1}\mathbin{\mathrm{OR}}u_{i+2}).
\]
Its inverse is \((a,b)\mapsto(b,a\mathbin{\mathrm{XOR}}f(b))\). Each tick uses coordinates at ring distance at most two. By induction, every record through tick \(T\) depends only on its initial \(2T\)-neighborhood. If the remote setting's read/write region is outside those neighborhoods for **all** local apparatus/record regions observed in the window, the complete local history is independent of that setting at fixed \(\Omega\). Any local function of that history inherits this property.

With common setting-independent source and every-run binary outcomes, write \(A_x(\Omega),B_y(\Omega)\in\{-1,1\}\). Pointwise,
\[
 A_0(B_0+B_1)+A_1(B_0-B_1)\in\{-2,2\}.
\]
Averaging yields \(|S_{\rm CHSH}|\le2\). Observed dynamics need not be memoryless. This holds for any shared preparation law on the admitted pre-setting states. Better loading or a different law cannot raise the ceiling while these hypotheses remain.

The separation condition must hold for the entire covered window. If cones meet or allowed access extends outside it, the proof ceases to apply; this is a changed premise, not evidence of a quantum Bell model. No success-conditioned statistic replaces every-run outcomes.

### 5.2 No-signalling alone admits a stronger-than-quantum law

For binary settings and outputs, the mathematical countercontrol
\[
 P(a,b\mid x,y)=\tfrac12\,{\bf1}[a\oplus b=xy]
\]
has both marginals \(1/2\), but \(E_{xy}=(-1)^{xy}\) and CHSH \(4\). This is a probability-law counterexample, not a proposed OI mechanism or chosen source distribution.

Conversely, a shared classical variable with only local transitions yields complete histories \(H_A^\alpha(\Omega),H_B^\beta(\Omega)\) under local policies \(\alpha,\beta\). A common source gives complete-history no-signalling at every covered depth, with the Bell ceiling above. Thus passing the history test is necessary here and insufficient for quantum behavior.

### 5.3 Endpoint probabilities do not determine a local quantum lift

This independent diagnostic shows why actual interventions matter. Both \(I\) and \(U=\operatorname{diag}(1,1,1,-1)\) have identity configuration-basis transition probabilities on two qubits. Those probabilities have no cross-wing marginal dependence. Yet \(U\) is not a tensor product: its diagonal entries fail \(u_{00}u_{11}=u_{01}u_{10}\). Moreover,
\[
 U(|0\rangle|+\rangle)=|0\rangle|+\rangle,\qquad
 U(|1\rangle|+\rangle)=|1\rangle|-\rangle .
\]
An allowed \(X\) read on the second factor distinguishes the first preparation. This does **not** refute existence of a local lift for the identity table: \(I\) is one. It refutes the inference that a fixed-basis probability table determines locality of a chosen lift or its behavior under further interventions. It is not a candidate OI interaction.

## 6. What a successful composition bridge would buy

This is a sufficient comparison contract, not a new physical premise. It permits deterministic microscopic evolution and observer-relative information.

Let \(C_i\) be a physically specified cone of unnormalized nonnegative measures on the whole boundary at use \(i\): carrier, controllers, apparatus, old memory, remaining banks and fields that can affect later allowed observations. Let \(K_i(x,y,a,b)\) be the actual record-resolved transition kernel. Here \(a,b\) are **complete** new local records, including failures; the summed kernel preserves mass.

Require fixed linear comparison maps \(D_i\) from the span of \(C_i\) to operators on a fixed bipartite carrier including local ancillary memory as needed, with \(D_i(\mu)\ge0\) and \(\operatorname{tr}D_i(\mu)=\mu(1)\) for \(\mu\in C_i\). Positivity is not silently required on every ontic point mass. Maps may depend on the predetermined stage but cannot be refitted to realized settings/history. Require
\[
 D_{i+1}K_i(x,y,a,b)\mu
 =(\mathcal A_{i,a}^{x}\otimes\mathcal B_{i,b}^{y})D_i(\mu),
 \qquad\mu\in C_i,                                      \tag{1}
\]
where the branch maps are completely positive and each local sum is trace preserving. Initial \(D_0(\mu_0)=\rho_{AB}\) is common across later setting choices. All memory is assigned consistently and each output lies in the next admissible cone. A comparison map is mathematical, not an available hidden-state reader.

**Branch-law consequence.** At every node of a finite adaptive tree, the unnormalized native branch measure and decoded reference operator agree. Initialization starts the induction. The controller chooses from the respective retained local histories; (1) gives the identity on each child. Traces give every joint record probability, including zero/failure branches without postselection. Every further allowed terminal read needs a matched effect. This checks the elementary induction of the existing serial contract with a new explicit bipartite premise, without inheriting that draft's native computations.

**Complete-history no-signalling.** Fix Bob's policy \(\beta\) and full history \(h_B\), with composed branch map \(\mathcal B_{h_B}^{\beta}\). Summing Alice's branches for any policy \(\alpha\) gives a trace-preserving map \(\mathcal A^\alpha\). For adaptive trees, work backwards: each node's complete outcome family sums to a trace-preserving operation, including termination/failure. With \(E_{h_B}=(\mathcal B_{h_B}^{\beta})^*(I)\),
\[
\begin{aligned}
P(h_B\mid\alpha,\beta)
 &=\operatorname{tr}[(\mathcal A^\alpha\otimes
                    \mathcal B_{h_B}^{\beta})(\rho_{AB})]\\
 &=\operatorname{tr}[\rho_{AB}
       ((\mathcal A^\alpha)^*(I)\otimes E_{h_B})]\\
 &=\operatorname{tr}[\rho_{AB}(I\otimes E_{h_B})].
\end{aligned}                                          \tag{2}
\]
This is independent of \(\alpha\), and symmetrically for Alice. Local history and environmental memory may be included in the carrier. A mediator that interacts across the split during isolation cannot simply be discarded to obtain (1). Later communication changes the experiment and is allowed outside the isolation interval.

**Quantum bound.** In the binary projective CHSH subexperiment, local observables square to \(I\) and commute across factors. Its operator
\[
 C=A_0(B_0+B_1)+A_1(B_0-B_1)
\]
satisfies \(C^2=4I-[A_0,A_1][B_0,B_1]\). Each commutator has norm at most \(2\), hence \(\|C\|\le2\sqrt2\) and \(|\operatorname{tr}(\rho_{AB}C)|\le2\sqrt2\). A local dilation covers binary quantum measurements when needed. This bound is conditional on the common representation, not a derivation of it from OI.

Representing **every** admitted operation/preparation by (1) gives quantum soundness on the covered domain. A selected menu gives only that menu's soundness; a CHSH bound alone gives less. Quantum completeness needs actual target preparations/controls. Existing assembly is used after its hypotheses are physically supplied; repeating its classification does not close this gap.

## 7. One next proof obligation: the two-use prepared-pair interface

**Accountable #868, feeding #1060/#1169. Proposed next unit, not executed or newly authorized by this record.**

Supply one independently motivated physical prepared-pair family and prove or refute (1) at its first two use boundaries, for one predeclared two-setting-per-wing menu and all permitted local access in that bounded experiment. Begin with its actual source and operation contract; if absent, stop there. Do not solve for a hidden law because it makes a desired Bell table true.

| Datum | Required input and present status |
| --- | --- |
| Carrier | Whole pair, preparer, controllers, records, resources and observer cuts. The binary ring supplies a conditional local component; the required prepared-pair carrier is **unknown**. |
| Dynamics | One setting-independent reversible update and physical controller interactions. A preparation-indexed graph proposal must derive its adjacency/couplings and identify the changed screened-cone premise. That family is **unknown**; no cross-wing opcode is inserted. |
| Probability | Independently justified pre-setting source and preparation, common across selected programs; include every herald/failure. Local conditioned fair-bit law is mathematically known; the pair source/procedure is **unknown**. |
| Settings | Actual selectable loaders with controller knowledge and source independence accounted. Pair loaders are **unknown**. |
| Histories | All readable apparatus/controller fields, retained records, failures, timing and later allowed local reads during isolation. Physical pair access and its closure are **unknown**. |
| Reuse/composition | Outgoing boundary fits the second operation, including garbage and remaining/fresh resources. No automatic reset, resampling or discarded mediator. Closure is **unknown**. |
| Comparison | One fixed pair-state/test dictionary and local instruments, matching joint records and outgoing decoded states. Positive pair validity and (1) are the **proof obligation**, not the definition of native validity. |

A Bell-capable deterministic proposal retaining setting independence must leave the screened pointwise-local class. If it remains there, §5.1 settles its Bell ceiling before fitting a table; it can still serve apparatus development. Discarding an accessible controller is not a legitimate escape.

**Decision rule.** Pass the bounded bridge only when the full record-resolved native law and outgoing boundaries satisfy the same fixed instruments on both uses, including failures, and the required controls are physically available. Unequal Bob-history laws across Alice policies fail the isolated-history criterion. A positive representation gives the bound without tuning the distribution. A Bell-local candidate can earn a limited positive result; a Bell milestone additionally needs physically available \(S>2\), within the bound. If agreement rests on an unsourced restriction, preparation, measure, reset or access rule, stop at that clause.

Two uses discriminate candidates; they do not establish all-depth composition. Generalization requires closure of the same boundary/source family at every admitted depth and under spectators/ancillas. Joint-test positivity alone also leaves K2's product inclusion and preserving-generator premises open.

## 8. Compatibility and review boundary

This thread supplies no new physical ingredient to splice into a different model. Its local control uses the exact binary dynamics and conditional preparation of the accepted component. B3's continuous carrier, quadratic sensor, seed supply and exchange mechanism have not been realized on that ring. Parallel preparation/probability studies are not presumed to supply the missing pair data.

A joint construction must agree on \((S,F,\mu,\text{preparation},\text{controls},\text{access},\text{boundary})\). Equal single-read statistics on different carriers do not identify these tuples. A local apparatus loader need not prepare an entangled pair, and a measure appropriate to one component need not fit a prepared graph. Physical pair compatibility is **undetermined because its data are missing**, not demonstrated by shared notation.

The strongest supported outcome is a located source obligation and conditional Bell/history controls. No premise is adopted. The earlier abstract two-system paper's reported reuse failure keeps its separate pending review; none of its equations is used here. Accepted correlation-recovery and local-component studies retain their scopes.

This file records source review and hand algebra, not simulation, enumeration, implementation or new kernel certification. Pre-publication checks cover source pins, one-file scope, text/format consistency and sensitive material. Independent review should check primary sources, the response-complete/coarse distinction, (1)–(2), the finite-window cone proof, quantum-bound scope and source stop. Off-main references remain research support at their stated scope; a later enduring main claim requires §A.42's dependency/retention audit. No merge or manuscript promotion is implied.
