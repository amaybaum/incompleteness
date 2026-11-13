# NATIVE-FACTOR-SRC-1 — Native predictive-factor candidates, locality obstruction, and physical-source stop

**New paper-only writer packet · 10 November 2026 · INDEPENDENT REVIEW PENDING · physical source NOT PASSED**

**Primary programme:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) OI–QM exact/conditional operational sector. **Equal foundational priority:** [#1216](https://github.com/amaybaum/incompleteness/issues/1216) uniform approximate complete histories. **Physical source gate:** [#866](https://github.com/amaybaum/incompleteness/issues/866). Cost and quantum-selection dependencies: #1220, #1143, #868. **No new issue or physical assumption is introduced.**

**What this packet does:** Screen three *native* predictive descriptions for the unchanged finite SM binary ring: (A) a local finite-horizon causal-cone coordinate snapshot, (B) a global autonomous passive future-trace quotient, and (C) an observer-history Bayesian filtering state. Prove what they supply mathematically, identify a simple but general obstruction to autonomous coordinate patches, and stop at the first missing physical preparation/readout/controller step. This is not a claim that any candidate is a physically executable quantum instrument.

**Status and provenance:** NATIVE-PRED-1 [independent ACCEPT WITH NITS at \`95cead38\`](https://chatgpt.com/space/page_fa9ae3c07c208191bdf87950b734488b), no mathematical errors and its two README nits later corrected; [INT-FACTOR-1/CARD-GAUGE-1 independent accepts](https://chatgpt.com/space/page_b4f63a8bd3a88191a1e9318ec0e3577f) remain separately pinned. This new file contains *new hand proofs*, not an inherited independent verdict, Lean certification, numerical simulation, computation, experiment, implementation or authorized manuscript integration. Do not rewrite historical reviewed papers 01–15.

**Summary decisions:**
1. At T=2, the local coordinate cone \(q_2\) of **13 initial bits** determines all the original two-site/two-slice records through two updates; conditional on the visible canonical root, **nine** of those bits are unconstrained under the mathematical law \(U_c\). This is an intentionally nonminimal predictive *snapshot*, NOT an autonomous factor or available observer register.
2. On the full ring, **every proper same-site two-slice coordinate projection** \(q_I=(X|_I,Y|_I)\), for nonempty \(I\subsetneq\mathbb Z/L\mathbb Z\), fails the one-step deterministic autonomous intertwining criterion; the witness can be chosen within either canonical-root class whenever \(I\) contains observed sites 0 and 1. This does **not** exclude nonlinear/aggregated or whole-carrier predictive factors.
3. The canonical passive future-trace quotient \(q_\infty\) *is* an exact autonomous mathematical factor, by the previously established [Substratum Proposition 24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md), but is not an implemented readout or controller-compatible factor.
4. The Bayesian belief state \(\rho_t\) derived from the mathematical source \(U_c\) and retained passive history is an exact classical stochastic prediction representation; it is not a deterministic microscopic factor, a sourced memory device or QM.
5. No candidate passes the physical-source gate. Missing physical resources remain a **preparation/root producer**, an accounted observer/readout/clock/record interaction and native admissible controls, as recorded in CP-PREP-1. **Stop: UNSOURCED.**

## 1. Exact native source and observation dictionary

Pinned main baseline: \`cac5d26441dd33e9348151487e4df7b547195481\`. Read with [preparation-loading](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md), [physical-interface](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md), [CP-PREP-1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md), reviewed [NATIVE-PRED-1](15-native-predictive-factor-bound.md), and [Substratum Proposition 24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md).

All site indices are modulo \(L\ge9\). For complete state \(W=(X,Y)\in S_L=(\{0,1\}^L)^2\),

\[
F(X,Y)=(f(X)\oplus Y,X),\qquad
f_i(X)=X_{i-1}\oplus(X_{i+1}\lor X_{i+2}).
\]

This is the unchanged selected **mathematical native branch** of SM §3.1; the theory has not physically selected it as the unique laboratory substratum law.

The observer's declared passive mathematical projection is \(o(W)=(X_0,Y_0,X_1,Y_1)\), with both time slices visible at sites 0 and 1. The canonical-root support \(b_c\) fixes \(X_0=X_1=Y_0=0,\ Y_1=c\), for \(c\in\{0,1\}\), and \(U_c\) is uniform on the unpinned bits. This is **source-pinned mathematical realization data**, not a device that physically prepares the prescribed law. The conditioned *ready* source \(\eta_c=U_c(\cdot\mid E_c)\) has eight extra hidden constraints and is not interchangeable with \(U_c\).

For a paper-only passive experiment, a complete finite word means all \(o(W),o(FW),\ldots,o(F^T W)\). It does not include invented physical detector/status outputs. Any actual setting/controller/clock/readout/failure register must be *added to the common operational dictionary only if sourced* and independently accounted.

The no-go and candidate screening below concern passive deterministic factoring unless explicitly labelled otherwise. No writes, inverses, reinitializations or physical detector operations are assumed.

## 2. NATIVE-CONE-T: a source-native causal snapshot sufficient for a fixed horizon

For an integer \(T\ge1\), define the following sets of sites, interpreted modulo L and with duplicate residues merged:

\[
I_X(T)=\{-T,-T+1,\dots,1+2T\},\quad
I_Y(T)=\{-(T-1),\dots,1+2(T-1)\}.
\]

Define the *initial-coordinate predictive snapshot*

\[
q_T(X,Y)=(X|_{I_X(T)},Y|_{I_Y(T)}).
\]

**Proposition CONE-T (finite-horizon sufficiency).** \(q_T(W)\) determines the complete **passive** two-site/two-slice observation word \(H_T(W)=(o(W),\dots,o(F^T W))\). No prior, independence, root, preparation, controller or Born rule is required for this pointwise determinism.

**Proof.** Write the current field after \(t\) native updates as \(u_t\), with \(u_0=X\) and \(u_{-1}=Y\). The recurrence is

\[
u_{t+1}(i)=u_{t-1}(i)\oplus u_t(i-1)
          \oplus\bigl(u_t(i+1)\lor u_t(i+2)\bigr).
\]

By induction, for \(t\ge1\), \(u_t(i)\) depends only on initial \(X\) at sites in \([i-t,i+2t]\) and initial \(Y\) at sites in \([i-(t-1),i+2(t-1)]\). The base \(t=1\) follows directly from \(F\). For the induction step, apply the three spatial shifts \(-1,+1,+2\) to these dependency intervals and include \(u_{t-1}(i)\); all inputs lie in the stated expanded intervals. The observation at time t uses \(u_t(i),u_{t-1}(i)\) for i=0,1. Taking the union for \(0\le t\le T\) gives exactly the two sets \(I_X(T), I_Y(T)\), including \(Y_0,Y_1\) from the initial read. Modular wrap only identifies some sites and cannot introduce dependence outside the projected residue sets. □

**Explicit T=2 candidate:**

    I_X(2)={-2,-1,0,1,2,3,4,5}       (8 distinct sites for L>=9)
    I_Y(2)={-1,0,1,2,3}              (5 distinct sites)
    q_2=(13 binary coordinates total).

All four initial observer-root pins \(X_0,X_1,Y_0,Y_1\) belong to q₂; conditional on b_c, q₂ carries **nine free input bits** under \(U_c\). Its 13-bit footprint is a *sufficient* snapshot for two future updates, not a minimal predictor. NATIVE-PRED-1's accepted **16 factor states/4 fixed-code bits** is a lower bound for a *different* exact autonomous-state problem; neither number claims observer memory usage or a native physical measurement cost.

When the intervals do not wrap around the ring (e.g., \(3T+2\le L\)), their displayed sizes are \(3T+2\) X bits and \(3T-1\) Y bits, totalling \(6T+1\). For larger T their site sets saturate through modular overlaps; no efficient all-horizon construction is inferred.

## 3. NATIVE-CONE-FAIL: q₂ is not an autonomous native factor

**Proposition CONE-FAIL (explicit root-compatible countercontrol).** The snapshot \(q_2\) from §2 does **not** admit a deterministic self-update \(\bar F_2\) satisfying \(q_2\circ F=\bar F_2\circ q_2\) on the full carrier, or even consistently for the canonical-root initial states \(b_c\).

**Proof.** Choose one W with \(X_i=0\) for all i and with \(Y_1=c\) and all other Y bits zero. Let W' be identical except \(X_{-3}=1\). At \(L\ge9\), residue \(-3\) lies outside \(I_X(2)=\{-2,-1,0,1,2,3,4,5\}\), and \(X_{-3}\) is not a root pin. Thus \(q_2(W)=q_2(W')\), and both belong to the same canonical-root class. The first native output field is \(A_i=Y_i\oplus X_{i-1}\oplus(X_{i+1}\lor X_{i+2})\). At i=−2, the first-X predecessor is \(X_{-3}\), while \(X_{-1}=X_0=0\). Hence \(A_{-2}(W')=A_{-2}(W)\oplus1\). Because −2 is a retained X coordinate of \(q_2(FW)\), these projected next states differ. No deterministic \(\bar F_2\) could map the shared q₂ input to both outputs. □

Thus a finite dependency cone supplies finite-horizon *prediction given hidden input bits*, not an autonomous local machine which continues updating indefinitely from only its current reduced snapshot. At each additional horizon it may need more boundary information. That is a mathematical boundary condition, not a universal obstruction to an observable predictive quotient.

## 4. NATIVE-PATCH-NOGO: no proper same-site two-slice coordinate patch is an exact autonomous factor

**Proposition PATCH-NOGO (new, specifically coordinate projections).** Let \(I\) be **any** nonempty proper subset of the ring sites \(\mathbb Z/L\mathbb Z\), and let

\[
q_I(X,Y)=(X|_I,Y|_I)
\]

retain the complete two-slice coordinates at exactly those sites. There is no deterministic \(\bar F_I\) satisfying \(q_I\circ F=\bar F_I\circ q_I\) over the full state space \(S_L\).

Moreover, when \(I\supseteq\{0,1\}\), this non-intertwining has a witness with both initial states in **the same canonical-root class** b_c, for either c. Thus adding any proper, fixed selection of same-site microscopic coordinates to the original two-site cut cannot yield an exact autonomous coordinate-projection factor on that root class.

**Proof.** Because I is nonempty and proper on a cyclic ring, there exists \(i\in I\) whose immediate predecessor \(i-1\notin I\). Otherwise closure under predecessors would force I to contain every ring site. Choose W with X identically zero and Y arbitrary (for the rooted witness, choose \(Y_1=c\) and all other Y bits zero). Let W' differ only by flipping \(X_{i-1}\). Since \(i-1\notin I\), \(q_I(W)=q_I(W')\). With L≥9, the indices \(i-1,i+1,i+2\) are distinct. Set all other X bits to zero. In \(f_i(X)=X_{i-1}\oplus(X_{i+1}\lor X_{i+2})\), flipping \(X_{i-1}\) changes \(f_i\) by exactly one, with the OR term fixed at zero. Hence the next native current field at site i flips, \(A_i(W')=A_i(W)\oplus1\). Site i is retained by q_I, so \(q_I(FW')\ne q_I(FW)\). This contradicts any deterministic self-update of the projection.

If I contains observed sites 0 and 1, neither root-fixed X0 nor X1 can be the flipped \(X_{i-1}\) (it lies outside I). Choose the same Y1=c and X0=X1=Y0=0 in both worlds, so both belong to b_c. Both have positive U_c mass because U_c has full support on that root. The same contradiction holds. □

**Exact limitations:** This no-go targets **raw coordinate restrictions containing both slices at each retained site**, with no nonlinear synthesis, hidden compression, auxiliary bookkeeping or supplied external boundary data. It does not rule out q∞, q=id, conjugate/skew factors, statistics over histories, observer-level belief states, stochastic innovations, externally driven boundary conditions, or source-justified interventional factors. It is also not a quantum no-go theorem. The selected local F and L≥9 are premises, not deduced here from bare observer incompleteness.

## 5. Two alternative native predictive descriptions that remain mathematically possible

### A. Exact passive autonomous future-trace quotient q∞

The canonical map \(q_\infty:S_L\to Q_\infty\) sends W to the equivalence class of all W' with exactly the same passive readout word \(o(F^t W)\) for every t≥0. The quotient is deterministic, autonomous and reversible (on the full finite permutation carrier), with readout inherited from o. This is not a new construction: see [Substratum Proposition 24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md).

It is an exact *candidate mathematical factor*. Its **size**, whether it is a proper reduction of \(S_L\), whether it has an efficient finite local representation, and whether it intertwines **any physically sourced nontrivial intervention** are not determined here. One can always use q=id as a trivial autonomous factor, but that does not extract an observer-available physical subsystem.

NATIVE-PRED-1 proves \(|q_\infty(b_c)|\ge16\) at the canonical root. The raw initial observation \(\,o(W)=b_c\,\) is constant there, so **q∞ cannot be a deterministic function of the initial visible record** on that ensemble. It is therefore invalid to call its full state directly accessible to that observer. This does not exclude some later statistical estimate, partial herald, augmented physical sensor or externally supplied physical access.

### B. Exact Bayesian observer-history belief state ρ_t (not an autonomous microscopic factor)

Given the mathematical root prior \(U_c\), the native law F, and an already retained passive history \(h_t=(o(W_0),...,o(W_t))\), define \(\rho_t(w)=\Pr(W_t=w\mid h_t)\) over the entire ring state S_L. This is defined for positive-probability histories under that stipulated model.

Let \(z\) be the next observed two-site/two-slice readout and define

\[
p(z\mid\rho_t)=\sum_{w\in S_L}\rho_t(w)\,\mathbf1_{\{o(Fw)=z\}},
\]

\[
\rho_{t+1}(w')=
\frac{\mathbf1_{\{o(w')=z\}}\rho_t(F^{-1}w')}
     {p(z\mid\rho_t)}
\quad\text{when }p(z\mid\rho_t)>0.
\]

These are standard Bayesian filtering identities for a deterministic hidden-state model with passive observations; the passive history statistics are reproduced exactly, and prediction depends on \(\rho_t\) rather than the entire explicit earlier word when the model is supplied. This is a *history-updated probabilistic belief state*, not a deterministic \(q(W)\) that evolves autonomously without observation-dependent conditioning.

The update can be defined from accessible **records** and a mathematically specified model but does not establish physical memory, computation, an instrument that obtains the readings without disturbing the ring, or efficient resources. A naive explicit representation has up to \(2^{2L}\) microscopic probability weights; this is not a proved lower bound on the most efficient encoding. Nor is it a quantum state or derivation of Born statistics.

**Practical implication:** One must distinguish (1) a microscopic autonomous predictive factor, (2) a finite-horizon hidden-coordinate causal cone and (3) an observer-updatable stochastic belief state. Each solves a different mathematical problem. Their existence does not by itself implement the one physically selected OI operational theory needed for QM.

## 6. Native physical-source audit and first missing ingredient

The pinned [CP-PREP-1 source selection](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md) ended with **NOT PASSED**: an external Fredkin–Toffoli routing interaction was not identified as an executing process under this particular unchanged SM ring. No further native gate, controller, root source or new physical premise was authorized by that selection.

| Item | Mathematical source or result | Is a physically executable native operation actually supplied? |
| --- | --- | --- |
| F and inverse | F is the fixed reversible SM branch; inverse is an algebraic identity | Native law is a selected model input; no independently constructed laboratory substratum or inverse actuator |
| Canonical root law \(U_c\) | Normalized common-root mathematical prior, full support on all unconstrained hidden bits | **NO** prepared-root/request source and source renewal demonstrated |
| Ready law \(\eta_c\) | Eight-constraint conditional measure with exact one-tick pushforward | **NO** producer of the constraints or honest native herald/failure process |
| Passive readout \(o\) | Coordinates at sites 0 and 1 in two slices | **NO** physically accounted nondemolition reader, register, clock or retained-history interface demonstrated |
| Causal-cone \(q_2\) | Exact 13-bit hidden-coordinate snapshot for two-step predictions | **NO** observer port exposing outer sites, or source of simultaneous snapshot without changing the interface |
| Global quotient \(q_\infty\) | Mathematically valid passive deterministic factor | **NO** physical device to compute, store, read or update the quotient label from the declared observer access |
| Belief filter \(\rho_t\) | Exact classical statistical update given stipulated \(U_c,F,o\) and records | **NO** sourced computational memory/time/device or guaranteed noninvasive readout |
| Active setting/control operations | No q-compatible nontrivial native controller map identified under CP-PREP-1 | **NO**; cannot import INT-FACTOR-1 toy flips, a Fredkin abstract gate or inverse dynamics as physical operations |
| Complete operational logs | Required prep failures, read errors, aborts, residual state, resets, controller and apparatus records | **NO** physically specified complete-record process |
| Quantum target | A common classical-preserving selected operational sector meeting QM soundness/completeness | **NOT DERIVED**; Born, coherent interference, Bell, composition, reusable quantum instruments and Level-B #1216 approximation stay OPEN |

**Earliest blocked interface:** before promoting any of these mathematical predictive descriptions to a physical OI observer model, one must **source a genuine root/request preparation and the physical reader/controller/record interface under the same F**. The source audit does not even produce an authenticated set of nontrivial accessible interventions to test against q. Building a formal quotient or Bayesian posterior cannot fill that physical gap.

**Disposition:** **STOPPED — PHYSICAL SOURCE NOT PASSED / UNSOURCED**, while the scoped passive mathematical results above are new **review-pending** propositions. This is not a no-go for physically available OI–QM equivalence; it is a precisely located missing-source obstruction for this selected ring and current evidence.

## 7. Implications for #1169, #1216 and #1220

- **#1169 physical operational selection:** A selected *visible* operational subtheory must specify a common preparation/measurement/controller dictionary and state updates. q∞'s abstract existence does not select those operations. The coordinate-patch no-go prevents mistaking an enlarged *raw local readout* for a closed deterministic native operational subsystem. A non-coordinate factor or physical observer-history predictor remains conceivable, but must be sourced, not inferred from representability.
- **#1216 approximation:** Exact finite-horizon cone prediction of the native *classical* law is not Level-B approximation to QM. A mathematically Bayesian predictor is a stochastic description derived from a stipulated source; it does not derive quantum operations, uniform precision or scalable preparation. NATIVE-PRED-1's exact deterministic four-bit-capacity bound also cannot automatically constrain randomized or approximate belief-state descriptions.
- **#1220 resource costs:** q₂'s 13-bit input footprint, q∞'s unknown finite size and ρ_t's potentially exponential naive representation have different cost meanings. None is an established physical hardware overhead or efficient-simulation theorem. Quantitative resources require a sourced scalable implementation and fair total accounting.
- **#1143 classical preservation and #868 composition:** The ring's passive records are legitimate classical stochastic histories under an assumed normalized source; they do not rule out classical observations nor generate quantum coherence, Bell pairs, joint-state closure, no-signalling across composite preparations or Born selection.

**Precise next owner gate (no execution authorized here):** Ask for **one physical source candidate** that identifies a ready/request producer, a nondisturbing or otherwise accounted observer readout, and a retained record/control process under the *same actual native F*. Only then test whether the admitted operations factor through a proposed **non-coordinate** q (or, alternatively, whether an admitted observer-updated belief state suffices for the operational interface). If no such process can be demonstrated, record NOT PASSED and stop rather than postulate extra operations to fit QM.

A positive operational result would still need independent derivation of the quantum repertoire across classical and quantum contexts; a negative source result is meaningful at the stated source/interface scope.

## 8. Independent mathematical/source-review checklist and governance

**This packet has no independent mathematical review** and must not inherit the existing accepted result NATIVE-PRED-1 at 95cead38. A separate non-author reviewer should:

1. Verify cone dependency intervals for X and Y, time-index convention, the exact T=2 sites and bit counts, including L=9 modular-wrap case.
2. Check the explicit q₂ root-preserving counterexample with X_(−3)=1, Y1=c, and A_(−2) effect. Compare claimed nonautonomy only for q₂, not all possible factors.
3. Check PATCH-NOGO for every proper nonempty subset I using the i-1 boundary predecessor and L≥9 non-overlap; verify root-class witness when {0,1}⊆I. Ensure "coordinate projection" restrictions remain explicit.
4. Confirm that q∞ existence is **already** Substratum Proposition 24.4, that its state is not determined by the initial two-site observation under U_c, and that properness/smallness is not asserted.
5. Verify Bayesian filtering normalization, time ordering, readout-conditioned update and absence of any implicit physical nondemolition record source.
6. Verify that physical-source screening does not turn source-pinned U_c or conditioned η_c into an apparatus, nor mistake classical exact-history prediction for a quantum/Born result.
7. Check the negative classification is **source NOT PASSED**, not proof of impossibility for all latent source mechanisms, and that no new numerical/Lean/computational/experimental authorization is inferred.

**Requested review outcome:** ACCEPT / ACCEPT WITH NITS / REVISE at an exact immutable Git head, identifying any separate documentation nits. Maintain original NATIVE-PRED-1 mathematics and all other historical research papers unchanged. PR #1222 remains **draft and unmerged** pending an independent owner integration decision.

**No scientific/Boolean simulation, numerical execution, Lean build, native experiment, newly adopted physical premise, F/E designation, dispatch, publication, or merge occurred in this paper-only writer unit.**