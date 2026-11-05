# ARROW-1 theorem-recovery note

**Status: WIP / UNVERIFIED.** Phase 1 of the #1112 correction round. Reviewed
independently twice, both reviews model-authored and both ACCEPT WITH CHANGES:
- at `bd398f05`: #1113 c.6649600806;
- at `37b39d1c` (delta review): #1113 c.6649698455.

This revision addresses both. Nothing in this note changes a manuscript statement or
promotes a result.

- **Base:** `f5c281ae10a913ec68fa41b3b839ad0b164979cd`. Every locator `File:line` is at
  this commit.
- **Authorization:** #1112 c.6649271094. No computation was run and no Lean module was
  built.
- **Support labels.** Each result below carries one of these labels:
  - **[K]** kernel-checked theorem, cited by identifier;
  - **[PP]** paper proof in the corpus;
  - **[EA]** exact algebra written out in this note;
  - **[HA]** hand argument in this note, not in the corpus;
  - **[AMB]** ambient FLRW/GR background calculation, not a native OI derivation;
  - **[LIT]** literature read first-hand (exact arXiv version given);
  - **[LIT2]** literature known only second-hand.

  Literature never establishes that a result follows from OI.
- **Purpose.** The rule is "theorem recovery before concession" (AGENTS.md, Code Review
  Rules). For each unproved claim, this note:
  - identifies the strongest existing result;
  - states what a proof would have to establish;
  - attempts recovery inside the corpus;
  - records the exact gap.

  Failure to recover a proof is not disproof. "Refuted" is used only where a counterexample
  is exhibited.

## Summary

| # | Claim (short) | Verdict |
|---|---|---|
| A1 | Horizon clock is monotone along observer worldlines | **Area: proved [EA, AMB]** as ambient FLRW kinematics, given an expanding background with the null energy condition (NEC).<br>• **Apparent horizon** (conditions on the interval considered): non-decreasing; strict iff ρ + p/c² > 0; constant in exact de Sitter.<br>• **Event horizon** (flat; conditions on all of [t, ∞)): non-decreasing; Ṙ_e(t) > 0 iff H is non-constant on [t, ∞); constant iff exact de Sitter on [t, ∞).<br>Reading the area as *entropy* along a dynamical horizon is **open** (GR:56). "Monotonic for as long as ä > 0" is **refuted as a general kinematic criterion** (phantom, NEC-violating), and **false as strict increase in exact de Sitter**. In the corpus's NEC-respecting background, ä > 0 is not the operative condition (§E.4). |
| A2 | Cosmological arrow | **Conditional.** The direction of A1 is the sign of H, which is an input. Why the expanding branch is the one realized: **open.** |
| A3 | Thermodynamic arrow descends from ρ_s = ρ_crit | **Open.** The cited identity is instantaneous and concerns the boundary entropy only; it does not reach the step. The physical direction of entropy increase is **conditional on asymmetric boundary data**. |
| A4 | Generalized second law; "non-decreasing from a product initial state" | GSL **open** (as GR:805 states). Theorem A.6 is **proved [PP]** as a two-sided bound relative to t = 0. Its monotone reading at GR:607 is **refuted** (two-qubit counterexample, §C.4). |
| A5 | Memory arrow aligns with the clock | Direction: **conditional** on a non-stationary preparation and the orientation convention. Alignment with the clock: **open.** |
| A6 | Measurement arrow | Inherits A5: **conditional** / **open**. |
| A7 | Alignment ("all other arrows align", "every arrow … descends", "four aligned arrows") | **Open — unresolved, not refuted.** Alignment is T-even, and none of the obstructions forbids it (§C.6). No common mechanism is proved; the gap is stated in §B.7. |
| A8 | "The framework derives the arrow" / "resolves the arrow-of-time question" / closes the Ellis objection | **Not supported as stated.** What is derived reduces to A1 (conditional, ambient) plus A9 (symmetric). The rest is open. Only the reading "a globally monotone state function of (S, φ)" is excluded (§C.1). |
| A9 | Observer-selection rule (Main §4.6) | **Proved [PP]**, conditional on (EM), the rate condition, bounded diameter and canonical typicality, in the iterated-channel description. **Time-symmetric** (§C.3). It supplies no direction and no low-entropy boundary. |
| A10 | "The arrow's single open dependency is the ordering question and nothing further" | **Refuted as stated.** The section's own chain uses further inputs (§B.10). |
| A11 | "The asymmetry is introduced by the trace-out" (ch18:202) | **Refuted in its unconditional reading** (§C.3, §C.5). Under the invariant measure the traced-out process carries no entropy or memory asymmetry. |

The owner's expectation was "unresolved rather than refuted" for alignment. That holds:
no counterexample to alignment exists, and §C.6 explains why none of the obstructions
yields one. The refutations in the table concern narrower statements, each for the class actually
ruled out:
- the ä > 0 criterion, as a general kinematic criterion, and as strict increase in exact
  de Sitter;
- the monotone reading of Theorem A.6;
- the two unconditional inventory and trace-out sentences.

***

## A. The claims, quoted at `f5c281ae`

**A1 — monotone horizon clock.** Substratum:405:
> The framework's primary arrow is the cosmological horizon entropy
> $S_{\rm dS}(t) = A(t)/(4 l_p^2)$, monotonically increasing along any observer worldline in
> the $\Lambda$-dominated phase. … every observer in the accelerating phase agrees that
> $S_{\rm dS}$ increases … The horizon clock is observer-independent, continuous, and
> monotonic for as long as $\ddot a > 0$ …

Also at:
- Substratum:409: "The framework therefore derives the existence of a monotonic parameter along observer worldlines";
- ch02:192–194;
- Methodology:184.

**A2 — cosmological arrow.** Substratum:407:
> *Cosmological:* $S_{\rm dS}(t)$ monotonic in the $\Lambda$-dominated phase, as above.

Also Substratum:379: "time translation is broken intrinsically by the growth of the horizon".

**A3 — thermodynamic step.** Substratum:407:
> *Thermodynamic:* via Jacobson's coupling $\rho_s = \rho_{\rm crit}$ ([GR, §3]), the
> entropy of any horizon-bounded system increases with the observer's clock — the
> thermodynamic arrow descends from the structural arrow without an independent postulate.

ch02:194: "The thermodynamic arrow descends from Jacobson's coupling between boundary
entropy and matter entropy."

**A4 — generalized second law.** GR:607:
> Unitarity of $\varphi$ and subadditivity make the sum of the von Neumann entropies of $V$,
> $B$ and $D$ non-decreasing from a product initial state (Theorem A.6).

GR:805: "**The generalized second law is open.**"

