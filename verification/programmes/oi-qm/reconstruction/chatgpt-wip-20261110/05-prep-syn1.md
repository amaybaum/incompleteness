**PREP-SYN-1 — writer draft, 10 November 2026. NOT independently reviewed.** Bounded paper assessment for [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) equally; coordinates with [#866](https://github.com/amaybaum/incompleteness/issues/866), [#1143](https://github.com/amaybaum/incompleteness/issues/1143), [#868](https://github.com/amaybaum/incompleteness/issues/868) and [#1220](https://github.com/amaybaum/incompleteness/issues/1220). Follows the [Unit 2 v1a critical audit](https://chatgpt.com/space/page_e94d275c997c8191b2480f038ac1884b). Baseline is [preparation-loading.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md) at main pin cac5d26441dd33e9348151487e4df7b547195481.

**Decision:** one-bit syndrome correction is a mathematically sufficient change for ONE requested output bit under a changed request interface, but is not a full-state preparation and has no sourced physical pre-tick sensor/actuator. Full ready/request producer remains UNSOURCED. New information-timing, open-loop, and false-herald observations are conditional hand deductions; no scientific run, Lean proof, new physical principle or independent ACCEPT is claimed.

# 1 Pinned rule and exact precursor contract

For L≥9 on the two-slice binary SM ring, the previously studied physical proposal is F(X,Y)=(f(X) XOR Y,X), where f_i(X)=X_(i−1) XOR (X_(i+1) OR X_(i+2)). At the precursor visible root b_c, X_0=X_1=Y_0=0, Y_1=c, with other coordinates independent fair bits under the canonical rooted prior U_c.

The first post-tick controller field is A_1=X_0 XOR (X_2 OR X_3) XOR Y_1. Define G=X_2 OR X_3. At the stated root A_1=c XOR G, and the source has P(G=0)=1/4, P(G=1)=3/4. These are existing accepted-source arithmetic facts, not new discovery. The *full* target I_c additionally has eleven specified ready zeros across two slices, and the exact precursor E entails three zero pins plus five Y correlations (preparation-loading eqs. 5–6). Under U_c its conditional event mass is 2^(−8), as already proved in that source.

Our question is whether physical information and feedback can substitute for some **marginal output** restrictions without claiming that the same full-ready contract has been satisfied.

# 2 SYN-1: compensating one output (conditional, changed interface)

Suppose an as-yet-unsourced native controller knows G BEFORE the forward F tick and can write Y_1=c XOR G without changing the required X coordinates. Then A_1=G XOR (c XOR G)=c pointwise for either desired c. No replacement of F is needed for this algebra.

The availability of the pre-tick G sensor and the selectable Y_1 write is a **premise**, not a consequence of F. This changes the original visible precursor root, since its previously fixed Y_1=c becomes a hidden-correlated value. The prior common-root/preparation theorem cannot simply be transferred.

The full target still requires B=X and, in particular, B_2=B_3=0; hence X_2=X_3=0 remains necessary for that original target, regardless of encoding Y_1. One corrected output bit is not a full prepared state, a heralded factory, an observer instrument, reuse or a quantum operation.

# 3 SYN-2: open-loop optimum and information prerequisite

Permit a more general but still unsupported program encoding Y_1=c XOR D, with D independent of G (D may use independent random coins). Then P(A_1=c)=P(D=G)=(1/4)P(D=0)+(3/4)P(D=1)≤3/4. The best open-loop choice D=1 attains 3/4 but changes the original root. The original literal encoding D=0 has success 1/4.

With side information M available before the write, D=estimate_G(M) has error p_e=P(estimate_G≠G). Exact compensation requires G to be a function of M. Under the canonical prior H(G)=h₂(3/4)≈0.811278 bits, so exact pre-tick information must satisfy I(G;M)=H(G). For any p_e≤ε≤1/2, the familiar binary Fano inequality gives I(G;M)≥max(0,h₂(3/4)−h₂(ε)); see [Fano inequality](https://www.scholarpedia.org/article/Fano_inequality). This is an *information bound*, not a physical tick, memory-cell, work, energy or actual-readout bound. A supplied source correlation is not the same as a physical sensor.

# 4 Timing and false-herald separation

The declared two-site/two-slice mathematical observer at t=−1 sees only X_0,X_1,Y_0,Y_1, so under canonical U_c it has no information about G: I(G;O_(−1)|c)=0. One F tick later its controller readout includes A_1=c XOR G. The two-time mathematical record reveals G by G=A_1 XOR c and thus contains H(G)=h₂(3/4) bits about G. This information arrives **after**, not before, the specified loading operation. It is not a demonstrated physical read-and-rewrite instrument or a reset.

On the original root, the single-coordinate pass event H={A_1=c} equals {X_2=X_3=0} and has U_c(H)=1/4. The full original precursor condition E⊂H additionally requires X_(−1)=0 and five independent Y-coordinate relations; thus U_c(E|H)=(1/2)^6=1/64, and U_c(E)=1/256. A device checking only the requested controller bit would fail to certify the full precursor on 63/64 of the *mathematically passing* canonical-source cases. This is an ensemble false-positive diagnostic, NOT a real herald, measured success probability, or expectation of 256 physical attempts.

# 5 Physical-source decision and next bounded gate

The existing reversible F and visible projection make the post-tick syndrome *mathematically* available, but do not source an earlier probe, clock, request generator, sensor, actuator, field preservation, histories, failures, residual environment or renewal. The full precursor remains unproduced. The state-dependent ring is bounded-range, so this local correction also does not solve separated Bell experiments or quantum selection.

A discriminating next PAPER source unit should ask whether a pre-existing independently motivated F evolution and apparatus can convey G before Y_1 is set, with a **single fixed native law**, setting-independent uncontrolled source, explicit read/write and logged preparation histories. If such a process cannot be identified, record UNSOURCED; do not invent it. If the exact original I_c target is retained, prioritize physical production of its strict precursor E instead of substituting the weaker one-bit contract.

The acceptance test must distinguish (i) correct A_1, (ii) complete target state/correlations, (iii) actual physically produced source and accessible success/failure, (iv) repeatable output, and (v) cost uniformity. Keep classical registers intact and use #1143 C0/C1 controls; keep #868 Bell, Born and joint composition separate; use the #1220 two-ledger total-resource contract and leave #945 finite-bit repair untouched.

# 6 Separate reviewer brief (not dispatched)

A genuinely independent reviewer should check the pinned source and all of the following: A_1 formula and distribution of G; the changed-root caveat in SYN-1; ≤3/4 optimum for any independent randomized recoding and 1/4 for the original root; Fano assumptions and the entropy of G; post-tick timing and whether O_0 actually contains A_1; exact conditional event arithmetic U_c(E|H)=1/64 with L≥9; why an accessible mathematical projection does not source a real sensor; the separation from full original I_c, native quantum control, Bell, Born and scalable cost. The review should report ACCEPT / ACCEPT-WITH-NITS / REVISE with exact sections, and distinguish previously reviewed facts from new deductions.

**No independent review was performed in this writer session.** No native/scientific/numerical execution, branch/PR, freeze, F/E, dispatch, premise adoption, manuscript edit, or merge. The earlier accepted results and all owner gates remain unchanged.