# INT-FACTOR-1 — A coupled, reversible hidden-sector extension with exactly preserved observer histories

**New WIP · paper-only · 10 November 2026 · NOT independently reviewed.**

**Research owner and issue:** [#1169 OI–QM-EXT-1](https://github.com/amaybaum/incompleteness/issues/1169), with [#1216 APPROX-1](https://github.com/amaybaum/incompleteness/issues/1216) equally prioritized; [#866](https://github.com/amaybaum/incompleteness/issues/866) physical controller/preparation source; [#1143](https://github.com/amaybaum/incompleteness/issues/1143) classical contexts; [#1220](https://github.com/amaybaum/incompleteness/issues/1220) costs, and [#868](https://github.com/amaybaum/incompleteness/issues/868) composite/Bell physics.

**Purpose.** Distinguish "an added sector is an inert spectator" from the more interesting possibility that it **enters both the visible update and the hidden update**, yet the same observer sees an exactly identical full operational history for all its declared protocols. Establish the most precise sufficient condition, construct a non-product three-bit example, provide an actual countercontrol, and state the native physical-source obligations.

**Status.** The mathematics below is **new hand derivation, not an independent review or Lean proof**. The [eleven originally archived papers](README.md), [PREP-HIST-4](12-prep-history4-and-finite-decision.md) and [CARD-GAUGE-1](13-cardinality-observational-equivalence.md) retain their separate pinned review records. Their acceptance is not transferred to this file. No numerical/scientific experiment, external intervention/source, physical premise, F/E, dispatch, merge or manuscript promotion is undertaken.

**Abstract conclusion.** *Microscopic two-way dependence* of hidden and visible coordinates can coexist with identical complete observer histories, even when the coupled dynamics is **not conjugate to the trivial base × any independent one-bit permutation**. The sufficient mechanism is a common **observable factor map** intertwining dynamics, admitted actions and readouts, with compatible source pushforwards. This is a **classical reversible representational equivalence**, not a physically sourced native SM apparatus and not a derivation of QM.

## 1. Exact source boundary

Source-pinned earlier work:

- [CARD-GAUGE-1](13-cardinality-observational-equivalence.md): independent [Codex ACCEPT WITH NITS at c9f0d16c](https://chatgpt.com/space/page_af453671fa5c8191b7c9a5fced83c24a) on normalized decoupled hidden-factor equivalence. It is the **reference**, not the reviewer of the present extension. The current corrected CARD-GAUGE-1 text differs in the three P3 nits and needs separate focused confirmation.
- [Substratum §4 and Theorem 24(iii)](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md): only the **finite decoupled-ancilla** invariance has the previously established status. Propositions 24.3–24.5 distinguish observable predictive factors from raw microscopic fibres; a finite interface does not identify all hidden variables.
- [observer-relative finiteness audit](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/audits/manuscript/observer-relative-finiteness-20261030/DEPENDENCY-AUDIT.md): finite observable resolution does not force total S finite; finite A1 reconstructions keep their exact hypotheses.
- [Native SM physical-interface](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md), [preparation-loading](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md), and [CP-PREP-1 selection](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md): the genuine SM ring is a **different** update. Its physical readout, prep and controller source gate remains **NOT PASSED**. Our three-bit toy update below is *not* imported into that ring.

The core question is **mathematical source-class discrimination**. The additional hypothesis "a physically sourceable interaction implements this factor" is **not** granted.

## 2. INT-FACT: a sufficient factor-intertwining theorem

**Shared operational dictionary.** Fix preparation labels p, a set/grammar of allowed actions and adaptive protocols a, and a common alphabet/σ-algebra of all **accessible** records (including visible outcomes, allowed setting/preparation/controller logs, real failures, aborts and stopping symbols). Distinct models may have different microscopic carriers and dynamics. Do **not** compare protocols involving extra ports available in only one model.

**Finite deterministic formulation.** Let M have finite state space S, reversible update T:S→S, normalized prepared measures μ_p, readout o:S→R and admitted reversible controls I_a:S→S (with record rules depending on S). Let M' have finite S', reversible T', normalized ν_p, readout o':S'→R and admitted reversible controls I'_a:S'→S'. Assume a **surjective** map q:S'→S such that:

    q_*ν_p = μ_p        for every admitted preparation p;
    q∘T' = T∘q;
    q∘I'_a = I_a∘q   for every admitted control a;
    o' = o∘q;

and every other accessible record/status map for the admitted protocol also factors through q, with the same label meaning. The controller chooses its next label from its *already recorded accessible history*, identically in both models.

**Proposition INT-FACT (sufficiency only).** M and M' then have **exactly the same complete accessible-history law** for every finite fixed or adaptive protocol using that dictionary, including all admitted prepared roots. There is no restriction that T' be a product T×ψ, that q be a coordinate projection, that hidden coordinates never interact, or that |S'|=|S|.

**Proof.** For an initial S' state z, the q-image after any admitted update/control word is precisely the corresponding base state obtained by applying the same operational word to q(z); this follows by repeatedly using the intertwining identities. Each accessible record, including the chosen control and any admitted status log, therefore equals the corresponding base record pointwise under this coupling. Because q_*ν_p=μ_p, averaging over the prepared source gives equal probabilities of every fixed finite history. For adaptive protocols, if histories agree through time t, the same feedback policy chooses the same next control; induction preserves the coupling, state-factor identity and all recorded outcomes to the next step. The same argument covers stopping or abort controls if they are in the shared alphabet and factor through q. □

**Limitations.** This is a standard deterministic factor/simulation principle. It is **sufficient**, not a characterization of all observationally equivalent models. Equal laws could exist without any such state-level factor, and a q commuting with passive T alone is not enough for arbitrary measurement instruments or resource readouts. The assumptions about which controls are *physically available* cannot be created by this theorem. The statement uses finite toy spaces; a measurable normalized version needs separately explicit measurability and kernel hypotheses and is not invoked in the example.

## 3. INT-BIT: an exact two-way coupled three-bit extension

**Base model M.** The complete state is (v,r)∈{0,1}², and the observer reads only the visible bit v. Dynamics is a two-bit SWAP,

    T(v,r)=(r,v).

The two request/preparation labels p∈{0,1} set v=p and draw r independently uniform in {0,1}. The shared available reversible control menu includes, for each a∈{0,1}, a visible flip

    C_a(v,r)=(v⊕a,r).

Controls and records may be selected adaptively from earlier visible readouts; p, a, v and timing are the **common operational dictionary**. The hypothesis that these controls are physically implementable is NOT supplied for the native SM ring.

**Extended model M'.** The complete state is (v,h,k)∈{0,1}³ and the observer still reads only v. Under the same preparation label p, draw h and k **independently fair** and set v=p. Define the *single fixed reversible* update and the same labelled visible flip as

    T'(v,h,k) = (h⊕k, k, k⊕v)
    C'_a(v,h,k)=(v⊕a,h,k).

Define the visible-preserving factor map

    q(v,h,k)=(v, h⊕k).

All values are binary. This q is surjective. The prepared q-hidden coordinate r=h⊕k is fair and independent of the requested p, so q_*ν_p=μ_p for both p. Moreover

    q(T'(v,h,k))
        =(h⊕k, k⊕(k⊕v))
        =(h⊕k,v)
        =T(q(v,h,k)),

    q(C'_a(v,h,k))
        =(v⊕a,h⊕k)
        =C_a(q(v,h,k)),

and o'(v,h,k)=v=o(q(v,h,k)). The full INT-FACT hypotheses therefore hold for the declared preparation, update, visible flip and read protocols.

**Exact complete-record consequence.** If no controls are used, the base visible sequence is

    v_0=p, v_1=r, v_2=p, v_3=r, ...,

where r is fair. In M' this same sequence holds with r=h⊕k. With any finite adaptive sequence of the admitted C_a controls, all readout and chosen-control histories still agree **exactly in law**, not merely in a one-step marginal or approximately. The model has no special failure branch; if a future source adds physical failures, those must be included and checked separately.

**Microscopic coupling genuinely runs both ways in the displayed coordinates:**

- v_(t+1)=h_t⊕k_t, so k_t can affect the next visible coordinate;
- k_(t+1)=k_t⊕v_t, so the current visible coordinate affects the next hidden k.

Thus a hidden coordinate is **dynamically coupled** in both causal directions. The equivalence is not the original CARD-OBS independent-product assumption in these coordinates. Yet the q-reduced observable factor retains the simple SWAP process.

This establishes the *existence* of dynamically interacting-looking reversible completions with exactly matched admitted observable histories. It does not establish that every hidden coupling is gauge, nor that the interaction is physically sourced.

## 4. INT-ORD: the extension is not a trivial independent one-bit product in disguise

A potential concern is that the three-bit model might just be a coordinate change of T×ψ where ψ is an arbitrary independent reversible permutation of a *single* ancillary bit k. We can exclude that stronger triviality within this specified state-size comparison.

Compute explicitly:

    (T')²(v,h,k)=(v, k⊕v, h⊕v)
    (T')⁴(v,h,k)=(v,h,k).

For example, at (v,h,k)=(1,0,0),

    (T')²(1,0,0)=(1,1,1) ≠ (1,0,0).

Hence T' has global order **four**, not two. By contrast T²=id on the two-bit base, and **every** permutation ψ of a two-element ancillary state space has ψ²=id. Therefore (T×ψ)²=id for every such independent one-bit product, and no bijective conjugacy can map T' to T×ψ: a conjugacy preserves permutation order.

**Conclusion:** the exact observer-law equivalence need not come from a microscopic dynamics conjugate to a trivial one-bit spectator product. The extra degree of freedom has a genuinely different microscopic recurrence structure. Nevertheless the factor q exists, so this is **still observationally silent skew/quotient dynamics** for the admitted interfaces, not a proof of physically new quantum effects.

**Scope of the exclusion:** this does *not* exclude conjugacy to a product over a differently chosen base/intervention family, a larger ancillary space, or a representation with extra unobserved resources. Nor does it establish a native locality/geometric implementation.

## 5. INT-ACCESS: operational equivalence breaks when the protocol genuinely accesses the added factor

The factor theorem relies on **all** admitted control operations respecting q. A concrete way to break it is to extend the *common* protocol dictionary with a new command K. Interpret K in M as the identity on (v,r), and in M' as the reversible hidden-bit flip

    K'(v,h,k)=(v,h,k⊕1).

The labels/readouts are now common, and the implementations differ. But

    q(K'(v,h,k))=(v,h⊕k⊕1) ≠ q(v,h,k)=K(q(v,h,k)).

Prepare v=p and independent fair hidden sources, tick once and read v_1. Then apply K and tick once more; finally read v_2. In base M the visible outputs are (r,p), with the second output **certainly p**. In M', after the first tick the q-hidden state equals p. Flipping k toggles that q-hidden state to p⊕1, so the next visible output is **certainly p⊕1**. The common-menu recorded histories are therefore distinguishable (indeed disjoint on the second bit, TV **one**). This confirms why the admitted protocol family is a load-bearing premise, not just a description of currently visible coordinates.

If K has *no physically available port* in M' or a genuinely different implementation, this control must not be silently admitted as an experiment. In particular a mathematical ability to write k is not an already sourced embedded-observer operation. The example is a **scope countercontrol**.

It also distinguishes two notions:
- initially hidden (k unobserved directly at a given cut), and
- operationally inert across the **entire admitted intervention family** (q erases its effect on accessible histories).

The first alone does not entail the second.

## 6. Physical sourcing and #1216 comparison

| Obligation | Strongest result of INT-FACTOR-1 | Open physical step |
| --- | --- | --- |
| Classical deterministic dynamics | Two finite reversible updates and an explicit q-factor relation | Real source of the specific dynamics, stable root/hidden prior and admissible intervention ports in the actual OI substratum |
| Two-way hidden-visible dependence | v' depends on k and k' depends on v in the three-bit model | Demonstrate this as one *native*, observer–apparatus process with fixed locality, clock and accessible retained records, not an imported micro-rule |
| Complete adaptive accessible history | Exactly equal for the shared p/C_a/read dictionary | Actual physically executable observer readout, feedback and retry/failure records |
| Cardinality interpretation | Dynamics need not be a trivial decoupled product to be equivalent at fixed O | General interacting-sector classification and physically available enlarged-protocol comparison |
| #1216 approximate QM | Exact operational **TV=0** between these two **classical** toy models at every admitted finite horizon | One physically OI-derived scalable mechanism that approximates a quantum instrument family under preparations, adaptive choices, composition and Born statistics; none supplied here |
| #866 native source | **NOT PASSED / UNSOURCED** remains | Physical source of preparation, controller and readout at the actual SM ring F or an independently justified alternate native carrier |
| #1220 resources | Extended model has 3 microscopic bits versus base model's 2 | Implementation cost/complexity, physical initialization, timing and source law are not equal merely because observable laws are equal |
| #1143 and #868 | The classical-register fragment is preserved | Native coherent controls, joint state/CHSH target, Bell no-signalling and quantum-classical context switching all remain open |

**Native coupling gate:** No function q, T', root producer or controller in this paper is sourced as a subdynamics of the actual SM binary ring (which uses F(X,Y)=(f(X)⊕Y,X)). Substituting the toy bit-permutation for that physical process would violate the provenance rules. The fact that the toy maps are reversible is *not* a physical implementation proof.

**Research interpretation:** The mathematically more interesting finding is that an operational equivalence class can contain distinct **interacting microscopic dynamics**, not merely extra inert states. That supports targeting one common **observable operational theory** rather than reconstructing a unique hidden ontology. But since the example contains only classical bits and reversible permutations, it is *not* selection of QM by OI. It weakens uniqueness expectations without closing the positive existence gap.

## 7. Independent review packet and stopping rule

**Current standing: NEW WRITER PAPER — NO INDEPENDENT REVIEW.** Do not inherit the accepted CARD-GAUGE-1 verdict at c9f0d16c or the accepted PREP-HIST-4 verdict at 4fe17de6. No native program or SCIENTIFIC computation has been executed for this paper.

A distinct reviewer should independently check:

1. Factor theorem assumptions and induction across the shared admissible *adaptive* protocol, full accessible record, failure and stop semantics. Check that q is a sufficient, not claimed necessary, condition.
2. Prepared distributions: p shared; independent fair h,k imply fair r=h⊕k and no hidden p-dependence.
3. Explicit q∘T'=T∘q and q∘C'_a=C_a∘q; precise bit-order convention.
4. True two-way algebraic microscopic dependence v'=h⊕k and k'=k⊕v; do not mistake coordinate dependence for physically sourced interaction or for evidence of a quantum operation.
5. T'^2, T'^4 and order-four witness; conjugacy exclusion restricted to any **two-state independent ancillary permutation** and same base T.
6. Enlarged shared-menu K countercontrol with second visible bit forced p vs p⊕1; TV=1 conditional on fixed root, and why K is outside INT-FACT's original menu.
7. Existing source standing of Substratum Theorem 24(iii), native SM physical-interface, CP-PREP-1; no import of toy gates to SM.
8. Difference between exact classical-history equality and a #1216 Level-B OI–QM mechanism or #1220 scalable efficient simulation.

**Acceptable outcomes:** ACCEPT / ACCEPT WITH NITS / REVISE with exact source and section references. A scoped mathematical acceptance must leave **physical source NOT PASSED** and all QM-premise/closure issues OPEN.

**Next physical-source question after review:** Is there an *independently sourced* reversible observer–hidden–apparatus interaction in the actual SM model for which a nontrivial q intertwines every actually admissible operation and record (not just the passive update)? If not, the positive native source gate remains **NOT PASSED**; no new experiment should run without separate owner authorization.

No PR merge, freeze/F/E, dispatch, numerical/Lean experiment, physical premise adoption or manuscript promotion was authorized or performed.