**A5 — memory step.** Substratum:407:
> *Memory:* C2 (memory persistence) implies the observer's hidden sector preserves
> correlations forward along the clock rather than backward, because the coarse-grained
> mixing time of the hidden-sector dynamics is uniform in the two directions but the
> observer's measurement protocol commits to one.

**A6 — measurement step.** Substratum:407:
> *Measurement:* the observer records "past" outcomes and prepares "future" states — an
> asymmetry inherited from the memory layer, not added on top of it.

**A7 — alignment.**
- Substratum:401: "every arrow the observer sees descends from this confinement together with the horizon growth that the accelerating phase produces".
- Substratum:405: "At the observer level, the horizon clock picks out a direction, and all other arrows align with it."
- Substratum:407: "Four derived arrows align with the horizon clock through a structural cascade."
- ch02:196: "it derives a monotonic parameter along observer worldlines and four aligned arrows of time".
- ch18:216: "The alignment of the thermodynamic and cosmological arrows is structural rather than coincidental. Both arrows trace to the same initial conditions of the cosmological partition."

**A8 — "derived" headlines.**
- Substratum:403: "The framework derives the arrow; it posits the existence of the domain."
- Substratum:26: "a third projection (§5.4) that resolves the arrow-of-time question …, answering the Ellis objection".
- Substratum:14: "joined by a third projection that produces the arrow of time".
- Substratum:415: "The layered cascade closes the Ellis-axis objection for the arrow of time".
- Methodology:184: "The arrow is derived, not posited … No third temporal axiom is required, and none is concealed."
- Explainer:930: "You don't need to posit low initial entropy to explain why we see it".
- ch03:58: "The framework's account of the arrow of time, developed in Chapter 2 §2.6, follows from this exclusion".

**A9 — selection.**
- Main:744: "The rule replaces a postulate often imported from elsewhere — the 'past hypothesis' of low initial entropy, in its role of selecting observer-compatible configurations — with a theorem conditional on the effective-mixing hypothesis (EM)".
- Main:758, titled "**Corollary (past-hypothesis replacement, with its rate condition).**", ends: "The low-entropy initial condition commonly imported as a 'past hypothesis' to select observer-compatible configurations is replaced here, within that description, by a structural selection rule".

**A10 — inventory.** Substratum:413: "so the arrow's single open dependency is the ordering
question and nothing further."

**A11 — trace-out.** ch18:202: "The asymmetry is introduced by the trace-out — the
marginalization over the hidden sector that produces the embedded observer's reduced
description."

***

## B. Per claim: strongest result, target, closest results, gap, route

### B.1 Monotone horizon clock (A1)

- **Strongest existing result.** The corpus does not prove it. GR:56 names the two horizons:
  - the event horizon, $R_{\rm event} = a(t)\int_t^\infty c\,dt'/a(t')$;
  - the apparent/Hubble horizon, $R_A = c/H$, $A = 4\pi c^2/H^2$.

  GR:56 also states that they coincide only in exact de Sitter. No corpus document computes
  $dA/dt$. The Lean grep in c.6643840329, re-checked here, finds no horizon-monotonicity
  theorem.
- **Target statement (T1).** Let the background be an FLRW metric obeying the Friedmann
  equations with total density ρ and pressure p (Λ included as a component).
  - **(T1a) Apparent horizon, any curvature.** If $H > 0$ and $\rho + p/c^2 \ge 0$ on an
    interval $I$, then on $I$ the apparent-horizon area is non-decreasing. It is strictly
    increasing where $\rho + p/c^2 > 0$, and constant where $\rho + p/c^2 \equiv 0$ (exact
    de Sitter).
  - **(T1b) Event horizon, flat.** The event horizon at $t$ depends on the whole future
    $[t,\infty)$. A later phantom phase toward a big rip gives $R_e \to 0$, and so
    $\dot R_e < 0$ on $I$ can occur whatever holds on a bounded interval $I$. The
    hypotheses are therefore imposed on all of $[t,\infty)$; this is sufficient, not
    necessary. If the event horizon exists, $H > 0$ and $\dot H \le 0$ on $[t,\infty)$
    (NEC, flat), then $\dot R_e(t) \ge 0$. Equality holds iff H is constant on
    $[t,\infty)$. So $\dot R_e(t) > 0$ iff H is non-constant on $[t,\infty)$. That is not
    the apparent horizon's "strict iff $\rho+p/c^2>0$" condition: an exact de Sitter
    stretch followed by an NEC-respecting decrease of H gives $\dot R_e > 0$ during the
    stretch.
  - Phase 2 names the apparent horizon (F.2), so T1a is the statement Phase 2 relies on.
    T1b is recorded for completeness.
- **Proof.** §E [EA, AMB].
- **Gap.** None for T1 as stated. T1 is an ambient GR calculation: OI's covariant field
  equations are the open Level-G3 step (GR §8.7). T1 is therefore a statement about the
  background OI is applied to, not a derivation from (S, φ). Two further points:
  - Reading $A/(4l_p^2)$ along a *dynamical* FLRW horizon as the horizon's entropy goes
    beyond GR's calibration surface. GR:56 states that the dynamical (Kodama–Hayward)
    extension "is not established here".
  - So "the horizon entropy increases" is the area statement T1 plus an identification
    that is open.
- **Route.** Complete for the area (T1). The entropy reading is open.

### B.2 Cosmological arrow (A2)

- **Strongest existing result.** T1 orients A by the sign of H. Under $t \to -t$, H changes
  sign while $\dot H$, A and ρ + p do not, so $dA/dt$ is T-odd (§E.3). The horizon clock's
  direction is therefore *the direction of expansion*, re-expressed.
- **Inputs.** The expanding branch is taken as given:
  - Main:760 (iii): "The horizon's expansion sets $\tau_B \sim H^{-1}$";
  - ch04:30: "the cosmological initial conditions are taken as given";
  - Substratum:379: "The framework does not derive that structure". This is weak support:
    "that structure" there is the FRW symmetry pattern, not the expanding branch as such.
- **Target (T2).** A theorem from (S, φ), the partition and stated preparation data
  selecting $H > 0$ over $H < 0$ for the observer's accessible window.
- **Closest result.** None. Main §4.6 is symmetric (§C.3) and does not mention expansion.
- **Gap.** All of T2.
- **Route.** None inside the corpus. Under T-invariance the reversed history is the
  contracting branch, admissible on equal terms (§C.5). Any T2 needs boundary data or a
  measure that is not T-invariant.

### B.3 Thermodynamic step (A3)

