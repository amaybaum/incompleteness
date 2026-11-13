**OI–QM Bell source obligation, unit 2 — writer assessment v1 · 9 November 2026 · PAPER ONLY · AWAITING INDEPENDENT REVIEW**

**Owners/issues:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) (physical condition / equivalence) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) (approximation), **equal priority**; [#1143](https://github.com/amaybaum/incompleteness/issues/1143) (classical-preserving selection), [#868](https://github.com/amaybaum/incompleteness/issues/868) (pair source/composition) and [#1220](https://github.com/amaybaum/incompleteness/issues/1220) (total costs). Companion writer drafts: [CHSH operational floor](https://chatgpt.com/space/page_1a978cad60588191ac7a5aaf5bce1d) and [robust preparation-span theorem](https://chatgpt.com/space/page_66750b14a1dc8191a59a3c3dba1ae8f1). Existing independently reviewed documents remain unchanged.

**Claim classification.** The sources support a physical-source **STOP/UNSOURCED** for the current SM prepared-long-edge route. New here are two explicit conditional mathematical propositions: (A) a lower bound on the amount of response-complete ontic remote-setting sensitivity required for CHSH approximation; (B) a sufficient uniform-symmetry condition for no-signalling of complete accessible histories. Neither proves that OI physically generates the needed preparation, makes the proposed coupling executable, selects the quantum bound, or derives Born probabilities. A countercontrol implements PR correlations as a reversible response table, exhibiting insufficiency of symmetry and ordinary classical-register preservation.

**Independent review: NOT PERFORMED.** The writer's proofs and source reading do not count as an independent review. No numerical/scientific execution, Lean, new physical posits, branch/PR, freeze/F/E, dispatch, manuscript promotion or merge is authorized by this assessment.

# 1 Pin and source starting point

Read the following against the maintained-corpus source pin [cac5d26441dd33e9348151487e4df7b547195481](https://github.com/amaybaum/incompleteness/tree/cac5d26441dd33e9348151487e4df7b547195481), and retain all conditional language:

- [Main §3.3](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Main.md#L367): coupling-graph cone and screened-local Bell bound; adopted **option** of ontic parameter dependence with measurement independence stated as a posit; state/preparation-dependent long-edge *proposal*; physical H-Bell remains open.

- [SM §3.1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/SM.md#L100): state-dependent-geometry proposal; fixed reversible ring with right-neighbour selector depending only on nearby field values; the actual support of the selector is local, not a dynamically materialized distant Bell link.

- [#868 prepared-pair source paper](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/prepared-pair-source.md): exact balance equation Cμ=0 for complete local histories and exact affine-spanning test for ontic locality, with native pair/preparer **UNSOURCED**.

- [#868 operation-source paper](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/pair-operation-source.md): modifying the graph/update does not automatically source new native available observer operations; unchanged-interface ceilings are conditional, not a universal OI no-go.

- [Controller LEAD](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/physical-controller-20261107/LEAD.md): required common ready/request preparation and its physical producer, clock/herald and renewal remain missing for that *particular* ring-loading lead.

- [Accepted #1143 countermodels](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218): classical C0 and restricted-affine C1 show weak OI+E conditions do not suffice; classical measurement fragments are legitimate and must be preserved.

- [Accepted #1220 resource contract](https://chatgpt.com/space/page_472c33bfa4fc819182fe3dd26fbea24f): end-to-end physical and algorithmic resource ledgers remain separate; neither deterministic dynamics nor cheap local updates establish a scalable classical quantum sampler.

External conceptual comparison (not imported as physical sourcing): [Valentini, Signal-locality in hidden-variable theories](https://arxiv.org/abs/quant-ph/0106098), [Wood–Spekkens causal fine-tuning paper](https://arxiv.org/abs/1208.4119), and [Popescu–Rohrlich original superquantum negative control](https://research-information.bris.ac.uk/en/publications/quantum-nonlocality-as-an-axiom/). These works motivate careful handling of hidden equilibrium, no-signalling cancellation, and the fact that no-signalling alone does not select QM.

# 2 A sharper quantitative condition: remote-setting-sensitive ontic weight

Fix exactly the binary CHSH experiment, with `x,y∈{0,1}`, `a,b∈{−1,+1}`, uniformly and independently sampled settings, and one **response-complete, setting-independent** pre-setting hidden state `λ∼μ`. For every `λ`, deterministic evolution with each of the four possible setting pairs defines outcome functions `A_{xy}(λ),B_{xy}(λ)`.

Define `Λ_loc` as the set of hidden states for which `A_{x0}(λ)=A_{x1}(λ)` for each `x` AND `B_{0y}(λ)=B_{1y}(λ)` for each `y`; then the first outcomes on that λ can be written `A_x(λ),B_y(λ)`. Set `q:=μ(Λ\Λ_loc)`. This **counterfactual sensitive weight** is a probability over pre-setting states; it is **not** an observed rate of superluminal transmission, a physical gate-use flag, or the probability that a randomly selected actual setting pair reveals a difference. It is defined for a fixed experiment and access/response completeness contract.

**Proposition W-CHSH (new paper proof; independent review pending).** Under these hypotheses, the candidate CHSH expectation obeys

`S_P:=E_P[ab|00]+E_P[ab|01]+E_P[ab|10]−E_P[ab|11]≤2+2q.`

**Proof.** For each λ in `Λ_loc`, the pointwise CHSH score is `A_0(B_0+B_1)+A_1(B_0−B_1)∈{−2,2}`. For each λ outside `Λ_loc`, no factorization is assumed; the four signed products are each ±1, so the score is at most 4. Because one fixed source `μ` is used for **all four** setting pairs, averaging gives `S_P≤2(1−q)+4q`. □

The ideal quantum comparator is the Bell-pair CHSH target with `S_Q=2√2`, computed using the comparator's *supplied* quantum Born rule. Reproducing that benchmark exactly requires

`q≥√2−1≈0.41421356.`

If `TV(P_H,Q_H)≤ε` on a declared **common complete accessible-history alphabet**, and their uniform setting/outcome marginal is the stated CHSH one, then the bounded witness `4s_{xy}ab` gives `|S_P−S_Q|≤8ε` by data processing and the TV dual bound. Consequently,

`q≥max{0,√2−1−4ε}.`

This is a *necessary physical-interface condition conditional on the settings and counterfactual outcome hypotheses*, not a sufficient quantum mechanism, not a time/energy lower bound, and not a universal theorem about every deterministic OI branch. Excluding measurement dependence, ontic nonlocality or changing the accessible Bell protocol changes its applicability; no alternate setting-correlation route is silently ruled out.

# 3 Sharpness of the 41.4% threshold on the declared marginal

**Outcome-only control.** Define balanced binary-outcome boxes

`Q_v(a,b|x,y)=¼(1+ab\,v\,s_{xy})`, with `s_{00}=s_{01}=s_{10}=1,s_{11}=−1`.

For the four-setting Bell comparator `v=1/√2`. A local box `L=Q_{1/2}` is obtained by uniformly mixing the eight deterministic local tables that achieve CHSH +2 (choose the unique losing setting among four, and a simultaneous outcome sign flip). The PR box `N=Q_1` has no-signalling marginals but CHSH=4. Set `q=√2−1`. Then

`(1−q)L+qN=Q_{1/√2}`.

A response-complete deterministic realization can use a pre-setting mixture flag and shared randomness; its local component has pointwise factorization and its PR component has nonlocal response tables. Therefore `μ(Λ\Λ_loc)=q` in that supplied response construction, and W-CHSH is **sharp for this marginal comparison class**.

This is an abstract finite response construction with a supplied mixing weight. Since `√2−1` is irrational, a finite *uniform counting* source does not reproduce that exact weight without an additional law/limit; rational approximations can approximate it. No nonlocal source, hidden-law factory, physical native gate, complete-history closure, Born rule, or quantum composition has been derived. The sharpness example is **not** an acceptable physical source candidate on its own.

# 4 Native SM ring: a concrete finite-speed source obstruction

At `q=2`, the actual ring example in [SM §3.1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/SM.md#L104) has

`f_i(u)=u_{i−1} XOR (u_{i+1} OR u_{i+2})`, and `F(u,v)=(f(u) XOR v,u)`.

The full phase-space slice has two binary fields at each ring site. Both the selected neighbour values **and** the selector input belong to the actual step dependency. Hence the update of site `i` depends only on previous phase-space coordinates in the cyclic radius-2 ball `B(i,2)`; the previous-slice value at `i` is local.

**Proposition R-CONE (paper induction, scoped).** Let a setting change act only on a specified site set `A` and its declared local apparatus coordinates at the setting time. Suppose all subsequent native updates and controller couplings obey this radius-2 locality on the **whole response-relevant carrier**, and the isolated observed history before time `t` is read only in a region `R`, including the actual accessible logs there. Then changing the setting at fixed initial response-complete state cannot affect `R` by time `t` if `d_{ cyclic}(A,R)>2t`.

**Proof.** At time zero the difference support is in A. If all input differences are confined to `B(A,2k)`, every radius-2 update agrees outside `B(A,2(k+1))`; induction yields support contained in `B(A,2t)` after t updates. Local recorded histories have the same prefixes whenever the read regions lie outside the difference support. □

**Corollary.** If both Bell-wing setting/read regions satisfy the corresponding greater-than-`2t` separation during the entire declared measurement windows, and the common response-complete pre-setting law is setting-independent, `q=0`. The screened-local CHSH ceiling is 2; from the previous writer draft, the ideal Bell marginal then remains at least `(√2−1)/4` in TV distance. Merely increasing a *locally updated hidden memory* or loading a better common initial source cannot overcome this particular finite-window obstruction.

Conversely, if a setting is to affect a readout at cyclic distance d **through this unchanged local ring**, an onset before `ceil(d/2)` native ticks is impossible (under the declared local setting/record contract). A physically prepared long-edge graph could change the dependency radius and escape this lemma, but such an edge and its producer are not supplied by the ring. Even if the cones meet later, that alone does **not** guarantee Bell correlations or no-signalling. These ticks are graph-time units, not derived relativistic light-cone or complexity bounds.

# 5 A physically meaningful sufficient symmetry condition, and its limits

A possible *source-independent criterion to check* is an actual symmetry of native dynamics and preparations, rather than defining allowed sources by solving `Cμ=0` for a target table.

**Proposition SYM-BAL (conditional paper lemma).** For a given wing B, fixed local policy `β`, and two distant policies `α,α'`, let `H_B^{αβ},H_B^{α'β}:Λ→ℋ_B` be the deterministic **complete accessible-history maps**. If the physical source `μ` is invariant under a measurable bijection `T:Λ→Λ`, i.e. `T_#μ=μ`, and

`H_B^{α'β}=H_B^{αβ}∘T`,

then the two complete local-history laws coincide. If, for every admissible preparation and isolated policy comparison on both wings, actual native symmetry transformations satisfy these properties, complete-history operational no-signalling follows.

**Proof.** `(H_B^{α'β})_#μ=(H_B^{αβ})_#(T_#μ)=(H_B^{αβ})_#μ`. □

**Interpretation.** A common reversible update has invariant counting measure on its finite whole carrier; this is a mathematical source fact. It does **not** prove physical production of uniform microstates under selected preparation, or that there exists a transformation `T` relating the *specific remotely changed* history maps. Ordinary translation invariance of the ring is not by itself such a Bell-specific transformation, especially with fixed wing labels, programmed settings and observer records. For a reusable candidate, the symmetry must survive physically available conditioned preparations and adaptive continuations, including failures and acquired controller information. This is not established.

**No-signalling is weaker than quantum selection.** Even SYM-BAL plus classical-register operation availability fails to rule out a PR-box hidden response table, as the next control shows. A later positive candidate still needs a sourced probability law, the quantum upper bound, complete joint-state compatibility, reuse and context switching.

# 6 Exact nonquantum control: reversible PR response and access boundary

Let `x,y,r,a,b∈{0,1}` be setting bits, one shared hidden bit, and initially blank output cells. The fixed **global** reversible Boolean map

`G(x,y,r,a,b)=(x,y,r,a XOR r,b XOR r XOR (x AND y))`

is an involution, since all controls `x,y,r` are unchanged and the two targets are XOR-updated by fixed functions of them. Prepare `r` as an **assumed** setting-independent fair bit; begin `a=b=0`. The two recorded outputs are `a=r` and `b=r XOR xy`. Therefore `a XOR b=xy` identically. Each single-wing output is fair for every setting pair; CHSH reaches 4, the PR benchmark. This is an instance of arbitrary supplied response-law representation, **not a sourced SM/GR operation**.

For Bob with `y=1`, changing the remote x from 0 to 1 transforms the output `b=r` into `b=1−r`. The relabelling `T:r↦1−r` preserves the assumed uniform law and satisfies SYM-BAL **for the outcome-only Bob history**. Alice's outcome is independent of y pointwise. Hence *a symmetry-backed source can conceal ontic remote influence at the output level while permitting beyond-quantum correlations*. This falsifies any assertion that equilibrium/symmetry/no-signalling by itself selects Born probabilities or Tsirelson's limit.

**Crucial complete-history negative control:** If Bob can later read the hidden r while retaining b, then `b XOR r=xy`, and at `y=1` he learns Alice's x. The complete Bob histories `(b,r)` are then disjoint for x=0 versus x=1; SYM-BAL's required history-map relation fails for that *enlarged* accessible record. One must physically justify any inability to recover r, including indirectly via interference/recombination, rather than simply declaring it hidden forever. This is why the #1143 access-contract correction and #868 complete-history balance are load-bearing.

**Classical-fragment control:** Independent classical-register cells can be appended and reversibly copied using XOR into blank record cells. That shows **logical compatibility with classical records**, not that OI natively permits this specific global nonlocal program, its controllers, or physical preparation. The PR model is a *negative control for insufficient selection principles*, never a proposed quantum mechanism.

# 7 Source-gate assessment for a native prepared-long-edge route

The first positively sourced step is limited: SM permits state-dependent graph dynamics and demonstrates a bounded-range reversible ring update. The global response table of §6 is **not** that ring and cannot be imported as its missing long-edge operation.

| Gate | Concrete native source evidence required | Current status |
| --- | --- | --- |
| **P / preparer** | One autonomous process produces a Bell-relevant shared pair/edge and an accountable request/ready state under a single law, with source distribution, physical herald, failures, outgoing state and renewal | **UNSOURCED**; reviewed #868 pair source stops here; controller-lead precursor/renewal is separately unsourced |
| **G / propagation** | Full state-dependent functional-dependency graph including selector inputs actually carries a remote setting to the other wing's response inside the isolation window | **NOT DERIVED** for a prepared Bell pair; R-CONE excludes separated influence in the unchanged radius-2 ring |
| **O / operation & access** | Available executed wing policies, pointer/read/copy interfaces, sealed or retrievable ancillary information, with actual classical fragment retained | **OPEN**; no free hidden-data sealing or mathematical operator-to-gate promotion |
| **B / equilibrium & no-signalling** | Sourced `μ` and permissible `𝒫` satisfy all-policy complete-history balance; a physically generated relabeling or stronger conservation mechanism might explain cancellations | **OPEN**; SYM-BAL is merely conditional and PR shows its insufficiency |
| **Q / quantum selection** | Bell target, Born exponent/record probabilities, Tsirelson/superquantum exclusion, joint-state closure, compositions, switchable classical and quantum regimes | **OPEN**; W-CHSH only gives a necessary ontic sensitivity weight |
| **R / scaling** | All source, controller, read, error, memory, retry, precision and renewal costs bounded in the succinct target input | **UNDETERMINED** under accepted #1220 r1a |

**First physically missing step:** an independently motivated, actually executed pair/long-edge preparation with a fixed law and declared source. Merely adding a long edge by hand is a new posit. If a later source passes P/G/O, try to prove an actual source symmetry/invariance such as SYM-BAL **before** using quantum target data. Neither balancing nor positive CHSH alone establishes quantum-only selection.

**Disposition:** maintain the **UNSOURCED** physical source verdict. Keep #1169 and #1216 equally prioritized; carry W-CHSH and R-CONE as paper-level necessary conditions under explicit hypotheses. Keep the accepted #1143 classical-preservation countermodels as controls and #945 finite-bit repair in its own workstream.

# 8 Cost and approximation crosswalk (#1216 / #1220)

The new constraints are **operational possibility** constraints, not classical time hardness.

- **Approximation:** for a common setting-independent deterministic hidden response model with sensitivity weight q, `TV(P_H,Q_H)≥max{0,(√2−1−q)/4}`. For q=0 this reduces to the earlier 10.36% local floor. It is a lower bound on **complete-history TV** by projection to CHSH, provided the benchmark histories and accessible output mapping are fixed.

- **Native ring update:** the binary two-slice ring carries `2L` bits, with `O(L)` Boolean operations and `O(L)` working memory per full global native tick for an explicit sequential representation. A `T`-tick literal update costs `O(LT)` Boolean work, *conditional on the whole input state and controller instructions already being provided*. This is a cost of the ring update, not a uniform BQP-circuit simulation bound.

- **Graph-time propagation:** an influence between setting/write set A and a read region at cyclic distance d requires at least `ceil(d/2)` ticks under the unchanged local ring assumptions. Graph-time says nothing on its own about physical `c`, relativity, or BQP/BPP complexity.

- **Preparation:** obtaining any particular hidden ensemble, establishing the response-complete source independence across settings, and repeating a physically valid pair-preparation are not costed by merely assuming an invariant counting measure. For the current controller lead, the producer of the shared ready/request precursor and renewal are missing. An ensemble mass is not an accessible success probability.

- **Remote-sensitive fraction:** q is a probability of **counterfactual dependence**, not a fraction of observable nonlocal-gate launches; hence `q≥41.4%` gives no direct joule, time, communication or sampling-cost lower bound.

- **Strong versus weak simulation:** a reversible PR response-table control has cheap mathematical sampling for its specified one-shot target, but does not show efficient native quantum computation or even the ability to prepare that control under OI.

All three existing #1220 outcomes remain possible for a separately sourced, specified native scalable interface: efficient weak classical simulation; a proved scoped obstruction under explicit complexity assumptions; or undetermined. Under the current source gap the third classification applies to the full programme.

# 9 Proposed independent review and exact acceptance conditions

**REVIEW NOT PERFORMED.** This Page is a request-ready bounded paper draft. A separate reviewer must not be represented as having accepted it merely because the writer has supplied proofs. No human/agent reviewer was automatically dispatched.

Review questions, in order:

1. **W-CHSH / essential scope.** Are all four counterfactual response pairs defined on a response-complete **common pre-setting** λ without importing measurement independence beyond its stated premise? Does `q=μ(Λ\Λ_loc)` refer to **first outcomes** rather than arbitrary hidden data? Is the pointwise split `≤2` vs `≤4` correct, and the `8ε` TV-to-CHSH factor correct? Does the statement avoid interpreting q as communication rate?

2. **Sharpness.** Check the local eight-table mixture `Q_{1/2}`, deterministic PR response, and `(1−q)Q_{1/2}+qQ_1=Q_{1/√2}`. Confirm no exact irrational Born weight is claimed to arise from a finite uniform counting source.

3. **R-CONE.** Check the actual SM ring selector dependence, phase-space two-slice update, radius 2 per native tick, location of controller writes/reads, and the strict separation `d>2t`. Ensure new long edges, global apparatus or hidden setting correlations are not silently covered by the theorem.

4. **SYM-BAL and PR control.** Check pushforward argument for **complete histories**, the distribution-preserving relabeling criterion, its failure after r becomes accessible at Bob, and the global Boolean map's involution property. Do not mistake it for an SM physical mechanism.

5. **#1143/classical preservation.** E is not sufficient, restricted affine C1 remains a valid negative control, and classical records survive without allowing arbitrary garbage recovery. No target-defined Bell table is introduced as a source condition.

6. **#868/operation source.** Verify that the measured "first missing step" is one native pair/long-edge preparer and corresponding operation, with controller-lead ready/request renewal correctly separate.

7. **#1216/#1220.** Check that quantitative TV floor and q bound are only operational bounds, cost terms are conditional, #945 stays separate, and no BQP/BPP conclusion follows.

Requested reviewer output: **ACCEPT / ACCEPT-WITH-NITS / REVISE**, exact blocker quotes and line/section anchors, source/reference challenges, and a verdict on whether the new result is genuinely not already supplied by Main/#868. If a substantive overlap exists, mark it as a **derived corollary or re-expression**, not an independent discovery.

Existing experimental authorizations, Project statuses, GitHub PR states, F/E/CI/dispatch and manuscript/merge gates remain unchanged.