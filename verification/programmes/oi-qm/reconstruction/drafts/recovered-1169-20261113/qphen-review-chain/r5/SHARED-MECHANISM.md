# QPHEN Phase 1: the shared-mechanism requirements matrix (QX-0 to QX-7) (draft r5)

## 0. Standing

**Authority and status.**
- #1210 Phase 1, paper only (c.6736966265).
- Model-written. No mechanism is built, no computation on any proposed OI mechanism is run, no criterion is frozen,
  and no premise is adopted.
- Exact checks of paper claims on generic mathematical objects are allowed when labelled as such: "Allowed: generic
  checks" (#1210 c.6739250392, owner, 2026-11-09). The checks cited here (probes P1–P9 under `review/probes/`) are of
  that kind, and a result supported only by such a check is marked computation-supported in `SHARED-MECHANISM.md` §8.
- Owner records governing these specifications are listed, with author and time, in `QX3-ANTIBUNCHING.md` §0.

**Revisions.** Earlier texts are kept under `r1/`, `r2/`, `r3/` and `r4/`. The revision record is `DISPOSITIONS-r5.md`.

**Conventions.** Evidence layers, types (EN, CS, IQ, IR, untyped) and dependencies (MC, MECH-OPEN, —) are as in
`QX3-ANTIBUNCHING.md` §0 (r5).

**Inputs.**
- The three Phase 1 specifications (r5).
- Q-C2-1 r12/r13 drafts [D] for QX-0, QX-1, QX-2 and QX-7.
- Q-C2-2 r13 [D] for QX-5.
- `oicore/OICORE-1.md` [D].
- The corpus at `fd539e15`.

