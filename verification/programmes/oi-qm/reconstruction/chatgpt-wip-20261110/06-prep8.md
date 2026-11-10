**OI–QM PREP-8 — Exact reversible precursor factory in an enlarged abstract interface (paper-only writer draft, 10 November 2026)**

**Status:** newly written **conditional mathematical construction + matched information lower bound**; not a native implementation; **separate independent review pending**. The previous independently accepted physical-source verdict remains **NOT PASSED / UNSOURCED**. No scientific execution, numerical search, Lean, GitHub PR, merge, or physical premise adoption is undertaken.

**Issues and priority:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) physical sourcing and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) approximation remain equally prioritized; [#866](https://github.com/amaybaum/incompleteness/issues/866) native controller source, [#1143](https://github.com/amaybaum/incompleteness/issues/1143) classical-preserving selection, [#1220](https://github.com/amaybaum/incompleteness/issues/1220) resources. Companion: [PREP-SYN-1](https://chatgpt.com/space/page_6df5ac835f9c819186d936d50f96ac92), [Unit 2 critical audit](https://chatgpt.com/space/page_e94d275c997c8191b2480f038ac1884b).

**Exact source:** [preparation-loading.md §§3–7, pinned main cac5d264](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md); [physical-controller LEAD](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/physical-controller-20261107/LEAD.md); [CP-PREP-1 selection record](https://github.com/amaybaum/incompleteness/blob/main/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md). The eight-constraint mass, no-internal-free-reset and retained-output conclusions are existing work, not claimed new here.

**Main result:** For a canonical root-conditioned source on the binary ring, if a fixed preparation interaction may use **eight initially zero auxiliary bits** and reversible SWAP plus controlled-XOR gates on declared coordinates, it can deterministically produce the **complete original precursor** with the exact reviewed structured law, while retaining eight input bits as output garbage. Eight bits of *additional distinguishable output capacity* are necessary for any injective deterministic full-success map from this particular canonical-root support to the constrained original ring support, **assuming there are no other output channels carrying distinctions**. This is a tight abstract information-capacity statement, not a physical source of those gates, clean bits, clock or producer.

# 1 Immutable source contract and exact quantities

Take a binary ring of length L≥9, with complete two-slice state W=(X,Y) containing N=2L bits. Indices are modulo L. The *existing* unchanged native update is

`f_i(X)=X_(i−1) XOR (X_(i+1) OR X_(i+2))`, `F(X,Y)=(f(X) XOR Y,X)`.

The source paper's visible incoming root for desired request c is
`b_c: X_0=X_1=Y_0=0, Y_1=c`.
Let U_c be the **uniform** law over all W satisfying that root: its support size is `2^(N−4)`.

The **full** precursor condition E is the root plus these eight additional constraints:

`X_(−1)=X_2=X_3=0`;

`Y_(−2)=X_(−3)`, `Y_(−1)=X_(−2)`,
`Y_3=X_4 OR X_5`, `Y_4=X_5 OR X_6`,
`Y_5=X_4 XOR (X_6 OR X_7)`.

The constrained coordinates are `D_X={−1,2,3}` and `D_Y={−2,−1,3,4,5}`; for L≥9 all five Y coordinates are distinct and their prescribed values depend only on **unconstrained** X coordinates, though some of those unconstrained X labels may coincide modulo L. Call those prescribed functions `h_j(X)` for j∈D_Y.

The source has `U_c(E)=2^(−8)`, and the target `η_c=U_c(·|E)` is uniform on exactly `2^(N−12)` original ring states. The original paper proves `F_#η_c` is precisely its desired target I_c law, including all hidden remaining coordinates and the same uncontrolled hidden prior for both c. Neither U_c nor η_c is claimed to have an autonomous factory.

# 2 Proposition A — output-capacity lower bound (scoped)

**Statement.** Suppose a deterministic preparation process maps *every* input ring configuration W in the support of U_c, together with the same fixed initial auxiliary state, injectively to a final state (W',g). Suppose W' must satisfy E (thus has at most `2^(N−12)` possible values) and g is the **only** additional output carrying distinguishable residual information, with at most M possible values. Then

`2^(N−4) ≤ 2^(N−12) M`, so `M≥256` and `log₂M≥8`.

**Proof.** Injectivity requires at least as many distinct complete output states as incoming states. The complete output support is a subset of `E×G`, of size at most `2^(N−12)M`. Compare cardinalities. □

**Interpretation and restrictions.** This is a **support/capacity** lower bound under a canonical-root source, deterministic success on *every* incoming configuration, fixed initial ancillary resource and no other distinguishing output channels. Any outgoing preparer, clock, environment, inaccessible record, failure flag or retained reservoir is part of the complete output and must be counted in g if it carries distinctions. If the source was *already constrained*, the preparation may require less; if failures/postselection are allowed, the everywhere-success bound does not apply; if the system can interact with an unbounded reservoir, its actual outgoing capacity counts. The lemma proves **no** universal eight-bit thermodynamic heat cost, minimum number of gates, required free-energy budget or quantum entanglement cost.

This matches the existing source's eight-bit relative-entropy/support-deficit observation but adds a deliberately specified *tight abstract reversible implementation* below. The general need to retain information in reversible computation is not novel.

# 3 Proposition B — matching explicit reversible factory with eight clean auxiliary bits

Introduce eight auxiliary binary cells `a=(a_X,a_Y)`, with three components indexed by D_X and five by D_Y, **supplied initially as a=0⁸**. The augmented input law is `U_c⊗δ_(0⁸)`. Define a single fixed reversible transformation T on the augmented state as the following composition of bijections:

**Stage 1 — save the three pin coordinates.** For each i∈D_X, apply `SWAP(X_i,a_X,i)`. Starting from clean auxiliaries, this sets `X_(−1)=X_2=X_3=0` and stores their original three source values in the corresponding auxiliary cells.

**Stage 2 — save the five conditioned Y coordinates.** For each j∈D_Y apply `SWAP(Y_j,a_Y,j)`. With zeroed auxiliaries this makes all five Y target coordinates temporarily 0 and stores the original Y values in the auxiliary cells.

**Stage 3 — write the required functions reversibly.** For each j∈D_Y perform `Y_j ← Y_j XOR h_j(X)`. Since each h_j reads only the X coordinates **left unchanged** in Stage 1, this sets Y_j to precisely its required source contract value without modifying other ring cells or the garbage.

Every SWAP and every controlled XOR is individually bijective on the **entire augmented carrier**, even away from the clean-auxiliary input subspace, so their composition T is a permutation. Its inverse applies the five controlled XOR operations in reverse order, followed by reversed swaps. Crucially **the full transformation is fixed and independent of the desired request c**; it leaves the initially visible coordinates X_0,X_1,Y_0,Y_1 unchanged.

For every input W with root b_c and clean a, the output ring T_ring(W,0) satisfies E. Apply one subsequent **existing native F tick to the ring only**; by the already reviewed loading identity, the ring's law becomes the full I_c target and the outgoing eight-bit garbage is retained.

**Uniform-law statement.** Under U_c the eight originally selected coordinates in D_X∪D_Y are independent fair bits, independent of all the remaining coordinates. T moves exactly those eight bits into a, without using them in any target function h_j; the ring's remaining free coordinates stay uniform. Thus

`T_#(U_c⊗δ_(0⁸)) = η_c⊗U_(8)`

with `U_(8)` uniform on all 256 auxiliary bit strings, and consequently

`(F×id)_#T_#(U_c⊗δ_(0⁸))=(F_#η_c)⊗U_(8)`.

This produces **one common output hidden-prior family for c=0,1**. The auxiliary garbage is statistically independent of the final ring under this ideal specified law, not deleted or reset. The input has `N−4` bits of entropy; the ring target retains `N−12` and the garbage retains eight, preserving the total.

**Gate contract:** 8 abstract swaps plus 5 abstract controlled XOR writes, where the Boolean source functions are predeclared from the reviewed contract. These are **conditional available operations**, NOT operations shown to be executable by the particular native ring F or by an authorized OI controller.

# 4 Native physical sourcing: the construction is a comparator, not a derivation

The source search included [CP-PREP-1](https://github.com/amaybaum/incompleteness/blob/main/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md), whose independently reviewed physical-source stop remains **NOT PASSED**. Its examined Fredkin conditional switch belongs to a different physical dynamics and has no identified executing realization as the required operations on the unchanged ring. The externally specified SWAP and conditional-XOR stages above are likewise not identified as available native interactions of F.

To turn the abstract matched factory into **physical OI sourcing**, a candidate must actually provide:

1. **Eight ready cells or equivalent information sink:** physically generated/received under the same world law and with all reservoir outputs accounted, rather than writing a₀=0 by decree.

2. **Native operation and program source:** a single update on a larger specified carrier whose physically executable interactions implement the coordinate exchanges and conditional writes (or an independently sourced equivalent) while preserving the requested visible root. A mathematical permutation on a freely expanded state is not an apparatus made by F.

3. **Physically available initial common law:** the U_c root-conditioned state and setting choice c must themselves have an accountable producer; the input law here remains stipulated.

4. **Complete records and no hidden leakage by convention:** if a physical preparer learns h_j(X), controller data, the later input Z=Y_2 XOR X_4, or ancillary environment variables, retain actual accessible preparer logs. Independence of the ideal eight stored old bits from the target state does not make every possible physical implementation free from leaked information.

5. **Failure and reuse:** the conditional abstract process has no failure with *clean supplied* inputs, but actual dirty auxiliaries, clocks, attempt selection and outgoing garbage require a produced reset, bank, or compatible continuation. A used random garbage register is not automatically a fresh zero register.

6. **Native geometry and time:** source the actual update and routing under the prescribed ring, including the full dependency and gate availability; an abstract constant gate count is not physical constant-time execution.

**Source verdict remains UNSOURCED.** The main new value is a precise *capacity and gate-source target*, plus a demonstration that the canonical-source entropy deficit is **not a universal logical impossibility** for enlarged reversible apparatuses. This still does not prepare a Bell pair, source nonlocal interactions, derive the Born rule, or select quantum operational structure.

# 5 Classical observations, approximation and resource crosswalk

**Classical fragment and #1143:** the preparation gadget uses only reversible Boolean logic and preserves a conventional classical-register interpretation. It neither excludes classical observations nor excludes the reviewed C0/C1 countermodels. Its existence under expanded operations does not provide an OI-derived selection rule or general quantum-capable interface.

**#1216 approximation:** for the source/model actually specified, the abstract factory's *ring output law* equals the reviewed I_c preparation law **exactly**, not merely approximately. This is a statement within an enlarged *assumed-gate* model; it cannot be promoted to Level B native OI–QM approximation. If a future native implementation approximates the abstract factory kernels uniformly by `η_j` and has source error `η₀`, the accepted complete-history TV budget applies, including all actual apparatus logs and failure/truncation terms. A good marginal or an ideal postselection is not a complete-history result.

**#1220 two-ledger costs:** in an abstract classical Boolean circuit model with direct access to the fixed relative indices, the factory uses eight SWAPs and five controlled writes, each h_j requiring bounded Boolean work. Sampling U_c requires O(L) bit work/storage for N=2L sites, and one explicit global F tick costs O(L) Boolean work. Thus an *abstract supplied-source/supplied-clean-ancilla component* has an O(L) literal sampler for its declared full mathematical output law. This is **not** a physical implementation-cost bound for the native OI rule or scalable quantum computation, because clean ancilla manufacture, controller/clock/gate execution and observer apparatus may be arbitrarily costly or unavailable.

**Output records:** the eight garbage bits are always retained, and if physically accessible they must belong to the complete observer history. Under the ideal abstract U_c source they are independent of the ring target, so outputting or retaining them does not disturb the target marginal. A real preparer may generate additional correlated records not represented by this ideal circuit, so its complete-history law must be rechecked.

**Renewal:** to repeat on independent fresh uses, supply fresh ready ring/source and eight clean auxiliaries each time or prove an actual reset/fresh bank; no inference of zero total cost follows from reversible gate count. No numerical 8kT ln 2 Landauer heat claim is licensed without a thermodynamic bath/temperature and actual erasure process. The alternative complexity outcomes for the still-unsourced quantum interface remain all open.

# 6 Decision packet and independent review boundary

**Recommended bounded next scientific question (existing #866 and #1169 home; no new issue required):** Does the **unchanged native SM ring**, perhaps with a physically justified attached observer-controller sector under one common reversible law, generate the eight ready bits/equivalent sink and execute the necessary information transfer to prepare E **without** introducing the desired full precursor as an input assumption? If no execution/source of the first clean auxiliary or gate can be demonstrated, STOP at that clause. Any altered native update, new added control class, independent supplier or fresh ambient low-entropy reservoir must be called a proposed physical premise and separately authorized. Do not infer the conditions from the target law.

**Request for a different independent reviewer — not performed here:**

- Verify the 2L-bit root and eight distinct constrained coordinates for all L≥9; ensure all h_j(X) depend only on unmodified X, with modulo-L aliases correctly handled.

- Verify every Stage 1–3 primitive is a permutation of the **whole** augmented space; check that setting Y_j to h_j uses the clean auxiliary and does not lose information.

- Check the exact equality of distributions `T_#(U_c⊗δ_0)=η_c⊗U_8` for c=0 and 1; check independence of auxiliary garbage and all free coordinates, including Z=Y_2 XOR X_4.

- Verify the conditional eight-bit output-capacity lower bound: it needs full-success injectivity, fixed root support, and an exhaustive outgoing distinguishability ledger. Check whether nonuniform target laws, failures or other output channels change its claim.

- Challenge the division between an **abstract external SWAP/XOR preparation circuit** and available native operations of the unchanged F. A conditional construction is not physical native sourcing.

- Check full outgoing ring, separate observer/preparer logs, renewal, and the existing #945/#868/#1143/#1220 gates and assumptions.

- Require an explicit **REVISE / ACCEPT WITH NITS / ACCEPT** paper-only verdict, attribution to the old entropy result, and a clearly separate **UNSOURCED** physical verdict.

No separate reviewer was available inside this writer session; this document is **not independently ACCEPTED**. The source remains gated and no scientific code/Lean execution, branch push, PR, manuscript edit, F/E/dispatch, physical-rule adoption or merge has taken place.