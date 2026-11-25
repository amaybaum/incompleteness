# U4 source inventory, r1

**Purpose.** Read-only source inventory for unit U4 of S3-PLAN-r9 (route M, D-1, SNR-1, H-RR recording
side, and the parked-record hypothesis). It lists and locates sources. It draws no conclusions, assesses
no correctness, and does not start U4. U4 waits for U1 acceptance.

**Authorization.** Owner (`amaybaum`), #1169 c.6891189024 (2026-11-15T07:39:57Z), item 5: "read-only
source inventory for U4 ... It draws no conclusions and does not start U4."

**Scope of U4 being served.** S3-PLAN-r9 (PR #1294 head `bfad2731`, blob `46ebc72d`, accepted in
#1169 c.6890079967 decision B): §8 route M, §8.4 checks 1–7 (D-1), §8.5 controls, §8.6 SNR-1 and
closure, §4.1 H-RR, §9 row U4. Owner decision A (#1169 c.6890079967): "a which-path record is
temporarily retained in the hidden sector and later becomes accessible again. U4 examines what this
would imply for interference and distinguishes it from quantum revivals in finite environments. No
mechanism is assumed or established."

**Base.** `origin/main` = `75cc51009aebcfb17c1bbf76d149760c540aac3b` (2026-11-15, merge of #1304).
All `path:line` citations without a commit are at this commit. Branches read by name only:
`research/ro3-carrier-inventory-1055-20261114` (`78089e5e`), `research/codex-native-apparatus-20261113`
(`7086bd30`), `research/oiqm-sel-excl1-20261110` (contains `0ecfddeb`),
`research/ro1-sector-c-1169-20261114` (`3ec1e465`). Issues and PRs were read through the GitHub API on
2026-11-15.

**Status labels** (§A.42 item 8, §A.46 item 7). These record where an item lives and how its own record
describes it; no label below is an assessment made here.
- **[M]** on `main`, manuscript or kernel text; its support layer is as the source states it.
- **[M-r]** on `main`, a research record (WIP, unverified, or reviewed as its own status line says).
- **[NP]** named premise: on `main`, verification only reported or relayed, so usable only as a named
  premise (designation taken from S3-PLAN-r9 §§8.2, 8.4 and S3-U1-r5 §9, or from the record itself).
- **[OFF]** off `main` (branch, PR, Issue comment); provenance unless later landed.
- **[EXT]** external literature; to verify first-hand. Where the corpus already cites it, the corpus
  location and its recorded read status are given.

***

## 1. Measurement and record formation

### 1.1 MR-1 (`verification/programmes/oi-qm/reconstruction/measurement-record-formation/`)

| # | Location | Label | Content |
|---|---|---|---|
| 1.1 | `README.md`:1–63 | [M-r] | Standing note: preregistration frozen at `1a236f33` (#1023 c.6549225579); GAP token provisional, "stands only if a controls-only stage 2 ... returns every reference result of §M.4–§M.8; otherwise it is `VOID`"; stage 2 never authorized; negative claims limited to sources read |
| 1.2 | `preregistration.md`:27–55 (§1) | [M-r] | Frozen question ("On one fixed interface ... which microscopic interaction forms a record while preserving, modifying or eliminating ... coherent recombination"); three levels representable / available / derived (:37 ff.) |
| 1.3 | `preregistration.md`:121–200 (§§3.1–3.4) | [M-r] | RFI tuple definition; record conditions R1–R4; resources, heat, reset; controls and inverses |
| 1.4 | `preregistration.md`:202–254 (§3.5) | [M-r] | Absorption / loss of interference / irreversibility kept separate; decoherence vs dephasing definitions; example table incl. reversible which-path marking (:216) and Zurek redundancy (:218); Proposition S (:224); complementarity benchmark `V = |⟨d_L|d_R⟩|`, `D² + V² = 1`, Englert 1996 inequality (:228–239); Catani et al. predictability–visibility witness `V + P ≤ 1` (:241–254) |
| 1.5 | `preregistration.md`:280–311 (§4.3) | [M-r] | Proposition A1 (records are functions of the complete state); A2 (non-functional records abandon P-bij, P-obs or P-set); B2 (rests on #912 theorem, not independently reviewed on `main`, per README) |
| 1.6 | `preregistration.md`:387–425 (§4.5) | [M-r] | AW-MR1–AW-MR7; AW-MR5 symplectic native step, Catani et al. toy theory reproduces Mach–Zehnder, which-way, eraser, delayed-choice, bomb-tester (:406–417); AW-MR6 complementarity match is not a witness (:418) |
| 1.7 | `preregistration.md`:471–477 (§5.4) | [M-r] | T0: coherence before marking, an obligation |
| 1.8 | `preregistration.md`:479–508 (§5.5) | [M-r] | Test battery: T3 undo (:485), T4 eraser with full unnormalized branch masses, "CC4 and CC5 reproduce erasers" (:490–491), T8 source deletion (:503), T9 inverse audit (:507) |
| 1.9 | `preregistration.md`:510–540 (§§5.6–5.7) | [M-r] | Setting independence decided as a property of `μ` (:512); witnesses W1 (:519), W2; list of non-witnesses incl. "an eraser fringe" (:539) |
| 1.10 | `preregistration.md`:542–575 (§5.8) | [M-r] | Control table CC1–CC8: CC1 classical hidden memory (:568), CC4 epistemically restricted field (:571), CC5 classical eraser (:572), CC6 supplied inaccessible inverse (:573), CC7 classical dephasing, no record (:574) |
| 1.11 | `preregistration.md`:586–654 (§6) | [M-r] | Outcome tokens (1.1 GAP; 2.2–2.8 incl. `CLASSICAL-REPRODUCED/<CC>`, `NONCLASSICAL`, `CONTEXTUAL`) and decision rule |
| 1.12 | `preregistration.md`:656–697 (§7) | [M-r] | Stage plan (stage 2 separate owner gate, controls first), authority limits, hard-to-vary clause |
| 1.13 | `preregistration.md`:739–770 (§9) | [M-r] | Literature table with per-item read status (used in §5 below) |
| 1.14 | `amendments/MR-star.md`:21–440 (K★) | [M-r] | K★ blocked then frozen; K1 tension (§K★.5); CC2 kept at class level |
| 1.15 | `amendments/MR-star.md`:462–484 (§S.1) | [M-r] | What K1 fixes |
| 1.16 | `amendments/MR-star.md`:491–495 S-L1 | [M-r] | Superposition `pr_Y φ^t(s) = Σ_X Φ^t_{YX}(s_X)` |
| 1.17 | `amendments/MR-star.md`:498–510 S-C1 | [NP] | No conditional dynamics; (a) no selection of operations (designated named premise in S3-U1-r5 §9) |
| 1.18 | `amendments/MR-star.md`:511–515 S-L2 | [M-r] | Available operations are time shifts `φ^n` within the budget; observer-side choices change only region and tick read |
| 1.19 | `amendments/MR-star.md`:517–527 S-L3 | [NP] | Time reversal representable, not available; "No region executes `σ` on another"; inverse only as global wait `φ^{N−1}`. Under independent verification by #1169 c.6891189024 item 4 |
| 1.20 | `amendments/MR-star.md`:529–562 S-L4 | [NP] | No confinement (named premise per `observer-interface-obsmu-20261104/ANALYSIS.md`:485–489) |
| 1.21 | `amendments/MR-star.md`:564–582 S-C4a, S-C4b | [M-r] | No confined pointer; conserved linear quantities global (S-C4a withdrawn as GAP ground by C-2) |
| 1.22 | `amendments/MR-star.md`:584–593 S-L5 | [NP] | Marking and interference loss decoupled; marker affects later tests only through `Φ_{DA} s_A`; wording amended by C-9 (:1433–1440) |
| 1.23 | `amendments/MR-star.md`:595–601 S-L6 | [M-r] | Budget below recurrence: `φ^N = id`; a ready observer carries no information about the cell at `t_0 + N` |
| 1.24 | `amendments/MR-star.md`:603–618 S-L7 | [M-r] | Epistemic-restriction sub-question: single-time current-slice access is isotropic; two-slice access is not; which slices are read "is not fixed by the sources" (cites SM:252, drift noted in S3-PLAN-r9 §3) |
| 1.25 | `amendments/MR-star.md`:620–682 (§S.3) | [M-r] | Sources σ1–σ13 screened; μ leg: counting measure gives no ready region (:642); σ6 global recurrence (:661); σ12 non-additive rules not screened (:667, :670–682) |
| 1.26 | `amendments/MR-star.md`:683–750 (§§S.4–S.5) | [M-r] | Maximum-skepticism pass; selection rule selects none → GAP |
| 1.27 | `amendments/MR-star.md`:751–806 (§S.6) | [M-r] | Gem-finding nodes; AW-MR8–AW-MR12; AW-MR11 budgets below recurrence (:797–799) |
| 1.28 | `amendments/MR-star.md`:844–883 (§§M.1–M.2) | [M-r] | GAP token, scope (`K★ = {K1}`, σ1–σ13, budget below recurrence), "not a no-go" (:863), standing (:876–878) |
| 1.29 | `amendments/MR-star.md`:1018–1074 (§M.6) | [NP] | Countercontrol instances: CC1 (:1064), CC3 (:1065), **CC4** (:1066), **CC5** classical eraser (:1067), CC6 (:1068), **CC7** dephasing without record (:1069), CC8 (:1070), CC2 (:1071). CC4, CC5, CC7 are named premises; under verification by #1169 c.6891189024 item 4 |
| 1.30 | `amendments/MR-star.md`:1076–1294 (§§M.7–M.14) | [M-r] | Frozen stage-2 test menu, T7 inequality, T8/T9, mutations, results schema, invariants |
| 1.31 | `amendments/MR-star.md`:1295–1300 | [M-r] | Review record: independent review of `fc68d333` REVISE; "verified S-L1, S-L3, S-L4 (case analysis), S-L6, S-L7, B-T0 to B-T7, Lemma G and the countercontrol checks" |
| 1.32 | `amendments/MR-star.md`:1320–1340 C-2 | [M-r] | Localized records: impossibility withdrawn; K1 free-field wake counterexample on `ℤ` (site 0 carries `δ` at every even tick) |
| 1.33 | `amendments/MR-star.md`:1342–1371 C-3 | [M-r] | R gap reframed; named element "absence of a physically sourced quiet, ready region" (:1344); "A wake does not yet establish a stable, distinguishable, reusable record" (:1361) |
| 1.34 | `amendments/MR-star.md`:1373–1380 C-4 | [M-r] | Trace route UNDECIDED; deciding it is a calculation, not run, not authorized |
| 1.35 | `amendments/MR-star.md`:1401–1412 C-6 | [M-r] | AW-MR8 scoped: K1 step additive, no conditional dynamics; records through wakes undecided |
| 1.36 | `amendments/MR-star.md`:1491–1505 C-14; :1521–1553 C.1 | [M-r] | Result after corrections (GAP, class G, scope); C.1-3 "The wake is retained information, not yet a record" (:1543–1546) |
| 1.37 | `amendments/stage1-log.json`:745, :773 | [M-r] | GAP standing; review "relayed by the coordinator" |
| 1.38 | `amendments/KS-substitution.md`, `amendments/D3-CC2-class-level.md` | [M-r] | Kochen–Specker reading substitution; CC2 class-level decision |
| 1.39 | `LA-EQUAL-REVIEW.md`:1–564 | [M-r] | Consolidated model-authored reviews of LA-EQUAL; full equality not established (README) |

### 1.2 MR★ and MR-1 governance on GitHub

| # | Location | Label | Content |
|---|---|---|---|
| 1.40 | PR #1023 (closed, not merged; branch `research/measurement-record-formation-20261031` kept at `af1e9be2`) | [OFF] | MR-1 preregistration and stage-1 PR; records landed on `main` separately (#866 c.6631480154) |
| 1.41 | #1023 c.6549225579 | [OFF] | Owner freeze designation of the preregistration at `1a236f33` |
| 1.42 | #1023 c.6549252522 | [OFF] | Owner authorization of stage 1, literature-first, paper-only |
| 1.43 | #1023 c.6555028014 | [OFF] | Independent review of `fc68d333` REVISE; one correction round authorized |
| 1.44 | #1023 c.6555169983 | [OFF] | Stage-1 result: scoped GAP (1.1, class G), confirmed at `af1e9be2`; source of the K1 summary quotes and the caveats "This is not a no-go ..." and "the absence of a proved ready supply is an open sourcing problem ..." |
| 1.45 | #1023 c.6631485315 | [OFF] | Retired without merging; branch kept |
| 1.46 | #866 c.6548283392 | [OFF] | Owner authorization of the measurement/record-formation study: coherence before which-path marking is the obligation; repeat/undo/composition/eraser; "not single-shot fringes"; countercontrol list incl. "eraser-style postselection with full unnormalized branch masses" (body line 11) |
| 1.47 | #866 c.6631480154 | [OFF] | MR-1 handoff to #866 row O-REC; stage-1 evidence on `main` |

### 1.3 O-OBSMU (`verification/programmes/oi-qm/reconstruction/observer-interface-obsmu-20261104/`)

| # | Location | Label | Content |
|---|---|---|---|
| 1.48 | `README.md`:1–20 | [M-r] | "WIP / UNVERIFIED research record"; no established physical premise |
| 1.49 | `ANALYSIS.md`:75–124 (§§1–2) | [M-r] | Obligation by consumer; L5 readiness and records (:100); capacity (4) readable, persistent records cites MR-1 GAP (:124) |
| 1.50 | `ANALYSIS.md`:466–522 (§3.6 Node D) | [M-r] | K1 dynamical obstructions; :485–489 rules S-L4 a named premise because the review is only relayed |
| 1.51 | `ANALYSIS.md`:950–1010 (§4.6.2) | [M-r] | Laboratory preparations; record reliability vs reversibility (Loschmidt/Boltzmann point at :958–962; "general Loschmidt statement is not proved here", :1009) |
| 1.52 | `ANALYSIS.md`:1216–1259 (§7) | [M-r] | Off-`main` reference classification for the record |

### 1.4 PC-1 and related record-formation screens

| # | Location | Label | Content |
|---|---|---|---|
| 1.53 | `verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/README.md`:1–12 | [M-r] | Standing: "Strict result: `INCONCLUSIVE (void)`" for stage 1 and stage-2 run 1; run 2 in `stage2/run-2/RESULT.md` |
| 1.54 | #866 c.6627392555 | [OFF] | PC-1 closed; "scoped negative. None of the 25 screened rules qualifies; these are classical measurable bijections with function-valued records" (source of plan's M-8) |
| 1.55 | `verification/lean-mathlib/OIBridge/PC1Controls.lean`:132, :324 | [M] | Kernel controls `gauged_rot_mem_onesClass`, `falsifier_available_of_mem` (cited in MR-1 README) |
| 1.56 | `verification/programmes/oi-qm/reconstruction/native-interaction-source-2-20261110/` (`SOURCE-SCREEN.md`, `STATUS.md`) | [M-r] | NATIVE-INT-SRC-2 boundary write and one-tick retention; now on `main` (PR #1223 merged). S3-PLAN-r9 §2.1 lists it as "reviewed, not merged" |
| 1.57 | `verification/programmes/oi-qm/reconstruction/native-preparation-source-1-20261110/` (`PREPARATION-SCREEN.md`, `STATUS.md`) | [M-r] | NATIVE-PREP-SRC-1 quiescent-bank screen; now on `main` (PR #1225 merged, `b496290b`). Plan lists it as "reviewed, not merged" |
| 1.58 | PR #1278 (draft, head `7086bd30`), `verification/programmes/oi-qm/reconstruction/native-apparatus-source-20261113/ASSESSMENT.md`:12–18, :55–72 | [OFF] | Codex NATIVE-APPARATUS-SRC-1: preparation, selectable intervention, "complete held readout and failures", repeated-run resources classified derived / assumed / absent; physical source NOT PASSED |
| 1.59 | `verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md`:518–565; `STATUS.md` | [M-r] | OA-1 three gaps; Gap 1 resolved by MP-0a (resource) or MP-0b (H-MEM interface convention) (:537, :556–565); r5 is the accepted text per `STATUS.md` |

### 1.5 RO-1 drafts that U4 reads

| # | Location | Label | Content |
|---|---|---|---|
| 1.60 | S3-PLAN-r9 §§4.1, 8, 9 (PR #1294 at `bfad2731`, blob `46ebc72d`, `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-PLAN-r9.md`) | [OFF] | The U4 specification: four-way separation, Points 1–3, D-1 conditions (α)–(δ) and outcomes, controls M-1–M-8, SNR-1, closure (a′)–(e′), U4 row |
| 1.61 | S3-U1-r5 (PR #1294 head `3ec1e465`, blob `68983f86`), same directory, :570–573 | [OFF] | U1's parked-record clause: C-RET defines what would count; "A return by recurrence (S-L6) is global and lies beyond the budget, so it is not retention". Under review, not accepted |
| 1.62 | S3-U1-r5 :900, :906–911, :964–967 | [OFF] | AW-6 (C-RET readback form does not inherit R2-type negatives); standards comparison for the S-L3 re-check; "What U4 can use" list; S-L3, S-L5, S-C1, CC4, CC5, CC7 named premises |

***

## 2. Double-slit, which-path and eraser material in the corpus

### 2.1 Manuscripts

| # | Location | Label | Content |
|---|---|---|---|
| 2.1 | `papers/Main.md`:682 (§4.1) | [M] | Double slit as finite action-labelled family (both open, one closed, which-path record coupled); intervention dilation realizes it; "coupling a which-path record is an intervention that changes it"; "a derivation of the two-slit interference pattern from the substratum dynamics is open" |
| 2.2 | `papers/Main.md`:480–482 | [M] | Theorem (intervention dilation: finite classical action-labelled comb) and its response-table proof, used by :682 |
| 2.3 | `papers/Main.md`:652 | [M] | Projective measurement as conditioning on a visible outcome and re-marginalizing; Lüders rule for the represented diagonal sector only |
| 2.4 | `papers/Main.md`:680 | [M] | Experimental degrees of freedom (photons, slits, detectors) are visible-sector objects |
| 2.5 | `papers/Main.md`:326–328 | [M] | Lemma (diagonal preservation) for permutation-unitary channels; certified for `t = 1…6` in `c1_cp_scope_probes.py` |
| 2.6 | `papers/Main.md`:588 | [M] | Observer-level lift "derives neither a non-monomial admissible operator nor the layer flow ... unresolved rather than excluded" (later in the line; kernel `obs_not_layerFlowExecutable`) |
| 2.7 | `papers/Methodology.md`:401 | [M] | Measurement context as coupling-and-partition configuration; cites Main §4.1 double slit; contextuality as partition-dependence of emergent valuation |
| 2.8 | `papers/GR.md`:350 | [M] | Two kinds of coherence loss: "environmental decoherence, in which which-path records pass to unobserved degrees of freedom such as emitted radiation while the total evolution remains unitary", and an additional nonunitary effect; selection among completions (a)–(c) open |
| 2.9 | `book/ch07-gravity.md`:189 | [M] | Book mirror of GR:350 |
| 2.10 | `papers/Substratum.md`:463 | [M] | Measurement problem: observer-relative account at fixed-basis level; double-slit interference derivation from dynamics open |
| 2.11 | `book/ch19-open-problems.md`:60 (§19.2.5), :333 | [M] | Measurement problem entry and status row |

### 2.2 SUBSTATE-1 (`verification/programmes/substratum/continuous-substates/`)

| # | Location | Label | Content |
|---|---|---|---|
| 2.12 | `observation-context-protocol.md`:1–11 | [M-r] | "preregistered research protocol and exact reference controls"; question (one continuous-state microdynamics, passive Markov records vs interference under interventions); eraser reveals conditional fringes without restoring the unsorted marginal; tracks #1007 and draft PR #1009 |
| 2.13 | `observation-context-protocol.md`:13–28 | [M-r] | Six-row coherent-reference table (both open, one-slit subnormalized, marker stored not read, marker read in path basis, marker read in complementary basis); stated as Born-rule benchmarks, "not predictions made by OI"; nonadditivity `(+1/2, −1/2)` not a uniqueness witness |
| 2.14 | `observation-context-protocol.md`:30–45 | [M-r] | Competing models C0 (fixed-path), C1 (classical coherent waves), C2, OI; decision rule |
| 2.15 | `observation-context-protocol.md`:47–53 | [M-r] | What would move the frontier: dynamical noncommuting interventions, composition with spectators, distinctive nonclassical witness |
| 2.16 | `observation-context-protocol.md`:61–105 | [M-r] | Sourcing audit (F2); native test gate: if a setting is "only a decoder applied afterward to inaccessible fields, return BLOCKED: no available intervention" |
| 2.17 | `observation_context_probe.py`:33–91 | [M-r] | Exact reference controls, incl. `eraser_joint`, unsorted screen uniform, conditioned opposite ports |
| 2.18 | `README.md`:245, :289 | [M-r] | Two-slit, one-slit, which-way and eraser reference controls; no which-path/complementary interventions established |
| 2.19 | `yangmills-substate-bridge.md`:99 | [M-r] | "Native observation sourcing verdict: BLOCKED for this retained interface"; the two same-preparation selectable path/eraser measurements not both implemented |
| 2.20 | PR #1009 (closed, not merged; branch `research/substate-1` at `77482a8c`) | [OFF] | SUBSTATE-1 working branch (kept per `README.md`:11) |
| 2.21 | #1007 (open) | [OFF] | SUBSTATE-1 accountable Issue |

### 2.3 Other which-path and eraser records on `main`

| # | Location | Label | Content |
|---|---|---|---|
| 2.22 | `verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`:1–12, :44–52 | [M-r] | Apparatus-1 (SA-1, proposes one changed premise, adopts none): "An eraser restores the conjugate value when the record has been neither registered nor copied; after a copy, the returned value is `x + w`" |
| 2.23 | same, :628–668 (§4.5) | [M-r] | "The state handed on, retained information and recombination": eraser and its loss after the which-way record is copied, "the classical counterparts of the eraser and of its loss" (:661–663) |
| 2.24 | same, :250 | [M-r] | Lead L7: native bidirectional receiver, "masking by a uniform background, recovery by later background access" |
| 2.25 | same, :292–296, :335–343 | [M-r] | SA-1(b) terminal registration; "The native dynamics does not enforce terminality ... an archive is irreversible only relative to a budget below recurrence" (cites S-L6) |
| 2.26 | `verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md`:985–995 | [M-r] | MECH-1: unregistered monitoring meters, if recombined, let dephasing be undone (AP1 §4.5 eraser) |
| 2.27 | `verification/programmes/oi-qm/reconstruction/minacc-1-20261108/DESIGN.md`:380–390; `RESULT.md`:1–8 | [M-r] | M-INACC-1: retained cells may couple again later; AP1 eraser-type recombination in the class; WIP / UNVERIFIED |
| 2.28 | `verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md`:11–14, :112–134 | [M-r] | Receiving interaction: uniform hidden background makes the immediate receiver law independent of the signal; "Later access to the background can restore the signal exactly"; recovery identity `S = R − K` if `R` retained (:132–134); draft #1173 review status |

***

## 3. Hidden-sector retention and return

### 3.1 Main and companion manuscripts

| # | Location | Label | Content |
|---|---|---|---|
| 3.1 | `papers/Main.md`:72 (C1), :74 (C2-structural and C2 timescale forms), :76 (C3), :78 (C4) | [M] | Conditions; C2-structural: record persists to readback; "reversibility supplies this retention for every law, Markov laws included"; coarse-grained channel can degrade record before readback |
| 3.2 | `papers/Main.md`:121, :135–143 | [M] | Recurrence step (`φ^N = id`); theorem history readback + finite recurrence ⇒ indivisibility; scope: global recurrence-cycle result only (:139) |
| 3.3 | `papers/Main.md`:145 | [M] | Routed readback: write, store, read clauses on rooted maps (two formalizations) |
| 3.4 | `papers/Main.md`:147 | [M] | Non-permutation `T` is a sufficient witness of C1; delayed-revival family hides influence at step one (`review4_probes.py`) |
| 3.5 | `papers/Main.md`:153 | [M] | Relation to prior work: information backflow witnesses divisibility failure [4, 5]; divisibility can fail without it; process tensor [7]; Bylicka et al. [9] for invertible maps only |
| 3.6 | `papers/Main.md`:157 | [M] | Readback gap gives conditional memory; "A sufficient further condition is a revival of distinguishability within the window" |
| 3.7 | `papers/Main.md`:159–169 | [M] | Storage under C2 (erosion `e^{−τ_S/τ_B}`); Lemma (fast bath erases readback); remarks on what it does not give |
| 3.8 | `papers/Main.md`:171–176 | [M] | Lemma (accessible conditional memory from readback), `I ≥ p_0 δ²/ln 2`; remark: (C1)–(C3) admit zero-memory realizations (tape and ledger "never meet") |
| 3.9 | `papers/Main.md`:178–180 | [M] | Roles of C2–C4; weak-coupling and fast-bath regimes (Jaynes–Cummings with Lorentzian density mentioned) |
| 3.10 | `papers/Main.md`:182–202 (§2.4) | [M] | Six-hidden-state model: hidden sector as memory register; record "I was at `x = 0`" written at step 1, read at step 2 (:200); process-tensor check (:198) |
| 3.11 | `papers/Main.md`:334–338 | [M] | P-indivisibility is not quantum non-Markovianity (:334); ancilla-assisted BLP witness (:336); three notions kept apart (:338) |
| 3.12 | `papers/Main.md`:439 | [M] | Delayed-revival family `X_1 = X_0`, `X_2` uniform, `X_3 = X_0`: permutation `T^{(1)}`, P-indivisible |
| 3.13 | `papers/Main.md`:445–451 | [M] | Hidden-sector dephasing between couplings; Poincaré recurrence at `t_R`; fast-bath regime looks thermalized "even though the underlying trajectory remains reversible and quasi-periodic"; mixing-class contrapositive |
| 3.14 | `papers/Main.md`:512–514 | [M] | Per-process capacity bound; "a two-hidden-state, three-visible-state bijection already exhibits full distinguishability revival"; revival counterexample certified by `c3_dilation_probes.py` |
| 3.15 | `papers/Main.md`:536–542 | [M] | Characterization theorem on accessible timescales `t ≪ t_R` |
| 3.16 | `papers/Main.md`:616–638 | [M] | C4 as diagnostic; proof via readback lemma (:628); consolidation: fixed finite realization has an exactly `L`-periodic multi-time law (:638) |
| 3.17 | `papers/Main.md`:797, :799, :801, :803, :805, :809, :917 | [M] | Refs [3] Breuer–Petruccione, [4]/[5] Rivas–Huelga–Plenio, [6] Pechukas, [7] Pollock et al., [9] Bylicka–Johansson–Acín, [63] Breuer–Laine–Piilo |
| 3.18 | `papers/SM.md`:1380, :1384 | [M] | C2 not established by energy conservation: "phase mixing within the Hamiltonian hidden sector can destroy the accessibility of the particular record written by `V` before readback"; record persistence an explicit hypothesis |
| 3.19 | `papers/Substratum.md`:44 | [M] | `(S, φ)` a finite lossless memory |
| 3.20 | `papers/Structure.md`:114, :118, :1140–1150, :1277 | [M] | C2/C4 restated; conditional-memory framing; Tomizuka–Takeda hidden-model decoherence with non-Markovian reduced dynamics (ref :1474) |
| 3.21 | `book/ch15-quantum-engineering.md`:103–105, :128–130, :142–158, :176–226 | [M] | Mechanism proposal (as labelled in source): coherence partially revives where an engineered bath's return revives distinguishability; capacity-controlled revival `F(r) = 2r − r²`; BEC analogue test |
| 3.22 | `book/ch18-beyond.md`:72–84 | [M] | Restricted quantum-statistical regime (mechanism proposal), revival measure `𝒩`; :78 notes partial revival is standard open-systems phenomenology (BLP, RHP) |
| 3.23 | `book/ch09-universality.md`:284–286; `book/ch13-quantum-biology.md`:80, :134–144; `book/appendix-a-prediction-status.md`:170 (row F1) | [M] | Partial distinguishability revival predictions (mechanism proposal) and prediction-status row |
| 3.24 | `book/appendix-b-derivations.md`:96 | [M] | CP-indivisibility witnessed by ancilla-assisted distinguishability; system-only trace-distance revival weaker |

### 3.2 Kernel modules and probes on `main`

| # | Location | Label | Content |
|---|---|---|---|
| 3.25 | `verification/lean-mathlib/OIBridge/RecurrenceHorizon.lean` (191 lines) | [M] | Recurrence-horizon route: identity return at `n` plus earlier overlap gives `C4r n` and P-indivisibility (`pIndivisible_of_identity_return_of_overlap`, :119) |
| 3.26 | `verification/lean-mathlib/OIBridge/RootedRecurrenceBridge.lean` (121) | [M] | Exact return of the rooted trajectory law under the actual common prior |
| 3.27 | `verification/lean-mathlib/OIBridge/CausalReadback.lean` (344) | [M] | C4 causal-readback audit: candidate forms `C4e`, `C4r` on rooted one-time marginals |
| 3.28 | `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean` (726) | [M] | `RoutedReadbackAtStorage`, the manuscripts' realization clause, storage-time reading |
| 3.29 | `verification/lean-mathlib/OIBridge/ReadbackRobustness.lean` (305) | [M] | Act 9 readback robustness on the map axis |
| 3.30 | `verification/lean-mathlib/OIBridge/ObservableFactorRecurrence.lean` (92); `ObservableMeasureReturn.lean` (115) | [M-r] | SUBSTATE-1 research modules: finite visible factor with arbitrary hidden carrier; measurable visible return ("research candidate"); census rows `verification/lean-manuscript-census.json`:1688–1704 mark them research-only |
| 3.31 | `papers/oi_lattice_code/foundations/c4_backflow_probes.py`:1–15 | [M] | Readback-lemma certification; Q2 "revival family"; Q3 coin control |
| 3.32 | `papers/oi_lattice_code/foundations/c3_dilation_probes.py`; `recurrence_entropy_probes.py` | [M] | Revival counterexample and doubly-stochastic obstruction (cited at Main:514); recurrence entropy probes |
| 3.33 | `verification/audits/physical-realization/c4-causal-readback/` (preregistration, amendments); `verification/programmes/oi-qm/track-i/recurrence-tightness/` (preregistration, result, amendment-1); `verification/programmes/oi-qm/track-b/act-09-readback-robustness/` (preregistration, result); `verification/audits/manuscript/recurrence-identifiability-recovery-20261028/README.md` | [M-r] | Control planes and results behind 3.25–3.29 |

### 3.3 O-RET (#1032) records on `main` (`verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103/`)

| # | Location | Label | Content |
|---|---|---|---|
| 3.34 | `README.md`:1–40 | [M-r] | Phase A PASS on 49 frozen tuples establishes implementation agreement only, "not physical retention in native OI dynamics"; Lemma S′, Lemma Q, `DEFINITIONS.md` not independently validated on `main`, not premises |
| 3.35 | `DEFINITIONS.md`; `ANNOTATION.md`; `DESIGN-PULSE.md`; `PREREG-PHASE-A.md`; `phaseA/run-1/RESULT.md`, `REVIEW.md` | [M-r] | O-RET definitions (`ε* = 1/20`), travelling-pulse design, Phase A preregistration and run-1 records |
| 3.36 | `phaseB-negative/THEOREM-N.md`:1–5, :383–415, :417–450; `phaseB-negative/REVIEW.md` | [M-r] | Theorem N, a scoped paper negative for family `𝔉` (K1 and SMR over `𝔽₂`, rings `N ∈ {5,7,8}`, declared registers), reviewed at exact head; §6.2 "Not a universal no-go theorem for OI retention" with its exclusions |
| 3.37 | `phase-b-o5-20261106/DESIGN.md` (PR #1177 merged as `924d421b`) | [M-r] | One O5 register-geometry screen, stopped at geometry/read-access source gap |
| 3.38 | `classical-retention-20261107/LEAD.md`:1–15 (PR #1186 merged as `f88c1842`) | [M-r] | External colloidal position-bit lead; native register, write and later read not supplied by OI sources; stopped |
| 3.39 | `SOURCES.md`:113 | [M-r] | O-RET source list incl. #866, #1007 |
| 3.40 | #1032 body | [OFF] | O-RET planning: physical retention and cross-read coherence open |
| 3.41 | #1032 c.6567189236 | [OFF] | Countercontrol: CNOT-like `T(c,m) = (c, m ⊕ c)` couples yet is unreadable under the uniform law; ready memory is a separate resource (`D_KL = log 2`); "unreviewed illustration" |
| 3.42 | #1032 c.6692541241; #1143 c.6692765618 | [OFF] | Owner rulings: cross-read coherence a separate #1032 obligation, "open pending a physically sourced coherent carrier and a read capable of preserving it"; two-read statistics can arise from classical memory (S8-A, #1143 c.6681999486) |

### 3.4 RO-3 recurrence inventory (off `main`)

| # | Location | Label | Content |
|---|---|---|---|
| 3.43 | PR #1303 (draft, head `78089e5e`), `verification/programmes/oi-qm/reconstruction/drafts/ro3-carrier-inventory-20261114/RO3-INVENTORY-r4.md`:144–213 | [OFF] | UNREVIEWED inventory: exact recurrence (§1.1), exact common visible return `Γ_L = I` (§1.2), recurrence-based P-indivisibility (§1.3), all-time classification (§1.4), A.8 cycle typicality (§1.5), per carrier class F / G / I |
| 3.44 | same, :259–380 (§2) | [OFF] | Per class: finite carrier established at recurrence-cycle scope only; `t_R` can exceed every accessible window (:272–273); infinite completions do not inherit exact recurrence |
| 3.45 | same directory, `OBL-RO3-2-r2.md` | [OFF] | Mixing of the prime-alphabet linear update on the infinite lattice; unreviewed r2 |

### 3.5 SUBSTATE-1 return and revival records on `main`

| # | Location | Label | Content |
|---|---|---|---|
| 3.46 | `verification/programmes/substratum/continuous-substates/cubic-wave-revival.md`:1–45 | [M-r] | "Research candidate": torus extension of the cubic wave update with a distributed finite readout; observable revival (`wF⁴ = w`) "without microscopic return"; no global finite-order recurrence; notes a retained transcript distinguishes the roots |
| 3.47 | same directory, `later-access-preregistration.md`; `later-access-result.md`:8–60 | [M-r] | Setting-conditioned later access: token `LA-EQUAL`, informativeness `EMPTY`, conditional on H-prior, H-inventory, H-access, H-rule, H-torus; LA-EQUAL proof standing in MR-1 `LA-EQUAL-REVIEW.md` and `la-equal-gap/` |
| 3.48 | same directory, `native-sign-echo.md`:1–8 | [M-r] | Masked two-tick sign echo on native ticks |
| 3.49 | same directory, `BOUNDARY-CONTROLS.md`; `infinite-xor-counterexample.md` | [M-r] | Finite boundary observations with infinite hidden stream; reversible infinite-tape XOR counterexample |

***

## 4. Renewal: same-seed reuse vs fresh cells

| # | Location | Label | Content |
|---|---|---|---|
| 4.1 | `0ecfddeb`:`verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md` (194 lines; branch `research/oiqm-sel-excl1-20261110`, PR #1228 draft, head `75681105`) | [OFF] | SEL-EXCL-1: reversible complete-record PR countercontrol. §1 (:28–58) one deterministic reversible global update, interface "specified, not derived" (:46); §2 single use, no-signalling, CHSH; §3 (:85–102) finite reuse, complete-history lemma with fresh cells; §4 locality gap; §7 (:159–194) same-source reuse stress test |
| 4.2 | #1143 c.6773265132, c.6777584931, c.6779013024 | [OFF] | Independent full review ACCEPT WITH NITS; focused review ACCEPT of `0ecfddeb`; handoff |
| 4.3 | #913 body, row O-REUSE | [OFF] | "Reusable instruments, composition and freshness"; Foundational; blocked: O-INS; not authorized; status-source cell names branch `2af1d5d5` (correction routed by #1169 c.6890079967 C7) |
| 4.4 | #913 c.6628909432 | [OFF] | #912 state handoff: `native-x-v2/` ("Reuse of the unchanged carrier leaves the decoder cone"), `composition_flag_v6/` ("Gates, storage, clock and isolation are supplied, not derived"), on branch `draft/oi-composition-access-20261024` at `2af1d5d5` |
| 4.5 | `verification/programmes/oi-qm/reconstruction/composition-access-20261024/REPORT.md`:57–69 | [M-r] | Fresh resources: "An independent initial seed bank supplies this condition only when earlier dynamics and access have not used it or conditioned on it"; review author-posted, no reviewer named (`SCOPE.md`, per MR-1 README) |
| 4.6 | `native-preparation-source-1-20261110/PREPARATION-SCREEN.md` (on `main`) | [M-r] | Supplied bank needs 13/15/17 extra hidden coordinates for L = 9/10/≥11, "not a universal physical cost or minimum" |
| 4.7 | S3-PLAN-r9 §4.1 (H-RR, RR-1–RR-3, support/refute/undetermined conditions); §8.3 Point 3 | [OFF] | H-RR as a hypothesis; U4 "reads the records' bearing on RR-1 to RR-3 for recording" |
| 4.8 | S3-PLAN-r9 §4 bullets citing SEL-DISC-1 P5 (l. 53) and §4 (l. 79) | [OFF] | "Scarcity alone is not a separator" (#1143 records, not read here at source) |
| 4.9 | #911 (reset-reuse audit), via #913 body | [OFF] | "exact fixed-vector reset-reuse audit finds a public-record error"; "supplied independent-pair renewal keeps continuous-resource costs explicit" |
| 4.10 | `apparatus-1-20261107/DESIGN.md`:664–668 | [M-r] | Spent ready cells recorded as consumed; reset or further supply is a #1147 resource |

***

## 5. External literature for the parked-record case (all [EXT], to verify first-hand)

Corpus citations and recorded read status are given where they exist. Bibliographic details not in
the corpus are from memory and are unconfirmed.

### 5.1 Complementarity and which-path information

| # | Reference | Corpus location / read status | Note |
|---|---|---|---|
| 5.1 | W. K. Wootters, W. H. Zurek, *Phys. Rev. D* 19, 473 (1979) | not cited (the one "Wootters" hit, `mechanism-1-20261107/DESIGN.md`:267, concerns discrete phase space at `q = 2`) | Quantitative complementarity in the double slit |
| 5.2 | D. M. Greenberger, A. Yasin, *Phys. Lett. A* 128, 391 (1988) | not cited | Predictability–visibility relation |
| 5.3 | B.-G. Englert, *Phys. Rev. Lett.* 77, 2154 (1996) | MR-1 `preregistration.md`:232, §9 table; abstract only | `D² + V² ≤ 1` |
| 5.4 | B.-G. Englert, J. A. Bergou, *Opt. Commun.* 179, 337 (2000) | not cited | Quantitative quantum erasure |
| 5.5 | S. Dürr, T. Nonn, G. Rempe, *Nature* 395, 33 (1998) | not cited | Which-way atom interferometer without momentum kicks |
| 5.6 | L. Catani, M. Leifer, G. Scala, D. Schmid, R. W. Spekkens, *Phys. Rev. A* 108, 022207 (2023); *Phys. Rev. Lett.* 129, 240401 (2022) | MR-1 §9; PRA read (text); PRL "not read; execution blocker" | Predictability–visibility, noncontextual bound `V + P ≤ 1` |

### 5.2 Quantum eraser and delayed choice

| # | Reference | Corpus location / read status | Note |
|---|---|---|---|
| 5.7 | M. O. Scully, K. Drühl, *Phys. Rev. A* 25, 2208 (1982) | MR-1 §9; abstract only | Original eraser proposal |
| 5.8 | M. O. Scully, B.-G. Englert, H. Walther, *Nature* 351, 111 (1991) | MR-1 `preregistration.md`:216, §9; abstract only | Which-path marking by cavity photons |
| 5.9 | P. G. Kwiat, A. M. Steinberg, R. Y. Chiao, *Phys. Rev. A* 45, 7729 (1992) | not cited | Two-photon eraser, "revival of coherence" |
| 5.10 | T. J. Herzog, P. G. Kwiat, H. Weinfurter, A. Zeilinger, *Phys. Rev. Lett.* 75, 3034 (1995) | not cited | Complementarity and the eraser |
| 5.11 | Y.-H. Kim, R. Yu, S. P. Kulik, Y. Shih, M. O. Scully, *Phys. Rev. Lett.* 84, 1 (2000) | not cited | Delayed-choice eraser |
| 5.12 | S. P. Walborn, M. O. Terra Cunha, S. Pádua, C. H. Monken, *Phys. Rev. A* 65, 033818 (2002) | not cited | Double-slit eraser |
| 5.13 | X.-S. Ma, J. Kofler, A. Zeilinger, *Rev. Mod. Phys.* 88, 015005 (2016) | not cited | Review of delayed-choice experiments |
| 5.14 | L. Catani, M. Leifer, D. Schmid, R. W. Spekkens, *Quantum* 7, 1119 (2023); R. W. Spekkens, *Phys. Rev. A* 75, 032110 (2007) | MR-1 §9; Quantum text read, Spekkens 2007 abstract | Classical toy theory reproducing which-way and eraser phenomenology (CC4) |

### 5.3 Decoherence, recoherence and revivals in finite environments

| # | Reference | Corpus location / read status | Note |
|---|---|---|---|
| 5.15 | W. H. Zurek, *Phys. Rev. D* 26, 1862 (1982) | not cited | Environment-induced superselection; finite spin environment with recurrences |
| 5.16 | W. H. Zurek, *Rev. Mod. Phys.* 75, 715 (2003) | MR-1 `preregistration.md`:218, §9; abstract only | Decoherence, einselection; redundancy |
| 5.17 | M. Schlosshauer, *Rev. Mod. Phys.* 76, 1267 (2005); *Decoherence and the Quantum-to-Classical Transition* (Springer, 2007) | not cited | Reviews incl. reversibility and recoherence |
| 5.18 | E. Joos, H. D. Zeh et al., *Decoherence and the Appearance of a Classical World in Quantum Theory*, 2nd ed. (Springer, 2003) | not cited | Monograph |
| 5.19 | F. M. Cucchietti, J. P. Paz, W. H. Zurek, *Phys. Rev. A* 72, 052113 (2005) | not cited | Decoherence from spin environments |
| 5.20 | N. V. Prokof'ev, P. C. E. Stamp, *Rep. Prog. Phys.* 63, 669 (2000) | not cited | Spin-bath theory |
| 5.21 | A. V. Khaetskii, D. Loss, L. Glazman, *Phys. Rev. Lett.* 88, 186802 (2002) | not cited | Central-spin decoherence by nuclear bath |
| 5.22 | J. H. Eberly, N. B. Narozhny, J. J. Sanchez-Mondragon, *Phys. Rev. Lett.* 44, 1323 (1980); G. Rempe, H. Walther, N. Klein, *Phys. Rev. Lett.* 58, 353 (1987) | not cited (Main:180 mentions Jaynes–Cummings in a different role) | Collapse and revival in the Jaynes–Cummings model, theory and observation |
| 5.23 | M. Brune et al., *Phys. Rev. Lett.* 77, 4887 (1996); J.-M. Raimond, M. Brune, S. Haroche, *Rev. Mod. Phys.* 73, 565 (2001) | not cited | Progressive decoherence of a cavity "meter" |
| 5.24 | E. L. Hahn, *Phys. Rev.* 80, 580 (1950) | not cited | Spin echo |
| 5.25 | A. Peres, *Phys. Rev. A* 30, 1610 (1984); R. A. Jalabert, H. M. Pastawski, *Phys. Rev. Lett.* 86, 2490 (2001); T. Gorin, T. Prosen, T. H. Seligman, M. Žnidarič, *Phys. Rep.* 435, 33 (2006) | Loschmidt named only as the reversibility point (`observer-interface-obsmu-20261104/ANALYSIS.md`:958–962) | Loschmidt echo and fidelity decay |
| 5.26 | P. Bocchieri, A. Loinger, *Phys. Rev.* 107, 337 (1957) | not cited (Main cites Poincaré recurrence without a reference) | Quantum recurrence theorem |
| 5.27 | M. Kac, *Bull. Amer. Math. Soc.* 53, 1002 (1947) | not cited | Mean recurrence time |

### 5.4 Information backflow and non-Markovianity

| # | Reference | Corpus location / read status | Note |
|---|---|---|---|
| 5.28 | H.-P. Breuer, E.-M. Laine, J. Piilo, *Phys. Rev. Lett.* 103, 210401 (2009) | `papers/Main.md`:917 [63]; used at :336 | Trace-distance backflow measure |
| 5.29 | Á. Rivas, S. F. Huelga, M. B. Plenio, *Phys. Rev. Lett.* 105, 050403 (2010); *Rep. Prog. Phys.* 77, 094001 (2014) | `papers/Main.md`:799, :801 [4], [5] | CP-divisibility and entanglement witness; review |
| 5.30 | B. Bylicka, M. Johansson, A. Acín, *Phys. Rev. Lett.* 118, 120501 (2017) | `papers/Main.md`:809 [9] | Backflow for invertible dynamics |
| 5.31 | F. A. Pollock et al., *Phys. Rev. Lett.* 120, 040405 (2018) | `papers/Main.md`:805 [7] | Operational Markov condition (process tensor) |
| 5.32 | P. Pechukas, *Phys. Rev. Lett.* 73, 1060 (1994) | `papers/Main.md`:803 [6] | Reduced dynamics need not be CP |
| 5.33 | H.-P. Breuer, E.-M. Laine, J. Piilo, B. Vacchini, *Rev. Mod. Phys.* 88, 021002 (2016); I. de Vega, D. Alonso, *Rev. Mod. Phys.* 89, 015001 (2017) | not cited | Non-Markovian dynamics reviews |
| 5.34 | B.-H. Liu et al., *Nature Physics* 7, 931 (2011) | not cited | Photonic control of the Markovian / non-Markovian transition |
| 5.35 | E.-M. Laine, J. Piilo, H.-P. Breuer, *EPL* 92, 60010 (2010) | not cited | Witness for initial system–environment correlations |
| 5.36 | C. Bäcker, K. Beyer, W. T. Strunz, *Phys. Rev. Lett.* 132, 060402 (2024) | `papers/Main.md`:847 [28] | Local disclosure of quantum memory in non-Markovian dynamics |
| 5.37 | R. Tomizuka, T. Takeda, arXiv:2604.06891 (2026) | `papers/Structure.md`:1277, :1474 | Hidden-model decoherence, non-Markovian classical–quantum dynamics |
| 5.38 | H.-P. Breuer, F. Petruccione, *The Theory of Open Quantum Systems* (OUP, 2002) | `papers/Main.md`:797 [3] | Textbook |

***

## 6. Gaps: topics U4 needs where the corpus has nothing located

Each item records an absence in the sources searched (`papers/`, `book/`, `verification/` at the base
commit; Issues and PRs listed above). It is not a claim that the framework is silent (§A.19).

| # | Topic | What was searched | Nearest corpus material |
|---|---|---|---|
| 6.1 | The parked-record hypothesis as such: a which-path record moved into the hidden sector and later re-accessible, and its bearing on interference | "parked" (7 hits, none on records), "which-path", "eraser", "retention", "later access" | 2.23–2.28 (eraser after copy, later background access, terminality relative to recurrence); 1.32–1.36 (wake); 3.10 (six-state memory register); 1.61 (U1 C-RET clause) |
| 6.2 | A corpus treatment distinguishing a parked-record return from quantum revivals in finite environments (Jaynes–Cummings, spin bath, echoes) | "recoheren" (0), "collapse and revival" (0), "Loschmidt" (3, none on revivals), "spin echo/Hahn" (4, unrelated kernel names), "spin bath/central spin" (book ch13/ch15 platform mentions only) | 3.6, 3.12–3.14 (distinguishability revival, delayed-revival family, full revival with `m < n`); 3.21–3.24 (book mechanism proposal); 3.46 (observable revival without microscopic return) |
| 6.3 | Any corpus derivation of fringe visibility as a function of time when a marker's record returns within the budget (between S-L5's offset form and S-L6's global recurrence) | MR★ §S.2, §S.3, C-2 to C-4; Theorem N §6.2 | 1.22, 1.23, 1.34 (trace route undecided, calculation not run) |
| 6.4 | Corpus citations for the eraser experiments Kwiat et al. 1992, Herzog et al. 1995, Kim et al. 2000, Walborn et al. 2002, and for Wootters–Zurek 1979, Greenberger–Yasin 1988 | names searched across corpus | none (5.1, 5.2, 5.9–5.12) |
| 6.5 | First-hand reads of the eraser and complementarity sources the corpus does cite | MR-1 §9 read status | Scully–Drühl, Scully–Englert–Walther, Englert 1996, Zurek 2003: abstracts only; Catani et al. 2022 PRL: not read |
| 6.6 | Recurrence-scale statements for an infinite or non-recurrent hidden sector in the record-return setting | RO-3 drafts (off `main`) | 3.43–3.45 (unreviewed); 3.46 |
| 6.7 | A sourced native marker preparation other than the noisy counting-measure marker (D-1 condition δ) | MR★ :642, C-3; NATIVE-PREP-SRC-1; OA-1 Gap 1 | 1.25, 1.33, 1.57, 1.59 |

**Citation checks made while locating sources** (recorded, not assessed):
- S3-PLAN-r9 §8.5 M-4 quotes "A single quantum-eraser fringe alone is not a success criterion" from
  #866 c.6548283392. That phrase was not found verbatim in that comment, the #866 body or the `main`
  tree; the comment's nearest text is "not single-shot fringes" and "eraser-style postselection with
  full unnormalized branch masses" (1.46).
- S3-PLAN-r9 §2.1 lists NATIVE-INT-SRC-2 and NATIVE-PREP-SRC-1 as "reviewed, not merged"; both PRs
  (#1223, #1225) are now merged and the records are on `main` (1.56, 1.57).
- M-8's source reads "scoped negative" (#866 c.6627392555); the PC-1 `README.md` on `main` reads
  "Strict result: `INCONCLUSIVE (void)`" (1.53, 1.54).
- The plan's line citations Main:326–328, :588 and :682 resolve to the same text at `75cc5100` as at
  the plan's base `dfeec843`.
