# QPHEN Phase 1: the shared-mechanism requirements matrix (QX-0 to QX-7)

## 0. Standing

- **Authority.** #1210 Phase 1, paper only (c.6736966265).
- **Status.** Model-written and awaiting independent review. No mechanism is built, no computation is run, no
  criterion is frozen and no premise is adopted.
- **Conventions.** The evidence layers and requirement types are as in `QX3-ANTIBUNCHING.md` §0.
- **What this file does.** It maps, for each experiment, the capabilities an OI construction would need, and
  states the smallest set one construction would need in order to serve all eight.
- **Inputs.**
  - The three Phase 1 specifications: `QX3-ANTIBUNCHING.md`, `QX4-INCOMPATIBILITY-LG.md` and `QX6-BELL-CHSH.md`.
  - Q-C2-1 drafts r12/r13 [D] for QX-0, QX-1, QX-2 and QX-7.
  - Q-C2-2 r13 [D] for QX-5.
  - OICORE-1 r6 [D].
  - The corpus at `fd539e15`.
- **Programme rule.** One shared mechanism. Every extension is justified independently, reviewed, and evaluated for
  its effect on earlier experiments (#1210 programme requirement 1).

***

## 1. Capabilities

| id | capability | type and status |
| --- | --- | --- |
| M1 | one bijective second-order step on finite cells (L-BIJ, L-SYM, L-SYMP) | EN |
| M2 | probabilities from configuration counting (N2) | CS. Close to native for `H`, supplied for apparatus cells. Gives dyadic rationals only |
| M3 | epistemic supply restriction: half-known ready cells (SA-1(c)) | CS, posited and not derived (AP1:347). It carries complementarity's universality in QX-0 (D) |
| M4 | known-value and QA-family preparations (H-PREP) | CS, open hypothesis |
| M5 | meters with terminal registration (SA-1(b)) | CS (RET-s: an idealization below recurrence) |
| M6 | setting switch: per-tick, per-edge arming with isolation (P3, E-iso) | CS, in tension with FIX. A dynamics row (Q-C2-1 R7-B2). The FIX alternative is NR-16 |
| M7 | held, unread records and forward conditioning (RET-w; L-HOLD, L-FWD) | retention EN; isolation and conditioning CS |
| M8 | an owner-typed observer access class with a completeness check (L-ACC; D15) | CS. ACC_op's consistency with the core is open (OICORE-1 §3.2) |
| M9 | representation identifications: path, port, frame, U′ functionals, click (L-PATH, L-PORT, L-CAL, L-UPRIME, L-CLICK) | IR, owner-typed under D18 and REP-INV-tested |
| M10 | phase settings `{0, π}` | EN step; CS supply |
| M11 | quarter phase and `Y` read (NNB on U′) | a supplied conditional premise. Not native under one-cell identification (AP1 Lemma 5) |
| M12 | one fixed non-Clifford operation on an encoded carrier | **MC**: Obligation C / OICORE-1's drive clause. Open (OICORE-1 §8.10) |
| M13 | repeated composition of a fixed operation | MC (C's horizons `K ∈ {6, 12}`) |
| M14 | number-conserving routing, with location-reading detectors | NX: non-affine, classical reversible (QX-3 A3.1) |
| M15 | reciprocal detector coupling, kept under any non-affine extension | a constraint, needed to preserve QX-0 (QX-3 A3.2) |
| M16 | null-result invasiveness of location detectors (`K_null ≠ id`) | an NX constraint (QX-4 A4.4) |
| M17 | two-system composite: cone separation, per-observer access maps, local tomography | cone lemma P (Main §3.3); access maps CS (supplied abstractly, W); local tomography carried as a hypothesis (COMP-1) |
| M18 | pair source | NX. Absent (prepared-pair-source (W)). Inside M2D U2's scope no entangling operation exists (W) |
| M19 | ontic parameter dependence: cross-wing response through preparation-indexed adjacency | CS as named open hypothesis H-Bell, dynamics type (Substratum:131) |
| M20 | complete-history no-signalling and Tsirelson soundness over the admitted preparation class | constraints. Open; failed by the only explicit candidate (W) |
| M21 | the validation layer: `D`, `K`, `K_null`, NONABS, SPI, STAB, NCONS, cone distances, MI | method: construction-internal, never observer data, and never an import of quantum behaviour |
| M22 | exact LP noncontextuality method: Farkas certificates, Lemma NC-F, attributed completions | method (Q-C2-2 [D]) |
| M23 | exchange symmetry of identical excitations | NX. Absent from the corpus |

## 2. Requirements matrix

Legend:
- **R**: required for the experiment's discriminating (Level ≥ 2) form;
- **r**: required for its Level-1 or reduced form;
- **?**: depends on a pending owner decision or an optional variant;
- **·**: not needed;
- **b**: benchmark only (IQ).

| | QX-0 which-path | QX-1 superposition and recombination | QX-2 eraser | QX-3 antibunching | QX-4 incompatibility / LG | QX-5 contextuality | QX-6 Bell | QX-7 composition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1 step | R | R | R | R | R | R | R | R |
| M2 N2 | R | R | R | R | R | R | R | R |
| M3 SA-1(c) | R (universality) | r | R | r (`V` half) | R (backaction) | R (P2 inputs) | ? (masking, R6.9) | r |
| M4 H-PREP | R | R | R | R | R | R | R | R |
| M5 SA-1(b) | R | R | R | R | R | ? (reads) | R (per wing) | R |
| M6 P3 / E-iso | R (detector switch) | R | R | R | R | ? | R (settings) | R |
| M7 held records, conditioning | R (`D`) | r | R | r (herald) | r | R (heralds) | R (histories) | r |
| M8 typed access class | R (B-P) | · | r | · | R (4b) | R | R (per wing) | r (B-C) |
| M9 identifications | R | R | R | R (+ L-CLICK) | R | R | R | R |
| M10 `{0, π}` | R | r | R | R | r | r | r | r |
| M11 quarter phase / `Y` | ? (D4) | ? | · | · | ? | ? (spanning) | ? (GHZ option) | r (`Λ_{y,b}`) |
| M12 non-Clifford operation | · | R | · | · (only R3.8) | R (4c, and 4b's quantum value) | R (beyond stabilizer) | R for QM-matching settings, not sufficient (A6.2) | R |
| M13 repeated composition | · | R | · | · | r (2 applications, A4.5) | · | r | R |
| M14 routing | ? (NR-13) | · | · | R | R (INM) | · | · | · |
| M15 reciprocity kept | R (control) | · | R | R | R | · | r | · |
| M16 null-result invasiveness | · | · | · | · | R (INM) | · | · | · |
| M17 composite | · | · | · | ? (W3) | · | · | R | ? (NR-11) |
| M18 pair source | · | · | · | ? (W3) | · | · | R | · |
| M19 cross-wing response | · | · | · | · | · | · | R | · |
| M20 no-signalling, Tsirelson | · | · | · | · | r (NSIT reported) | · | R | · |
| M21 validation layer | R | R | R | R | R | R | R | R |
| M22 LP method | R (Test B) | · | · | · | R (4b) | R | ? | r (B-C) |
| M23 exchange symmetry | · | · | · | ? (W3) | · | · | · | · |
| imported (IQ) only in a benchmark | QM-P comparators | supplied gates | QM comparators | Fock-1 law | supplied `π/3` rotation | QM fragment | calibrated `η*`, supplied pair | supplied gates |

## 3. The minimal set for one construction serving all eight

**Core (in every column).** M1, M2, M4, M5, M6 or its FIX-compatible replacement, M9 typed under D18, and M21.

**Epistemic restriction and access, with no dynamics credit.** M3, M7 and M8.
- In the current construction these carry four things:
  - complementarity's universality (QX-0);
  - backaction (QX-4a);
  - the fragment of every contextuality test (QX-0 B, QX-4b, QX-5);
  - the only candidate for no-signalling masking in a parameter-dependent Bell completion (QX-6 A6.4).
- M3 is the single most cross-cutting B principle and is posited, not derived.
- Its ablation is predicted to change predictions in QX-0, QX-4 and QX-6.

**One fixed non-affine rule (dynamics) that supplies:**
- M12 and M13, Obligation C;
- M14 under the constraints M15 and M16;
- consistency with QX-5's fragment.

There are at present **three distinct non-affine rules** in play:
- C's gadget rules `g ∈ {AND, NAND, OR, NOR}` (Q-C2-1 [D]);
- `G_SM`, SM's state-dependent ring rule, used by Q-C2-2 and M2D. It is a stated hypothesis in SM and not
  physically sourced. Its edges are not reciprocal for `L ≥ 5` (M2D §0 item 1 (W));
- QX-3's routing (controlled swap; NX).

Under FIX one rule must serve all three roles, or each further rule is a separate extension with its own
justification and its own evaluation against QX-0.

**Two-system structure (QX-6, and options in QX-3 and QX-7).** M17 and M18.

**Cross-wing dynamics (QX-6 only).** M19 under M20.
- This is the one capability whose necessity follows from a result on `main` rather than from the current toolkit's
  limits.
- By Main §3.3's theorem, no construction made of access restrictions, state restrictions on a setting-independent
  ensemble, or local operations, M12 included, exceeds `|S| = 2` under full-mass accounting (QX-6 A6.1).

**Counting.** Construction B's present principles (M3–M8) supply none of M12, M14 and M19. A construction serving all
eight therefore needs, at minimum:
- a coherent-mixing resource (M12);
- dynamically generated exclusivity (M14);
- a cross-wing response with no-signalling masking (M19 with M20);
- a pair source (M18).

Whether these can be fewer than four independent premises is open. The hypothesis below names one way they could
coincide.

**H-SDC (named only; not adopted, not typed, not evaluated).**
- **Statement.** One fixed state-dependent-coupling rule, in the sense of SM's `G(x)` (SM §3.1; Substratum:131),
  supplies M12 through its non-affine encoded action, M14 through state-controlled routing, and M19 through
  preparation-indexed long edges.
- **Motivation.** `G_SM` is SM's example of state-dependent geometry. Preparation-indexed adjacency is OI's proposed
  Bell escape. Routing is state-controlled coupling.
- **Productivity test (§A.31).** It counts only if one rule, fixed in advance with its identifications and reads, does
  all three. Describing three mechanisms as "some nonlinear coupling" is relabelling, not a result.
- **Known obstacles, stated first because the reading is favourable to the framework:**
  1. Non-affine rules need not be symplectic or reciprocal. `G_SM`'s edges are not reciprocal, so QX-0's backaction
     mechanism and its complementarity are not guaranteed (M15).
  2. Under `STAB(K)`, C-type positives have rotation orders 3 or 6 only (cone review [D]). Any LG or Bell use is then
     restricted to the `π/3` grid (QX-4 A4.6; QX-6 A6.3).
  3. M2D Theorem U2 (W) bars entangling encoded unitaries for every fixed bijection under R1^⊗n and H-LIFT, so M18
     must come from outside that scope.
  4. The rule must exclude PR-type responses (M20). No principle bounding `S` at `2√2` is known.
  5. H-Bell is recorded as downstream of an unmet curvature re-founding obligation (ROADMAP:764-769).

## 4. Cross-experiment tensions an extension must be evaluated against

| # | tension | experiments | source |
| --- | --- | --- | --- |
| T1 | Routing (M14) lets a detector record the path without the kick, which would make QX-0 report P-RECORD-WITHOUT-SUPPRESSION unless reciprocity (M15) is kept | QX-0, QX-3 | QX-3 A3.2 |
| T2 | An INM detector must act on its silent branch (M16), or OI's own ontic model obeys the INM Leggett–Garg bound. The routing coupling must carry an outcome-independent kick | QX-3, QX-4 | QX-4 A4.4 |
| T3 | P3 arming is the setting switch for every experiment but is in tension with FIX | all | `DESIGN-DS.md` §2 [D]; OICORE-1 §2 |
| T4 | Three different non-affine rules are in use (§3) | QX-1, QX-3, QX-5, QX-7 | Q-C2-1, Q-C2-2, M2D |
| T5 | An access restriction can manufacture no-signalling (QX-6) or contextuality (QX-0 B, QX-4b, QX-5). It must be reported `access_only` and never credited with dynamics | QX-0, QX-4, QX-5, QX-6 | owner c.6734374076; Q-C2-1 r6 B3 [D]; NO-SIGNALLING.md item 5 (W) |
| T6 | N2 gives dyadic probabilities, so irrational targets (`2√2`; PO-RAC `(1 + 1/√2)/2`) are unreachable exactly. Witnesses and comparators must be stated at rational settings, with exact decision procedures | QX-4, QX-6 | QX-4 §7; QX-6 A6.3 |
| T7 | L-PORT fixes the encoded anticorrelation and must not be credited as dynamics | QX-0, QX-3 | `DESIGN-DS.md` §5 finding 5 [D] |
| T8 | OI is a macrorealist-per-se, invasive, epistemically restricted model. No witness in QX-0 to QX-4 excludes that class. Only QX-5 (over a typed fragment) and QX-6 (local hidden variables) reach beyond it, and QX-6 does so only with a nonlocal response | all | QX-3 §2; QX-4 §2; QX-6 §2 |

**Controls an extension must preserve** (§A.29, as the extension's own controls):
- QX-0's P-COMPLEMENTARITY existence and universality readings, if Q-C2-1 returns them;
- `K₃ ≤ 1` for the affine sub-case (QX-4 A4.1);
- Main §3.3's Bell ceiling for local constructions;
- C's ABL: affine rules give no W-CL;
- Lemma P and Theorem C within their scopes;
- ARP-1-MARC's SURVIVAL within its scope;
- OICORE-1's Lemma M: restrictions alone with the core force no control.

## 5. Dependency refinements proposed for #1210's table (planning input only; no Issue edit made)

| ID | as recorded | proposed refinement (for the owner's decision) |
| --- | --- | --- |
| QX-3 | blocked: QX-0 review | W1 and W2 are independent of Obligation C. They need M14 (a non-affine routing extension) and the M15 control. W2's best case excludes classical fields only |
| QX-4 | blocked: QX-0 | 4a is posable on Q-C2-1's apparatus (Level 1). 4b belongs with QX-5. 4c needs C-EXPOSURE or C-SIZE-DEPENDENT (A4.1, A4.5), and its INM variant needs M14 and M16 |
| QX-6 | blocked: QX-1 | QX-1 / Obligation C is necessary for QM-matching local settings but not sufficient (A6.2). The binding prerequisites are a pair source (M18), H-Bell's cross-wing response (M19) and complete-history no-signalling (M20), none of which any Q-C2-1 outcome supplies |
| QX-5, QX-7 | per ARP order; blocked: QX-0 | T4: the rule used by QX-5 (`G_SM`) differs from C's gadget rules. Selecting a shared mechanism needs one rule |

## 6. Common reporting schema (outline; not frozen)

For every experiment and every ablation:
- **`pred_change`** (computed): whether the reachable detector-record observables change;
- **`mech_change`** (computed): whether the validation-layer cells' realizing mechanisms change;
- **`access_only`** (computed): whether the full world laws are identical, with only the registered or unread records
  differing;
- **`dynamics_credit`** (the row's kind): a state or access restriction is never credited with new dynamics.

Also reported for every experiment:
- the classical classes each witness excludes, and those it does not;
- the Level, with no level awarded from a lower one;
- the REP-INV status of each identification.

## 7. References to content off `main`

The three specifications' §10–§11 tables apply. Every Q-C2-1, Q-C2-2 and OICORE-1 citation is an off-`main` draft (D),
used as a planning input and not as an established premise. AP1, M2D and the oi-qm-ext-1 records are on `main` (W),
model-reviewed, and conditional on their stated hypotheses (§A.46 item 7).
