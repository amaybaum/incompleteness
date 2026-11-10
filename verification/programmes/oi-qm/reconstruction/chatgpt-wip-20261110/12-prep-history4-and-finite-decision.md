# PREP-HIST-4 — Four-tick masked-read obstruction and finite-horizon observability dichotomy

**Paper-only WIP · 10 November 2026 · newly authored, NOT independently reviewed.**

**Status and provenance:** This document is a *new* analytical continuation of [PREP-READ-2](11-prep-read2.md), whose previous bounded mathematics was independently accepted as part of the [Codex paper review at 6879c7c0](https://chatgpt.com/space/page_2f791d4a97fc8191ade6141a5ed9bdfe). The current propositions **were not covered by that review**. They are source-pinned hand derivations, not a Lean/kernel result, scientific numerical execution, native instrument or physical OI sourcing pass.

**Main issues:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) remain equally prioritized. [#866](https://github.com/amaybaum/incompleteness/issues/866) owns physical controller/preparation supply; [#1143](https://github.com/amaybaum/incompleteness/issues/1143) retains classical settings; [#868](https://github.com/amaybaum/incompleteness/issues/868) retains physical Bell pair/composition; [#1220](https://github.com/amaybaum/incompleteness/issues/1220) owns resource accounting. The native physical source remains **NOT PASSED / UNSOURCED**. Keep PR #1222 **draft/unmerged**.

**Headline findings (paper-level):**
1. For **every** L≥9, with original setting c=1 and the original two-site, two-slice observer, **two canonical-root initial states with different full-precursor readiness yield identical observable histories for four forward SM ticks**. Therefore no deterministic exact classifier of the readiness event on all canonical-root states can use at most four such ticks. An exact classifier, *if any*, needs at least **five** ticks; five are not proved sufficient. This strengthens the reviewed two-tick lower bound in this specific setting.
2. For c=1 and **three** forward ticks, flipping Y5 maps **each fully ready state** injectively to a nonready state with the **same full original-observer history**. Hence the conditional probability of full readiness in any positive-probability three-tick history atom is at most **1/2**; independent randomized acceptance cannot raise it above 1/2. This is a weaker numerical posterior bound than READ-2's ≤1/8 at two ticks but covers a later horizon.
3. In any fixed **finite** deterministic world with a fixed observation map, exact discrimination of a specified initial event by some finite passive history has a generic *decidable-in-principle* dichotomy: by a horizon of at most `|S|−1` updates, either each history class is entirely ready or entirely nonready, or at least one ready/nonready pair is indistinguishable for **all** future passive histories. This is standard finite-state partition refinement, not an OI-specific novelty or an efficient test.

None of these statements constructs a physical detector, an accessible persistent memory, a success flag, a prepared quantum state, Born probabilities, a quantum Bell experiment, or an efficient simulator.

## 1. Fixed source and exact experiment

All formulas specialize the independently reviewed source [preparation-loading.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md) and [physical-interface.md](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md), at immutable repository main `cac5d26441dd33e9348151487e4df7b547195481`. Original user-facing summary [PREP-READ-2](11-prep-read2.md) is an accepted scoped earlier hand-analysis, not re-proved here.

Let L≥9, with indices modulo L, and let a two-slice complete ring state be W=(X,Y)∈{0,1}^(2L). The *same unchanged native* second-order update is

```
f_i(U) = U_(i−1) XOR (U_(i+1) OR U_(i+2))
F(U,V) = (f(U) XOR V, U).
```

On the original incoming root `b_c`, require `X0=X1=Y0=0` and `Y1=c`; the canonical-root prior `U_c` is uniform on all remaining coordinates. The original **full** precursor condition `E_c` adds:

```
X_(−1)=X2=X3=0
Y_(−2)=X_(−3), Y_(−1)=X_(−2)
Y3=X4 OR X5
Y4=X5 OR X6
Y5=X4 XOR (X6 OR X7).
```

Its canonical conditional mass is `U_c(E_c)=1/256`, as proved in the pinned source.

The observer never changes: it sees the two-slice **coordinates only at sites 0 and 1**, at each mathematical tick. Write `o(W)` for that four-bit projection. The T-tick retained mathematical history, *not itself a physical memory*, is

`H_T(W)=(o(W),o(FW),...,o(F^T W))`, with T≥0.

Here T=1 means one forward update; T=4 includes input and four post-input records. The original starting cut is t=−1 in the source document; this indexing is relative to that cut.

## 2. Proposition H3 — three-tick hidden-bit pairing for c=1

**Claim.** For every W∈E_1, let `J(W)` be the state obtained by flipping only the initial Y5 bit. Then

`J(W)∉E_1` and `H_3(J(W))=H_3(W)`.

Consequently, for any positive-probability atom h of H_3 under the **uniform** U_1,

`Pr(E_1 | H_3=h) ≤ 1/2`.

The same bound holds for any positive-mass acceptance rule based only on H_3 and private randomness independent of the complete ring input.

**Proof of history identity.** Let the successive current slices be

`A=f(X) XOR Y`, `C=f(A) XOR X`, `D=f(C) XOR A`.

On E_1 the first native tick yields the reviewed prepared conditions

`A_(−2)=A_(−1)=A0=A3=A4=A5=0`, `A1=1`, `A2=z`, and `X_(−1)=X0=X1=X2=X3=0`.

Flipping only Y5 changes A5 and no other A coordinate, and leaves original input-site observer data and the first output record identical. At the next tick, the observer sees C0 and C1, neither of which depends on A5; likewise `C_(−1)` and `C2` are unchanged. On E_1,

`C2 = X2 XOR A1 XOR (A3 OR A4) = 1`.

The same remains true for the Y5-flipped state because A1,A3,A4,X2 were not changed. The third-tick observed current bits are

`D0=A0 XOR C_(−1) XOR (C1 OR C2)`,

`D1=A1 XOR C0 XOR (C2 OR C3)`.

Flipping Y5 can affect C3 (and other unobserved C sites), but **C2=1** forces both displayed OR terms to equal 1. Hence D0,D1 and all previous two-slice observer fields through H_3 are unchanged. Flipping the prescribed Y5 of an E_1 state violates its one mandatory Y5 constraint, so J(W)∉E_1. □

**Proof of posterior statement.** J is an injection from the ready states in any H_3 atom into disjoint nonready states in that same atom; all states in the canonical-root support have equal U_1 mass. Therefore the number of nonready states in any such atom is at least the ready count. Thus its conditional ready fraction is at most 1/2. Any randomized acceptance based only on H_3 and independent noise forms a mixture of these atom posteriors. □

**Scope.** This is a **c=1** result under exactly the original source, root and complete mathematical two-site history. It does not prove anything about c=0, a changed detector, active interventions, externally correlated private randomness, or a different preparation prior. The old c=0 third-tick influence example in [PREP-READ-2](11-prep-read2.md) is not contradicted.

## 3. Proposition H4 — an explicit four-tick indistinguishable ready/nonready pair

**Claim.** For **every ring L≥9**, the map H_4 does not decide E_1 on the entire canonical-root support. In particular, there is no universal zero-error indicator `g(H_4(W))=1_{E_1}(W)` valid for all W∈b_1.

**Witness.** Fix the initial current slice X identically zero. Fix initial Y identically zero except `Y1=1` and `Y5=b`, where b is either 0 or 1. Call the resulting two complete initial states W_b.

They both obey the original visible root b_1. W_0 satisfies every extra E_1 condition. W_1 violates E_1 *only* at the original Y5 relation (which requires Y5=0 when X is zero).

Using only the unchanged native F and hand algebra, denote current slices after the first, second, third, and fourth updates by A,C,D,Q. A equals the initial Y because X=0. All four observer histories agree, as follows.

| Input / update | Observed site-0 current | Observed site-1 current | The preceding-slice site-0/site-1 bits |
| --- | --- | --- | --- |
| Input W_b | X0=0 | X1=0 | Y0=0, Y1=1 |
| 1st update: A | A0=0 | A1=1 | X0=0, X1=0 |
| 2nd update: C | C0=1 | C1=0 | A0=0, A1=1 |
| 3rd update: D | D0=0 | D1=1 | C0=1, C1=0 |
| 4th update: Q | Q0=1 | Q1=1 | D0=0, D1=1 |

**Derivation of the fourth-tick mask.** The intermediate coordinates required for the two original read sites are:

```
A1=1, A5=b, all other A_i=0

C_(−2)=0, C_(−1)=1, C0=1, C1=0, C2=1,
C3=b, C4=b, C5=0

D_(−1)=1, D0=0, D1=1, D2=b, D3=1 XOR b

Q0 = C0 XOR D_(−1) XOR (D1 OR D2)
   = 1 XOR 1 XOR (1 OR b) = 1

Q1 = C1 XOR D0 XOR (D2 OR D3)
   = 0 XOR 0 XOR (b OR (1 XOR b)) = 1.
```

All identities use the original f_i, with no alternate gate or fitted initial source. For L≥9, the listed site indices and the relevant local neighbourhoods do not accidentally identify the Y5 perturbation with another listed input site modulo L. Both complete histories H_4(W_0) and H_4(W_1) are therefore **identical**, although exactly one W_b is ready. □

**Consequence:** an exact deterministic classifier of **all** states in the canonical-root support cannot exist at T≤4, since H_T is a prefix of H_4. Thus **at least five forward updates are necessary** for universal complete-predecessor certification under this *fixed observer*. Whether T=5 (or any later finite horizon) suffices remains **OPEN**.

**Important non-consequence:** a single indistinguishable ready/nonready pair does **not** rule out a *sound positive-yield herald* that simply declines to accept that pair's history. The c=1 H3 posterior bound in §2 is stronger for T=3, but no corresponding uniform posterior ≤1/2 is claimed for T=4. Nor does this witness prove the two states stay observationally identical forever.

## 4. Proposition FIN-H — finite-state eventual-observability dichotomy

This section is a **general standard finite-state partition-refinement argument**, not a new OI physics law. Its role is to make the unresolved longer-history question mathematically precise.

Let S be any finite state space of size M, F:S→S a deterministic complete update (bijective here), o:S→O a fixed output map and E⊂S a designated *initial-event* predicate. Define H_T and `s ~_T t` iff H_T(s)=H_T(t). These equivalence relations get finer as T grows. Since each strict refinement increases the number of equivalence classes, there can be at most M−1 strict refinements in total.

**Stabilization lemma.** If `~_T = ~_(T+1)` once, then the observation partitions never refine further. For s~_T t, equality at T+1 says that their shifted successors F(s),F(t) have equal histories through T, i.e. F(s)~_T F(t). Thus every future shift stays in the same relation and all later output bits agree. By induction `~_(T+k)=~_T` for all k≥0.

Therefore the full-history indistinguishability relation is already determined by `H_(M−1)` (a deliberately conservative bound; the initial observer partition may sharpen it).

**Dichotomy for exact universal classification on a known input subset A⊂S.**

- If every H_(M−1) atom intersected with A is contained either wholly in E or wholly in A\E, then a finite mathematical decision rule `g(H_(M−1)(s))=1_E(s)` exists on A.
- Otherwise there exist s∈A∩E and t∈A\E with identical H_(M−1). By stabilization, they have identical observer histories for **every future passive time**, and no such finite or infinite passive-history classifier can distinguish their readiness.

For the binary ring, M=2^(2L). Thus T≤2^(2L)−1 forward updates is a **finite in-principle threshold** sufficient to settle the yes/no mathematical classification question *if one had a way to evaluate the finite partition*. This gives **no practical efficient algorithmic cost, physical clock, memory, reliable detector, or hardware readout**. No enumeration or computation of these partitions was executed in this WIP.

This is **not** a theorem that the ring's readiness E_1 is ever decidable from its two-site history. Which side of the dichotomy the selected ring realizes remains open.

**Precise distinction from heralding:** even if full classification fails, there may be an observation atom of positive canonical probability entirely contained in E, allowing a mathematically sound but incomplete herald. Conversely a full classifier determines readiness for all branches. Their existence questions and resource costs are different.

## 5. Physical interpretation and cross-programme discipline

- **Native positive content:** the exact F dynamics carries and sometimes masks local dependencies. The paired W_0/W_1 example exposes a nonlinear masking mechanism that defeats the naive inference “a signal enters the causal cone, therefore the observer knows the hidden bit.”
- **Source gap:** the time-indexed mathematical history is a list of projection values, **not** a native physical recorder. No apparatus storing five or more clocked samples, physically selectable root, nondemolition probe, flag, failure log, source regeneration or reusable post-measurement ring has been supplied. The earlier [CP-PREP-1 gate](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md) remains NOT PASSED.
- **#1216 accuracy:** H3 and H4 concern **specific exact classification** under one input class and observer cut; they do not impose a TV bound on **QM benchmark complete histories**. Exact failure of universal readiness classification does not rule out arbitrary finite-precision operational approximation with a different common physically sourced interface.
- **#1143 classical contexts:** the binary ring is an explicitly classical reversible model. Its behavior must not exclude classical measurement regimes. Neither masked information, partial readout nor eventual finite classification selects Born probabilities or rules out the reviewed classical countermodels.
- **#868 Bell/quantum:** no prepared long-edge pair, compatible local quantum instruments, joint-state closure, no-signalling physical record mechanism or Tsirelson bound is derived.
- **#1220 resources:** M=2^(2L) gives an exponential-in-L *upper horizon for conceptual determination*, not a proven runtime lower bound, an efficient classical sampler, or a physically possible clock/memory schedule. Actual recording, detector errors, sources and renewal must be accounted separately.

**First next scientific question:** Determine whether E_1 is **fully decidable** or **partly sound-heraldable** from the unchanged original two-site passive history using an independently reviewed *symbolic* argument; keep the two questions separate. If neither can be decided analytically, propose a separate authorized bounded computational study **before performing any search**. A numerical exploration performed ad hoc would violate the present paper-only scope.

## 6. Independent-review packet and stop rules

**This new paper has NOT been independently reviewed.** The prior [Codex report](https://chatgpt.com/space/page_2f791d4a97fc8191ade6141a5ed9bdfe) covers the unchanged earlier eleven archives at `6879c7c023259d00d2b9a7ba152c694328d56458` only. The present #12 file and index update must not inherit that acceptance.

An independent reviewer should check:

1. Ring rule F and the E_1 precursor event against the pinned main source for all L≥9, especially modulo-L site reuse.
2. **H3:** Verify C2=1 on all E_1 and on the Y5-flipped partner; D0/D1 mask any C3 difference. Check the injection and equal-mass posterior ≤1/2 for **every** H3 atom under U_1.
3. **H4:** Verify W_0∈E_1, W_1∉E_1 with the same b_1 root; recompute displayed C/D/Q intermediate values by hand; verify for L=9 and general L≥9 without code, unless a separate scientific execution authorization is given.
4. Confirm H_4 equality on the **two-slice local history**, not only the latest current field, and the exact shift from input t=−1 to four forward updates.
5. Check logical scope: the pair disproves **universal exact readiness classification** at T≤4, **not** every positive-yield sound herald or eventual infinite-history distinction.
6. **FIN-H:** Verify the relation recursion and why equality of two consecutive global partitions causes permanent stability; distinguish the global S from initial-root subset A (restricting the partition prematurely can invalidate the early-stop proof).
7. Check the bound M−1, and no claim of polynomial-time decidability, physical implementability, quantum approximation error floor or real memory supply.
8. Preserve accepted earlier archive claims, classical controls, actual observer/access/source limitations and all #866 physical gate statuses.

Review verdict to request: **ACCEPT / ACCEPT WITH NITS / REVISE**, with exact file/section and status pinned to the WIP commit. An accepted mathematical result is not a physical preparation mechanism.

**No physical premise adoption, science/Lean/numerical execution, special F/E designation, experiment, authorizing issue change, PR merge or manuscript update took place.**