- **Strongest existing results.**
  1. **$\rho_s = \rho_{\rm crit}$** [PP], GR §7.2 (GR:428–430), with its temperature input
     from GR §3.1. The identity is $\rho_s = 3c^2H^2/(8\pi G)$: an instantaneous equality,
     even in H. It concerns the *boundary* entropy's energy density, not the entropy of
     matter inside the horizon.
  2. **Theorem A.6** [PP]. See B.4 and §C.4.
  3. **The unital-channel remark at GR:805** [PP]. If the hidden state is maximally mixed,
     the marginal channel $\Phi_V$ is unital, so $S_{\rm matter}$ does not decrease *over
     that one channel application*. Composing steps needs the hidden state re-prepared
     maximally mixed at each step, which is a Markov assumption the exact dynamics does not
     supply (Main:760 (ii)).
  4. **The fast-bath erasure lemma** [PP], Main:165–167. In the iterated-channel
     description under uniform erosion, the readback gap decays as
     $\delta_0 e^{-(k-1)\tau_S/\tau_B}$. This is a statement about steps *away from a
     rooted record*, and applies in either direction (§C.3).
- **Target (T3, relational).** For a stated class of histories and a coarse-grained
  visible (matter) entropy $S_{\rm cg}$, on the observer's window,
  $\operatorname{sign}\dot S_{\rm cg} = \operatorname{sign}\dot A$. Explicit premises would
  include:
  - (P1) a non-stationary (low-entropy or product) preparation;
  - (P2) a *monotonicity* theorem for $S_{\rm cg}$ in the exact dynamics, not a bound, over
    the window;
  - (P3) a relation tying the entropy gradient to $\dot A$: either a common boundary for
    (P1) and the minimum of A, or an identity linking $S_{\rm cg}$ (or the hidden sectors'
    coarse-grained entropy) to A.
- **Closest results.**
  - (P1) is the hypothesis of Theorem A.6.
  - (P2) is supplied only in the iterated-channel description under (EM). Main:760 (ii)
    states that its governance of the exact compressions "is not established".
  - (P3) is the identification GR:805 names as missing: "a relation between horizon area
    and the hidden sectors' coarse-grained entropy along the evaporation".
- **Gap.** (P2) for the exact dynamics, and all of (P3). The cited identity (1) cannot
  supply (P3): it relates $\rho_s$ to H², not the matter entropy to A. The step as written
  ("via Jacobson's coupling … the entropy of any horizon-bounded system increases") has
  no derivation behind it.
