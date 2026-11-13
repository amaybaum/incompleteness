# QPHEN Phase 1: the shared-mechanism requirements matrix (QX-0 to QX-7) (draft r2)

## 0. Standing

**Authority and status.**
- #1210 Phase 1, paper only (c.6736966265).
- Model-written. No mechanism is built, no computation is run, no criterion is frozen, and no premise is adopted.

**Revisions.**
- r1 is `r1/SHARED-MECHANISM-r1.md` (`5b07a5b9…`). It was reviewed REVISE in `review/REVIEW-PHASE1.md` (`8d704712…`).
- r2 propagates B1–B5 and applies N8, N9, N11 and N12. Dispositions are in `DISPOSITIONS-r2.md`.

**Conventions.** Evidence layers, types (EN, CS, IQ, IR, untyped) and dependencies (MC, MECH-OPEN, —) are as in
`QX3-ANTIBUNCHING.md` §0 (r2).

**Inputs.**
- The three Phase 1 specifications (r2).
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
| M2 | probabilities from configuration counting (N2) | CS | — | available; dyadic rationals only |
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
| M16 | null-result invasiveness of location detectors (`K_null ≠ id`) | constraint | MECH-OPEN | required for INM agreement with QM under QX-4 A4.4's hypotheses (H1), (H2), (H4) |
| M17 | two-system composite: cone separation, per-observer access maps, local tomography | cone lemma P (Main §3.3); access maps CS (supplied abstractly, W); local tomography a hypothesis (COMP-1) | — | partial |
| M18 | pair source (two-party; three-party for the GHZ-type option) | untyped | MECH-OPEN | absent (prepared-pair-source (W)); no entangling operation within M2D U2's scope (W) |
| M19 | cross-wing response (ontic parameter dependence; preparation-indexed adjacency) | CS as the named open hypothesis H-Bell (dynamics) | MECH-OPEN | open (Substratum:131) |
| M20 | complete-history no-signalling and Tsirelson soundness over the admitted preparation class | constraints | MECH-OPEN | open; failed by the only explicit candidate (W) |
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
| M3 SA-1(c) | R (universality) | r | R | r (`V` half) | R (backaction; AW-QX4-1) | R (P2 inputs) | ? (R6.9 candidate) | r |
| M4 H-PREP | R | R | R | R | R | R | R | R |
| M5 SA-1(b) | R | R | R | R | R | ? (reads) | R (per wing) | R |
| M6 P3 / E-iso | R (detector switch) | R | R | R | R | ? | R (settings, inside each wing; A6.1) | R |
| M7 held records, conditioning | R (`D`) | r | R | r (herald) | r | R (heralds) | R (histories) | r |
| M8 typed access class | R (B-P) | · | r | · | R (4b) | R | R (per wing) | r (B-C) |
| M9 identifications | R | R | R | R (+ L-CLICK) | R | R | R | R |
| M10 `{0, π}` | R | r | R | R | r | r | r | r |
| M11 quarter phase / `Y` | ? (D4(a)) | ? | · | · | ? | ? (spanning) | · (the GHZ-type option uses `X/Z` reads; QX-6 §2) | r (`Λ_{y,b}`) |
| M12 non-Clifford operation | · | R | · | · (only R3.8) | R (4c's QM-matching value; 4b's quantum value) | R (beyond stabilizer) | r (QM-matching settings with stabilizer pairs; not sufficient; A6.2) | R |
| M13 repeated composition | · | R | · | · | r (2 applications; A4.5) | · | r | R |
| M14 routing | ? (NR-13) | · | · | R | R (INM) | · | · | · |
| M15 reciprocity kept | R (control) | · | R | R | R | · | r | · |
| M16 null-result invasiveness | · | · | · | · | R (INM, under H1, H2, H4) | · | · | · |
| M17 composite | · | · | · | ? (W3) | · | · | R | ? (NR-11) |
| M18 pair source | · | · | · | ? (W3) | · | · | R (three-party for GHZ-type) | · |
| M19 cross-wing response | · | · | · | · | · | · | R | · |
| M20 no-signalling, Tsirelson | · | · | · | · | r (NSIT reported) | · | R | · |
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
- Main §3.3 covers one-step own-wing settings. This programme's extension A6.1 [A, unreviewed] covers multi-tick
  own-wing operations and arming inside each wing, with a declared local `⊥ ↦ +1` rule.
