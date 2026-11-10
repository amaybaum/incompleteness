# NATIVE-PRED-1 — Exact native two-site predictive-factor capacity and physical-source boundary

**New paper-only writer draft · 10 November 2026 · INDEPENDENT REVIEW PENDING**

**Owner/workstreams:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) OI–QM mechanism/equivalence and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) complete-history approximation retain equal foundational priority; [#866](https://github.com/amaybaum/incompleteness/issues/866) physical preparation/controller/readout sourcing, [#1143](https://github.com/amaybaum/incompleteness/issues/1143) classical-preserving selection, [#868](https://github.com/amaybaum/incompleteness/issues/868) composite/Bell physics and [#1220](https://github.com/amaybaum/incompleteness/issues/1220) total resource accounting remain independent obligations.

**Review provenance:** This new draft follows [Codex's dual ACCEPT](https://chatgpt.com/space/page_b4f63a8bd3a88191a1e9318ec0e3577f) for [INT-FACTOR-1](14-interacting-hidden-factor.md) at 1736a596 and the CARD-GAUGE-1 correction diff. The accepted proof, the original PREP-HIST result and the original eleven research drafts remain unchanged. **The propositions in THIS file have NOT been independently reviewed.** They are hand algebra and source reading, not a Lean/kernel theorem, Boolean enumeration, scientific experiment or physical source pass.

**Headline (scoped):** Under the canonical-root uniform law U_c of the unchanged binary SM ring, the original visible two-site/two-slice observer has **16 positive-probability different first-two-forward-tick histories** at one and the same initial visible root b_c. Hence any passive deterministic autonomous factor q that reproduces these histories must distinguish at least **16 factor states over that initial root**, with Shannon entropy at least 2+2h₂(1/4) ≈3.62256 bits under U_c and fixed-length binary label capacity at least **four bits**. The same holds for each c∈{0,1}, so a single globally defined factor covering both roots has at least 32 distinct states across those disjoint visible-root fibres. This is an *information/predictive-factor* lower bound, **not** an apparatus-memory, energy, efficiency or QM lower bound.

A canonical passive factor exists mathematically as the finite future-trace quotient of the **whole** reversible ring, already covered in substance by [Substratum Proposition 24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md). That factor need not be small or physically readable, and it is **not** an operational factor for unsourced interventions. The physical ready/request producer, observer, controller, recording and renewal remain **NOT PASSED / UNSOURCED**.

## 1. Pinned model and fixed observer dictionary

Actual accepted/source-reviewed binary specialization, at main commit [cac5d26441dd33e9348151487e4df7b547195481](https://github.com/amaybaum/incompleteness/tree/cac5d26441dd33e9348151487e4df7b547195481):

- [preparation-loading.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md), §§3–5, defines the exact F, canonical root b_c, U_c, full eight-constraint precursor E_c and an explicitly **unbuilt** physical preparer.
- [physical-interface.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md) fixes the original mathematical two-site observer and its complete two-slice readout.
- [CP-PREP-1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md) holds the physical-source gate **NOT PASSED**; no new source or native execution is authorized here.
- [PREP-READ-2](11-prep-read2.md) and [PREP-HIST-4](12-prep-history4-and-finite-decision.md) separately analyze readiness recognition. This paper concerns the **autonomous predictive state needed to reproduce general canonical-root histories**, a distinct question.

Fix L≥9; all site labels mod L. Complete initial state W=(X,Y), both binary L-site fields, with actual native deterministic reversible F:

    F(X,Y)=(A,X),           A_i=Y_i⊕f_i(X),
    f_i(X)=X_(i−1)⊕(X_(i+1)∨X_(i+2)).
    F(A,X)=(C,A),           C_i=X_i⊕f_i(A).

The *original two-site observer* reads BOTH slices at **sites 0 and 1**. Write o(W)=(X0,Y0,X1,Y1). The root b_c fixes X0=X1=Y0=0, Y1=c. Under the mathematical reference law U_c, each other X or Y bit is independently fair. This fixed hidden prior is realization data, **not** a physically sourced ring preparer. We retain both c values and their common uncontrolled hidden prior.

The observed length-three sampling window (input plus two forward updates) is

    H₂(W)=[o(W),o(F(W)),o(F²(W))].

Because X0=X1=0 at b_c and previous fields are X then A, under that root H₂ is completely determined by the two successive **current** visible output pairs (A0,A1) and (C0,C1). The historical time convention in the source starts the precursor at t=−1; here T=1,2 denote forward update counts from that starting cut.

## 2. NATIVE-NEXT-2: exact 16-way branching of passive two-update histories

**Proposition (new bounded hand derivation).** Under U_c on the canonical root b_c, the four binary variables

    P=A0,
    Q=A1⊕c,
    R=C0,
    S=C1⊕A0

are jointly independent, with

    P ~ Bernoulli(1/2),
    Q ~ Bernoulli(3/4),
    R ~ Bernoulli(1/2),
    S ~ Bernoulli(3/4).

Therefore **every one of the 16 possible (A0,A1,C0,C1) histories has strictly positive probability**, for both c=0 and c=1; the Shannon information is

    H(H₂ | b_c)=H(P,Q,R,S)=2+2 h₂(1/4)≈3.622556248918266 bits.

**Proof.** Under root X0=X1=Y0=0,Y1=c,

    A0 = X_(−1)⊕X₂,
    A1 = c⊕(X₂∨X₃).

So Q=X₂∨X₃ has probability 3/4 of being 1, and P is independent fair conditional on X₂,X₃ because X_(−1) is an independent fair bit. Thus P and Q are independent.

For the second native tick:

    C0 = A_(−1)⊕(A1∨A₂),
    C1 = A0⊕(A₂∨A₃),

and at the root

    A_(−1)=Y_(−1)⊕X_(−2),
    A₂=Y₂⊕(X₃∨X₄),
    A₃=Y₃⊕X₂⊕(X₄∨X₅).

Condition on **all** initial X bits. The three Y coordinates Y_(−1), Y₂, Y₃ are distinct, unpinned and mutually independent fair bits (L≥9, in fact their distinctness needs much less). Hence A_(−1),A₂,A₃ are conditionally independent fair bits. Therefore S=A₂∨A₃ is Bernoulli(3/4), with a law independent of X (and thus of P,Q); R=A_(−1)⊕(A1∨A₂) is fair and independent of S, P and Q because the free A_(−1) masks everything it is XORed with. Integrating over X leaves the four variables jointly independent with the stated probabilities. Finally H₂ is a bijective re-encoding of (P,Q,R,S) once c is fixed, because A1=c⊕Q, C1=P⊕S, so its entropy and support are precisely those asserted. □

**Probability-level control:** each of the four variables has nonzero probability of either value, so all 16 histories occur. The least per-history probability is (1/2)(1/4)(1/2)(1/4)=1/64; the largest is (1/2)(3/4)(1/2)(3/4)=9/64. These are probabilities in the mathematical canonical-root ensemble, **not** observed physical success/failure rates. No simulation or enumeration was used.

**Scope:** The independence is special to U_c; it should not be transferred to the **prepared**, eight-constraint conditional law η_c. It concerns records through **two** native updates, not all future histories, quantum measurements, or a physical realized source.

## 3. NATIVE-QMIN: the unavoidable hidden predictive-factor capacity

**Definition (passive autonomous deterministic factor).** A candidate factor is a set Q with deterministic update \bar F:Q→Q, factor map q:S_L→Q and visible readout \bar o:Q→{0,1}⁴ such that on the full invariant carrier S_L={0,1}^{2L},

    q∘F = \bar F∘q,
    o=\bar o∘q.

The conditions hold for every state in the stated carrier, **not merely for the initial rooted subset**, because F generally takes b_c states outside b_c. They imply every full passive observable future is a deterministic function of q(W). No control/intervention equivalence is asserted without separately sourced compatible physical control maps.

**Proposition (scoped lower bound).** Every passive autonomous q as above must obey

    |q(b_c)| ≥ 16                                for each c=0,1,
    |q(b₀ ∪ b₁)| ≥ 32                         when both roots are admitted.

Additionally, when W~U_c,

    H(q(W) | b_c) ≥ 2+2 h₂(1/4) ≈3.62256 bits.

Thus any **fixed-length binary code representing all factor labels over a fixed root** has at least four bits of code capacity. That is a lower bound on deterministic predictive-factor state-label capacity, **not** on a physically embodied observer memory register or a thermodynamic cost.

**Proof.** If q(W)=q(W'), then the deterministic factor identity gives q(F^t W)=q(F^t W') for every t≥0; composing with \bar o yields o(F^t W)=o(F^t W') at each time. So W,W' with distinct H₂ cannot share q. NATIVE-NEXT-2 gives 16 positive-probability different H₂ on each b_c, proving the first count. The initial visible root itself is a function of q, so q-images of b₀ and b₁ are disjoint (their Y1 readout differs), proving the combined 32. H₂ is a deterministic function of q(W), so H(q(W)|b_c)≥H(H₂|b_c) by the data-processing/entropy monotonicity under deterministic maps. The binary label conclusion follows from |q(b_c)|≥16. □

**Why this matters:** A two-site readout alone has only one value on b_c; it cannot tell the next 16 possible two-update histories apart. A native factor that claims to be autonomous and predictive must account for at least four hidden-state-label bits' worth of distinction **over this initial root**. Mere geometric closeness of a hidden bit to the observer or causal arrival at one future time does not replace this deterministic factor requirement. This result strengthens the one-step no-autonomous-raw-observer diagnostic without proving any specific proper/small q exists.

## 4. NATIVE-QFUT: a canonical mathematical passive factor exists—but this is not a physical source

Because S_L is finite and F is a permutation, define a future-trace equivalence

    W ~ W'  iff  o(F^t W)=o(F^t W') for every t≥0.

Let Q∞=S_L/~ and q∞:S_L→Q∞ the quotient map, with \bar o([W])=o(W) and \bar F([W])=[F(W)]. The quotient dynamics is well-defined because equal infinite future histories imply equal successor histories. Because the full ring F has a finite order, equal future traces also imply equal predecessor traces, so \bar F is a **permutation** on Q∞. The quotient is a passive deterministic factor; it is in fact the *coarsest* factor which still determines every full future passive readout: any candidate q satisfying §3 must refine this future-trace partition.

This is **not a new theorem unique to this paper**. The passive finite-permutation predictive quotient, its identification using word histories given a state-count bound, and its access qualifications appear in existing [Substratum Proposition 24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md).

**Crucial physical-type distinction:** Q∞ is defined using the entire future of an omnisciently known complete W. The *mathematical existence* of that quotient cannot install an executable readout of q∞ into the already-specified two-site observer, create a finite physical recording register, source a root, generate a selectable controller, or recover a hidden coordinate at a permitted time. Computing q∞ from hidden W would require access not supplied by the original observer. Nor does q∞ automatically intertwine a newly proposed intervention; every actual control needs its own q-compatibility proof.

**Unresolved quantitative problem:** The size |Q∞| for this specific SM ring under this observer, its minimal physically accessible sufficient statistic (if any), and whether Q∞ is a **proper** reduction of S_L are not computed here. The lower bound |Q∞(b_c)|≥16 does not certify a nontrivial reduction; the identity factor q=id always exists mathematically. A large quotient is not an efficient implementable device.

## 5. Prepared-source cross-check and what does NOT follow

Under the accepted **conditional** prepared precursor η_c=U_c(·|E_c), the one-tick output has, among other constraints,

    A0=0, A1=c, A_(−1)=0, A₃=0,
    X0=X1=X₂=0, A₂=z (independent fair).

The second observer output then becomes

    C0 = A_(−1)⊕(A1∨A₂)=c∨z,
    C1 = A0⊕(A₂∨A₃)=z.

Thus the displayed two-update histories for this specially conditioned preparation have only **two** possible z-dependent outcomes, as expected from the already reviewed target law. This does not contradict the 16-way canonical-root conclusion: U_c is the *unprepared* common-prior baseline, while η_c assumes eight hidden constraints, whose physical producer is missing.

An autonomous q intended to work across both canonical source inputs and conditioned ready inputs must satisfy the stronger all-input conditions. If a candidate restricts its domain to η_c, it should say so and check that all actual operations preserve its declared domain. An artificial prior imposed to make q small does not count as a physically selected mechanism.

The one-tick endpoint expressions and the conditional two-tick history are **classical deterministic ring algebra**, not a Born selector, coherent superposition, quarter-phase gate, Bell-pair or no-signalling operational construction. The present bound does not yield a QM sampling-hardness or scalable-efficiency conclusion.

## 6. Source gate and exact next obligation for #1169/#1216

| Question | Current source/result | Next necessary demonstration |
| --- | --- | --- |
| Actual F and two-site projection | Existing source-reviewed SM branch; native algebra as above | Keep unchanged ring L≥9 and original observer meaning |
| Raw two-site o as autonomous state factor | **DISPROVED** on canonical-root class by distinct next output pairs; independently source-checked in Codex INT review | Do not set q=o; retain hidden predictive coordinates |
| At least 16 distinct q states over each canonical root | **NEW WRITER PAPER** NATIVE-QMIN, independent review pending | Independently audit four-variable independence and q-capacity proof |
| Canonical passive q∞ | EXISTENCE (standard finite predictive quotient; [Substratum Prop.24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md)) | Determine whether a *proper small* native factor exists, without confusing this abstract quotient with physical access |
| Actually admitted controller/measurement/record maps | **NOT SOURCED** under #866 CP-PREP-1 gate | Source physically executable initial root/ready producer, readout/clock, allowed actions and failure/remaining-state records |
| Factor intertwinement for admitted actions | **OPEN**; passive q∞ alone insufficient | For a candidate q, verify q∘I_a=\bar I_a∘q for each physically sourced allowed action, including adaptive switching and composition |
| Physical selection of quantum operational subtheory | **OPEN** | Derive mixing, Born, joint-state closure, Bell/no-signalling and classical-preserving quantum experimental scope from the *same* mechanism |
| Approximation #1216 | Existing Level A representability ≠ Level B derivation | Check one source-backed scalable q/interface gives complete-history TV≤ε uniformly as specified; cost/error ledger under #1220 |

**Next paper-only step if reviewed:** A source-qualified *candidate factor* for actual F with a minimal declared observation/intervention dictionary, distinguished from the abstract q∞. Use the one-step/two-step countercontrols above as mandatory falsifiers. Identify physical state coordinates and the concrete device producing, reading and updating any proposed extra register. If no physical producer exists under currently sourced operations, issue a **stopped UNSOURCED verdict**, not a hypothetical success.

**Do not escalate to scientific computation** merely because finite Q∞ exists. Any bounded exact symbolic/Lean/numerical test would require a separate protocol, authorized scope, review and resource budget. Physical source remains **NOT PASSED / UNSOURCED**, and the existing finite-branch A1 premises remain unchanged.

## 7. Independent review checklist and governance

**NEW WRITER-ONLY DRAFT — NO INDEPENDENT VERDICT.** The earlier three independent reviews do not transfer to this paper.

Ask an independent reviewer to check:

1. Pinned F, b_c, U_c and two-site/two-slice observer, including L=9 modular distinctness of Y_(−1),Y₂,Y₃ and X_(−1),X₂,X₃.
2. Four transformed variables P=A0, Q=A1⊕c, R=C0, S=C1⊕A0: all conditional laws and *joint* independence; the min/max per-history probabilities and exact entropy 2+2h₂(1/4).
3. Whether all 16 histories really differ on the **complete two-slice** records despite prior slices and initial root being fixed; prove each attains positive U_c mass without numerical enumeration.
4. Cardinality ≥16 for any deterministic autonomous passive factor over b_c, ≥32 across two disjoint roots, and Shannon entropy vs fixed-length-code distinction. Require full-state q∘F, not an illegal forward update defined only on non-invariant root states.
5. q∞ passive quotient consistency and its **historical attribution to Substratum Prop. 24.4**; no novelty or physical executability claim.
6. Prepared η_c versus canonical U_c comparison, ensuring new 16-state result is not silently claimed under η_c.
7. Missing physically executable preparation, hidden access, control, detector/readout/clock and failure record sources; no inherited INT-FACTOR-1 physical result.
8. Clear #1169/#1216/#1220 source/approximation/complexity separation and no imported quantum-Born or hidden-cardinality premise.

Review result should be **ACCEPT / ACCEPT WITH NITS / REVISE**, tied to immutable head and exact file. Even an ACCEPT would be for this bounded mathematical finding, not native OI–QM physics.

**No simulation, Boolean enumeration, scientific/Lean run, proof-kernel compilation, new physics premise, PR merge, F/E designation, dispatch, manuscript promotion or physical-source success occurred.**