- **Route inside the corpus.** Partial. The most direct candidate is capacity growth:
  - GR §5's boundary-mode count makes the hidden capacity scale with $A/\epsilon^2$;
  - Theorem A.6 already allows the sector grouping $V_t, B_t, D_t$ to change with t;
  - so a growing A enlarges the maximum coarse-grained entropy.

  This supplies room for entropy growth, not growth itself: it still needs (P1), (P2) and
  the GR:805 identification. The literature analogue (Layzer; Frautschi, "Entropy in an
  expanding universe") is **[LIT2]**, not read first-hand for this note.

### B.4 Generalized second law and Theorem A.6 (A4)

- **Strongest existing result. Theorem A.6** [PP], GR:799–803. For a product state at
  $t = 0$ evolving under $U_\varphi$, and for every $t$ and every regrouping:
  $\sum_X S(\rho_{X_t}(t)) \ge \sum_X S(\rho_X(0))$.
  - The proof (subadditivity, then unitarity) uses no sign of t.
  - $U_\varphi$ is invertible, so the bound holds for $t < 0$ as well.
  - It is a two-sided bound with its minimum at the preparation time.
- **Target (T4, GSL).** $S_{\rm matter}+S_{\rm BH}+S_{\rm dS}$ is non-decreasing along the
  observer's clock. Premises:
  - (P1) as above;
  - the GR:805 identification, $S_{\rm BH}(t) = S(\rho_{B_t}(t))$ and
    $S_{\rm dS}(t) = S(\rho_{D_t}(t))$, or a coarse-grained replacement;
  - a monotonicity theorem: Theorem A.6 bounds against $t=0$ only, and §C.4 shows it does
    not give monotonicity.
- **Closest.** Theorem A.6 and the unital-channel remark, both stated at GR:805 with their
  limits.
- **Gap.** Exactly as GR:805 states, plus monotonicity.
- **Route.** None inside the corpus. **GSL: open**, already stated correctly at GR:805 and
  ch07:155–157.
- **GR:607.** It reads "non-decreasing from a product initial state". That is refuted as a
  monotonicity statement by §C.4 and should state the bound.

### B.5 Memory step (A5)

- **Strongest existing results.** Main's realization and readback theorems are *rooted*:
  - the process dilation starts from $P_0 \otimes \mu_H$ at $t = 0$ (Main:518);
  - the recurrence/indivisibility theorem uses rooted maps $\Gamma_t$ with a shared hidden
    prior (Main:137);
  - the conditions (C2) and (C4) are phrased forward from a write to a readback (Main:76,
    :80).

  Each holds for every bijection φ. Since $\varphi^{-1}$ is also a bijection, each has a
  mirror statement for $t < 0$ from the same root (§C.3, *closure under inversion*).
- **Target (T5).** In the realization class used for the cosmological cut, records of the
  visible past are written and read back in the direction of increasing A. Premises:
  - a preparation (root) at $t_0$, the low-A end of the window;
  - persistence and readback forward from $t_0$;
  - a reason the root sits at the low-A end and not the high-A end.
- **Closest.** The rooted theorems give "away from the root", in both directions. The
  orientation of the protocol is a convention (Substratum:409; Methodology:184, "related by
  forward iteration of φ").
- **Gap.** The link between the root time and the horizon clock (the third premise of T5).
  The text's own mechanism ("the observer's measurement protocol commits to one") is the
  orientation convention.
- **Route.** None inside the corpus beyond the common-boundary form of §C.6 (β).

### B.6 Measurement step (A6)

The step inherits A5 by its own text. The record/prepare asymmetry is the memory
asymmetry under the protocol convention. Target, gap and route are those of B.5.

### B.7 Alignment: a common mechanism (A7)

- **Strongest existing result.** None proves alignment.
  - Substratum §5.4 asserts it.
  - ch18:216 attributes it to "the same initial conditions", that is, to boundary data
    posited at the same time. That supplies a common cause by stipulation, not a mechanism.
  - ch18:216 also asserts "C1–C4 hold at the cosmological boundary", against GR:52 ("(C4)
    … **Not presently discharged.**").
- **Target (T7, common alignment mechanism).** For a class $\mathcal C$ of tuples
  (finite bijection φ, partition family $V_t$, preparation), stated in advance, and for
  every history in $\mathcal C$ on the observer's accessible window $W$:
  $$\operatorname{sign}\dot A(t) = \operatorname{sign}\dot S_{\rm cg}(t) = \text{(direction of record formation)} = \text{(direction of preparation→registration)},\quad t\in W,$$
  derived from one property of the substratum and partition, not from four separate
  inputs. Explicit premises any proof would need:
  - (Q1) **A as a substratum quantity.** The horizon area, or a proxy, is a function of the
    substratum configuration and partition, so that "$\dot A$" is defined inside OI. At
    present A enters only through the ambient FLRW background (B.1).
  - (Q2) **Entropy–area relation.** An identity or inequality linking $S_{\rm cg}$, or the
    hidden sectors' coarse-grained entropy, to A: the GR:805 gap.
  - (Q3) **Exact monotonicity on W.** For $S_{\rm cg}$ under the exact compressions, not
    only the iterated channel: Main:760 (ii).
  - (Q4) **Record–entropy link.** Records form in the direction in which $S_{\rm cg}$
    increases. The corpus has the ingredients (erasure lemma, readback lemma), but only
    rooted and two-sided.
- **What the obstructions allow (§C.6).** T7 is a *relational*, T-even statement, and none
  of §C.1–§C.5 excludes it. They exclude only:
  - a global version (beyond a recurrence window);
  - a version that fixes the *direction* from (S, φ) alone.
- **Closest results.** Theorem A.6 (for Q3, but two-sided and a bound); `counting_passive`
  (orients energy given monotone Ω, not time); the boundary-mode count (for Q1/Q2, at the
  exact de Sitter calibration only).
- **Gap.** Q1–Q4, each unproved.
- **Route.** None found. The weak conditional statement available now is §C.6 (β): with a
  product preparation and the minimum of A at the same time, both quantities are bounded
  below by their values there. Its content is the posited coincidence. That is the ch18
  position, not a mechanism.
- **Verdict: open (unresolved).** No counterexample.

### B.8 "The framework derives the arrow" (A8)

- **What the text itself concedes.**
  - Substratum:409: the §4.6 content is symmetric; which direction is "future" is
    convention; "The framework therefore derives the existence of a monotonic parameter
    along observer worldlines, not a substrate-level arrow of time."
  - Substratum:413: the derivation is conditional on the ordering of moments.
- **What survives.**
  - A1 (conditional, ambient, constant in exact de Sitter);
  - A9 (symmetric selection);
  - the convention.
- **Not supported as stated.**
  - The arrow as a physical direction: A2, A3, A5, A6.
  - The arrow as a set of aligned arrows: A7.
  - "Resolves the arrow-of-time question" and "closes the Ellis-axis objection" rest on
    the cascade, which is open.
- **Excluded by §C.1.** Only one reading is excluded: a globally monotone function of the
  substratum state. Substratum:409 already agrees with that ("agreeing with the objection's
  premise").
- **Not checked.** The source of the "Ellis objection" is uncited in the corpus and was
  not checked.

### B.9 Observer-selection rule (A9)

- **Strongest existing result.** Main §4.6 theorem and corollaries [PP]. Conditional on:
  - (EM);
  - the rate condition $\tau_{\rm mix}\ll\tau_S$;
  - bounded coupling-graph diameter;
  - canonical typicality [31];
  - stated for the description generated by iterating $\mathcal K_\Sigma$ (Main:760 (ii)).

  No kernel counterpart: the coverage ledger grades it `GAP`.
- **Time symmetry.** By §C.3 the theorem holds verbatim for $\varphi^{-1}$, with the same
  gap.
- **What it does and does not do.**
  - It selects *where* (non-equilibrium regions).
  - It does not select *which way*.
  - It does not supply a low-entropy boundary. A selected non-equilibrium region of a
    reversible system is, absent past-boundary data, as likely to sit at a local entropy
    minimum as on a monotone slope: the Boltzmann/Loschmidt point, in c.6643691865.
- **Verdict.**
  - Retain as proved under its hypotheses.
  - The title "past-hypothesis replacement" attributes to it the replacement of a boundary
    condition. Its body scopes that replacement to the role "to select observer-compatible
    configurations". The title does not.

### B.10 Inventory (A10)

Substratum:413 states that "the arrow's single open dependency is the ordering question and
nothing further". The same section conditions its chain on further inputs:
- (EM) (Substratum:401, :407);
- the iterated-channel description (Substratum:401, :407, :409);
- the expanding branch ($H > 0$), implicit in "the $\Lambda$-dominated phase" and "the
  accelerating phase" (Substratum:405). The condition $\ddot a > 0$ named there does not
  itself imply $H > 0$.
- a measurement-protocol orientation (Substratum:407).

The thermodynamic step also needs (P1)–(P3) of B.3. Each of these is a dependency other
than the ordering, so the sentence is false as stated: **refuted** by exhibition. The fix
is a complete list, not a proof.

***

## C. Obstructions that bound any recovery

Each is stated as a constraint on what a recovery can deliver, not as a refutation of
alignment.

### C.1 Reversibility with finite recurrence: no globally monotone state function [EA]

Let φ be a bijection of the finite set S, so $\varphi^N = \mathrm{id}$ for some N
(Main:123, Step 1). Suppose $F: S \to \mathbb R$ satisfies $F(\varphi s) \ge F(s)$ for all
s. Summing $F(\varphi s) - F(s) \ge 0$ around each cycle gives 0, so every term vanishes,
and $F\circ\varphi = F$.

The same holds for any functional of the evolving distribution:
- $p_t = p_0\circ\varphi^{-t}$ is N-periodic;
- so is every coarse-grained entropy $S_{\rm cg}(p_t)$;
- so are the sector entropies of Theorem A.6.

**Consequence.** Any monotonicity is confined to a window shorter than the recurrence time
and anchored by data on that window. Main §2.3's own theorem exhibits this: the one-step
distinguishability contracts, $d(\delta_iT,\delta_jT) < 1$, and returns to 1 at $t = N$
(Main:125–129).

### C.2 Rooted results are closed under inversion [HA]

Main's realization, readback and indivisibility results, and Theorem A.6:
- quantify over all bijections φ of a finite set;
- start from a preparation at a root time, $P_0\otimes\mu_H$ or a product state.

$\varphi^{-1}$ is a bijection of the same set, so each result applies to the process run
backward from the same root. For the existence theorem at Main:518, this means the class of
laws realizable from a root is the same for backward runs. For the bound results
(Main:137, Theorem A.6), the conclusion holds for $t < 0$. Their conclusions describe
evolution *away from the root* in both directions.

**The abstract step is kernel-checked [K].** `no_universal_oriented_property`
(`verification/lean-mathlib/OIBridge/OrientationClosure.lean`:249) states:
- let a class C be closed under a map Θ and inhabited;
- let a property P satisfy $P(R) \Rightarrow \neg P(\Theta R)$ on C;
- then P cannot hold throughout C.

The instantiation by hand [HA]:
- Θ is $\varphi\mapsto\varphi^{-1}$ (with the same root);
- C is a hypothesis class closed under inversion;
- P is "the conclusion points toward $t > 0$ and not toward $t < 0$".

A one-sided arrow therefore cannot come from these results without one of:
- a hypothesis not closed under $\varphi\mapsto\varphi^{-1}$;
- a second boundary.

### C.3 Stationarity: block entropies and $M_k$ are reversal-invariant; §4.6 is symmetric [HA]

Take the canonical measure μ of Main Lemma 3 (uniform, φ-invariant) on
$S = \mathcal C_V\times\mathcal C_H$, and $X_t = \pi_V\varphi^t(s)$ with $s\sim\mu$,
$t\in\mathbb Z$.

1. **Stationarity.** $\mu\circ\varphi^{-1} = \mu$, so $(X_{t+m})_t$ has the law of
   $(X_t)_t$, and the block entropy $H_n := H(X_t,\dots,X_{t+n-1})$ does not depend on t.
2. **Reversal invariance of $M_k$.** Main defines
   $M_k := I(X_{<k};X_{k+1}\mid X_k)$ (Main:471). By the chain rule,
   $$M_k = H(X_0..X_k) + H(X_k,X_{k+1}) - H(X_k) - H(X_0..X_{k+1}) = H_{k+1}+H_2-H_1-H_{k+2}.$$
   For the reversed process $Y_t = X_{-t}$, the same four blocks appear, shifted, so
   $M_k^{\rm rev} = M_k$. Every block-entropy functional is reversal-invariant, including
   excess entropy and entropy rate.
3. **Consequence for (C4) and (C2).** Under the invariant measure, (C4) holds forward at an
   order exactly when it holds backward, as measured by $M_k>0$. The condition then
   distinguishes no direction.
4. **Main §4.6 is symmetric, under two stated assumptions.**
   - **Assumption (P_Σ).** Main:746 does not define $P_\Sigma$. Read it as the
     μ-orthogonal conditional expectation onto the coarse observables of Σ, self-adjoint on
     $L^2(\mu)$. Main's own examples (Main:760 (ii)) fit this reading.
     - With it, the compression for $\varphi^{-1}$ is
       $P_\Sigma\mathcal U_\varphi^{\dagger}P_\Sigma = \mathcal K_\Sigma^{\dagger}$.
     - Its spectrum is the complex conjugate of $\mathcal K_\Sigma$'s, with the same moduli.
     - With Π the projection onto the invariant part,
       $\|(\mathcal K_\Sigma^\dagger)^n-\Pi\| = \|(\mathcal K_\Sigma^n-\Pi)^\dagger\| = \|\mathcal K_\Sigma^n-\Pi\|$,
       so the gap and $\tau_{\rm mix}$ are the same, in the spectral/$L^2$ reading of
       $\tau_{\rm mix}$.
   - **Assumption (bounded range of $\varphi^{-1}$).** The proof uses φ's causal cone
     (Main:754, :364), so the φ⁻¹ version needs $\varphi^{-1}$ to have bounded per-step
     range. A local bijection's inverse need not be local: $x_i \mapsto x_i + x_{i+1}$
     mod 3 on an odd ring has a dense inverse. The assumption holds under the corpus's
     T-invariance posit with a site-local T, where $\varphi^{-1} = \mathcal T\varphi\mathcal T$.
     That is the case of the second-order wave update of SM Theorem 17 (kernel:
     `wave_time_reversal_invariant`, `verification/lean/OI_Time_Reversal.lean`), whose time
     reversal swaps the two time layers site by site.
   - Under both assumptions, (EM) holds for φ exactly when it holds for $\varphi^{-1}$, and
     the theorem and both corollaries hold verbatim for $\varphi^{-1}$. Substratum:409
     already says the bound "applies equally in both directions"; this is the reason.
   - Items 1–3 need neither assumption.

A stationary process need not be reversible in law. A 3-cycle on visible states has
$P(0\to1)\ne P(1\to0)$. That asymmetry is a chirality of φ, not an entropy or memory
gradient: items 1–3 still hold. Under the corpus's T-invariance posit it disappears up to
relabeling (§C.5).

### C.4 Theorem A.6 is two-sided, and its monotone reading fails [EA, counterexample]

**Two-sidedness.** By C.2, the bound $\Sigma(t)\ge\Sigma(0)$ holds for $t<0$ too. The
preparation time is a global minimum of the bound, not the start of a monotone increase.

**Counterexample to "non-decreasing" (GR:607).** Take:
- $V$ and $B$ one bit each, $D$ trivial;
- $\varphi(v,b) = (v\oplus b, b)$, a permutation of $\{0,1\}^2$ (CNOT, an involution);
- the product initial state $\delta_{v=0}\otimes\mathrm{unif}_b$, diagonal, so all
  entropies are Shannon entropies.

Then:

| t | joint state | $S_V$ | $S_B$ | $\Sigma(t)$ |
|---|---|---|---|---|
| 0 | uniform on $\{(0,0),(0,1)\}$ | 0 | ln 2 | ln 2 |
| 1 | uniform on $\{(0,0),(1,1)\}$ | ln 2 | ln 2 | 2 ln 2 |
| 2 | $\varphi^2 = \mathrm{id}$: as at t = 0 | 0 | ln 2 | ln 2 |

- Theorem A.6's hypotheses hold and its conclusion $\Sigma(t)\ge\ln 2$ holds.
- $\Sigma(2) < \Sigma(1)$, so the sum is not non-decreasing for $t>0$.
- The same pattern recurs for every φ that correlates the sectors at some t (C.1).

This is a counterexample to the monotone reading only. Theorem A.6 itself is correct.

### C.5 T-invariance: the reversed visible process is the relabeled forward process [HA]

Assume the corpus's posits:
- an involution $\mathcal T$ with $\varphi = \mathcal T\varphi^{-1}\mathcal T$ (ch06:62;
  SM Theorem 19);
- $\mathcal T$ preserves the partition, acting as θ on visible states;
- the counting (uniform) measure.

Then for every n and every history $(i_0,\dots,i_n)$:
$$P(X_0=i_0,\dots,X_n=i_n) = P(X_0=\theta i_n,\dots,X_n=\theta i_0).$$

*Proof.*
1. $s\mapsto s' := \mathcal T\varphi^n s$ is a μ-preserving bijection.
2. $\varphi\mathcal T = \mathcal T\varphi^{-1}$ gives $\varphi^k s' = \mathcal T\varphi^{n-k}s$.
3. Its visible part is $\theta\,\pi_V\varphi^{n-k}s$.

This extends SM Theorem 19 from two-time counts to histories. It is a hand argument in
this note, not a corpus result; a reviewer should check it.

**Consequence.** Under the invariant measure the trace-out produces a process whose time
reversal is its θ-image. The trace-out alone introduces no asymmetry. That refutes the
unconditional reading of ch18:202. ch18:210's conditional reading (initial conditions)
stands.

**Witness: memory without an arrow [EA].** Take $\mathcal C_V = \mathcal C_H = \{0,1\}$,
$\varphi(v,h) = (h,v)$ and the uniform prior.
- The visible process is $(a,b,a,b,\dots)$ with $a, b$ independent and uniform.
- Its law is reversal-symmetric.
- $M_1 = I(X_0;X_2\mid X_1) = 1$ bit, since $X_2 = X_0$.

So history readback ((C4) at order 1) holds at full strength with no time asymmetry.

**Alignment is unaffected.** This assumes, as standard, that the horizon area A and the
coarse-grained entropy $S_{\rm cg}$ are T-even: T leaves the value at each instant fixed
and reverses the order of instants. Then $\mathcal T$ maps an expanding history in which
entropy increases to a contracting history in which entropy decreases. Both are *aligned*.
The T-image of an aligned history is aligned.

### C.6 What alignment can still mean

The obstructions constrain direction, globality and stationarity. Alignment survives them
in four senses.

- **(α) Relational alignment (T-even).**
  - The statement $\operatorname{sign}\dot S_{\rm cg} = \operatorname{sign}\dot A$ is
    invariant under $t\to-t$, because both sides flip.
  - Neither C.1 nor C.3 nor C.5 excludes it. For example, an identity
    $S_{\rm cg} = f(A)$ with f increasing would give it under any measure.
  - Recovering alignment means proving T7 (B.7): premises Q1–Q4. The direction would then
    still come from boundary data or convention.
- **(β) Conditional alignment from a common boundary [EA, weak].**
  - Take a product state at $t_0$ (Theorem A.6), with $A(t_0)$ the minimum of A on the
    window. Then $\Sigma(t)\ge\Sigma(t_0)$ and $A(t)\ge A(t_0)$ for all t on the window.
  - The statement is true and trivial. Its content is the posited coincidence of the two
    boundary data, which is ch18:216's "same initial conditions".
  - A non-trivial version needs Q3 (monotonicity) and a reason for the coincidence (Q2).
- **(γ) Windowed alignment.** On finite S any alignment holds at most on windows shorter
  than the recurrence time (C.1).
- **(δ) Direction.** The direction never comes from (S, φ) alone (C.1, C.3). It comes from
  boundary data (a preparation, the expanding branch) or from convention.

***

## D. Verdicts

| Claim | Verdict | Precise content |
|---|---|---|
| A1 clock (area) | **proved** (ambient) | **T1a** (apparent horizon): FLRW + Friedmann, with $H>0$ and $\rho+p/c^2\ge0$ on the interval; non-decreasing, strict iff $\rho+p/c^2>0$, constant in exact de Sitter.<br>**T1b** (event horizon, flat): with the conditions on all of $[t,\infty)$, non-decreasing; $\dot R_e(t)>0$ iff H is non-constant on $[t,\infty)$; constant iff exact de Sitter on $[t,\infty)$.<br>Entropy reading: **open** (GR:56).<br>The ä > 0 criterion is **refuted as a general kinematic criterion** (phantom, NEC-violating) and **false as strict increase in exact de Sitter**. In the corpus's NEC-respecting background, ä > 0 is not the operative condition (§E.4). |
| A2 cosmological | **conditional** | On the expanding branch, an input. Why that branch: **open**. |
| A3 thermodynamic | **open** | Gap: (P2) exact monotonicity and (P3) the entropy–area relation. Direction: conditional on asymmetric boundary data. The cited ρ_s = ρ_crit does not reach the step. |
| A4 GSL | **open** | Gap as at GR:805, plus monotonicity. |
| A4 Theorem A.6 | **proved** [PP] | Two-sided bound relative to t = 0. Monotone reading (GR:607) **refuted** by §C.4. |
| A5 memory | **conditional** (direction) / **open** (alignment) | Direction from a non-stationary preparation and the orientation convention. Alignment gap: the link between root time and the horizon clock. |
| A6 measurement | as A5 | — |
| A7 alignment | **open (unresolved)** | Not refuted. Target T7, premises Q1–Q4 open. Weak conditional form (β) only. |
| A8 "derives the arrow" | **not supported as stated** | Reduces to A1 + A9 + convention. The global reading is excluded (§C.1). |
| A9 selection | **proved** [PP], conditional | Hypotheses as at Main:744–760; time-symmetric; no direction; no low-entropy boundary. |
| A10 inventory | **refuted as stated** | Further dependencies exhibited (B.10). |
| A11 trace-out | **refuted** (unconditional reading) | §C.3, §C.5. The conditional reading (ch18:210) stands. |

***

## E. Horizon kinematics

These are ambient GR computations [AMB], written out as exact algebra [EA]:
- c is kept explicit in the flat case;
- c = 1 is used for general curvature;
- ρ is mass density and p pressure, with Λ included as a component ($p_\Lambda = -\rho_\Lambda c^2$).

### E.1 Which horizon

The corpus defines the horizon causally as the **event horizon** (GR:56), but computes with
the **apparent/Hubble horizon**, area $A = 4\pi c^2/H^2$ (GR:56; Substratum:405's
$S_{\rm dS}=A/4l_p^2$). They coincide only in exact de Sitter. Phase 2 text must name the
one it uses. Below, both are treated.

Equations used:
- From Cai & Kim, arXiv:hep-th/0501055v1, read first-hand **[LIT]**, with n = 3 and c = 1:
  - $\dot H - k/a^2 = -4\pi G(\rho+p)$ (eq. 2.14);
  - $\tilde r_A = (H^2+k/a^2)^{-1/2}$ (eq. 2.3);
  - the event horizon (eq. 2.4);
  - $\dot{\tilde r}_A = -H\tilde r_A^3(\dot H - k/a^2)$ (eq. 2.15).
- Standard, not from Cai & Kim: the acceleration equation
  $\ddot a/a = -\tfrac{4\pi G}{3}(\rho+3p)$.

### E.2 Apparent horizon

- **General curvature (c = 1).** From the two displayed relations,
  $$\dot{\tilde r}_A = 4\pi G\,H\,\tilde r_A^{\,3}\,(\rho+p),\qquad \frac{dA}{dt} = 8\pi\tilde r_A\dot{\tilde r}_A = 32\pi^2G\,H\,\tilde r_A^{\,4}(\rho+p).$$
- **Flat (k = 0), c explicit.** Here $R_A = c/H$ and $A = 4\pi c^2/H^2$, so
  $$\frac{dA}{dt} = -\frac{8\pi c^2\dot H}{H^3},\qquad \dot H = -4\pi G\Big(\rho+\frac{p}{c^2}\Big)\ \Rightarrow\ \frac{dA}{dt} = \frac{32\pi^2Gc^2}{H^3}\Big(\rho+\frac{p}{c^2}\Big).$$

**Role of each condition.**
- **The sign is $\operatorname{sign}(H)\cdot\operatorname{sign}(\rho+p/c^2)$.**
- **Given H, the NEC ($\rho+p/c^2\ge0$) fixes the sign.**
  - With $H>0$ the area is non-decreasing.
  - On the contracting branch ($H<0$) it is non-increasing.
  - In the equality case $\rho+p/c^2\equiv0$ (exact de Sitter) it is constant on either
    branch.
- **Strict growth** on the expanding branch holds iff $\rho+p/c^2>0$.
- **In ΛCDM** today, $\rho+p/c^2 = \rho_m + \tfrac43\rho_r > 0$, so A grows strictly. It
  approaches the de Sitter value asymptotically, as $\rho_m\to0$.

### E.3 Event horizon (flat)

$R_e(t) = a(t)\int_t^\infty c\,dt'/a(t')$, which exists iff the integral converges. Then:
- $\dot R_e = HR_e - c$.
- If $H>0$ and $\dot H\le0$ on $[t,\infty)$ (flat with NEC), then $H(t')\le H(t)$ for
  $t'\ge t$. So $a(t)/a(t')\ge e^{-H(t)(t'-t)}$, hence $R_e\ge c/H$ and $\dot R_e\ge0$.
- Equality holds iff H is constant on $[t,\infty)$: exact de Sitter from t on.

**The event horizon is defined by the future boundary $t\to\infty$.** Its time reverse is
the particle horizon $R_p(t) = a(t)\int_{t_i}^t c\,dt'/a(t')$, defined by the past boundary.
Choosing the event horizon (GR:56) therefore already fixes which end of time is the
reference. Under $t\to-t$ they exchange: H flips sign, while $\dot H$, A and $\rho+p$ do
not. So $dA/dt$ is T-odd, and the clock's direction is the direction of expansion.

### E.4 Exact de Sitter, and why ä > 0 is the wrong criterion

**Exact de Sitter.** $\rho+p/c^2 = 0$, so $\dot H = 0$ and $R_A = R_e = c/H$ are constant
(also Cai & Kim, below their eq. (2.4)). The horizon clock **stops** on GR's own
calibration surface (GR:56).

**The criteria compared.** $\ddot a>0 \iff \rho+3p/c^2<0$, whereas area growth (with
$H>0$) $\iff \rho+p/c^2>0$. Single-fluid flat solutions with
$w = p/(\rho c^2)$ constant give:

| Regime | ä | $dA/dt$ | Shows |
|---|---|---|---|
| matter/radiation ($w = 0, \tfrac13$) | $<0$ | $>0$ | ä > 0 is **not necessary** |
| quintessence ($-1<w<-\tfrac13$) | $>0$ | $>0$ | — |
| exact Λ ($w=-1$) | $>0$ | $=0$ | ä > 0 does **not give increase** |
| phantom ($w<-1$; $a\propto(-t)^{2/(3(1+w))}$, $t<0$) | $>0$ | $<0$ | ä > 0 is **not sufficient** (NEC violated) |

In the phantom row, $H = 2/(3(1+w)t) > 0$ and $\dot H = -2/(3(1+w)t^2) > 0$, so A shrinks
while $\ddot a/a = \dot H + H^2 > 0$.

**The correct criterion is "$H>0$ and the NEC".** It gives non-decreasing A, strict where
$\rho+p/c^2>0$, and constant in exact de Sitter.

**Scope of the verdict on ä > 0.** The verdict covers only the class each row rules out.
Substratum:405 says "monotonic for as long as $\ddot a>0$" and "every observer in the
accelerating phase agrees that $S_{\rm dS}$ increases".
- **As a general kinematic criterion it is refuted** by the phantom row. That row violates
  the NEC.
- **As strict increase it is false in exact de Sitter**: ä > 0 there, and A is constant.
  Exact de Sitter is GR's own calibration surface.
- **Inside the corpus's background it is weakly true but not operative.** That background
  respects the NEC, and GR excludes phantom crossing, conditionally (GR:12, :358, :553).
  There, ä > 0 with H > 0 gives $dA/dt\ge0$, so the statement holds weakly. ä > 0 is still
  not the operative condition: growth is governed by $H>0$ and $\rho+p/c^2>0$, and the
  criterion omits the decelerating era, in which A also grows.
- The "not necessary" row shows the criterion is incomplete. It does not refute a
  sufficiency claim.

***

## F. Wording principles for Phase 2

General rules:
- Minimum change (§A.25).
- Remove an assertion rather than tag it (§A.30).
- No self-narration of revisions (§A.27, §A.30, §A.33). Substratum:401's "Before §4.6 … With
  §4.6 in place" goes.
- Neutral register in `papers/` (§A.32). The book keeps its essay register but not a
  stronger status.
- Every book edit is mirrored in FULL.

### F.1 Retain

- Keep a derived or proved claim only with its hypotheses stated where it is proved.
- The selection theorem is described as selecting *where* observers can exist, in the
  iterated-channel description under (EM) and the rate condition. It is never described as
  selecting a time direction or supplying a low-entropy boundary.
- Theorem A.6 and "the generalized second law is open" stay as written at GR:797–805.

### F.2 Conditional

Name every input in the sentence that uses it:
- **The background.** "An expanding FLRW background ($H>0$) satisfying the null energy
  condition", as an input, not derived.
- **The horizon.** Name it: "the apparent (Hubble) horizon, $A = 4\pi c^2/H^2$".
- **The clock.** Replace "monotonic / monotonically increasing" with "non-decreasing,
  strictly increasing while $\rho+p/c^2>0$, constant in exact de Sitter". Drop the
  "$\ddot a>0$" and "accelerating phase" criteria (§E.4).
- **The thermodynamic direction.** Conditional on a low-entropy or product preparation;
  the horizon-area/entropy identification is open.
- **Memory and measurement.** Conditional on a non-stationary preparation and the
  orientation convention.
- **GR:607.** State the bound: "bounded below by its value at a product initial state, at
  every t". GR:797's "non-decreasing" defines the generalized second law and is followed by
  "supplies the following inequality toward it". It is a correct definition, not an
  overstatement (delta review c.6649698455, item D), and stays unchanged.
- **Substratum:407's thermodynamic step.** Drop the universal "the entropy of any
  horizon-bounded system increases with the observer's clock". No result supports it (B.3).
- **GR:214.** "monotone bath count ⇒ passive (energy orientation)", not a time direction.

### F.3 Unresolved

- State declaratively, where the cascade is stated, that the alignment of the
  thermodynamic, memory and measurement arrows with the horizon parameter is not
  established. Do not call it refuted or impossible.
- Remove the arrow-as-derived claims from the headline sentences (Substratum:14, 26, 403,
  415; Methodology:184 "none is concealed"; Explainer:930's sentence; ch03:58), rather than
  qualifying them in place.
- Where the "three projections" framing lists the arrow, narrow the item to what is
  established: the symmetric selection rule and, on the expanding branch, a non-decreasing
  horizon parameter. Do not delete the framing wholesale.
- Substratum:413: list the dependencies (B.10) in place of "nothing further".

### F.4 Main:758 retitle, and Main's upstream independence

- **The retitle (owner-approved).** "**Corollary (past-hypothesis replacement, with its rate
  condition).**" becomes "**Corollary (observer-selection rule, with its rate
  condition).**".
  - The statement and hypotheses are unchanged.
  - The retitle removes an attribution and adds no claim, citation or premise, so it
    creates no dependence of Main on downstream content.
  - The body's last sentence is already scoped ("to select observer-compatible
    configurations … within that description"). The authorization covers the title and
    :760 only, so the body stays.
- **Necessary consequences of the retitle**, authorized by the owner ruling #1112
  c.6649643759 (amaybaum, 2026-11-05):
  1. **Main:744.** It refers to "the rate condition $\tau_{\rm mix}\ll\tau_S$ stated in the
     past-hypothesis corollary". After the retitle that label dangles. The minimal fix
     changes the label phrase only.
  2. **`verification/coverage/LEDGER.json`.** `tools/proof_census.py` builds a statement's
     identifier from its parenthetical label. The entry
     `MAIN:C-past-hypothesis-replacement-rate-condition` would no longer match, and
     `tools/coverage_check.py` (release gate) would fail. The entry has to be renamed to
     the new identifier, with its fingerprint updated, in the same commit. The ledger is
     mutable, not a frozen record.
- **Main:760 (iii): NO CHANGE**, by owner ruling c.6649643759 item 4 ("Record NO CHANGE
  unless a concrete defect is identified and reviewed").
  - **Earlier recommendation, now ruled.** The sentence reads "The horizon's expansion
  sets $\tau_B \sim H^{-1}$ structurally, not thermally". It makes:
  - no monotonicity claim;
  - no time-direction claim;
  - no low-entropy claim.

  It describes the cosmological realization, which Main states is developed in companion
  work and consumed by no proof in Main (Main:72). This note finds no ARROW-1 defect in it.
  If the owner or a reviewer wants the expanding branch named there, the only admissible
  form names it as an observed input, without importing §E or citing GR or Substratum, so
  that Main stays independent of downstream results (Code Review Rules).
- **Authorized scope** (c.6649643759 item 1):
  - the Main:744 label phrase only;
  - in LEDGER.json, the `id`, `label` and `fingerprint` fields only, with `kernel: GAP`
    and the assumptions unchanged. The new identifier is
    `MAIN:C-observer-selection-rule-rate-condition`.
- **ch18:190 (c.6649643759 item 2).** Correct the unconditional unidirectionality claim
  (§C.1), without asserting that observer experience must reverse during recurrence.

***

## Literature

**Read first-hand [LIT]:**
- R. M. Wald, "The Arrow of Time and the Initial Conditions of the Universe",
  **arXiv:gr-qc/0507094v1** (21 Jul 2005). Its argument: a present thermodynamic arrow
  requires a very special early state, and Wald argues that a dynamical origin of that
  state is not plausible. Its footnote 1 describes Carroll–Chen as giving a *locally*
  observed arrow in a universe time-symmetric on large scales, with inflation and
  "deflation" episodes on equal footing. This parallels C.2/C.6 (δ). It supports nothing
  about OI.
- R.-G. Cai and S. P. Kim, "First Law of Thermodynamics and Friedmann Equations of
  Friedmann-Robertson-Walker Universe", **arXiv:hep-th/0501055v1** (8 Jan 2005), JHEP 0502
  (2005) 050. Used for:
  - eqs. (2.3) apparent-horizon radius, (2.4) event-horizon definition, (2.14) Friedmann
    $\dot H$ equation, (2.15) $\dot{\tilde r}_A$;
  - the remark that in pure de Sitter the three horizons coincide and are constant.

**Known only second-hand [LIT2], not used as support:** Carroll–Chen, hep-th/0410270 and
gr-qc/0505037 (via Wald's footnote only); Layzer and Frautschi on entropy in an expanding
universe; Davies on cosmological event-horizon area and the generalized second law.

## Not checked

- The source of the "Ellis objection".
- The companion *Physics Modulo Gauge* (cited at Substratum:403, :413).
- Main reference [31].
- Any Lean counterpart: none was found by grep, and no Lean build was run.
- Byte identity of the FULL mirrors across whole chapters.
- §C.2, §C.3 and §C.5 are hand arguments written for this note, and §C.4 and §E are exact
  algebra written for this note. None was machine-checked. The review packet below lists
  them.

## Review packet: what an independent reviewer must verify

1. **§E.2.** The apparent-horizon derivative in both forms, the sign role of H, the NEC
   role, and the equality case.
2. **§E.3 and T1b.** The event-horizon bound $R_e\ge c/H$ when $\dot H\le0$ on
   $[t,\infty)$; the de Sitter equality case; the event/particle exchange under $t\to-t$;
   and that T1b's hypotheses are stated on $[t,\infty)$.
3. **§E.4.** The four regimes, especially the phantom solution's signs, and the scope of
   the ä > 0 verdict: general criterion refuted; strict increase false in exact de Sitter;
   weakly true but not operative in the NEC background.
4. **§C.4.** The CNOT table, that it satisfies Theorem A.6's hypotheses, and that it
   refutes only the monotone reading.
5. **§C.3.** The block-entropy identity for $M_k$ and its reversal invariance under the
   invariant measure. The adjoint-compression argument under the stated $P_\Sigma$
   reading. The bounded-range assumption for $\varphi^{-1}$, and that it holds for a
   site-local T.
6. **§C.5.** The multi-time extension of SM Theorem 19; the swap witness; and, assuming A
   and $S_{\rm cg}$ are T-even, that T maps aligned histories to aligned histories.
7. **§C.2.** That each rooted result cited (Main:137, :518, Theorem A.6) has its backward
   counterpart. That `no_universal_oriented_property` (OrientationClosure.lean:249) states
   the abstract step as quoted, and that the hand instantiation is valid.
8. **§B.3 (P3).** That $\rho_s=\rho_{\rm crit}$ concerns the boundary entropy only, and
   cannot by itself supply the entropy–area relation.
9. **§B.7.** That T7's premises Q1–Q4 are each unproved in the corpus, and that no
   counterexample to alignment exists, so the verdict is open, not refuted.
10. **§B.10.** That each listed dependency is used by Substratum §5.4's own text.
11. **§F.4.** Whether the Main:744 label phrase and the LEDGER.json rename are in scope as
    necessary consequences of the retitle.
12. **Locators.** That every quoted locator matches `f5c281ae`.
