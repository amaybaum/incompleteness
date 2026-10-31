# Introductory paper: source map, owner decisions and risks (design stage)

Every claim the outline would carry is mapped to:
- its exact source file:line at `main` `687e885b1cfd24d6f17eee439101afc8acf07015`;
- its kernel declaration, if any;
- its verification layer and correctness status;
- its originality class (AUDIT r4) and that class's evidence basis.

A claim with no source is listed under UNTRACED and is not carried.

## Provenance and path keys

- **Repository paths** are read at `687e885b` from the worktree `S/paper/mainwt` (clean, HEAD
  `687e885b`).
  - `Main:` = `papers/Main.md`; `GR:` = `papers/GR.md`; `ch07:` = `book/ch07-gravity.md`.
  - `OIBridge/X.lean:N` = `verification/lean-mathlib/OIBridge/X.lean`, line N.
  - `BH01/F:N` = `verification/programmes/black-hole-information/bh01_access_v1/F`, line N;
    `BH02/F:N` likewise for `bh02_scramble_v1/`.
- **Line stability.** `git diff 52e2db40 687e885b` changes Main only at :522 and :610 (#932, one
  for one). It also touches GR:20, glossary:39, FULL, ch18:114 and the new
  `verification/audits/manuscript/f29-witness-quantifier/`. Every other line AUDIT r4 cites keeps
  its number and text.
- **AUDIT** = `verification/audits/manuscript/introductory-paper-20261025/novelty-v5/AUDIT.md`.
  - It is read on branch `draft/oi-introductory-paper-20261025` at `1e9c05c7`, which is **not on
    `main`**.
  - Its status (README.md:31–37 of that directory) is "work-in-progress evidence record".
  - r4 was re-checked: ACCEPT WITH NITS, applied (AUDIT:20–22).
  - It cites the two literature studies by sha256. Those files exist only in the session
    scratchpad (`S/introaudit/lit-correspondence/LITERATURE-v2.md`, sha256 `005cfe94…1c26`;
    `S/introaudit/lit-blackhole/LITERATURE-v2.md`, sha256 `c7475d09…ce0d`). Both hashes were
    re-verified here.
  - The source keys (B23, B25, B26, EG, BD, …) resolve through LC §1. The arXiv identifiers are
    listed at the end of this file.
- **Kernel** means what AUDIT §0.3 means (AUDIT:270–280): the declaration exists with the quoted
  statement, its proof contains no `sorry`, `admit` or `native_decide`, and its module declares no
  `axiom`.
  - Re-checked here at `687e885b` for Equivalence, EquivalenceChain, HiddenMemory, C3Necessity,
    RecurrenceHorizon, RootedClassification(AllTime), TrackBQfbBridge and PhysicalC4Discharge:
    zero hits.
  - No Lean build was run, and no axiom report was observed, in the audit or here.
- **Black-hole "reviewed"** means a separate-agent internal review that closes with ACCEPT:
  - BH-01: `BH01/review/README.md:5–11`; REVIEW BLOCK (wording) at `587d4196`; ACCEPT WITH NITS at
    `95458016`; ACCEPT at `df2ea6f5`, as the opening line of `RECHECK-df2ea6f5.md`.
  - BH-02/BH-04: `BH02/review/README.md:3–7`; ACCEPT WITH NITS at `1739f4e0` (REVIEW.md:1) and
    `91e2230a` (:188); ACCEPT at `1f1aec6f` (:252) and `ce7937d2` (:279).
  - The later commits `606c98d8` and `84aca6b0` are wording-only. Diffs from `df2ea6f5` and
    `ce7937d2` were checked: status lines, replay recipe and two citation phrasings.
  - Not external validation or owner adoption (`BH01/review/README.md:3`; PROGRAMME.md:3).
- **Layers.**
  - kernel;
  - exact computation: exact arithmetic, an exhaustive finite check, or a probe in exact
    arithmetic;
  - numerical: double precision, controlled;
  - prose proof;
  - literature;
  - definition.
