**PREP-OBS-1 — Observer-relative native heralding: exact seven-output selection and its physical source gap**

**Paper-only writer draft · 10 November 2026 · INDEPENDENT REVIEW PENDING**

**Main question.** Can finite observational incompleteness, combined with the actual native reversible SM ring, select a physically useful preparation without inserting an extra target-designed reversible factory?

**Bounded answer.** The unchanged F already turns the eight hidden predecessor restrictions into **seven simultaneous post-tick output tests** under the existing canonical-root law. Conditioning on those exact tests produces the entire desired prepared-ring output law with probability 1/256. The previously declared two-site observer is insufficient and yields at best 1/32 *posterior* confidence in full readiness when it sees matching early outputs. A proposed enlarged **read-only mathematical observation** would certify readiness, but no native nondemolition multi-site detector, output log, physical root producer or reset mechanism is sourced. Therefore this is an **exact conditional mathematical selection** and an **UNSOURCED physical heralded preparation**, not a quantum operation or full OI–QM bridge.

**Accountability:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) equally prioritized; [#866](https://github.com/amaybaum/incompleteness/issues/866) native prep, [#1143](https://github.com/amaybaum/incompleteness/issues/1143) classical-preserving selection, [#868](https://github.com/amaybaum/incompleteness/issues/868) physical pair and composition, [#1220](https://github.com/amaybaum/incompleteness/issues/1220) resource accounting. Source-reviewed prior results and the writer-only [PREP-CORR-1](https://chatgpt.com/space/page_e8d639b1de408191a09a4d7c10f1d9e2) remain intact; this is an additive hypothesis/argument, not retroactive independent acceptance.

No numerical/scientific experiment, Lean build, physical-premise adoption, GitHub PR/push, special CI/F/E, dispatch, manuscript promotion or merge is performed.

# 1. Exact source and fixed interpretation

Pinned source [preparation-loading.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md), blob 1802ea3c335eb7457739fa5af13b3aefd0c603af, and [physical-interface.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md), blob 3229ef3c. [Rooted-family audit](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/audits/operational/rooted-observer-family-sourcing/result.md), blob 34ea388d, sources a **mathematical observer-rooted family** and canonical common-prior baseline but not a physical producer of each root. [CP-PREP-1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md), blob 736ea7e3, stopped on physical source. No cited source claims an actual herald for the event below.

Fix ring L≥9, W=(X,Y) on two binary slices and actual native reversible rule:

\`F(X,Y)=(A,B)\`, \`A_i=Y_i⊕f_i(X)\`, \`B=X\`, \`f_i(X)=X_(i−1)⊕(X_(i+1)∨X_(i+2))\`.

For a known request c, the canonical root event is

\`b_c: X_0=X_1=Y_0=0,\quad Y_1=c\`.

The canonical law \`U_c\` is uniform on b_c, with every other coordinate independent fair. The **strict** predecessor readiness event \`E_c\` consists of the root and eight further restrictions:

\`X_(−1)=X_2=X_3=0;\`

\`Y_(−2)=X_(−3),\quad Y_(−1)=X_(−2),\`

\`Y_3=X_4∨X_5,\quad Y_4=X_5∨X_6,\quad Y_5=X_4⊕(X_6∨X_7)\`.

The reviewed source proves \`U_c(E_c)=2^(−8)\`, \`η_c=U_c(·|E_c)\`, and that the full desired prepared **ring** output has law \`I_c=F_#η_c\`. Neither b_c nor E_c has an identified autonomous physical producer.

Notation: \`J={−2,−1,3,4,5}\` is the set of five *distinct* post-tick test sites (mod L). The already declared embedded observer reads the two-slice registers at sites 0 and 1 only. A proposed observer with the five extra sites is a **changed observer-access class** whose physical executability is open.

# 2. Proposition OBS-1: exact native output equivalence

**Claim (new paper restatement/derivation, independent review pending).** On the source root b_c,

\[
E_c\quad\Longleftrightarrow\quad
\left(A_0=0,\ A_1=c,\ A_j=0\ \text{for every }j\in J\right)
\tag{OBS-1}
\]

where A is the **actual one-tick** native field F(W). No additional update, quantum map, inverse evolution or external reversible gate is used in this logical equivalence.

**Proof.** At the root, \`f_0(X)=X_(−1)⊕X_2\` and \`f_1(X)=X_2∨X_3\`, so \`A_0=X_(−1)⊕X_2\`, \`A_1=c⊕(X_2∨X_3)\`. The pair \`A_0=0,A_1=c\` forces X_2=X_3=0, then X_(−1)=0, and conversely those three zeros force the pair.

Given those zeros and the root, the five site formulas reduce to

\[
f_{−2}(X)=X_{−3},\quad
f_{−1}(X)=X_{−2},\quad
f_3(X)=X_4\lor X_5,\quad
f_4(X)=X_5\lor X_6,\quad
f_5(X)=X_4\oplus(X_6\lor X_7).
\]

Thus on the already-certified three-zero sector, each \`A_j=Y_j⊕f_j(X)\` vanishes exactly when the corresponding one of the five Y restrictions holds. Together they are precisely E_c. □

**Scope:** the equivalence concerns a single full field snapshot after F plus the declared known initial root. It is a mathematical readout identity. It does not establish that those five extra sites are all accessible to a real embedded observer or that copying their values is nondemolition and compatible with the next native operation.

# 3. Exact conditional preparation by mathematical postselection

Let \`M_7\` be the seven-output check in OBS-1 and let \`H\` be the event it passes. Because H=E_c as events on the original W,

\[
P_{U_c}(H)=1/256,\qquad
\operatorname{Law}_{U_c}(F(W)\mid H)=F_\#\eta_c=I_c.
\tag{OBS-2}
\]

This is an exact **full-ring law**, not merely an endpoint match; it also inherits the same supplied root law for both c values because the eight hidden restrictions are independent of c under U_c.

**Important semantic qualification.** The observation-and-selection description makes a conditional distribution. It is not an operation that maps *every* incoming ring state to I_c. The unselected 255/256 of the input ensemble still evolves under F and cannot be silently discarded from a complete operational history. The physical request/source producer, actual detector/probe coupling, output record, accepted/failed states and renewal remain unbuilt.

If an ideal physical apparatus could perform the OBS-1 test after one native tick without altering the desired ring state or destroying needed correlations, preserve the flag and include its environment, it would be a **heralded**, not deterministic, precursor-to-I_c preparation **conditional on an independently produced b_c source**. This is a proposed *detector interface*, not an already available native one. A real test that reads the entire hidden condition by an oracle would not count as physical sourcing.

**Uniform-global origin.** If the whole ring instead begins in the completely uniform global Ω over all 2^(2L) states, the specified root b_c has Ω mass 1/16 and E_c has Ω mass 1/4096. These are ensemble masses, not demonstrated iid attempt probabilities. A prior root-conditioning step itself requires physical selection/production.

# 4. Proposition OBS-2: existing two-site observer cannot certify E

Let \`M_2\` be the complete mathematical initial-root plus first-output observation of the **existing two-site observer** at sites 0 and 1 (both slices). Under the fixed root b_c its only varying first post-tick values are \`A_0,A_1\`; B_0=B_1=0. Define the matching record \`m_*=(A_0=0,A_1=c)\`.

From the source, \`P_{U_c}(m_*)=1/8\`, while E_c⊂m_* and \`P_{U_c}(E_c)=1/256\`. Consequently

\[
P_{U_c}(E_c\mid m_*)=\frac{1/256}{1/8}=\frac1{32}.
\tag{OBS-3}
\]

The other output records have \`P(E_c\mid M_2=m)=0\`.

**No-perfect-herald lemma (restricted readout).** Any nontrivial acceptance rule that sees only M_2 and *independent* private randomness—not inaccessible W coordinates—has

\[
P(E_c\mid\mathrm{accept})\leq 1/32.
\tag{OBS-4}
\]

**Proof.** On each M_2 record the random acceptance decision carries no further information about E_c. Thus the posterior probability of E_c on the accepted sample is a convex combination of the fixed per-record posteriors, whose maximum is 1/32. Equality is attained by accepting only m_*. □

The **conditional full-ring** law of F(W) on accepted one-tick histories is therefore at least 31/32 in TV from I_c, because I_c puts probability 1 on F(E_c) and the selected law puts at most 1/32 there. This does **not** establish a corresponding bound on the *currently observed two-site* output law: on the matching record that output agrees exactly with the desired one. The discrepancy is in the remaining hidden state and potentially later accessible histories.

**Meaning:** current visible success does not certify full physical readiness. This is not a statement that every possible longer observer history or additional apparatus is unable to distinguish E_c. It also does not ban a physical detector from gaining additional information—its interaction and readout class must simply be sourced explicitly.

# 5. Five independently unresolved syndrome bits at the early cut

Under U_c and conditioned on the matching M_2 record m_*, the three X zero constraints are fixed. The five residual bits

\[
S_j=A_j=Y_j\oplus h_j(X),\qquad j\in J
\]

are conditionally independent, unbiased bits (they use five distinct independent free Y_j coordinates). E_c is exactly the event that all five vanish. Thus

\[
H(S_J\mid M_2=m_*)=5\ \mathrm{bits},\qquad
P(S_J=0^5\mid M_2=m_*)=2^{-5}.
\]

For the **restricted model of one-tick coordinate readouts** that has no access to the initial Y_J values and can inspect only a chosen subset of the output coordinates plus the already declared M_2, every omitted A_j leaves a free fair residual bit. Hence no strict subset of these five designated output-coordinate tests can **perfectly certify E_c** on positive-probability accepted branches.

This is a **restricted coordinate-read necessity**, NOT a universal five-bit detector-memory requirement. A single physically executable Boolean flag \`1[S_J=0^5]\` would be enough if the apparatus could genuinely compute and record it without importing a nonnative operation or hiding its cost. The unobserved residual entropy describes mathematical conditional uncertainty, not a thermodynamic five-bit erasure cost.

The five extra test sites are spatially separated around the ring (indices modulo L). Treating them as a combined instantaneous herald is a changed observer-access interface that may require signal routing, timing, readout, measurement disturbance and memory. None has been sourced from the existing two-site observer.

# 6. Approximate detector precision and failure cost

Suppose, **purely as a conditional engineering model**, a detector returns estimated seven-bit output values \`\\widehat{M}_7\` and the probability that *any* component differs from the actual OBS-1 value is at most δ. Let H be the true event (probability p=1/256) and \`\\widehat H\` the observed pass event. Then

\[
P(H\cap \widehat H)\ge p-\delta,\qquad
P(\widehat H)\le p+\delta.
\]

For 0≤δ<p, the posterior accuracy satisfies

\[
P(H\mid\widehat H)\ge \frac{p-\delta}{p+\delta}.
\tag{OBS-5}
\]

**Proof:** the symmetric difference of H and \`\\widehat H\` has probability at most δ. Therefore true positives are at least p−δ and all declared positives are at most p+δ. □

A **sufficient**, not necessary, requirement to guarantee postselected ready fraction ≥1−ε from this bound is

\[
\delta\le \frac{\epsilon p}{2-\epsilon}
=\frac{\epsilon}{256(2-\epsilon)}.
\tag{OBS-6}
\]

If component-j bit-error probabilities are e_j under the actual source, a union bound δ≤Σ_j e_j suffices—no independent detector-error assumption is needed. These are abstract detector-quality bounds, not measurement noise data or a physically sourced decoder.

**Outcome and cost bookkeeping:** the protocol's raw herald success remains about p only if detector errors are appropriately small; nonaccepted outcomes and all source/clock/detector failures remain in the actual complete history. A mathematically perfect conditional law at yield p cannot be identified with an *always-successful* target interface: its success-flag marginal has TV gap at least 1−p=255/256 from an ideal deterministic-success flag. An honest target can instead be the same **heralded instrument**, with its failures and success rate included. An expected 256-attempt cost needs independently regenerated sources or a specified uniform per-attempt conditional success lower bound, not merely a one-attempt ensemble mass.

# 7. Physical origin decision: observation is not a produced boundary condition

The inspected maintained OI corpus supplies an **observer-relative, fixed-prior rooted law**, and the SM ring supplies F and the exact algebraic seven-output detector predicate. It does NOT supply a physical selection operation, externally readable field contacts at five additional positions, nondemolition copying, an input root factory, a herald storage cell, permitted feedback, or renewal.

The correct formulation of the candidate **observational-selection route** is therefore:

1. **Source:** a physically generated root b_c with a common uncontrolled hidden prior and selectable c (first existing source gap).

2. **Native dynamics:** one actual F tick; no imported new quantum gate.

3. **Measurement:** a physically executable post-tick detector that makes the OBS-1 seven-output comparison and retains its record, with its controller, delays, disturbance and extra access typed.

4. **Outcome law:** keep both H=1 and H=0 branches; only the accepted branch has the exact I_c ring law in the mathematical idealization.

5. **Reuse:** verify a usable outgoing prepared ring, records and fresh root/ancillas after success or failure; no automatic reset.

6. **Scientific controls:** retain existing two-site observer as a deliberately insufficient readout; preserve ordinary classical observations; keep #1143 C0/C1, #868 Bell, native Born, quantum joint-state closure and composition open.

Neither conditioning a mathematically selected ensemble nor writing an abstract predicate \`1_{E_c}\` into an observer description is an independently sourced physical process. The physical selection could conceivably occur by native interaction and actual embedded records; demonstrating that is the next **source gate**, not an assumption to add by definition.

A candidate that admits the five extra read sites needs explicit comparison against the original observer cut. Extra access may alter subsequent native observational possibilities and could violate a separate quantum-equivalence claim if hidden information becomes directly observable. Source the observer physics before calling either cut fundamental.

# 8. Disposition and independent review

**New paper claim:** OBS-1 explicitly translates all eight predecessor constraints into seven read-only one-tick field conditions under native F; OBS-2 proves a 1/32 false-herald limit for the existing early two-site observer; an expanded observer could in principle select I_c with probability 1/256, subject to a physical detector. The prior entropy/source and 7/8 early-output TV results are kept under their original statuses. This is conditional classical reversible mathematics, **not** a Bell/quantum mechanism or a physical OI sourcing pass.

**Independent review: NOT YET PERFORMED.** Invite a different reviewer to check the exact F expansion for each output site, indexing for all L≥9, the event equivalence E_c↔seven tests, common-root dependence on c, and the precise F_#η_c conditional-law equality. Challenge the proof that the existing one-tick observer's only nontrivial record is (A0,A1), the posterior 1/32, the randomized herald bound, and whether omitted Y_j remain independently fair under all allowed coordinate-read conditioning. Check OBS-5/6 detector-noise inequalities, error symbols and p=1/256; do not confuse a success probability with a physical iid retry cost or a full-history comparison.

Check against [#866 source-selection stop](https://github.com/amaybaum/incompleteness/issues/866): no physical ability to read the extra five field sites, no real herald, no new source producer, no composition and no Born rule should be asserted. Review must keep approved exact reviews and every frozen execution/merge gate unchanged.

The reviewer may return ACCEPT, ACCEPT-WITH-NITS, or REVISE **for the paper-level mathematical argument only**. Even an ACCEPT does not authorize physical construction, simulation, native experiment, new premise, special dispatch, CI/F/E, manuscript change or merge. The actual result is a new **read-access and herald-source target**, not a native factory.