- Under those hypotheses, constructions built only from access restrictions, state restrictions on a
  setting-independent ensemble, own-wing local operations (M12 included) and local registration rules do not exceed
  `|S| = 2`.
- M19 is itself a candidate OI principle (H-Bell), and A6.1 does not cover it.

**Counting.**
- Construction B's present principles (M3–M8) supply none of M12 or M19, and M14 only if an affine router is admitted
  and supplied.
- A construction serving all eight therefore needs, at minimum:
  - a coherent-mixing resource (M12);
  - a cross-wing response with a no-signalling mask (M19 with M20);
  - a pair source (M18);
  - a routing element (M14), which may or may not be a further non-affine premise, depending on Q3-2 and MECH-OPEN.
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
| T2 | With `Q₁` fixed by preparation from a setting-independent supply, placement independent of the ontic state, and `Q` a configuration functional (IR), an INM detector must act on its silent branch (M16). Otherwise construction B's ontic model obeys the INM bound against QM. The routing coupling must keep an outcome-independent kick | QX-3, QX-4 | QX-4 A4.4 (H1)–(H4) |
| T3 | P3 arming is every experiment's setting switch but is in tension with FIX. A6.1 admits it in QX-6 only inside each wing | all | `DESIGN-DS.md` §2 [D]; OICORE-1 §2 [D] |
| T4 | Two non-affine rules are in use (C's gadget rules; `G_SM`). Routing adds a third only under `NCONS_global` | QX-1, QX-3, QX-5, QX-7 | Q-C2-1, Q-C2-2, M2D; QX-3 A3.1 |
| T5 | An access restriction can manufacture no-signalling (QX-6) or contextuality (QX-0 B, QX-4b, QX-5). It is reported `access_only` and never credited with dynamics | QX-0, QX-4, QX-5, QX-6 | owner c.6734374076; `DESIGN-DS.md` §5 finding 6 [D]; NO-SIGNALLING.md item 5 (W) |
| T6 | N2 gives dyadic probabilities, so irrational targets (`2√2`; PO-RAC `(1 + 1/√2)/2`) are exactly unreachable. Comparators sit at rational settings, with exact decision procedures; TLM is exact on correlators only | QX-4, QX-6 | QX-4 §7; QX-6 §1, A6.3 |
| T7 | L-PORT fixes the encoded anticorrelation and is not credited as dynamics | QX-0, QX-3 | `DESIGN-DS.md` §5 finding 5 [D] |
| T8 | Construction B, given SA-1(c) (CS) and the IR premise that the read quantity is a configuration functional, is a macrorealist-per-se, invasive, epistemically restricted model. No witness in QX-0 to QX-4 excludes that class. QX-5 does so only over a typed fragment. QX-6 excludes local hidden variables, and only with a cross-wing response | all | QX-3 §2; QX-4 §2, §7; QX-6 §2 |
| T9 | With a sharp supply, the affine-symplectic class reaches the supra-quantum `K₃ = 2`. Admitting sharp supplies (dropping SA-1(c)) can therefore make a construction QM-incompatible in QX-4 | QX-0, QX-4 | QX-4 A4.1(b); AW-QX4-1 |

**Controls an extension must preserve** (§A.29; the extension's own controls):
- QX-0's P-COMPLEMENTARITY existence and universality readings, if Q-C2-1 returns them.
- `K₃ ≤ 1` at one mode, and at two modes under SA-1(c) or environment supplies (QX-4 A4.1(a)–(b); the latter a scan).
- Main §3.3's Bell ceiling, with A6.1's extension, for local constructions under the `⊥` rule.
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
  - W2's best case excludes classical fields only.

**QX-4**
- Recorded: blocked: QX-0.
- Proposed:
  - 4a is posable on Q-C2-1's apparatus, at Level 1.
  - 4b belongs with QX-5.
  - 4c's QM-matching value needs C-EXPOSURE or C-SIZE-DEPENDENT (A4.1(c), A4.5).
  - The INM variant needs M14 and M16 under (H1)–(H4).
  - AW-QX4-1 is recorded.

**QX-6**
- Recorded: blocked: QX-1.
- Proposed:
  - QX-1 / Obligation C is needed for QM-matching settings with stabilizer pair states, and is not sufficient (A6.2).
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
| M2D; AP1; oi-qm-ext-1 records; ARP-1-MARC result | §§1, 3, 4 | on `main` (W, or a native round), conditional on their stated hypotheses (§A.46 item 7) |