- **Originality labels** follow AUDIT §0.4 (AUDIT:282–319): KNOWN, PARTLY KNOWN, REFRAMING,
  NOVEL-CANDIDATE, WITHDRAWN, or not classified. Each is shown with its evidence basis
  (FT / FT-r4 / REC / NR) and with the PROVISIONAL mark where AUDIT applies it.

## Claim register

### §1–§2 Hypothesis, setting, definitions

| ID | Claim | Source @687e885b | Kernel | Layer | Correctness | Originality (AUDIT r4) |
|---|---|---|---|---|---|---|
| §1-a | OI hypothesis; physical identification is a representation choice; theorems mathematical; no ontology falsifier established | Main:28, :62, :702, :704 | — | prose | statement of hypothesis | not classified ((e), interpretation; AUDIT:1409–1460). Positioning against 't Hooft 2016 and Spekkens 2007 pending (NR; AUDIT:1452–1460) |
| §1-b | The question posed by the reduction | Main:28 | — | prose | — | n/a |
| §1-c | Scope: exact at the finite observable-law level; operational completion separate | Main:22, :534, :622, :758 | — | prose | — | n/a |
| §1-d | Incompleteness ≠ uncertainty relations | Main:28, :572 | (Main:572 cites `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`, `finite_horizon_equivalence`) | prose | — | not classified |
| §2-a | Observation $(S,\varphi,V)$; finite visible space | Main:44, :48 | — | definition | — | n/a |
| §2-b | Bijective representative a reconstruction choice; total finiteness a posit | Main:56, :62, :708 (ii) | — | prose | — | n/a |
| §2-c | Prior is part of the realization datum; invariance does not select the measure | Main:60, :86 | `invariance_does_not_select` (CanonicalMeasure:242) | kernel (measure); definition | kernel | not classified ((e); AUDIT:1416–1423) |
| §2-d | Classes $S$, $D$, $Q_{\mathrm{fb}}$ | Main:98–99, :526–530 | `Stochastic` (Equivalence:147), `RevReal`/`RevRealizable` (:157/:182), `QfbReal`/`QfbRealizable` (:190/:216) | kernel definitions | — | n/a |
| §2-e | C1–C4 are diagnostics, not hypotheses | Main:72, :74, :76, :78, :80, :596 | — | definition / prose; enumeration `primitive_probes.py` | prose + exhaustive probe | n/a |

### §3 The correspondence

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §3-a | E1 $S\iff D\iff Q_{\mathrm{fb}}$ | Main:16–18, :526–532, :580(1) | `finite_horizon_equivalence` (Equivalence:462); compositions :466–468 | kernel | kernel, six directions | PARTLY KNOWN; packaging PROVISIONAL (comb-realization theorem NR) — C4, AUDIT:631–709 (FT: EG, B23/B25/B26, Calvo, Milz 2020, Strasberg 2019) |
| §3-b | S⇒D, clock + trajectory record, correlated initial law | Main:500, :532 | `S_imp_D` (Equivalence:422) | kernel | kernel | PARTLY KNOWN (EG Prop. 13, FT); "not located" PROVISIONAL (Bennett 1973, HMM realization NR) — C1, AUDIT:496–542 |
| §3-c | S⇒D with $\mu_H$ independent of $x_0$ | Main:496–500, :498 | none (Main:500: "not formalized") | prose proof + exact probes (`process_dilation_probes.py`; `review4_probes.py` P-G) | prose + probe | PARTLY KNOWN (EG Prop. 16, LPW Prop. 1.5, FT); packaging PROVISIONAL — C1′, AUDIT:544–570 |
| §3-d | D⇒$Q_{\mathrm{fb}}$, permutation unitary | Main:262–266, :532 | `D_imp_Qfb` (Equivalence:294); `permMatrix_mem_unitaryGroup` (EquivalenceChain:179); `isDiag_Phi` (:253) | kernel | kernel; `sdq_probes.py` 1,488 realizations | KNOWN (B25 v3 p.12; B23 §4.3; B26 §4; FT) — C2, AUDIT:572–595 |
| §3-e | $Q_{\mathrm{fb}}$⇒S | Main:532 | `Qfb_imp_S` (Equivalence:245) | kernel | kernel | REFRAMING (Strasberg–García Díaz Eq. (3), FT-r4) — C3, AUDIT:597–629 |
| §3-f | Universal, Markov included; bare form false | Main:98–99, :534, :592, :596–598 | — (follows from E1) | prose | proved via E1 | C4-old WITHDRAWN (AUDIT:697–702); remark not classified |
| §3-g | Born dictionary in the definition; exponent not selected | Main:20, :534 | — | prose + probe (check 6, `equivalence_recovery_probes.py`) | prose + probe | KNOWN, non-discriminating (B26 Thm 3.1, FT) — C2 sub-item, AUDIT:588–592 |
| §3-h | No exact all-time fixed realization of a nonperiodic law | Main:618 | — | prose proof | prose | not classified |

