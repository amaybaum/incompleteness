**PREP-CORR-1 · Native correlation-origin assessment, 10 November 2026 · PAPER ONLY / WRITER DRAFT**

**Research focus:** Can the **actual unchanged SM reversible update** produce useful ring–apparatus/observer correlations from an independently motivated input, instead of assuming a target-fit correlated law? The answer is **YES, conditional on a prepared canonical visible root**; **NO, from the fully uniform global counting source by closed passive reversible evolution**. The existing ring's one-tick correlated outputs do not create the missing eight-bit full precursor resource or constitute a physical preparation factory.

**Main paper finding:** under the already declared canonical-root law, one native step makes 1+h₂(1/4)≈1.811278 bits of previously hidden Boolean information available in the mathematical two-site observer record and creates the same amount of inter-slice mutual information. This uses the actual F, not an imported SWAP/XOR operation. However the initial root already fixes four coordinates, and the full ring's entropy remains invariant. The required full eight-condition precursor remains **UNSOURCED**.

**Issue accountability and retained priority:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) equally prioritized; [#866](https://github.com/amaybaum/incompleteness/issues/866) native controller/preparer, [#1143](https://github.com/amaybaum/incompleteness/issues/1143) classical-preserving selection, [#868](https://github.com/amaybaum/incompleteness/issues/868) pair/Bell composition, [#1220](https://github.com/amaybaum/incompleteness/issues/1220) total physical/classical resources.

**Evidence status:** Source reading and analytical hand proofs by the same writer; **NO independent review, Lean/kernel/numerical execution, native experiment, PR, issue edit, adoption or merge**. The existing [PREP-NATIVE-2 conditional capacity work](https://chatgpt.com/space/page_c4b1b4bda5cc8191942f95b5d9a4b2fb) is also a writer draft and is not promoted to independently accepted status. This paper's stronger visible two-site bound is new **relative to these writer drafts**, not claimed a novel result in the wider literature.

# 1. Source pins and precise observer contract

Pinned main: [cac5d26441dd33e9348151487e4df7b547195481](https://github.com/amaybaum/incompleteness/tree/cac5d26441dd33e9348151487e4df7b547195481). Sources actually read:

- [preparation-loading.md, blob 1802ea3c](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md): the ring F, input root b_c, eight extra predecessor constraints, complete declared two-site records, status of conditional source law, and no available factory.

- [rooted observer-family audit, blob 34ea388d](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/audits/operational/rooted-observer-family-sourcing/result.md): a canonical common-prior **realization datum** exists at the maintained observer layer, but its physical producer/choice among structured laws is not thereby derived; the reduced substratum alone does not select a unique prior.

- [physical-interface.md, blob 3229ef3c](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md): a two-site observer includes **both controller and receiver registers on both slices**, and no physical sensor, setting generator or reset is silently implied by mathematical projection.

- [CP-PREP-1, blob 736ea7e3](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md): the examined external switch does not provide an executing native preparation interaction in the fixed ring; source gate remains NOT PASSED.

Fix ring size L≥9, N=2L and fields X,Y∈{0,1}^L. The **actually declared** reversible step is

    F(X,Y)=(A,B)=(f(X) XOR Y, X)
    f_i(X)=X_(i−1) XOR (X_(i+1) OR X_(i+2)).

For a *known fixed desired setting c* the canonical-root law U_c is uniform over

    b_c: X_0=X_1=Y_0=0, Y_1=c.

All other bits—including X_(−1),X_2,X_3—are independent fair bits. The observer projection at t=−1 exposes sites 0 and 1 on both slices, hence b_c is visible and fixed. At t=0 the same observer's mathematical projection contains (A_0,B_0,A_1,B_1), where B_0=B_1=0; a real read/logging device is still a physical-source obligation.

# 2. Proposition CORR-1 — one genuinely native readout of two hidden functions

Using X_0=X_1=Y_0=0 and Y_1=c in the fixed F, derive the exact native identities

    A_0 = X_(−1) XOR X_2 =: U,
    A_1 = c XOR (X_2 OR X_3) =: c XOR G.

Here U and G are functions of **initially hidden X coordinates relative to the declared observer cut**. X_(−1) is an independent fair bit, so conditional on (X_2,X_3), U is fair. Consequently U is independent of G, U~Bernoulli(1/2), and G~Bernoulli(3/4). This is an **exact** conclusion from the canonical-root realization law, not an approximation or a quantum comparator.

The observer's first two output bits (A_0,A_1), together with its already known setting c, determine U and G. Thus

    H(A_0,A_1 | c) = H(U,G)
      = 1 + h₂(1/4)
      = 3 − (3/4)log₂3 ≈ 1.811278 bits.

Because the output is a deterministic function of the original hidden X field, its mutual information with that field is exactly

    I((A_0,A_1); X | c) = 1+h₂(1/4).

**Interpretation:** the *existing native F* creates a nontrivial observer-relative readout of hidden information in one mathematical tick. This is the same known mechanism that supplied the earlier syndrome G, now with the independent receiver signal U included. It is a precise positive native **information-transfer** result; it is not an autonomous preparation of the incoming root, a verified hardware read, or evidence that hidden dynamics select the Born law.

# 3. Proposition CORR-2 — exact inter-slice mutual information and conserved source budget

Initially, under U_c, X and Y are independent, because their four fixed coordinates impose no cross-slice correlation; hence I(X;Y|c)=0.

After the native F, B=X. Conditional on B, the two output bits A_0 and A_1 are fixed functions of B, while every A_j for j≠0,1 remains an independent fair bit because its incoming Y_j was a free, independent fair bit. Those L−2 other outputs are also independent of B and of (A_0,A_1). Therefore

    H(B|c) = L−2,
    H(A|c) = (L−2)+1+h₂(1/4),
    H(A|B,c) = L−2,

so

    I(A;B | c) = 1+h₂(1/4) ≈ 1.811278 bits.

This is a genuine *correlation increase between the time-slice factors* (from zero), created by one application of the unchanged native reversible update.

**Crucial accounting:** this is **not entropy creation from a completely disordered global state**. Under U_c the whole ring contains N−4 bits of Shannon entropy, i.e. 4 bits of relative entropy to the full uniform law Ω on 2^N states. Because F is a permutation,

    H(F_#U_c)=N−4,     D(F_#U_c || Ω)=4 bits.

The four-bit deficit partitions exactly into

    D(P_A || Uniform(A)) = 1−h₂(1/4),
    D(P_B || Uniform(B)) = 2,
    I(A;B) = 1+h₂(1/4),

and their sum is 4. The original four fixed root coordinates supply the information/order that F redistributes into observable marginal bias, fixed B values, and A–B correlations.

**Setting scope:** all entropy and mutual-information identities above are **conditioned on the known fixed setting c**. Averaging over unknown random c without retaining the setting record can change the unconditional information values and must not be conflated with these experimental conditional laws.

# 4. Proposition CORR-3 — no spontaneous source from global uniform equilibrium

Let Ω be uniform on the *entire* 2L-bit world, without any conditioned root. Since F is a permutation, F_#Ω=Ω. Under Ω, the new slices A and B remain independent, jointly uniform binary vectors:

    I_Ω(A;B)=0.

This conclusion holds for every fixed deterministic F^t and every fixed coordinate split of the complete world, because uniform counting on the entire finite Cartesian state set remains uniform under any permutation.

**First source stop:** neither the four-bit root b_c nor the extra eight hidden precursor constraints can become guaranteed merely by waiting for passive closed-ring dynamics from Ω. For each fixed setting c and any predetermined tick, the event b_c has Ω probability 1/16 and the stricter event E_c has Ω probability 1/4096. A mathematical conditioning on b_c gives a legitimate canonical-root realization, not a physical herald, controller or source law generated autonomously by F.

A root distribution with H=N−4 can be transported by F to create the correlations of CORR-2; it cannot produce the *complete* E_c distribution with H=N−12 on the same closed ring, as the accepted preparation-loading source and [PREP-NATIVE-1](https://chatgpt.com/space/page_4c790600a63081919cd634f4d6aeca30) already explain. Eight additional bits of full-ring entropy reduction relative to U_c must be supplied or transferred to an accounted reservoir/auxiliary output; the exact resource may be clean initialization or appropriate preexisting correlations under the conditional capacity results of [PREP-NATIVE-2](https://chatgpt.com/space/page_c4b1b4bda5cc8191942f95b5d9a4b2fb).

**No no-go for an enlarged physical world:** an independently prepared, nonuniform or correlated reservoir interacting with the ring can change its marginal law without changing global reversibility. But that actual source and coupled update must be derived and the outgoing reservoir retained; describing it is not sourcing it.

# 5. Stronger *observable* one-tick negative control for the original target

The **original fully prepared precursor law** η_c=U_c(·|E_c) includes X_(−1)=X_2=X_3=0. Under the same actual native one-tick F, its two-site observer sees A_0=0 and A_1=c **with probability one**.

Under the unprepared canonical-root U_c, the same two-site output equals (0,c) precisely when

    X_2=X_3=0 and X_(−1)=0,

which has probability (1/2)^3=1/8. Hence, for the explicitly declared accessible mathematical pair (A_0,A_1),

    TV(Law_U(A_0,A_1), Law_η(A_0,A_1))
      = 1 − 1/8 = 7/8 = 87.5%.

The full mathematically declared observer's t=−1→0 history contains this pair and has TV distance **at least** 7/8 by data processing. This is **stronger** than the one-coordinate controller-read distance 3/4 in PREP-NATIVE-1, but is still restricted to this particular unprepared source versus this particular prepared-loader target and declared observer cut. It is **not** a Bell/quantum benchmark, not an all-protocol OI no-go, and not a claim that a physical readout has been constructed.

**False-herald diagnostic:** among canonical-root states where *both visible outputs* pass (A_0=0,A_1=c), only the five additional Y relations remain to enforce the complete precursor. Because each is an independent fair test conditional on X,

    P_U(E_c | A_0=0,A_1=c) = 2^(−5) = 1/32.

Thus even the two-site visible pass is not a full precursor herald. The fraction is an **ensemble conditional probability**, not a physical device's actual positive predictive value or production success rate. Any real herald must include its availability, logs, possible backaction, failure/no-read branches and resource renewal.

# 6. Candidate physical origin screen and source ledger

The existing state-dependent ring is a **positive native interaction candidate for conditional information transfer**, but its beginning is a prepared root, not an autonomous factory. The audited paths separate:

| Layer | What is independently supported | What remains missing |
| --- | --- | --- |
| Formal finite observer realization | Main and rooted-observer audit provide a fixed observer cut, a canonical common-prior baseline per root, and deterministic reversible evolution as realization data | A native process selecting/producing that root and distinguishing physical preparations in a fully embedded world |
| Source b_c (four fixed coordinates) | Mathematically permitted, same uniform hidden prior for both settings c | A common physically produced input state with selectable c, controller loading, clock and record cuts |
| One native F tick | Exact positive correlated output (CORR-1/2), 1+h₂(1/4) bits of hidden readout and inter-slice information | Available physical sensor, retained records, repeatable apparatus, no imported addressable gate decomposition |
| Target E_c | Eight-constraint prior, conditional one-tick loader and full outgoing state already proven | Independently sourced eight-bit-equivalent low-entropy/correlated resource and its executing coupling, accessible herald, failures, renewal |
| Composite/quantum target | Local classical-register contexts remain legitimate and unchanged; no new Bell operation inserted | Physically generated pair, nonlocal response (if Bell is targeted), Born law, joint-state closure, no-signalling and soundness across switchable contexts |

**Source verdict:** a **native information-transfer lemma is positive** for the declared root; the **autonomous physical origin of the order/correlations is UNSOURCED**. The previously checked Fredkin/Toffoli switch belongs to a different dynamics and cannot be imported. This does not refute possible future independently justified full-world preparation mechanisms.

**Precise next candidate criterion:** Before proposing another apparatus, identify (from an independently motivated part of existing OI physics) an *earlier* complete source state and fixed reversible update, whose **physically executable interactions** generate b_c and the required later E_c source/auxiliary resource without defining that input state by conditioning on the desired outcome. Carry source records, outgoing state, failed preparation histories and costs. If all candidate starts simply assume b_c or E_c, the derivation has only moved the initial-condition source gap backwards.

# 7. #1169 / #1216 / #1220 quantitative implications

**#1169:** The one-tick dynamics supplies an actual example of native observer-relative information flow, supporting the idea that incomplete observers can recover hidden information later. It does not single out quantum-realizable preparations or exclude [#1143's classical C0/C1 controls](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218), because this experiment is a classical reversible ring. A sourced physical selection principle remains open.

**#1216:** For the declared two-site one-tick prepared-versus-unprepared interface, there is an observable law gap of at least 7/8; this refines the previous 3/4 diagnostic. It does not automatically lower-bound approximation error to quantum mechanics, because the benchmark here is the *specific native prepared-loader history*, not a quantum target and not arbitrary remapped measurements. A new uniform OI-derived cross-resource interface is still required.

**#1220:** Given all source coordinates, an explicit global native F tick needs O(L) bounded Boolean work and O(L) bits of classical state; the target record here is constant size, and the positive mutual information is an output *statistic*, not an algorithmic or energy cost. Producing b_c, generating 8 further bits of conditional capacity, building controller/read hardware, maintaining records and renewing the source all remain uncosted/unsourced. This proves neither efficient native quantum sampling nor any classical hardness.

**#868 / quantum composition:** CORR-1/2 show **classical reversible correlation transfer**; they do not create quantum pair states, nonlocal Bell histories, a Born measure, interference or general composition. Long-range prepared graph and native coherent operation source are still independently required.

**Stopped physical source gate:** Keep #866 CP-PREP-1 **NOT PASSED**, #945 finite-bit approximation repair separate, and all execution/merge gates unchanged.

# 8. Review packet and stopping decision

**Separate independent review: NOT PERFORMED.** Writer-side source and mathematical derivations do not count as an ACCEPT verdict. Review should verify:

1. Pinned F and root, correct modulo-L index independence for L≥9, especially A_0=X_(−1) XOR X_2 and A_1=c XOR(X_2 OR X_3).

2. U fair/independent of G and all conditional distributions; entropy 1+h₂(1/4), careful **conditioning on the setting c** and exact observer cut.

3. Full A/B conditional entropies, initial I(X;Y)=0, final I(A;B)=1+h₂(1/4), and the four-bit KL/relative-entropy decomposition; distinguish distributional from physical information acquisition.

4. Uniform-global Ω is stationary and independent across full coordinate partitions; no claim of thermodynamic equilibration, free energy, or physical root factory follows from mathematical counting.

5. Prepared η vs unprepared U two-site TV exactly 7/8, accessible-history TV at least 7/8, and the joint two-site pass conditional E probability 1/32.

6. Avoid transporting the 7/8 bound to an unspecified OI–QM comparator or claiming a new native quantum capability; preserve classical fragments, Bell/no-signalling/Born and resource obligations.

7. No target-fitted law, unsourced sensor, programmable SWAP/XOR, low-entropy reservoir, clock, herald, reset or attached physical apparatus has been introduced by the equations.

Request **ACCEPT / ACCEPT WITH NITS / REVISE** with exact source/section blockers. If only a conditional positive transport result is accepted, retain the **UNSOURCED** physical factory verdict. Research output is restricted to this off-repository paper Page; no scientific execution, Lean/probe, GitHub branch/PR, F/E, dispatch, premise adoption, manuscript update or merge has been performed.