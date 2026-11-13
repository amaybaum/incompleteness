**PREP-NATIVE-1 — paper-only source and obstruction assessment, 10 November 2026.**

**Status: writer-authored scoped mathematical corollary; INDEPENDENT REVIEW PENDING; physical source still UNSOURCED.** This paper carries forward [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) at equal priority, with native-preparation accountability in [#866](https://github.com/amaybaum/incompleteness/issues/866), classical-preservation controls from [#1143](https://github.com/amaybaum/incompleteness/issues/1143), composition sourcing in [#868](https://github.com/amaybaum/incompleteness/issues/868), and complete resource accounting in [#1220](https://github.com/amaybaum/incompleteness/issues/1220).

**Precise result:** With a canonical-root uniform initial law and the unchanged closed reversible ring, passive evolution cannot concentrate probability into the complete eight-condition precursor at a predetermined time beyond 1/256. The full-ring output law remains at total variation at least 255/256 from the required law. A union bound gives at most T/256 probability of ever visiting the event at T predeclared passive cuts. These facts are direct, explicit **corollaries of the already-reviewed support-counting/entropy analysis**, not a new physical no-go theorem or proof of OI–QM equivalence.

**Preserved previous result:** [PREP-8 conditional eight-bit SWAP/XOR factory](https://chatgpt.com/space/page_daabe5b3c6ec819187f0ef7730aad59f) is a writer draft, **not yet independently accepted**, and uses operations/ready auxiliary bits **not sourced as available native interactions**. This paper neither retroactively accepts that model nor silently converts the source stop to a pass. A separately accepted physical-source selection [CP-PREP-1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md) stopped without an executing switch from its external physical comparator.

No native/scientific/numerical experiment, Lean execution, physical-premise adoption, PR, branch push, F/E designation, dispatch, merge or manuscript promotion is part of this writer assessment.

# 1. Pinned sources and experimental contract

Read against immutable main source [cac5d26441dd33e9348151487e4df7b547195481](https://github.com/amaybaum/incompleteness/tree/cac5d26441dd33e9348151487e4df7b547195481), particularly:

- [Physical preparation and selectable loading §§3–7](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md) — complete target, eight precursor restrictions, common hidden prior, source-event mass, retained failure branches, and non-reset of the outgoing world.

- [Physical controller source-selection LEAD](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/physical-controller-20261107/LEAD.md) — root/ready/request producer, physical herald, accessible logging, controller clock and renewal unsourced.

- [CP-PREP-1 source selection](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md) — no identified Fredkin/Toffoli switch executing under unchanged SM ring; the inspected comparator has different dynamics.

- [PREP-8 abstract reversible construction](https://chatgpt.com/space/page_daabe5b3c6ec819187f0ef7730aad59f) — external clean bits, SWAP and controlled-XOR are explicit hypotheses; no source of their physical availability was found.

Fix an L≥9 cyclic binary ring. The complete two-slice state is W=(X,Y) with N=2L binary coordinates, and the already established reversible update is

    f_i(X)=X_(i−1) XOR (X_(i+1) OR X_(i+2)),
    F(X,Y)=(f(X) XOR Y, X),
    F^{-1}(A,B)=(B, A XOR f(B)).

The incoming visible root b_c is X_0=X_1=Y_0=0, Y_1=c. Set A_c={W:b_c holds}. The **canonical-root source** U_c is uniform on A_c, of cardinality |A_c|=2^(N−4).

The target full precursor event E_c is b_c plus the eight additional constraints:

    X_(−1)=X_2=X_3=0
    Y_(−2)=X_(−3), Y_(−1)=X_(−2)
    Y_3=X_4 OR X_5
    Y_4=X_5 OR X_6
    Y_5=X_4 XOR (X_6 OR X_7).

Under the reviewed source's counting, |E_c|=2^(N−12)=|A_c|/256 and U_c(E_c)=1/256. Define η_c=U_c(·|E_c), uniform on E_c. The reviewed one-tick loader maps η_c to the declared full target I_c distribution: (F)_#η_c. The actual source contract is one common law across both c values; the physical production of that law and the selectable root is not supplied.

# 2. Proposition N-1 — exact fixed-time no-go and its observable limitation

**Conditional statement (paper-level corollary; external review pending).** Let P be any permutation of the **same closed ring state space** and perform no ancillary interaction, postselection or state-dependent stopping. At a predetermined time, the ring law P_#U_c is uniform on P(A_c), a set with 2^(N−4) elements. Consequently

    Pr_{W~U_c}[P(W)∈E_c]
      = |P(A_c)∩E_c| / |A_c| ≤ 1/256.

Moreover, with full-ring TV defined by TV(μ,ν)=½ Σ_w |μ(w)−ν(w)|,

    TV(P_#U_c, η_c)
      = 1 − |P(A_c)∩E_c|/|A_c|
      ≥ 255/256.

**Proof:** P is injective and maps the equal-weight elements of A_c one-to-one to equal-weight elements of P(A_c). At most |E_c| of these outputs can lie inside the smaller target. For total variation, η_c assigns weight 256/|A_c| to each point of E_c while P_#U_c assigns 1/|A_c| to each point of P(A_c). The sum of pointwise minima is |P(A_c)∩E_c|/|A_c|; TV is one minus that overlap. □

**Specific native conclusion:** take P=F^t for any fixed nonnegative integer t. The conclusion holds for that fixed time with no new premise. The same argument applies to the **loaded full state** F(E_c) and target F_#η_c; at t=1, F(A_c) contains F(E_c), so the full-state TV lower bound 255/256 is **attained exactly**.

**Crucial scope:** This is a bound between **complete underlying ring states**, not automatically a TV bound on the observer's accessible histories. Projecting to fewer records can strictly reduce distance. A model that reproduces a limited visible experiment may fail to prepare E_c exactly but still have close visible records. This paper does NOT turn a full-ontology preparation gap into an unrestricted Level-B operational OI–QM obstruction.

**Not new as a general theorem:** the previously accepted loader already shows the eight-bit entropy/support mismatch and impossibility of fixed-time complete reset within the closed ring. N-1 expresses it as a sharp TV obstruction for the specific fixed-time distributional comparison, with no novel physical sourcing claimed.

# 3. Proposition N-2 — bounded passive waiting and stopping-time caveat

**Conditional statement:** Choose T≥1 predetermined candidate times t_0,…,t_(T−1). Sample one initial W~U_c and allow **only passive evolution** by the unchanged deterministic F in between. For the fixed target E_c at any candidate cut,

    Pr[there exists j<T such that F^(t_j)(W)∈E_c]
       ≤ min(1,T/256).

**Proof:** By N-1, every single-time event has initial probability at most 1/256. The union bound over T events yields the statement, regardless of temporal dependence among the events. □

This also bounds an idealized *passive waiting* strategy that magically detects E_c and stops on its first occurrence among T declared cuts; it does **not** supply an accessible physical herald or make stopping noninteracting. It says nothing decisive about eventual visitation at large T, and no general impossibility of adaptive preparation follows.

If a proposed controller physically writes, changes the underlying update, introduces a coupled reservoir, changes the input law after failure, or samples fresh trials, N-2's single passive-orbit hypotheses fail. Such a candidate must specify its own actual interaction, all accessible logs, repeated source generation and failures.

**Probability versus cost:** T/256 is a probability upper bound under a chosen initial ensemble, NOT an expected 256-tick factory cost. An expected-attempt calculation requires physical success flags, fresh or conditionally bounded success probabilities, accounted source renewal, and a valid stopping model—precisely the missing fields from #866/#1220.

# 4. One genuine declared visible-record bound (not a quantum result)

For the reviewed single loading tick, on the original root Y_1=c,

    A_1 = c XOR (X_2 OR X_3).

The two X bits are fair and independent under U_c. Hence the declared controller bit A_1 differs from the intended c with probability 3/4. In the **mathematically declared observer record** that includes c and this post-tick controller read,

    TV(Law_U(A_1), δ_c)=3/4.

The **complete accessible-history** law of that same declared mathematical two-site projection is therefore at least 3/4 from the ideal prepared-loader history law that has A_1=c deterministically, by data processing *in the correct direction* (a marginal can only decrease TV).

This is a different, narrower operational statement than the 255/256 full-state mismatch. It requires that the controller read really belongs to the declared record cut, which it does in the prepared-loader paper. It does NOT show a real physical sensor has been sourced, nor establish a quantum-Bell or complete OI–QM approximation floor.

If the experiment changes its root encoding, setting port, read cut, stopping time or failure alphabet, the 3/4 comparison must be re-derived for that changed interface; it cannot be silently transferred to a different candidate.

# 5. Why PREP-8 changes the assumptions, and the first unsupported source

The PREP-8 paper proposes eight clean auxiliary bits a=0⁸, 8 SWAP stages saving the originally unprepared constrained coordinates into a, and 5 controlled-XOR writes setting the Y correlations. Its augmented transformation T is a mathematically reversible permutation on (W,a); with U_c and clean auxiliary bits, the ideal full precursor law is η_c on W and the missing 8 bits are retained as output garbage. This construction is still **unreviewed as a separate writer draft**, and its gate and source assumptions are explicit.

N-1 does **not** refute that augmented result, because its assumptions differ. A physically interacting enlarged system can change the ring marginal while preserving injectivity of the complete world state. The matched capacity requirement in PREP-8 is eight bits of *distinguishable auxiliary output* under its specific everywhere-success/no-other-output hypotheses; it is not a universal hardware, thermodynamic or quantum cost.

**Native-source screen:**

- If one merely adjoins an independent auxiliary sector (even one that begins at zero) but keeps the joint update F×G with **no interaction back into the ring**, the ring marginal remains F^t_#U_c and N-1 still applies. An auxiliary label is not a preparer.

- If one adds SWAP, conditional XOR, prepared switch networks, a clock, a setting writer or a coupled reservoir, the complete source/interface is **different** and those operations require physical derivation. They cannot be called executable under the unchanged native ring merely because they are reversible functions.

- The independently accepted CP-PREP-1 selection audit found that its particular Fredkin/Toffoli physical switch does not supply the required native interaction under F. This is not an impossibility theorem for other candidate enlarged OI models.

**Earliest missing native step for PREP-NATIVE-1:** an independently sourced **coupled** operation that transfers information between the ring's initially unconstrained coordinates and a physically prepared reservoir/controller under one specified full-world reversible rule, together with its initial resource law. Without it, the eight-bit abstract capacity is not a native preparation. The source must support the original complete precursor and selectable c without fitting its hidden distribution directly to the desired target.

# 6. Decision and resource crosswalk (equal foundational priorities)

| Programme | What N-1/N-2 contribute | What is still open |
| --- | --- | --- |
| #1169 + #866 | A scoped **paper mathematical obstruction** to fixed-time and bounded passive-wait production of the original precursor using the unchanged ring-only update. A physical producer of coupled reservoir and executable writes remains UNSOURCED | A physically justified native enlarged apparatus, complete prep/controller/record mechanism, nonlocal pair source, common classical/quantum access and full selection |
| #1216 | A sharp **full-state** TV floor (255/256), and a separate scoped mathematical **declared controller-record** TV floor (3/4) for the one-tick unprepared loader | A uniform OI-derived Level-B correspondence for quantum tests, arbitrary finite-precision complete histories, soundness and composition; do not conflate the preparation-vs-target error with the quantum benchmark |
| #1220 | A clear split between ring-only passive evolution, supplied-source conditional classical sampler, and auxiliary-gate comparator; eight-bit output capacity and T-tick passive probability bound | Full physical and weak-classical-sampler ledgers for source/clean bits, clock, gates, preparer logs, failures, herald, renewal and all-horizon resource growth |
| #1143 / #868 | Existing classical register observations remain legitimate; the ring-only obstruction does not eliminate C0/C1 countermodels or derive Bell behaviour | Native Born rule, separated-wing quantum correlations, operational no-signalling, joint-state closure and no-superquantum selection remain separate |

**Priority recommendation:** do not write a larger abstract universal-gate factory yet. Use PREP-NATIVE-1 as a **scoped paper obstruction for the unchanged closed ring** and source only one physically motivated, actually executing enlarged-ring reservoir coupling before any positive physical-preparation claim. If no such mechanism is supported in the inspected sources, retain UNSOURCED rather than assume a low-entropy supply. Keep #1169 and #1216 at equal priority, and #945 finite-bit theorem repair inside its existing workstream.

# 7. Independent review and integration gates

**Independent reviewer: NOT ASSIGNED OR EXECUTED in this ChatGPT session.** The author checked source formulas and the set-counting/TV/union-bound algebra; this is **not independent ACCEPT**. No new CI result, empirical run or formal Lean proof is claimed.

Request a separate source/mathematics reviewer to check:

1. Source pin, exact precursor constraints and the eight distinct target coordinates for every L≥9 (including modulo-L aliases); |A_c|=2^(2L−4), |E_c|=2^(2L−12), η_c uniform and the existing F forward loading.

2. N-1's permutation-pushforward law and exact formula for TV, including equality at the one-tick correctly identified target F(E_c). Check not to mix target E_c with F(E_c).

3. N-2's union bound over a fixed target event and passive predetermined times, and its **failure** under state-changing interventions, resampling or unknown physical herald.

4. The declared A_1=c XOR(X_2 OR X_3) single-read TV=3/4, and the distinction between full-state information and genuine complete **accessible** histories.

5. PREP-8's separate conditional source/gate assumptions and matched eight-bit output-capacity statement; no claim that native F implements SWAP/controlled-XOR or even a physical clean auxiliary.

6. Existing accepted source stops in #866/CP-PREP-1, and clear attribution to the old support-counting lemma rather than a falsely novel physical theorem.

7. Resource accounting and whether initial canonical U_c, setting generator, reservoir, controller, complete logs, failures and renewal are actually produced rather than assumed.

Reviewer verdict must be one of ACCEPT, ACCEPT-WITH-NITS or REVISE for this **bounded mathematical paper only**; physical source stays NOT PASSED unless separately established. Publish to a repository branch/PR, designate F/E, dispatch native execution, adopt an enlarged physical interaction, promote the manuscript or merge **only under the existing separate approvals**. The Page and any associated GitHub Issue planning comments are not such approvals.