### §4 Memory

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §4-a | Pushforward identity, distinguishability floor, capacity floor | Main:582–590 | `unavoidable_hidden_predictive_memory` (HiddenMemory:185), `pushforward_identity` (:83), `distinguishability_floor` (:114), `capacity_floor` (:170) | kernel; exhaustive probe `memory_probes.py` (1,464 cases) | kernel for the joint law; time-$t$ reading not formalized (Main:588) | REFRAMING (DPI); attribution PROVISIONAL (DPI text NR; SC Thm 5 FT, different statement) — C10, AUDIT:1128–1153 |
| §4-b | Memory biconditional, prose, directions named | Main:99, :580(2), :592 | components above + `S_imp_D` | kernel components + prose | two links not formalized (time-$t$ reading; CMI vanishing criterion) | REFRAMING — C10-B, AUDIT:1155–1180 |
| §4-c | $\log_2 m \ge I^*$ | Main:484–494 | `c3_necessity` (C3Necessity:80), `card_hidden_ge_two_pow_Istar` (:117), `c3_necessity_and_capacity` (:130) | kernel | kernel | REFRAMING; PROVISIONAL — C11, AUDIT:1182–1189 |
| §4-d | Readback lemma | Main:167–170 | none | prose proof + exact probe (`c4_backflow_probes.py`) | prose + probe | REFRAMING; PROVISIONAL (Pinsker NR) — C9, AUDIT:1114–1126 |
| §4-e | (ii) ⟺ (iii), corrected (iii) | Main:516–522, :596, :608, :610; F29 record `verification/audits/manuscript/f29-witness-quantifier/result.md:6–30`, acceptance output :66–124 | none | prose proof (both directions; Main:608); finite acceptance test (exact rationals; Markov M and two memory processes, $K\le3$) | prose; test covers 3 processes | REFRAMING, near-definitional — C12, AUDIT:1191–1268 (its F29 candidate is now fixed by #932) |
| §4-f | C1–C3 without C4: zero backflow | Main:172 | — | exact probe (`review3_probes.py`) | probe | not classified |

### §5 Quantum-like behaviour

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §5-a | Stochasticity by marginalization | Main:90, :105 | — | definition | — | n/a |
| §5-b | Minimal model: $T(1,0)$, $T(2,0)=I$, $\Lambda(2,1)$ negative, memory witness | Main:178–196 | — | exact computation, in text | re-checked here by an exact scratch script (`S/paper/design/probe/examples.py`): $T(1,0)$ entries 2/3, 1/3; $T(2,0)=I$; $\Lambda=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$; $1$ against $1/3$. Not a repository artifact; the paper should cite Main:178–196 | not classified |
| §5-c | Non-permutation $T$ + recurrence ⇒ P-indivisible | Main:115–129 | `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148). Census `manuscript: []` (AUDIT:832–833) | kernel (rooted form) + prose (Main's matrix form) | kernel | KNOWN (RHP 2014 Thm 2.4 "only if", FT-r4; BD Prop. 1, FT; DO3 v3 Prop. 1 concurrent) — C8, AUDIT:821–913 |
| §5-d | Monotonicity necessary, not sufficient | Main:121 | — | exact probe (`translation_probes.py`) | probe | not classified |
| §5-e | Stochastic-inverse lemma; readback ⇒ indivisibility in the recurrence cycle | Main:133–141 | `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110); `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) | kernel (lemma; routed level); history-level step prose | lemma kernel; history-level step prose (F11, AUDIT:1558) | KNOWN (C7: BB Problem 23, B23 fn 5; FT — AUDIT:800–819); mechanism KNOWN (C8) |
| §5-f | XOR: memory, matrix family factors through $\Lambda=I$ | Main:141, :606 | — | exact probe (`review4_probes.py`); re-checked here (all two-time kernels $\tfrac12 J$; $I(X_0;X_2\mid X_1)=1$ bit; i.i.d. control 0) | probe | KNOWN (RHP 2014 Eq. (15), FT-r4); DO3 v3 App. A concurrent; first statement unverified — AUDIT:1464–1525 |
| §5-g | Population P-indivisibility ≠ quantum non-Markovianity outside the diagonal-preserving class | Main:322–330, :334 | — | prose proof + exact probe (`c1_cp_scope_probes.py`, $\mathbb Q(\sqrt2)$) | prose + probe | not classified |
| Alt: C8-R | Rooted families realizable by one finite permutation with shared prior = `PPer` | not stated in any manuscript (AUDIT:938–946); census note `verification/lean-manuscript-census.json:809`; `verification/programmes/oi-qm/track-i/arc-b-rooted-classification/result.md` (full-support separation :87–116) | `finiteRootedRealizable_iff_pper` (RootedClassificationAllTime:192); → `pper_of_finiteRootedRealizable` (RootedClassification:339); ← `pper_has_responseRealization` (RootedClassificationAllTime:162) | kernel (finite visible; zero-prior padding) | kernel; full-support separation is prose + probe only | NOVEL-CANDIDATE, novelty unverified; no priority sentence; sufficiency PARTLY KNOWN (EG Props. 16–18, FT); necessity folklore — AUDIT:915–1070 |
| Alt: LG | Invasive classical comb reproduces $K=3/2$ | Main:460–464 | — | prose construction + exact probes (`intervention_probes.py`, `lg_comb_probes.py`) | prose + probe | not classified |

### §6 Reproduced versus derived

| ID | Claim | Source | Kernel | Layer | Correctness | Originality |
|---|---|---|---|---|---|---|
| §6-a | Representation, not explanation | Main:616 | — | prose | — | not classified ((e)) |
| §6-b | Visible law does not select the relating evolution (carried clauses only) | Main:624 | `bridge_traj` (TrackBQfbBridge:276), `rooted_eq_iff_slice_eq` (:180), `realData_traj_stochastic` (:286), `padData_rooted` (OperationalSourcing:476) | kernel | kernel for the four named clauses; the rest UNTRACED-1 | not classified |
| §6-c | Three statuses | Main:624 (closing sentences) | — | prose | — | n/a |
| §6-d | E2 operational-completion characterization; independence of the five conditions; bare finite OI ⇏ QM | GR:216–226; Main:352, :542 | `exactAll_iff_physical_general` (GeneralCarrier:100): → `physical_of_exactAll` (PhysicalCharacterization:301), ← `exactAll_of_physical_general` (GeneralCarrier:93) via `krausSoundExt_of_validity_inert` (OperationalValidity:124), `compositeCompleteness` (AncillaClosure:373), `exactAll_of_levelOne` (LevelOneSeam:196); `five_way_minimality` (RankGapTheory:702); `oi_alone_not_qm` (GeneralCarrier:160); `realizesSealedOICore_of_control` (OIRealization:252); also `main_result` (:188), `oi_compatible_classification` (:168) | kernel | kernel (GR:218 names no external premise; isometry extension discharged, GR:218) | not classified (not examined by AUDIT r4) |
| §6-e | No fixed finite carrier reproduces a qubit | Main:538, :540, :580(3) | — | prose (factorization) + imported (HKLP [55]); SIC remark exact probe (`nogo_probes.py`) | prose + import | REFRAMING; PROVISIONAL (Hardy 2004 NR, [55] NR; GH, MO FT) — C14, AUDIT:1287–1301 |
| §6-f | ε-realization and gluing; not uniqueness | Main:544–562, :576–578, :580(4) | none (F7 open: "proved unconditionally" with no kernel anchor; AUDIT:1554) | prose proof + exact probes (`opglue_probes.py`) | prose + probe; not audited internally (AUDIT:1316) | not classified (C15, AUDIT:1303–1321) |
| Alt: OI⁺ | OI⁺ ⟺ exact finite endomorphic operational QM; principles independent | Main:564–568 | `carrier_general_oiPlus` (CarrierGeneralOIPlus:213): → `qm_of_oiPlus` (:191), ← `oiPlus_of_qm` (:198); `oiPlus_independence` (:230; also CompletedOI:506) | kernel | kernel | not classified |
| Alt: RW | Finite reversible read-write dynamics does not generate state mixing | Main:568 | `readWriteSourced_not_qm` (ReadWriteControl:174), `substratum_plus_control_qm` (StructuralClosure:414) | kernel | kernel | not classified |

### §7 Black-hole application

| ID | Claim | Source | Layer | Correctness | Originality |
|---|---|---|---|---|---|
| §7-a | Nested partition $V/B/D$ | ch07:120–122; GR:719 | definition | — | n/a |
| §7-b | Bijectivity conserves global information | ch07:118 (first sentence); BH01/MANUSCRIPT-AUDIT.md:91 ("supports") | definition-level | — | n/a |
| §7-c | Bijectivity neither implies nor is necessary for accessible recovery; zero advantage needs $\lvert K\rvert\ge\lvert M\rvert$ | BH01/REPORT.md:17–18, :35–47 | exhaustive exact enumeration (all 40,320 bijections of $\{0,1\}^3$ in two layouts; maps of $\{0,1\}^2$) + written proof | reviewed ACCEPT (`df2ea6f5`); review: computations reproduce exactly (BH01/review/REVIEW.md:3) | not classified (C16-S, AUDIT:1395–1402; no literature map). The report classes it CONFIRMING (REPORT:251) |
| §7-d | Complete endpoint access ⇒ exact recovery; $P_{\mathrm{succ}}\ge1/\lvert K\rvert$; R1–R4 sufficient, not necessary | BH01/REPORT.md:20–21, :49–58, :66–86, :98–112 | written proof + exhaustive check | reviewed (F1 of the first review corrected the necessary/sufficient wording; RECHECK, opening line of `RECHECK-95458016.md`) | known in kind: "remnant-capacity form of a known fact" (REPORT:110–112); C4 there is "the linear secret-sharing threshold" (:131–132). Not literature-mapped |
| §7-e | Nested trace-out consistency is a Fubini identity, no recovery content | BH01/REPORT.md:29, :139–142; GR:731; ch07:124 | written proof + exhaustive check | reviewed | not classified |
| §7-f | GR A.7 decoupling support reversed (≥ $10^{57}$ at 30 $M_\odot$); scope of what it shows | BH01/REPORT.md:30, :211–245; BH01/review/REVIEW.md:3; GR:811, :813 | exact interval arithmetic (rational bounds; control K7) | reviewed, independently recomputed (REPORT:233–235) | audit observation (REPORT:257) |
| §7-g | Permutations on configuration states: no entanglement; $S(R)\le H(p_0)$; conserved overlap | BH02/REPORT.md:14–15, :26–42 | one-line proofs + exhaustive exact sweeps | reviewed ACCEPT (`ce7937d2`); review: "C1, C2, C4 … are correct and correctly scoped" (BH02/review/REVIEW.md:5) | known in kind (elementary); not literature-mapped |
| §7-h | H-scramble fails for every bijection in GR's configuration setting; the Page value enters only through the posited Haar ensemble | BH02/REPORT.md:18–19, :77–102; GR:817, :833 | proof from §7-g; textual analysis | reviewed | not classified |
| §7-i | Page-time fraction and β-dependence; constant greybody factor cancels; β > 1 semiclassically | ch07:137–143; GR:859–865; BH02/REPORT.md:22, :118–134 | exact algebra + literature (Page 2013 read in full in BH-02, REPORT:191) | reviewed; KNOWN | KNOWN — C16a (Page 2013 Eq. (8), FT), C16b (Page 2005 Eqs. (5)–(10), FT), AUDIT:1327–1347 |
| §7-j | Open items | ch07:126, :147–151, :155–157; GR:805, :833; BH02/REPORT.md:21, :112–114; PROGRAMME.md:3 | — | open | C16c PARTLY KNOWN, PROVISIONAL, conditional on H-scramble (AUDIT:1348–1361); C16d WITHDRAWN (AUDIT:1362–1386) |
| Alt | Shell factorization (C6(c)) CONDITIONAL; supplied-superposition counterexample (C3, NUMERICAL) | BH02/REPORT.md:16, :20, :103–111 | exact + numerical | reviewed. The review notes that amendment A1 was informed by the outcome and decided the C6(c) verdict (BH02/review/REVIEW.md:15–19) | not classified |

### §8 Open problems

Sources as in `OUTLINE.md` §8:
- Main:22, :20, :99, :139, :360–377, :392–394, :433–451, :480, :500, :534, :542, :580(2), :594,
  :608, :618, :624, :702–704, :708, :720, :758;
- GR:226.

The Bell ceiling (Main:360–377) is a prose proof checked by probe (check 11,
`equivalence_recovery_probes.py`). Main:379 calls it Bell's theorem applied, so it is KNOWN in
kind, but AUDIT r4 does not classify it.

## UNTRACED (not carried)

1. **Main:624, two sub-claims:**
   - the single-time fibre-Gram classification ("two lifts are related by it exactly when … the
     fibre-Gram data agrees up to the anchored phases … every positive semidefinite, rank-bounded,
     identity-summing family with the prescribed diagonal is realized");
   - "an ancilla carried between steps … can separate two lifts … already in the two-step law
     (exact computation)".

   Main names no kernel identifier or artifact at the site. A `FibreGram` definition exists
   (`OIBridge/CrossTimeInvariants.lean:33, :106, :159`, "act 12"), but the theorem carrying the
   classification was not located in this pass. Trace it before any use.
2. **Main:352, "kernel-verified with no external premise", at Main's site.** Main names no
   identifier there. It is traced through GR:218 instead, and the paper should cite GR §3.3 and
   the identifiers in §6-d.
3. **C8-D, the rooted recurrence dichotomy.** Its source is novelty audit revision 4, §4 (cited in
   AUDIT:1072–1112), not a file on `main`. Its components trace (§5-c, §5-e). The combined
   statement does not, and its prose steps B3, B4 and A1 are not in the kernel.
4. **"Machine-checked"** as an attribute of the paper's results. It needs a Lean build and axiom
   report at the drafting commit. None was observed (AUDIT:277). The release gate's
   `Mathlib bridge` check would supply it. It was not inspected here.
5. **Any empirical test or prediction of OI.** No source supports one at the finite-law level
   (Main:702–704). It is not carried.
6. **The cosmological realization of C1–C4** (the horizon as the hidden sector, $\tau_S/\tau_B$,
   capacity). It is "nowhere consumed by a proof here" (Main:72), so it is out of scope.

## Owner decisions to prepare (not decided here)

### Decision 1: scope

The options are set out in `OUTLINE.md`, "Alternative scopes".

- **Recommended (≈ 14.25 pp).**
  - Established mathematics: E1 with its three constructions (§3); the memory floor and capacity
    (§4-a to §4-c); the readback lemma (§4-d); the recurrence indivisibility results (§5-c to §5-e)
    with the XOR and Hadamard scope limits; the representation, relating-evolution and
    operational-completion boundaries (§6-a to §6-e).
  - Reviewed black-hole findings: BH-01 A, C1, C2 and E with item F; BH-02 C1, C2, C6(a) and C6(b);
    BH-04 C7, with Page 2013 and 2005 (KNOWN).
  - Open: H-scramble, A.8 → A.9 (C6(d)), the generalized second law, islands, BH-03 and BH-05 to
    BH-07.
- **Alt-L (≈ 12.25 pp).** The same mathematics. The black-hole section is reduced to BH-01 A and C2
  plus the conditional Page time and H-scramble's role. ε-gluing and Bell are omitted.
- **Alt-X (≈ 15.0 pp).** Adds:
  - C8-R as new manuscript content, a candidate with no priority sentence. Before any "not located"
    clause, P1.1 and P1.2 must be read in primary text and BD's forward citations checked
    (AUDIT:2018–2029);
  - OI⁺ (E4) and `readWriteSourced_not_qm`;
  - the Leggett–Garg comb.
- **Questions within decision 1:**
  - (a) whether §7-f (item F) may appear while GR:811 still states the decoupling unconditioned
    (R11);
  - (b) whether §5-c should cite the rooted kernel theorem, which has census `manuscript: []` and
    so needs a census registry update in the same commit (§A.35);
  - (c) whether the minimal model of Main §2.4 or the XOR family serves as the paper's single
    worked example, if pages force a choice.

### Decision 2: the Explainer

The outline needs nothing from it.
- AUDIT:129–130 states that the Explainer is superseded and is not a drafting source.
  `papers/Explainer.md:3` carries the "supplementary historical exposition" status line.
- The outline draws no content from it. Appendix A, the claim and kernel map, would be rebuilt from
  Main's status ledger (Main:710–722), not from the Explainer's summary tables.
- If the paper is meant to replace the Explainer, the retirement is a separate change. Its
  dependents, counted at `687e885b` with `git grep -c Explainer`, are:
  - `verification/lean/edge_rigidity_probe.py`, 58 references, run in CI
    (`.github/workflows/verify.yml:257`);
  - `verification/lean-manuscript-census.json`, 15;
  - `verification/coverage/LEDGER.json`, 9;
  - one each in `papers/Main.md` (:66), `README.md`, `book/README.md`, `.zenodo.json` and
    `LICENSE`.

  These agree in kind with the unreviewed EXPLAINER-AUDIT §5, which is not relied on beyond these
  counts.
- The planned filename `papers/Introduction.md` (audit README.md:112) would be picked up by every
  `papers/*.md` glob: `build.sh`, the voice, staleness, census and citation checks.

## Risks: claims that could read stronger than their evidence

| # | Risk | Safe form | Basis |
|---|---|---|---|
| R1 | The title "From Deterministic Dynamics to Quantum Observations" reads as a derivation | a neutral title (OUTLINE) | F4 open on Main:2 (AUDIT:1551) |
| R2 | "Born rule derived" | the Born form is part of the definition of $Q_{\mathrm{fb}}$, and the exponent is not selected | Main:534; AUDIT:588–592 |
| R3 | E1 read as a characterization of non-Markovianity or of QM | universal representation; Markov included | Main:596–598; AUDIT:460–464, :697–702 |
| R4 | (ii) ⟺ (iii) displayed or presented as a characterization theorem | prose only, with its reduction; §A.34 bars the display (no kernel witness either way) | Main:608; AUDIT:1264–1267 |
| R5 | The memory biconditional displayed as proved | prose, directions named, two unformalized links stated | Main:99, :580(2) |
| R6 | "Machine-checked" beyond the kernel declarations, or without a build | list the declarations; list the unformalized steps; attach a build | AUDIT:2040–2045, :277 |
| R7 | C8-R priority, or "we have not located" beyond the scope read | no priority sentence; in Alt-X, only the restricted "not located" form | AUDIT:1032–1070, :2018–2029 |
| R8 | (C4) said to force P-indivisibility on accessible windows; P-indivisibility equated with quantum non-Markovianity | global recurrence-cycle form only; XOR and Hadamard limits | Main:141, :330, :334 |
| R9 | The history-level (C4) ⇒ rooted non-permutation step presented as kernel | marked prose (F11) | AUDIT:1558; Main:139 |
| R10 | Black-hole computations presented as black-hole physics, or their reviews as validation | "finite toy access model"; "separate-agent internal review" | BH01/REPORT.md:285–302; BH01/review/README.md:3 |
| R11 | **Corpus tension (§A.25).** The paper would state, from reviewed records, that bijectivity does not deliver accessible recovery (claim A) and that A.7's decoupling support is reversed (item F). Live sites still carry the stronger wording: ch07:110 "resolves the paradox … because $\varphi$ is bijective"; ch07:159–161; GR:811 "D is frozen on evaporation timescales". The packages propose wording but authorize no manuscript change (BH01/MANUSCRIPT-AUDIT.md:3–11; PROGRAMME.md:3, :56) | owner choice: correct those sites first, or keep §7 to statements that do not contradict them (Alt-L) | BH01/MANUSCRIPT-AUDIT.md:56–60, :143–160; BH01/REPORT.md:237–245 |
| R12 | 0.646 presented as the Page time; "derivation of the Page curve" | conditional on β = 1 and on H-scramble | ch07:143; BH02/REPORT.md:22, :96–102 |
| R13 | The ≤ n³ bound, the Main:210 contrast or Main:504's definition carried over | omit (F13 unresolved) | AUDIT:1872–1918 |
| R14 | Main's sentences on Calvo, Pimenta and Doukas, its Born-equilibrium sentence, or the stale [24] imported | rewrite from the full-text studies | F14–F19, AUDIT:1561–1566 |
| R15 | ε-gluing relied on ("proved unconditionally") | cited, not used | F7 open, AUDIT:1554 |
| R16 | C14's attribution | cite Hardy 2004 and [55] only after reading them | AUDIT:1292–1301 |
| R17 | **Provenance (§A.42).** The originality classes rest on AUDIT r4, which sits on a branch not on `main`, and on two literature studies held only in the session scratchpad | land or retain the audit and the studies on `main` before the paper cites their conclusions | AUDIT:134–145; audit README.md:31–37 |
| R18 | The OI hypothesis read as supported by the theorems | "the theorems are mathematical; the physical identification is a representation choice; no ontology-level falsifier is established" | Main:62, :704 |
| R19 | Self-assessment or meta-commentary in the paper (§A.32/§A.33; `tools/voice_check.py` scans `papers/*.md`) | state content and status only | AGENTS.md §A.32–§A.33 |
| R20 | BH-02 C6(c) cited as a firm result | omit, or cite with the A1 disclosure | BH02/review/REVIEW.md:15–19 |

## Literature keys (from the LC §1 retrieval table, sha256-pinned there)

| Key | Source |
|---|---|
| B23 | arXiv:2309.03085v2 |
| B25 | arXiv:2302.10778v3 |
| B26 | arXiv:2608.04354v1 |
| EG | arXiv:2602.23491v1 (Egri et al.) |
| BD | arXiv:1408.7062v3 (Buscemi–Datta) |
| DO3 | arXiv:2602.22095v3 |
| PI | arXiv:2505.08785v1 |
| CA2 | arXiv:2601.18720v2 (Calvo) |
| SCH | arXiv:2106.03513v1 |
| GO | arXiv:1309.6586v2 |
| HHO | arXiv:quant-ph/0212019v2 |
| GH | arXiv:quant-ph/0110166v3 |
| MO | arXiv:0711.4770v2 |
| SC | arXiv:cond-mat/9907176v2 |
| BB | arXiv:1209.3632v5 |
| BCN | arXiv:2405.05794v3 |
| BI | arXiv:2609.11402v1 |
| LPW | Levin–Peres–Wilmer, 2nd ed. |

The FT-r4 sources, with URLs and sha256, are in AUDIT §8 (AUDIT:2091–2111):
- RHP 2014, arXiv:1405.0303v2;
- RHP 2010, arXiv:0911.4270v2;
- BJA, arXiv:1603.04288v2;
- BLP 2009, arXiv:0908.0238v2;
- Milz et al. 2019, arXiv:1901.05223v2;
- Milz et al. 2020, arXiv:1907.05807v3;
- Strasberg–García Díaz, arXiv:1905.03018v2;
- Capela et al., arXiv:1910.04236v1;
- JDM 1960.

Page 1993, 2005 and 2013, and Penington 2019, are taken from the black-hole study (BH §§2–4, sha256
`c7475d09…`); Page 2013 is arXiv:1301.4995v3 and Page 2005 is arXiv:hep-th/0409024v3
(BH02/review/README.md:7).
