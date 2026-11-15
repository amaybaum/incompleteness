# SEL-ACCESS-1 — Why passive OI records cannot by themselves select a quantum intervention repertoire

**Writer:** ChatGPT (separate from Codex's #866 native-source writer)  
**Date:** 2026-11-10  
**Status:** **PAPER-ONLY WIP — INDEPENDENT CODEX ACCEPT WITH NITS AT IMMUTABLE `ea8827ff6b4c3e405310216c75bcc32157d069bb`; TWO NONBLOCKING P3 CLARIFICATIONS APPLIED AFTER REVIEW; FOCUSED DIFF CHECK PENDING**  
**Accountable issue:** [#1143](https://github.com/amaybaum/incompleteness/issues/1143) (one bounded unit authorized by [owner comment 6764389038](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6764389038)).  
**Snapshot:** main `cac5d26441dd33e9348151487e4df7b547195481`. No existing reviewed or frozen file is changed by this unit.

**Review provenance:** Separate non-author Codex review [COMMENTED on PR #1224](https://github.com/amaybaum/incompleteness/pull/1224) with **ACCEPT WITH NITS** for the mathematics at immutable `ea8827ff6b4c3e405310216c75bcc32157d069bb` (verified blob `c2b2ddd2efe7984d19bfe08b3a55005fb340b84d`). Reviewer identified P3-N1 (protocol/history type) and P3-N2 (calibrated raw-register continuation), with no scientific blocker. The present revisions address those nits; **they are not themselves independently reviewed**, and the accepted original remains available by exact commit. No physical-source gate or off-`main` evidence obligation is passed by this verdict.

**Central decision.** A rule that selects OI realizations **only by instantaneous embeddedness and passive complete-history probability laws** cannot, in a model class allowing operational menu restrictions, force the existence of additional physically executable noncommuting measurements. Quantum capability is a property of a **whole sourced preparation/intervention/record theory**, not of a passive visible stochastic process. This is a conditional *access-sensitivity obstruction*, not a no-go for OI-derived quantum mechanics or an assertion that a classical fragment is nonquantum behavior.

**Scientific stop:** The stronger claim that OI itself selects the full quantum operational class remains **OPEN / PHYSICAL SOURCE NOT PASSED**. This paper does not source any coherent native operation, Born probabilities, measurement apparatus, Bell pair, hidden probability law, or scalable uniform simulator.

## 1. Scope, semantics and independently checked inputs

Separate four objects before testing a proposed selection principle:

1. **Microscopic realization:** finite reversible world \((S,F)\), initial/preparation laws \(\mu_p\), embedded readout \(o\), apparatus/controller state and all latent registers.
2. **Passive observer law:** complete probability laws \(\mathsf L_{\rm pass}(M)\) for an agreed *protocol set* of passive tick/read schedules and a **separate** set of complete output histories for each protocol, including retained outcomes. Both models use the same calibrated output alphabet, status/failure/stop conventions and record meanings. These probabilities are not the entire operational theory.
3. **Operational theory:** physically admitted preparation labels, executable interventions, allowed sequential/adaptive programs, full accessible records (including failure and stopping), and composite protocols. A menu is an actual availability claim, not merely a formula for an operator.
4. **Quantum target:** a predeclared family of finite-dimensional preparations, instruments, compositions and complete histories. **Soundness** asks whether each admitted OI behavior is target-compatible, while **coverage/completeness** asks whether each required target protocol is implementable in the same OI theory. **Physical sourcing** asks whether the named microscopic devices and probability laws follow from independently justified native physical premises. They are distinct verdicts.

**Standing main sources.** [Main §3.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Main.md) proves the finite-horizon \(S\Leftrightarrow D\Leftrightarrow Q_{\mathrm{fb}}\) fixed-basis record-law representation, which is universal and does not select coherent instruments. [M-1 alternating-W](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oiqmsel-m1-alt-w-20261105/RESULT.md) and [B4′](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/bsel-2-b4prime-20261105/B4PRIME.md) supply *specific* finite-lift complete-record/gauge distinctions. Equality of records under specified procedures is neither arbitrary physical access nor two-sided gauge relatedness. Their theorem classes, physical-source limitations and record domains must remain intact.

**Off-main research control (not promoted to main-proved status).** The independently model-reviewed [#1143 C0/C1 assessment](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218) gives two explicit deterministic countermodels and a "pure composite / mixed marginal" candidate E, with an independently accepted r1a correction to its apparatus-access contract. The reviewed [selection addendum](https://chatgpt.com/space/page_844e90bfb4708191a4d3917c5278bf63) maps source gaps but proves no new selection rule. These Pages are **off `main`** and may inform the *paper-only* critique, not establish a durable result until the claim-relevant proofs and evidence meet [AGENTS.md §A.42](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/AGENTS.md). Below the elementary access-restriction argument is proved independently; the nontrivial C1 construction is cited with its off-main standing, not silently re-proved.

**Frozen design boundary.** [#1210 Phase 1 r7c](https://github.com/amaybaum/incompleteness/issues/1210#issuecomment-6743200254) is a frozen, conditional experimental design: quantum comparator targets, locality design assumptions and unresolved physical mechanisms must not be converted to OI theorems. No #1210 file, gate, metric, frozen rule or authorization is changed.

## 2. SEL-MENU — a necessary access sensitivity of any complete selection principle

**Definition (passive-law predicate).** Fix passive preparation labels \(P_0\) and a set \(\mathcal L_0\) of passive tick/read *protocols* \(w\). For each such protocol let \(\mathrm{Hist}(w)\) be its separate set of complete accessible outcome histories, including a declared failure/stopping convention when applicable. The preparation labels, protocol meanings and calibrated record alphabet are shared between compared models. A selection criterion \(\mathcal S\) *factors through passive laws* when its truth value on any candidate M is a function only of:

- the full collection \(\{\Pr_M(h\mid p,w):p\in P_0,\,w\in\mathcal L_0,\,h\in\mathrm{Hist}(w)\}\);
- properties of the instantaneous embedding/observer cut and the underlying unmodified deterministic dynamics that are **unchanged by deleting operational controls**.

In particular \(\mathcal S\) does **not** inspect whether a prospective additional controller or measurement can be executed. This is an explicitly *restricted* class of selection rules. A principle that constrains **all physically available interventions**, apparatus/source admissibility or composite histories is *not* assumed to factor this way.

**Operational restriction.** Fix a model M with passive tick/read *protocols* \(\mathcal L_0\) and some larger program grammar \(\mathcal L\). Let \(M|_{\mathcal K}\) mean that the same state space, initial passive preparations, unmodified passive dynamics and **calibrated raw readout** are kept, but only programs generated by a smaller allowed operational menu \(\mathcal K\) are admitted. Full accessible outcome histories are compared for protocols actually common to the two menus, under the same labels and record interpretations. New commands missing in \(M|_{\mathcal K}\) have no output law there; they cannot be treated as an arbitrary outcome or silently replaced by a physically unavailable action.

**Proposition SEL-MENU (conditional obstruction).** Suppose the candidate class \(\mathfrak C\) contains both M and \(M|_{\mathcal K}\), where they have identical passive source/readout laws and embedding. For any \(\mathcal S\) factoring through the above passive data,

\[
\mathcal S(M)=\mathcal S(M|_{\mathcal K}).
\]

If additionally \(\mathcal S(M)\) is true and the operational target requires an instrument \(J\) for which **no admitted program** of \(M|_{\mathcal K}\) realizes the target's required complete accessible-history behavior, then \(\mathcal S\) is **not sufficient** to guarantee target completeness throughout \(\mathfrak C\).

**Proof.** Deleting nonpassive commands changes neither the state/readout/dynamics nor the passive experiments and their common preparation laws. The data on which \(\mathcal S\) depends are equal, so its truth value is equal. The target-completeness predicate fails for \(M|_{\mathcal K}\) by the explicit unavailability/non-realizability assumption on J, although \(\mathcal S\) holds. Therefore \(\mathcal S\Rightarrow\mathrm{Coverage}_{\rm target}\) is false for \(\mathfrak C\). \(\square\)

**Exactly which hypotheses matter.** This theorem does **not** assert that *all* physically motivated observer constraints depend only on passive laws, that a quantum-capable OI model exists, or that dropping a nonprimitive command always removes a target operation (another admitted program might implement it). To apply the final clause, J must be unavailable even by the *compositions permitted under the smaller menu*. A source principle that rules out the restricted menu by independently requiring some actual device does **not** satisfy the theorem's closure assumption and could evade the obstruction. This is what an adequate positive selection theory must address.

### An explicit nontrivial classical-preservation control

Take the finite reversible world \((v,h,b)\in\{0,1\}^3\), passive update

\[
\sigma(v,h,b)=(h,v,b),
\]

and the **raw calibrated** visible readout \(o(v,h,b)=(v,b)\), with no context-dependent recoding of that readout. Let the same passive root prepare \(v=b=0\) with hidden \(h\) independent fair. Passive records contain an actual swap-and-readback: after one step the first visible bit reveals h, and after a second step it returns to v. Both models retain valid classical outcomes and repeatable b-readings.

The extended menu additionally admits the reversible visible-bit command

\[
\tau(v,h,b)=(v,h,b\oplus1).
\]

The restricted menu admits passive \(\sigma\) and nondemolition **raw** reads but **no operation changing b** during a run. Both models have exactly the same complete passive histories. Yet the program "prepare \(b=0\), apply \(\tau\), read the raw calibrated b register" yields **raw b=1** in the extended model; any composition of permitted \(\sigma\) and raw reads in the restricted model leaves **raw b=0**. A constant-output report or protocol-dependent relabeling of that value is a *different output*, not an implementation of the target operation under the common record dictionary. If postprocessing is admitted as a separate operation, its records and its effects on subsequent permitted continuations must be explicitly included, and the target requires equality of the **complete raw-accessible histories**, not just one arbitrarily recoded terminal scalar. This is a concrete countercontrol to deriving even a *classical selectable gate* from passive-law equality alone. It is not a quantum no-go by itself; it merely illustrates the operational-menu premise of SEL-MENU.

The wider finite OI core and this swap example have existing source treatments. This section uses a direct proof of the narrow menu distinction rather than claiming a new physical machine.

## 3. Classical countermodels constrain the selection ladder

The following is an **evidence-and-scope matrix**, not an inference that all of its source claims are established on `main`:

| Candidate restrictions | Existing countermodel / control | Supported conclusion at its stated scope | Missing source / reason not to promote |
| --- | --- | --- | --- |
| Finite embedded observer, reversible deterministic world, partial readout and memory/readback (weak B0) | C0 classical reversible swap-memory model in the off-main reviewed #1143 paper; native finite C1–C4 core in maintained records | These requirements allow a classical-simplex completion. They do not **force** the declared full quantum Bell target. | Selecting which preparation and intervention menus are physically available; B0 is not the whole philosophical content of OI. |
| Strengthen to permanent inaccessible hidden bit B∞ | C0 with a driven but operationally erased k under a stated restricted menu | Persistent hidden opacity is **consistent with classical behavior**; added spectator/hidden-gauge structure is not a nonclassical selector. | This example is not observer-minimal; forbidding all such quotients is an independent restriction. |
| Add E: an operationally pure joint preparation with a mixed local marginal | C0 full classical simplex **fails** E by elementary extreme-point/marginal argument; restricted affine C1 *satisfies* E under its uniform Lagrangian preparation/access contract | E excludes a **full simplex** but not all restricted classical probability models. It does not itself establish Bell capability, coherent quantum instrumentation or general Born probabilities. | Physical derivation of E and the non-recoverable apparatus garbage/type restrictions remains **OPEN**. The C1 model and its closure are assessed off-main, not reproduced as established theorem here. |
| E plus a recombination/interference-like detector contrast and classical register fragment | C1 restricted affine-symplectic classical model from the reviewed paper | A **classical** disturbance/recombination analogue can reproduce selected interference-shaped output comparisons while preserving repeatable classical contexts and consistent complete records. | The intermediate meter is a real accessible record; sealed complementary apparatus degrees are excluded by **posited** typed access rules, not by bare OI. |
| Demand full Bell/CHSH target under specified independent-setting, local-wing tests | C0 and C1 admit **only local response maps** in the stated Bell protocol and use a setting-independent source | Under those explicit premises \(|\mathrm{CHSH}|\le2\), so those candidate theories lack the quantum Bell target \(|\mathrm{CHSH}|=2\sqrt2\). | The locality and measurement-independence premises are experimental/test-model conditions, **not** consequences of determinism or of OI. Parameter-dependent or other nonlocal deterministic constructions are not ruled out; no native Bell process is sourced. |
| Actual common quantum-operational theory, with classical measurement subtheories | Still no independently sourced native realization | **Open**: requires an operation/state family with physically supplied preparation, measurement, adaptive control, Born statistics and complete composition; independent soundness/coverage checks. | #866 native source gate NOT PASSED; #1169 exact, #1216 approximate, #868 joint and #1220 resources remain separate. |

### Why E is insufficient, without dismissing classical observations

The full classical-simplex case is easy: extreme points of \(\Delta(X_A\times X_B)\) are the point masses \(\delta_{(a,b)}\), whose A marginal is \(\delta_a\), again pure. Thus E (an operationally pure whole with mixed local restriction) fails for a full simplex with all classical point preparations accessible.

But **a restricted convex subset of classical distributions can have non-point extreme preparations**. The prior #1143 C1 construction takes preparations uniform over affine Lagrangian subspaces of a finite binary phase space, closes them under a stipulated restricted reversible interaction and typed measurement/access contract, and exhibits an extreme joint law with a mixed local marginal. Under its declared local/independent-setting Bell protocol it still obeys CHSH ≤ 2. The existence/closure argument is recorded in the independently model-reviewed off-main assessment; it is **not** a native OI derivation of the preparation restriction, not an accepted main theorem being newly established here, and it does **not** exclude all deterministic models with ontic parameter dependence.

A quantum-capable theory can contain the same kind of ordinary repeatable classical measurement fragment. Therefore the selection question is **not** "how do we forbid classical observations?" It is "what one physically justified repertoire permits quantum-complete contexts *as well as* classical fragments, and excludes operations with nonquantum full-history behavior?"

### CHSH algebra with exposed assumptions

Suppose a pair test admits setting-independent complete latent data \(\lambda\), and under that specific test locality each wing produces \(A_x(\lambda),B_y(\lambda)\in\{-1,+1\}\) depending only on its own setting \(x,y\). Then for every \(\lambda\),

\[
A_0(B_0+B_1)+A_1(B_0-B_1)\in\{-2,2\}.
\]

Averaging against the same normalized \(\lambda\) distribution gives \(|S_{\rm CHSH}|\le2\). This is the usual Bell-local bound; it is not a proof that OI must obey those assumptions. The quantum comparator allows \(2\sqrt2\), using the quantum formalism including Born/trace rules. That comparator is **not** an OI measurement mechanism, and the bound does not itself identify the missing native physical resource.

## 4. What a positive selection principle must do

The **minimum independent obligations**, not a new sufficient axiom package:

1. **Specify the selection's type.** Is it a condition on microscopic dynamics \(\varphi\), accessible preparation laws \(\mu\), the observer embedding, the controller/readout menu, source resources, or the *tuple* of those objects? A criterion formulated on only observed passive marginals is limited by SEL-MENU. An observer access restriction must be sourced, not posited because it protects desired quantum outcomes.
2. **Source a nonpassive context switch in a single realization.** Under the unchanged/native micro-rule or an independently selected physical branch, identify a real preparation/request source, actual interaction, retained record/clock/failure and any available inverse or resetting. Different target contexts must be programs of **one** source-backed realization (or uniform common rule family), not individually re-fitted hidden priors.
3. **Keep a nontrivial classical fragment.** At least compatible preparations and repeatable, record-consistent classical measurements remain operationally possible under the same selection. Test this as a **positive preservation** property, not as an exemption from quantum soundness.
4. **Avoid false quantum capability inferences.** E, ignorance, classical Bayesian filtering, finite fixed-basis quantum representation, non-Markovian readback, order-dependent classical controls and a single disturbance/interference-shaped contrast each fail to prove full quantum coverage. A candidate that matches a finite target law by importing Born or a coherent operator needs separate labels "quantum benchmark" and "native physical source."
5. **Demand both directional checks.** **Soundness:** every physically admitted OI operation/history in the predeclared scope is compatible with quantum operational laws; do not hide incompatible full records as classical fragments. **Coverage:** required finite quantum preparations, incompatible instruments, adaptive switching and composites are available with one common source and correct full histories. In the **approximate** #1216 route each direction needs a quantified error and system/horizon/resource scaling, not just isolated Level-A representations.
6. **Use the existing falsifiers and source gate.** For any proposed positive selection rule, explicitly check C0, C1, the Bell-local conditional subcase, the M-1/B4′ same-record versus gauge separation, and a retained classical context. If a candidate rejects C1, identify the **independently derived** criterion doing so, and explain why it does not merely restate the target Bell/quantum statistics. If no actual intervention source is found under #866, classify the test **UNSOURCED**, not "derivation completed."

**A genuinely stronger direction would be source-first:** specify an executable native interaction process and then establish what preparation/measurement family and record probabilities it yields. This is the separate [#866 NATIVE-INT-SRC-2](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6763916830) writer's task, not something this paper undertakes. The current #1143 paper independently supplies *selection falsifiers and an access-sensitivity criterion*, not that process.

## 5. Stop result and handoff

**SEL-ACCESS-1 outcome (writer assessment, reviewer pending):**

- **Derived in this paper:** the conditional SEL-MENU proposition and the explicit swap/visible-toggle nontrivial classical access control. These are elementary logic/classical reversible examples, not an exotic new theorem or physical discovery.
- **Reused as independently available main records:** Main's \(S\Leftrightarrow D\Leftrightarrow Q_{\rm fb}\) finite-history correspondence; M-1/B4′ mathematical gauge-versus-complete-record distinctions; the already defined native physical-source gate.
- **Off-main external reviewer input (not adopted as main-established evidence):** C0, C1, candidate E, source-specific typed-access necessity and scoped CHSH coverage gap from the independent #1143 paper assessment. Their exact definitions and proof are not re-engineered here. Their evidence must be brought onto main or independently re-established for any later durable scientific claim.
- **Disproved at conditional mathematical scope:** "Passive-law/embeddedness-invariant selection alone universally guarantees coverage of additional executable operations" **in any class closed under operation-menu restriction** containing a selected full/restricted pair. This is not a refutation of all OI observer-selection hypotheses.
- **Still OPEN:** derivation of a physically admissible restriction selecting the full quantum operational class with classical fragments, Born rule and general composite soundness/coverage; the physical source of a nonpassive native intervention; uniform arbitrary-precision Level B and efficient classical resources.

**Priority recommendation:** After independent review, add SEL-MENU as a *negative selection dependency* under #1143 and link #1169. Continue to prioritize #866's separately authorized source-first writer. Do **not** start another passive-statistics or hidden-size programme from this unit.

**No scientific/numerical/Lean computation, experiment, new physical premise, branch rewriting, frozen-design edit, F/E, workflow dispatch, manuscript change or integration to `main` occurred.** This work requires a separate non-author paper review at a pinned SHA and a separate owner decision for any eventual integration.

## Independent review checklist

A non-author reviewer should verify, at an exact immutable draft head:

1. **SEL-MENU quantifiers:** the criterion's passive-law invariance, both models in the class, identical source/readout/dynamics and the *additional assumption* that J cannot be realized by any program in the restricted operational grammar. Verify the proposition does not claim every OI theory is closed under such restrictions.
2. **Concrete C0 restriction:** the swap/flip maps are reversible, the **raw calibrated** b-coordinate is unchanged by every restricted protocol but flipped by the extra command, the passive history laws are exactly identical, any cosmetic relabelled terminal scalar is excluded as a substitute for the same raw register, and a nontrivial readback/classical fragment remains.
3. **Countermodel provenance:** the full C0 and C1/E algebra was accepted **off main** and is not re-proved or upgraded to main-established theorem; the C1 typed live/record/sealed-garbage no-recovery contract remains a **posited** assumption. Check the mixture/pure-state and conditional CHSH statements on their stated interfaces.
4. **Classification:** soundness, target coverage and physical sourcing remain distinct. B0/B∞/E cannot be credited with quantum-generation on the cited evidence, but this does not refute a future source-backed context-dependent OI theory.
5. **Classical preservation:** ordinary compatible/repeatable records are retained as a legitimate quantum subtheory, not excluded as "nonquantum excess."
6. **Scope and controls:** Main §3.4 fixed-basis representation remains intact; M-1/B4′ record/gauge distinctions are not mislabeled as native access; no quantum comparator, Born rule, phase/mixing operator or setting-dependent hidden prior is silently imported.
7. **Governance:** no edits to #1210's frozen r7c or any active Codex #866 branch, and no scientific execution. Any eventual main integration needs the full §A.42 item-8 off-main support audit.

**Requested reviewer verdict:** ACCEPT / ACCEPT WITH NITS / REVISE, with exact mathematical/source scope and named P3/documentary issues. Even ACCEPT would not pass the physical-source gate or establish operational OI↔QM equivalence.
