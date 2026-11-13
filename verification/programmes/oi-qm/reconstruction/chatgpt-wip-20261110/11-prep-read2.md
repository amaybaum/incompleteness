**PREP-READ-2 — Native two-site historical access and earliest possible full-ready certification**

**Writer draft · 10 November 2026 · paper-only · NOT INDEPENDENTLY REVIEWED.** Main homes: [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) equally prioritized; interface sourcing in [#866](https://github.com/amaybaum/incompleteness/issues/866); classical-preserving selection [#1143](https://github.com/amaybaum/incompleteness/issues/1143); composite/Bell work [#868](https://github.com/amaybaum/incompleteness/issues/868); costs [#1220](https://github.com/amaybaum/incompleteness/issues/1220).

**Result:** under the unchanged SM binary ring and the specified canonical-root source, the original two-site mathematical observer's complete local history through two successive forward ticks leaves at least **three of the precursor's five extra Y constraints conditionally fair and unread**. No acceptance rule using only that history and independent randomness can certify the full ready event with conditional probability greater than **1/8**. Two initial worlds that differ in whether they satisfy the event have exactly the same observer history over this window. A third tick is therefore **necessary but not proved sufficient** for perfect passive two-site certification. An explicit initial-state pair shows that the hidden Y5 bit can start to influence the original controller site at the third tick; this is a causal-reach witness, not a functioning herald.

**Sourcing conclusion:** the current formal observer-realization layer supplies a mathematical projection, and the actual F supplies causal information transport. Neither furnishes a native physical seven-site detector or read/hold/route operation. The previously accepted [CP-PREP-1 source gate](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md) remains **NOT PASSED**.

**Provenance:** new paper-only hand derivations and read-only source comparison, not Lean/kernel proof, numerical run, independent ACCEPT, physical construction or manuscript promotion. Existing [PREP-OBS-1](https://chatgpt.com/space/page_3e80b3bdd86c8191a93de7579116c058), [PREP-CORR-1](https://chatgpt.com/space/page_e8d639b1de408191a09a4d7c10f1d9e2), and [#1220 contract](https://chatgpt.com/space/page_472c33bfa4fc819182fe3dd26fbea24f) remain unchanged.

# 1. Pinned model, root, observer and available operations

Source pin: repository main commit [cac5d26441dd33e9348151487e4df7b547195481](https://github.com/amaybaum/incompleteness/tree/cac5d26441dd33e9348151487e4df7b547195481).

Key actual files:

- [SM preparation-loading.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md), blob 1802ea3c335eb7457739fa5af13b3aefd0c603af: actual update, exact eight constraints, two-site two-slice observer, source/counting and no factory

- [physical-interface.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md), blob 3229ef3cd234e613a4b0cb63bab548e0fec666a9: fixed two-site observer access, distinct from physical read/clock

- [ReadWriteControl.lean](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/lean-mathlib/OIBridge/ReadWriteControl.lean): abstract parameterized local permutations, not an executing sensor for this fixed SM ring

- [SubstratumInterfaceAudit.lean](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean): observer permutation theory is defined at configuration-level and does not establish spatially available, clocked F-specific readout routing; the file explicitly does not answer executability

- [Rooted observer-family audit](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/audits/operational/rooted-observer-family-sourcing/result.md): observation projection and canonical shared-root prior exist as realization data, not as a unique physical factory

For ring length L≥9, two-slice initial state W=(X,Y), site labels modulo L, and fixed reversible update

    F(X,Y)=(A,B),  A_i=Y_i⊕f_i(X),  B_i=X_i
    f_i(X)=X_(i−1)⊕(X_(i+1)∨X_(i+2)).

Initial precursor time is t=−1. Fixed incoming visible root b_c: X0=X1=Y0=0 and Y1=c. The canonical root law U_c makes all other X/Y coordinates independent fair bits. The intended full readiness event E_c adds X_(−1)=X2=X3=0 and five Y relations:

    Y_(−2)=X_(−3)
    Y_(−1)=X_(−2)
    Y3=X4∨X5
    Y4=X5∨X6
    Y5=X4⊕(X6∨X7).

The source already establishes U_c(E_c)=1/256 and the one-tick prepared target I_c=F_# U_c(·|E_c).

The **original mathematical observer** sees only the two-slice registers at sites V={0,1}. Its retained history through t=1 comprises its projection of W_(−1)=(X,Y), W_0=(A,X), and W_1=(C,A) with C=f(A)⊕X. A physical memory storing that history is not independently supplied merely by writing this projection.

# 2. Exact dependency calculation through the second forward tick

At t=0, original observer's current bits are

    A0 = X_(−1)⊕X2,
    A1 = c⊕(X2∨X3),

and its previous bits are B0=X0=0, B1=X1=0. Thus the first-tick history accesses none of Y_(−2),Y4,Y5.

At t=1, W_1=(C,A), so the **new current observed bits** are

    C0 = X0⊕A_(−1)⊕(A1∨A2),
    C1 = X1⊕A0⊕(A2∨A3).

At b_c this simplifies to C0=A_(−1)⊕(A1∨A2), and C1=A0⊕(A2∨A3). The expressions A_(−1),A0,A1,A2,A3 depend on the initial Y values at **only** the sites {−1,0,1,2,3}, together with X. Therefore the complete two-site projection history through t=1 depends on initial Y through the set {−1,0,1,2,3} and **does not depend on** the three distinct initial Y coordinates {−2,4,5}, for every L≥9.

Cyclic-index control: for L=9, the latter sites are {7,4,5} while the used set is {8,0,1,2,3}; they remain disjoint. For any larger L they are disjoint as well. Initial source U_c is a product measure over the free Y bits, and its relevant Y_(−2),Y4,Y5 remain independent fair bits conditional on all X, on the other Y coordinates and on the observed history. Their target-required values may be functions of X but cannot change that conditional fairness.

This is an **exact dependency calculation**, not a finite computational search and not an assumption that every mathematically available coordinate can be physically read.

# 3. Proposition READ-2: no perfect herald from two ticks of the old observer

Let H_2(W) denote the entire mathematical two-site/two-slice observed history at t=−1,0,1, and let E_c be full original readiness. For any observed-history atom h with positive U_c-probability,

    P_Uc(E_c | H_2=h) ≤ (1/2)^3=1/8.                 (READ-2)

**Proof.** Condition on all initial X and all Y other than Y_(−2),Y4,Y5; this includes more information than H_2 (by §2). The three omitted Y values are still independent fair bits, and E_c requires each of them to agree with one specified function of X. Their conditional simultaneous probability is 1/8. The remaining five restrictions can only reduce that probability. Averaging first over the other unobserved coordinates conditional on H_2=h preserves the upper bound. □

**Randomized acceptance corollary.** If an accept/reject decision uses only H_2 and additional independent private randomness, then any nonzero-probability accepted set obeys

    P_Uc(E_c | accept) ≤ 1/8.

This is an upper bound on posterior readiness confidence; it does NOT assert a particular history achieves 1/8. Since F² is a permutation, the selected complete output ring-state law, conditional on such an acceptance, differs in TV by **at least 7/8** from the fully prepared target F²_#η_c, by the event F²(E_c). This TV comparison is between **full ring states** and cannot be transferred unchanged to the observer's visible histories.

**Paired-state indistinguishability witness.** Choose any W∈E_c (nonempty for L≥9), and define W' by flipping only the initial bit Y5. Then W'∉E_c. By §2 their two-site histories through t=1 are identical. Thus not even a deterministic perfect classifier can decide E_c for all canonical-root states from this window.

**Time implication.** If no new interaction, site read or observer cut is added, **at least three forward native ticks** are necessary before exact full-readiness certification can become logically possible. This is a *lower bound on earliest possible information arrival*, not proof of a three-tick detector or a reusable native herald.

# 4. Earliest possible influence at the third tick: a conditional differential witness

The previous statement cannot be generalized to “the original observer can never learn Y5.” A local path can carry that influence later.

Take c=0, all initial X coordinates zero, and all initial Y coordinates zero except possibly Y5=b∈{0,1}. For b=0, the complete world stays all zero. For b=1, at first tick A5=1 and all other A values vanish; B=X=0. At second tick C=f(A), and in particular C3=1 while C0=C1=C2=0. At third tick W_2=(D,C) with D=f(C)⊕A. At the original observed controller site i=1,

    D1 = C0⊕(C2∨C3)⊕A1 = 1.

Thus the site-1 current field after three forward ticks differs for b=0 and b=1. The initial Y5 perturbation is **not** perpetually unobservable under the native dynamics.

This witness establishes only **possible causal influence** on one observed bit at three ticks. It does **not** prove that the original observer can infer the Y5 value for every initial X/Y state, that all eight E_c constraints can be inferred jointly from any finite two-site history, or that a physical instrument reliably stores the required information. For larger L the local indices used here are within the specified neighbourhood, so the same hand witness applies without wrapping-induced collisions for L≥9.

# 5. Comparison against existing observer interfaces and physical-source gates

| Interface / source | What is mathematically established | What is actually sourced physically |
| --- | --- | --- |
| Original two-site observer, first forward tick | Posterior full-readiness confidence at most 1/32 on matching outputs (existing PREP-OBS-1) | Mathematical projection only; no real herald/clock/retained apparatus |
| Original two-site observer, two forward ticks | New READ-2 posterior bound ≤1/8 for every history, with three independent hidden Y constraints | Native F executes but read/record/stop protocol is not built; no perfect herald in that restricted mathematical window |
| Third and later passive ticks | Third-tick *influence witness* exists for Y5; later observability/reconstruction of full E_c is **OPEN** | No persistent measurement record or guaranteed decoder established |
| Enlarged seven-site projection after one tick | E_c equivalent to seven output conditions, exact mathematical conditional selection with mass 1/256 (existing PREP-OBS-1) | This changes observer cut and requires seven-site readout, routing, memory, failures and renewal; no native sensor supplied |
| ReadWriteControl / SubstratumInterfaceAudit | Generic local permutation/read-write mathematical structures and configuration-level sourced theory | No certified physical implementation of seven-site measurement, fixed F-specific port routing or a readable classical herald cell |
| Separate CP-PREP-1 source screen | Examined external Fredkin/Toffoli switch is a concrete physical mechanism in its own model | It does not implement the required native F interface; gate remains NOT PASSED |

**Observer embedding:** choosing seven visible sites instead of two still yields a proper subset of the ring for L≥9, but it is a **different observer** with different accessible history. Calling it the original observer's measurement without sourcing a physical information-routing process would change the comparison. In particular, full OI↔QM soundness may restrict which extra hidden fields a physical observer can expose.

**Physical information-flow gate:** the demonstrated native F transport is insufficient for a *registered and retained* success flag unless the actual full-world dynamics includes an executing observation/memory interaction. The abstract read/write family or the act of conditioning a probability measure is not such a source. The first missing positive step is a physically justified reader/transport into the old observer's record **or** an independently justified larger observer cut, with all apparatus states and locality/clock timing retained. Even that would not source the initial canonical root b_c or any renewal.

# 6. What a future native-access candidate must establish

Choose **one** actual source-backed route rather than adding a new target-fitted read operator:

**Option A — same two-site cut (preferred if continuing old apparatus):** identify a physically executable native process that retains a time-ordered read history beyond t=1 and delivers enough information about the remote-predecessor constraints to classify E_c without accessing prohibited coordinates. Use the actual F, fixed source U_c and the original sites; declare the attempted readout, timing, residual state, disturbance, failure/no-read and whether success leaves a usable prepared ring. The first three-tick differential path is a *test cue*, not a derivation of a complete herald.

**Option B — larger observer cut:** justify a concrete proper-subsystem observer whose physical measurement interface directly accesses the seven required output sites at t=0, and show the read is nondemolition or characterize its actual disturbed continuation. The logical seven-bit predicate alone is insufficient; physical access, data collection, record retention and resource cost are the load-bearing changes. If the larger cut accesses additional information inconsistent with a proposed quantum subtheory, that is a separate soundness control, not permission to hide records.

In both cases, first physically source the selectable canonical-root input and its actual uniform hidden-prior preparation (or an alternative independently justified incoming law). An ideal conditional acceptance mass is not a retry probability. A real success flag must have its failed and accepted branches in the same complete-history law, and source/reuse must be accounted as in [#1220](https://chatgpt.com/space/page_472c33bfa4fc819182fe3dd26fbea24f).

This research remains a **classical native preparation/readout diagnostic**. No Born probabilities, Bell state, coherent nonmonomial operation, quantum closure, or classical simulation complexity claim follows from delayed signalling inside this ring. Preserve #1143 classical-register observations and countermodels.

# 7. Independent review checklist and disposition

**Review status: NOT INDEPENDENTLY REVIEWED.** Hand analysis from the same ChatGPT writer and read-only source inspection do not earn a scientific ACCEPT.

A different reviewer should independently check: (1) actual F and full source E_c; (2) second-tick C0/C1 equations and the absence of Y_(−2),Y4,Y5, including L=9 modulo aliasing; (3) conditioning argument that those three bits remain independent fair given all permitted early histories; (4) posterior ≤1/8 and extension to randomized acceptance using independent randomness; (5) output full-state TV≥7/8 and explicit warning against conflating it with accessible-history TV; (6) paired-state indistinguishability through t=1; (7) third-tick Y5 differential witness and why it is not a full herald; (8) compatibility of early/late histories with actual physical clock/memory; (9) physical source standing of ReadWriteControl and SubstratumInterfaceAudit; and (10) acceptance boundaries, failed preparation and classical/quantum programme separation.

Expected review return: ACCEPT / ACCEPT-WITH-NITS / REVISE **for this bounded paper argument only**, with exact source/section anchors, and explicit verification that the result is distinct from the older first-tick 1/32 bound. The physical readout/preparation source remains **UNSOURCED / NOT PASSED** independently of any mathematical verdict.

No special native round, execution/Lean/probes, F/E designation, branch/PR push, physical-premise adoption, manuscript change or merge was performed or authorized by this paper.