**PREP-NATIVE-2 — Native coupling, conditional entropy capacity and correlated-apparatus control. Paper-only writer draft · 10 November 2026.**

**Scientific scope:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) remain equally prioritized; physical source is tracked under [#866](https://github.com/amaybaum/incompleteness/issues/866), classical-preserving selection under [#1143](https://github.com/amaybaum/incompleteness/issues/1143), joint composition under [#868](https://github.com/amaybaum/incompleteness/issues/868), and resources under [#1220](https://github.com/amaybaum/incompleteness/issues/1220). This follows [PREP-NATIVE-1](https://chatgpt.com/space/page_4c790600a63081919cd634f4d6aeca30) and [PREP-8](https://chatgpt.com/space/page_daabe5b3c6ec819187f0ef7730aad59f).

**Main bounded results for review:**

1. The selected SM ring **already contains a native reversible conditional-XOR coupling**, which becomes an exact function-writing operation only with adequately prepared target/source bits; independent uniform input masks the correlation.

2. For any **reversible combined ring–reservoir** that deterministically prepares the original eight-constraint full target from canonical-ring input, including previously correlated reservoirs, the input apparatus must satisfy a sharp **conditional-entropy capacity** bound: \`k-H(R|W)≥8\` bits if the final reservoir has at most \`2^k\` states and retains every other outgoing distinction.

3. An **independent, fully uniform reservoir** cannot improve fixed-time preparation probability beyond \`1/256\`, regardless of arbitrary reversible coupling. A reservoir with a **uniform marginal but eight bits of preexisting correlation** with the ring can be sufficient in an *abstract controlled-XOR comparator*. The latter is *not* an OI-derived correlation source.

4. A declared approximate full-state success requirement gives a finite-error lower bound on \`k-H(R|W)\`, but no automatic bound on accessible histories or quantum computational complexity.

**Provenance:** conditional hand mathematics composed by the ChatGPT writer; **not independently reviewed**, not Lean kernel certified, and not a physical mechanism derivation. The accepted CP-PREP-1 source status remains **NOT PASSED**; no new physical assumption or scientific execution is adopted. No repository, PR, branch, merge or experiment gate is modified.

# 1. Exact pinned source and unchanged state

Pinned reviewed source: [preparation-loading.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md), [physical-controller LEAD.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/physical-controller-20261107/LEAD.md), and the merged [CP-PREP-1 physical switch selection](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md). Main source snapshot is commit \`cac5d26441dd33e9348151487e4df7b547195481\`.

Let the two-slice binary SM ring have length L≥9 and W=(X,Y)∈{0,1}^(2L), with the fixed native bijection

\`F(X,Y)=(A,B)=(f(X)⊕Y,X)\`, where \`f_i(X)=X_(i−1)⊕(X_(i+1)∨X_(i+2))\`.

At the incoming root b_c, \`X_0=X_1=Y_0=0,\u00a0Y_1=c\`. Write A_c for that subset of complete states and U_c for its uniform law. Then \`|A_c|=2^(2L−4)\`.

The desired *complete original precursor* E_c is A_c plus eight restrictions: X_(−1)=X_2=X_3=0 and the five Y values Y_j=h_j(X) for j in J={−2,−1,3,4,5}, with

\`h_(−2)=X_(−3), h_(−1)=X_(−2), h_3=X_4∨X_5, h_4=X_5∨X_6, h_5=X_4⊕(X_6∨X_7)\`.

Under the three pinned X restrictions and visible root, \`h_j(X)=f_j(X)\` on each j∈J. \`|E_c|=2^(2L−12)=|A_c|/256\`. Let \`η_c=U_c(·|E_c)\`. The source establishes that \`F_#η_c\` is precisely the reviewed target output I_c for each c, with one common uncontrolled hidden prior.

The physical production of A_c, η_c, selectable request c, detector/access and renewal remains separately unsourced; the present analysis does not remove that source boundary.

# 2. POSITIVE native result: the actual F already computes a controlled reversible write

For *every* ring state W and every site j,

\`A_j=Y_j⊕f_j(X)\`, \`B=X\`.

Thus the **actual native step F**, not an imported gate, applies simultaneous controlled XORs between the old Y slice and Boolean functions of X, and stores every old X bit in the new previous slice B. The joint update is bijective, with explicit inverse \`F^(−1)(A,B)=(B,A⊕f(B))\`.

For each j∈J, if the *incoming* Y_j is zero, the outgoing identity becomes \`A_j=f_j(B)\`. Therefore five independently initialized zero Y cells can yield five exact outgoing function correlations through **one genuine native F tick**, although the output correlation is typed between A and B, not the original required predecessor relation Y_j=f_j(X). An output retyping or a physical rewrite of previous-slice fields has not been supplied; the full E_c target is not thereby prepared.

**Canonical-source noise lemma.** Under U_c, each of the five incoming Y_j for j∈J is an independent fair bit, independent of X and all other Y_j. Conditioned on B=X, the five outputs A_j=Y_j⊕f_j(X) are therefore independent fair bits, and

\`P_U[A_j=f_j(B)\u00a0for every j∈J\mid B]=2^(−5)\`.

The output vector A_J is conditionally uniform given B, despite the genuine native nonlinear coupling. In particular **native execution of a controlled Boolean function is distinct from preparation of the input source that makes its output informative**.

The exact reviewed precursor E_c requires Y_J=f_J(X), equivalently outgoing A_J=0 after the native tick, together with three additional X zeros. Their combined probability under U_c is 2^(−5)×2^(−3)=1/256. This is a restatement of the pinned source in terms of *where native computation is already present*, not a newly sourced factory.

**Warning:** the decomposition of a full time-step F as a conceptual conditional-XOR followed by a slice exchange does not give an observer independently selectable conditional-XOR or SWAP gate. Its components cannot be counted as native available operations absent a physical control/read interface.

# 3. The physical resource condition is conditional entropy, not simply clean bits

Consider an augmented finite **complete** system (W,R), where W retains the original N=2L ring coordinates and R is a k-bit apparatus/reservoir with alphabet size at most 2^k. Assume the initial W law is exactly U_c; allow *arbitrary preexisting correlation* of R with W. Let the full update P be a permutation of the combined finite carrier, including all unobserved apparatus output and environmental distinctions in R. Assume its output ring W' lies in E_c with probability 1 under that actual initial joint law.

**Proposition CAP-8 (new statement tailored to this interface; independent review pending):**

\`k-H(R|W)\geq8\quad\text{bits},\`

where Shannon entropies are in base 2 under the initial joint law. In particular k≥8.

**Proof.** The initial ring is uniform on A_c, so \`H(W)=N−4\`. Reversibility of the complete permutation gives

\`H(W',R')=H(W,R)=(N−4)+H(R|W)\`.

Because the output ring is supported on E_c, \`H(W')≤log₂|E_c|=N−12\`, while \`H(R')≤k\`. Subadditivity yields

\`(N−4)+H(R|W)≤H(W')+H(R')≤(N−12)+k\`.

Rearrange. □

This is a **resource-theoretic** conditional theorem: it applies to every specified reversible combined update under these exact source, target and complete-output assumptions; it does not prove any such update is available under native F.

The identity \`H(R|W)=H(R)−I(W;R)\` gives a useful resource split:

\`k-H(R|W)=[k-H(R)]+I(W;R)\`.

Thus the necessary eight-bit capacity may come from **initial reservoir negentropy**, from **preexisting ring–reservoir mutual information**, or a mixture. Counting only clean/zero bits as resources would incorrectly exclude a correlated but marginally uniform apparatus.

**Caution:** the mutual information here is between *full ontic variables*, not necessarily an observed quantity accessible to the embedded controller. Its physical production and usable read/write interaction remain independent obligations. Correlation does not by itself make an arbitrary reversible gate executable.

# 4. Two decisive controls: uniform-independent failure and correlated-uniform success

## 4.1 Fully uniform independent reservoir cannot help

Take the initial independent joint law \`U_c⊗U_R\`, with U_R uniform on **all** 2^k reservoir states. The input is uniform on A_c×R, a set of size \`|A_c|2^k\`. Under **any** complete-state permutation P—regardless of how strongly it couples W and R—its output is uniform on an image of the same size.

At most \`|E_c|2^k\` distinct complete output states have ring part in E_c. Therefore

\`P[W'∈E_c]≤(|E_c|2^k)/(|A_c|2^k)=1/256.\`

This is the **enlarged-apparatus** fixed-time analogue of PREP-NATIVE-1. It is stronger than the CAP-8 exact-success entropy condition for this uniform case: it bounds actual success at every fixed time even if there is arbitrary reversible interaction with the reservoir. A fully mixed *independent* ancillary supply cannot serve as a ready-state factory by merely increasing k.

This proof does **not** apply to a reservoir with uniform marginal law but nontrivial preexisting correlations with W: independence is essential. A conditional-root restriction on the entire world, a nonuniform reservoir, fresh low-entropy fuel, heralded postselection, or a changing source may escape these premises and must be accounted rather than quietly prohibited.

## 4.2 A marginally uniform but perfectly correlated reservoir can help (ABSTRACT only)

Define \`D_X={−1,2,3}\`, \`D_Y={−2,−1,3,4,5}\`. Let \`s(W)\` be the eight-bit vector formed from the **original values** \`(X_i)_{i∈D_X}\` and \`(Y_j)_{j∈D_Y}\`.

Construct an initial joint law by sampling W~U_c and setting the eight-bit reservoir \`R:=s(W)\`. Since those eight ring bits are independent fair bits under U_c, the **marginal R is uniform on all 256 bit strings**, but it is perfectly correlated with W: \`H(R)=I(W;R)=8\` and \`H(R|W)=0\`. It saturates CAP-8 with k=8, despite having no locally biased/zero reservoir cells.

Define a single abstract reversible comparison transformation P on (W,R):

1. For each i∈D_X, perform \`X_i ← X_i⊕R_{X,i}\`. Since on this **particular prepared joint source** the stored R bit equals the original X_i, the corresponding ring coordinate becomes zero.

2. For each j∈D_Y, perform \`Y_j ← Y_j⊕R_{Y,j}\`, setting the corresponding ring Y coordinate to zero.

3. For each j∈D_Y, perform \`Y_j ← Y_j⊕h_j(X)\`, where h_j is computed from the now-corrected X. These five outputs become precisely the required correlated Y values.

The map is a composition of controlled XOR operations on the full augmented carrier, leaving R untouched; it is a bijection on **all** (W,R) configurations, not merely on the specially prepared source.

Under the prepared correlated initial law, its ring output has **exactly η_c** while the auxiliary output R retains the eight original bits. Since the eight selected source bits were independent of the remaining ones, the final joint output factors as \`η_c⊗U_R\`, matching the same final output distribution as the clean-ancilla PREP-8 abstract comparator.

**Scientific meaning:** an apparatus with *uniform local statistics* can nevertheless be a preparation resource if its state is already correlated with the ring. This is a counterexample to a blanket statement that “uniform apparatus marginals can never help.” It is NOT a native physical factory: the initial copying correlation \`R=s(W)\` is **supplied**, and the controlled XOR operations have not been implemented by unchanged SM dynamics. Their physical source is precisely what must now be investigated.

## 4.3 Clean-ancilla comparator from PREP-8

The existing [PREP-8 writer draft](https://chatgpt.com/space/page_daabe5b3c6ec819187f0ef7730aad59f) takes the alternative resource \`R=0^8\` (a pure initially clean reservoir), uses abstract SWAP to retain the displaced eight old ring bits, and then writes the h_j correlations. It also reaches η_c with an eight-bit outgoing garbage vector. This comparator has \`H(R)=0\`, \`I(W;R)=0\`; thus \`k-H(R|W)=8\` by reservoir negentropy rather than mutual information.

Both are **sufficient abstract information-resource examples** under imported operations. Neither is a physical OI derivation; switching between them does not provide the source of the initial order/correlation or the required controller.

# 5. Quantitative finite-error condition (full ontology, not operational quantum equivalence)

Let δ=P[W'∉E_c] under a finite complete permutation P with initial W~U_c and possibly correlated k-bit reservoir R. Keep **all** failed output states in the complete output alphabet, with no postselection.

**Proposition CAP-ε (conditional entropy converse):**

\`k-H(R|W) \geq 8-h_2(δ)-δ\log_2(4095)\`.

**Proof:** Let V be the indicator of failure W'∉E_c. Because V is a function of W',

\`H(W')=H(V)+(1-δ)H(W'|V=0)+δ H(W'|V=1)\`

\`≤h_2(δ)+(1-δ)\log_2|E_c|+δ\log_2(2^N-|E_c|)\`.

As \`|E_c|=2^{N−12}\` and \`2^N-|E_c|=4095|E_c|\`, this becomes \`H(W')≤(N−12)+h_2(δ)+δ\log_2 4095\`. Reversibility and subadditivity as in CAP-8 give the claimed inequality. □

If the desired full-ring target law is η_c, then \`TV(Law(W'),η_c)≥δ\` by testing the event E_c. Conversely a demanded full-ring error \`TV≤ε≤1/2\` implies δ≤ε and

\`k-H(R|W)\geq 8-h_2(ε)-ε\log_2(4095)\`

since the entropy-correction term is increasing on 0≤δ≤1/2. Where the right side is negative, the trivial \`k-H(R|W)≥0\` is stronger.

This is a **necessary source-resource bound** under the declared finite full-ring comparison. It is not a Born-probability, quantum-computing, or observable-history accuracy theorem: the embedded observer's projection may hide large full-state differences. For an independent fully uniform reservoir, the **stronger counting result** in §4.1 gives \`δ≥255/256\` at a fixed time, regardless of k.

Rare-herald conditioning, variable-time stopping or reusable preparation factories require their own complete source/history accounting; they are not handled by erasing failure states from this target.

# 6. What this means for physical selection

The source search establishes a useful **positive** native fact—F actually executes conditional Boolean mixing of the old two slices—but neither it nor the external Fredkin/Toffoli reference supplies a **physically executable** full PREP-8 preparation process. The first missing physical source has two alternative, precisely typed forms:

- **Negentropy route:** an actual OI producer of sufficiently clean/unconstrained auxiliary state plus available reversible information transfer under one specified world update.

- **Correlation route:** an actual OI process producing preexisting ring–apparatus correlations, with a verified conditional entropy deficit and available interactions that convert those correlations into the requisite ready state.

The abstract correlation-copy control shows the two can be equivalent as *resource accounting*, not that either is native or efficient. In a globally closed reversible history, any earlier creation of such order/correlation must also be traced to its initial source or changed boundary: simply moving the resource to an earlier tick does not eliminate the sourcing obligation.

**One decisive native proof obligation:** specify a genuinely existing physical process \`G\` (under the unchanged SM rule or an independently motivated, separately authorized extension), with full state, preparation producer, controller, setting and read access, which outputs *either* a clean eight-bit-equivalent sink *or* at least eight bits of conditional information capacity, then implements actual permitted coupling to meet **all eight** E_c constraints with retained records/failures and a compatible next use. Avoid defining the source by \`R=s(W)\` or by \`η_c\` as a target-fitted input law. If no such G can be sourced, record **UNSOURCED** and stop instead of inventing another abstract gate.

**Classical regimes retained:** any source candidate must preserve ordinary classical register read/copy contexts. Conditional preparation of a classical ring input cannot by itself exclude [#1143's C0/C1 countermodels](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218), yield Bell nonlocality, derive native Born probabilities, prove joint-state closure or select the quantum bound. Those targets remain independently open.

**Precision/source accounting:** [#1216](https://github.com/amaybaum/incompleteness/issues/1216) uses CAP-ε only for the *specific declared full-state target*; [#1220](https://github.com/amaybaum/incompleteness/issues/1220) must charge initial reservoir entropy or correlation, producer cost, native gate/control, records, failure/reset/renewal and arbitrary size. No operational strong/weak classical-simulation complexity follows from these entropy inequalities. Keep [#945](https://github.com/amaybaum/incompleteness/issues/945)'s fixed-b proof repair separate.

# 7. Review and provenance controls

**Review state: NOT INDEPENDENTLY REVIEWED.** The writer checked algebra and source scope using pinned files; this is **not** acceptance by a separate expert, Lean run, physical execution or integration result. Existing accepted source and review artifacts are retained without change.

A separate reviewer should check:

1. Correct pinned SM Boolean form and source E_c, root b_c, eight additional constraints and |\`A_c\`|/|\`E_c\`|=256 for all L≥9 with modulo-index aliasing.

2. Positive F coupling and *conditioned* joint law: under U_c, five target Y_j are independently fair, so \`A_J|B\` is uniform. Check that an outgoing \`A_j=f_j(B)\` condition is **not** mislabeled the original precursor Y_j=f_j(X).

3. CAP-8 proof under arbitrary W–R correlations, and the exact decomposition \`k-H(R|W)=k-H(R)+I(W;R)\`; check that all other outgoing world states are included in R.

4. Independent-uniform-reservoir success ≤1/256 under **arbitrary coupled permutation**, and the counterexample with *uniform marginal but perfectly correlated* R=s(W); do not drop independence.

5. Correlation-assisted XOR map reversibility on its *full* state space, its unchanged root c, full exact output η_c and whether the final reservoir is statistically independent of the ring under the specified law.

6. CAP-ε error/entropy counting, correct factor 4095, error region ε≤1/2, and the distinction from TV of actual observer histories.

7. Resource ledger: neither nonzero mutual information nor clean bits is an already sourced available OI controller; constant abstract Boolean gates do not give native clock, selection, herald, resets, energy/space or BQP complexity.

8. Comparison with [#866 CP-PREP-1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md): preserve the **physical NOT PASSED** source gate and the conditional operation-source restriction.

Suggested review verdict on this *mathematical/source packet*: ACCEPT / ACCEPT-WITH-NITS / REVISE with exact faults and provenance. **Even an ACCEPT of the mathematics must not be promoted to a physical PREP source pass.**

No GitHub/PR/Issue edit, manuscript promotion, physical premise adoption, numerical or native scientific execution, F/E, dispatch or merge has been carried out.