**Programme rule.** One shared mechanism. Every extension is justified independently, reviewed, and evaluated for its
effect on earlier experiments (#1210 requirement 1).

***

## 1. Capabilities

| id | capability | type | dependency | status |
| --- | --- | --- | --- | --- |
| M1 | one bijective second-order step on finite cells (L-BIJ, L-SYM, L-SYMP) | EN | — | available |
| M2 | probabilities from configuration counting (N2) | CS | — | available; rational only (dyadic at `q = 2` without conditioning) |
| M3 | epistemic supply restriction: half-known ready cells (SA-1(c)) | CS (posited, not derived; AP1:347) | — | available; carries complementarity's universality in QX-0 [D] |
| M4 | known-value and QA-family preparations (H-PREP) | CS (open hypothesis) | — | available |
| M5 | meters with terminal registration (SA-1(b)) | CS (RET-s; idealization below recurrence) | — | available |
| M6 | setting switch: per-tick, per-edge arming with isolation (P3, E-iso) | CS, in tension with FIX; a dynamics row (Q-C2-1 R7-B2) | — | available; the FIX alternative is NR-16 |
| M7 | held unread records, forward conditioning (RET-w; L-HOLD, L-FWD) | retention EN; isolation and conditioning CS | — | available |
| M8 | owner-typed observer access class with a completeness check (L-ACC; D15) | CS (D15(a) typed CS by the owner, #1169 c.6735014875) | — | available. Consistency of ACC_op with the core is open (OICORE-1 §3.2) |
| M9 | representation identifications: path, port, frame, U′ (L-PATH, L-PORT, L-CAL, L-UPRIME), and the click (L-CLICK) | IR. D18 was decided (a), conditional, for the four mappings (#1169 c.6735014875, amaybaum, 2026-11-09T07:52:50Z), with a representation ledger and a check that no mapping supplies a quantum-specific resource. L-CLICK is outside that decision | — | ledger in Q-C2-1 [D]; L-CLICK needs owner typing |
| M10 | phase settings `{0, π}` | EN step; CS supply | — | available |
| M11 | quarter phase and `Y` read (NNB on U′) | supplied conditional premise | — | not native under the one-cell identification (AP1 Lemma 5). D4(a): "Test what existing OI dynamics can produce before introducing quarter phases or NNB" (c.6735014875) |
| M12 | one fixed non-Clifford operation on an encoded carrier | — | MC (Obligation C / OICORE-1 drive clause) | open |
| M13 | repeated composition of a fixed operation | — | MC | open (C's horizons `K ∈ {6, 12}`) |
| M14 | routing: one excitation to exactly one of two cells, read as own-cell occupation, conserving number on a declared domain | untyped (dynamics) | MECH-OPEN | affine under `NCONS_ready`; non-affine under `NCONS_global` (QX-3 A3.1(b)–(c)). Whether OI's step supplies either is not evaluated |
| M15 | reciprocal detector coupling, preserved under any routing or non-affine element | constraint | — | holds in the affine-symplectic class; copy-only detection breaks it (QX-3 A3.2) |
| M16 | null-result invasiveness of location detectors (`K_null ≠ id`) | constraint; its only identified support is agreement with QM, so it is a hypothesis under test (§9) | MECH-OPEN | required for INM agreement with QX-4c's comparator protocol under QX-4 A4.4's hypotheses (H1), (H2), (H4) |
| M17 | two-system composite: cone separation, per-observer access maps, local tomography | cone lemma P (Main §3.3); access maps CS (supplied abstractly, W); local tomography a hypothesis (COMP-1) | — | partial |
| M18 | pair source (two-party; three-party for the GHZ-type option) | untyped | MECH-OPEN | absent (prepared-pair-source (W)); no entangling operation within M2D U2's scope (W) |
| M19 | cross-wing response (ontic parameter dependence; preparation-indexed adjacency) | CS as the named open hypothesis H-Bell (dynamics) | MECH-OPEN | open (Substratum:131) |
| M20 | complete-history no-signalling and Tsirelson soundness over the admitted preparation class | constraints. Tsirelson soundness has no identified support other than agreement with QM, so it is a hypothesis under test (§9) | MECH-OPEN | open; failed by the only explicit candidate (W) |
| M21 | validation layer: `D`, `K`, `K_null`, NONABS, SPI, STAB, `NCONS_ready`, `NCONS_global`, cone distances, MI | method (construction-internal; never observer data; never an import of quantum behaviour) | — | definable |
| M22 | exact LP noncontextuality method: Farkas certificates, Lemma NC-F, attributed completions | method | — | available [D] |
| M23 | exchange symmetry of identical excitations | untyped | MECH-OPEN | absent from the corpus |

## 2. Requirements matrix

**Cell legend.**
- **R**: required for the experiment's discriminating (Level ≥ 2) form.
- **r**: required for its Level-1 or reduced form.
- **?**: depends on a pending owner decision or an optional variant.
- **·**: not needed.

| | QX-0 which-path | QX-1 superposition and recombination | QX-2 eraser | QX-3 antibunching | QX-4 incompatibility / LG | QX-5 contextuality | QX-6 Bell | QX-7 composition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1 step | R | R | R | R | R | R | R | R |
| M2 N2 | R | R | R | R | R | R | R | R |
| M3 SA-1(c) | R (universality) | r | R | r (`V` half) | R (backaction) | R (P2 inputs) | ? (R6.9 candidate) | r |
| M4 H-PREP | R | R | R | R | R | R | R | R |
| M5 SA-1(b) | R | R | R | R | R | ? (reads) | R (per wing) | R |
| M6 P3 / E-iso | R (detector switch) | R | R | R | R | ? | R (settings, inside each wing; A6.1) | R |
| M7 held records, conditioning | R (`D`) | r | R | r (herald) | r | R (heralds) | R (histories) | r |
| M8 typed access class | R (B-P) | · | r | · | R (4b) | R | R (per wing) | r (B-C) |
| M9 identifications | R | R | R | R (+ L-CLICK) | R | R | R | R |
| M10 `{0, π}` | R | r | R | R | r | r | r | r |
| M11 quarter phase / `Y` | ? (D4(a)) | ? | · | · | ? | ? (spanning) | · (the GHZ-type option uses `X/Z` reads on the triangle graph state, protocol GHZ-2; QX-6 §2) | r (`Λ_{y,b}`) |
| M12 non-Clifford operation | · | R | · | · (only R3.8) | R (4c's QM-matching value with stabilizer preparations, A4.1(c); 4b's quantum value) | R (beyond stabilizer) | r (QM-matching settings with stabilizer pairs; not sufficient under A6.1's hypotheses, including the design assumptions (L′) and (R); A6.2) | R |
| M13 repeated composition | · | R | · | · | r (2 applications; A4.5) | · | r | R |
| M14 routing | ? (NR-13) | · | · | R | R (INM) | · | · | · |
| M15 reciprocity kept | R (control) | · | R | R | R | · | r | · |
| M16 null-result invasiveness | · | · | · | · | ? (tested in the INM variant under H1, H2, H4; QM-only, §9) | · | · | · |
| M17 composite | · | · | · | ? (W3) | · | · | R | ? (NR-11) |
| M18 pair source | · | · | · | ? (W3) | · | · | R (three-party for GHZ-type) | · |
| M19 cross-wing response | · | · | · | · | · | · | R | · |
| M20 no-signalling, Tsirelson | · | · | · | · | r (NSIT reported) | · | R (no-signalling); ? (Tsirelson half: tested; QM-only, §9) | · |
| M21 validation layer | R | R | R | R | R | R | R | R |
| M22 LP method | R (Test B) | · | · | · | R (4b) | R | ? | r (B-C) |
| M23 exchange symmetry | · | · | · | ? (W3) | · | · | · | · |

**Imported (IQ) inputs, admitted only in a benchmark:**

| experiment | IQ inputs |
| --- | --- |
| QX-0 | QM-P comparators |
| QX-1 | supplied gates |
| QX-2 | QM comparators |
| QX-3 | Fock-1 law |
| QX-4 | supplied `π/3` rotation |
| QX-5 | QM fragment |
| QX-6 | calibrated `η*`, supplied pair |
| QX-7 | supplied gates |

## 3. The minimal set for one construction serving all eight

**Core.** Every column needs:
- M1, M2, M4 and M5;
- M6, or its FIX-compatible replacement;
- M9, typed under D18(a), with L-CLICK typed separately;
- M21.

**Epistemic restriction and access, with no dynamics credit: M3, M7 and M8.** In the current construction these carry:
- complementarity's universality (QX-0);
- backaction (QX-4a);
- possibly the affine-scope Leggett–Garg bound. This is AW-QX4-1, a two-mode scan only and not a result;
- the fragment of every contextuality test (QX-0 B, QX-4b, QX-5);
- the only state restrictions available for a no-signalling mask in a parameter-dependent Bell completion. None is shown
  to mask (QX-6 A6.4).

M3 is the most cross-cutting B principle, and it is posited, not derived.

**Dynamics elements beyond the affine-symplectic step.**
- **Non-affine rules in use.** Two are in use at present:
  - C's gadget rules `g ∈ {AND, NAND, OR, NOR}` (Q-C2-1 [D]);
  - `G_SM`, SM's state-dependent ring rule, used by Q-C2-2 and M2D. It is a stated hypothesis in SM, not physically
    sourced, and its edges are not reciprocal for `L ≥ 5` (M2D §0 item 1 (W)).

  Under FIX one rule must serve both, or each is a separate extension with its own justification and its own
  evaluation against QX-0.
- **QX-3's routing (M14).** It is a third dynamics element only conditionally.
  - Under `NCONS_ready` an affine map routes, for example P2's `L` (QX-3 A3.1(b)).
  - Under `NCONS_global` it must be non-affine (A3.1(c)), making it a third non-affine rule unless one of the two above
    supplies it.
  - The domain is owner question Q3-2. Whether OI's step supplies an affine router is MECH-OPEN.
- **The constraints M15 and M16 apply to whatever routing is adopted.**

**Two-system structure: M17 and M18.** Needed by QX-6, and by options in QX-3 and QX-7.

**Cross-wing dynamics: M19 under M20 (QX-6 only).**
- Main §3.3 covers one-step own-wing settings. This programme's extension A6.1 [A, complete proof, independently
  reviewed; conditional on its design assumptions (L′) and (R)] covers
  multi-tick own-wing operations and arming inside each wing, with a declared local `⊥ ↦ +1` rule. It requires
  (L′): every tick's map is independent of a wing's setting outside that wing's region. Main's one-step form
  satisfies every hypothesis of A6.1 (QX-6 A6.1, table).
- Under those hypotheses, constructions built only from access restrictions, state restrictions on a
  setting-independent ensemble, own-wing local operations (M12 included) and local registration rules do not exceed
  `|S| = 2`.
- M19 is itself a candidate OI principle (H-Bell), and A6.1 does not cover it.

**Counting.**
- Construction B's present principles (M3–M8) supply none of M12 or M19, and M14 only if an affine router is admitted
  and supplied.
- A construction serving all eight therefore needs the following, each under the condition stated (§8.4):
  - a coherent-mixing resource (M12), for QX-4c's QM-matching value with stabilizer preparations (QX-4 A4.1(c)) and
    for QX-6's QM-matching settings with stabilizer pair states (QX-6 A6.2). For QX-1, QX-5 and QX-7 its support is
    Q-C2-1 and Q-C2-2 drafts [D], and there it is open;
  - a cross-wing response (M19) with a no-signalling mask (M20). Under (D) and (MI), `|S| > 2` needs a failure of (L′)
    or (R) (A6.1 [A]). With the design excluding failures of (L′) and insufficient separation (QX-6 §3.2), the
    failure left is a coupling path between the wings' regions shorter than the run, a cross-wing response, for which
    preparation-indexed adjacency (H-Bell) is the programme's candidate. Complete-history no-signalling is part of
    QX-6's Level-2 witness (QX-6 §9);
  - a pair source (M18), which QX-6's protocol presupposes (QX-6 §1);
  - a routing element (M14), for QX-3's creditable arm `B_3-route` and for QX-4's INM variant (QX-3 §8; QX-4 R4.9).
    It may or may not be a further non-affine premise, depending on Q3-2 and MECH-OPEN.
- Whether these can be fewer independent premises is open.

**H-SDC (named only; not adopted, typed or evaluated).**
- **Statement.** One fixed state-dependent-coupling rule, in the sense of SM's `G(x)` (SM §3.1; Substratum:131),
  supplies:
  - M12, through its non-affine encoded action;
  - M14, through state-controlled routing, if `NCONS_global` is required;
  - M19, through preparation-indexed long edges.
- **Productivity test (§A.31).** H-SDC counts only if one rule, fixed in advance with its identifications and reads,
  does all three. Describing three mechanisms as "some nonlinear coupling" is relabelling.
- **Known obstacles, stated first because the reading favours the framework.**
  1. Non-affine rules need not be symplectic or reciprocal. `G_SM`'s edges are not reciprocal, so M15 and QX-0's
     complementarity are not guaranteed.
  2. Under `STAB(K)`, C-type positives have orders 3 or 6 only (cone review [D]), which restricts Leggett–Garg and
     Bell uses to the `π/3` grid.
  3. M2D Theorem U2 (W) bars entangling encoded unitaries for every fixed bijection under R1^⊗n and H-LIFT, so M18
     must come from outside that scope.
  4. The rule must exclude PR-type responses (M20), and no principle bounding `S` at `2√2` is known.
  5. H-Bell is recorded as downstream of an unmet curvature re-founding obligation (`verification/ROADMAP.md`:974-979
     at `fd539e15`, quoted in HB-1 as 764-769).
  6. If `NCONS_ready` suffices, M14 does not need H-SDC at all, and one of its three claimed unifications falls away.

## 4. Cross-experiment tensions an extension must be evaluated against

| # | tension | experiments | source |
| --- | --- | --- | --- |
| T1 | A copy-only detector records the path without the kick, giving P-RECORD-WITHOUT-SUPPRESSION (`DESIGN-DS.md` finding 9, ABL-RECIP [D]). A routing element outside the affine-symplectic class need not be reciprocal. M15 is a control on every routing element | QX-0, QX-3 | QX-3 A3.2 |
| T2 | With `Q₁` fixed by preparation from a setting-independent supply, placement independent of the ontic state, and `Q` a configuration functional (IR), an INM detector must act on its silent branch (M16) if the construction is to match QX-4c's comparator protocol. Otherwise construction B's ontic model obeys the INM bound against that protocol. The routing coupling must act on its silent branch (`K_null ≠ id`), for example by keeping the reciprocal, outcome-independent kick | QX-3, QX-4 | QX-4 A4.4 (H1)–(H4) |
| T3 | P3 arming is every experiment's setting switch but is in tension with FIX. A6.1 admits it in QX-6 only inside each wing | all | `DESIGN-DS.md` §2 [D]; OICORE-1 §2 [D] |
| T4 | Two non-affine rules are in use (C's gadget rules; `G_SM`). Routing adds a third only under `NCONS_global` | QX-1, QX-3, QX-5, QX-7 | Q-C2-1, Q-C2-2, M2D; QX-3 A3.1 |
| T5 | An access restriction can manufacture no-signalling (QX-6) or contextuality (QX-0 B, QX-4b, QX-5). It is reported `access_only` and never credited with dynamics | QX-0, QX-4, QX-5, QX-6 | owner c.6734374076; `DESIGN-DS.md` §5 finding 6 [D]; NO-SIGNALLING.md item 5 (W) |
| T6 | N2 gives rational probabilities (dyadic at `q = 2` without conditioning), so irrational targets (`2√2`; PO-RAC `(1 + 1/√2)/2`) are exactly unreachable. Comparators sit at rational settings, with exact decision procedures; TLM is exact on correlators only | QX-4, QX-6 | QX-4 §7; QX-6 §1, A6.3 |
| T7 | L-PORT fixes the encoded anticorrelation and is not credited as dynamics | QX-0, QX-3 | `DESIGN-DS.md` §5 finding 5 [D] |
| T8 | Construction B, given SA-1(c) (CS) and the IR premise that the read quantity is a configuration functional, is a macrorealist-per-se, invasive, epistemically restricted model. No witness in QX-0 to QX-4 excludes that class. QX-5 does so only over a typed fragment. QX-6 excludes local hidden variables, and only with a cross-wing response | all | QX-3 §2; QX-4 §2, §7; QX-6 §2 |
| T9 | With a sharp mediator, the affine-symplectic class reaches `K₃ = 2`, above the Lüders bound `3/2` of QX-4c's comparator protocol (Lüders reads of the carrier's `Z`, unitary `G`). QM reaches `K₃ = 2` and `3` with measure-and-reprepare instruments (QX-4 §2). This is not a justification of SA-1(c), whose status remains posited, not derived (AP1:344-350; §9) | QX-0, QX-4 | QX-4 A4.1(b) |

**Controls an extension must preserve** (§A.29; the extension's own controls):
- QX-0's P-COMPLEMENTARITY existence and universality readings, if Q-C2-1 returns them.
- `K₃ ≤ 1` at one mode, and at two modes under SA-1(c) or environment supplies (QX-4 A4.1(a)–(b); the latter a scan).
- Main §3.3's Bell ceiling, with A6.1's extension, conditional on the design assumptions (L′) and (R), for local
  constructions under the `⊥` rule.
- C's ABL: affine rules give no W-CL. This is conditional on Theorem C [D] and on Lemma P, proved conditional on
  Theorem C(ii) and L1–L3.
- Lemma P and Theorem C within their scopes.
- ARP-1-MARC's SURVIVAL within its scope (affine `N_1`, `|H| ∈ {4, 6}`, `T = 4`).
- OICORE-1's Lemma M. It applies only where some core-realizer satisfies the restriction; it is not used for ACC_op,
  for which no witness is exhibited (OICORE-1 §3.1).

## 5. Dependency refinements proposed for #1210's table (planning input only; no Issue edit made)

**QX-3**
- Recorded: blocked, pending QX-0 review.
- Proposed:
  - W1 and W2 do not depend on Obligation C.
  - They need M14: affine under `NCONS_ready`, non-affine under `NCONS_global`; the domain is decided by Q3-2. Whether
    OI's step supplies the map is open.
  - They need the M15 control.
  - W2's best case excludes classical fields under square-law, independent detection and particle models with no
    wave-like phase variable, and no epistemically restricted model (QX-3 §2).

**QX-4**
- Recorded: blocked: QX-0.
- Proposed:
  - 4a is posable on Q-C2-1's apparatus, at Level 1.
  - 4b belongs with QX-5.
  - With stabilizer preparations, 4c's QM-matching value needs C-EXPOSURE or C-SIZE-DEPENDENT (A4.1(c), A4.5). With
    a non-stabilizer preparation and a further mode, a Clifford `G` is not excluded (A4.1(c)).
  - The INM variant needs M14. Matching the comparator protocol under INM, given (H1), (H2) and (H4), also needs M16,
    which is a hypothesis under test (§9).
  - AW-QX4-1 is recorded.

**QX-6**
- Recorded: blocked: QX-1.
- Proposed:
  - QX-1 / Obligation C is needed for QM-matching settings with stabilizer pair states. It is not sufficient for
    constructions satisfying A6.1's hypotheses, including its design assumptions (L′) and (R) (A6.2).
  - The binding prerequisites are a pair source (M18), H-Bell's cross-wing response (M19) and complete-history
    no-signalling (M20). No Q-C2-1 outcome supplies any of them.

**QX-5, QX-7**
- Recorded: per ARP order; blocked: QX-0.
- Proposed: T4. QX-5's rule (`G_SM`) differs from C's gadget rules, and one shared mechanism needs one rule.

## 6. Common reporting schema (outline; not frozen)

**For every experiment and ablation:**
- `pred_change` (computed): do the reachable detector-record observables change?
- `mech_change` (computed): do the realizing mechanisms in the validation layer change?
- `access_only` (computed): are the full world laws identical, with only the registered or unread records
  differing?
- `dynamics_credit` (the row's kind): a state or access restriction is never credited with new dynamics.

**Also reported for every experiment:**
- the classical classes each witness excludes and those it does not;
- the Level, with no level awarded from a lower one;
- each identification's D18-ledger and REP-INV status;
- for Bell-type tests, the declared `⊥` rule.

## 7. References to content off `main`

The three specifications' reference tables (QX-3 §10, QX-4 §10, QX-6 §11) apply. This file adds:

| reference | claim | classification |
| --- | --- | --- |
| #1210 c.6736966265; #1169 c.6734304025, c.6734374076, c.6735014875 | §0; M8, M9 and M11 typing; T5 | owner records; quoted where used |
| `oicore/OICORE-1.md` §§2, 3.1, 3.2, 8.4, 8.10 | M6, M8, M12, T3; Lemma M's applicability | off `main` (D) |
| Q-C2-1 `DECISIONS.md` and the r13 drafts; Q-C2-2 r13 | the M-rows' status; T1, T4, T7 | off `main` (D) |
| `review/REVIEW-PHASE1.md`; probes P1 to P3 | A3.1(b)–(c), A4.1(b), the triangle-graph contradiction, as propagated here | off `main` (D); exact finite computations on generic objects |
| `review/REVIEW-PHASE1-r2.md` (`47af406f…`); probe P4 (`2e7c2de9…`) | §8's disproved items for A6.1 and R4.9; GHZ-1's values | off `main` (D); exact finite computations on generic objects |
| writer's probes P5-A61, P5-LG, P5-GHZ, P5-QX3 (`review/probes/p5_r3_*.py`) | §8 entries that cite them | off `main` (D); exact, except P5-A61's random sample and P5-LG's Lüders search |
| `review/REVIEW-PHASE1-r3.md` (`448614ea…`); reviewer probes `p6_r3rev_a61.py`, `p6_r3rev_lg.py`, `p6_r3rev_ghz_chsh.py`, `p6_r3rev_qx3.py`, `p6_r3rev_aw3.py` | §8: A6.1's independent review; the independent reproduction of every X entry; Q4-P7's mixture; Q3-P6a; Q4-O1's `m = 3` sample | off `main` (D); exact checks on generic objects, except the `m = 3` random sample |
| writer's probe `review/probes/p7_r4_lg_order.py` | §8 Q4-P4 and Q4-D6: the stated tensor order and gate placement, and the other placement of `H` | off `main` (D); exact; imports no earlier probe |
| `review/REVIEW-PHASE1-r4.md` (`755c3af0…`); reviewer probe `review/probes/p8_r4rev_membership.py` (`81013173…`) | §8: Q4-P19's argument; Q4-D3's membership; the second reproduction of Q3-P6a, Q4-P7 and Q4-D1's values; Q4-P15's symplecticity | off `main` (D); exact checks on generic objects; imports no earlier probe |
| writer's probe `review/probes/p9_r5_symplectic_detector.py` | §8 Q4-P19's exhaustive count; Q4-D3's membership; Q4-P15's symplecticity | off `main` (D); exact, exhaustive over the affine maps of `F_2⁴`; imports no earlier probe |
| #1210 c.6738145827, c.6738337450, c.6738866690, c.6739250392, c.6739286623 (amaybaum, 2026-11-09) | §0; §8 rules; §9 rules | owner records; quoted with author and time in `QX3-ANTIBUNCHING.md` §0 |
| Substratum:131, :467, :481; Main:22, :44, :50, :56, :362-389, :406-414, :429; AP1:282-350, :415-421; `arp/qc21/DECISIONS.md` D15 | §9 | on `main` (P; AP1 W), except `DECISIONS.md` (off `main`, D) |
| M2D; AP1; oi-qm-ext-1 records; ARP-1-MARC result | §§1, 3, 4 | on `main` (W, or a native round), conditional on their stated hypotheses (§A.46 item 7) |

## 8. Claim-status ledger (QX-3, QX-4, QX-6 and this file)

**Rules.**
- Every substantive claim of the three specifications and of this file appears in exactly one of three lists:
  **proved**, **disproved** or **open**.
  - A proved entry states its hypotheses and its strongest support:
    - K: kernel;
    - P: a paper proof on `main`;
    - A: a derivation in these files, unreviewed unless stated;
    - X: an exact or exhaustive finite computation on generic mathematical objects, with its scope;
    - L: literature, not checked here unless stated.
  - A disproved entry states the refuted statement, an explicit counterexample, and a membership line. The membership
    line shows that the counterexample satisfies every defining condition of the class the refuted claim is about.
    Where membership cannot be shown, the refuted claim is restated over a class the counterexample belongs to, and
    the original, narrower claim is listed as open.
  - An open entry states what is missing.
- An X computation is a probe under `review/probes/`: re-runnable, off `main`, and on generic objects only, never on
  an OI mechanism. It counts as X at its stated scope when it has been independently reproduced, by a second probe
  written separately (P1–P4, P6 and P8 by reviewers; P5, P7 and P9 by the writer). An entry whose only support is
  such a computation is marked **computation-supported** ("Allowed: generic checks", #1210 c.6739250392, owner,
  2026-11-09).
- A claim whose only support is a W record or a D draft is open (§A.46 item 7).
- Paper expectations for arms and ablations are open unless they are listed as proved.
- Every branch of the decision trees (QX-3 §6, QX-4 §6, QX-6 §7) is open, because its antecedent is a Q-C2-1 outcome
  not yet obtained.
- Owner questions and dependency proposals (§5) are planning items, not claims.
- Each direction of an equivalence is a separate entry (§A.34).

### 8.1 QX-3

**Proved**
- **Q3-P1** [A; X: P2, all cosets of `F_2⁴`, 314,368 cases; reproduced by `p6_r3rev_qx3.py`]. *A3.1(a).*
  - Hypotheses: supply bits uniform on a coset (N2); detector functionals `f_A`, `f_B` affine; a click is the value 1.
  - Conclusion: `α ∈ {0, 1, 2}`, or `α` is undefined.
- **Q3-P2** [A; X: P2, `p6_r3rev_qx3.py`]. A3.1(a), direction (⇐): if `f_B = f_A + 1` with `f_A` non-constant, then
  `α = 0`.
- **Q3-P3** [A; X: P2, `p6_r3rev_qx3.py`]. A3.1(a), direction (⇒): if `α = 0`, then `f_B = f_A + 1` with `f_A`
  non-constant.
- **Q3-P4** [X: P2, P5-QX3, `p6_r3rev_qx3.py`; computation-supported]. *A3.1(b).*
  `L(s, c₁, c₂) = (s, s + c₁, s + c₂)` is a linear bijection of `F_2³`. On the ready support (`c₁ = 1`, `c₂ = 0`,
  `s` uniform):
  - it routes one excitation by `s` into `c₁` or `c₂`;
  - own-cell reads give `α = 0`;
  - weight is conserved.

  `L` equals the Fredkin gate on the sector `c₁ + c₂ = 1`. 48 affine bijections of `F_2³` route on the ready support
  with weight conserved there.
- **Q3-P5** [A; X: P2, P5-QX3, `p6_r3rev_qx3.py` on `F_2³`]. *A3.1(c)*, with weight counting every coordinate, `s`
  included.
  - Direction (⇒): an affine bijection of `F_2ⁿ` that preserves Hamming weight everywhere is a coordinate
    permutation.
  - Direction (⇐): every coordinate permutation is affine and weight-preserving.
  - On `F_2³` there are 6 such maps.
- **Q3-P6** [A; X: P5-QX3, `p6_r3rev_qx3.py`]. A coordinate permutation cannot route by an unknown bit, so under
  `NCONS_global` a router is non-affine. Fredkin is a non-affine, globally weight-preserving router.
  - Computation-supported counts: all 8 globally weight-preserving routing bijections of `F_2³` are non-affine.
- **Q3-P6a** [A; X: `p6_r3rev_qx3.py` (c), `p8_r4rev_membership.py` (8)]. *A3.1(c), field-only weight.*
  - An affine map that preserves field weight for both values of `s` acts on the field cells as the identity or the
    swap, the same for both values, so it cannot route.
  - Computation-supported count: the 64 field-weight-preserving routing bijections of `F_2³` are all non-affine.
- **Q3-P7** [A, from Q3-P1 to Q3-P3]. *ABL-ROUTE's values.* With `f_A = f_B` non-constant, `α = 2`; under routing,
  `α = 0`.
- **Q3-P8** [L].
  - The Cauchy–Schwarz bound `α ≥ 1` for classical fields with square-law, independent detection (W1).
  - Classical-field Hong–Ou–Mandel visibility is at most `1/2` (W3).
  - QM's `g⁽²⁾(0)` values for Fock-`n`, coherent and thermal sources, and the Hong–Ou–Mandel dip (§2).
- **Q3-P9** [search record]. The §A.19 search of `papers/*.md`, `book/ch*.md` and `book/appendix*.md` at `fd539e15`,
  for the listed terms, finds no OI treatment of single-quantum statistics.
- **Q3-P10** [A]. *§3, coherent mixing.* W1 and W2 need only operations in the stabilizer and classical-reversible
  class:
  - `{0, π}` phases, which are Pauli `Z`;
  - the 50:50 split and recombination, which are Hadamard-type Clifford operations;
  - routing by `L` (linear) or Fredkin (classical reversible).
- **Q3-P11** [A, exact]. *§7 item 5.* The dyadic law with cells `9, 151, 71, 25` out of 256, so `P_AB = 9/256`,
  `P_A = 5/8` and `P_B = 5/16`, gives `α = 9/50`.

**Disproved**
- **Q3-D1.** *Claim:* "Routing one excitation by an unknown bit into one of two separate cells, read as own-cell
  occupation, with excitation number conserved on the ready support, needs a non-affine map."
  - *Counterexample:* the linear map `L` of Q3-P4 (P2; P5-QX3; `p6_r3rev_qx3.py`).
  - *Membership:*
    - `L` is a bijection of `F_2³`.
    - On the ready support it sends `s = 0` to `(0, 1, 0)` and `s = 1` to `(1, 0, 1)`, so one excitation sits in
      field cell `c₁` or in field cell `c₂`, selected by the unknown bit `s`.
    - Each detector reads its own cell's occupation.
    - The weight is 1 before and after for `s = 0`, and 2 before and after for `s = 1`.
    - `L` is linear, hence not non-affine.

**Open**
- **Q3-O1** (MECH-OPEN). Whether OI's step supplies an affine router of `L`'s kind, or a non-affine router (R3.6, M14).
- **Q3-O2.** Which additional physical constraints, if any, make non-affine routing necessary. `NCONS_global` is one
  such constraint, and no OI principle with a reason independent of QM is identified that requires it (§9; Q3-2).
- **Q3-O3.** W3's classical status: whether an epistemically restricted discrete model reproduces the full
  Hong–Ou–Mandel dip.
- **Q3-O4.** L-CLICK's typing (Q3-3) and its REP-INV status.
- **Q3-O5** (supported only by D or W records).
  - The symmetric spatial ring gives `f_A = f_B` (Q-C2-1 r6 finding 5 [D]).
  - Construction B is noncontextual at stabilizer scope (`DESIGN-DS.md` §4 [D]; OICORE-1 §5(b) [D]).
  - The copy-only hazard (`DESIGN-DS.md` finding 9 [D]).
  - `G_SM` is non-reciprocal for `L ≥ 5` (M2D [W]).
  - Complementarity's reciprocity mechanism (AP1 §3.2 [W]).
  - The toy field theory reproduces the interference phenomena listed in §2 (L, abstract only).
- **Q3-O6.** The paper expectations of `A_3`, `B_3-enc` and `B_3-route` (`V = 1` included), and of every ablation
  except ABL-ROUTE's `α` values (Q3-P7).

### 8.2 QX-4

**Proved**
- **Q4-P1** [A; X: P3, 24 maps; `p6_r3rev_lg.py` (5a)]. *A4.1(a).* Hypotheses: one encoded mode `(z, x)`,
  affine-symplectic `G` with translations, and a `Z` read that adds a uniform kick to `x`.
  - The correlators lie in `{0, ±1}` and follow the stated case table.
  - Every form of `K₃` is at most 1.
  - The same holds for one qubit with a Clifford `G` and Lüders `Z` reads, for any preparation (A4.2).
- **Q4-P2** [X: P3, exhaustive over 11,520 affine-symplectic maps with translations on two modes, one read model;
  `p6_r3rev_lg.py` (5b); computation-supported]. *A4.1(b).*
  - The maximum of `K₃` is 1 with a half-known or environment mediator.
  - It is 2 with a sharp mediator, with the stated witness.
- **Q4-P3** [A; X: P5-LG, all 11,520 two-qubit Cliffords with product stabilizer preparations]. *A4.1(c).*
  - Hypotheses: in the affine class, N2 laws uniform on a coset; in the Clifford class, pure stabilizer preparations
    of every mode and Lüders `Z` reads.
  - Conclusion: the correlators lie in `{0, ±1}` at any number of modes, so `K₃` is an integer.
  - Consequence: under these hypotheses a value in `(1, 3/2]` needs a non-Clifford `G`. With the Lüders bound
    (Q4-P8), `K₃ ≤ 1` in the Clifford class.
  - For convex mixtures of pure stabilizer states, `K₃ ≤ 1` still holds, by linearity.
- **Q4-P4** [X: P5-LG, `p6_r3rev_lg.py` (1), (4), and `p7_r4_lg_order.py`; exact; computation-supported].
  *A4.1(c)'s counterexamples.* Tensor order carrier ⊗ mediator, basis `|c m⟩`; Lüders reads of `Z` on the carrier.
  - `CNOT` from an ancilla `cos θ|0⟩ + sin θ|1⟩` onto a carrier in `|0⟩` gives `C₁₂ = cos 2θ`.
  - `G = (I ⊗ H)·CNOT_{m→c}`: the `CNOT` has the mediator as control and the carrier as target, then `H` acts on the
    mediator. With carrier `|+⟩` and mediator Bloch vector `(sin β, 0, cos β)` it gives `K₃ = cos β + sin β`.
  - `G = (I ⊗ H)·SWAP·CNOT_{m→c}`, with `H` on the mediator slot, mediator `|0⟩` and carrier Bloch vector
    `(sin β, 0, cos β)`, gives `K₃ = cos β + sin β`.
  - With `H` on the carrier instead, the values are `K₃ = −cos β` and `K₃ = 0` respectively.
- **Q4-P5** [A]. *A4.3.*
  - On a `Z±` preparation, a `t₂` read whose kick lands on the unknown conjugate slot leaves the law of `Q₃`
    unchanged.
  - A Lüders `Z` read leaves a `Z` eigenstate unchanged.

  Both pass the adroitness control.
- **Q4-P6** [A; the Leggett–Garg argument, L]. *A4.4.*
  - Under (H1)–(H4), every INM form of `K₃` is at most 1.
  - Hence a construction matching the comparator protocol under INM, given (H1), (H2) and (H4), violates (H3).
- **Q4-P7** [X: P3, `p6_r3rev_lg.py` (5b), (6), `p8_r4rev_membership.py` (5); computation-supported]. *ABL-T1.*
  With an ordinary kicking `t₁` read and A4.1(b)'s witness `G`:
  - a sharp mediator gives `K₃ = 2` from the `t₁` kick alone;
  - an environment mediator gives `K₃ = 0`;
  - the mixture with weight `3/4` on the sharp mediator gives `K₃ = 3/2`.

  In every branch the `t₂` read's kick does not enter `z₃`, so the `t₂` read leaves the law of `Q₃` unchanged.
- **Q4-P8** [A: the proof in QX-4 §2; symbolic checks `p6_r3rev_lg.py` (3); numerical evidence P5-LG; L: Budroni and
  Emary, not read first-hand]. *The Lüders bound.* `K₃ ≤ 3/2` for dichotomic projective reads with the Lüders update,
  in any dimension, with degenerate `Q` included.
- **Q4-P9** [X: P5-LG, `p6_r3rev_lg.py` (2); exact; computation-supported].
  - A measure-and-reprepare instrument (read `Z`, prepare the other eigenstate), with `G = X` and preparation `|0⟩`,
    gives `K₃ = 3`.
  - The mixture with weight `w` on that repreparation gives `K₃ = 6w − 3`, so `K₃ = 2` at `w = 5/6`.
- **Q4-P10** [A, from `C(θ) = n_z² + (1 − n_z²) cos θ`; P3 and `p6_r3rev_lg.py` (7)]. *A4.6's comparator values
  (Lüders reads).*
  - With the axis `⊥ z`: `3/2` at `π/3`, and `37/25` at `arccos(3/5)`.
  - With the axis along a body diagonal: `4/3` at `π/3`.
  - An order-3 rotation with `z` in its plane gives `C₁₂ + C₂₃ + C₁₃ = −3/2`.
- **Q4-P11** [A]. For a Lüders read at `t₂` that does not commute with the evolved `Q₃`, NSIT fails for some
  preparation. Reason: `Σ_a P_a Q P_a ≠ Q` when `Q` fails to commute with some `P_a`.
- **Q4-P12** [A]. With stabilizer preparations and Pauli reads on a qubit, `P_succ ≤ 3/4`. A single-qubit stabilizer
  state has nonzero expectation for at most one of `Z` and `X`.
- **Q4-P13** [L].
  - Busch's criterion, each direction separately: (⇒) jointly measurable unsharp `Z`, `X` satisfy
    `η_Z² + η_X² ≤ 1`; (⇐) every such pair is jointly measurable.
  - Spekkens et al.: a preparation-noncontextual model gives `P_succ ≤ 3/4` (one direction).
  - Leggett–Garg: macrorealism per se with non-invasive measurability gives `K₃ ≤ 1`.
  - The qubit optimum `P_succ = (1 + 1/√2)/2`.
- **Q4-P14** [P, exact: Main:486, `lg_comb_probes.py`]. Main's classical comb reaches `K₃ = 3/2` with invasive
  permutation instruments.
- **Q4-P15** [X: P4(2), P5-LG(1); symplecticity: `p8_r4rev_membership.py` (6), `p9_r5_symplectic_detector.py`;
  computation-supported]. *R4.9.* The copy coupling `m ← m + c` is affine and not symplectic; the reciprocal coupling
  is affine and symplectic; the occupation-conditional kick `x ← x + c·m′` is not affine.
- **Q4-P16** [A]. *QX-4 §2, joint measurability.* Choosing the sharp `Z` read with probability `p` and the sharp `X`
  read otherwise gives sharpnesses `η_Z = p` and `η_X = 1 − p`, so this mixing reaches only `η_Z + η_X ≤ 1`.
- **Q4-P17** [A, elementary]. *QX-4 §2 table.* A classical wave whose two paths carry unit polarization vectors `e₁`,
  `e₂` has visibility `V = |e₁·e₂|` and path distinguishability `D = (1 − |e₁·e₂|²)^{1/2}`, so `V² + D² = 1`.
- **Q4-P18** [A]. *A4.5, first part.* The three-time protocol applies `G` twice: once between `t₁` and `t₂`, and once
  between `t₂` and `t₃`.
- **Q4-P19** [A: the argument below, from `review/REVIEW-PHASE1-r4.md` B1, checked by hand; X:
  `p8_r4rev_membership.py` (6), `p9_r5_symplectic_detector.py`, exhaustive over the 720 × 16 affine-symplectic maps].
  *Q4-D3's affine-symplectic form; R4.9.* On `F_2⁴` with coordinates `(c, x, m, m′)` (location cell, carrier
  conjugate, meter slots) and symplectic pairs `(c, x)` and `(m, m′)`, an affine-symplectic map that is the identity
  on the branch `c = 0` changes no meter slot on the branch `c = 1`. So a detector that interacts only when its cell
  is occupied and records that occupation (changes a meter slot on `c = 1`) lies outside the affine-symplectic class,
  and every affine-symplectic coupling that records occupation acts on its silent branch `c = 0`.
  - Let `T(y) = My + b` be the identity on `{c = 0}`. Then `b = T(0) = 0` and `M e_j = e_j` for `j ≠ c`, so
    `M = I + d e_cᵀ` with `d = M e_c − e_c`.
  - Symplecticity gives `ω(d, e_j) = 0` for `j ∈ {x, m, m′}`, that is `d_c = d_m′ = d_m = 0`.
  - So `d` lies in the span of `e_x`, and on `{c = 1}` the map `y ↦ y + d` changes no meter slot. ∎
  - Exhaustively, none of the 11,520 affine-symplectic maps is the identity on `c = 0` while changing a meter slot on
    `c = 1`; 6 affine bijections that are not symplectic do both.

**Disproved**
- **Q4-D1.** *Claim, as restated:* "Without (H2), a construction reaching the comparator protocol's value
  `K₃ = 3/2` needs a `t₂` read that changes the law of `Q₃`."
  - *Counterexample:* the mixture of Q4-P7. With weight `3/4` on the sharp mediator and `1/4` on the environment
    mediator, A4.1(b)'s witness `G` with an ordinary kicking `t₁` read gives `K₃ = 3/2`, and in every branch the `t₂`
    read's kick does not enter `z₃` (`p6_r3rev_lg.py` (6); `p8_r4rev_membership.py` (5)).
  - *Membership:*
    - `Q = z` is a configuration functional, so (H1) holds.
    - Detector placement is fixed in advance, so (H4) holds.
    - `Q₁` is read by an ordinary kicking read, so (H2) fails, as the claim's class requires.
    - The value is `3/2`, the comparator protocol's maximum.
    - The `t₂` read leaves the law of `Q₃` unchanged in every branch.
  - *Restatement.* The `t₂` read here is an ordinary read, not an INM detector with `K_null = id`. INM detectors are
    not posable in the encoded setting (R4.9). The form of the claim for a genuine INM detector is therefore open
    (Q4-O8).
- **Q4-D2.** *Claim, as restated:* "Every affine-symplectic `G` with translations on two modes, with sharp supplies
  admitted, under A4.1's read model, gives `K₃ ≤ 1`."
  - *Counterexample:* A4.1(b)'s witness `G: z′ = z + v, x′ = w, w′ = z, v′ = x + w`, carrier `X⁺`, mediator `(0, 0)`,
    `K₃ = 2` (P3; `p6_r3rev_lg.py` (5b)).
  - *Membership:*
    - The witness is affine with zero translation, and symplectic for the pairs `(z, x)` and `(v, w)` (checked in
      `p6_r3rev_lg.py` (5b)).
    - It acts on two modes.
    - The mediator `(0, 0)` is a sharp supply, admitted by the claim.
    - The carrier `X⁺` is a half-known supply.
    - The reads follow A4.1's model.
  - Whether `A_4`'s admissible `G` includes this map is not shown, so the claim for `A_4` itself is open (Q4-O6).
- **Q4-D3.** *Claim, as restated:* "A detector that interacts only when its cell is occupied is a controlled coupling
  and lies outside the class of affine maps of `F_2⁴` (not necessarily symplectic)."
  - *Counterexample:* the copy coupling `m ← m + c` (P4(2), P5-LG(1)).
  - *Membership:* the meter changes exactly when the location cell is occupied (`c = 1`), and does not change
    otherwise, so the coupling interacts only when the cell is occupied. The map
    `(c, x, m, m′) ↦ (c, x, m + c, m′)` is linear over `F_2`. The copy coupling is not symplectic for the pairs
    `(c, x)` and `(m, m′)` (`p8_r4rev_membership.py` (6); `p9_r5_symplectic_detector.py`).
  - The claim's affine-symplectic form holds (Q4-P19).
- **Q4-D4.** *Claim:* "`3/2` is the quantum maximum of `K₃` for dichotomic reads, and `K₃ = 2` is supra-quantum, or
  QM-incompatible."
  - *Counterexample:* the measure-and-reprepare instruments of Q4-P9, which give `K₃ = 3` and `K₃ = 2` in QM.
  - *Membership:*
    - The flip instrument has Kraus operators `|1⟩⟨0|` for outcome `+1` and `|0⟩⟨1|` for outcome `−1`. These sum to
      a trace-preserving instrument, and its outcome probabilities are those of a dichotomic `Z` read.
    - The weight-`w` mixture has Kraus operators `√w|1⟩⟨0|` and `√(1−w)|0⟩⟨0|` for `+1`, and `√w|0⟩⟨1|` and
      `√(1−w)|1⟩⟨1|` for `−1`. It is again a trace-preserving dichotomic `Z` read.
    - `G = X` is unitary, the same instrument is used at every time, and each `C_ij` comes from runs reading only at
      `t_i` and `t_j`.

    So both are quantum Leggett–Garg protocols with dichotomic reads. The bound `3/2` holds for the Lüders protocol
    (Q4-P8).
- **Q4-D5.** *Claim:* "Throughout the affine and Clifford classes the correlators lie in `{0, ±1}` at any number of
  modes", with no hypothesis on the preparations.
  - *Counterexample:* `C₁₂ = cos 2θ` (Q4-P4).
  - *Membership:* `CNOT` is a Clifford unitary, the reads are Lüders `Z` reads, and the claim places no condition on
    the preparation, so the non-stabilizer ancilla is admitted.
- **Q4-D6.** *Claim:* "Under the comparator protocol, with more than one mode, a value of `K₃` above 1 needs a
  non-Clifford `G`."
  - *Counterexample:* the comparator protocol reaches `K₃ = √2`, and `7/5` at a rational point, with the two-qubit
    Clifford `G` of Q4-P4 (`p7_r4_lg_order.py`, exact).
  - *Membership:*
    - The reads are Lüders reads of the carrier's `Z`.
    - `G` is unitary and Clifford, as checked in `p7_r4_lg_order.py`.
    - Two modes are present: carrier and mediator.
    - One preparation is non-stabilizer, which the claim admits.
  - The corresponding statement about OI's own value under C-NONSTABILIZER is not refuted. It is open (Q4-O2).
- **Q4-D7.** *Claim:* "NSIT fails (for the given preparation) whenever the `t₂` read does not commute with the evolved
  `Q₃`."
  - *Counterexample:* the maximally mixed preparation, with `G = I` and a Lüders `X` read at `t₂`. `P(z₃)` is `1/2`
    with or without that read (`p6_r3rev_lg.py` (7)).
  - *Membership:* the Lüders `X` read does not commute with `Q₃ = Z`, and the maximally mixed state is a preparation.

**Open**
- **Q4-O1** (AW-QX4-1). Whether `K₃ ≤ 1` holds in the affine-symplectic class for `m > 2` modes and other read models
  under SA-1(c). A proof would establish a property of SA-1(c); it would not justify SA-1(c). A random sample at
  `m = 3` (`p6_r3rev_aw3.py`) finds no counterexample; it is not a proof.
- **Q4-O2** (MECH-OPEN). The value of construction B under C-NONSTABILIZER with an affine `G` on two or more modes.
- **Q4-O3** (MECH-OPEN; R4.9, R4.10). Whether OI's step supplies a location detector, and whether it is null-result
  invasive.
- **Q4-O4** (supported only by D or W records).
  - R4.3's sequential `Z/X` Lüders law at stabilizer scope (AP1 §0 [W]; OICORE-1 §5(b) [D]).
  - The classical two-bit register's `P_succ = 1` (`DESIGN-DS.md` finding 6 [D]).
  - Lemma NC-F (Q-C2-2 [D]).
  - The C-EXPOSURE spectra (cone review [D]).
  - Construction B's adroitness at the ontic level (`DESIGN-DS.md` §1 [D]).
  - A4.5's statement that C-SIZE-DEPENDENT (fixed at `K = 6`) suffices for posing QX-4c (Q-C2-1 [D]).
- **Q4-O5** (L, not read first-hand). For von Neumann reads of a degenerate `Q`, values of `K₃` above `3/2`.
- **Q4-O6.** `A_4`'s value of `K₃`, and the other paper expectations of `A_4`, `B_4-nat` (beyond Q4-P1 and Q4-P2),
  `B_4-C` and the ablations, except those listed as proved above (Q4-P2, Q4-P3, Q4-P6, Q4-P7).
- **Q4-O7.** The converse of Q4-P13's Spekkens et al. direction: whether preparation contextuality of a fragment
  implies `P_succ > 3/4`. No equivalence is asserted (QX-4 §1).
- **Q4-O8.** Q4-D1's claim for a genuine INM detector with `K_null = id` at `t₂`, without (H2).

### 8.3 QX-6

**Proved**
- **Q6-P1** [P: Main §3.3, Main:366-391; the pointwise bound checked exhaustively]. Main's Bell ceiling, under its
  hypotheses (i)–(iv) and with a `±1` outcome in every run. The cone lemma (Main:364) [P].
- **Q6-P2** [A: complete paper proof in QX-6 A6.1; each hypothesis checked against Main:364-391; independently
  reviewed in `review/REVIEW-PHASE1-r3.md` (`448614ea…`); exact checks P5-A61 and `p6_r3rev_a61.py`]. *A6.1.*
  Conditional on (D), (L′), (R) with the `⊥` rule, and (MI): `|S| ≤ 2`.
  - (L′) and (R) are design assumptions of the Bell test, not consequences of OI (§9).
  - The lemma is a paper derivation in these files. It is not on `main` and not kernel-checked.
- **Q6-P3** [A; QX-6 A6.1 table; P5-A61(4); `p6_r3rev_a61.py`].
  - Main's one-step setting form satisfies (D), (L′), (R), the `⊥` rule and (MI).
  - It does not satisfy the single-graph form of (R) in every case (P5-A61(5)).
- **Q6-P4** [A; X: P1, all 60 two-qubit stabilizer states and all 1,080 three-qubit 1+2 states with signed Pauli
  settings; `p6_r3rev_ghz_chsh.py`; Fine's theorem, L]. Stabilizer pair states with Pauli settings give `|S| ≤ 2`.
- **Q6-P5** [A, exact; `p6_r3rev_ghz_chsh.py`].
  - A non-stabilizer pair state with Pauli settings reaches `2√2`.
  - `|Φ⁺⟩` with the stated settings gives `2√2`.
  - The `π/3` comparator gives `S = 5/2`, on the TLM boundary (P1).
- **Q6-P6** [X: P1, P4(3), P5-GHZ, `p6_r3rev_ghz_chsh.py`; computation-supported].
  - GHZ-1's and GHZ-2's QM values and local maxima.
  - GHZ-1's `X/Z` content.
  - The local-Clifford map.
- **Q6-P7** [L, not read first-hand].
  - The CHSH bound and Tsirelson's bound.
  - TLM, each direction separately: (⇒) every quantum correlator quadruple satisfies it (Landau 1987); (⇐) every
    quadruple satisfying it is quantum (Landau 1988; Masanes 2003).
  - Fine's theorem.
- **Q6-P8** [P: Main:418-421]. The measurement-dependence bound `S ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}`, equivalently
  `I_ont ≥ (S − 2)²/(32 ln 2)` for an observed `S > 2`.
- **Q6-P9** [A]. *A6.3.* N2 laws are rational (dyadic at `q = 2` without conditioning), so `2√2` and `±1/√2` are not
  reached exactly.
- **Q6-P10** [A, from Q6-P2; conditional on (L′) and (R)]. *A6.2's "not sufficient"; ABL-NL; ABL-BOT.*
  - Own-wing operations satisfying (L′) and (R) do not exceed 2.
  - A6.1 holds with `⊥ ↦ +1` in (R) replaced by any fixed local rule: the proof is unchanged, since steps 5–6 use
    only that each outcome is a function of its readout region.
- **Q6-P11** [K: COMP-1, a native round whose receipt holds]. The typed composite interface's product laws hold
  without local tomography, at that round's stated scope.

**Disproved**
- **Q6-D1.** *Claim:* "Under (D) with one graph `G` containing every tick's dependency graph, (L) (each setting acts
  only through operations that read and write only its own region), (R) measured in `G`, and (MI), `|S| ≤ 2`."
  - *Counterexample:* P4(1), rebuilt in P5-A61(1) and `p6_r3rev_a61.py`. The one-tick map `op_A ∘ φ ∘ op_B` gives
    the PR box, `S = 4`.
  - *Membership:*
    - (D): the map is deterministic and bijective for every setting, and `G` is the union of its dependency graphs.
    - (L): `op_B` reads and writes only `B`'s region, and `op_A` only `A`'s.
    - (R): in `G`, `d_G(B, R_A) = 1 > T_A − t_B = 0`, and `A`'s region is not connected to `R_B`.
    - (MI): the source variable `λ` is uniform and independent of the settings.
- **Q6-D2.** *Claim:* "A GHZ-type all-versus-nothing contradiction needs `Y` reads."
  - *Counterexample:* GHZ-2, the triangle graph state with `X/Z` reads (P1; P5-GHZ; `p6_r3rev_ghz_chsh.py`).
  - *Membership:*
    - Only `X` and `Z` reads are used.
    - The predictions `+1, +1, +1, −1` for `XZZ`, `ZXZ`, `ZZX`, `XXX` have product `−1`. Any local assignment gives
      the four products a product of `+1`, since each `x_i` and `z_i` appears twice. That is an all-versus-nothing
      contradiction.
- **Q6-D3.** *Claim:* "`X/Z` reads give a GHZ-type contradiction on `(|000⟩ + |111⟩)/√2`."
  - *Counterexample:* the local assignment `x_i = z_i = +1` (P5-GHZ; `p6_r3rev_ghz_chsh.py`).
  - *Membership:* the state is GHZ-1's, the reads are `X/Z` only, and the assignment satisfies every `X/Z` string with
    nonzero expectation on that state (`ZZI`, `IZZ`, `ZIZ`, `XXX`, all `+1`).

**Open**
- **Q6-O1.** H-Bell, the cross-wing response (R6.7).
- **Q6-O2.** The pair source (R6.5).
- **Q6-O3.** Complete-history no-signalling (R6.8) and post-measurement repeatability (R6.11).
- **Q6-O4.** Masking by a restricted preparation class (R6.9; A6.4), including whether ABL-SA1c or ABL-N2 signals.
- **Q6-O5.** Tsirelson soundness (R6.10).
- **Q6-O6.** Local tomography of a constructed composite (R6.12), per-wing access maps (R6.3), and an embedded
  second observer.
- **Q6-O7.** Whether an R60-type operation gives `π/3`-grid local settings (A6.3).
- **Q6-O8** (supported only by W records).
  - The shared-parity candidate's results: `η*`, reuse signalling at `h > 0`, and PR at `η = 0`.
  - The balance-map statements of prepared-pair-source §§4–5, A6.4's "signals iff" (each direction) included.
  - M2D Theorems U2 and NC.
- **Q6-O9.** A6.4's §A.31 corollary, "non-equilibrium supplies signal".
- **Q6-O10.** The paper expectations of `B_6-nl` and of the ablations, except those in Q6-P10.

### 8.4 This file

- **Proved.**
  - T6's rationality statement [A, as Q6-P9].
  - §3's Bell statement for constructions satisfying A6.1's hypotheses, conditional on the design assumptions (L′)
    and (R) (Q6-P2).
  - §3's routing statements (Q3-P4 to Q3-P6a).
  - §3's "Counting" necessity statements, each with its condition: M12 for QX-4c's QM-matching value with stabilizer
    preparations (Q4-P3) and for QX-6's QM-matching settings with stabilizer pair states (Q6-P4); under (D) and (MI),
    a failure of (L′) or (R) for `|S| > 2` (Q6-P2), which, with the design excluding failures of (L′) and
    insufficient separation, is a cross-wing coupling path (QX-6 §3.2); M18 and M14 by the protocols' definitions
    (QX-6 §1; QX-3 §8; QX-4 R4.9).
- **Disproved.** None beyond §§8.1–8.3.
- **Open.**
  - The M-rows' availability claims that rest on Q-C2-1 or OICORE-1 drafts [D] or reconstruction records [W].
  - H-SDC, which is named only.
  - The T-rows' sourced statements, as classified at their sources.
  - Whether the minimal premise count of §3 can be reduced.
  - §3's "Counting": the necessity of M12 for QX-1, QX-5 and QX-7, whose support is Q-C2-1 and Q-C2-2 drafts [D].

## 9. Restrictions and their reasons

**Three questions, answered separately for each restriction:**
- (i) Is the restriction mathematically well-defined?
- (ii) Does it follow from OI's independently justified principles?
- (iii) Does it reproduce the relevant quantum predictions, and under which comparator protocol?

A positive answer to (iii) does not establish (ii), and column (iii) is never cited as support for column (ii).

**Answers.**
- In (ii), "none identified" counts as open.
- A restriction whose only identified support is agreement with QM is a hypothesis under test, not a requirement. It
  is marked **QM-only** in the last column. SA-1(c), null-result invasiveness and Tsirelson soundness are carried as
  hypotheses under test in #1210's dependency table (decision O1: #1210 c.6738866690, amaybaum,
  2026-11-09T11:25:06Z; confirmed at c.6739250392).
- A protocol or comparator declaration constrains how an experiment is run or credited, not OI's laws. Its column
  (ii) answers no and records the reason it is adopted.
- Column (iii) reads "not applicable" where the restriction makes no quantum prediction by itself.

| restriction | where used | (i) well-defined? | (ii) follows from independently justified OI principles? | (iii) reproduces the relevant QM predictions? (comparator) | standing |
| --- | --- | --- | --- | --- | --- |
| SA-1(a): reciprocal coupling through the native second-order step | QX-0; QX-3 A3.2; QX-4 R4.3; M15 | yes (AP1:282-287) | yes, conditional on Substratum (A4)–(A5), with (A5)'s restriction to linear "imposed" and (A5) "partly derived" (Substratum:98, :100): the step's form, symmetry and symplecticity are native for the wave branch on that condition (AP1:286-287, :313-320; Substratum:48) | yes, together with SA-1(b) and (c), for the stabilizer-scope sequential `Z/X` law (AP1 §0 [W]; comparator: Pauli Lüders instruments on a qubit, AP1 ledger I1) | native element |
| SA-1(a′) and E-iso: per-tick, per-edge arming and decoupled cells | every setting switch; P3 | yes (AP1:288-291, :305-309) | no. "Per-tick, per-edge arming is not native" (AP1:290-291), and E-iso "is not derived" (AP1:309). The stated reason is operational: a setting selection needs a switch | not applicable (a control posit) | posit; in tension with FIX (T3) |
| SA-1(b): terminal registration | every read | yes (AP1:292-296) | open. Motivation: Main's Definition makes the observer a subsystem coupled through `φ` (Main:44; AP1:328-336), and terminality is the counterpart of an archived record. "The native dynamics does not enforce terminality" (AP1:338) | yes, with SA-1(a) and (c), at stabilizer scope (AP1 [W]; comparator as above) | posit (AP1 ledger P1); an idealization below recurrence |
| SA-1(c): half-known ready cells (M3) | QX-0 universality; QX-3 `V`; QX-4 backaction; R6.9 candidate | yes (AP1:297-299) | open; none identified. "Clause (c) is not derived. Its motivation is closure plus the E-AR obstruction, and the latter is a programme-internal reason" (AP1:347-349). Closure (Lemma 3) shows that (a) and (b) preserve (c), which is consistency, not a reason it holds. The E-AR obstruction is the absence of a finite-dimensional quantum carrier with sharp cells (AP1:221, :677), which is agreement with QM and is not usable here. In the cited literature the analogous restriction is a postulate (AP1:356-361) | yes at stabilizer scope (AP1 Lemma 4 [W]; comparator: Pauli Lüders instruments on a qubit). In QX-4 it coincides with `K₃ ≤ 1` at the scanned scope (AW-QX4-1) | **QM-only**: a hypothesis under test, not a requirement |
| N2: the uniform law on unknown slots | everywhere | yes (AP1:416) | yes for the counting measure, Main's maximal-entropy selection, "a selection principle, not uniqueness from invariance alone" (Main:56, Lemma 3). Open for its application to supplied ready cells, which goes through H-PREP (AP1:350-355) | yes at stabilizer scope, with SA-1 (AP1 [W]); no for irrational quantum values, since the laws are rational (T6) | native measure; application conditional on H-PREP |
| H-PREP: a laboratory preparation law is the in-realization conditional of the measure | preparations | yes as stated (AP1:417) | open: a named hypothesis, not adopted (AP1:417) | not applicable (an identification) | open hypothesis |
| `NCONS` domain: `NCONS_ready` or `NCONS_global` | QX-3 R3.6, A3.1 | yes (QX-3 §1) | open; none identified for `NCONS_global`. `NCONS_ready` is a property of the admitted supplies, not a law | on the ready support both domains give `α = 0` under routing (A3.1(b)–(c)); `V` is open. The comparator, a Fock-1 source in the Hanbury Brown–Twiss arrangement, does not separate the two domains | owner question Q3-2 |
| the local `⊥ ↦ +1` rule | QX-6 `S` | yes (QX-6 §1) | no: a protocol declaration, not an OI principle. Its reason is that Main's theorem requires a `±1` outcome in every run (Main:376-377), and the rule supplies one as a function of each wing's own records. It makes an excess over 2 harder, not easier | not applicable to the ideal comparator, which has no `⊥` | protocol (Q6-5) |
| full-mass accounting; conditioning only on a setting-independent herald registered before the setting | QX-3, QX-6 | yes (QX-3 §1; QX-6 §1) | no: a protocol declaration, not an OI principle. It excludes post-selection and detection loopholes | not applicable | protocol |
| measurement independence (MI; Main (iv)) | QX-6 A6.1 | yes (Main:374-376) | no: "retained as a posit about the initial condition, not derived" (Main:406-412) | not applicable; it bounds local completions at 2 | posit, in Main |
| (L′) and (R) of A6.1 | QX-6 R6.2, R6.4 | yes (QX-6 A6.1) | no. These are design assumptions of the Bell test: own-wing settings and separation. They are not consequences of OI. OI's chosen branch (a) gives up Main's (ii) and (iii), of which (L′) and (R) are the generalizations (Main:403-406, :414), and H-Bell's preparation-indexed long edges are a failure of (R) (QX-6 §3.2) | not applicable; they bound `|S| ≤ 2` | design assumptions (protocol). A6.1 is proved conditional on them |
| D15 access class `Acc` (B-P), and per-wing access maps | QX-0 B; QX-4b; QX-5; QX-6 R6.3 | yes for D15 option (a) (`DECISIONS.md` D15 [D]); the per-wing maps are supplied abstractly (two-system interface §2 [W]) | open. Typed CS by the owner (c.6735014875). Its content is the SA-1(b) registrations, so it carries SA-1(b)'s status. No derivation beyond `V ⊊ S` (Main:50, Lemma 2) is identified | not applicable. An access restriction can manufacture contextuality or no-signalling (T5), so it is reported `access_only` | CS |
| preparation class fixed by the balance equations (R6.9) | QX-6 | yes for a fixed realization (prepared-pair-source §4 [W]) | open; none identified. A class defined only by the balance equations is fitted to no-signalling | no-signalling, by its definition. Tsirelson soundness does not follow (R6.10) | hypothesis under test; creditable only if fixed in advance by an independent principle with a consequence of its own (§A.29) |
| complete-history no-signalling (R6.8, M20) | QX-6 | yes (QX-6 §1; NO-SIGNALLING.md §1 [W]) | open. It is a requirement of the framework's chosen branch, "with operational no-signaling required" (Substratum:467; Main:414), stated and not derived | yes: local instruments on any bipartite state satisfy it (two-system interface eq. (14) [W]) | requirement of the chosen branch, not derived |
| Tsirelson soundness (R6.10, M20) | QX-6 | yes | open; none identified. "Bare C1–C4 or graph locality do not enforce Tsirelson" (Substratum:481) | yes: `|S| ≤ 2√2` for every bipartite tensor-product quantum strategy (L) | **QM-only**: a hypothesis under test |
| null-result invasiveness of INM detectors (M16, R4.10) | QX-4 INM | yes (`K_null ≠ id`; QX-4 §1) | open; none identified | yes: given (H1), (H2) and (H4), it is needed to match QX-4c's comparator protocol under INM (A4.4) | **QM-only**: a hypothesis under test |
| reciprocity of detector couplings (M15) | QX-0, QX-3, QX-4 | yes (QX-3 A3.2) | conditional: yes in the affine-symplectic class, from SA-1(a)'s step, on the same condition as the SA-1(a) row; the support is a W record (AP1:313-327 [W]). Open for non-affine rules, since `G_SM` is not reciprocal (M2D [W]) | preserves QX-0's complementarity reading | a control from an existing result (§A.29) |
| (H1)–(H4) of A4.4 | QX-4 INM | yes (QX-4 A4.4) | (H1) is an IR identification of `Q` with a configuration functional, open (via L-CAL and L-UPRIME under D18(a)). (H2) and (H4) are protocol conditions taken from the cited INM experiments (L). (H3) is the hypothesis under test | not applicable | protocol and identification hypotheses |
| FIX: one fixed law | every experiment | yes (OICORE-1 §2 [D]) | yes: Main's Definition has one dynamics `φ` (Main:44) | not applicable | programme rule |
| L-PATH, L-PORT, L-CAL, L-UPRIME | every experiment | yes (Q-C2-1 ledger [D]) | no: representation choices, not OI principles, typed IR under D18(a), conditional (c.6735014875), with a check that none introduces quantum dynamics, probabilities or desired outcomes | L-PORT fixes `α = 0` in the encoded setting by identification, so `B_3-enc` is not credited | IR; ledger and REP-INV |
| L-CLICK | QX-3 R3.5 | yes (QX-3 R3.5) | open: owner typing pending (Q3-3) | with routing, own-cell clicks give `α = 0` (A3.1(b)) | IR candidate; REP-INV test |
| QX-4c's comparator protocol and crediting window `(1, 3/2]` | QX-4 §§2, 8 | yes (QX-4 §2) | no: not an OI restriction; it defines the QM comparator and what is credited. Values outside the window are reported | by definition | comparator declaration |
