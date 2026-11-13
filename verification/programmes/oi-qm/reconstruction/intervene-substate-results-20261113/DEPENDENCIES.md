# Off-`main` references of the option-(c) carried results (§A.42 item 8)

Every reference that `NEW-RESULTS.md` makes to content not on `main` (`c3b5f37a`) is listed below
against the claim it is attached to, and classified by reading that claim:
- **provenance**: the claim does not use the referenced content;
- **support on `main`**: the content the claim uses is on `main` and supports it as it stands there;
  any difference from the cited version is stated;
- **support off `main` (gap)**: the claim uses content that is only off `main`.

Each gap states how it is closed or narrowed in the package. References to content on `main` that
the carried results use are listed at the end for completeness. Line conventions are those of
`NEW-RESULTS.md` (I:n, S:n, R3:n, RV:n; Main:n and OB/ at `c3b5f37a`).

## Off-`main` references

| Row | Reference | Claim it is attached to | Classification | Closure in the package |
|---|---|---|---|---|
| A1 | APPROX-UNIT1 r4a, C1–C3: #1221 (open, draft), `research/approx-unit1-r4a-1216-20261109` @ `e41cf6137be165add39c7e557e97d3dddf110239`, `verification/programmes/oi-qm/approximation/unit1/APPROX-UNIT1.md`:471–483 | §1, T5: (T5a) CM is an `Architecture`; (T5b) a square CM isometry is monomial; (T5d) the FI-1 witness | **support off `main` (gap).** (c)'s `op` case uses (T5b); the theory equality needs (T5a) for `genTheory CM` to exist; the headline uses (T5d). | **Narrowed.** T5(c) is stated conditional on (T5a), (T5b) and (T5d) as named hypotheses with their status (argued in two drafts off `main`, hand-checked in RV:47–62). The unconditional headline "FI-1 is not theory-invariant" is not asserted by the package; it becomes available when (T5a), (T5b), (T5d) land, through #1221 or another reviewed record. The same parts are also argued in I:159–168, :179 (row C), which the package does not carry by owner scope. |
| A2 | APPROX-UNIT1 r4a §4.2, NX-1 and its route split, same commit, `APPROX-UNIT1.md`:365–375; APPROX r2 on `ccr-9c2ecca4-vkb666` @ `820519cf011c…`, `handoff-20261109/1216-approx/` (the version INTERVENE r2 used, I:279) | §0.3 (E_f classical class), §3.1 G1 (its object), §3.2 E2's last sentence (route E_f) | **support off `main` (gap)** for the definition of the E_f classical class, as cited. | **Closed by self-contained statement.** §0.3 states NX-1 (copied from I:123) and the E_f classical class in full, with the spanning hypothesis, and §0.3 states T3 in full. No carried result uses any other part of APPROX's NX-1 definition or of the route split; APPROX r2/r4a are then provenance for the term. |
| B | BRIDGE-UNIT1 §5.1, FI-1: `ccr-9c2ecca4-vkb666` @ `820519cf`, `handoff-20261109/1211-bridge/BRIDGE-UNIT1.md`:401–416 | §0.2 (FI-1), §1 (T5 headline) | **support on `main`.** FI-1 as used (∃ K on S×Fin 1 with 𝓘 K ∧ ¬IsMonomial K, for the generating architecture 𝓘; I:121) is the conclusion of `exists_nonMonomial_of_layerFlowExecutable`, OB/ExecSource.lean:52 [K]; GR:266 names it "a non-monomial admissible operator at level one" [P]. Difference: BRIDGE §5.1 poses FI-1 for the substratum dynamics "with the visible/hidden trace-out and the observer's stated read/write access"; the package uses only the architecture-relative predicate, which is the kernel conclusion verbatim. | Closed. BRIDGE-UNIT1 is provenance. |
| C | INTERVENE-1 r2: #1230 (open, draft), `research/intervene-1-20261111` @ `ea12fde1bbc4b546f4690bf89817971796aeb501`, `INTERVENE-UNIT1.md` | §1 (T5 statement and (c) proof, copied); §0.1 (H3, H4, H6, H-IND, copied); §0.3 (T3, copied as context) | **provenance** for every copied item: the content each claim uses is in the package. T3's own proof uses the draft's T0/T1 (I:100–104, :129–131), which the package does not carry; no carried result uses T3's conclusion, only its hypothesis (G1). | No gap. T3 appears as context, not as a carried result; its substance on `main` is MECH-2 Lemma F(b) (the MECH-2 row of the `main` content table below). |
| D1 | SUBSTATE-BRIDGE-1 r2: #1232 (open, draft), `research/substate-bridge-1-20261111` @ `86a413c88cd14d344aa41b6f47885aeb24da6910`, `SUBSTATE-BRIDGE-UNIT1.md` | §2–§6 (statements and proofs copied) | **provenance**: the copied content is in the package. | No gap. |
| D2 | SUBSTATE-BRIDGE-1 r2, L3 (S:167–171), not carried | §5, N2's "why it is needed" (necessity of a directed write–read path for route A) | **support off `main` (gap)**: the necessity of N2 rests on L3, the common-cause argument for a factor no setting writes. The reconciliation reads L3 as the standard Bell argument and consistent with Q-868-H r3 (V) (R3:66), which is also off `main`. | **Narrowed.** The N2 cell states the requirement conditional on L3 (Δ20). N2 is an open requirement in any case; no carried result asserts it as proved. |
| D3 | SUBSTATE-BRIDGE-1 r2, L2 (S:153) and class (a)3 (S:263), not carried | §5, SLL exclusion branch: "would extend class (a)3 to all substates" | **support off `main` (gap)**: L2 rests on Bell-scope Theorem N (row E2) and on Bell's theorem for a measurable λ (row L). | **Narrowed.** The exclusion branch's consequence is stated conditional on L2 and Theorem N (Δ16). SLL is an open obligation; neither branch is asserted. |
| E1 | Bell-scope r2: #1231 (open, draft), `research/bell-scope-868-20261111` @ `e1534b08fa3f361e05416b3cc0c1dcd2f3b23918`, `BELL-SCOPE-UNIT1.md` §3.1, (Sep) | §0.4 ((Sep)), §5 (SLL "wings that satisfy (Sep)") | **support off `main` (gap)** for the definition as cited. | **Closed by self-contained statement**: §0.4 quotes (Sep) in full. Main's Corollary (Main:414) states the corresponding separation for its wings [P]. |
| E2 | Bell-scope r2, Theorem N (§3.2) and 𝒞_sep | §5, SLL exclusion consequence (through L2) | **support off `main` (gap).** | **Narrowed** with row D3 (conditional statement). The gap stays open until #1231 lands; this is the SLL context the Bell ladder (#868) works from. |
| E3 | Bell-scope r2, O1 (long edges) and O2 (the within-cone window) | §5, routes B and C | **support on `main`.** Main:412 states the preparation-indexed adjacency of option (a) with long edges; Main:414 states that such edges place the update outside (vii) and states the window Δt/√3 < d ≤ Δt/‖n̂‖₁ for wings spacelike with respect to c. Difference: at the drafts' pin the sentence "Wings separated by less than the graph cone … fall outside the Corollary" stood at Main:416; the explicit spacelike-at-c window clause entered with #1233 (RV:43–46). | Closed: routes B and C are anchored on Main:412 and Main:414 (Δ12); "Bell-scope O1/O2" remain as provenance labels. |
| E4 | Bell-scope r2, finding F1 (the scoping of ledger (x)) and O3 | §5, SLL's last sentence; the open routes listed in SLL | **support on `main`.** Main:724 at `c3b5f37a`: (x) binds the reference-class graph `G_φ^ref`; (xiv) is measurement independence. Difference: F1 recorded (x) as unscoped at `cac5d264` (Main:726 there). | Closed (Δ16). F1 is provenance. |
| F | PR #1233 at `7f80ee6e` as SUBSTATE cites it (S:323; merged to `main` by `553e790b`, committed 2026-11-11T14:09:35Z; the PR merge time recorded in RV:41 is 14:09:36Z), and its independent review, comment 6794566946 (blocker B1: under (vii), `G_φ^K = G_φ` for every non-empty K) | §4.2, L4 and its relation to `main` | **support on `main`** for the finite case: Main:362 at `c3b5f37a` defines `G_φ^K` and states the linear-update clause for finite `S_i` [P]. **Provenance** for L4 itself, which is proved from its own definition and does not use the review's argument or its exhaustive ring check (S:323). | Closed (Δ10, Δ11): the stale "off `main`" sentence of S:157 and the unscoped-(x) sentence of S:163 are replaced by Main:362 and Main:724. |
| G | Mixed-path unit under #868 (owner authorization #868 c.6794392080; #1235, `research/mixed-path-868-20261111`) | §5, route C "subject of the mixed-path unit under #868" | **provenance**: no claim uses that unit or a result of it (S:322); the reconciliation did not read it (R3:68). | No gap. |
| H | REC-1 r7: `research/rec-1-1169-20261113` @ `9f7d2612` (`REC-1-r7.md`; the branch head is `cd38655c` at this writing, three later commits, P0 r1 to r3 with their review and confirmation records) | §0.1 (Q1/Q2 vocabulary and the Q1 typing of the hypotheses); the comparisons to REC-1 rows 9, 18, 35, 40, 10–11, C12, H-xiv, OBL-SP in §3.1, §5, §6; the standing sentence (Q2-F, Q2-P) | **provenance.** The vocabulary is restated in §0.1 from `REC-1-r7.md`:94–104. The typing of H-IND as Q1-I/Q1-μ is the reconciliation's own reading (R3:43, :83), not a REC-1 row. The row comparisons are context; no carried result's support uses a REC-1 result. | No gap. The vocabulary was read at `9f7d2612`; `REC-1-r7.md` is unchanged from `9f7d2612` to the branch head. |
| I | Reconciliation records on #1271 (open, draft), `research/reconcile-1230-1232-20261113` @ `703ae20e57f9ffeb0eb458ec688883b3fc64a632`: `RECONCILE-r3.md`, `REVIEW-r1.md`, `CONFIRM-r2.md` | "What it adds" paragraphs; hand-check citations (RV:n); the corrections (`CHANGES.md`) | **provenance.** The reconciliation supplies the classification and the corrections; its hand checks are model-written and are not verification (§A.46 item 7). No carried result rests on them as support. | No gap. |
| J | ChatGPT reviews posted under the owner's account: 5857985732 (#1230 at `ea12fde1`, 2026-11-11T11:25:22Z, ACCEPT WITH DOCUMENTATION NITS); 5859960068 (#1232 at `86a413c8`, 2026-11-11T14:03:54Z, ACCEPT WITH NITS); 5892291246 (#1271 at `703ae20e`, 2026-11-13T14:00:42Z, ACCEPT WITH INTEGRATION NITS) | the scope label (§0.1), the ⊥ note (§2), the N1–N4 sentence (§5); `CHANGES.md` | **provenance.** Each nit applied is a wording change argued from the source text; no claim rests on a review. | No gap. |
| K | Owner decisions #1169 c.6854728636 and c.6855167580 | the carried set; SLL as an open obligation | **provenance** (authorization and scope, §A.45 rule 3). | No gap. |
| X | Generic exact checks of the drafts: `probes/generic_substate_checks.py` (blob `fa434cd4`, sha256 `d269224f72d3fc5499e658f943851e7707af893cda964b7cb6a8b4b1c37bbb99`) and `.out` (blob `3861f1b0`, sha256 `9845ed1e860788f7d0a2edf90416e9b5e19169e57c55bb842a5d68fe300644ee`) at `86a413c8`; INTERVENE `checks.py` X5 at `ea12fde1` | §3.1 [X S2], [X S2b], [X S2c]; §3.2 S3; §5 N4 [X S4]; §6 [X S7]; §3.1 copied mention of X5 | **provenance.** Each tag's content is hand-checked in the package (§3.1, §3.2, §5, §6) without running any script. X5 is mentioned as T3's control and is not used by G1; its value (−1/2 for the Hadamard) is also stated in APPROX r4a §4.2 (row A2). The probes encode no OI rule (S:5). | No gap if the hand checks are accepted at review. If a reviewer requires the scripts as support, the alternative closure is to land both probe files unchanged with the record; the package does not do this. |
| L | External inputs [L], not §A.42 item 8 references: (i) the kernel-measurability step of E1 ("monotone-class argument, standard"), through Dynkin's π–λ theorem; (ii) Spekkens 2008 and Ferrie–Emerson, the states-or-effects negativity trade-off; (iii) Bell's theorem for a measurable λ (§5's opening statement; inside L2) | (i) §2 E1 proof; (ii) §3.2 consequence; (iii) §5 opening statement and SLL exclusion consequence | (i) **support in the package**: the step is hand-checked in §2 from Dynkin's π–λ theorem, a standard theorem; (ii) **provenance**: E2 is self-contained; (iii) used by §5's opening statement for a measurable λ (on `main` for finite Ω, Main:366–381, :401–404) and inside the conditional of rows D3/E2. | (i) Closed by the hand check after the E1 proof (π–λ argument); Dynkin's π–λ theorem is standard [L]. (ii), (iii) none. |

## Content on `main` that the carried results use or cite

| Content | Where | Used by |
|---|---|---|
| `InstAvail`, `instAvail_mono`, `Architecture`, `realized_of_instAvail`, `genTheory`, `LabelInvariant` | OB/ImplementationLocality.lean:268–289, :305, :506–516, :530, :852, :364 | §1; §7 |
| `substratumClass`, `substratumClass_arch`, `substratumClass_labelInvariant` | OB/StructuralClosure.lean:180, :231, :275 | §1 |
| `substratumTheory` | OB/RouteB.lean:284 | §1 |
| `IsMonomial`, `preservesDiag_conj_of_monomial` | OB/SubstratumInterface.lean:75, :126 | §0.2, §7 |
| `PreservesDiag` | OB/DiagonalTheory.lean:68 | §0.2 |
| `ColMonomial`, `preservesDiag_conjChannel_of_colMonomial` | OB/SubstantiveCensus.lean:651, :654 | §0.2 |
| `exists_nonMonomial_of_layerFlowExecutable` (FI-1 anchor) | OB/ExecSource.lean:52; GR:266 | §0.2, §1 |
| `waveStep`, `project_waveStep` | OB/NativePadicReduction.lean:32, :56 | §4.1 |
| `nonnegClass_nonnegBounded` | OB/F2CoherenceControls.lean:173 | §2, §7 |
| F2-1 A★2 | `verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md`:38–45 | §2 |
| OA-1 configuration ceiling | `verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md`:408–422 | §7 |
| OA-2 Lemma 0 and N0 | `verification/programmes/oi-qm/reconstruction/oa-2-20261112/OA-2-REPORT-r4.md`:199–223 | §2, §7 |
| MECH-2 Lemma F, H-LIFT, Theorem NC | `verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md`:309–325, :485 | §0.1, §0.3, §3.2, §7 |
| Preparation-span diagnostic | `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/prepared-pair-source.md` §5 (:134) | §5, N3 |
| SUBSTATE-1 per-site continua | `verification/programmes/substratum/continuous-substates/README.md`:53–55 | §4.1 |
| RS/ANALYSIS.md:28–30, :169–175; RS/README.md:196–199 | `verification/programmes/substratum/recursive-substates/` | §3.1, §5 |
| Main | Main:42, :48, :58, :360, :362, :366–381, :401–404, :412, :414, :416, :423, :590, :718, :724 | throughout |
| H-Bell (i)–(iii) | `papers/Substratum.md`:131–133 | §5 |
| The state-dependent neighbour rule | `papers/SM.md`:112 | §4.2 |

The RS/, CS/, MECH-2 and `oi-qm-ext-1` files cited above are unchanged between the drafts' pin
`cac5d264` and `c3b5f37a` (`git diff --stat`); under OIBridge only `OIRealization.lean` changed,
which no carried result cites. OA-1 r5 and OA-2 r4 entered `main` after the drafts' pin (merge `c3b5f37a`, #1265);
the drafts do not cite them, and the package cites them as the reconciliation does (R3:41, R3:45). `papers/Main.md`,
`papers/SM.md` and `papers/Substratum.md` changed; their lines are cited at `c3b5f37a`.

## Gaps left open

1. **Row A1.** T5's unconditional headline waits on (T5a), (T5b), (T5d) landing (#1221 or another
   reviewed record). The package carries T5(c) conditionally.
2. **Rows D2, D3, E2.** N2's necessity (L3) and SLL's exclusion-branch consequence (L2, Theorem N)
   are carried conditionally; their unconditional forms wait on #1232's L2/L3 and #1231's Theorem N.

No reference other than those of gaps 1–2 is a gap.
